# 목표
- LangGraph + bedrock + LangChain + tools
- LangGraph
    - StateGraph -> Agent -> ToolNode -> Agent 순환 루프 구성하는 자율형 에이전트 기본 구성
    - Reason/Tool/Observe 루프 구성
- 질의 -> 적절한 Tool을 LLM이 선택하고, Tool을 사용, 결과를 이용하여 관찰 -> 최종 답변까지 반복 진행 체크


# 구조
```
/
L app
    L agent
        L __init__.py
        L graph.py      : LangGraph 구성 (노드를 추가하는 등 구성)
        L prompts.py    : Agent의 프롴프트
        L state.py      : 상태 관리
    L main.py           : Agent 구동
L steps
    L step12_langgraph_agent.py : 테스트 코드
``` 

# 실행
```
python -m steps.step12_langgraph_agent
```