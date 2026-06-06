import win32com.client#check chatgpt for module installation  i forgot the name
def speak(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

speak("Hi")