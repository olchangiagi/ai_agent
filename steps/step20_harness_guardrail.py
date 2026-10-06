'''
- 하네스를 적용하여 에이전트를 작동시키는 테스트 코드
'''

# 리소스 한도 -> DataClass 데코레이터 사용
from dataclasses import dataclass
# 시간 한도
import time
# 툴 사용 한도 -> 툴 사용 목록 제한
ALLOWED_TOOLS = {"sales_summary", "top_products", "refund_summary", "search_company_policy", "remember_user_preference", "recall_user_memory", "get_exchange_rate"}

# 에이전트 실행시 허용할 한도 -> 값으로 세팅
@dataclass
class Limits:
    max_tool_rounds: int = 6 # 최대 tool 실행 라운드 횟수
    max_seconds :float = 120.0 # 최대 전체 실행 시간(초단위)
    # ... 필요한 제한값 추가

# 에이전트가 사전에 정한 한도를 넘지 않도록 관리
class Budget:
    def __init__(self, limits:Limits|None):
        # 인스턴스 맴버 세팅
        self.limits = limits or Limits()
        # 정확한 시간 측정을 위해서 프로그램에 영향을 받지 않는 함수 사용
        self.started = time.monotonic()
        # 툴 사용 라운드 관리
        self.tool_rounds = 0
    
    # Tool 실행 할 때마다 횟수, 경과 시간 검사
    def consume_tool_round(self):
        # 툴 사용 -> 라운드 1회 증가
        self.tool_rounds += 1
        # checking
        if self.tool_rounds > self.limits.max_tool_rounds:
            raise RuntimeError("툴 사용 제한 횟수 초과")
        if time.monotonic() - self.started > self.limits.max_seconds:
            raise RuntimeError("실제 실행 시간 제한 초과")

        pass
