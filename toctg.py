import os
mas=[]
f=open('slova.txt','r',encoding='UTF-8')
z=0
for x in f:
    z=z+1
    print(z)
    ms=x.split('|')
    slovo=ms[0].strip()
    ctg=ms[1].strip()
    if(not('/' in ctg)):
        f2=open('categories/'+ctg+'.txt','a',encoding='UTF-8')
        f2.write(slovo+'\n')
        f2.close()
f.close()

