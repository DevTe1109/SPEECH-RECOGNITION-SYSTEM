import speech_recognition as sr

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(file_path) as source:
        print("🎤 Listening to audio...")
        audio = recognizer.record(source)

    try:
        print("🧠 Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print("✅ Transcription:\n")
        print(text)
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"❌ Could not request results; {e}")

if __name__ == "__main__":
    path = input("Enter path to WAV audio file: ")
    transcribe_audio(path)
