index-tts readme
----------------

```bash
# install git-lfs
# Debian/Ubuntu: sudo apt update && sudo apt install git-lfs
# or use the official installer script from packagecloud if preferred.
# ref: https://git-lfs.com/
git lfs install
git clone https://github.com/index-tts/index-tts app
cd app
git lfs pull
# using proxy
# set $env:all_proxy=http://192.168.100.16:7890 # Windows PowerShell
# export all_proxy=http://192.168.100.16:7890 # Linux or macOS
python3 -m venv .venv
source .venv/bin/activate
pip install -U uv
uv sync --all-extras
# or using aliyun mirror
uv sync --all-extras --default-index "https://mirrors.aliyun.com/pypi/simple"
# or using tsinghua mirror
uv sync --all-extras --default-index "https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple"

export HF_ENDPOINT="https://hf-mirror.com"
uv tool install "huggingface-hub[cli,hf_xet]"
hf download IndexTeam/IndexTTS-2 --local-dir=checkpoints
uv run tools/gpu_check.py
uv run webui.py
```