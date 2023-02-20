import wave
import numpy as np

def read_wav_file(filename):
    un_point = []
    with wave.open(filename, 'rb') as wav:
        n_channels = wav.getnchannels()
        sample_width = wav.getsampwidth()
        frame_rate = wav.getframerate()
        n_frames = wav.getnframes()

        data = wav.readframes(n_frames)
        audio_data = np.frombuffer(data, dtype=np.int8)

        # Reshape audio data based on number of channels
        audio_data = audio_data.reshape(-1, n_channels)

        #for i in range(len(audio_data)-1):
        #    un_point += [audio_data[i][0]]
        audio_data_norme = (audio_data / np.iinfo(np.int8).max)
        for i in range(len(audio_data)-1):
            print(audio_data_norme[len(audio_data_norme)-i-1][0])
        print(len(audio_data_norme))
        #print(audio_data / np.iinfo(np.int16).max)
        return audio_data

read_wav_file('C:/Users/arthu/OneDrive/Projet bop-it/Sons/Glassbreaker SFX/8KHZ 8bit/1point.wav')