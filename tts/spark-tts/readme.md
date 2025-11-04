spark-tts readme
----------------

```bash
git clone https://github.com/SparkAudio/Spark-TTS.git app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com

mkdir -p pretrained_models

# Make sure you have git-lfs installed (https://git-lfs.com)
git lfs install

git clone https://huggingface.co/SparkAudio/Spark-TTS-0.5B pretrained_models/Spark-TTS-0.5B

# or using huggingface-cli with hf-mirror.com
export HF_ENDPOINT = "https://hf-mirror.com"
huggingface-cli download --resume-download SparkAudio/Spark-TTS-0.5B --local-dir pretrained_models/Spark-TTS-0.5B


# when got error
# TypeError: argument of type 'bool' is not iterable
# then install pydantic==2.10.6
pip install pydantic==2.10.6 -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com
python webui.py --device 0
```