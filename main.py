answer = 0
check = 0
result = []
str = ""
for x in s:
    if x.isdigit() == False:
        str += x
        print(str)
        check += {"zero" : 1, "one" : 1, "two" : 1, "three" : 1, "four" : 1, "five" : 1, "six" : 1, "seven" : 1, "eight" : 1, "nine" : 1}.get(str, 0)
        if check == 1:
            print(str)
            result.append({"zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}.get(str))
            str = ""
            check = 0
    else:
        result.append(x)

print(result)
print(int(''.join(result)))