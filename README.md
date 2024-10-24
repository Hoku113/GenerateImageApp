# 画像生成AIアプリ

画像生成AIを使って簡易なアプリを作成

![site](./asset/site.png)

## 実行手順

1. Google Colabを開く
<a target="_blank" href="https://colab.research.google.com/github/Hoku113/GenerateImageApp/blob/master/StableDiffusionApp.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


2. `ドライブにコピー`を押下し、上から順番に実行しアプリを起動

![copy_drive](./asset/copy_drive.png)

※Google Colabのランタイムを必ずGPUにすること

3. `External URL`のIPアドレスをコピーする

4. `your url is:`に書かれているuriをクリックする

5. 先ほどコピーしたIPアドレスを入力し`Click to Submit`を押す

※ ポート番号は不要です。

![access](./asset/access.png)


## 使用しているAIモデルについて
このプロジェクトには、以下のAIモデルが含まれます。各モデルの利用は、指定されたライセンスに準拠します：
- **Stable Diffusion 2 Base by StabilityAI**: OpenRAIL++ [詳細](https://huggingface.co/stabilityai/stable-diffusion-2-base)
- **B-LoRA Village Oil by LoRA Library**: OpenRAIL++ [詳細](https://huggingface.co/lora-library/B-LoRA-village_oil)
- **Anime Kawai Diffusion by Ojimi**: CreativeML OpenRAIL-M [詳細](https://huggingface.co/Ojimi/anime-kawai-diffusion)
