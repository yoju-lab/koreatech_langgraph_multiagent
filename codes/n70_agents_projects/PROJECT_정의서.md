
# 📘 프로젝트 정의서: 아, 뭐 먹지? 뭐 하지?

---

## ✅ 프로젝트 개요

**"아, 뭐 먹지? 뭐 하지?"**는 GPT 및 LangGraph를 기반으로 사용자의 자연어 입력을 분석하고,  
현재 시간, 계절, 날씨를 고려하여 적절한 **음식 또는 활동을 추천**하는 스마트 개인 비서형 AI 서비스입니다.

사용자는 단순히 `"배고파"`, `"심심해"`, `"뭐하지?"` 와 같은 자연어를 입력하면,  
GPT가 이를 이해하고 추천 흐름을 자동으로 제어합니다.

---

## 🎯 목표

- 자연어 기반 상황 분석 및 의도 분류
- 실시간 조건(날씨, 시간대, 계절)에 맞춘 개인화 추천
- 음식/활동 → 장소 검색 → 감성 요약까지 완결된 추천 서비스 구현
- 초급자도 이해할 수 있는 LangGraph 기반 구조 실습 지원

---

## 🧩 기술 스택

| 항목 | 사용 기술 |
|------|-----------|
| LLM 기반 추천 | GPT-4o (via `langchain-openai`)  
| 흐름 제어 | LangGraph  
| 웹 UI | Streamlit (옵션)  
| 외부 API | Kakao Local API, OpenWeather API  
| 환경 구성 | Python 3.12, `.env`, `python-dotenv`  

---

## 🧠 주요 기능

| 기능 | 설명 |
|------|------|
| Intent 분류 | 입력 문장을 `food`, `activity`, `unknown` 으로 분류  
| 시간대 감지 | 현재 시각 → `"아침", "점심", "저녁", "야간"`  
| 계절 감지 | 현재 월 → `"봄", "여름", "가을", "겨울"`  
| 날씨 확인 | OpenWeather API를 통해 날씨 (`Rain`, `Clear` 등) 추출  
| 음식/활동 추천 | 조건 기반으로 GPT 추천 2가지 생성  
| 장소 검색 | Kakao API로 추천 항목 기반 장소 추천  
| 감성 메시지 생성 | 최종 결과를 요약 문장으로 생성해 사용자에게 출력  

---

## 🗂 에이전트 구성

| 에이전트 | 설명 |
|----------|------|
| `classify_intent` | 입력 문장 분석 → 추천 흐름 분기  
| `get_time_slot` | 시간대 추출 (5~11: 아침 등)  
| `get_season` | 월 기준 계절 추출  
| `get_weather` | 날씨 API 호출 → 현재 날씨 추출  
| `recommend_food` | GPT로 음식 추천 2개 생성  
| `recommend_activity` | GPT로 활동 추천 2개 생성  
| `generate_search_keyword` | 검색 키워드 (예: 한식, 북카페 등) 생성  
| `search_place` | Kakao API로 장소 추천  
| `summarize_message` | 최종 안내 문장 생성  
| `intent_unsupported_handler` | 추천 불가 시 graceful 종료 메시지 제공  

---

---

## 🚀 실행 및 접속 방법

### 1. Web UI 실행 (`app.py`)
- **역할**: 사용자가 지역과 기분을 입력하고 추천 결과를 실시간으로 확인할 수 있는 Streamlit 기반 웹 인터페이스입니다.
- **실행 방법**:
  ```bash
  streamlit run app.py
  ```
- **접속 방법**: 실행 후 터미널에 표시되는 URL(기본값: `http://localhost:8501`)로 브라우저에서 접속합니다.

### 2. LangGraph 핵심 로직 (`run_graph.py`)
- **역할**: 전체 추천 서비스의 '두뇌' 역할을 하는 오케스트레이터입니다. 각 에이전트(의도 파악, 시간/날씨 확인, 추천 등)를 연결하는 상태 그래프(State Graph)를 정의하고 컴파일합니다.
- **실행 방법**: 
  - 본 파일은 라이브러리 형태로 설계되어 `app.py`나 `test_runner.py`에서 임포트되어 실행됩니다.
  - 단독 로직 테스트를 원할 경우 `test_runner.py`를 실행하십시오.

---

## 🧪 테스트 및 실행 스크립트

- **Web UI 실행**: `streamlit run app.py`
- **터미널 로직 테스트**: `python test_runner.py`
- **단위 테스트(Pytest)**: `pytest test_graph.py`

---

## 👨‍🏫 수업 활용 안내

- 각 에이전트별 `.ipynb` 실습 파일 제공 (설명 + 주석 포함)
- 테스트 스크립트 및 UI 코드 주석화 제공
- 수업 난이도 조절 가능: LangGraph 흐름 → 각 노드 실습

---

## 📂 프로젝트 구성 파일 예시

```
📦 ah-mwo-meokji (codes/n70_agents_projects/)
├── agents/
│   ├── intent.py
│   ├── time.py
│   ├── season.py
│   ├── weather.py
│   ├── food.py
│   ├── activity.py
│   ├── keyword.py
│   ├── place.py
│   ├── summary.py
│   └── intent_unsupported.py
├── run_graph.py
├── app.py
├── test_runner.py
├── test_graph.py
../.env
```

---

## ✨ 확장 아이디어

- `"다른 음식 추천해줘"` → 대화형 흐름 확장
- 지도 시각화 / 추천 기록 저장
- 사용자 피드백(👍/👎) 수집 및 반영
- 대화형 Web UI 구성 (Streamlit Chat)

---


