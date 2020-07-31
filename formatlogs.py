import json, re, os

suff: str = '.tbf'


def findlogs(dir: str = '.') -> list:
    logs: list = []

    for file in os.listdir(dir):
        if file.endswith(suff):
            logs.append(file)
    
    return logs


def formatlog(oldlog, currline, newsuff: str = '.formatted'):
    with open(re.sub(suff + '$', newsuff, oldlog), "a") as newlog:
        newlog.write(currline['common_log'] + ' "')

        if 'Referer' in currline['request']['headers']:
            newlog.write(currline['request']['headers']['Referer'][0])
        else:
            newlog.write('-')
            
        newlog.write('" "' + currline['request']['headers']['User-Agent'][0] + '"\n')


for log in findlogs():
    with open(log) as f:
        for line in f:
            d: dict = json.loads(line)

            formatlog(log, d)

