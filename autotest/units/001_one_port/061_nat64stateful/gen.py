#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scapy.all import *


def write_pcap(filename, *packetsList):
	if len(packetsList) == 0:
		PcapWriter(filename)._write_header(Ether())
		return

	PcapWriter(filename)

	for packets in packetsList:
		if type(packets) == list:
			for packet in packets:
				packet.time = 0
				wrpcap(filename, [p for p in packet], append=True)
		else:
			packets.time = 0
			wrpcap(filename, [p for p in packets], append=True)


# check lan (ipv6 -> ipv4). create state, use state
write_pcap("001-send.pcap",
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/TCP(dport=80, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/TCP(dport=443, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.103", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/TCP(dport=80, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.103", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/TCP(dport=443, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/TCP(dport=80, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/TCP(dport=443, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.103", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/TCP(dport=80, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.103", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/TCP(dport=443, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.104", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/TCP(dport=8000, sport=8000))

write_pcap("001-expect.pcap",
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0)/TCP(dport=80, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0)/TCP(dport=443, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.103", src="153.153.153.153", ttl=63, id=0)/TCP(dport=80, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.103", src="153.153.153.153", ttl=63, id=0)/TCP(dport=443, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0)/TCP(dport=80, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0)/TCP(dport=443, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.103", src="153.153.153.153", ttl=63, id=0)/TCP(dport=80, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.103", src="153.153.153.153", ttl=63, id=0)/TCP(dport=443, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.104", src="153.153.153.153", ttl=63, id=0)/TCP(dport=8000, sport=8000))


# check wan (ipv4 -> ipv6). use state or drop
write_pcap("002-send.pcap",
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/TCP(dport=2048, sport=443),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/TCP(dport=2048, sport=80, flags="SA"),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/TCP(dport=2048, sport=443, flags="F"),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/TCP(dport=2048, sport=443),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/TCP(dport=2048, sport=80, flags="AF"),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/TCP(dport=2048, sport=443, flags="SA"),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/TCP(dport=2948, sport=80), # dropped
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/TCP(dport=2948, sport=443), # dropped
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/TCP(dport=2048, sport=81), # dropped
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/TCP(dport=2048, sport=444), # dropped
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.199", src="102.102.102.102", ttl=64)/TCP(dport=2048, sport=80), # dropped
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.199", src="102.102.102.102", ttl=64)/TCP(dport=2048, sport=443), # dropped
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.199", ttl=64)/TCP(dport=2048, sport=80), # dropped
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.199", ttl=64)/TCP(dport=2048, sport=443)) # dropped

write_pcap("002-expect.pcap",
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.102", hlim=63, fl=0)/TCP(dport=2048, sport=80),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.102", hlim=63, fl=0)/TCP(dport=2048, sport=443),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.103", hlim=63, fl=0)/TCP(dport=2048, sport=80, flags="SA"),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.103", hlim=63, fl=0)/TCP(dport=2048, sport=443, flags="F"),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.102", hlim=63, fl=0)/TCP(dport=2048, sport=80),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.102", hlim=63, fl=0)/TCP(dport=2048, sport=443),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.103", hlim=63, fl=0)/TCP(dport=2048, sport=80, flags="AF"),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.103", hlim=63, fl=0)/TCP(dport=2048, sport=443, flags="SA"))


# check tc
write_pcap("003-send.pcap",
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64, tc=0x01)/TCP(dport=80, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64, tc=0x02)/TCP(dport=80, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64, tc=0x04)/TCP(dport=80, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64, tc=0x80)/TCP(dport=80, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64, tc=0xFF)/TCP(dport=80, sport=2048))

write_pcap("003-expect.pcap",
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0, tos=0x01)/TCP(dport=80, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0, tos=0x02)/TCP(dport=80, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0, tos=0x04)/TCP(dport=80, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0, tos=0x80)/TCP(dport=80, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0, tos=0xFF)/TCP(dport=80, sport=2048))


# check tos
write_pcap("004-send.pcap",
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, tos=0x01)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, tos=0x02)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, tos=0x04)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, tos=0x80)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, tos=0xFF)/TCP(dport=2048, sport=80))

