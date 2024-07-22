from speech_to_text import speech_to_text
from text_to_speech import text_to_speech
from Translator import translate_text
import google.generativeai as genai
import requests
def genai_response(text):
    genai.configure(api_key=open("./keys.txt",'r').read().split()[0])

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 50,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[]
    )

    instruction = "response like scholar and limit response to 50 words and also give response so that it is a clean sentence with full stops, letters only\nprompt: "
    response = chat_session.send_message(instruction + text)
    return response.text

def latest_news(dept):
    url = "https://google-news13.p.rapidapi.com/"
    querystring = {"lr": "en-US"}
    headers = {
        "x-rapidapi-key": open("./keys.txt",'r').read().split()[1],
        "x-rapidapi-host": "google-news13.p.rapidapi.com"
    }
    if dept in ["latest", "entertainment", "world", "bussiness", "health", "sport", "science", "technology"]:
        url += dept
    else:
        url += "latest"
    response = requests.get(url, headers=headers, params=querystring).json()
    print()
    news = ""
    counter = 0
    for i in response["items"]:
        if counter == 2:
            break
        news += i["title"] + " that is " + i["snippet"]
        news = news.rstrip('.')
        news += ".\n"
        counter += 1
    return news



lang_codes1 = {
    "Telugu": "te-IN",
    "Hindi": "hi-IN",
    "English": "en-US"

}

lang_codes2 = {
    "Telugu": "te",
    "Hindi": "hi",
    "English": "en"
}

print("Select the language you like. For example Telugu, Hindi, English etc.")
text_to_speech("Select the language you like. For example Telugu, Hindi, English", "en")
language = speech_to_text()
# language = "Telugu"
lang_code1 = lang_codes1[language]
lang_code2 = lang_codes2[language]


intro = translate_text("Hi Kailash! How can I help you?", "en", lang_code2)
print(intro)
text_to_speech(intro, lang_code2)
while True:
    prompt = speech_to_text(lang_code1)
    if translate_text("news", "en", lang_code2) in prompt:
        dept = prompt.split()[-1]
        dept = translate_text(dept, lang_code2, "en").lower()
        # print(dept)
        news = latest_news(dept)
        translated_text = translate_text(news, "en", lang_code2)
        print("response: ", translated_text)
        text_to_speech(translated_text, lang_code2)
    else:
        translated_text = translate_text(prompt, lang_code2, "en")
        response = genai_response(translated_text)
        translated_text = translate_text(response, "en", lang_code2)
        print("response: ", translated_text)
        text_to_speech(translated_text, lang_code2)

