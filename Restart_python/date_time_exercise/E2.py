from datetime import datetime
date_string = "Feb 25 2020 4:20PM"
curr_time=datetime.strptime(date_string,"%b %d %Y %I:%M%p")
print(curr_time)
