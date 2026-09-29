# 목표
- PostgreSQL(Docker compose) / pgvector + bedrock embedding
- PostgreSQL (RDB)에 extension을 설치하여 백터를 컬럼의 타입으로 사용 가능하게 확장
    - 테이블내 특정 컬럼이 백터를 저장할 수 있도록 구성
    - RDB 기능, 백터DB기능 같이 사용 가능

# 구성
```
/
L docker-compose.yml
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
```