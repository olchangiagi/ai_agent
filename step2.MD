# 목표
- AWS Bedrock을 이용하여 LLM 직접 호출
```
AWS 인증 -> Bedrock Runtime Client 생성 -> LLM에 프롬프트 전달 -> 응답 파싱
```

# 구조
/
L app/              : 모듈(타 프로젝트에서도 사용 가능하게 구조화)
    L bedrock.py    : Bedrock Runtime Client 생성
    L config.py     : 프로젝트 전체 환경변수 총괄 관리(.env 로드, 추가)
L steps/
    L step2_bedrock_llm_call.py : LLM 호출 및 응답 처리

# 실행
```
python -m steps.step2_bedrock_llm_call

# AI Agent 5줄 설명

1. **AI Agent**는 스스로 목표를 인식하고 이를 달성하기 위해 계획을 세우는 인공지능 시스템입니다.

2. 단순히 질문에 답하는 것을 넘어, **주변 환경을 인식(Perception)**하고 상황을 판단합니다.

3. 판단한 내용을 바탕으로 **자율적으로 행동(Action)**을 결정하고 실행합니다.

4. 필요한 경우 **도구(Tool)나 API를 활용**하여 검색, 계산, 코드 실행 등 실제 작업을 수행합니다.

5. 결과를 관찰하고 피드백을 받아 **다음 행동을 조정**하며, 최종 목표를 달성할 때까지 이 과정을 반복합니다.
```