import speech_recognition as sr

def speechToTranscript(filename):
    r = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio_data = 