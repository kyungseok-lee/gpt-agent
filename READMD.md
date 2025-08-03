# GPT Agent

## UV 설치
```shell
# brew를 사용한 설치
brew install uv

# 또는
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Python 설치 및 Global 지정
```shell
# 기본 실행 파일도 생성: python, python3 심볼릭 실행 파일을 PATH에 둠
uv python install 3.13 --default

# 원하는 버전 설치 (예: 3.12)
uv python install 3.12

# global 설정
uv python pin 3.12
```

## 프로젝트 관리
```shell
uv init chap08
cd chap08
uv add requests fastapi
uv run python main.py
```
