'''
- 메타데이터와 본문(규정) 분리
'''

from pathlib import Path
import yaml

def load_markdown(path:Path):
    '''
    returns
        - meta data (dict 형태 등)
        - body 본문 규정 데이터(텍스트, 문자열)
    '''
    # 1. markdown 전체 읽은 후 yaml 프런트 포멧터가 존재하는지 확인
    text = path.read_text(encoding = 'utf-8')
    # print(text)
    # 2. 구분자 체크(---)
    if not text.startswith('---'):
        return {}, text
    # 3. '---' 최대 2회만 분할
    _, meta, body = text.split('---', 2)
    # print(meta)
    # print('-' * 30)
    # print(body)
    # 4. 반환(dict, text)
    # yaml.safe_load() -> 키:값..... -> 안전하게 파싱 -> dict 반환
    return yaml.safe_load(meta) or {}, body.strip()