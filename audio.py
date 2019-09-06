import speech_recognition as sr


def record():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(""" Give Jarvis a command.
                  Example : where is eifel tower
                  Your turn. Speak the command : """)
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said : " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
    return data
