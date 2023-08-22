import csv
import numpy as np
data=[]
with open(r"C:\Users\pf3l1\Downloads\MER_T07_02A-2020-02-03.csv", 'r') as csvfile:
          file_reader=csv.reader(csvfile,delimiter=',')
          for row in file_reader:
                  data.append(row)
d= np.array(data)         
print(d)

#Q1
print(d.shape)
c=type(d)
print(c)

#Q2
print("data contained ",d[0:11,3])

#Q3
headers=d[0]
print("headers ",headers)

#Q4
print("data contained",d[0:21,1:3])

#Q5
print("data contained in first three rows",d[0:4,0:6]," \n data contained in last three rows",d[-3:])

#Q6
copy_array=d.copy()
copy_array=np.delete(copy_array,0,0)

sort_index=np.argsort(copy_array[:,2])
array_sort_netamount=copy_array[sort_index]
print("net amount of electricity geneerated",array_sort_netamount)
print("\n")


#Q8
print("unique sectors ")
l=np.unique(copy_array[:,4])
print(l)



#Q9
#mask = data[:, 4] == "Electricity Net Generation From Wind, All Sectors"
#filtered_data = data[mask]
#for row in filtered_data:
    #print("MSN:", row[0])
    #print("YYYYMM:", row[1])
    #print("Value:", row[2])
    #print("Column_Order:", row[3])
    #print("Description:", row[4])
    #print("Unit:", row[5])
    #print()




#for i in d[0:,4]==

#for i in d[0:,4]==13:

if d[0:,3]==13:
        print(d[0:,0:5])