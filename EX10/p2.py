d="Dr. Kalam was President of India"
f=open("viz.txt","w")
f.write(d)
with open("viz.txt","r+") as f:
    t=f.read()
    print(t)
    print("Current Cursor Position: ",f.tell())
    print("After Change the seek() position:")
    f.seek(14)
    print("Current Cursor Position: ",f.tell())
    f.write("|a Good Human being|")
    f.seek(0)
    t=f.read()
    print(t)
