#text = input('text: ')
#text = text.split('.')
#print(text)

def ip_ok(ip):
    ip = ip.split('.')
    print(ip)
    for byte in ip:
        if int(byte) > 255:
            return False
        return True

t = ip_ok(200.3.5.7)
print(t)