write_pcap("004-expect.pcap",
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.102", hlim=63, fl=0, tc=0x01)/TCP(dport=2048, sport=80),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.102", hlim=63, fl=0, tc=0x02)/TCP(dport=2048, sport=80),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.102", hlim=63, fl=0, tc=0x04)/TCP(dport=2048, sport=80),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.102", hlim=63, fl=0, tc=0x80)/TCP(dport=2048, sport=80),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.102", hlim=63, fl=0, tc=0xFF)/TCP(dport=2048, sport=80))


# fragment not allowed yet. pass "atomic" fragment
write_pcap("005-send.pcap",
           fragment6(Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/IPv6ExtHdrFragment(id=0x12345678)/TCP(dport=80, sport=2048)/("ABCDEFGH123456789012"*128), fragSize=1280),
           fragment6(Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/IPv6ExtHdrFragment(id=0x12345678)/UDP(dport=80, sport=2048)/("ABCDEFGH123456789012"*128), fragSize=1280),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/IPv6ExtHdrFragment(id=0x87654321, m=0, offset=0)/TCP(dport=80, sport=2048),
           fragment6(Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/IPv6ExtHdrFragment(id=0xABCDEF12)/ICMPv6EchoRequest(id=0x1234, seq=0x8765)/("ABCDEFGH123456789012"*128), fragSize=1280))

write_pcap("005-expect.pcap",
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0)/TCP(dport=80, sport=2048))


# fragment not allowed yet
write_pcap("006-send.pcap",
           fragment(Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, id=0x1234)/TCP(dport=2048, sport=80)/("ABCDEFGH123456789012"*128), fragsize=1208),
           fragment(Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, id=0x1234)/UDP(dport=2048, sport=80)/("ABCDEFGH123456789012"*128), fragsize=1208),
           fragment(Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, id=0x1234)/ICMP(type=8, id=0x1234, seq=0x8765)/("ABCDEFGH123456789012"*128), fragsize=1208))

write_pcap("006-expect.pcap")


# icmpv6 -> icmpv4. ping only yet
write_pcap("007-send.pcap",
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/ICMPv6EchoRequest(id=0x1234, seq=0x8765)/"du hast vyacheslavich",
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/ICMPv6EchoReply(id=0x5678, seq=0x4321)/"vitalya 2")

write_pcap("007-expect.pcap",
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0)/ICMP(type=8, id=0x1234, seq=0x8765)/"du hast vyacheslavich")


# icmpv4 -> icmpv6. pong only yet
write_pcap("008-send.pcap",
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/ICMP(type=0, id=0x1234, seq=0x8765)/"du hast vyacheslavich",
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/ICMP(type=0, id=0x8765, seq=0x8765)/"du hast vyacheslavich",
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.199", ttl=64)/ICMP(type=0, id=0x1234, seq=0x8765)/"du hast vyacheslavich",
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.199", src="102.102.102.102", ttl=64)/ICMP(type=0, id=0x1234, seq=0x8765)/"du hast vyacheslavich",
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/ICMP(type=8, id=0x5678, seq=0x4321)/"vitalya 2")

write_pcap("008-expect.pcap",
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.102", hlim=63, fl=0)/ICMPv6EchoReply(id=0x1234, seq=0x8765)/"du hast vyacheslavich")


# unsupported proto and broken packets
write_pcap("009-send.pcap",
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64, nh=0x1B),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64, nh=0x1B, plen=1),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64, nh=0x1B, plen=123),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/IPv6ExtHdrDestOpt(nh=0x1B),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64, plen=0)/IPv6ExtHdrDestOpt(nh=0x1B),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64, plen=1)/IPv6ExtHdrDestOpt(nh=0x1B),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64, plen=7)/IPv6ExtHdrDestOpt(nh=0x1B),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64, plen=9)/IPv6ExtHdrDestOpt(nh=0x1B),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64, plen=300)/IPv6ExtHdrDestOpt(nh=0x1B))

write_pcap("009-expect.pcap")


