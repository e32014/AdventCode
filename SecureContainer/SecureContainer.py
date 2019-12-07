
def guessCheck(value):
    hasTwo = False
    onlyIncrease = True
    strVal = str(value)
    for i in range(0, len(strVal) - 1):
        if strVal[i] == strVal[i+1]:
            if not((i+2 < len(strVal) and strVal[i+1] == strVal[i+2]) or (i-1>=0 and strVal[i-1] == strVal[i])):
                hasTwo = True
        if int(strVal[i]) > int(strVal[i+1]):
            onlyIncrease = False
    return onlyIncrease and hasTwo

found = 0

for i in range(246515, 739106):
    if guessCheck(i):
        found += 1

print(found)