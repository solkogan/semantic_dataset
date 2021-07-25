import os
mas=[]
f=open('slova.txt','r',encoding='UTF-8')
z=0
for x in f:
    z=z+1
    print(z)
    ms=x.split('|')
    slovo=ms[0]
    ctg=ms[1]
    prefix=slovo[0:2]
    if(len(prefix)>=2 and not('/' in prefix)):
        flag=0
        if(os.path.exists('words/'+prefix+'.txt')):
            f3=open('words/'+prefix+'.txt','r',encoding='UTF-8')
            for xx in f3:
                if(xx==x):
                    flag=1
            f3.close()
        if(flag==0):
            f2=open('words/'+prefix+'.txt','a',encoding='UTF-8')
            f2.write(x)
            f2.close()
f.close()

