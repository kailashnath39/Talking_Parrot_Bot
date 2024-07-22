from gtts import gTTS
import pygame
import io


def text_to_speech(text, language='en'):
    # Convert the text to speech and save it to a bytes buffer
    tts = gTTS(text=text, lang=language, slow=False)
    buffer = io.BytesIO()
    tts.write_to_fp(buffer)
    buffer.seek(0)

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the saved audio file from the buffer
    pygame.mixer.music.load(buffer, 'mp3')

    # Play the audio file
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# text_to_speech("హాయ్ కైలాష్!నేను మీకు ఎలా సహాయపడగలను?", "te")

