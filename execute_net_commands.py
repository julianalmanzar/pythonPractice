import threading
import net_tools

# host = {'hostname': 'msp-sw-dgha-02', 'port': '22', 'username': 'admin', 'password': 'j!*9qxdWUE@#3PnY'}

commands = ["conf t",
            "radius-server key ##=kUP$ILIMm7;Nv-C",
            "radius-server host 172.20.80.110 key ##=kUP$ILIMm7;Nv-C usage login",
            "radius-server host source-interface vlan 90",
            "ip http authentication aaa login-authentication https local radius",
            "aaa authentication login authorization SSH radius",
            "aaa authentication enable authorization SSH radius",
            "aaa accounting login start-stop group radius",
            "line ssh",
            "login authentication SSH",
            "enable authentication SSH",
            "exit",
            "end",
            "wr",
            "Y"]

hosts = ["msp-sw-vent-01",
         "msp-sw-esta-01",
         "msp-sw-dgha-12",
         "msp-sw-nomi-02",
         "msp-sw-nomi-03",
         "msp-sw-despa-01",
         "msp-sw-central-02",
         "msp-sw-digemaps-02",
         "msp-sw-dps-01",
         "msp-sw-gfinanc-01",
         "msp-sw-gfinanc-02",
         "msp-sw-teso-02",
         "msp-sw-dpi-01",
         "msp-sw-digecits-02",
         "msp-sw-despa-02",
         "msp-sw-dgha-14",
         "msp-sw-sisp-01"]

threads = list()
for hostname in hosts:
    host = {'hostname': hostname, 'port': '22', 'username': 'admin', 'password': 'j!*9qxdWUE@#3PnY'}
    th = threading.Thread(target=net_tools.execute_bulk_commands, args=(host, commands))
    threads.append(th)

for thread in threads:
    thread.start()

for thread in threads:
    th.join()
