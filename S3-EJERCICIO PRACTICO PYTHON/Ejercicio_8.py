ips_log = ["10.0.0.5", "200.0.0.1", "10.0.0.8", "45.33.32.156", "10.0.0.10"]
blacklist = ["200.0.0.1", "45.33.32.156"]
total_procesadas = 0

for ip in ips_log:
    if ip in blacklist:
        continue
    print(f'Procesando: {ip}')
    total_procesadas += 1
print(f'Total procesadas: {total_procesadas}')
