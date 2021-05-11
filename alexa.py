import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        date1 = datetime.datetime.now().strftime('%D')
        talk('Current date is ' +date1)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'send whatsapp message' in command:
        talk('sure')
        talk('Please write the number')
        number = input()
        talk('Please write the message')
        mess = input()
        min1 = datetime.datetime.now().strftime('%M')
        hour = datetime.datetime.now().strftime('%H')
        pywhatkit.sendwhatmsg(number, mess, 00, 00)
    elif 'close' in command:
        talk('Sure, have a good day ahead')
        quit()


    else:
        talk('Command not found')


while True:
    run_alexa()
