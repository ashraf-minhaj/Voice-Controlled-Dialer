"""
*** Voice Controlled Call dialer ***
by: Ashraf Minhaj
mail: ashraf_minhaj@yahoo.com
blogpost/ Tutorial: ashrafminhajgb.blogspot.com
"""

"""
Required:
1. python3
2. speechRecognition package
2.1. google speech to text api
"""

import speech_recognition as sr     #for speech recognition [speech to text]
import pyttsx3                      #for speech [text to speech]
import serial                 #for serial communication to arduino

talk = pyttsx3.init()

#ard = serial.Serial("COM", 9600) #Set port and buad rate 

def dial(num):

    talk.setProperty('rate', 90)
    talk.say("Calling")
    talk.say(num)
    #ard.write(num)
    
    talk.runAndWait()


while True:         #forever loop

    try:
        speech = sr.Recognizer()
    
        #take input from microphone
        with sr.Microphone() as source:
            print("Say 'CALL' followed by a Cell Number \n>>> ")
            voice = speech.listen(source) 
            text = speech.recognize_google(voice)
            print(text) #print what it heard just to debug

            textList = text.split(" ")

            if textList.pop(0) == 'call':
                number = ''.join(textList)
                print(number)

            dial(number)

                
    
    except: #No wake up word found
        pass #Do nothing avoiding the error