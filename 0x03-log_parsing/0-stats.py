#!/usr/bin/python3
"""A module for simple log parsing"""

from sys import stdin
from datetime import datetime


def verify_line(line):
    """verify a line fits a particular syntax"""
    data = {}
    status = [200, 301, 400, 401, 403, 404, 405, 500]
    if line and isinstance(line, str):
        lineBreak = line.split()
        if len(lineBreak) == 9:
            data['ip'] = lineBreak[0]
            data['date'] = ' '.join(lineBreak[2:4])
            data['req'] = ' '.join(lineBreak[4:7])
            data['status'] = lineBreak[7]
            data['size'] = lineBreak[8]
            try:
                data['status'] = int(data['status'])
                data['size'] = int(data['size'])
            except ValueError:
                pass
            else:
                if data['status'] in status:
                    return data


def displayData(status, fileSize):
    """display data to output"""
    print(f"File size: {fileSize}")
    fileSize = 0
    stats = sorted(status)
    for j in stats:
        if status[j] > 0:
            print(f"{j}: {status[j]}")


if __name__ == "__main__":
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
        raise
    else:
        displayData(status, fileSize)
