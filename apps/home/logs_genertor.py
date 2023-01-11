import pyshark
def generate_details_logs():
    with open("log.txt","a") as f:
        capture = pyshark.LiveCapture(interface='Wi-Fi')
        for packet in capture.sniff_continuously(packet_count=5):
            f.write(packet)
            
capture = pyshark.LiveCapture(interface='wlan0')
for packet in capture.sniff_continuously(packet_count=5):
    print(packet)
def filter_logs():
    with open("log.txt", "r") as f:
        json = {"packet": []}
        packet = None
        k = -1
        layer = None
        for i in f:

            if i.startswith("Packet"):
                k += 1
                packet = i + str(k)
                layer = None

                json["packet"].append({"id": k})
            elif i.startswith("Layer"):
                layer = i[:-2]
                json["packet"][k].update({layer: ""})


            else:
                if layer is None:
                    continue
                else:
                    json["packet"][k][layer] += i.lstrip() + "\n"
    return  json

