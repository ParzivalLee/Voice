# Voice语音库，调用阿里云开放SDK
# 1. 全局配置
## 1.1 环境配置
### 1.1.1 python依赖安装
```commandline
pip install -r requirements.txt
```
### 1.1.2 阿里云SDK配置
1. 解压Packages中的压缩包
2. 进入压缩文件夹，打开终端输入如下命令
```commandline
pip install -r requirements.txt //安装依赖
python setup.py build
python setup.py install
```
## 1.2 全局配置参数
- _URL_ 语音合成请求地址
- _TOKEN_ 阿里云提供的token
- _APPKEY_ 阿里云控制台的app key

# 2. 语音识别类 VoiceMaker.py
## 2.1 config.py 参数配置
- _VM_OUTPUT_DIR_ 合成的语音输出的文件夹
- _VM_OUTPUT_FILE_ 合成的语音输出的文件（不需要加后缀）
- _VM_VOICE_ 合成的语音使用的人声
- _VM_AFORMAT_ 合成的语音格式

## 2.2 使用说明
### 2.2.1 初始化声音合成类

```python
import Voice

# 输出文件夹可选，默认为
vm = Voice.VoiceMaker(output_file="输出文件夹")
# text 为要合成语音的文本，必不可少的参数，另外两项参数可在config.py中配置
vm.start(text="要合成语音的文本", output_file="要输出的文件", voice="声音选择")
```
