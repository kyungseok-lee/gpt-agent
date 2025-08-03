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

## 개발 워크플로우
### 일반적인 개발 워크플로우
```shell
# 1. 프로젝트 생성
uv init my-project --python 3.12
cd my-project

# 2. 의존성 추가
uv add fastapi uvicorn
uv add --dev pytest black ruff mypy

# 3. 코드 작성
# src/my_project/main.py 작성

# 4. 테스트 실행
uv run pytest

# 5. 코드 포맷팅
uv run black src/
uv run ruff check src/

# 6. 애플리케이션 실행
uv run python src/my_project/main.py
```

### pyproject.toml 예제
```toml
[project]
name = "my-project"
version = "0.1.0"
description = "My awesome project"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
dependencies = [
    "fastapi>=0.104.0",
    "uvicorn[standard]>=0.24.0",
    "pydantic>=2.0.0",
]
requires-python = ">=3.12"

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
    "mypy>=1.7.0",
]

[tool.uv.scripts]
dev = "uvicorn my_project.main:app --reload"
test = "pytest tests/ -v"
lint = "ruff check src/"
format = "black src/ tests/"
typecheck = "mypy src/"
check-all = ["lint", "typecheck", "test"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.black]
line-length = 88
target-version = ['py312']

[tool.ruff]
target-version = "py312"
line-length = 88

[tool.mypy]
python_version = "3.12"
strict = true
```