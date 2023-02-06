
"""
given=(('333', '33'), ('1416', '55'))
res=[]
for x in given:
    temp=[]
    for y in x:
        temp.append(int(y))
    res.append(tuple(temp))
print(tuple(res))
        
"""
"""
L1=[ [1, 2, 3], True,  [11, 12, 13], [  14 , False] ]
L2=[ [11, 12, 3], True,  [21, 22, 13], [  24 , False] ]
s1=set()
s2=set()
for x in L1:
    if(isinstance(x,list)):
        for y in x:
            s1.add(y)
    else:
        s1.add(x)
for x in L2:
    if(isinstance(x,list)):
        for y in x:
            s2.add(y)
    else:
        s2.add(x)
print(f"s1: {s1}")
print(f"s2: {s2}")
s_common=s1.intersection(s2)
print("common= ",end='')
print(s_common)
val=1
for x in s_common:
    val=val*x
print(val)

s_diff=s1.symmetric_difference(s2)
print("not common= ",end='')
print(s_diff)
val=1
for x in s_diff:
    val=val*x
print(val)

s_union=s1.union(s2)
print("union= ",end='')
print(s_union)
val=1
for x in s_union:
    val=val*x
print(val)

s_diff2=set()
for x in s_union:
    if x not in s_common and x in s1:
        s_diff2.add(x)
val=1
for x in s_diff2:
    val=val*x
print(f"s_diff2: {s_diff2}")
print(val)
"""
"""

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
res=dict()
for key,value in dic1.items():
    res[key]=value
for key,value in dic2.items():
    res[key]=value
for key,value in dic3.items():
    res[key]=value
print(res)

"""
"""
given = {1:10, 2:20}
x=int(input("enter a key: "))
if(given.get(x) is not None):
    print(f"Exists {given[x]}")
else:
    print("Not Exists")
"""
"""
n=int(input("Enter n value: "))
res=dict()
for i in range(1,n+1):
    res[i]=i*i
print(res)
"""
"""
given={'data1':100,'data2':-54,'data3':247}
res=1
for val in given.values():
    res=res*val
print(res)

"""
"""
given={1:10, 2:20}
max_val=-99999
min_val=999999
for val in given.values():
    max_val=max(max_val,val)
    min_val=min(min_val,val)
print(f"max val={max_val}")
print(f"min val={min_val}")
"""
"""
dict_1={'a': 100, 'b': 200, 'c':300}
dict_2={'a': 300, 'b': 200, 'd':400}
for key,value in dict_2.items():
    if(key in dict_1):
        dict_1[key]=dict_1[key]+value
    else:
        dict_1[key]=value
print(dict_1)
"""

"""
res=set()
given=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
for x in given:
    for val in x.values():
        res.add(val)
print(res)
"""
"""
given={'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
temp=[]
for key,val in given.items():
    temp.append([val,key])
temp.sort(reverse=True)
for i in range(0,3):
    print(temp[i][1])
"""

