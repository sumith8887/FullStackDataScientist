word_count=0
with open("file1.txt","r") as f1:
    text=f1.read()
    words=text.split()
    print(len(words))
