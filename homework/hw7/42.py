#Write a for loop that removes all vowels (a, e, i, o, u) from a string.

vowels = ['a', 'e', 'i', 'o', 'u']
str = "notaaeiou"
result = ""
i = 0

while i < len(str):
    if str[i] not in vowels:
        result += str[i]
    i += 1

print(result)
