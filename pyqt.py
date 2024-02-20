import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
import speech_recognition as sr

class SpeechRecognitionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Canlı kayıdın Metine Dönüştürme")
        self.setGeometry(100, 100, 400, 200)

        self.init_ui()

    def init_ui(self):
        # Arka planı siyah yapma
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(0, 0, 0))
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        self.setPalette(palette)

        self.duration_slider = QSlider(Qt.Horizontal)
        self.duration_slider.setMinimum(1)
        self.duration_slider.setMaximum(60)
        self.duration_slider.setValue(3)

        self.start_button = QPushButton("Başla")
        self.start_button.clicked.connect(self.start_recognition)

        self.result_label = QLabel("Tanınan Metin:")
        self.result_text = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.duration_slider)
        layout.addWidget(self.start_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def start_recognition(self):
        duration = self.duration_slider.value()

        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Lütfen konuşun")
            print("Kaydediliyor...")

            audio_data = r.record(source, duration=duration)

            print("Kayıt Tamamlandı!")

            try:
                text = r.recognize_google(audio_data, language="tr-TR")
                self.result_text.setText(text)

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

def run_app():
    app = QApplication(sys.argv)
    main_app = SpeechRecognitionApp()
    main_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()
