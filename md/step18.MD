# 목표
- 운영상에 세밀한 평가 및 LangChain, LangGraph 운영 모니터링 등 추적하기 위한 장치 필요
    - LangSmith 설정

# 세팅
- LangSmith 가입
    - https://smith.langchain.com/
    - 대시보드 -> 앱선택 -> tracing -> + Project 클릭 -> "ai-agent" 입력 후 생성
        - 키 생성 버튼 사용 -> .env 카피


# 구조
```
/
L steps
    L step18_observability.py
L app
    L observability.py          : LangSmith 상태 반환
```