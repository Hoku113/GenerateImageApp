
from diffusers import DiffusionPipeline
from models import models

def generateImage(prompt, negative_prompt=None, style=None, device="cpu"):

  # モデルの読み込み
  pipeline = DiffusionPipeline.from_pretrained(models[style]).to(device)

  # 画像の生成
  image = pipeline(prompt, negative_prompt=negative_prompt).images[0]

  return image

