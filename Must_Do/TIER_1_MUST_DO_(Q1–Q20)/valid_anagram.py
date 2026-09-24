# Example: "listen", "silent" → True
s1 = "listeN"
s2 = "silenT"
s1 = s1.lower()
s2 = s2.lower()

if len(s1) != len(s2):
    print("false")

else:

    dict = {}

    for i in s1:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for i in s2:
        if i in dict:
            dict[i] -= 1
        else:
            print("False")
            break

    else:

        for value in dict.values():
            if value != 0:
                print("false")
                break
        else:
            print("true")