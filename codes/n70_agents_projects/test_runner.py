from run_graph import graph

# 이 스크립트는 LangGraph 흐름을 터미널에서 테스트하기 위한 테스트 실행기입니다.
# Streamlit 없이도 상태 입력만으로 추천 전체 흐름을 실행할 수 있습니다.

# 🧪 테스트용 입력 상태 설정
test_input = {
    "user_input": "배고파",
    "location": "홍대"
}

# LangGraph 실행 및 결과 출력
print("🧠 LangGraph 실행 시작...\n")
try:
    events = list(graph.stream(test_input))  # 그래프 실행
    print("✅ 실행 완료. 단계별 상태:\n")

    # 각 단계별 상태 출력
    for i, e in enumerate(events):
        step_name = list(e.keys())[0]
        print(f"Step {i+1}: {step_name}")
        print(e, "\n")

    # 최종 요약 메시지 추출 (summarize_message 내부 또는 마지막 상태)
    final_state = events[-1].get("__end__") or events[-1]
    summary = final_state.get("summarize_message", final_state)
    final_message = summary.get("final_message", "추천 메시지가 없습니다.")

    print("📦 최종 추천 메시지:")
    print(final_message)

except Exception as e:
    print("❌ 실행 중 오류 발생:")
    print(str(e))
    
    