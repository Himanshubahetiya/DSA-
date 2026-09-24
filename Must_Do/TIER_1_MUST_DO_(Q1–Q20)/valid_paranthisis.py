# Example: "()[]{}" → True, "(]" → False
s = "(){}[]"

stack = []

pairs = {
    "}":"{",
    "]":"[",
    ")":"("
}

for ch in s:
    if ch in pairs:
        if not stack or stack.pop() != pairs[ch]:
            print("False")
            break

    else:
        stack.append(ch)

else:
    if not stack:
        print("true")
    else:
        print("false")