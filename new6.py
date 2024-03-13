import tkinter as tk
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

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
    def __init__(self, master):
        self.master = master
        master.title("Language Translator")

        self.translator = Translator()

        self.input_label = tk.Label(master, text="Enter Text:")
        self.input_label.grid(row=0, column=0, sticky='w')

        self.input_text = tk.Text(master, height=5, width=50)
        self.input_text.grid(row=0, column=1, columnspan=2)

        self.language_label = tk.Label(master, text="Select Language:")
        self.language_label.grid(row=1, column=0, sticky='w')

        self.language_choice = tk.StringVar()
        self.language_choice.set("Select Language")
        self.language_menu = tk.OptionMenu(master, self.language_choice, dic)
        self.language_menu.grid(row=1, column=1, sticky='w')

        self.translate_button = tk.Button(master, text="Translate", command=self.translate)
        self.translate_button.grid(row=1, column=2, sticky='e')

        self.output_label = tk.Label(master, text="Translated Text:")
        self.output_label.grid(row=2, column=0, sticky='w')

        self.output_text = tk.Text(master, height=5, width=50)
        self.output_text.grid(row=2, column=1, columnspan=2)

    def translate(self):
        input_text = self.input_text.get("1.0", "end-1c")
        if input_text:
            dest_language = language_codes[self.language_choice.get()]
            translated_text = self.translate_text(input_text, dest_language)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, translated_text)
            self.speak(translated_text, dest_language)

    def translate_text(self, text, dest_language):
        translation = self.translator.translate(text, dest=dest_language)
        return translation.text

    def speak(self, text, lang='en'):
        tts = gTTS(text=text, lang=lang)
        tts.save("translated_voice.mp3")
        playsound("translated_voice.mp3")
        os.remove("translated_voice.mp3")

def main():
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
