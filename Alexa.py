# Ikemuefuna Emmanuel
# 2019234083
# Electrical Engineering 
# ECE 331
# Signal and Systems 
# Speech to alexa Recognition Project

# Import the library in your Python script
import speech_recognition as sr

# Initialize a recognizer object:
r = sr.Recognizer()

# Use the Microphone class to access the microphone and record audio:
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something...")
    audio = r.listen(source)

# Use the recognize_google() method to perform speech recognition
alexa = r.recognize_google(audio)
print("You said: " + alexa)

# Add error handling to handle cases where the speech recognition fails
try:
    alexa = r.recognize_google(audio)
    print("You said: " + alexa)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Alexa Speech Recognition service; {0}".format(e))

