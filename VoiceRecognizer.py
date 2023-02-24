import time
import speech_recognition as sr
import config

# Initialize the SpeechRecognizer object
r = sr.Recognizer()

# Get the language configuration from the config file
language = config.language_codes[config.input_language]

# Open a log file to record any errors encountered during speech recognition
log_file = open(f"logs/{time.time()}", 'w')


# Define a function to get spoken words from the user
def get_spoken_text():
    # Use the user's microphone as the audio source
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        # Attempt to recognize the spoken words using Google Speech Recognition API
        text = r.recognize_google(audio, language=language)
        log_file.write(f"{time.time()} - {text}\n")
        return text
    except sr.UnknownValueError:
        # If the SpeechRecognizer was unable to recognize any spoken words, return an empty string
        return ""
    except sr.RequestError as e:
        # If there was an error with the Google Speech Recognition service, record the error in the log file
        log_file.write(f"{time.time()} - Could not request results from Google Speech Recognition service; {e}\n")
        return ""
