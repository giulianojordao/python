prompt = 'Please entere a score between 0.0 and 1.0: '
score = raw_input(prompt)

try:
	score = float(score)
	
	if score >= 0.9 and score <= 1.0:
		grade = 'A'
	elif score >= 0.8 and score < 0.9:
		grade = 'B'
	elif score >= 0.7 and score < 0.8:
		grade = 'C'
	elif score >= 0.6 and score < 0.7:
		grade = 'D'
	elif score < 0.6:
		grade = 'F'
	else:
		grade = 'Bad score'
	print 'Grade: ', grade
	
except:
	print 'Please enter proper score between 0.0 and 1.0!'	