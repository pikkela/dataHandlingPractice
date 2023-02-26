from pickle import FALSE, TRUE
from posixpath import split
import re
import getRegisterData
import json


regData = getRegisterData.getData()
regs = getRegisterData.getRegisters()
    
################ handle data from tuff meter #########################
sp = regData.decode().split('\r\n')
for line in sp:
    regIndex = line.find(':')
    dataIndex = len(line)
#print(sp)
######################################################################  


################ create json file from register txt #########################
def createJson():
    fields = ['REGISTER', 'NUMBER', 'VARIABLE NAME', 'FORMAT', 'NOTE']
    l = 1
    dict1 = {}
    for reg in regs:
        #register id to json file
        regId = 'regId_'+str(l)
        i = 0
        dict2 = {}

        while i<len(fields):
            #check if reg.split(,)[i] is out of range
            if i >= len(reg.split(',')):
                dict2[fields[i]] = ''
            else:
                atr = reg.split(',')[i]

                if '\n' in atr:
                    atr = atr.strip('\n')
                dict2[fields[i]] = atr
            i += 1
        dict1[regId] = dict2
        l += 1
        #convert REGISTER numbers to int and make it an array
        if '-' in dict1[regId]['REGISTER']:
            dict1[regId]['REGISTER'] = [int(dict1[regId]['REGISTER'].split('-')[0]), int(dict1[regId]['REGISTER'].split('-')[1])]
        else:
            dict1[regId]['REGISTER'] = [int(dict1[regId]['REGISTER'])]


    #print(json.dumps(dict1, indent = 4, sort_keys=True))
    #save json file
    out_file = open('registers.json', 'w')
    json.dump(dict1, out_file, indent = 4, sort_keys=True)
    #close register file
    out_file.close()
######################################################################
#createJson()

################ create json file from registers.json and sp #########################
fields = ['DATE', 'TIME', 'DATA', 'NOTE', 'FORMAT', 'NUMBER', 'VARIABLE NAME',]
f = open('registers.json', 'r')
data = json.load(f)
i = 1
date = sp[0].split(' ')[0]
time = sp[0].split(' ')[1]
print(date + ' ' + time)
for a in sp:
    print(a)

dict1 = {}
dict2 = {}

while i < len(data):
    regId = "regId_"+str(i)
    dict2[fields[0]] = date
    dict2[fields[1]] = time
    dict2[fields[2]] = time
    dict2[fields[3]] = json.dumps(data[regId]["NOTE"], indent = 4, sort_keys=True)
    dict2[fields[4]] = json.dumps(data[regId]["FORMAT"], indent = 4, sort_keys=True)
    dict2[fields[5]] = json.dumps(data[regId]["NUMBER"], indent = 4, sort_keys=True)
    dict2[fields[6]] = json.dumps(data[regId]["VARIABLE NAME"], indent = 4, sort_keys=True)
    dict1[regId] = dict2
    #print(json.dumps(data[regId], indent = 4, sort_keys=True))
    # print(json.dumps(data[regId]["FORMAT"], indent = 4, sort_keys=True))
    # print(json.dumps(data[regId]["NUMBER"], indent = 4, sort_keys=True))
    # print(json.dumps(data[regId]["VARIABLE NAME"], indent = 4, sort_keys=True))
    i += 1
#print(dict1)
