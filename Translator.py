from googletrans import Translator


def translate_text(text, src_language='auto', dest_language='en'):
    # Initialize the Translator
    translator = Translator()

    # Translate the text
    translation = translator.translate(text, src=src_language, dest=dest_language)

    # Print the original and translated text
    # print(f"Original text ({src_language}): {text}")
    return translation.text

