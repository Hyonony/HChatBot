import speech_recognition as sr
from pronunciation_rules import PRONUNCIATION_RULES
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

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
        audio = r.listen(source)

    # 음성을 텍스트로 변환
    text = r.recognize_google(audio, language="ko-KR")
    print("사용자가 말한 내용: " + text)
    
    # 노이즈 제거 및 발음 보정
    text = text.lower().strip()
    for key, value in PRONUNCIATION_RULES.items():
        text = text.replace(key, value)
    
    # NLTK를 활용한 텍스트 처리
    tokens = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('korean'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
    
    processed_text = ' '.join(stemmed_tokens)
    
    print("처리된 텍스트: " + processed_text)

except sr.RequestError as e:
    print("Google 음성 인식 서비스에 연결할 수 없습니다: {0}".format(e))
except sr.UnknownValueError:
    print("Google 음성 인식에 실패했습니다. 마이크 연결을 확인해 주세요.")
except OSError as e:
    print("마이크 사용에 실패했습니다: {0}".format(e))
except Exception as e:
    print("알 수 없는 오류가 발생했습니다: {0}".format(e))
