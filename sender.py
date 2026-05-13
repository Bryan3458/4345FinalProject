import sounddevice as sd
import numpy as np
import time

SAMPLE_RATE = 44100 
BIT_DURATION = 0.5 
GAP_DURATION = 0.3  

FREQ_START = 500
FREQ_ZERO = 1000
FREQ_ONE = 2000
FREQ_END = 3000

def play_tone(freq, duration):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    
    signal = np.sin(2 * np.pi * freq * t).astype(np.float32)
    
    
    fade_len = int(SAMPLE_RATE * 0.02)
    fade = np.linspace(0, 1, fade_len)
    signal[:fade_len] *= fade
    signal[-fade_len:] *= fade[::-1]
    
    sd.play(signal, SAMPLE_RATE)
    sd.wait()

def send_message(message):
    play_tone(FREQ_START, BIT_DURATION)
    time.sleep(GAP_DURATION)

    bits = []
    for char in message:
        bits += [int(b) for b in format(ord(char), '08b')]

    for i, bit in enumerate(bits):
        freq = FREQ_ONE if bit == 1 else FREQ_ZERO
        print(f"Bit {i+1}: {bit}")
        play_tone(freq, BIT_DURATION)
        time.sleep(GAP_DURATION)

    play_tone(FREQ_END, BIT_DURATION)
    print("--- Done! ---")

msg = input("Enter message: ")
send_message(msg)