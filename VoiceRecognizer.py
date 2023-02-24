import time
import speech_recognition as sr

import config

# Initialize the SpeechRecognizer object
r = sr.Recognizer()

# Get the language configuration from the config file
language = config.language

# Open a log file to record any errors encountered during speech recognition
log_file = open(f"logs/{time.time()}")


# Define a function to get spoken words from the user
def get_spoken_text():
    # Use the user's microphone as the audio source
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        # Attempt to recognize the spoken words using Google Speech Recognition API
        return r.recognize_google(audio, language=language)
    except sr.UnknownValueError:
        # If the SpeechRecognizer was unable to recognize any spoken words, return an empty string
        return ""
    except sr.RequestError as e:
        # If there was an error with the Google Speech Recognition service, record the error in the log file
        log_file.write("Could not request results from Google Speech Recognition service; {0}\n".format(e))
