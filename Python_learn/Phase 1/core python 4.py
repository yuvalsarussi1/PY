word_enter = input("enter sentence")
words = word_enter.split()
print("number of words=",len(words))
print(words[::-1])

for word in words:
 print(word[::-1])



new = (max(words, key=len))
print(new.upper())



