def repeatedString(s,n):
    c = s.count("a")
    div = n//len(s)
    if n%len(s)==0:
        c = div*c
    else:
        m = n%len(s)
        c= c*div +s[:m].count("a")
    return c
s = input()
n = int(input())
print(repeatedString(s,n))
