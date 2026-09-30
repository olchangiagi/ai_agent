'''
- 기본 RAG 
    - 질문 고정 -> 청크 검색(백터 DB) -> 유사도순 랭킹(top k개 획득) -> 프롬프트 + 검색 내용 -> LLM 호출
'''
from app.retrieval import vector_search
from app.rag import answer

# q = '상품 자체 하자는 언제까지 환불할 수 있나요?' 
q = '입사 6개월차 신입 개발자입니다. 연차 사용 가능한가요?'

# for chunk in vector_search(q, 3):
#     print(chunk)

print(answer(q))