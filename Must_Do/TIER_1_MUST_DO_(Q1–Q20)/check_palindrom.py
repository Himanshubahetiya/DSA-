s = "A man, a plan,%,&, @ a canal: Panama"

# s = s.lower()
# s = s.split()
# f = ''.join(s)
# f = f.replace(",", "")
# f = f.replace(":", "")

# rev = ""
# for i in f:
#     rev = i + rev

# if rev == f:
#     print("true")

f = ""

for i in s.lower():
    if i.isalnum():
        f += i


rev = ""

for i in f:
    rev =  i + rev

if rev == f:
    print("true")
else:
    print("false")



