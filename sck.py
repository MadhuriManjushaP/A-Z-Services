from nltk.corpus import stopwords
import re
string = input("Enter the sentence:")
stop_words = set(stopwords.words())
spl =  re.findall(r"[\w']+", string)
print(spl)
main_words = []
for i in spl:
    if i not in stop_words:
        main_words.append(i)
print(main_words)
f = open("C:\\Users\\LENOVO\\Desktop\\sa.txt", 'r+')
l = []
main = []
for word in f.read().split():
    l.append(word)
for i in range(0, len(main_words)):
    for j in range(0, len(l)):
        if main_words[i] == l[j]:
            print("true")
            words = main_words[i]
            main.append(words)
            j = j + 1
print(main)