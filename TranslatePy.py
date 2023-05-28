from googletrans import Translator

text_input = input("Digite: ")
translator = Translator()

translated = translator.translate(text_input, src="en", dest="pt")

print(translated.text)