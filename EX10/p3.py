import os,sys
fn=input("Enter File Name: ")
if os.path.isfile(fn):
    print("File exist:",fn)
    f=open(fn,"r")
else:
    print("File does not exist:",fn)
    sys.exit(0)
lc=wc=cc=0
for l in f:
    lc=lc+1
    cc=cc+len(l)
    w=l.split()
    wc=wc+len(w)
print("Number of Lines Count:",lc)
print("Number of Words Count:",wc)
print("Number of Characters Count:",cc)

