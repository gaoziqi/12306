from os import path
import json


class Global(object):
    """Global var"""
    __global = None

    def __init__(self):
        self.mutex = False  # 线程间安全锁
        self.process = 1  # 开启线程数量
        self.period = 5  # 连续访问间隔时间

    @staticmethod
    def get_instance():
        if Global.__global is None:
            Global.__global = Global()
        return Global.__global


def _global():
    return Global.get_instance()


class Base(object):
    """docstring for base"""

    def __init__(self):
        super(Base, self).__init__()
        with open(path.dirname(path.realpath(__file__)) + '/station.json', 'r') as r:
            self.station = json.load(r)
            self.rstation = dict((v, k) for k, v in self.station.items())
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, sdch, dr',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'leep-alive',
            'Host': 'kyfw.12306.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWekit/537.36 (KHTML,\
            like Gecko) Chrome/54.0.2840.71 Safari/537.36'
        }
