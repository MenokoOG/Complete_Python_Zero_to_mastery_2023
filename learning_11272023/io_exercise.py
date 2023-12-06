"""I/O lesson exercise, Menoko OG, 11-2023"""
" This exercise takes a file and translates it and then writes a new file in translated language"
from translate import Translator

translator = Translator(to_lang="fr")
try:
    with open('test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        # print(translation)
        with open('test-fr.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print("Check your file path silly!")
