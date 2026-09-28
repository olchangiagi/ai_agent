# 목표
- Langchain 이해, 간단 chain 구성, LLM 호출
- Chain 구성
    - 프롬프트 구성 -> LLM 호출
    - 해당 구성은 향후 복잡한 Agent 구성으로 확장 가능

# 구조
```
/
L app
    L llm.py    : LLM 모듈
L steps
    L step4_langchain_basic.py  : 체인 구성 (prompt, LLM)
```