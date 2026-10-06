'''
- 하네스를 적용하여 에이전트 작동시키는 테스트 코드
'''
# 기능 확인
from app.main import run
import asyncio

async def main():
    result = await run("2026년 9월 매출을 요약해줘.")
    final = result.get('final')
    print(final.answer if final else result["messages"][-1].content)

asyncio.run(
    main()
)