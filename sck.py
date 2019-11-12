string = input("Enter the sentence:")

stop_words = {'ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out',
              'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its',
              'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as',
              'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these',
              'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should',
              'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all',
              'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does',
              'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did',
              'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which',
              'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against',
              'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than',}


spl = string.split(" ")
main_words = []
f = open("C:\\Users\\LENOVO\\Desktop\\sa.txt", 'r+')
l = []
for word in f.read().split():
    l.append(word)
for i in spl:
    if i not in stop_words:
        main_words.append(i)
print(main_words)
for i in range(0,len(main_words)):
    for j in range(0,len(l)):
        if main_words[i] == l[j]:
            print("true")
            j=j+1
            print(main_words[i])




