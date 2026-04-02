import pyaudio
import numpy as np

p = pyaudio.PyAudio()

try:
    info = p.get_default_input_device_info()
    print("Default Input Device:", info['name'])
except Exception as e:
    print("Coult not get default device:", e)

try:
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)

    print("Listening for 3 seconds to measure volume...")
    max_volume = 0
    for _ in range(int(44100 / 1024 * 3)):
        try:
            data = np.frombuffer(stream.read(1024, exception_on_overflow=False), dtype=np.int16)
            vol = np.max(np.abs(data))
            if vol > max_volume:
                max_volume = vol
        except Exception as e:
            pass

    print(f"Max recorded volume (0-32768): {max_volume}")

    if max_volume < 100:
        print("RESULT: ALMOST NO SOUND. Microphone might be muted, blocked by Windows Privacy, or wrong default device.")
    else:
        print("RESULT: SOUND CAPTURED.")

    stream.stop_stream()
    stream.close()
except Exception as e:
    print("Could not listen to microphone:", e)

p.terminate()
