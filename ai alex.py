import speech_recognition as sr
import pywhatkit
import pyttsx3
import datetime
import wikipedia
import pyjokes
engine =pyttsx3.init()
listener =sr.Recognizer()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
  engine.say(text)
  engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice=listener.listen(source)
            command =listener.recognize_google(voice)
            command =command.upper()
            if 'ALEXA' in command:
                command=command.replace('ALEXA','')
                print(command)

    except:
        pass
    return command
def run_command():
    command =take_command()
    if 'PLAY' in command:
        song=command.replace('PLAY','')
        talk('playing '+song)
        pywhatkit.playonyt(song)
    elif 'TIME' in command:
        time=datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('current time is '+time)
    elif 'WHATSAPP' in command:
        person=command.replace('WHATSAPP MESSAGE','')
        pywhatkit.sendwhatmsg('+91'+person,'hi',22,38)
    elif 'WHO IS' in command:
        person=command.replace('WHO IS','')
        info=wikipedia.summary(person,3)
        print(info)
        talk(info)
    elif 'JOKE' in command:

        talk(pyjokes.get_joke())
    else:
        talk('can you please tell agin')


while True:
    run_command()