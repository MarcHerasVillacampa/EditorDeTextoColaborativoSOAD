
import time

def insertInTxt(file,position,text):
    
    print(f"insertInTxt({file},{position},{text})")
    with open(file, 'r+') as f:
        content = f.read()
        print("contenido : ",content)
        f.seek(position)
        f.write(text)
        f.flush()
        print("texto insertado : ",content)
        print(f.read())
        f.truncate()
        print(f.read())
        f.write(content[position:])
        f.flush()
        print(f.read())
        f.close()
    


# def insertInTxt(file,position,text):
#     print("Meter en el TXT esto ------------->",text)
#     with open(file, 'a') as f:
#         f.write(text)
#         f.flush()
#         f.close()


def ereaseInTxt(file,position,amount):
    print(f"ereaseInTxt({file},{position},{amount})")
    text=""
    with open(file, 'r+') as f:
        text = f.read()
        f.truncate(0)
        f.flush()
       
        # print("algo ",text[int(position)+int(amount):])
        f.close()
    with open(file, 'a') as f:
         f.write(text[0:10]+text[11:])
    
        

# ereaseInTxt("foo.txt",2,2)
# for i in range(20):
#     insertInTxt("prueba.txt",0,"-")

ereaseInTxt("foo.txt",2,2)