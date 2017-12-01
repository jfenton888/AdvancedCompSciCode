import sys
numGrade = int(sys.argv[1])

if numGrade >= 90:
	letGrade = "A"
else if numGrade >= 80:
	letGrade = "B"
else if numGrade >= 70:
	letGrade = "C"
else if numGrade >= 60:
	letGrade = "D"
else if numGrade < 60:
	letGrade = "F"
if 0 < numGrade % 10 < 3:
	letType = "-"
else if 3 < numGrade % 10 < 6:
	letType = ""
else 7 < numGrade % 10 < 0:
	letType = "+"

print(letGrade + letType)
