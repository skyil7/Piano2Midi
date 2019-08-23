# Piano 2 Midi
>If you want English README.md, Click [here](README_EN.md).
## 🎵Introduction
Piano 2 Midi는 여러분의 피아노 연주를 듣고, 딥러닝을 통하여 이를 디지털 악보화 해주는 프로그램입니다!

WAV 형식으로 녹음된 피아노 연주를 입력하면, 프로그램이 이를 MID 형식의 파일로 변환하여 같은 디렉토리에 출력해줍니다.

## 🎹How to use
>현재 .exe 형태의 파일은 제공하지 않습니다.

1. 프로젝트를 다운로드합니다.
2. [여기](https://storage.googleapis.com/magentadata/models/onsets_frames_transcription/maestro_checkpoint.zip)를 클릭하여 미리 학습된 데이터셋 체크포인트를 다운로드하여, 프로젝트 폴더안에 압축을 풀어줍니다.
3. 아래 `pip` 명령어를 활용하여 필요한 라이브러리를 모두 설치합니다.
~~~
    pip install --upgrade tensorflow 
    pip install magenta
~~~
4. `Piano2Midi.py` 를 실행하고, 잠시 기다리다가 파일을 입력하라는 안내가 나오면 파일 이름을 입력합니다.
5. 잠시 기다리면, 프로그램이 프로젝트 경로에 (파일이름).mid 형식으로 파일을 출력하고 종료됩니다.

## 🎼Magenta Library
이 프로그램은 [Tensorflow Magenta](https://github.com/tensorflow/magenta)의 [onsets_frames_transcription](https://github.com/tensorflow/magenta/tree/master/magenta/models/onsets_frames_transcription) 모델을 활용하여 제작되었습니다.

데이터셋은 역시 Magenta의 [Maestro](https://magenta.tensorflow.org/datasets/maestro)를 사용하였고, 이에 관련된 자세한 포스트는 [여기](https://magenta.tensorflow.org/maestro-wave2midi2wave)에서 확인할 수 있습니다.

## 📜License
Magenta 라이브러리는 Apache License 2.0을 따르며, Maestro 데이터셋도 동일합니다.

또한 이 프로젝트도 Apache License 2.0을 적용하여 자유롭게 이용하실 수 있습니다.

## 📋Update Plan
### Midi 2 Piano
Maestro 데이터셋을 활용해서 이번엔 midi를 wav 음악으로 연주해주는 딥러닝 프로그램을 만들어 볼 것.