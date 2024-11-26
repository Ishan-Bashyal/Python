a= "python\'s"
print (a)


b="python\nprogramming"
print(b)


c="python\b programming"
print(c)


d="python\tprograming"
print(d)

print('python\t program'.expandtabs(tabsize=4))


e="python\rabc"
print(e)
#abc replaces pyt


f="pyt\rabcabc"
print(f)


print(r'Hello\n python')
print(R'Hello\bHello\n python')


print('C:users\\python')


g="python"
print(g.upper())


h="PYTHON"
print(h.lower())


i="python programming"
print(i.capitalize())


j="python programming"
print(j.title())


k="python"
print(k.center(11,'*'))

#if string length is odd 
#left side= n-1/2
#right side= n+1/2

#if string is even (python is even n=6)
#left side= n+1/2
#right side= n+1/2


l="python"
print(l.ljust(10,'*'))


m="python"
print(m.rjust(10,'*'))


n="pythonp"
print(n.find('p'))
print(n.rfind('p'))
print(n.index('p'))
print(n.rindex('p'))

o="pythonp"
p=o.rfind('t')
q=p-len(o)
print(q)

print(n.count('p'))


r="python"
print(r.center(11,'*'))

s='PYThon'
print(s.swapcase())


t='PYThon'
print(t.replace('PY','z'))
#if other characters except python it doesnt replace anything and shows PYThon


# a-z=97-122
# A-Z=65-90
# 0-9=48-57


u='python'
v=u.maketrans('pxk','wxk')
print(u.translate(v))
# replacement using two characters ends with error


w='x2'
print(w.zfill(7))

x='python'
print(x.startswith('py'))
print(x.endswith(''))


y='Python1'
print(y.isupper())
print(y.islower())
print(y.istitle())
print(y.isalpha()) #All should be alphabet
print(y.isdigit())
print(y.isalnum()) #Python has both 1 and alphabet either having one will work
print(y.isidentifier())
print(y.isprintable()) 
print(y.isspace())













