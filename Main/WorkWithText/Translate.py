from mtranslate import translate
def TranslateText(text):

    translated_text = translate(text, 'ru')
    return translated_text