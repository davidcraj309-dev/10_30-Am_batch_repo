# get unic ip ID . from the loge the request
# get how many 200,300,400 error code
# write the result to csv file


import os

path = "C:\\Users\\Yesu\\OneDrive\\Documents\\Desktop\\"

myfile = "mylog.log"


##1.Reads first 100 content using read mode

""" print(os.path.join(path,myfile))

with open(os.path.join(path,myfile)) as f:
    content  = f.read()
    print(content[:100]) """


##2.Reads first line content using read mode

""" with open(os.path.join(path,myfile)) as f:
    for each in f:
        print(each)
        break """

##3.need find user_id and status code from log file

""" 
import os

path = "C:\\Users\\Yesu\\OneDrive\\Documents\\Desktop"
myfile = "mylog.log"

with open(os.path.join(path,myfile)) as f:
    for each_line in f:
        print(each_line.split(" "))
        break """

##4.need pick user_id[3] and status code[8] from log file

""" import os

path = "C:\\Users\\Yesu\\OneDrive\\Documents\\Desktop"
myfile =  "mylog.log"

with open(os.path.join(path,myfile)) as f:
    for each_line in f:
        mylist = each_line.split(" ") #the spilted list assigned to  mylist(variable)

        ip,http_status = mylist[3],mylist[8] #stored in ip,http_status varible and Filtered
        print(http_status)
        print(ip)
        break """

##5.to save and append this user_id and status code need store[] in varibale


import os
import csv

path = "C:\\Users\\Yesu\\OneDrive\\Documents\\Desktop"
myfile =  "mylog.log"


ip = []
http_status = []
mydict = {}


with open(os.path.join(path,myfile)) as f:
    for each_line in f:
        mylist = each_line.split(" ")
        ip.append(mylist[3])
        http_status.append(mylist[8])

    # print(ip)
    # print(http_status)


##5.need to count frequency for ip, http_status using func frequency(mylist)



def frequency(mylist):

    for each in mylist:
        if each not in mydict:
            mydict[each] = 1
        else:
            mydict[each] += 1

    return mydict



##6.need save in csv file 

def write_to_csv(mydict):
    with open(os.path.join(path,"new_csv.csv"),"a",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Sno","http_status","Freqency"])
        Sno = 1

        for each in mydict:
            writer.writerow([Sno,each,mydict[each]])
            Sno += 1

rest1 =  frequency(ip)
rest2 =  frequency(http_status)

write_to_csv(rest1)
write_to_csv(rest2)

print("csv file created Sucessfully")



