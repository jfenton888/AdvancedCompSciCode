data = [[],[]]
qAsked = 0
person = 0
q = ['Who are you\n' , 'dogs or cats\n' , 'are you as cool as Z\n']
while True:
	while qAsked <= 3:
		data[person][qAsked] = input(q[qAsked])
		if data[person][0] == Z or data[person][0] == Zhi:
			data[person][2] = 'Oh wait this is ' + data[person] + ' he wins'
		qAsked += 1
	lastPers = (input('Are you the last person to take my survey \n') + ' ')
	if lastPers == 'yes':
		numOfPers = len(data)//3
		break
	person += 1
perDisp = 0
if perDisp <= numOfPers:
	print (data[perDisp])