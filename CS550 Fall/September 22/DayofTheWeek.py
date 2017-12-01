import sys
cDofWeek = ["Sunday" , "Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday"]
y = int(sys.argv[1])
m = int(sys.argv[2])
d = int(sys.argv[3])


y0 = y - (14 - m) // 12
x = y0 + y0//4 - y0//100 + y0//400
m0 = m + 12 * ((14 - m) // 12) - 2
dow = ((d + x + (31*m0)// 12)) % 7

print(cDofWeek[dow])


# import sys
# import math

# cYear = int(sys.argv[1])
# cMonth = int(sys.argv[2])
# cDay = int(sys.argv[3])
# isLeapYear = (int(sys.argv[1]) % 4 == 0) and (int(sys.argv[1]) % 100 != 0) or (int(sys.argv[1]) % 16 == 0)
# cDofWeek = ["Sunday" , "Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday"]
# moreDays = 0
# for x in range(0, cYear):
# 	curYear = x
# 	moreDays = moreDays + 1
# 	print(moreDays)
# 	if 0 == curYear % 4:
# 		moreDays = moreDays + 1
# 	print(moreDays)
# 	if 0 == curYear % 100:
# 		moreDays = moreDays - 1
# 	print(moreDays)
# 	if 0 == curYear % 400:
# 		moreDays = moreDays + 1
# 	print(moreDays)

# fDayofYear = (moreDays + 6) % 7


#  if isLeapYear == True:
# 	if cMonth == 10:
# 		fDayofMonth = 0
# 	elif cMonth == 5:
# 		fDayofMonth = 1
# 	elif cMonth == 2 or cMonth == 8:
# 		fDayofMonth = 2
# 	elif cMonth == 3 or cMonth == 11:
# 		fDayofMonth = 3
# 	elif cMonth == 6:
# 		fDayofMonth = 4
# 	elif cMonth == 9 or cMonth == 12:
# 		fDayofMonth = 5	
# 	elif cMonth == 1 or cMonth == 4 or cMonth ==7:
# 		fDayofMonth = 6						
# else:
# 	if cMonth == 1 or cMonth == 10:
# 		fDayofMonth = 0
# 	elif cMonth == 5:
# 		fDayofMonth = 1
# 	elif cMonth == 8:
# 		fDayofMonth = 2
# 	elif cMonth == 2 or cMonth == 3 or cMonth == 11:
# 		fDayofMonth = 3
# 	elif cMonth == 6:
# 		fDayofMonth = 4
# 	elif cMonth == 9 or cMonth == 12:
# 		fDayofMonth = 5	
# 	elif cMonth == 4 or cMonth ==7:
# 		fDayofMonth = 6	
# dow = (cDay + fDayofMonth + fDayofYear)%7

# print(fDayofYear)
# print(cDofWeek[dow])


