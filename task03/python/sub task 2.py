import csv
d=[]
put=input("stuff ")
d.append(put)
with open("/home/sreejith-m/Desktop/program/input.txt","w",newline='') as f:
    write=csv.writer(f)
    f.write(' '.join(d))
    f.close()
with open("/home/sreejith-m/Desktop/program/input.txt","r",) as e:
    read=csv.reader(e,delimiter=' ')
    for i in read:
        print(i)
with open("/home/sreejith-m/Desktop/program/output.txt","w") as g:
    writing=csv.writer(g)
    g.write(' '.join(i))
    f.close()