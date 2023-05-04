"""
VoiceReader 语音识别类
@filename VoiceReader.py
@description 调用了阿里云接口的语音识别库
"""

from .config import *
import nls
import time


# 以下代码会根据音频文件内容反复进行实时语音识别（文件转写）
class VoiceReader:

    # @param voice_file 音频文件（不加后缀）
    def __init__(self, voice_file):
        self.sr = nls.NlsSpeechTranscriber(
            url=URL,
            token=TOKEN,
            appkey=APPKEY,
            on_sentence_begin=self.onSentenceBegin,
            on_sentence_end=self.onSentenceEnd,
            on_start=self.onStart,
            on_result_changed=self.onResultChg,
            on_completed=self.onCompleted,
            on_error=self.onError,
            on_close=self.onClose
        )
        self.__test_file = voice_file
        self.text = None

    def loadfile(self, filename):
        with open(filename, "rb") as f:
            self.__data = f.read()

    def start(self):
        self.loadfile(self.__test_file)
        self.sr.start(aformat=VR_AFORMAT,
                      enable_intermediate_result=True,
                      enable_punctuation_prediction=True,
                      enable_inverse_text_normalization=True)

        self.__slices = zip(*(iter(self.__data),) * 640)

        for i in self.__slices:
            self.sr.send_audio(bytes(i))
            time.sleep(0.01)

        self.sr.stop()

        return self.text

    def onSentenceBegin(self, message, *args):
        # print("test_on_sentence_begin:{}".format(message))
        pass

    def onSentenceEnd(self, message, *args):
        # print("test_on_sentence_end:{}".format(message))
        self.text = eval(message)['payload']['result']
        pass

    def onStart(self, message, *args):
        # print("test_on_start:{}".format(message))
        pass

    def onError(self, message, *args):
        # print("on_error args=>{}".format(args))
        pass

    def onClose(self, *args):
        # print("on_close: args=>{}".format(args))
        pass

    def onResultChg(self, message, *args):
        # print("test_on_chg:{}".format(message))
        pass

    def onCompleted(self, message, *args):
        # print("on_completed:args=>{} message=>{}".format(args, message))
        pass
