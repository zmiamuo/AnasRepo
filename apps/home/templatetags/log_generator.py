import csv
import random
import time
import pyshark
from datetime import  datetime
from django import template
register=template.Library()
import random

# define interface
def generate_logs():
    filed_name = ["time", "ip_source", "ip_dest", "protocol"]

    with open('data.csv', 'w',newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=filed_name)
        csv_writer.writeheader()
    networkInterface = "Wi-Fi"

# define capture object
    capture = pyshark.LiveCapture(interface=networkInterface)

    print("listening on %s" % networkInterface)

    for packet in capture.sniff_continuously(packet_count=400):
    # adjusted output
        try:
        # get timestamp
            now =datetime.now().strftime("%H:%M:%S")
        # get packet content
            protocol = packet.transport_layer  # protocol type
            src_addr = packet.ip.src  # source address
            src_port = packet[protocol].srcport  # source port
            dst_addr = packet.ip.dst  # destination address
            dst_port = packet[protocol].dstport  # destination port
            with open('data.csv', 'a',newline='') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=filed_name)

                info = {
                    "time": now,
                    "ip_source": src_addr + ":" + src_port,
                     "ip_dest": dst_addr + ":" + dst_port,
                    "protocol": protocol

                        }
                print(protocol)
                csv_writer.writerow(info)

            # output packet info
            print("%s IP %s:%s <-> %s:%s (%s)" % (now, src_addr, src_port, dst_addr, dst_port, protocol))
        except AttributeError as e:
        # ignore packets other than TCP, UDP and IPv4
            pass