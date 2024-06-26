import speech_recognition as sr

# 음성 인식기 생성
r = sr.Recognizer()

# 마이크로부터 음성 입력 받기
with sr.Microphone() as source:
    print("말씀해 주세요.")
    audio = r.listen(source)

try:
    # 음성을 텍스트로 변환
    text = r.recognize_google(audio, language="ko-KR")
    print("사용자가 말한 내용: " + text)
    
    # 노이즈 제거 및 발음 보정
    text = text.lower().strip()
    text = text.replace("ㅋ", "")
    text = text.replace("ㅠ", "")
    text = text.replace("ㅜ", "")

    print("처리된 텍스트: " + text)

except sr.UnknownValueError:
    print("Google 음성 인식에 실패했습니다.")
except sr.RequestError as e:
    print("Google 음성 인식 요청에 실패했습니다: {0}".format(e))
