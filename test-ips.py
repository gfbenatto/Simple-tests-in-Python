"""
Verify that the IPs are valid or invalid.

"""


def ip_ok(ip):
    ip = ip.split('.')
    print(ip)
    for byte in ip:
        if int(byte) > 255:
            return False
    return True

f = open('ips.txt')
valid = open('valid.txt', 'w')
invalid = open('invalid.txt', 'w')
for linha in f.readlines():
    if ip_ok(linha):
        valid.write(linha)
    else:
        invalid.write(linha)
f.close()
valid.close()
invalid.close()