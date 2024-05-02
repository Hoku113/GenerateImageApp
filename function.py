
from diffusers import DiffusionPipeline

def generateImage(prompt, negative_prompt=None, style=None, device="cpu"):

  # モデルの種類
  models = {
      "なし" : "stabilityai/stable-diffusion-xl-base-1.0",
      "アニメ": "Ojimi/anime-kawai-diffusion",
      "油絵": "stablediffusionapi/painters-checkpoint-oil-p",
      "写真": "dreamlike-art/dreamlike-photoreal-2.0",
      "ファンタジー": "volrath50/fantasy-card-diffusion",
      "スチームパンク": "AIArtsChannel/steampunk-diffusion"
  }

  # モデルの読み込み
  pipeline = DiffusionPipeline.from_pretrained(models[style]).to(device)

  # 画像の生成
  image = pipeline(prompt, negative_prompt=negative_prompt).images[0]

  return image