"""
given={'Math':81, 'Physics':83, 'Chemistry':87}
temp=[]
for key,val in given.items():
    temp.append((key,val))
temp.sort(key=lambda x:x[1],reverse=True)
print(temp)

"""
"""
list1=['S001', 'S002', 'S003', 'S004']
list2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
list3=[85, 98, 89, 92]
n=len(list1)
res=dict()
for i in range(0,n):
    res[list1[i]]={list2[i]:list3[i]}
print(res)
"""
"""
given={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
res=[]
temp=[]
for key,value in given.items():
    temp.append([key,value])
key1=temp[0][0]
key2=temp[1][0]
for i in range(0,len(temp[0][1])):
    res.append({key1:temp[0][1][i],key2:temp[1][1][i]})
print(res)

"""
"""
given={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
for key,val in given.items():
    n=len(val)
    i=0
    while(i<len(val)):
        if(val[i]%2!=0):
            val.pop(i)
        else:
            i=i+1
print(given)
"""
"""
test_list= ["Gfg","is","Best"]
subs_dict = {"Gfg":[5,6,7],"is":[7,4,2]}
k = 0
n=len(test_list)
for i in range(0,n):
    if(subs_dict.get(test_list[i]) is not None):
        test_list[i]=subs_dict[test_list[i]][k]
print(test_list)

"""
"""
given="Geeks for Geeks and Geeks for Geeks is great Website"
print(' '.join(dict.fromkeys(given.split())))

"""
"""
s=3
given="paradox"
given=list(given)
n=len(given)
for i in range(s-1,n):
    given[i]=chr(ord('z')-(ord(given[i])-ord('a')))
print("".join(given))

"""
"""

given=[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
res=dict()
for x in given:
    if(res.get(x) is not None):
        res[x]=res[x]+1
    else:
        res[x]=1
for key,val in res.items():
    print(f"{key} : {val}")
    
"""
"""

string1="Hello"
string2="dnaKfhelddf"
check=dict()
for x in string2:
    if(check.get(x) is not None):
        check[x]=check[x]+1
    else:
        check[x]=1
flag=True
for x in string1:
    if(check.get(x) is None):
        print("Not possible")
        flag=False
        break
    else:
        if(check[x]==0):
            print("Not Possible")
            flag=False
            break
        else:
            check[x]=check[x]-1
if(flag):
    print(True)

"""
"""

test_dict={1:"Gfg is love", 2: "Gfg is good"}
sub_list=["love", "good"]
temp=[]
for x in sub_list:
    for key,val in test_dict.items():
        if x in val:
            temp.append(key)
for x in temp:
    test_dict.pop(x)
print(test_dict)
"""
""" 

data="Tendulkar took up cricket at the age of eleven, made his Test match debut on 15 November 1989 against Pakistan in Karachi at the age of sixteen, and went on to represent Mumbai domestically and India internationally for close to twenty-four years. In 2002, halfway through his career, Wisden ranked him the second-greatest Test batsman of all time, behind Don Bradman, and the second-greatest ODI batsman of all time, behind Viv Richards.[9] Later in his career, Tendulkar was part of the Indian team that won the 2011 Cricket World Cup, his first win in six World Cup appearances for India.[10] He had previously been named "Player of the Tournament" at the 2003 edition of the tournament.

Tendulkar received the Arjuna Award in 1994 for his outstanding sporting achievements, the Khel Ratna Award, India's highest sporting honour, in 1997, and the Padma Shri and Padma Vibhushan awards in 1999 and 2008, respectively, two of India's highest civilian awards.[11][12] A few hours after the end of his last match in November 2013, the Prime Minister's Office announced the decision to award him the Bharat Ratna, India's highest civilian award.[13][14] As of 2021, he is the youngest recipient to date and was the first sportsperson to receive the award.[15][16] In 2012, Tendulkar was nominated to the Rajya Sabha, the upper house of the Parliament of India."
data=data.split()
print(data)
"""
"""

import pandas as pd

f=pd.read_csv("/Users/kothapallygnanapraneeth/Downloads")
"""
"""
f=open("/Users/kothapallygnanapraneeth/Downloads/hypothyroid.csv",'w+').readlines()
n=791
path="/Users/kothapallygnanapraneeth/Downloads/"
number=1
for i in range(0,4):
    f = open(path+str(number)+".csv",'w+').writelines(f[i*791:(i+1)*791])
    number=number+1

"""
"""

file_path=
output=
f=open(file_path,"r")
data=f.read()
f.close()
data=data.split('\n)
data=data[::-1]
print(f"len(data)={len(data)} and type(data)={type(data)}")
no_of_file=4
rows_in_each_file=len(data)//no_of_files
start=0
for i in range(1,no_of_files+1):
                output_file=output+'\\'+f"File_{i}.txt"
                output_file_csv=output+'\\'+f"File_{i}.csv"
                csv_f=open(output_file_csv,"w")
                txt_f=open(output_file,"w")
                for j in data[start:start+rows_in_each_file]:
                   csv_f.write(j+'\n')
                   txt_f.write(j[::-1]+"\n")
                
output_file=output+'\\'+f"File_{i}.txt"
output_file_csv=output+'\\'+f"File_{i}.csv"
csv_f=open(output_file_csv,"w")
txt_f=open(output_file,"w")
                
"""







