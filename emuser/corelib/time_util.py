from datetime import datetime
from dateutil.relativedelta import relativedelta
def convert_datetime_str(ago):
    num_month = int(ago.split(" month")[0])
    date = (datetime.today() - relativedelta(num_month))
    return (date.year, date.month)
       
