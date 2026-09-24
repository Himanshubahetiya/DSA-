# Example: "swiss" → 1 (the character w)
s = "swiss"
s = s.lower()
dict = {}

for i in s:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1


for key, value in dict.items():
    if value == 1:
        print(key)
        break
