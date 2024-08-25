import csv
d=[]
x=int(input("enter value of n "))
d.append(x)
with open("/home/sreejith-m/Desktop/program/input.txt","w",newline='') as no:
    write= csv.writer(no)
    write.writerow(d)
    no.close()
with open("/home/sreejith-m/Desktop/program/input.txt","r") as read:
    reading=csv.reader(read)
    for i in reading:
        s=' '.join(i)
        p=int(s)
        q=p//2
        z=1
        if p%2==0:
            p+=1
        c=p
    with open("/home/sreejith-m/Desktop/program/output.txt","w",newline='') as output:
        writes=csv.writer(output)
        for w in range(q,0,-1):
            b=w*" ",z*"*"
            writes.writerow(b)
            z+=2
        for e in range(0,q+1):
            d=e*" ",c*"*"
            writes.writerow(d)
            c-=2