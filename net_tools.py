import paramiko
import time
import re
import threading


def create_connection(host):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(**host, look_for_keys=False, allow_agent=False)
    cli = ssh.invoke_shell()
    return ssh, cli


def read_output(cli):
    message = cli.recv(1000000000000000000000000).decode('utf-8')
    return message


def cisco_get_port_mac(host, mac):
    ssh, cli = create_connection(host)
    cli.send(f'show mac address-table address {mac}\n')
    time.sleep(1)
    message = read_output(cli)
    port = re.findall("gi[0123456789].{1,5}|fa[0123456789].{1,5}", message, flags=re.IGNORECASE)
    ssh.close()
    return port[0].strip()


def fortinet_get_port_mac(host, mac):
    try:
        ssh, cli = create_connection(host)
        cli.send(f'diagnose switch mac-address list | grep {mac}\n')
        time.sleep(10)
        message = read_output(cli)
        port = re.findall("port[0-9]{1,2}", message, flags=re.IGNORECASE)
        ssh.close()
        print(host['hostname'] + "    " + str(port[0].strip())+"\n")
    except IndexError:
        print(host['hostname'] + " not available\n")
    return


def execute_command(host, command):
    ssh, cli = create_connection(host)
    cli.send(command)
    time.sleep(10)
    message = read_output(cli)
    ssh.close()
    return message


def execute_bulk_commands(host, commands):
    ssh, cli = create_connection(host)
    for command in commands:
        print(host['hostname'] + "------>" + command + "\n")
        cli.send(command+"\n")
        time.sleep(2)
    ssh.close()
