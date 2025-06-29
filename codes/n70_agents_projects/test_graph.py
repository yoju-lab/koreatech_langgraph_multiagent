import pytest
from run_graph import graph

# pytest에서 공통으로 사용할 기본 입력 상태 설정
@pytest.fixture
def base_state():
    # 테스트에 사용할 간단한 상태 값 (입력 문장과 지역 정보)
    return {
        "user_input": "배고파",   # 추천 흐름 시작용 입력 문장
        "location": "홍대"       # 테스트용 지역
    }

# LangGraph 실행 테스트 함수
def test_graph_execution(base_state):
    # LangGraph 실행: 상태를 기반으로 전체 흐름을 순차적으로 실행
    events = list(graph.stream(base_state))

    # 실행 결과는 리스트 형태여야 하며, 1개 이상 단계가 있어야 함
    assert isinstance(events, list)
    assert len(events) > 0

    # 최종 상태 추출 (마지막 단계 또는 __end__ 키 기준)
    final_state = events[-1].get("__end__") or events[-1]
    summary = final_state.get("summarize_message", final_state)

    # 최종 메시지가 존재해야 함
    assert "final_message" in summary
    assert isinstance(summary["final_message"], str)

    # 결과 메시지 콘솔에 출력
    print("\n✅ 요약 메시지:")
    print(summary["final_message"])
    
    