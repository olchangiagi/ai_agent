# 목표
- 앞전 단계에서 프롬프트 -> 업무수행(LLM호출)을 하나의 에이전트로 가정
- 에이전트를 여러개 만들어 협업 -> A2A 표현
- LangChain의 Chain 단위 구성을 n개 구성하여 서로 상호 다른 작업을 진행하도록 구성
- 순차적 협업 패턴 진행
    - LangChain 완결되는 단위 -> 에이전트로 표현
    - 구성( 회차 제한)
        - 신입 개발자 에이전트
        - 전문 리뷰어 에이전트
        - 피드백 반영 에이전트
    - 완성된 코드를 개발

# 구조
```
/
L steps
    L step5_a2a_basic.py

```

# 실행 (응답 토큰은 1200으로 제한)
```
python -m steps.step5_a2a_basic

목표 사용자 비밀번호를 입력받아 DB에 저장하는 간단한 함수 (보안 고려)
==================================================

[신입 개발자] 코드 작성 중...
---
 ```python
import bcrypt
import sqlite3

def create_table():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id ... 
 (코드 생략) 
 ---

[전문 개발자] 코드 검토 중...
---
 # 코드 리뷰

전반적으로 bcrypt를 활용한 비밀번호 해싱 기본기는 잘 갖춰져 있습니다. 하지만 프로덕션 관점에서 몇 가지 중요한 문제가 있습니다.

## 🔴 보안 취약성

### 1. 커넥션 관리 및 예외 처리 미흡
`create_table()`, `verify_password()`에 `try/finally`가 없어 예외 발생 시 커넥션이 누수됩니다.

```python
def verify_password(username: str, input_password: str) -> bool:
    conn = sqlite3.connect('users.db')
    try:
        cur = conn.cursor()
        cur.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
        row = cur.fetchone()
    finally:
        conn.close()
    ...
```

### 2. username에 대한 입력 검증 부재
`save_user_password`에서 `plain_password`만 검증하고 `username`은 빈 문자열, None, 공백 등이 그대로 들어갈 수 있습니다.

```python
if not username or not username.strip():
    raise ValueError("사용자명은 필수입니다.")
```

### 3. 사용자 존재 여부 노출 (부분적 문제)
`print("이미 존재하는 사용자입니다.")` 는 콘솔 로그이므로 치명적이진 않지만, 만약 이 함수가 API 응답으로 그대로 노출된다면 **user enumeration 공격**에 취약해집니다. 지금 구조에서 실제 서비스로 확장 시 주의가 필요합니다.

### 4. bcrypt 72바이트 제한 미고려
bcrypt는 72바이트까지만 처리하고 이후는 잘립니다. 매우 긴 비밀번호에 대한 명시적 상한선 검증이 없습니다.

```python
if len(plain_password.encode('utf-8')) > 72:
    raise ValueError("비밀번호는 72바이트를 초과할 수 없습니다.")
```

## 🟡 비효율적인 부분

### 5. 매 함수 호출마다 새 커넥션 생성
매번 `sqlite3.connect()`를 호출하는 것은 소규모 스크립트에선 괜찮지만, 반복 호출이 많은 상황에선 비효율적입니다. 커넥션 풀링이나 컨텍스트 매니저 패턴을 고려하세요.

```python
from contextlib import contextmanager

@contextmanager
def get_connection():
    conn = sqlite3.connect('users.db')
    try:
        yield conn
    finally:
        conn.close()
```

## 🟡 스타일 가이드

### 6. DB 경로 하드코딩
`'users.db'`가 여러 곳에 중복 하드코딩되어 있습니다. 상수로 분리하세요.

```python
DB_PATH = 'users.db'
```

### 7. `print` 대신 `logging` 사용 권장
프로덕션 코드에서 `print`는 로그 레벨 제어, 파일 출력 등이 불가능합니다.

```python
import logging
logger = logging.getLogger(__name__)
...
logger.warning("이미 존재하는 사용자입니다: %s", username)
```

### 8. 타입 힌트 일관성
`create_table()`에 반환 타입 힌트(`-> None`)가 빠져 있습니다.

## ✅  ... 


[신입 개발자] 피드백 반영하여 수정 중...
최종 결과물
리뷰 감사합니다! 지적하신 부분들을 모두 반영해서 다시 작성했습니다. 특히 커넥션 누수와 72바이트 제한 부분은 미처 생각 못 했네요 😅

```python
import bcrypt
import sqlite3
import logging
from contextlib import contextmanager
from typing import Generator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_PATH = 'users.db'
BCRYPT_MAX_BYTES = 72
MIN_PASSWORD_LENGTH = 8


@contextmanager
def get_connection() -> Generator[sqlite3.Connection, None, None]:
    """DB 커넥션을 안전하게 생성하고 종료하는 컨텍스트 매니저"""
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()


def create_table() -> None:
    """users 테이블 생성 (없으면)"""
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        ''')
        conn.commit()


def _validate_username(username: str) -> None:
    """사용자명 유효성 검사"""
    if not username or not username.strip():
        raise ValueError("사용자명은 필수입니다.")


def _validate_password(plain_password: str) -> None:
    """비밀번호 유효성 검사 (길이, bcrypt 바이트 제한)"""
    if not plain_password or len(plain_password) < MIN_PASSWORD_LENGTH:
        raise ValueError(f"비밀번호는 최소 {MIN_PASSWORD_LENGTH}자 이상이어야 합니다.")

    password_bytes = plain_password.encode('utf-8')
    if len(password_bytes) > BCRYPT_MAX_BYTES:
        raise ValueError(f"비밀번호는 {BCRYPT_MAX_BYTES}바이트를 초과할 수 없습니다.")


def save_user_password(username: str, plain_password: str) -> bool:
    """비밀번호를 bcrypt로 해싱하여 DB에 저장"""
    _validate_username(username)
    _validate_password(plain_password)

    username = username.strip()

    # 비밀번호 해싱 (salt 자동 생성됨)
    hashed = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())

    with get_connection() as conn:
        cur = conn.cursor()
        try:
            cur.execute(
                'INSERT INTO users (username, password_hash) VALUES (?, ?)',
                (username, hashed.decode('utf-8'))
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            # 내부 로그로만 남기고, 외부(API 등)로는 일반화된 메시지만 노출해야
```