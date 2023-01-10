#!/usr/bin/python3
'''
Script for log parsing
'''
import sys


if __name__ == "__main__":
    a = []
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    dictio = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
              "405": 0, "500": 0}
    i = 0
    file_size = 0
    try:
        for lines in sys.stdin:
            a = lines.split(" ")
            if "\n" in a[-1]:
                value = a[-1][:-1]
            else:
                value = a[-1]
            if len(a) > 2 and a[-2] in codes and value.isnumeric() is True:
                dictio[a[-2]] += 1
                file_size += int(value)
                i += 1
            if i % 10 == 0:
                print("File size: {}".format(file_size))
                for code in codes:
                    if dictio[code] > 0:
                        print("{}: {}".format(code, dictio[code]))
        exit()
    except Exception:
        pass
    finally:
        print("File size: {}".format(file_size))
        for code in codes:
            if dictio[code] > 0:
                print("{}: {}".format(code, dictio[code]))
