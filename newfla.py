from flask import Flask, render_template, request
from playsound import playsound
from googletrans import Translator
from gtts import gTTS
import os
import speech_recognition as sr

app = Flask(__name__)

# Dictionary mapping language names to language codes
dic = ('afrikaans', 'af', 'albanian', 'sq',  
       'amharic', 'am', 'arabic', 'ar', 
       'armenian', 'hy', 'azerbaijani', 'az',  
       'basque', 'eu', 'belarusian', 'be', 
       'bengali', 'bn', 'bosnian', 'bs', 'bulgarian', 
       'bg', 'catalan', 'ca', 'cebuano', 
       'ceb', 'chichewa', 'ny', 'chinese (simplified)', 
       'zh-cn', 'chinese (traditional)', 
       'zh-tw', 'corsican', 'co', 'croatian', 'hr', 
       'czech', 'cs', 'danish', 'da', 'dutch', 
       'nl', 'english', 'en', 'esperanto', 'eo',  
       'estonian', 'et', 'filipino', 'tl', 'finnish', 
       'fi', 'french', 'fr', 'frisian', 'fy', 'galician', 
       'gl', 'georgian', 'ka', 'german', 
       'de', 'greek', 'el', 'gujarati', 'gu', 
       'haitian creole', 'ht', 'hausa', 'ha', 
       'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 
       'hi', 'hmong', 'hmn', 'hungarian', 
       'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',  
       'id', 'irish', 'ga', 'italian', 
       'it', 'japanese', 'ja', 'javanese', 'jw', 
       'kannada', 'kn', 'kazakh', 'kk', 'khmer', 
       'km', 'korean', 'ko', 'kurdish (kurmanji)',  
       'ku', 'kyrgyz', 'ky', 'lao', 'lo', 
       'latin', 'la', 'latvian', 'lv', 'lithuanian', 
       'lt', 'luxembourgish', 'lb', 
       'macedonian', 'mk', 'malagasy', 'mg', 'malay', 
       'ms', 'malayalam', 'ml', 'maltese', 
       'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian', 
       'mn', 'myanmar (burmese)', 'my', 
       'nepali', 'ne', 'norwegian', 'no', 'odia', 'or', 
       'pashto', 'ps', 'persian', 'fa', 
       'polish', 'pl', 'portuguese', 'pt', 'punjabi',  
       'pa', 'romanian', 'ro', 'russian', 
       'ru', 'samoan', 'sm', 'scots gaelic', 'gd', 
       'serbian', 'sr', 'sesotho', 'st', 
       'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si', 
       'slovak', 'sk', 'slovenian', 'sl', 
       'somali', 'so', 'spanish', 'es', 'sundanese', 
       'su', 'swahili', 'sw', 'swedish', 
       'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu', 
       'te', 'thai', 'th', 'turkish', 
       'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 
       'ug', 'uzbek',  'uz', 
       'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh', 
       'yiddish', 'yi', 'yoruba', 
       'yo', 'zulu', 'zu') 


class LanguageTranslatorApp:
    def __init__(self):
        self.translator = Translator()
        self.recognizer = sr.Recognizer()

    def translate_text(self, text, dest_language):
        translation = self.translator.translate(text, dest=dest_language)
        return translation.text

    def speak(self, text, lang='en'):
        tts = gTTS(text=text, lang=lang)
        tts.save("translated_voice.mp3")
        playsound("translated_voice.mp3")
        os.remove("translated_voice.mp3")
    def listen_microphone(self):
        with sr.Microphone() as source:
            print("Speak:")
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            query = self.recognizer.recognize_google(audio)
            return query
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""
translator_app = LanguageTranslatorApp()
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the form was submitted with microphone input
        if 'microphone' in request.form:
            input_text = translator_app.listen_microphone()
        else:
            input_text = request.form['input_text']
        dest_language = request.form['language_choice']
        translated_text = translator_app.translate_text(input_text, dest_language)
        translator_app.speak(translated_text, dest_language)
        return render_template('index.html', translated_text=translated_text)
    return render_template('index.html', languages=dic)

if __name__ == '__main__':
    app.run(debug=True)
