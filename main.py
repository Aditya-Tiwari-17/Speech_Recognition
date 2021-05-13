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
engine.say("hey i am Aura i am here to help you")
engine.say("i loveeeee Aaditya")
engine.runAndWait()


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
            if 'aura' in command:
                command = command.replace('aura', '')
                print(command)
    except:
        pass
    return command


def run_aura():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a Aditya in my life')
    elif 'are you single' in command:
        talk('I am in a relationship with Aditya Tiwari')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'who made you' in command:
        talk('I was made with all the love by Aditya Tiwari')
    else:
        talk('Please say the command again.')


while True:
    run_aura()

