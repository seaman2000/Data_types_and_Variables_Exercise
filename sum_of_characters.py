number_of_characters = int(input())

result = 0

for each_char in range(number_of_characters):
    char = input()
    result += ord(char)

print(f"The sum equals: {result}")