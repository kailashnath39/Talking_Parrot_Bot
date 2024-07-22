import speech_recognition as sr


def speech_to_text(lang_code = "en-US"):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Ready to record. Please speak into the microphone.")
        audio = recognizer.listen(source, timeout=5)

    # Convert audio to text
    try:
        print("Recognizing the speech...")
        text = recognizer.recognize_google(audio, language=lang_code)
        print("\n\nYou said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
