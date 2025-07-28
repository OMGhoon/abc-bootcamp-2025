from dotenv import load_dotenv
from ai import get_personality_analysis

load_dotenv()

print("# AI 관상가입니다. 얼굴 특징을 입력해주시면 성격과 미래를 전망래드릴게요.")
line = input("성격 특징 : ").strip() #White spaces (space, tab, new line, carrgort) 제거
#print(repr(line))

if not line:
    print("에러: 얼굴 특징을 입력하지 않으셨습니다.")
else:
    print("입력하신 얼굴 특징 : ", line)
    print("분석 중...")
    result = get_personality_analysis(line)
    print("분석 완료")
    print(result)

# get_personality_analysis()