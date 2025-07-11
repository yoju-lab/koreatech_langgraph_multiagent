# LangGraph: 개념 및 그래프 접근법

## 1. 개념 설명

### LangGraph 소개
- **LangGraph란?** LangGraph는 LangChain에서 제공하는 **멀티 에이전트 오케스트레이션 프레임워크**입니다. 대형 언어 모델(LLM) 에이전트들을 **그래프 형태**로 연결하여 복잡한 작업을 수행하도록 설계되었습니다.
- **배경:** 하나의 LLM 에이전트로 해결하기 어려운 복잡한 문제를 여러 전문 에이전트로 분할해 협업시키는 아이디어에서 출발했습니다. LangGraph는 이러한 **다중 에이전트 시스템**을 체계적으로 구현하기 위한 도구입니다.
- **주요 목적:** 대화형 에이전트, 복잡한 태스크 자동화, 사용자 정의 LLM 파이프라인 등 **AI 워크플로우를 확장 가능**하게 구축하는 토대를 제공합니다.

### 철학과 배경 (Why LangGraph?)
- **멀티 에이전트 철학:** “혼자서는 어려운 일을 여럿이 분담하면 더 잘할 수 있다.” LangGraph는 **전문화된 에이전트들의 협업**을 통해 성능을 향상시키는 철학을 담고 있습니다. 한 에이전트가 모든 일을 다 하는 대신, 각 에이전트가 특정 역할에 집중하도록 분리합니다.
- **상태 기계 관점:** LangGraph의 그래프 접근법은 **상태 기계(State Machine)** 개념과 유사합니다. 각 에이전트 노드는 하나의 상태처럼 동작하고, 에이전트 간 전이는 상태 전이처럼 관리됩니다. 이러한 **구조적 설계**를 통해 복잡한 상호작용을 체계적으로 제어할 수 있습니다.
- **배경 및 등장:** Autogen, CrewAI 등 다양한 멀티 에이전트 프레임워크가 등장하는 가운데, LangChain 팀은 LangGraph를 통해 **그래프 기반 멀티 에이전트 워크플로우**의 이점을 강조했습니다. 이는 **유연한 흐름 제어**와 **공유 상태 관리**를 지원하여 기존 연속 실행(seq2seq) 방식의 한계를 보완합니다.

### 그래프 구조 – 노드(Node)와 엣지(Edge)
- **노드 (Node):** 그래프의 노드는 각각 **독립된 에이전트**를 나타냅니다. 각 에이전트는 자체 프롬프트, LLM 모델, 그리고 전용 **도구(tool)**들을 가질 수 있습니다. 예를 들어, 정보 검색을 담당하는 에이전트, 코드 실행을 담당하는 에이전트 등이 노드가 됩니다.
- **엣지 (Edge):** 노드 간 **이동 경로**를 나타냅니다. 한 에이전트의 출력이 어느 다음 에이전트로 전달될지를 결정합니다. 엣지는 **방향성**을 가지며, **조건부 제어**가 가능합니다. 즉, 현재 상태나 메시지 내용에 따라 다른 경로를 선택할 수 있습니다 (분기/반복 구현 가능).
- **그래프 vs 순차 체인:** 전통적인 체인(chain)은 고정된 순서를 따르지만, **그래프 구조**에서는 유연한 경로 선택과 **분기/병렬 흐름**이 가능합니다. 이를 통해 **복잡한 워크플로우**를 자연스럽게 표현할 수 있습니다.

### 상태 기반 에이전트 설계
- **공유 상태 (State):** LangGraph의 핵심은 에이전트들 사이에 공유되는 **그래프 상태**입니다. 이 상태에는 대화 메시지, 중간 결과, 기타 컨텍스트 데이터가 포함됩니다. 모든 에이전트 노드는 이 **공용 메모리**를 통해 서로 소통합니다.
- **에이전트 실행 모델:** 각 에이전트 노드는 자신의 역할에 맞는 **LLM 프롬프트**를 받아 상태를 처리하고, 새로운 정보를 상태에 추가합니다. 예를 들어, ‘검색’ 에이전트는 질문을 받아 검색 결과를 상태에 추가하고, ‘답변’ 에이전트는 상태에 있는 검색 결과를 읽어 답을 생성합니다.
- **상태 업데이트와 전이:** 에이전트가 작업을 마치면 상태(예: 메시지 목록, 작업 완료 플래그 등)를 갱신하고, **다음으로 어느 노드로 이동할지 결정**합니다. LangGraph에서는 이 전이를 쉽게 정의할 수 있으며, 각 노드의 실행이 끝날 때 **어떤 상태이면 어느 노드로 이동**같은 로직을 구현합니다. (예: 상태에 `sender="Researcher"`이면 다음은 `Chart Generator` 노드로 등)

