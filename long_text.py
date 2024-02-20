# Gerekli kütüphaneleri içe aktarın
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Bir konuşma tanıma nesnesi oluşturun
r = sr.Recognizer()

# Ses dosyasındaki metni tanımak için bir fonksiyon
def transcribe_audio(path):
    with sr.AudioFile(path) as source:
        audio_listened = r.record(source)
        text = r.recognize_google(audio_listened, language="tr-TR")
    return text

# Sessizlikte ses dosyasını parçalara bölen ve her birine konuşma tanıma uygulayan bir fonksiyon
def get_large_audio_transcription_on_silence(path):
    sound = AudioSegment.from_file(path)
    chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=sound.dBFS-14, keep_silence=500)
    folder_name = "ses-parcaları"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(folder_name, f"parca{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        try:
            text = transcribe_audio(chunk_filename)
        except sr.UnknownValueError as e:
            print("Hata:", str(e))
        else:
            text = f"{text.capitalize()}. "
            print(chunk_filename, ":", text)
            whole_text += text
    return whole_text

# Belirli bir aralıkta ses dosyasını bölen ve her birine konuşma tanıma uygulayan bir fonksiyon
def get_large_audio_transcription_fixed_interval(path, dakika=5):
    sound = AudioSegment.from_file(path)
    chunk_length_ms = int(1000 * 60 * dakika)
    chunks = [sound[i:i + chunk_length_ms] for i in range(0, len(sound), chunk_length_ms)]
    folder_name = "sabit-aralik-ses-parcaları"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(folder_name, f"parca{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        try:
            text = transcribe_audio(chunk_filename)
        except sr.UnknownValueError as e:
            print("Hata:", str(e))
        else:
            text = f"{text.capitalize()}. "
            print(chunk_filename, ":", text)
            whole_text += text
    return whole_text

if __name__ == '__main__':
    import sys
    path = sys.argv[1]
    print("\nTam metin:", get_large_audio_transcription_on_silence(path))
    print("="*50)
    print("\nTam metin:", get_large_audio_transcription_fixed_interval(path, dakika=1/6))
