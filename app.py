import tkinter as tk
from src.translator import translate_text
from src.languages import LANGUAGES

window = tk.Tk()
window.title("AI Language Translator")
window.geometry("400x450")

title_label = tk.Label(window, text="AI Language Translator", font=("Arial", 16))
title_label.pack(pady=10)

input_text= tk.Text(window, height=5, width=40)
input_text.pack(pady=10)

languages= ['English', "Arabic", "French", "German", "Spanish"]

source_lang= tk.StringVar(window)
source_lang.set("English")

source_menu= tk.OptionMenu(window, source_lang, *languages)
source_menu.pack(pady=5)

target_lang= tk.StringVar(window)
target_lang.set("Arabic")

target_menu = tk.OptionMenu(window, target_lang, *languages)
target_menu.pack(pady=5)

def on_translate_click():
    text = input_text.get("1.0", tk.END).strip()

    if text == "":
        result_label.config(text="الرجاء إدخال نص للترجمة", fg="red")
        return

    source_name = source_lang.get()
    target_name = target_lang.get()
    source_code = LANGUAGES[source_name]
    target_code = LANGUAGES[target_name]

    result = translate_text(text, source_code, target_code)
    result_label.config(text=result, fg="blue")

translate_button = tk.Button(window, text="Translate", command=on_translate_click)
translate_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12), wraplength=350, fg="blue")
result_label.pack(pady=10)

window.mainloop()