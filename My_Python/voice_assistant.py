import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import urllib.parse


# -----------------------------
# Text-to-Speech Function
# -----------------------------
engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# -----------------------------
# Take Voice Command
# -----------------------------
def take_command():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)

        print("You said:", command)

        return command.lower()

    except sr.UnknownValueError:

        speak("Sorry, I did not understand that.")
        return ""

    except sr.RequestError:

        speak("Sorry, I am having trouble connecting to the speech service.")
        return ""


# -----------------------------
# Voice Assistant
# -----------------------------
def run_assistant():

    speak("Hello! I am your voice assistant.")
    speak(
        "You can ask me to open YouTube, open Google, "
        "tell the time, tell the date, search something, "
        "or ask about something."
    )

    while True:

        command = take_command()

        if not command:
            continue

        # Open YouTube
        if "youtube" in command:

            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube.")

        # Open Google
        elif "open google" in command:

            webbrowser.open("https://www.google.com")
            speak("Opening Google.")

        # Tell time
        elif "time" in command:

            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}.")

        # Tell date
        elif "date" in command:

            today = datetime.datetime.now().strftime(
                "%A, %B %d, %Y"
            )

            speak(f"Today is {today}.")

        # Google search
        elif "search" in command:

            query = command.replace("search", "").strip()

            if query:

                url = (
                    "https://www.google.com/search?q="
                    + urllib.parse.quote(query)
                )

                webbrowser.open(url)

                speak(f"Searching for {query} on Google.")

        # Wikipedia search
        elif "wikipedia" in command:

            topic = command.replace("wikipedia", "").strip()

            if topic:

                try:

                    result = wikipedia.summary(
                        topic,
                        sentences=2
                    )

                    speak(result)

                except wikipedia.exceptions.DisambiguationError:

                    speak(
                        "There are multiple results for that topic. "
                        "Please be more specific."
                    )

                except wikipedia.exceptions.PageError:

                    speak("I could not find that topic on Wikipedia.")

        # Exit
        elif (
            "exit" in command
            or "quit" in command
            or "goodbye" in command
        ):

            speak("Goodbye! Have a nice day.")
            break

        else:

            speak(
                "I can open YouTube or Google, "
                "tell you the time or date, "
                "search Google, or search Wikipedia."
            )


# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    run_assistant()
    
    