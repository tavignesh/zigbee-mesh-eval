import serial
from datetime import datetime
from time import perf_counter
import csv
from multiprocessing import Process

global pkts_1, pkts_2, pkts_3, pkts_4, pkts_5, dev1pkt, dev2pkt, dev3pkt, dev4pkt, dev5pkt, dev1pktc, dev2pktc, dev3pktc, dev4pktc, dev5pktc, dev1pktf, dev2pktf, dev3pktf, dev4pktf, dev5pktf, c1, c2, c3, c4, c5, pkts_6, pkts_7, pkts_8, pkts_9, pkts_10, dev6pkt, dev7pkt, dev8pkt, dev9pkt, dev10pkt, dev6pktc, dev7pktc, dev8pktc, dev9pktc, dev10pktc, dev6pktf, dev7pktf, dev8pktf, dev9pktf, dev10pktf, c6, c7, c8, c9, c10

logfilename = "logg3.csv"
pid_file = "pidfile.txt"
analysisfile = "pktloss.csv"
fields = ["devid","pid","time", "diff", "data", "rawdata","validity"] 

dev1pkt = 999999999
dev2pkt = 999999999
dev3pkt = 999999999
dev4pkt = 999999999
dev5pkt = 999999999
dev6pkt = 999999999
dev7pkt = 999999999
dev8pkt = 999999999
dev9pkt = 999999999
dev10pkt = 999999999

dev1pktf = 0
dev2pktf = 0
dev3pktf = 0
dev4pktf = 0
dev5pktf = 0
dev6pktf = 0
dev7pktf = 0
dev8pktf = 0
dev9pktf = 0
dev10pktf = 0

dev1pktc = 0
dev2pktc = 0
dev3pktc = 0
dev4pktc = 0
dev5pktc = 0
dev6pktc = 0
dev7pktc = 0
dev8pktc = 0
dev9pktc = 0
dev10pktc = 0

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0
c10 = 0

with open(pid_file, 'w') as f:
    pass

