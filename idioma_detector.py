from langdetect import detect
from iso639 import Lang

text = input("Escribe: ")
code = detect(text)

if(len(text) > 10):
    print(Lang(code).name)
else:
    print("Cadena demasiado corta.")

