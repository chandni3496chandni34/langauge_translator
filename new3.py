import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from indic_transliteration import sanscript
import pyttsx3
import playsound

engine = pyttsx3.init()
filename = "output.mp3"
print("Engine initialized successfully")

translator = Translator()
LANG_CODES = {code: name for code, name in LANGUAGES.items()}

def speak(text, filename):
    print("Speaking:", text)
    engine.save_to_file(text, filename)
    engine.runAndWait()
    playsound.playsound(filename)

def transliterate(text, src_lang):
    if src_lang != 'en' and src_lang in sanscript.SCHEMES.keys():
        return sanscript.transliterate(text, sanscript.ITRANS, sanscript.IAST)
    else:
        return text

def translate_text():
    text = text_input.get("1.0", "end-1c")
    dest_language = language_combobox.get()
    try:
        translation = translator.translate(text, dest=dest_language)
        print(translation.text)  # Moved inside the try block
        translated_text.set(translation.text)
        translated_text_transliterated.set(transliterate(translation.text, translation.src))
        speak(translation.text, filename)
    except Exception as e:
        translated_text.set(f"Error: {str(e)}")
        translated_text_transliterated.set("")

def clear_text():
    text_input.delete("1.0", "end")
    translated_text.set("")
    translated_text_transliterated.set("")

root = tk.Tk()
root.title("Real-Time Language Translator")

text_label = ttk.Label(root, text="Enter text to translate:")
text_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

text_input = tk.Text(root, height=5, width=40)
text_input.grid(row=1, column=0, padx=10, pady=5, sticky="w")

language_label = ttk.Label(root, text="Select destination language:")
language_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

language_combobox = ttk.Combobox(root, values=list(LANG_CODES.values()))
language_combobox.grid(row=3, column=0, padx=10, pady=5, sticky="w")
language_combobox.set("English")

translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=4, column=0, padx=10, pady=5, sticky="w")

clear_button = ttk.Button(root, text="Clear", command=clear_text)
clear_button.grid(row=4, column=0, padx=80, pady=5, sticky="w")

translated_text = tk.StringVar()
translated_text_transliterated = tk.StringVar()  # Define the translated_text_transliterated variable

translated_label = ttk.Label(root, text="Formal Translation:")
translated_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

translated_display = ttk.Label(root, textvariable=translated_text, wraplength=400, anchor="w")
translated_display.grid(row=6, column=0, padx=10, pady=5, sticky="w")

translated_label_transliterated = ttk.Label(root, text="Transliterated Translation:")
translated_label_transliterated.grid(row=7, column=0, padx=10, pady=5, sticky="w")

translated_display_transliterated = ttk.Label(root, textvariable=translated_text_transliterated, wraplength=400, anchor="w")
translated_display_transliterated.grid(row=8, column=0, padx=10, pady=5, sticky="w")

root.mainloop()