def start_pkt_id(devid2, pid2):
    global pkts_1, pkts_2, pkts_3, pkts_4, pkts_5, dev1pkt, dev2pkt, dev3pkt, dev4pkt, dev5pkt, dev1pktc, dev2pktc, dev3pktc, dev4pktc, dev5pktc, dev1pktf, dev2pktf, dev3pktf, dev4pktf, dev5pktf, c1, c2, c3, c4, c5, pkts_6, pkts_7, pkts_8, pkts_9, pkts_10, dev6pkt, dev7pkt, dev8pkt, dev9pkt, dev10pkt, dev6pktc, dev7pktc, dev8pktc, dev9pktc, dev10pktc, dev6pktf, dev7pktf, dev8pktf, dev9pktf, dev10pktf, c6, c7, c8, c9, c10
    try:
        pid = int(pid2, 16)
        devid = int(devid2, 16)
    except Exception as e:
        devid = 0
        pid = 99999999999
        #print(e)
 
    try:
        if devid == 1 and c1 == 0:
            if int(pid) < dev1pkt and int(pid) != 0:
                c1 = 1
                dev1pkt = int(pid)
                pnt =  "devid : " + str(devid) + "  pktid : " + str(dev1pkt)
                with open(pid_file, 'a') as f:
                    f.write(pnt + '\n')
        elif devid == 2 and c2 == 0:
            if int(pid) < dev2pkt and int(pid) != 0:
                dev2pkt = int(pid)
                c2 = 1
                pnt =  "devid : " + str(devid) + "  pktid : " + str(dev2pkt)
                with open(pid_file, 'a') as f:
                    f.write(pnt + '\n')
        elif devid == 3 and c3 == 0:
            if int(pid) < dev3pkt and int(pid) != 0:
                dev3pkt = int(pid)
                c3 = 1
                pnt =  "devid : " + str(devid) + "  pktid : " + str(dev3pkt)
                with open(pid_file, 'a') as f:
                    f.write(pnt + '\n')
        elif devid == 4 and c4 == 0:
            if int(pid) < dev4pkt and int(pid) != 0:
                dev4pkt = int(pid)
                c4 = 1
                pnt =  "devid : " + str(devid) + "  pktid : " + str(dev4pkt)
                with open(pid_file, 'a') as f:
                    f.write(pnt + '\n')
        elif devid == 5 and c5 == 0:
            if int(pid) < dev5pkt and int(pid) != 0:
                dev5pkt = int(pid)
                c5 = 1
                pnt =  "devid : " + str(devid) + "  pktid : " + str(dev5pkt)
                with open(pid_file, 'a') as f:
                    f.write(pnt + '\n')
        elif devid == 6 and c6 == 0:
            if int(pid) < dev6pkt and int(pid) != 0:
                dev6pkt = int(pid)
                c6 = 1
                pnt =  "devid : " + str(devid) + "  pktid : " + str(dev5pkt)
                with open(pid_file, 'a') as f:
                    f.write(pnt + '\n')
        elif devid == 7 and c7 == 0:
            if int(pid) < dev7pkt and int(pid) != 0:
                dev7pkt = int(pid)
                c7 = 1
                pnt =  "devid : " + str(devid) + "  pktid : " + str(dev5pkt)
                with open(pid_file, 'a') as f:
                    f.write(pnt + '\n')
        elif devid == 8 and c8 == 0:
            if int(pid) < dev8pkt and int(pid) != 0:
                dev8pkt = int(pid)
                c8 = 1
                pnt =  "devid : " + str(devid) + "  pktid : " + str(dev5pkt)
                with open(pid_file, 'a') as f:
                    f.write(pnt + '\n')
        elif devid == 9 and c9 == 0:
            if int(pid) < dev9pkt and int(pid) != 0:
                dev9pkt = int(pid)
                c9 = 1
                pnt =  "devid : " + str(devid) + "  pktid : " + str(dev5pkt)
                with open(pid_file, 'a') as f:
                    f.write(pnt + '\n')
        elif devid == 10 and c10 == 0:
            if int(pid) < dev10pkt and int(pid) != 0:
                dev10pkt = int(pid)
                c10 = 1
                pnt =  "devid : " + str(devid) + "  pktid : " + str(dev5pkt)
                with open(pid_file, 'a') as f:
                    f.write(pnt + '\n')
        

        if devid == 1:
            if int(pid) > dev1pktf and int(pid) != 0:
                dev1pktf = int(pid)
                dev1pktc += 1
        elif devid == 2:
            if int(pid) > dev2pktf and int(pid) != 0:
                dev2pktf = int(pid)
                dev2pktc += 1
        elif devid == 3:
            if int(pid) > dev3pktf and int(pid) != 0:
                dev3pktf = int(pid)
                dev3pktc += 1
        elif devid == 4:
            if int(pid) > dev4pktf and int(pid) != 0:
                dev4pktf = int(pid)
                dev4pktc += 1
        elif devid == 5:
            if int(pid) > dev5pktf and int(pid) != 0:
                dev5pktf = int(pid)
                dev5pktc += 1
        elif devid == 6:
            if int(pid) > dev6pktf and int(pid) != 0:
                dev6pktf = int(pid)
                dev6pktc += 1
        elif devid == 7:
            if int(pid) > dev7pktf and int(pid) != 0:
                dev7pktf = int(pid)
                dev7pktc += 1
        elif devid == 8:
            if int(pid) > dev8pktf and int(pid) != 0:
                dev8pktf = int(pid)
                dev8pktc += 1
        elif devid == 9:
            if int(pid) > dev9pktf and int(pid) != 0:
                dev9pktf = int(pid)
                dev9pktc += 1
        elif devid == 10:
            if int(pid) > dev10pktf and int(pid) != 0:
                dev10pktf = int(pid)
                dev10pktc += 1

        pkts_1 = dev1pktf - dev1pkt + 1
        pkts_2 = dev2pktf - dev2pkt + 1
        pkts_3 = dev3pktf - dev3pkt + 1
        pkts_4 = dev4pktf - dev4pkt + 1
        pkts_5 = dev5pktf - dev5pkt + 1
        pkts_6 = dev6pktf - dev6pkt + 1
        pkts_7 = dev7pktf - dev7pkt + 1
        pkts_8 = dev8pktf - dev8pkt + 1
        pkts_9 = dev9pktf - dev9pkt + 1
        pkts_10 = dev10pktf - dev10pkt + 1
        

    except Exception as e:
        #print("PKT ID ERROR : ", e)
        pass

