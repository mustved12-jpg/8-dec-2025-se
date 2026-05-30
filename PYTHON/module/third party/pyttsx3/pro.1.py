# pip install pyttsx3
import pyttsx3
engin=pyttsx3.init()
engin.setProperty("rate",150)# voise
engin.setProperty("volume",0.5)# 1.0 full volume hai
engin.say("tujhe bhool jana jana mumkin nhi too yaaad naa aaye esa koi din nhi oooohohooooo")
engin.runAndWait()
