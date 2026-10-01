# 목표
- LangGraph + 정형 데이터(postgreSQL) + 비정형 데이터(pgvector) 같이 추론의 지식으로 사용
- 환불 통계 (SQL tool)와 환불 정책(Rag tool)을 한 질문에서 함께 처리/사용

# sql
- 환불 통계를 위한 sql 처리
```
python -m scripts.migrate
```

# 구조
```
/
L app
    L tools
        L sql_tools.py          : 추가로 특정 날짜내에 환불 요청 건수, 금액, 사유 등 조회
L steps
    L step13_sql_rag_agent.py   : 질문을 가지고 LLM 추론 진행
```