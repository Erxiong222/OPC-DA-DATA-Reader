import json
import time
import datetime
import os


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)

def writejson(data):
    time_str = time.strftime('%Y-%m-%d-%H-%M',time.localtime())
    path = 'C:/json/'
    if not os.path.exists(path):
        os.makedirs(path)
    str = path + time_str + '.txt'
    f = open(str,'a')
    for x in data:
        result = {}
        result['time'] = x[0]
        result['id'] = x[1]
        result['value'] = x[2]
        jsondata = json.dumps(result, cls=DateEncoder)
        f.write(jsondata + '\n')
    f.close()
