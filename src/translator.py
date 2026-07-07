from deep_translator import GoogleTranslator
def translate_text(text, source_lang, target_lang):
    try:
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"حصل خطأ أثناء الترجمة: {e}"
    
if __name__ == "__main__":
    result = translate_text("Hello, how are you?", "en", "ar")
    print(result)