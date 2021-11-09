# '''
# return_day(1) # "Sunday"
# return_day(2) # "Monday"
# return_day(3) # "Tuesday"
# return_day(4) # "Wednesday"
# return_day(5) # "Thursday"
# return_day(6) # "Friday"
# return_day(7) # "Saturday"
# return_day(41) # None
# '''
# def return_day():
#     pass
#
def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None

print(return_day(1))
