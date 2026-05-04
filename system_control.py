import speech_recognition as sr 
import pyttsx3 
import os 
import webbrowser

#Initialize text-to-speech engine

engine = pyttsx3.init()

def speak(text): 
  engine.say(text) 
  engine.runAndWait()

#Initialize recognizer

r = sr.Recognizer()

def take_command():
  with sr.Microphone() as source:
     print("Listening...") 
     r.pause_threshold = 1
     audio = r.listen(source)

  try:
      print("Recognizing...")
      query = r.recognize_google(audio, language='en-in')
      print(f"You said: {query}\n")
  except Exception as e:
      print("Say that again please...")
      return "None"
  return query.lower()

#Main automation logic

if __name__ == "__main__":
    speak("Voice assistant activated")

    while True:
       command = take_command()

       if 'open word' in command:
        speak("Opening Microsoft Word")
        os.system("start winword")

       elif 'open notepad' in command:
        speak("Opening Notepad")
        os.system("notepad")

       elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

       elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

       elif 'new document' in command:
        speak("Creating a new Word document")
        os.system("start winword")

       elif 'shutdown computer' in command:
           speak("Shutting down computer")
           os.system("shutdown /s /t 5")

       elif 'restart computer' in command:
           speak("Restarting computer")
           os.system("shutdown /r /t 5")

       elif 'exit' in command or 'stop' in command:
        speak("Goodbye")
        break

       else:
        speak("Command not recognized")