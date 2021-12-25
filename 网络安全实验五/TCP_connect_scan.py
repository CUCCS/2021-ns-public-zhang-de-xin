from scapy.all import *
from scapy.layers.inet import IP, TCP

def tcpScan(target,ports):
    print("tcp全连接扫描 %s with ports %s" % (target, ports))
    for port in ports:
        send=sr1(IP(dst=target)/TCP(dport=port,flags="S"),timeout=2,verbose=0)
        if (send is None):
            print("%d lose" %port)
        elif send.haslayer("TCP"):
            
            if send["TCP"].flags == "SA":
                send_1 = sr1(IP(dst=target) / TCP(dport=port, flags="AR"), timeout=2, verbose=0)
                print("%d open" %port)
            elif send["TCP"].flags == "RA":
                print("%d close" %port)

def main():
    p=range(1,1024)
    tcpScan('192.168.56.106',p)

if __name__ == '__main__':
    main()