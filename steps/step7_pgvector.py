'''
텍스트 -> 임베딩 하여 생성된 백터 데이터를 PostgreSQL pgvector에 저장하고, 유사도 검색 SQL 실행
'''

# 1. 모듈 가져오기
from pgvector import Vector
from app.embedding import get_embeddings
from app.database import connect

# 2. 검색어로 사용될만한 샘플 문장 준비 (hr, sales, cs)
samples = ["환불정책", "연차 휴가 규정", "월 매출 분석"]

# 3. 임베딩 : [[...], [...], [...]]
vectors = get_embeddings().embed_documents(samples)

# 4. DB 쿼리 수행
with connect() as conn, conn.cursor() as cur: # with문 2개 사용과 동일
    # 데이터: 원문 텍스트, 임베딩된 백터
    for text, vec in zip(samples, vectors):
        # print(text, vec)
        # SQL 실행
        cur.execute("""
            insert into demo_vectors(content, embedding) values (%s, %s)
            on conflict(content)
            do update set embedding = EXCLUDED.embedding
        """, (text, Vector(vec)))
        # break
    conn.commit()
    pass