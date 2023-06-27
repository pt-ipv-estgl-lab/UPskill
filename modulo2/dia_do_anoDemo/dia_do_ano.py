def is_year_leap(year):
# verify if an year is leap or commun
# return: True if is a leap year, False if is a commun year, and None if year < 1582
# params: year the year (number) to check
    if year < 1582: 
        return None
    if year % 4 != 0: 
        return False
    if year % 100 != 0: 
        return True
    if year % 400 != 0:
        return False
    return True


def days_in_month(year, month):
#
# Your code from LAB 4.3.1.7.
#
    pass

def day_of_year(year, month, day):
#
# Write your new code here.
#
    return 366

# test_data = [1900, 2000, 2016, 1987, 1400]
# test_results = [False, True, True, False, None]
# for i in range(len(test_data)):
# 	yr = test_data[i]
# 	print(yr,"-> ",end="")
# 	result = is_year_leap(yr)
# 	if result == test_results[i]:
# 		print("OK")
# 	else:
# 		print("Failed")

#print(day_of_year(2000, 12, 31))
