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
    print("{} : {}%".format(datetime.datetime.now(),dsk.percent))
    time.sleep(1)
