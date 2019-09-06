from speak import speak
from time import ctime
import webbrowser as wb


def jarvis(data, name, speak):
    if "how are you" in data:
        speak("I am fine")

    elif "what time is it" in data:
        speak(ctime())

    elif "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on " + name + ", I will show you where " + location + " is.")
        wb.open_new_tab("https://www.google.nl/maps/place/" +
                        location + "/&amp;")
    else:
        speak(",,,,,,,I did not get what you said !")
