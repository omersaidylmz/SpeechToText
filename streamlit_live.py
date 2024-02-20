import streamlit as st
import speech_recognition as sr

def recognize_speech(duration):
    # initialize the recognizer
    r = sr.Recognizer()

    st.info("Lütfen konuşun")

    with sr.Microphone() as source:
        st.warning("Kaydediliyor...")
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=duration)
        st.success("Kayıt Tamamlandı!")
        
        st.subheader("Tanınan Metin:")
        # convert speech to text with Turkish language support
        try:
            text = r.recognize_google(audio_data, language="tr-TR")
            st.write(text)

            # Save the recognized text to a text file
            save_to_file(text, "recognized_text.txt")
            st.success("Tanınan metin başarıyla bir dosyaya kaydedildi: recognized_text.txt")
        except sr.UnknownValueError:
            st.error("Konuşma Anlaşılamadı")
        except sr.RequestError as e:
            st.error(f"Hata Oluştu: {e}")

def save_to_file(text, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

def main():
    st.title("Canlı kayıdın Metine Dönüştürme")

    duration = st.slider("Kayıt Süresi (saniye)", min_value=1, max_value=60, value=3, step=1)

    if st.button("Başla"):
        recognize_speech(duration)

if __name__ == "__main__":
    main()
