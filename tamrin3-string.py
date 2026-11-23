#تمرین دوم : الگوریتم تحلیل رشته 
s = input("Enter a string: ")

words = s.split()

print("Number of words:", len(words))

print("Number of characters:", len(s))

max_char = max(s, key=s.count)
print("Most repeated character:", max_char)

for word in set(words):
    print(word, ":", words.count(word))