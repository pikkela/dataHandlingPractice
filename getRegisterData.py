import urllib3


def getData():
    http = urllib3.PoolManager()

    r = http.request('GET', 'https://raw.githubusercontent.com/pikkela/gamchall/main/registerData.txt')

    return r.data

def getRegisters():
    with open('registers.txt', 'r', encoding='utf-8') as f:
        registers = f.readlines()
    return registers