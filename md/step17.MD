# 목표
- 검색 품질을 (직)감으로 판단하지 않고 반복 측정이 가능한 평가 데이터셋을 구성
- 질문, 답변 데이터 구성, 필요시 반복 수행
    - 질의 -> 결과 -> 해석 및 평가
    - 평가지표는 Mean reciprocal Rank(MRR, 평균 역순위)
    - RAG 검색 정확도 평가

# 구조
```
/
L app
    L evaluation
        L __init__.py           
        L dataset.py            : 테스트용 데이터셋
        L retrival_eval.py      : 평가
L steps
    L step17_evaluation.py      : 테스트 메인 코드
```