# broken packets
write_pcap("010-send.pcap",
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, len=0)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, len=1)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, len=19)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, len=21)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, len=300)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*20))/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*20), len=0)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*20), len=1)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*20), len=19)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*20), len=20)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*20), len=21)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*20), len=39)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*20), len=41)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*20), len=300)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*40))/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*40), len=0)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*40), len=1)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*40), len=19)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*40), len=20)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*40), len=21)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*40), len=39)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*40), len=40)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*40), len=41)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*40), len=59)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*40), len=61)/TCP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64, options=("\x02"*40), len=300)/TCP(dport=2048, sport=80))

write_pcap("010-expect.pcap",
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.102", hlim=63, fl=0)/TCP(dport=2048, sport=80),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.102", hlim=63, fl=0)/TCP(dport=2048, sport=80),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.102", hlim=63, fl=0)/TCP(dport=2048, sport=80))


# UDP. check wan (ipv4 -> ipv6). no state. drop
write_pcap("011-send.pcap",
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/UDP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/UDP(dport=2048, sport=443),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/UDP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/UDP(dport=2048, sport=443),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/UDP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/UDP(dport=2048, sport=443),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/UDP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/UDP(dport=2048, sport=443),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/UDP(dport=2948, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/UDP(dport=2948, sport=443),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/UDP(dport=2048, sport=81),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/UDP(dport=2048, sport=444),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.199", src="102.102.102.102", ttl=64)/UDP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.199", src="102.102.102.102", ttl=64)/UDP(dport=2048, sport=443),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.199", ttl=64)/UDP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.199", ttl=64)/UDP(dport=2048, sport=443))

write_pcap("011-expect.pcap")


# UDP. check lan (ipv6 -> ipv4). create state, use state
write_pcap("012-send.pcap",
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/UDP(dport=80, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/UDP(dport=443, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.103", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/UDP(dport=80, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.103", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/UDP(dport=443, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/UDP(dport=80, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/UDP(dport=443, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.103", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/UDP(dport=80, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.103", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", hlim=64)/UDP(dport=443, sport=2048))

write_pcap("012-expect.pcap",
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0)/UDP(dport=80, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0)/UDP(dport=443, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.103", src="153.153.153.153", ttl=63, id=0)/UDP(dport=80, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.103", src="153.153.153.153", ttl=63, id=0)/UDP(dport=443, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0)/UDP(dport=80, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0)/UDP(dport=443, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.103", src="153.153.153.153", ttl=63, id=0)/UDP(dport=80, sport=2048),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.103", src="153.153.153.153", ttl=63, id=0)/UDP(dport=443, sport=2048))


# UDP. check wan (ipv4 -> ipv6). use state or drop
write_pcap("013-send.pcap",
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/UDP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/UDP(dport=2048, sport=443),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/UDP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/UDP(dport=2048, sport=443),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/UDP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/UDP(dport=2048, sport=443),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/UDP(dport=2048, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/UDP(dport=2048, sport=443),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/UDP(dport=2948, sport=80), # dropped
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/UDP(dport=2948, sport=443), # dropped
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/UDP(dport=2048, sport=81), # dropped
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/UDP(dport=2048, sport=444), # dropped
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.199", src="102.102.102.102", ttl=64)/UDP(dport=2048, sport=80), # dropped
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.199", src="102.102.102.102", ttl=64)/UDP(dport=2048, sport=443), # dropped
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.199", ttl=64)/UDP(dport=2048, sport=80), # dropped
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.199", ttl=64)/UDP(dport=2048, sport=443)) # dropped

write_pcap("013-expect.pcap",
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.102", hlim=63, fl=0)/UDP(dport=2048, sport=80),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.102", hlim=63, fl=0)/UDP(dport=2048, sport=443),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.103", hlim=63, fl=0)/UDP(dport=2048, sport=80),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.103", hlim=63, fl=0)/UDP(dport=2048, sport=443),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.102", hlim=63, fl=0)/UDP(dport=2048, sport=80),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.102", hlim=63, fl=0)/UDP(dport=2048, sport=443),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.103", hlim=63, fl=0)/UDP(dport=2048, sport=80),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa", src="64:ff9b::102.102.102.103", hlim=63, fl=0)/UDP(dport=2048, sport=443))


# check collisions (tries)
write_pcap("014-send.pcap",
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", hlim=64)/TCP(dport=80, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", hlim=64)/TCP(dport=443, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.103", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", hlim=64)/TCP(dport=80, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.103", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", hlim=64)/TCP(dport=443, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", hlim=64)/TCP(dport=80, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", hlim=64)/TCP(dport=443, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.103", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", hlim=64)/TCP(dport=80, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.103", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", hlim=64)/TCP(dport=443, sport=2048),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.104", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", hlim=64)/TCP(dport=8000, sport=8000),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:01")/Dot1Q(vlan=100)/IPv6(dst="64:ff9b::102.102.102.102", src="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", hlim=64)/ICMPv6EchoRequest(id=0x1234, seq=0x8888)/"du hast vyacheslavich")

write_pcap("014-expect.pcap",
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0)/TCP(dport=80, sport=6070),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0)/TCP(dport=443, sport=6070),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.103", src="153.153.153.153", ttl=63, id=0)/TCP(dport=80, sport=6070),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.103", src="153.153.153.153", ttl=63, id=0)/TCP(dport=443, sport=6070),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0)/TCP(dport=80, sport=6070),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0)/TCP(dport=443, sport=6070),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.103", src="153.153.153.153", ttl=63, id=0)/TCP(dport=80, sport=6070),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.103", src="153.153.153.153", ttl=63, id=0)/TCP(dport=443, sport=6070),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.104", src="153.153.153.153", ttl=63, id=0)/TCP(dport=8000, sport=12022),
           Ether(dst="00:00:00:22:22:22", src="00:11:22:33:44:55")/Dot1Q(vlan=200)/IP(dst="102.102.102.102", src="153.153.153.153", ttl=63, id=0)/ICMP(type=8, id=0x21ea, seq=0x8888)/"du hast vyacheslavich")


