'''
프로그램 전체 환경변수 로드, 관리
'''
import os
from dotenv import load_dotenv

# 환경변수 로드(.env)
load_dotenv() # 환경변수 설정 완료(os 레벨)

# 변수로 사용
# .enb -> load_dotenv() -> os단 환경변수 자동 세팅
# os.getenv(키값, 누락시 사용)
AWS_REGION = os.getenv('AWS_REGION', 'us-east-1') # 리전
BEDROCK_CHAT_MODEL = os.getenv('BEDROCK_CHAT_MODEL', 'us.anthropic.claude-sonnet-5') # LLM 모델
BEDROCK_EMBED_MODEL = os.getenv('BEDROCK_EMBED_MODEL', 'amazon.titan-embed-text-v2:0') # 임베딩 모델, 토크나이저(api용 사용)
DATABASE_URL = os.getenv('', '') # 백터 DB 주소