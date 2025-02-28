from googletrans import Translator

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text

if __name__ == "__main__":
    print("Simple Language Translation Tool")
    text = input("Enter text to translate: ")
    src_lang = input("Enter source language (e.g., 'en' for English): ")
    dest_lang = input("Enter destination language (e.g., 'fr' for French): ")
    
    try:
        translated_text = translate_text(text, src_lang, dest_lang)
        print(f"Translated Text: {translated_text}")
    except Exception as e:
        print(f"Error: {e}")
