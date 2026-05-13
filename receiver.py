import sounddevice as sd
import numpy as np
from scipy.fft import fft, fftfreq

SAMPLE_RATE = 44100
FREQ_START = 500
FREQ_ZERO = 1000
FREQ_ONE = 2000
FREQ_END = 3000
THRESHOLD = 20  
TOLERANCE = 80  

def get_loudest_freq(audio):
    if len(audio) == 0: return None
    audio = audio - np.mean(audio)
    spectrum = np.abs(fft(audio))[:len(audio)//2]
    frequencies = fftfreq(len(audio), 1/SAMPLE_RATE)[:len(audio)//2]
    idx = np.argmax(spectrum)
    if spectrum[idx] > THRESHOLD:
        return frequencies[idx]
    return None

def listen():
    print("Waiting for sender to start")
    
    while True:
        rec = sd.rec(int(SAMPLE_RATE * 0.1), samplerate=SAMPLE_RATE, channels=1)
        sd.wait()
        f = get_loudest_freq(rec.flatten())
        if f and abs(f - FREQ_START) < TOLERANCE:
            print("Detecting")
            break

    bits = []
    while True:
        rec = sd.rec(int(SAMPLE_RATE * 0.1), samplerate=SAMPLE_RATE, channels=1)
        sd.wait()
        f = get_loudest_freq(rec.flatten())

        if f is not None:
            if abs(f - FREQ_END) < TOLERANCE:
                print("Stop Detecting!")
                break
            
            bit = None
            if abs(f - FREQ_ONE) < TOLERANCE: bit = 1
            elif abs(f - FREQ_ZERO) < TOLERANCE: bit = 0

            if bit is not None:
                bits.append(bit)
                print(f"Received Bit: {bit}")

                while True:
                    silence_rec = sd.rec(int(SAMPLE_RATE * 0.05), samplerate=SAMPLE_RATE, channels=1)
                    sd.wait()
                    if get_loudest_freq(silence_rec.flatten()) is None:
                        break 

    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) == 8:
            chars.append(chr(int("".join(map(str, byte)), 2)))
    print(f"\nMessage: {''.join(chars)}")

listen()