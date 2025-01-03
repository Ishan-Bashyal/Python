#reverse of a string a="programming". 

a = 'programming'
print("Reversed is: ", end="")
i = len(a) - 1

while i >= 0:
    print(a[i], end="")
    i -= 1
