"""
Voice Recorder 音频录制器
@filename VoiceRecorder.py
@description 用于录制音频的工具
"""

import pyaudio
import time
import threading
from .config import *


class VoiceRecorder:
    def __init__(self, output_file):
        # 音频输出文件
        self.outputFile = output_file
        # 是否正在录制
        self.__recording = False
        self.__lock = False

        self.frames = []

        self.__th = None

    # 录音
    def record(self):
        # 初始化 PyAudio
        audio = pyaudio.PyAudio()

        # 打开音频流
        stream = audio.open(format=VRCD_FORMAT, channels=VRCD_CHANNELS,
                            rate=VRCD_RATE, input=True,
                            frames_per_buffer=VRCD_CHUNK)

        self.frames = []

        # 录制音频数据
        while self.__recording:
            data = stream.read(VRCD_CHUNK)
            self.frames.append(data)

        # 停止音频流
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # 将录制的音频保存为 PCM 格式的文件
        with open(self.outputFile, 'wb') as pcm_file:
            pcm_file.write(b''.join(self.frames))

        # 全部完成后解锁线程
        self.__lock = False

    # 开始录音
    def start(self):
        # 锁，确保只有一个录音线程
        if self.__recording:
            return
        self.__recording = True
        # 生成线程
        self.__th = threading.Thread(target=self.record)
        self.__th.start()

    # 结束录音
    def stop(self):
        # 停止录制音频
        self.__recording = False

        # 锁
        while self.__lock:
            time.sleep(0.05)
            pass

        # 结束线程
        self.__th.join()