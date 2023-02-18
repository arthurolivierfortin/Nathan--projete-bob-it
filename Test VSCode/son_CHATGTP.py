import wave
import numpy as np
import RPi.GPIO as GPIO

def read_wav_file(filename):
    with wave.open(filename, 'rb') as wav:
        n_channels = wav.getnchannels()
        sample_width = wav.getsampwidth()
        frame_rate = wav.getframerate()
        n_frames = wav.getnframes()

        data = wav.readframes(n_frames)
        audio_data = np.frombuffer(data, dtype=np.int16)

        # Reshape audio data based on number of channels
        audio_data = audio_data.reshape(-1, n_channels)

        return audio_data

def convert_to_pwm(audio_data, pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    pwm = GPIO.PWM(pin, 1000)
    pwm.start(0)

    # Normalize audio data to range between -1 and 1
    audio_data_norm = audio_data / np.iinfo(np.int16).max

    # Map audio data to PWM duty cycle range
    pwm_duty = (audio_data_norm + 1) * 50

    for duty in pwm_duty:
        pwm.ChangeDutyCycle(duty)