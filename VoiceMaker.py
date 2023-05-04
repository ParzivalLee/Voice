"""
声音合成器
@filename VoiceMaker.py
@description 调用了阿里云的SDK，可以进行声音合成，限制300字符以内
"""
from .config import *
import nls
import os


# 声音合成类
class VoiceMaker:
    # 初始化文件
    # 配置参数在config.py中
    # @param output_file 输出文件，不需要加后缀
    def __init__(self, output_file=VM_OUTPUT_FILE):
        self.__url = URL
        self.__token = TOKEN
        self.__appKey = APPKEY
        self.__outputFile = output_file
        self.tts = nls.NlsSpeechSynthesizer(url=self.__url,
                                            appkey=self.__appKey,
                                            token=self.__token,
                                            on_metainfo=self.onMetainfo,
                                            on_data=self.onData,
                                            on_close=self.onClose,
                                            on_completed=self.onCompleted,
                                            on_error=self.onError)
        # 文件指针
        self.__f = None

    # @param text 要合成语音的文本
    # @param voice 语音角色
    def start(self, text, output_file=None, voice=VM_VOICE):
        # 如果指定了输出文件，则使用指定的输出文件
        if output_file:
            self.__outputFile = output_file
        self.__f = open(self.__outputFile, "wb")
        self.tts.start(text=text,
                       voice=voice,
                       aformat=VM_AFORMAT,
                       pitch_rate=VM_PITCH_RATE,
                       speech_rate=VM_SPEED)

    def onMetainfo(self, message, *args):
        # print("meta info message=>{}".format(message))
        pass

    def onError(self, message, *args):
        # print("error args=>{}".format(args))
        pass

    def onClose(self, *args):
        # print("close: args=>{}".format(args))
        try:
            self.__f.close()
        except Exception as e:
            print("close file failed since:", e)

    def onData(self, data, *args):
        try:
            self.__f.write(data)
        except Exception as e:
            print("write data failed:", e)

    def onCompleted(self, message, *args):
        # print("completed:args=>{} message=>{}".format(args, message))
        pass
