#import module 
import pyttsx3

# Initialize the TTS engine

engine = pyttsx3.init()

# speed of voice (defualt voice 200)
engine.setProperty('rate', 130)


# Get available voices
voices = engine.getProperty('voices')
# Print available voices =====================>
# for voice in voices:
#     print(f"ID: {voice.id}, Name: {voice.name}, Lang: {voice.languages}")
# Choose a voice (for example, index 1)
voice_index = 1  # Change this index based on your preference (0 voice man and 1 female)
engine.setProperty('voice', voices[voice_index].id)


# Define the text to be spoken
text = ''''Hello there!
This voice is not just sound — it's an emotion.
Carefully crafted with passion and creativity.
Designed to bring words to life.
Every word you hear holds a piece of hard work.
Proudly created by Maaz'''
# Speak the text
engine.say(text)


# Wait for the speaking to finish 
engine.runAndWait()
