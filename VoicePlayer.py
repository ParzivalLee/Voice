"""
音频播放器
@filename VoicePlayer.py
@description 用于播放语音文件
"""

import pyaudio


class VoicePlayer:
    def __init__(self, voice_file='output/output.pcm', channels=1, width=2, rate=16000):
        self.voiceFile = voice_file
        self.channels = channels
        self.width = width
        self.rate = rate
        pass

    def play(self, voice_file=None):
        if not voice_file:
            voice_file = self.voiceFile
        # 打开PCM文件
        with open(voice_file, 'rb') as fp:
            data = fp.read()
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(self.width),
                        channels=self.channels,
                        rate=self.rate,
                        output=True)
        # 播放PCM文件数据
        stream.write(data)
        # 关闭播放器和文件
        stream.stop_stream()
        stream.close()
        p.terminate()
