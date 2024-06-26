import speech_recognition as sr
from pronunciation_rules import PRONUNCIATION_RULES
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from korean_stopword import STOP_WORDS 

# NLTK 'punkt' 리소스 다운로드
nltk.download('punkt')

# NLTK 'stopwords' 리소스 다운로드
nltk.download('stopwords')

# 음성 인식기 생성
r = sr.Recognizer()

try:
    # 마이크로부터 음성 입력 받기
    with sr.Microphone() as source:
        print("말씀해 주세요.")
        r.adjust_for_ambient_noise(source, duration=1)  # 주변 소음 감지 및 조정
        audio = r.listen(source, timeout=10, phrase_time_limit=30)  # 타임아웃 및 제한 시간 설정

    # 음성을 텍스트로 변환
    text = r.recognize_google(audio, language="ko-KR")
    print("사용자가 말한 내용: " + text)
    
    # 노이즈 제거 및 발음 보정
    text = text.lower().strip()
    for key, value in PRONUNCIATION_RULES.items():
        text = text.replace(key, value)
    
    # NLTK를 활용한 텍스트 처리
    tokens = nltk.word_tokenize(text)
    filtered_tokens = [word for word in tokens if word.lower() not in STOP_WORDS]  # 수정된 부분
    
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
    
    processed_text = ' '.join(stemmed_tokens)
    
    print("처리된 텍스트: " + processed_text)

except sr.WaitTimeoutError:
    print("음성 입력 시간이 초과되었습니다. 타임아웃 설정을 확인하세요.")
except sr.RequestError as e:
    print("Google 음성 인식 서비스에 연결할 수 없습니다: {0}".format(e))
except sr.UnknownValueError as e:
    print("Google 음성 인식에 실패했습니다: {0}".format(e))
except OSError as e:
    print("마이크 사용에 실패했습니다: {0}".format(e))
except Exception as e:
    print("알 수 없는 오류가 발생했습니다: {0}".format(e))