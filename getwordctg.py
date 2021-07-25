import os

def getcat(txt):
    txt=txt.strip().lower()
    mas=[]
    prefix=txt[0:2]
    if(os.path.exists('words/'+prefix+'.txt')):
        f=open('words/'+prefix+'.txt','r',encoding='UTF-8')
        for x in f:
            x=x.strip()
            ms=x.split('|')
            slovo=ms[0].strip()
            ctg=ms[1].strip()
            if(slovo==txt):
                mas.append(ctg)
    if(mas==[]):
        return None
    else:
        return mas

def getwords(ctg):
    mas=[]
    if(os.path.exists('categories/'+ctg+'.txt')):
        f=open('categories/'+ctg+'.txt','r',encoding='UTF-8')
        for x in f:
            if(not(' ' in x.strip())):
                mas.append(x.strip())
        f.close()
    if(mas==[]):
        return None
    else:
        return mas
        
