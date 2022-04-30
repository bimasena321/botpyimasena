import speech_recognition as sr
from gtts import gTTS
import os
import pyttsx3
import pywhatkit

print("[1].mulai")
print("[2].install bahan2x")
print("[0].keluar")

nma = int(input("==>"))

if nma == 1:
    mesin = pyttsx3.init()
    suara = mesin.getProperty('voices')


    song = "suara anda tidak jelas mohon diulang kembali"
    bas = "id"
    vim = sr.Recognizer()

    with sr.Microphone() as b:
        mesin.say('good morning mr.bima')
        mesin.say('say something')
        mesin.runAndWait()
        print('mendengarkan:')
        suara = vim.listen(b)

    try:
        pesan = suara.Recognizer(suara)
        pywhatkit.playonyt(pesan)
        print('kamu: {}'.format(pesan))
    except:
        nama = gTTS(text=song, lang=bas)
        nama.save('song.mp3')
        os.system('song.mp3')
elif nma == 2:
    os.system('pip install -r requirements.txt')
else:
    print("pipihan anda tidak ada")

