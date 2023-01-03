import colander
from datetime import datetime
import pandas as pd

def parse_date_to_datetime(date):
    print(date)
    """01/10/2022 -> 2022/10/01 00:00:00.00"""
    if date is None:
        return colander.null

    if isinstance(date, pd._libs.tslibs.timestamps.Timestamp):
        date_time_formatted = date.strftime("%Y/%m/%d 00:00:00.00")
        return date_time_formatted
    date_parse = datetime.strptime(date, "%Y-%m-%d")
    date_time_formatted = date_parse.strftime("%Y/%m/%d 00:00:00.00")
    print(date_time_formatted)
    return date_time_formatted



#parse_date_to_datetime('2022-11-26')



from dateutil import parser
#s= '25 April, 2020, 2:50, pm, IST'
s = '2022-11-26'
dat = parser.parse(s)
#datetime.datetime(2020, 4, 25, 14, 50)

print(dat)