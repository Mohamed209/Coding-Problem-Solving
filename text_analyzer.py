#This is an example project, showing a program that analyzes a sample file
#to find count of each character in the text
import string
d = dict.fromkeys(string.ascii_lowercase,0)#dictionary of ascii char to map each time char found with count
def get_words_list_fromfile(filepath):
    with open(filepath) as file:
        lines=file.readlines()#read files line by line
        wordslist=[]#list for saving every word
        for line in lines :
            wordslist.append(line.split())
    file.close()
    return wordslist
def count_chars(word):
    for char in word:
        if char in d:
            d[char]=d[char]+1
        else:
            continue
list_of_words=get_words_list_fromfile("test.txt")#"test.txt"should be saved in current working directory or you may send the function file path
for wordsperline in list_of_words:
    for word in wordsperline:
        count_chars(word)
print(d)
