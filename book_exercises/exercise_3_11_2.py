import time

prompt1 = 'Enter hours: '
prompt2 = 'Enter rate: '

hours = raw_input(prompt1)
rate = raw_input(prompt2)

hours = float(hours)
rate = float(rate)

if hours > 40:
	overtime = hours - 40
	otrate = 1.5 * rate
	pay = 40 * rate + overtime * otrate

else: 
	pay = hours * rate

print 'Pay: ', pay

time.sleep(3)

