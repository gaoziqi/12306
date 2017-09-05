import json
import requests
from _global import Base


class Query(Base):
    """docstring for ClassName"""

    class Ticket(object):
        """解析每条数据"""
        parser = {
            0: 'checkG1234',  # 不为''可预定
            1: '预订',  # 显示预订无用
            2: '未知0',
            3: '车次',
            4: '始发站',
            5: '终点站',
            6: '出发站',
            7: '到达站',
            8: '出发时间',
            9: '到达时间',
            10: '历时',
            11: '有无余票',  # 有Y 无N 还没开始卖IS_TIME_NOT_BUY
            12: '未知1',
            13: '始发日期',
            14: '未知2',
            15: '未知3',
            16: '未知4',
            17: '未知5',
            18: '未知6',
            19: '未知7',
            20: '未知8',
            21: '未知9',
            22: '未知10',
            23: '软卧',
            24: '',
            25: '',
            26: '',
            27: '',
            28: '硬卧',
            29: '',
            30: '二等座',
            31: '一等座',
            32: '商务座',
            33: '高级软卧',
            34: '未知11',
            35: '未知12',
        }

        def __init__(self, msg):
            d = msg.split('|')

    def __init__(self):
        super(Query, self).__init__()
        self.url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={0}&leftTicketDTO.from_station={1}&leftTicketDTO.to_station={2}&purpose_codes=ADULT'
        self.headers['Referer'] = 'https://kyfw.12306.cn/otn/leftTicket/init'
        self.headers['If-Modified-Since'] = '0'
        self.headers['X-Requested-With'] = 'XMLHttpRequest'

    def run(self, date, f, t):
        url = self.url.format(date, self.station[f], self.station[t])
        r = requests.get(url, headers=self.headers, verify=False)
        result = json.loads(r.text)['data']['result']
        return result


# r = Query().run('2017-10-01', '天津', '淄博')
