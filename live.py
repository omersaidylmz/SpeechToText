import speech_recognition as sr
import sys

duration = int(sys.argv[1])

# initialize the recognizer
r = sr.Recognizer()
print("Lütfen konuşun")
with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=duration)
    print("Tanınıyor...")
    # convert speech to text with Turkish language support
    text = r.recognize_google(audio_data, language="tr-TR")
    print("Metin:", text)
