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
- 커스텀 노드 생성

## 🖼 결과 샘플

![생성 이미지 1](output/sample_001.png)

## 🔧 트러블슈팅

- WSL vs Windows 환경 차이 해결
- GPU 활용을 위한 환경 설정

## 📝 배운 점

- API 연동 경험
- 환경 설정 문제 해결
- Python을 활용한 자동화

## 저장소 구성

- `preprocess_node.py` – Pillow를 이용해 밝기 조절과 업스케일을 처리하는 실제용 커스텀 노드.
- `node.py` – 밝기 조절만 수행하는 최소 예제 노드.
- `Default-SD1.5.json` – ComfyUI에서 내보낸 예시 워크플로 JSON.

## 요구 사항

- Python 3.10 이상
- `127.0.0.1:8188`에서 대기 중인 ComfyUI 인스턴스
- Python 패키지: `torch`, `numpy`, `Pillow`

## 커스텀 노드 설치

1. `preprocess_node.py`를 ComfyUI의 `custom_nodes` 디렉터리(예: `ComfyUI/custom_nodes/workflowComfyui/preprocess_node.py`)에 복사합니다.
2. ComfyUI를 재시작하거나 “Reload custom nodes”를 눌러 `NODE_CLASS_MAPPING`에 등록된 새 클래스를 읽어오게 합니다.
3. ComfyUI 그래프에서 `image/process_image` 카테고리의 **Image Preprocess** 노드로 표시됩니다.

## 노드 파라미터 (`preprocess_node.py`)

| 입력         | 타입  | 설명                                                                            |
| ------------ | ----- | ------------------------------------------------------------------------------- |
| `image`      | IMAGE | ComfyUI 워크플로 내부에서 사용하는 배치 텐서.                                   |
| `brightness` | float | Pillow `ImageEnhance.Brightness`에 전달되는 배수 (기본 1.2, 1.0이면 변화 없음). |
| `method`     | enum  | 업스케일에 사용할 리샘플링 방식 (`nearest`, `bilinear`, `bicubic`, `lanczos`).  |
| `upscale_by` | float | 입력 해상도에 곱해지는 스케일 값 (0.05–4.0).                                    |

노드 내부에서는 `tensor_to_pil`로 텐서를 PIL 이미지로 변환하고 밝기·업스케일을 마친 뒤 `pil_to_tensor`를 통해 다시 텐서로 돌려 downstream 노드가 ComfyUI 표준 형식을 그대로 사용할 수 있도록 합니다.

## 샘플 워크플로 사용

1. ComfyUI를 실행하고 `Default-SD1.5.json`에서 사용되는 체크포인트와 LoRA를 준비합니다.
2. ComfyUI UI에서 `Load` → `Load (API format)`을 선택해 `Default-SD1.5.json`을 불러옵니다.
3. CLIP Text Encode 노드의 프롬프트나 KSampler 노드의 시드 값을 원하는 대로 수정합니다.
4. 그래프를 실행하면 `SaveImage` 노드 설정에 따라 결과 이미지가 저장됩니다.

## 팁

- 가벼운 노드를 추가로 만들 때는 `node.py`를 최소 템플릿으로 활용해 보세요.
- 전처리 로직을 수정한 뒤에는 ComfyUI를 다시 불러오거나 “Reload custom nodes” 기능을 사용해야 변경 사항이 반영됩니다.
