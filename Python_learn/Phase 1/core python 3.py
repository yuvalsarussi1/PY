name = input("enter name")
vowel_count = 0


for index, letter in enumerate(name, start=1):
    if letter.lower() in "aeiou":
        vowel_count += 1
    print(index, letter)
print("number of words =",len(name),"number of vowels =", vowel_count)

    
    