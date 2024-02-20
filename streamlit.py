import streamlit as st
import speech_recognition as sr

def recognize_audio(file_path):
    # initialize the recognizer
    r = sr.Recognizer()

    # open the file
    with sr.AudioFile(file_path) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text) with Turkish language support
        text = r.recognize_google(audio_data, language="tr-TR")
        return text

def save_to_file(text, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

def main():
    st.title("Sesden Metine Çevirme Uygulaması")

    uploaded_file = st.file_uploader("Dosya Ekleme", type=["wav", "mp3"])

    if uploaded_file:
        result = recognize_audio(uploaded_file)
        st.subheader("Çevirilen Metin:")
        st.write(result)

        # Save the recognized text to a text file
        save_to_file(result, "kayıt_text.txt")
        st.success("Tanınan metin başarıyla bir dosyaya kaydedildi: kayıt_text.txt")

if __name__ == "__main__":
    main()
