# 목표
- Agent Memory
- PostgreSQL + pgvector 방식으로 지식 저장 (현재) + memory 저장소 활용
- Memory 저장소를 활용하면 짧은 답변, 기존 질문에 대한 답변을 메모리에서 확인하여 LLM 사용 없이 응답 가능한 구조 구성 -> 중요도 관리 -> 토큰 비용(운영비) 절감 도움
- 장기기억 활용

- 역할
    - LLM: 판단, 답변을 담당 두뇌
    - RAG: 회사 문서, 규정등 LLM이 모르는 정보
    - DB: 실제 데이터들 저장, 조회
    - MEMORY: 사용자의 맥락 이해, 패턴 기억 -> 사용자 주의, 답변형태, 업무 형태, 기억포인트 등등 저장 -> 사용자 질문시 해당 내용을 기반으로 답변할 때 제공
        - 사용자의 선호하는 방식으로 답변을 구성하게 도움
        - LLM이 추론을 할 때, 사용자가 누구이고, 어떤 업무를 하고, 어떤 방식으로 답변 받기를 원하는지 삽입(프롬프트)
        - LLM이 사용자를 처음 만난 사람처럼 행동하지 말고, 과거의 중요한 정보(맥락)을 제공하는 역할 담당

# 구조
```
/
L sql
    L migrations
        L 005_memory.sql    : 사용자의 정보를 저장하는 테이블, 검색
L app
    L tools
        L memory_tools.py   : sql 역할 담당, 기능적으로 메모리 역할
    L agent
        L graph             : tool 등록
L steps
    L step14_memory.py      : 메모리 테스트
L .env                      : 사용자 ID 더미 구성
```

# 오류 조치
```
# 005 실행 로그 삭제 -> psql에서 진행
delete from schema_migrations where name='005_memory.sql';

# agent_memories 삭제
drop table agent_memories;

# sql 실행 -> 터이널 에서 진행
python -m scripts.migrate

# demo() 주석 모두 해제
step14_memory.py

# 프로그램 실행
python -m steps.step14_memory

```