wan2.2-animate
--------------


```bash
git clone https://huggingface.co/spaces/Wan-AI/Wan2.2-Animate app
# or using mirror in China mainland
git clone https://hf-mirror.com/spaces/Wan-AI/Wan2.2-Animate app
cd app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
# missing gradio
pip install gradio -i https://mirrors.aliyun.com/pypi/simple/
# set env `DASHSCOPE_API_KEY`, get that from aliyun
python app.py
```