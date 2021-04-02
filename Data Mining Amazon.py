'''
Luke Carlson
This program shows the best and worst stock of Amazon
'''
Volume1 = 0
AdjClose1 = 0
Date = 0
data_list = []
def get_data_list(File_Name):
    with open(File_Name) as file:#Use this file
        for line in file:#Create file one line at a time
            data_list.append(line.strip().split(','))
get_data_list("amazon.txt")
mastertuple = [] #The mastertuple switches between being a list and a tuple frequently

def get_monthly_averages(data_list):
    line = 1#DO NOT MOVE
    while(0 == 0):#HANDLES ALL MONTHS
        Endmonth = 0
        Volume1 = 0
        Month = 0
        VolumeN = 0
        AdjCloseN = 0
        MonthVar = data_list[:][line][0][5:7]
        while(Endmonth != -1):#HANDLES MONTH
            Date = data_list[:][line][0][:7]
            Volume1 = float(data_list[:][line][5])
            AdjClose1 = float(data_list[:][line][6])
            AdjCloseN += Volume1 * AdjClose1
            VolumeN += Volume1
            average_price = AdjCloseN / VolumeN
            average_price ="%.2f" % average_price
            line += 1
            if (MonthVar != data_list[:][line][0][5:7]):
                Adjvar = (float(average_price), data_list[:][line - 1][0][:7])
                mastertuple.append(Adjvar)
                Month += 1
                Endmonth = -1
        if(data_list[:][line][0] == "."):
            break
    mastertuple.sort()

    a1 = (mastertuple[0][1],mastertuple[0][0])
    a2 = (mastertuple[1][1],mastertuple[1][0])
    a3 = (mastertuple[2][1],mastertuple[2][0])
    a4 = (mastertuple[3][1],mastertuple[3][0])
    a5 = (mastertuple[4][1],mastertuple[4][0])
    a6 = (mastertuple[5][1],mastertuple[5][0])
    z1 = (mastertuple[76][1],mastertuple[76][0])
    z2 = (mastertuple[77][1],mastertuple[77][0])
    z3 = (mastertuple[78][1],mastertuple[78][0])
    z4 = (mastertuple[79][1],mastertuple[79][0])
    z5 = (mastertuple[80][1],mastertuple[80][0])
    z6 = (mastertuple[81][1],mastertuple[81][0])

    bestmon = (a1, a2, a3, a4, a5, a6)
    worstmon = (z1, z2, z3, z4, z5, z6)

    with open('Output.txt', 'w') as fp:
        fp.write("Amazon Stock from Jan 1, 2008 to Oct. 28, 2014\nSix Worst Months:\nMonth   Average")
        fp.write("\n")
        fp.write('\n'.join('%s %s' % x for x in worstmon))
        fp.write("\n\nSix Best Months:\nMonth   Average")
        fp.write("\n")
        fp.write('\n'.join('%s %s' % x for x in bestmon))
        fp.close()

get_monthly_averages(data_list)




