import time

import net_tools

switches_ports = {'172.20.90.83': 'port24', '172.20.90.80': 'port24', '172.20.90.21': 'port6',
                  '172.20.90.48': 'port21', '172.20.90.23': 'port24', '172.20.90.41': 'port25',
                  '172.20.90.36': 'port24', '172.20.90.81': 'port24', '172.20.90.59': 'port24',
                  '172.20.90.26': 'port24', '172.20.90.90': 'port24', '172.20.90.31': 'port24',
                  '172.20.90.13': 'port28', '172.20.90.86': 'port24', '172.20.90.38': 'port24',
                  '172.20.90.70': 'port24', '172.20.90.78': 'port24', '172.20.90.30': 'port24',
                  '172.20.90.91': 'port23', '172.20.90.87': 'port24', '172.20.90.85': 'port12',
                  '172.20.90.22': 'port25', '172.20.90.39': 'port24', '172.20.90.58': 'port24',
                  '172.20.90.100': 'port24', '172.20.90.42': 'port24', '172.20.90.12': 'port24',
                  '172.20.90.15': 'port24', '172.20.90.29': 'port1', '172.20.90.73': 'port20',
                  '172.20.90.82': 'port23', '172.20.90.51': 'port24', '172.20.90.53': 'port24',
                  '172.20.90.24': 'port24', '172.20.90.92': 'port24', '172.20.90.14': 'port24',
                  '172.20.90.89': 'port24', '172.20.90.84': 'port14', '172.20.90.54': 'port24',
                  '172.20.90.49': 'port23', '172.20.90.27': 'port24', '172.20.90.88': 'port24',
                  '172.20.90.40': 'port21', '172.20.90.99': 'port24', '172.20.90.28': 'port24'}

#switches_ports = {'172.20.90.40': 'port21'}

for switch_port in switches_ports:
    try:
        host = {'hostname': switch_port, 'port': '22', 'username': 'admin', 'password': 'j!*9qxdWUE@#3PnY'}
        ssh, cli = net_tools.create_connection(host)
        cli.send('config switch vlan\n')
        time.sleep(2)
        cli.send('edit 1\n')
        time.sleep(2)
        cli.send('set dhcp-snooping enable\n')
        time.sleep(2)
        cli.send('end\n')
        time.sleep(2)
        cli.send('config switch interface\n')
        time.sleep(2)
        cli.send(f'edit {switches_ports[switch_port]}\n')
        time.sleep(2)
        cli.send('set dhcp-snooping trusted\n')
        time.sleep(2)
        cli.send('end\n')
        time.sleep(2)
        print(net_tools.read_output(cli))
        ssh.close()
    except Exception as erroL:
        print("No se pudo configrar el equipo " + switch_port + "debido a que " + str(erroL))
