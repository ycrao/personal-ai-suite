cn-ocr
------

### 官网

- 文档：https://cnocr.readthedocs.io/zh-cn/stable/install/
- 仓库：https://github.com/breezedeus/cnocr
- 在线演示：https://huggingface.co/spaces/breezedeus/CnOCR-Demo
- 文章：https://www.breezedeus.com/article/cnocr-v2.3-better-more


### 安装及使用

```bash
cd ocr-demo/cn-ocr
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r r.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
python3 main.py
# 第一次执行可能比较慢，因为需要下载模型，可以提前将模型下载配置好
# ref https://cnocr.readthedocs.io/zh-cn/stable/usage/ & https://huggingface.co/breezedeus/cnstd-cnocr-models

# 回显结果
[{'text': '中国移动', 'score': 0.5608038902282715, 'position': array([[213, 181],
       [359, 180],
       [359, 213],
       [213, 214]], dtype=int32)}, {'text': 'China Mobile', 'score': 0.6331827640533447, 'position': array([[213, 216],
       [359, 214],
       [359, 234],
       [213, 235]], dtype=int32)}, {'text': '扫一扫', 'score': 0.9903545379638672, 'position': array([[418, 258],
       [487, 257],
       [487, 282],
       [419, 283]], dtype=int32)}, {'text': '领好礼', 'score': 0.9941188097000122, 'position': array([[418, 282],
       [483, 282],
       [483, 307],
       [418, 307]], dtype=int32)}]
# position 数组存放的是坐标信息，测试下来应该是相对于左上角的坐标，[x, y] x轴向右移动x像素 y轴向下移动y像素
```

官方提供有 `http` 接口服务，参考下列命令安装并操作。

```bash
pip3 install cnocr[serve] onnxruntime
cnocr serve -p 8501
curl -F image=@./sample.jpg http://127.0.0.1:8501/ocr
```

执行完上面 `curl` 命令，会回显如下识别结果：

```json
{"status_code":200,"results":[{"text":"中国移动","score":0.5608038902282715,"position":[[213,181],[359,180],[359,213],[213,214]]},{"text":"China Mobile","score":0.6331827640533447,"position":[[213,216],[359,214],[359,234],[213,235]]},{"text":"扫一扫","score":0.9903545379638672,"position":[[418,258],[487,257],[487,282],[419,283]]},{"text":"领好礼","score":0.9941188097000122,"position":[[418,282],[483,282],[483,307],[418,307]]}]}
```
