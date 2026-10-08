def count_the_occurences():
    with open("sample.txt",'r') as file:
        content=file.read()
        words=content.lower().split()
        count=0
        for w in words:
            if w.find("program")==0 and len(w)==7:
                count+=1
        print("The word 'program' occurred")
        print(count)
        print("Times in the file")
count_the_occurences()
