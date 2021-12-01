import os

dirList = os.listdir('reports/')
masterList = {} # dict of all securtiy reports, each entry will have 2 lists as values
# 1. data on person
# 2. list of clearances they are on

def parse(fname): # parse a security report
    with open(fname) as f: s = f.readlines()
    smallList = {} # dict of a security report with peoples data
    
    for i in s:
        if("EmplID:" in i): # grab just line with data
            lst = list(filter(None,i.strip().split(",")))
        
            ID = lst[1]
            lastName = lst[3]
            firstName = lst[5]
            cardNum = lst[7]
            name = lst[5] + " " + lst[3]

            if(cardNum == '#######'): # account for missing card number and grab next line
                cardNum = ''.join(filter(str.isdigit, s[s.index(i) + 1]))

            smallList[name] = []
            smallList[name].extend((firstName,lastName,ID,cardNum))

    return smallList

# add to smallLists to masterList and account for collisions

for dir in dirList:
    tempDict = parse('reports/' + dir)
    for key in tempDict.keys():
        if (key not in masterList.keys()):
            masterList[key] = [[],[]]
            masterList[key][0] = tempDict[key]
            masterList[key][1].append(dir.replace('.csv',''))
        else:
            masterList[key][1].append(dir.replace('.csv',''))

# Write out to file

with open('auditData.csv', 'w') as out:
    out.write("First Name,Last Name,Employee ID,Card Number,Clearance Group\n")
    
    for key in masterList.keys():
        info = ""
        for index in range(len(masterList[key][0])): # creates string of individuals data
            info += masterList[key][0][index]
            info += ","
        for clearance in masterList[key][1]: # print data + clearances
            out.write(info + clearance + '\n')