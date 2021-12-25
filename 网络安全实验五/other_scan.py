from scapy.all import *
from scapy.layers.inet import IP, TCP, ICMP

def synScan(target,ports):
    print("tcp全连接扫描 %s with ports %s" % (target, ports))
    for port in ports:
        send=sr1(IP(dst=target)/TCP(dport=port,flags="S"),timeout=2,verbose=0)
        if (send is None):
            print("%d closed" %port)
        elif send.haslayer("TCP"):
            print(send["TCP"].flags)
            if send["TCP"].flags == "SA":
                send_1 = sr1(IP(dst=target) / TCP(dport=port, flags="R"), timeout=2, verbose=0)#只修改这里
                print("%d opend" %port)
            elif send["TCP"].flags == "RA":
                print("%d closed" %port)
                
def nullScan(target,ports):
    print("tcp NULL 扫描 %s with ports %s" % (target, ports))
    for port in ports:
        null_scan_resp = sr1(IP(dst=target)/TCP(dport=port,flags=""),timeout=5)
        if (str(type(null_scan_resp))=="<class 'NoneType'>"):
            print("%d Open|Filtered" %port)
        elif(null_scan_resp.haslayer(TCP)):
            if(null_scan_resp.getlayer(TCP).flags == "R" or null_scan_resp.getlayer(TCP).flags == "A"):
                print("%d closed" %port)
        elif(null_scan_resp.haslayer(ICMP)):
            if(int(null_scan_resp.getlayer(ICMP).type)==3 and int(null_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                print("%d Filtered" %port)

def xmaxScan(target,ports):
    print("tcp xmax 扫描 %s with ports %s" % (target, ports))
    for port in ports:
        fin_scan_resp = sr1(IP(dst=target)/TCP(dport=port,flags="FPU"),timeout=5)
        if (str(type(fin_scan_resp))=="<class 'NoneType'>"):
            print("%d Open|Filtered" %port)
        elif(fin_scan_resp.haslayer(TCP)):
            if(fin_scan_resp.getlayer(TCP).flags == "R"):
                print("%d Closed" %port)
        elif(fin_scan_resp.haslayer(ICMP)):
            if(int(fin_scan_resp.getlayer(ICMP).type)==3 and int(fin_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                print("%d Filtered" %port)
