# ComfyUI Python API 연동 프로젝트

## 📌 프로젝트 소개

ComfyUI의 API를 활용하여 Python 스크립트로 이미지 생성을 자동화하는 프로젝트입니다.

## 🛠 기술 스택

- Python 3.x
- ComfyUI API
- WebSocket, HTTP Request

## ⚙️ 설치 및 실행 방법

### 1. ComfyUI 설치 및 실행

[ComfyUI 다운로드 링크]
실행: `run_nvidia_gpu.bat`

### 2. Python 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. 실행

```bash
python test.py
```

## 📂 주요 기능

- ComfyUI 워크플로우를 Python으로 자동 실행
- API 통신을 통한 이미지 생성 자동화
- 생성된 이미지 자동 저장

## 🖼 결과 샘플

![생성 이미지 1](output/sample_001.png)

## 🔧 트러블슈팅

- WSL vs Windows 환경 차이 해결
- GPU 활용을 위한 환경 설정

## 📝 배운 점

- API 연동 경험
- 환경 설정 문제 해결
- Python을 활용한 자동화
