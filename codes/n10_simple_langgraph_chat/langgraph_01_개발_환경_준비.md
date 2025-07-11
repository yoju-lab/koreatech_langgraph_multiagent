# 개발 환경 준비

## 1. 개발 환경 준비 가이드

본 과정의 실습은 Windows 11 환경애서 Python 실행 환경과 IDE를 설정해야 합니다. 여기서는 **Miniconda**, **conda 가상환경**, 그리고 **VS Code**를 활용하여 AI 도구까지 사용할 수 있는 개발 환경을 구축하는 방법을 설명합니다.

### Miniconda 설치 및 conda-forge 설정

**Miniconda**는 Python과 패키지 관리자(conda)를 손쉽게 설치할 수 있는 경량 배포판입니다. 다음은 Windows 11에 Miniconda를 설치하는 단계입니다:

1. **Miniconda 다운로드 및 설치:** [Installing Miniconda 페이지](https://www.anaconda.com/docs/getting-started/miniconda/install#quick-command-line-install)에서 Quick install instructions 아래 Windows Command Prompt 탭에 있는 명령을 복사해 명령창에서 아래와 같이 실행합니다.
   ```
   curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o .\miniconda.exe
   start /wait "" .\miniconda.exe /S
   del .\miniconda.exe
   ```
2. **설치 완료 후:** 설치를 마치면, Windows 시작 메뉴의 "Anaconda (miniconda3) / Anaconda Prompt" 를 실행합니다. 이를 이용해 conda 명령어를 실행할 수 있습니다.

### Python 3.12용 conda 가상환경 생성

이제 파이썬 개발을 위한 가상환경을 만들어 보겠습니다. 가상환경을 사용하면 프로젝트마다 별도의 패키지 구성을 유지할 수 있어 충돌을 막고 관리가 쉬워집니다. Python 3.12 버전을 사용하고, AI 도구들을 함께 설치할 것이므로 환경 이름을 예시로 **langgraph_basic**라고 하겠습니다.

1. **가상환경 생성:** Anaconda Prompt에서 다음 명령을 실행합니다.  
   ```
   conda create -n langgraph_basic python=3.12
   ```  
   `-n langgraph_basic` 옵션은 환경 이름을 지정하는 것이고, `python=3.12`는 해당 버전의 파이썬을 설치하라는 뜻입니다. 앞서 설정한 conda-forge 채널로부터 Python 3.12 및 기본 패키지들이 설치됩니다.

2. **환경 활성화:** 환경을 생성한 후 아래 명령으로 해당 환경을 활성화합니다.  
   ```
   conda activate langgraph_basic
   ```  
   프롬프트에 (langgraph_basic) 이 표시되면 이제 이 가상환경에서 파이썬을 실행하게 됩니다. 이 상태에서 `python --version`을 입력해보면 Python 3.12.xx 형태로 버전이 출력될 것입니다.

3. **필요 패키지 설치:** 이 환경에 개발에 필요한 패키지를 추가로 설치합니다:  
   ```
   pip install python-dotenv notebook langgraph langchain-openai langchain-community tavily-python
   ```   
   

### VS Code 설치 및 필수 확장팩 설치 (한글 지원 포함)

개발을 편리하게 진행하려면 **Visual Studio Code** (VS Code)를 설치하는 것이 좋습니다. VS Code는 가볍고 확장성이 좋아 파이썬 개발과 AI 도구 활용에 널리 사용됩니다. 

- **VS Code 다운로드:** [VS Code 공식 사이트](https://code.visualstudio.com/)에서 Windows용 설치 파일을 받아 설치합니다. Windows 11에서는 별다른 설정 없이 기본 설치를 진행하면 됩니다. 설치 후 VS Code를 실행합니다.
- **한글 언어 팩 설치:** VS Code는 기본적으로 영문 인터페이스지만, 한국어로 UI를 볼 수 있도록 **Korean Language Pack** 확장을 제공합니다. VS Code 왼쪽 확장 아이콘(바퀴 모양)을 클릭하고 "korean language pack"을 검색하여 **Korean Language Pack for Visual Studio Code**(Microsoft 제공)를 설치합니다. 설치 후 VS Code를 다시 시작하면 VS Code 메뉴 등이 한글로 표시됩니다.
- **Python 확장팩 설치:** VS Code에서 파이썬을 사용하려면 Microsoft에서 제공하는 공식 **Python 확장**을 설치해야 합니다. 이 확장은 코드 편집기에서 파이썬 문법 하이라이팅, 자동완성, 디버깅, Jupyter Notebook 지원 등을 제공합니다. 확장 검색에서 "Python"을 찾아 **Python (ms-python.python)** 확장을 설치하세요.
- **필수 Python 관련 확장:** **Jupyter** 확장을 설치합니다. Jupyter 확장은 VS Code 내에서 노트북 환경을 사용할 수 있게 해줍니다.

### VS Code에서 conda 가상환경 연동 방법

앞서 생성한 conda 가상환경(langgraph_basic)을 VS Code에 연동하여, 터미널과 디버거, 에디터가 모두 해당 환경의 Python을 사용하도록 설정해야 합니다. 설정하는 방법은 아래와 같습니다:

1. **인터프리터 선택:** VS Code에서 `Ctrl+Shift+P`를 눌러 **“Python: Select Interpreter”**를 실행합니다. 그러면 설치된 Python 인터프리터 목록이 나타나는데, 여기서 **langgraph_basic (Python 3.12)**와 같은 항목을 찾아 선택합니다. (목록에 바로 보이지 않는 경우, *Enter interpreter path*를 눌러 Miniconda 설치 경로의 `envs/langgraph_basic/python.exe`를 직접 지정할 수도 있습니다.)
2. **환경 활성화 확인:** 인터프리터를 선택하면 VS Code 하단 상태 바에 선택된 Python 버전과 환경명이 표시됩니다. 예를 들어 `Python 3.12.0 64-bit ('langgraph_basic': conda)`처럼 보입니다. 또한 새 터미널을 열 때 자동으로 `conda activate langgraph_basic`가 실행되어 해당 환경이 활성화된 터미널이 열리게 됩니다.
3. **테스트:** 터미널 패널에서 `python --version`을 쳐서 3.12 버전이 출력되는지 확인합니다. 또, 간단한 파이썬 파일을 열고 실행해보거나 (우클릭 -> **터미널에서 Python 파일 실행**), 혹은 Jupyter 노트북을 열어 커널로 해당 환경의 파이썬을 선택해 보는 방식으로 환경이 올바르게 연결되었는지 테스트합니다.

이제 VS Code에서 파이썬 파일을 실행하거나 디버깅할 때 langgraph_basic 가상환경이 사용됩니다. 이 환경에 설치한 **langchain_openai, langgraph** 등의 패키지도 바로 임포트하여 활용할 수 있습니다.
