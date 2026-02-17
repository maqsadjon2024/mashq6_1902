#87
import random

def random_list(n,a=0,b=100):
    return [random.randint(a,b) for _ in range(n)]

print(random_list(5))

#88
def uniq_words(text):
    words = text.split()
    return ' '.join(dict.fromkeys(words))

print(uniq_words("olma anor olma uzum anor"))

#89
def harf_raqam(text):
    return [ord(c)-96 for c in text if c.isalpha()]

print(harf_raqam("abc"))

#90
def to_seconds(h,m,s):
    return h*3600 + m*60 + s

print(to_seconds(1,30,15))
