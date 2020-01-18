# This is an example project, showing a program that analyzes a sample file
# to find count of each character in the text
# here is text file contents
'''Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcenfr fv orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabthu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orgnf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba bg thrff.
Gurer fubhyq or bar-- naq cersrenoylbayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arrire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!'''
import string
# dictionary of ascii char to map each time char found with count
d = dict.fromkeys(string.ascii_lowercase, 0)


def get_words_list_fromfile(filepath):
    with open(filepath) as file:
        lines = file.readlines()  # read files line by line
        wordslist = []  # list for saving every word
        for line in lines:
            wordslist.append(line.split())
    file.close()
    return wordslist


def count_chars(word):
    for char in word:
        if char in d:
            d[char] = d[char]+1
        else:
            continue


# "test.txt"should be saved in current working directory or you may send the function file path
list_of_words = get_words_list_fromfile("test.txt")
for wordsperline in list_of_words:
    for word in wordsperline:
        count_chars(word)
print(d)
