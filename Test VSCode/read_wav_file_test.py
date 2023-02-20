import wave
import numpy as np

def read_wav_file(filename):
    liste=[]
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
        #print(np.iinfo(np.int8).max)
        #print(np.iinfo(np.int8).min)
        
        file = open('1point.txt', 'w')
        
        #x = (((audio_data[len(audio_data)-1-1][0])+128)*256)
        #print(x)
        #print(len(str(x)))
        #y = int(5-len(str(x)))
        #print("0"*y+str(x))
        #print(len(x))
        for i in range(len(audio_data)-1):
            #print((audio_data_norme[len(audio_data_norme)-i-1][0])
            #print(int((audio_data[len(audio_data)-i-1][0])+128)*256)
            x = (((audio_data[len(audio_data)-i-1][0])+128)*256)
            print(x)
            print(f"{len(str(x))} = len de x")
            y = int(5-len(str(x)))
            print("0"*y+str(x))
            file.writelines("0"*y+str(x))
        file.close()
        #print(audio_data / np.iinfo(np.int16).max)
        return audio_data

read_wav_file('C:/Users/arthu/OneDrive/Projet bop-it/Sons/Glassbreaker SFX/8KHZ 8bit/1point.wav')