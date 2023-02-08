def ips_between(start, end):
    s = start.split('.')
    e = end.split('.')
    ips = 0

    if s[3] != e[3]:
        ips += (int(e[3]) - int(s[3]))
    if s[2] != e[2]:
        ips += (int(e[2]) - int(s[2])) * 256
    if s[1] != e[1]:
        ips += (int(e[1]) - int(s[1])) * 65536
    if s[0] != e[0]:
        ips += (int(e[0]) - int(s[0])) * 16777216    

    return ips


print(ips_between("10.0.0.0", "10.0.1.10"))
print(ips_between("20.0.0.10", "20.0.1.0"))