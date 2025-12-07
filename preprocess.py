from PIL import ImageEnhance, Image
import torch
import numpy as np


def MyCustomNode_inputs():
    return {
        "required": {
            "image": ("IMAGE",),
            "method": (["nearest", "bilinear", "bicubic", "lanczos"],),
            "upscale_by": (
                "FLOAT",
                {"default": 2, "min": 0.05, "max": 4, "step": 0.05},
            ),
            "brightness": (
                "FLOAT",
                {"default": 1.2, "min": 0.0, "max": 3.0, "step": 0.05},
            ),
        },
    }


# Tensor → PIL
def tensor_to_pil(tensor):
    # [4, 512, 512, 3]
    batch_count = tensor.shape[0]

    pil_images = []
    for i in range(batch_count):
        img = 255.0 * tensor[i].cpu().numpy()
        img = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
        pil_images.append(img)
    return pil_images


# PIL → Tensor
def pil_to_tensor(pil_images):
    # (H, W, 3) → [1, H, W, 3]
    tensor_list = []
    for img in pil_images:
        # 0~255 정수 -> 0~1 소수 변환
        img_array = np.array(img).astype(np.float32) / 255.0
        tensor_list.append(torch.from_numpy(img_array))

    # 여러 장을 하나로 합침 (Stack) -> [Batch, H, W, C]
    return torch.stack(tensor_list)


class ImagePreprocessNode:
    @classmethod
    def INPUT_TYPES(cls):
        return MyCustomNode_inputs()

    RETURN_TYPES = ("IMAGE",)

    FUNCTION = "process_image"

    CATEGORY = "image/process_image"

    def process_image(
        self,
        image,
        brightness,
        method,
        upscale_by,
    ):

        #  텍스트를 PIL 상수로 바꿔주는 사전 정의
        pil_methods = {
            "nearest": Image.Resampling.NEAREST,
            "bilinear": Image.Resampling.BILINEAR,
            "bicubic": Image.Resampling.BICUBIC,
            "lanczos": Image.Resampling.LANCZOS,
        }
        # 텐서 -> PIL 변환 (필수)
        pil_image = tensor_to_pil(image)

        processed_images = []

        for img in pil_image:
            # 밝기 조정
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(brightness)

            # 업스케일
            new_width = int(img.width * upscale_by)
            new_height = int(img.height * upscale_by)
            img = img.resize((new_width, new_height), pil_methods[method])

            processed_images.append(img)

        # PIL -> 텐서 변환 (필수)
        output_image = pil_to_tensor(processed_images)

        return (output_image,)


NODE_CLASS_MAPPING = {"ImagePreprocess": ImagePreprocessNode}
NODE_DISPLAY_NAME_MAPPINGS = {"ImagePreprocess": "Image_Preprocess"}
