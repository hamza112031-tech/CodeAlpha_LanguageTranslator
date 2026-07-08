import tkinter as tk
from src.translator import translate_text
from src.languages import LANGUAGES
BG_COLOR = "#f0f4f8"
BUTTON_COLOR = "#4a90d9"
TEXT_COLOR = "#2c3e50"

window = tk.Tk()
window.configure(bg=BG_COLOR)
window.title("AI Language Translator")
window.geometry("400x450")

title_label = tk.Label(window, text="AI Language Translator", font=("Arial", 16), bg=BG_COLOR, fg=TEXT_COLOR)
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

def on_clear_click():
    input_text.delete("1.0", tk.END)
    result_label.config(text="")

def on_copy_click():
    result_text = result_label.cget("text")
    window.clipboard_clear()
    window.clipboard_append(result_text)

copy_button = tk.Button(window, text="Copy Result", command=on_copy_click, bg="#27ae60", fg="white")
copy_button.pack(pady=5)

translate_button = tk.Button(window, text="Translate", command=on_translate_click, bg=BUTTON_COLOR, fg="white")
translate_button.pack(pady=10)
clear_button = tk.Button(window, text="Clear", command=on_clear_click, bg="#e74c3c", fg="white")
clear_button.pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 12), wraplength=350, fg="blue", bg=BG_COLOR)
result_label.pack(pady=10)

window.mainloop()