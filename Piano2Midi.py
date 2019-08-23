import tensorflow as tf
import os

from magenta.protobuf import music_pb2
from magenta.music import sequences_lib, midi_io
from magenta.models.onsets_frames_transcription import configs, data, train_util, audio_label_data_utils, constants

# Trained Model Directory
MODEL_DIR = './train'

# Hyperparamter
config = configs.CONFIG_MAP['onsets_frames']
hparams = config.hparams
hparams.batch_size = 1
hparams.use_cudnn = False
hparams.audio_transform = False

example = tf.placeholder(tf.string, [None])

# Logging
tf.logging.info('model_dir=%s', MODEL_DIR)
tf.logging.info('checkpoint_path=%s', 'checkpoint')

# 배치 생성
dataset = data.provide_batch(examples=example, preprocess_examples=True,
    params=hparams, is_training=False, shuffle_examples=False,
    skip_n_initial_records=0)

# Estimator
estimator = train_util.create_estimator(config.model_fn, MODEL_DIR, hparams)

# 배치를 순환하는 이터레이터
iterator =dataset.make_initializable_iterator()
next_record = iterator.get_next()

sess = tf.Session()

#전역변수 및 로컬변수 초기화
sess.run([tf.initializers.global_variables(), tf.initializers.local_variables()])

#tensor로부터 사용하려는 데이터를 불러와 Dataset 인스턴스 생성
def input_fn(params):
    del params
    return tf.data.Dataset.from_tensors(sess.run(next_record))

def infer(filename):
    # WAV 파일 Binary로 읽기
    wav = open(filename,'rb')
    wav_data = wav.read()
    wav.close()

    tf.logging.info('User .WAV FIle %s length %s bytes', filename, len(wav_data))

    ## 전처리
    # 청크로 분할 후, Protocol Buffers 로 변환
    to_process = []
    examples = list(audio_label_data_utils.process_record(wav_data=wav_data, ns=music_pb2.NoteSequence(),
                                                          example_id=filename, min_length=0, max_length=-1, allow_empty_notesequence=True))

    # 분할된 버퍼를 시리얼라이즈
    to_process.append(examples[0].SerializeToString())

    #############################################################

    #시리얼라이즈한 버퍼를 iterator에 주입
    sess.run(iterator.initializer, {example:to_process})

    # Inference
    predictions = list(estimator.predict(input_fn, yield_single_examples=False))
    #가정 설정문으로 prediction size를 1로 보장
    assert len(predictions) == 1

    #예측 결과 불러오기
    frame_predictions = predictions[0]['frame_predictions'][0]
    onset_predictions = predictions[0]['onset_predictions'][0]  # 치는 순간
    velocity_values = predictions[0]['velocity_values'][0]      #강약

    #MIDI로 인코딩
    sequence_prediction = sequences_lib.pianoroll_to_note_sequence(
        frame_predictions,
        frames_per_second=data.hparams_frames_per_second(hparams),
        min_duration_ms=0,
        min_midi_pitch=constants.MIN_MIDI_PITCH,
        onset_predictions=onset_predictions,
        velocity_values=velocity_values)

    basename = os.path.split(os.path.splitext(filename)[0])[1] + '.mid'
    output_filename = os.path.join('', basename)

    midi_filename = (output_filename)
    midi_io.sequence_proto_to_midi_file(sequence_prediction, midi_filename)

    print('Program Ended, Your MIDI File is in', output_filename)

    sess.close()

if __name__ == '__main__':
    file = input('Input Your .WAV Filename:')
    infer(file)