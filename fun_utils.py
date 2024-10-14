import os


def check_date(command):    # defining a function
    print(os.system(command))

check_date('date')   # calling a funct

import datetime
print(datetime.datetime.today())