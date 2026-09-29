'''
- fixed-size 단위 청킹 처리 모듈
- 최대 길이는 700 설정(글저수), 토큰 최대는 1024이므로, 범위안에 여유롭게 들어옴
- 청킹의 trade-off
    - chunk가 작으면 검색 정밀도 상승, 하지만 문맥이 잘릴 수 있음
    - chunk가 크면 문맥 보전 상승, 하지만 불필요한 내용 포함 가능
- chunk 사이즈는 rag 성능의 하이퍼파라미터 -> 검색 평가를 통해서 최적 크기를 결정
- 고정크기 -> overlap -> token 기반 -> 시멘틱/구조 기반 청킹 or 청킹 에이전트 개발 반영
'''

def splite_text(text:str, max_chars:int = 700):
    # 청크별로 모으는 그릇, 현재 순서상 문서 데이터
    chunks, current_doc = [], ""
    # \n\n을 기준으로 분할 -> 문서마다 상이함
    # print(text.split('\n\n'))
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()] # 공백 제거 처리, 노이즈 제거

    # 순회 하면서 청킹 처리
    for p in paragraphs:
        # 1. 청킹 후보 (현재 보관 문서 + 줄바꿈 + 하나씩 뽑아낸 문단)
        candidate_doc = (current_doc + "\n\n" + p).strip()
        # 2. 청킹 후보에 대한 길이 확인(청킹의 분할 기준이 문자수 = 700)
        if current_doc and len(candidate_doc) > max_chars:
            # 3. 청크에 추가 -> 청크 1개 확정
            chunks.append(current_doc)
            # 4. 리셋
            current_doc = p
        else:
            # 현재 보관문서에 후보군 문서 설정
            current_doc = candidate_doc 

    # 마지막까지 다 확인을 해도 마지막에서 700을 넘기지 못했다면 남은 문단이 존재
    if current_doc:
        chunks.append(current_doc)

    # 청크 묶음 반환
    return chunks


