import glob
import argparse
parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument(
    "--drive",
    required=True,
    help="Drive(example: E:)",
)



args = parser.parse_args()
import psutil
import time
import datetime
while True:
    dsk = psutil.disk_usage(args.drive)
    print("{}".format(datetime.datetime.now()),str(dsk.percent)+"%","Used:","{}GB".format(round(dsk.used/1024/1024/1024)),"Free:","{}GB".format(round(dsk.free/1024/1024/1024)),"Total:","{}GB".format(round(dsk.total/1024/1024/1024)))
    time.sleep(10)
