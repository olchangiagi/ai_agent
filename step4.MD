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

# 실행
```
python -m steps.step4_langchain_basic

# LangChain Runnable 파이프라인

## 핵심 개념

LangChain의 `Runnable`은 **LCEL(LangChain Expression Language)**의 기반이 되는 표준 인터페이스입니다. `|` (파이프) 연산자로 컴포넌트들을 체이닝하여 데이터 흐름을 구성합니다.

**핵심 특징:**
- 모든 컴포넌트(Prompt, LLM, Parser 등)가 동일한 인터페이스(`invoke`, `stream`, `batch`) 지원
- Unix 파이프처럼 왼쪽 출력이 오른쪽 입력으로 자동 전달
- 병렬 처리, 스트리밍, 비동기 처리를 기본 지원

## 예시: 간단한 질의응답 체인

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. 각 컴포넌트 정의
prompt = ChatPromptTemplate.from_template(
    "당신은 {role} 전문가입니다. 질문: {question}"
)
model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

# 2. Runnable 체인 구성 (| 연산자로 연결)
chain = prompt | model | parser

# 3. 실행
result = chain.invoke({
    "role": "AI",
    "question": "LangChain이 뭔가요?"
})

print(result)
```

## 데이터 흐름 설명

```
{"role": "AI", "question": "..."}
        ↓
   [prompt] → ChatMessage 생성
        ↓
   [model]  → LLM 응답 (AIMessage)
        ↓
   [parser] → 순수 문자열 추출
        ↓
   최종 결과 (str)
```

## 추가 활용 포인트

| 메서드 | 용도 |
|--------|------|
| `chain.invoke()` | 단일 실행 |
| `chain.stream()` | 토큰 단위 스트리밍 |
| `chain.batch([...])` | 여러 입력 병렬 처리 |
| `chain.ainvoke()` | 비동기 실행 |

**장점**: 코드가 선언적이고 간결해지며, 각 단계를 독립적으로 테스트/교체하기 쉽습니다. 복잡한 RAG나 Agent 파이프라인도 이 패턴의 확장으로 구성됩니다.
```