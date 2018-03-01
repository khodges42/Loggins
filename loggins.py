import random
import string
import os
import csv
import datetime


#this was easier than figuring out random weights
events = ['Connection Opened', 'Connection Closed','Connection Opened', 'Connection Closed','Connection Opened', 'Connection Closed','Connection Opened', 'Connection Closed','Connection Opened', 'Connection Closed','Connection Opened', 'Connection Closed', 'Bad Credentials']


def random_date(start, end):
    return start + datetime.timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

def random_octet(low=1, high=255):
    return str(random.randint(low,high))

def random_ip(local=False):
    if local:
        return ("{}.{}.{}.{}".format("192", "168", random_octet(1,10), random_octet()))
    else:
        return ("{}.{}.{}.{}".format(random_octet(), random_octet(), random_octet(), random_octet()))

def random_port(weird_port):
    normal_ports = ["20", "80", "443", "110", "123"]
    weird_ports = ["22", "23", "389", "31337", "137"]
    if weird_port:
        return (random.choice(weird_ports))
    else:
        return (random.choice(normal_ports))

def generate_log():
    start = datetime.datetime(year=2015, month=5, day=24)
    end = datetime.datetime(year=2018, month=2, day=28)
    inbound = random.choice([True, False])
    weird_port = True if (random.randint(0, 10) == 9) else False
    return [
        str(random_date(start, end)),          #date
        random.choice(events),                 #event
        random_ip(local=(inbound)),            #source
        random_ip(local=(not inbound)),        #dest
        "inbound" if inbound else "outbound",  #inbound
        random_port(weird_port=weird_port),     #port
        str(weird_port or (random.randint(0,100)>95)) #Is sketchy traffic
    ]

logs = {}
with open('logs.csv', "w") as f:
    writer = csv.writer(f)
    writer.writerow(["date","event","source","dest","inbound","port","sketchy"])
    for i in range(10):
        log_list = generate_log()
        writer.writerow(log_list)

