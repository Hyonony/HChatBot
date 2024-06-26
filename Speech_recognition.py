import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language="ko-KR")
    print("You said: " + text)
    
    text = text.lower().strip()
    text = text.replace("ㅋ", "")
    text = text.replace("ㅠ", "")
    text = text.replace("ㅜ", "")

    print("Processed text: " + text)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
