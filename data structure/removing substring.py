s = "ABFCACDB"
while "AB" in s or "CD" in s:
    s=s.replace("AB","")
    s=s.replace("CD","")
print(s)

