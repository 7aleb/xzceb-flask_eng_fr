"""Function printing python version."""
from flask import Flask, render_template, request
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Function printing python version."""
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text
def french_to_english(french_text):
    """Function printing python version."""
    #write the code here
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text


app = Flask("Web Translator")

@app.route("/englishToFrench")
def translate_english_to_french():
    """translate en to fr"""
    text_to_translate = request.args.get('textToTranslate')
    translation = english_to_french(text_to_translate)
    return translation

@app.route("/frenchToEnglish")
def translate_french_to_english():
    """translate fr to en"""
    text_to_translate = request.args.get('textToTranslate')
    translation = french_to_english(text_to_translate)
    return translation

@app.route("/")
def render_index_page():
    """render template index.html"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
