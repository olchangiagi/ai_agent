# 목표
- PostgreSQL(Docker compose) / pgvector + bedrock embedding
- PostgreSQL (RDB)에 extension을 설치하여 백터를 컬럼의 타입으로 사용 가능하게 확장
    - 테이블내 특정 컬럼이 백터를 저장할 수 있도록 구성
    - RDB 기능, 백터DB기능 같이 사용 가능

# 구성
```
/
L docker-compose.yml
L app
    L database.py   : PostgreSQL 접속 커넥션 구성
L steps
    L step7_pgvector.py : 간단한 텍스트(문장)을 테이블 upsert(insert or update) 처리
```

# DB 구성
```
# DB 설치
docker compose up -d

# 연결정보 추가 (postgresql://agent:agent@localhost:5432/agentlab)
.env
app.config.py
```

# 초기 SQL 구성
```
/
L sql
    L migrations
        L 001_pgvector.sql
```

# 테이블 구성 및 초기 작업 
```
python -m scripts.migrate
```

# 확인
```
docker exec -it agent-postgres psql -U agent -d agentlab

# 생성된 schema 확인
\dt 
```

# 실행
```
python -m steps.step7_pgvector

환불정책 [-0.04075682908296585, 0.05940452963113785, -0.0009199480409733951, 0.014628028497099876, 0.01272689737379551, -0.032051026821136475, -0.028891494497656822, -0.03559470176696777, -0.012341924011707306...]
```

# 쿼리를 통해 데이터 확인
```
agentlab=# select id, content from demo_vectors;

 id |    content     
----+----------------
  1 | 환불정책
  2 | 연차 휴가 규정
  3 | 월 매출 분석

select 
    id, content,
    left(embedding::text, 14) || '...' as embadding
from demo_vectors; 

 id |    content     |     embadding     
----+----------------+-------------------
  1 | 환불정책       | [-0.04075683,0...
  2 | 연차 휴가 규정 | [-0.041086007,...
  3 | 월 매출 분석   | [-0.06644361,-...
(3 rows)
```

# 실행
```
(agent) PS C:\Users\olcha\workspace\ai_agent> python -m steps.step7_pgvector
('환불정책', 0.13430795073509216) <- cs 관련 샘플에서 가장 높은 점수를 얻음
('월 매출 분석', 0.11051657795906067)
('연차 휴가 규정', 0.013668003375411297)
```