ser = serial.Serial(
   port = 'COM9',
   baudrate = 9600,
   parity = serial.PARITY_NONE,
   stopbits = serial.STOPBITS_ONE,
   bytesize = serial.EIGHTBITS
)

if ser.is_open:
    print("Port opened: ", ser.port)
else:
    print("ERROR: Port not opened")

inphex = ""
#t_st = perf_counter()
t_st = 0
with open(logfilename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
if ser.read().hex() == "7e":
        inphex == "7e"
while 1:
    try:
        if len(inphex) < 62:
            inp = ser.read()
            inphex += inp.hex()
        elif len(inphex) > 62:
            inphex = ""
        elif len(inphex) == 62:
            #t_end = perf_counter()
            t_end = 0
            t_now = str(datetime.now().hour) +":"+ str(datetime.now().minute) +":"+ str(datetime.now().second) +":"+ (str(datetime.now().microsecond)[:2])
            t_diff = t_end - t_st
            t_diff = str(t_diff) + "s"
            #t_st = perf_counter()   
            t_st = 0
            print(t_now, t_diff[:5], inphex)
            vdty = "invalid"
            data = ""
            devid = ""
            pid = "00"
            tmp2 = inphex
            if inphex.startswith("7e") and inphex[32:34] == "ff" and inphex[58:-2] == "fe":
                data = inphex[44:-4]
                devid = inphex[34:36]
                pid = inphex[36:42]
                vdty = "valid"
                inphex = ""
            else:
                vdty = "invalid"
                tmp1 = "ff"
                while tmp1 != "7e":
                    tmp1 = ser.read().hex()
                inphex = "7e"

            start_pkt_id(devid, pid)
            dic = [{"time":t_now, "diff":t_diff, "rawdata":tmp2, "data":data, "devid":devid,"validity":vdty, "pid":int(pid,16)},]
            with open(logfilename, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writerows(dic)
    except:
        with open(analysisfile, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["Device ID", "Total Pkts", "Pkts Recived", "Loss %"])
            writer.writeheader()
            dict = [{"Device ID": "1", "Total Pkts": pkts_1, "Pkts Recived": dev1pktc, "Loss %": (dev1pktc/pkts_1)},
                    {"Device ID": "2", "Total Pkts": pkts_2, "Pkts Recived": dev2pktc, "Loss %": (dev2pktc/pkts_2)},
                    {"Device ID": "3", "Total Pkts": pkts_3, "Pkts Recived": dev3pktc, "Loss %": (dev3pktc/pkts_3)},
                    {"Device ID": "4", "Total Pkts": pkts_4, "Pkts Recived": dev4pktc, "Loss %": (dev4pktc/pkts_4)},
                    {"Device ID": "5", "Total Pkts": pkts_5, "Pkts Recived": dev5pktc, "Loss %": (dev5pktc/pkts_5)},
                    {"Device ID": "6", "Total Pkts": pkts_6, "Pkts Recived": dev6pktc, "Loss %": (dev6pktc/pkts_6)},
                    {"Device ID": "7", "Total Pkts": pkts_7, "Pkts Recived": dev7pktc, "Loss %": (dev7pktc/pkts_7)},
                    {"Device ID": "8", "Total Pkts": pkts_8, "Pkts Recived": dev8pktc, "Loss %": (dev8pktc/pkts_8)},
                    {"Device ID": "9", "Total Pkts": pkts_9, "Pkts Recived": dev9pktc, "Loss %": (dev9pktc/pkts_9)},
                    {"Device ID": "10", "Total Pkts": pkts_10, "Pkts Recived": dev10pktc, "Loss %": (dev10pktc/pkts_10)}]
            writer.writerows(dict)
            break
