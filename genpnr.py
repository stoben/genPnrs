
import sys
import datetime


def main(arg):

    # if len(arg) < 2:
    #     print("Invalid number of arguments")
    #     return        
    # else:
    
    #edit datespan here to generate numbers from to date (here 1970 to 1980)
    generateFile(datetime.datetime(1970,1,1), datetime.datetime(1980,1,1))


def generateFile(start, stop:datetime):


    
    count = start
    #personNumber = 1
    while(count <= stop):         
        for personnr in range(1000):
            getPnr("{0:02d}{1:02d}{2:02d}{3:03d}".format(count.day, count.month, int(count.strftime("%y")), personnr))
        count += datetime.timedelta(days=1)



def getPnr(dtpnr):
    sum = 0
    multiplier = 2
    constPre = [3,7,6,1,8,9,4,5,2,1]
    constPost = [5,4,3,2,7,6,5,4,3,2,1]

    num1 = 0
    num2 = 0

    c = 0
    for i in dtpnr:        
        if c < 9:
            num1 += int(i) * constPre[c]         
            num2 += int(i) * constPost[c]
        c += 1
    
    #check control    
    num1 = num1 % 11
    if num1 != 0:
        num1 = abs(11 - num1) #mod11

    if num1 == 10: 
        return None

    
    num2 += num1 * constPost[9]
    
    num2 = num2 % 11
    if num2 != 0:
        num2 = abs(11 - num2) #mod 11

    if num2 == 10:
        return None #not usable
    

    return print("{0}{1}{2}".format(dtpnr, num1, num2))
    



if __name__ == '__main__':
    main(sys.argv[1:])
