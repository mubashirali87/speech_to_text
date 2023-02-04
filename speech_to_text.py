import speech_recognition as sr

# initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
    print("Text: "+r.recognize_google(audio_text))
