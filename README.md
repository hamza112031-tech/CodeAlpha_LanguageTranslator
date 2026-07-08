# 🌐 AI Language Translator

A simple desktop application built with Python that translates text between multiple languages using a graphical user interface (GUI).

This project was developed as part of the **CodeAlpha Artificial Intelligence Internship** (Task 1: Language Translation Tool).

## 📋 Features

- Translate text between 5 languages: English, Arabic, French, German, and Spanish
- Simple and clean graphical interface built with `tkinter`
- Copy translated text to clipboard with one click
- Clear input/output with one click
- Error handling for empty input and translation failures

## 🛠️ Built With

- **Python 3.12**
- **tkinter** — for the graphical user interface
- **deep-translator** — for the translation engine (Google Translate backend)


## ⚙️ Installation

1. Clone the repository:
```bash
   git clone https://github.com/hamza112031-tech/CodeAlpha_LanguageTranslator.git
   cd CodeAlpha_LanguageTranslator
```

2. Create and activate a virtual environment:
```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1   # Windows PowerShell
```

3. Install the dependencies:
```bash
   pip install -r requirements.txt
```

4. Run the application:
```bash
   python app.py
```

## 🚀 Usage

1. Enter the text you want to translate in the text box.
2. Select the source language and target language from the dropdown menus.
3. Click **Translate** to see the result.
4. Use **Copy Result** to copy the translated text, or **Clear** to reset the fields.

