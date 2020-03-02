seq=input("please enter the sequence")
n=int(input("please enter the value of n"))
patternlist=[]
seq_counter=seq.count("A")+seq.count("T")+seq.count("C")+seq.count("G")
last_k_mer= seq_counter - n +1
print(seq_counter)
print(last_k_mer)
all_sub_string1=range(0,last_k_mer)
all_sub_string2=range(n,len(seq))
print(all_sub_string1)
print(all_sub_string2)
for i in range(0,last_k_mer):
    x=seq[i:i+n]
    patternlist.append(x)
print(patternlist)
listofcount=[]
for j in range(len(patternlist)):
    c=patternlist.count(patternlist[j])
    z=print(patternlist[j],c)
    listofcount.append(patternlist.count(patternlist[j]))
print(listofcount)
max=0
for k in listofcount:
    if listofcount[k]> max:
        max=listofcount[k]
        print(k)
        print(patternlist[k])



    
    


    
    
   
    
