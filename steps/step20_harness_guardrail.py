'''
- 하네스를 적용하여 에이전트를 작동시키는 테스트 코드
'''

# 리소스 한도 -> DataClass 데코레이터 사용
from dataclasses import dataclass
# 시간 한도
import time
# 툴 사용 한도 -> 툴 사용 목록 제한
ALLOWED_TOOLS = {"sales_summary", "top_products", "refund_summary", "search_company_policy", "remember_user_preference", "recall_user_memory", "get_exchange_rate"}