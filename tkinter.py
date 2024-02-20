import tkinter as tk
from tkinter import ttk
import speech_recognition as sr

class SpeechRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canlı kayıdın Metine Dönüştürme")

        self.init_ui()

    def init_ui(self):
        self.duration_var = tk.IntVar()
        self.duration_slider = ttk.Scale(self.root, from_=1, to=60, orient="horizontal", variable=self.duration_var)
        self.duration_slider.set(3)
        self.duration_slider.pack(pady=10)

        self.start_button = ttk.Button(self.root, text="Başla", command=self.start_recognition)
        self.start_button.pack(pady=10)

        self.result_label = ttk.Label(self.root, text="Tanınan Metin:")
        self.result_label.pack()

        self.result_text = tk.Text(self.root, height=5, width=40)
        self.result_text.pack()

    def start_recognition(self):
        duration = self.duration_var.get()

        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Lütfen konuşun")
            print("Kaydediliyor...")

            audio_data = r.record(source, duration=duration)

            print("Kayıt Tamamlandı!")

            try:
                text = r.recognize_google(audio_data, language="tr-TR")
                self.result_text.delete(1.0, tk.END)  # Temizleme işlemi
                self.result_text.insert(tk.END, text)

                # Save the recognized text to a text file
                save_to_file(text, "recognized_text.txt")
                print("Tanınan metin başarıyla bir dosyaya kaydedildi: recognized_text.txt")
            except sr.UnknownValueError:
                print("Konuşma Anlaşılamadı")
            except sr.RequestError as e:
                print(f"Hata Oluştu: {e}")

def save_to_file(text, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

def main():
    root = tk.Tk()
    app = SpeechRecognitionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
