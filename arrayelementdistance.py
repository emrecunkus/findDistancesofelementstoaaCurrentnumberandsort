num_array = [1, 2, 3, 4, 5]
Ordinary_Array = list()
Result = list()

Key_Number = 3

i = 0

while i < len(num_array):
    num = num_array[i]

    sub = abs(num - Key_Number)

    Ordinary_Array.append(sub)
    i += 1

Ordinary_Array.sort()
j = 0
print(Ordinary_Array)

for j in Ordinary_Array:

    a = j + Key_Number
    b = Key_Number - j
    if a in num_array:
        num_array.remove(a)
        Result.append(a)

    elif b in num_array:
        num_array.remove(b)
        Result.append(b)

print(Result)
