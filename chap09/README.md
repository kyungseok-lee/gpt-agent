# LLM Study

## 최초 프로젝트 생성 시
```shell
uv init
uv venv --python 3.13
```

## uv.lock 등이 존재하며 재철시 하는 경우
```shell
# 현재 잠금파일(uv.lock) 생성/갱신 & 설치
uv lock
uv sync # uv.lock을 기준으로 .venv에 설치
```

## 의존성 추가
```shell
uv add PyMuPDF pypdf langchain langchain_community langchain-openai load_dotenv langchain_chroma langchain_openai

uv pip streamlit
uv add streamlit
uv add watchdog

uv sync
```

## Jupyter
```jupyter
%pip install -> !uv install로 변환 필요
```

## 실행 시
```shell
uv run python ./src/myapp/main.py
```

## streamlit
```shell
uv run streamlit hello

export OPENAI_API_KEY=<openai api key> 
uv pip install streamlit
source .venv/bin/activate
streamlit run ./src/sec03/rag.py
streamlit run ./src/sec03/rag_0.py
streamlit run ./src/sec03/rag_1.py
```

http://localhost:8501/
