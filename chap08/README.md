# Chapter 08
Chapter 08 실행을 위한 초기 설정

초기화
```shell
uv init
uv venv --python 3.13
```

uv.lock 등올 설치할 경우
```shell
# 현재 잠금파일(uv.lock) 생성/갱신 & 설치
uv lock
uv sync # uv.lock을 기준으로 .venv에 설치
```

의존성
```shell
uv add langchain
uv add langchain-openai
```


실행
```shell
uv run python ./src/myapp/main.py
```