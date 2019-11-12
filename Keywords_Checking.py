from nltk.corpus import stopwords
string = input("enter the sentence:")
stop_words = set(stopwords.words('english'))
spl = string.split(" ")
a = []
f = open("C:\\Users\\LENOVO\\Desktop\\sa.txt", 'r+')
l = []
for word in f.read().split():
    l.append(word)
for w in spl:
    if w not in stop_words:
        a.append(w)
print(spl)
print(a)
for i in range(0,len(a)):
    for j in range(0,len(l)):
        if a[i] == l[j]:
            print("true")
            j=j+1
            print(a[i])
