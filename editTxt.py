
def insertInTxt(file,position,text):
    print("Meter en el TXT esto ------------->",text)
    with open(file, 'r+') as f:
        content = f.read()
        f.seek(position)
        f.write(text)
        f.flush()
        f.truncate()
        f.write(content[position:])
        f.close()

def ereaseInTxt(file,position,amount):
    print("Borrar en el TXT esto ------------->",position," ",amount)
    with open(file, 'r+') as f:
        text = f.read()
        f.seek(position)
        f.truncate()
        f.write(text[int(position+1)+int(amount):])
        f.flush()
        f.close()
