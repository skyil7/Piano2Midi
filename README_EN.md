
# Piano 2 Midi  
>한국어 README.md 가 필요하신 분은, [여기](README.md)를 눌러주세요..  
## 🎵Introduction
Piano 2 Midi is a program to covert your Piano music to Musical Instrument Digital Interface!
  
When you give a piano performance recorded in WAV format, the program converts it to a file in MID format.
  
## 🎹How to use  
>Currently, There is no .exe file for this project.
  
1. Download the whole Project
2. Click [here](https://storage.googleapis.com/magentadata/models/onsets_frames_transcription/maestro_checkpoint.zip) to download pre-trained Data checkpoint, and unpack it in project directory
3. Use `pip` below to download tensorflow and magenta lib.
~~~  
 pip install --upgrade tensorflow
 pip install magenta  
~~~  
4. Run `Piano2Midi.py` and wait for a while. And input your .wav file name that you want to convert.
5. Wait again. When program complete the converting, it will print a message to notice you. 
  
## 🎼Magenta Library  
This program made with [Tensorflow Magenta](https://github.com/tensorflow/magenta)'s [onsets_frames_transcription](https://github.com/tensorflow/magenta/tree/master/magenta/models/onsets_frames_transcription) model.
  
And used [Maestro](https://magenta.tensorflow.org/datasets/maestro) Dataset. You can find out some more information about this dataset from [here](https://magenta.tensorflow.org/maestro-wave2midi2wave).
  
## License  
Magenta is under Apache License 2.0, and Maestro dataset is same.  
  
And you can use this projects code under Apache License 2.0, same as magenta!
  
## Update Plan  
### Midi 2 Piano  
Using Maestro Dataset, I will make midi to piano program next time.