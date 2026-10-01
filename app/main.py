'''
LangGraph기반 Agent를 실행하는 코드
'''
import asyncio
from app.agent.graph import build_graph

async def run(query: str):
    '''
        사용자 질문 -> LangGraph 기반 Agent 전달
    '''
    result = await build_graph().ainvoke(
        # 사용자 메세지를 구성(상태내 messages키값으로), 라운드(llm 호출횟수) 0으로 세팅 -> AgentState 기본구성하여 호출
        {"messages":[("user", query)], "rounds":0}, 
        # 전체 순환 회수 제한
        config = {"recursion_limit":18}
     ) # 초기 상태를 설정하여 그래프에게 전달

    # 전체 맥락(상태의 변화들의 기록)
    print(result["messages"])

    # 최종 답변(LLM)
    print("+"*30)
    print("[최종 답변]\n\n", result["messages"][-1].content)
    print("+"*30)