# 목표
- Langchain Tool 구성
- SQL 수행 TOOl, RAG TOOL, ... 향후 외부도구 연결(MCP)(노션, 슬렉, 카톡, 외부 s/w, 데스크톱 sw, 뱅킹)
- 도구 구성하여 에이전트가 자율적으로 판단하여 도구를 사용하도록 구성 -> Lang Graph 출현

# 구조
```
/
L app
    L tools
        L __init__.py
        L rag_tools.py      : rag를 도구로 사용할 수 있는 내용 적제 -> @tool
        L sql_tools.py      : sql을 도구로 사용할 수 있는 내용 적제 -> @tool
L steps
    L step11_tools.py       : 툴 사용 테스트 코드
L sql
    L migrations
        L 003_business.sql  : sql 툴을 위한 대상 테이블과 더미 데이터
```

# 테이블 추가 및 데이터 추가
```
python -m scripts.migrate

agentlab=# \dt
             List of relations
 Schema |       Name        | Type  | Owner 
--------+-------------------+-------+-------
 public | demo_vectors      | table | agent
 public | document_chunks   | table | agent
 public | documents         | table | agent
 public | orders            | table | agent
 public | products          | table | agent
 public | schema_migrations | table | agent
(6 rows)

agentlab=# select * from products;
 product_id |    product_name     |  category  |   price    |   cost    
------------+---------------------+------------+------------+-----------
          1 | AI 업무자동화 Basic | software   |   49000.00 |  12000.00
          2 | AI 업무자동화 Pro   | software   |   99000.00 |  25000.00
          3 | 데이터 분석 패키지  | service    |  150000.00 |  50000.00
          4 | 사내 AI Agent 구축  | consulting | 1200000.00 | 500000.00
          5 | RAG 구축 컨설팅     | consulting |  800000.00 | 320000.00
(5 rows)
```

# 실행
```
python -m steps.step11_tools

revenue=3586000.00, orders=8, range=2026-09-01~2026-09-05
1. 사내 AI Agent 구축: qty=1, revenue=1200000.00 
2. RAG 구축 컨설팅: qty=1, revenue=800000.00 
3. 데이터 분석 패키지: qty=4, revenue=600000.00 
[source=HR-LEAVE-2026 | hybrid=0.428]
# 연차휴가 운영 규정

[source=HR-TRAVEL-2026 | hybrid=0.263]
# 국내 출장비 규정

[source=HR-TRAVEL-2026 | hybrid=0.200]
출장 교통비는 회사가 승인한 실비를 기준으로 정산한다.

[source=HR-TRAVEL-2026 | hybrid=0.079]
식비는 별도 영수증 제출 없이 회사의 일비 기준으로 지급한다.

[source=HR-LEAVE-2026 | hybrid=0.073]
입사 1년 미만 직원은 근로한 기간과 사내 운영 기준에 따라 사용할 수 있는 휴가를 확인해야 한다.
```