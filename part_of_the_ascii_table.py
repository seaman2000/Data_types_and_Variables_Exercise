start_index = int(input())
end_index = int(input())

for char in range(start_index , end_index + 1):
    if char == end_index:
        print(chr(char))
        break
    print(chr(char), end = " ")