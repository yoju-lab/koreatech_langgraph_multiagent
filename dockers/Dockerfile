FROM python:3.11

# 기본 도구 설치
RUN apt-get update && apt-get update --allow-unauthenticated && \
    apt-get install -y --no-install-recommends \
        git \
        curl \
        wget \
        sudo && \
    rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /apps

# Clone the Git repository. Here we dynamically specify the repository name using the variable defined earlier.
RUN git clone -b main https://github.com/yoju-lab/koreatech_langgraph_multiagent koreatech_langgraph_multiagent

# Changes the working directory to /app/${REPO_NAME}. This uses the variable to dynamically set the directory path.
WORKDIR /apps/koreatech_langgraph_multiagent

RUN pip install --no-cache-dir -r ./requirements.txt

RUN rm -rf .git

# VS Code 서버 준비
# RUN curl -fsSL https://code-server.dev/install.sh | sh

# 시작 스크립트 생성
# RUN echo '#!/bin/bash\ncode-server --host 0.0.0.0 --port 8080 /apps/${APP_DIR_NAME} & langgraph dev --port 8000 --host 0.0.0.0' > /start.sh \
#     && chmod +x /start.sh

