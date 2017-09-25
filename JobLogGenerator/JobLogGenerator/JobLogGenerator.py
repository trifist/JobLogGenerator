# coding: utf-8 
# created by wpcheng 
# Sept. 25th, 2017
import random

ecarxLogs = []
neusoftLogs = []
ecarxLogNumber = random.randint(8, 12)
neusoftLogNumber = random.randint(8, 12)


def readAllLogs():
    fEcarx = open("./ecarx.txt", "r", encoding="utf8")
    for line in fEcarx.readlines():
        ecarxLogs.append(line)
    fEcarx.close()

    fNeusoft = open("./neusoft.txt", "r", encoding="utf8")
    for line in fNeusoft.readlines():
        neusoftLogs.append(line)
    fNeusoft.close()

def generateEcarx():
    if(len(ecarxLogs) < 1):
        return
    logSet = set([])
    while (len(logSet) <= ecarxLogNumber):
        index = random.randint(0, len(ecarxLogs)-1)
        logSet.add(ecarxLogs[index])
    print("ecarx:")
    for log in logSet:
        print(log)
def generateNeusoft():
    if(len(neusoftLogs) < 1):
        return
    logSet = set([])
    while (len(logSet) <= neusoftLogNumber):
        index = random.randint(0, len(neusoftLogs)-1)
        logSet.add(neusoftLogs[index])
    print("neusoft:")
    for log in logSet:
        print(log)


def main():
    readAllLogs()
    generateEcarx()
    generateNeusoft()

if(__name__ == "__main__"):
    main()