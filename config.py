"""
配置文件
@filename config.py
@description 配置文件
"""
import pyaudio

# 请求地址
URL = "wss://nls-gateway.cn-shanghai.aliyuncs.com/ws/v1"
# Token
TOKEN = "这里输入你的token"
# App Key
APPKEY = "这里输入你的app key"

"""
VoiceMaker
语音合成部分
"""
# 输出文件(不需要加后缀)
VM_OUTPUT_FILE = "output.pcm"
# 人声
VM_VOICE = "zhida"
# 文件格式 支持pcm,mp3,wav
VM_AFORMAT = "pcm"
# 语调
VM_PITCH_RATE = -60
# 语速
VM_SPEED = -5


"""
VoiceReader
语音识别部分
"""
# 文件格式，支持pcm
VR_AFORMAT = "pcm"

"""
VoiceRecord
语音录制部分
"""

# 录音格式
VRCD_FORMAT = pyaudio.paInt16
# 录音通道
VRCD_CHANNELS = 1
# 采样率
VRCD_RATE = 16000
# Chunck 大小
VRCD_CHUNK = 1024
# 录音输出文件
VRCD_OUTPUT_FILENAME = "output.pcm"

"""
VoicePlayer
语音播放部分
"""
VP_CHANNELS = 1
VP_RATE = 16000
VP_CHUNCK = 1024
