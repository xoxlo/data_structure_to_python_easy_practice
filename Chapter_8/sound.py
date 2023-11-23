import speech_recognition as sr
import pyaudio
import wave
from playsound import playsound

def recognize_speech():
    # 음성인식 객체 생성
    recognizer = sr.Recognizer()

    try:
        # 마이크에서 오디오 캡처
        with sr.Microphone() as source:
            print("말하세요...")
            audio = recognizer.listen(source, timeout=5)

        # Google 음성인식 API를 사용하여 텍스트로 변환
        text = recognizer.recognize_google(audio, language="ko-KR")
        print("인식된 텍스트:", text)
    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
    except sr.RequestError as e:
        print(f"Google 음성인식 API에 접근할 수 없습니다. 오류: {e}")

if __name__ == "__main__":
    recognize_speech()
