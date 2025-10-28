umi-ocr
-------

>   `Umi-OCR` 提供了 [docker镜像](https://github.com/hiroi-sora/Umi-OCR_runtime_linux/blob/main/Dockerfile) 构建文件，我们自行构建一下镜像即可。 

```bash
docker build -t registry.cn-hangzhou.aliyuncs.com/douyasi/umi-ocr-paddle:latest .
docker push registry.cn-hangzhou.aliyuncs.com/douyasi/umi-ocr-paddle:latest
docker run -d --name umi-ocr \
    -e HEADLESS=true \
    -p 1224:1224 \
    registry.cn-hangzhou.aliyuncs.com/douyasi/umi-ocr-paddle:latest
```

http 接口参考：[api_ocr.md](https://github.com/hiroi-sora/Umi-OCR/blob/main/docs/http/api_ocr.md) 。

### 接口

#### 获取选项

```bash
curl --request GET \
  --url http://localhost:1224/api/ocr/get_options \
  --header 'Content-Type: application/json'
```

响应示例

```json
{
  "ocr.language": {
    "title": "Language/Model library",
    "optionsList": [
      [
        "models/config_chinese.txt",
        "简体中文"
      ],
      [
        "models/config_en.txt",
        "English"
      ],
      [
        "models/config_chinese_cht.txt",
        "繁體中文"
      ],
      [
        "models/config_japan.txt",
        "日本語"
      ],
      [
        "models/config_korean.txt",
        "한국어"
      ],
      [
        "models/config_cyrillic.txt",
        "Русский"
      ]
    ],
    "type": "enum",
    "default": "models/config_chinese.txt",
    "advanced": false
  },
  "ocr.cls": {
    "title": "Text direction correction",
    "default": false,
    "toolTip": "Enable direction classification to recognize slanted or inverted text. This may reduce recognition speed.",
    "type": "boolean",
    "advanced": false
  },
  "ocr.limit_side_len": {
    "title": "Limit image edge length",
    "optionsList": [
      [
        960,
        "960 (Default)"
      ],
      [
        2880,
        "2880"
      ],
      [
        4320,
        "4320"
      ],
      [
        999999,
        "Unlimited"
      ]
    ],
    "toolTip": "Compress images with edge length greater than this value to improve recognition speed. This may reduce recognition accuracy.",
    "type": "enum",
    "default": 960,
    "advanced": false
  },
  "tbpu.parser": {
    "title": "排版解析方案",
    "toolTip": "按什么方式，解析和排序图片中的文字块",
    "default": "multi_para",
    "optionsList": [
      [
        "multi_para",
        "多栏-按自然段换行"
      ],
      [
        "multi_line",
        "多栏-总是换行"
      ],
      [
        "multi_none",
        "多栏-无换行"
      ],
      [
        "single_para",
        "单栏-按自然段换行"
      ],
      [
        "single_line",
        "单栏-总是换行"
      ],
      [
        "single_none",
        "单栏-无换行"
      ],
      [
        "single_code",
        "单栏-保留缩进"
      ],
      [
        "none",
        "不做处理"
      ]
    ],
    "type": "enum",
    "advanced": false
  },
  "tbpu.ignoreArea": {
    "title": "忽略区域",
    "toolTip": "数组，每一项为[[左上角x,y],[右下角x,y]]。",
    "default": [],
    "type": "var",
    "advanced": false
  },
  "data.format": {
    "title": "数据返回格式",
    "toolTip": "返回值字典中，[\"data\"] 按什么格式表示OCR结果数据",
    "default": "dict",
    "optionsList": [
      [
        "dict",
        "含有位置等信息的原始字典"
      ],
      [
        "text",
        "纯文本"
      ]
    ],
    "type": "enum",
    "advanced": false
  }
}
```

#### 提交图像识别

这里有一张线下[卡片样图](./card-for-ocr.jpg)，转为 `base64` 后可供识别。

![卡片样图](./card-for-ocr.jpg)

目标的图片转成 `base64` 字符串较长（见 [card-for-ocr.base64.txt](./card-for-ocr.base64.txt)），下面 `curl` 命令中略去以简短字符串代替。

```bash
curl --request POST \
  --url http://localhost:1224/api/ocr \
  --header 'Content-Type: application/json' \
  --data '{
    "base64": "/9j/4AAQSkZJRgABAQEASABIAAD/......",
    "options": {
        "ocr.language": "models/config_chinese.txt",
        "ocr.cls": true,
        "ocr.limit_side_len": 4320,
        "tbpu.parser": "multi_line",
        "data.format": "text"
    }
}'
```

响应结果：

```json
{
  "code": 100,
  "data": "店址：融科天域小区车库进口旁边\n送货电话：18186159692\n可以电话购买锅盔\n达上十个即送上门\n邱记锅盔光谷总店\n本店为方便广大顾客，长期提供一公里内免费送货服务",
  "score": 0.9227295617262522,
  "time": 2.9691550731658936,
  "timestamp": 1732878974.3983686
}
```