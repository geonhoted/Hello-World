even = ['a', 'e', 'i', 'u', 'o', 'A', 'E', 'I', 'U', 'O']
count = 0

while (True):
    word = input()
    if word == '#':
        break
    else:
        count = 0
        for letter in word:
            if letter in even:
                count += 1
    print(count)