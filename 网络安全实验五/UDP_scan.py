from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP, ICMP

def udpScan(target,ports):
    print("UDP 扫描 %s with ports %s" % (target, ports))
    for port in ports:
        udp_scan_resp = sr1(IP(dst=target)/UDP(dport=port),timeout=5)
        if (str(type(udp_scan_resp))=="<class 'NoneType'>"):
            print("%d Open|Filtered" %port)
        elif udp_scan_resp.haslayer(UDP):
            if(udp_scan_resp[TCP].flags == "R"):
                print("%d Open" %port)
        elif udp_scan_resp.haslayer(ICMP):
            if(int(udp_scan_resp[ICMP].type)==3 and int(udp_scan_resp[ICMP].code) in [1,2,9,10,13]):
                print("%d Filtered" %port)
            if(int(udp_scan_resp[ICMP].type)==3 and int(udp_scan_resp[ICMP].code)==3):
                print("%d Closed" %port)                

def main():
    p=range(1,1024)
    udpScan('192.168.56.106',p)

if __name__ == '__main__':
    main()
