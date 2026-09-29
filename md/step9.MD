# 목표
- RAG(Retrieval-Augmented Generation)
    - 검색 증강, LLM이 학습하지 않는 LLM 기준 외부 데이터(사용자 관점 사내 데이터 등)를 검색을 통해 정보를 제공받아 여기에 기존 프롬프트와 결합하여 LLM에게 추론 처리
    - 검색은 백터를 기반으로 진행 -> 데이터는 백터화 되어 백터 DB에 저장되어 있어야 함
    - LLM이 답변하기 전에 외부 지식에서 필요한 정보를 검색(Retrieval)하고, 그 정보를 근거로 답변(Generation) 하게 하는 방식
- Agent의 관점에서는 RAG는 Tool임
    - 도구를 사용하는 여부는
        - 규칙적 구성
        - 자율적 판단하게 구성
            - 정책 부여 : 사내 규정, 업무 지식등의 질문은 RAG를 사용하라는 등 

- RAG 기본 사용

# 구조
```
/
L steps
    L step9_rag_basic.py : 검색 증강 테스트용
L app
    L retrieval.py : 백터 DB에 검색(질문 전달, K개)후 결과 반호나 함수 제공
    L rag.py : 질문 -> 백터 DB 검색 -> 결과 + 프롬프트 -> LLM 추론 요청 -> 응답
```

# 실행
```
python -m 
```