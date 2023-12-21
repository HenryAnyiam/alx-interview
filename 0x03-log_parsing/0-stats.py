#!/usr/bin/python3

from sys import stdin
from datetime import datetime


def verify_line(line):
    """verify a line fits a particular syntax"""
    data = {}
    status = [200, 301, 400, 401, 403, 404, 405, 500]
    if isinstance(line, str):
        lineBreak = line.split()
        if len(lineBreak) == 9:
            data['ip'] = lineBreak[0]
            data['date'] = ' '.join(lineBreak[2:4])
            data['req'] = ' '.join(lineBreak[4:7])
            data['status'] = lineBreak[7]
            data['size'] = lineBreak[8]
            if len(data['ip'].split('.')) == 4 and\
               data['req'].strip('"') == "GET /projects/260 HTTP/1.1":
                if len(data['date']) == 28:
                    data['date'] = (data['date'][1:-2] + '0')
                try:
                    data['date'] = datetime.fromisoformat(data['date'])
                    data['status'] = int(data['status'])
                    data['size'] = int(data['size'])
                except ValueError as e:
                    print(e)
                else:
                    if data['status'] in status:
                        return data


def displayData(status, fileSize):
    """display data to output"""
    print(f"File size: {fileSize}")
    fileSize = 0
    for j in status:
        if status[j] > 0:
            print(f"{j}: {status[j]}")


i = 0
status = {200: 0, 301: 0, 400: 0, 401: 0,
          403: 0, 404: 0, 405: 0, 500: 0}
fileSize = 0
try:
    for line in stdin:
        data = verify_line(line)
        if data:
            fileSize += data['size']
            status[data['status']] += 1
            i += 1
        if i == 10:
            displayData(status, fileSize)
            i = 0
except KeyboardInterrupt:
    displayData(status, fileSize)