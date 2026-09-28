'''
bedrock 임베딩 모델 생성, 재사용 모듈
텍스트 입력 -> 백터로 변환 처리시 사용할 수 있음
'''

from langchain_aws import BedrockEmbeddings
from .config import AWS_REGION, BEDROCK_EMBED_MODEL

# 싱글톤 스타일로 구성
_embeddings = None

def get_embeddings():
    global _embeddings
    if _embeddings:
        # 최소 1회만 초기화
        _embeddings = BedrockEmbeddings(model_id=BEDROCK_EMBED_MODEL, region_name=AWS_REGION)
    return _embeddings