### 메시지 흐름과 제어 흐름
- **메시지 전달:** LangGraph 그래프의 동작 흐름은 **메시지 패싱**으로 이해할 수 있습니다. 사용자의 입력 메시지가 그래프에 들어오면, **엔트리 노드(entry point)** 에이전트가 이를 받아 처리합니다. 그 에이전트의 출력 메시지가 그래프 상태에 추가되고, 정의된 엣지를 따라 다음 에이전트로 전달됩니다.
- **제어 흐름:** 엣지에는 **조건부 로직**을 부여할 수 있습니다. 예를 들어, 특정 에이전트의 출력 내용에 따라 **다른 에이전트로 분기**하거나 **그래프 실행을 종료(END)**할 수 있습니다. 별도의 “라우터(router)” 에이전트를 두어 메시지 내용을 해석하고 다음 경로를 결정하기도 합니다. 이를 통해 동적 의사결정이 가능한 워크플로우를 구현합니다.
- **예시 – Router 패턴:** 하나의 라우터 노드가 전체 메시지 내용의 맥락을 보고 “계속 진행”, “도구 호출”, “종료” 등의 신호를 결정하면, 각 신호에 대응되는 다음 노드로 이동합니다. 예컨대, **계속 진행**이면 다음 전문 에이전트로, **도구 호출**이면 외부 툴 실행 노드로, **종료**이면 END로 가는 식입니다. (이와 같은 구조로 에이전트 간 협업을 **유연하게 제어**합니다.)

### 실무 적용 고려사항
- **종료 조건 설정:** 멀티 에이전트 시스템은 잘못하면 무한 루프에 빠질 수 있습니다. **그래프 종료 조건(END)**을 명확히 정의해야 합니다. 예를 들어, 에이전트가 “최종 답변”이라는 특별 신호를 출력하면 그래프를 종료시키는 규칙을 두어야 합니다.
- **프롬프트 설계:** 각 에이전트에 **명확한 역할 지시**를 하는 프롬프트를 작성해야 합니다. 에이전트들이 공유 상태를 활용하면서도 자신의 책임만 수행하도록 지침을 줍니다. 예를 들어, 한 에이전트는 “질문을 분석하여 검색어 생성”, 다른 에이전트는 “검색 결과로부터 답 생성” 식으로 구체적인 지시가 필요합니다.
- **오버헤드와 비용:** 여러 에이전트가 순차/병렬로 LLM을 호출하므로 **API 호출 비용**과 **응답 지연**이 늘어날 수 있습니다. 실무 적용 시에는 필요한 최소한의 에이전트로 구성하고, 각 호출에 타임아웃 등의 제어를 넣어 **효율성**을 관리해야 합니다.
- **디버깅과 모니터링:** 그래프 구조상 흐름이 복잡해질 수 있으므로, **중간 상태 로깅**이나 **시각화**가 중요합니다. LangGraph로 실행되는 동안 어떤 경로를 거쳤는지, 각 노드의 입력/출력은 무엇이었는지 추적하는 것이 디버깅에 도움이 됩니다. (전문 도구: Langfuse 등 모니터링 솔루션 참고)
- **모델 한계 및 상호작용:** 각 에이전트는 LLM의 한계를 지닙니다. 예를 들어, 정보를 검색했지만 잘못 이해하거나, 두 에이전트가 같은 정보에 대해 상충된 결과를 낼 수 있습니다. 이러한 경우를 대비해 **휴먼 인터벤션(human-in-the-loop)**이나 추가 검증 단계를 그래프에 포함시키는 것도 고려해야 합니다.

### 활용 사례 및 마무리
- **QA 시스템:** 사용자의 질문을 받아 **검색 에이전트**가 웹에서 자료를 찾고, **답변 에이전트**가 결과를 요약하여 답변하는 시스템. 예를 들어 하나의 에이전트가 “서울 인구 검색”, 다음 에이전트가 “검색 결과로 답 생성” 형태로 협업합니다.
- **코드 생성 협업:** **코드 작성 에이전트**와 **코드 검토 에이전트**가 번갈아 작동하여 고품질 코드를 산출합니다. 작성자가 코드를 생성하면 검토자가 오류를 지적하고 수정 요청을 하며, 다시 작성자가 개선하는 **반복 루프**를 그래프를 통해 구현할 수 있습니다.
- **문서 요약 파이프라인:** 긴 문서를 **분할 요약 에이전트**가 부분 요약하고, **통합 요약 에이전트**가 이를 종합하여 최종 요약을 생성합니다. 이처럼 요약 작업을 단계별 에이전트로 분리하면 매우 긴 입력도 효율적으로 처리 가능합니다.
- **그 외 응용:** 대화형 비서에서 질의 유형에 따라 여러 전문 에이전트(예: 일정 관리, 이메일 작성)를 전환하며 처리하거나, 복잡한 문제를 해결하기 위해 **계획 수립 에이전트**가 하위 작업을 **전문 에이전트 팀**에 할당하는 등 다양하게 활용됩니다. LangGraph의 **그래프 접근법**은 이러한 확장적인 시나리오를 효과적으로 지원합니다.
- **마무리:** LangGraph를 활용하면 멀티 에이전트 서비스를 **구조적이고 안정적으로 설계**할 수 있습니다. 그래프 노드 간의 흐름을 명시적으로 관리함으로써 예측 가능성을 높이고, 각 에이전트를 모듈화하여 개발과 유지보수를 용이하게 합니다. 앞으로 실습을 통해 LangGraph 사용법을 익혀보겠습니다.

