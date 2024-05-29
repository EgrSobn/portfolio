"""
Для вычисления дисперсии и ср. квадр. отклонения использовать 
https://myslide.ru/documents_3/b9d7b50c38e81a4b8b7645742d3b22c7/img10.jpg
"""


class MathStats():
    def __init__(self, file):
        import csv

        self._file = file
        self._data = []
        self._mean = None
        self._max = float('-Inf')
        self._min = float('Inf')
        self._disp = None
        with open(self._file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for _r in reader:
                row = {
                    'Date': _r[''],
                    'Offline': float(_r['Offline Spend']),
                    'Online': float(_r['Online Spend']),
                }
                self._data.append(row)

    @property
    def data(self):
        return self._data

    def get_mean(self, data):
        """
        Вычисление среднего по оффлайн и онлайн тратам
        """

        sums = {'offline': 0, 'online': 0}
        for _l in data:
            sums['offline'] += _l['Offline']
            sums['online'] += _l['Online']

        self._mean = {'offline':sums['offline'] / len(data), 'online':sums['online'] / len(data)}

        return self._mean

    @property
    def max(self):
      # TODO
        offline_max = max(_i['Offline'] for _i in self._data)
        online_max = max(_i['Online'] for _i in self._data)
        self._max = {'offline': offline_max, 'online': online_max}
        return self._max

    @property
    def min(self):
        offline_min = min(_i['Offline'] for _i in self._data)
        online_min = min(_i['Online'] for _i in self._data)
        self._min = {'offline': offline_min, 'online': online_min}
        # TODO
        
        return self._min

    @property
    def disp(self):
        #offline
        substr_offline = 0
        substr_online = 0
        for _i in self._data:
          substr_offline += (_i['Offline'] - self._mean['offline'])**2
          substr_online += (_i['Online'] - self._mean['online'])**2
        self._disp = { 'offline': substr_offline / len(self._data), 'online': substr_online / len(self._data)}
        return self._disp

    # по аналогии — со среднем квадратичным отклонением
    @property
    def sigma_sq(self):
        from math import sqrt
        self._sigma_sq = {"offline": sqrt(self.disp["offline"]), "online": sqrt(self.disp["online"])}
        return self._sigma_sq