# check collisions (ipv4 -> ipv6)
write_pcap("015-send.pcap",
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/TCP(dport=6070, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/TCP(dport=6070, sport=443),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/TCP(dport=6070, sport=80, flags="SA"),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/TCP(dport=6070, sport=443, flags="F"),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/TCP(dport=6070, sport=80),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/TCP(dport=6070, sport=443),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/TCP(dport=6070, sport=80, flags="AF"),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.103", ttl=64)/TCP(dport=6070, sport=443, flags="SA"),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.104", ttl=64)/TCP(dport=12022, sport=8000),
           Ether(dst="00:11:22:33:44:55", src="00:00:00:00:00:02")/Dot1Q(vlan=200)/IP(dst="153.153.153.153", src="102.102.102.102", ttl=64)/ICMP(type=0, id=0x21ea, seq=0x8888)/"du hast vyacheslavich")

write_pcap("015-expect.pcap",
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", src="64:ff9b::102.102.102.102", hlim=63, fl=0)/TCP(dport=2048, sport=80),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", src="64:ff9b::102.102.102.102", hlim=63, fl=0)/TCP(dport=2048, sport=443),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", src="64:ff9b::102.102.102.103", hlim=63, fl=0)/TCP(dport=2048, sport=80, flags="SA"),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", src="64:ff9b::102.102.102.103", hlim=63, fl=0)/TCP(dport=2048, sport=443, flags="F"),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", src="64:ff9b::102.102.102.102", hlim=63, fl=0)/TCP(dport=2048, sport=80),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", src="64:ff9b::102.102.102.102", hlim=63, fl=0)/TCP(dport=2048, sport=443),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", src="64:ff9b::102.102.102.103", hlim=63, fl=0)/TCP(dport=2048, sport=80, flags="AF"),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", src="64:ff9b::102.102.102.103", hlim=63, fl=0)/TCP(dport=2048, sport=443, flags="SA"),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", src="64:ff9b::102.102.102.104", hlim=63, fl=0)/TCP(dport=8000, sport=8000),
           Ether(dst="00:00:00:11:11:11", src="00:11:22:33:44:55")/Dot1Q(vlan=100)/IPv6(dst="aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:aaaa:bbbb", src="64:ff9b::102.102.102.102", hlim=63, fl=0)/ICMPv6EchoReply(id=0x1234, seq=0x8888)/"du hast vyacheslavich")
