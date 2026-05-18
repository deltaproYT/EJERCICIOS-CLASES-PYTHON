ips = ['192.168.1.1',
       '10.0.0.255',
       '256.1.1.1',
       '192.168.1',
       '192.168.a.1']
for ip in ips:
    octals = ip.split('.')
    if len(octals) != 4:
        print(f'La IP: {ip} no es una IP Valida ')
        continue
    for octal in octals:
        if not octal.isdigit():
            print(f'La IP: {ip} no es una IP Valida ')
            break

        if int(octal) < 0 or int(octal) > 255:
            print(f'La IP: {ip} no es una IP Valida ')
            break
    else:
        print(f'La IP: {ip} es una IP valida ')