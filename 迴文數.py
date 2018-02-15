import time
#Make main func
def Main(Num):
	t = 0
	n1 = int(Num[::-1])
	n2 = int(Num)
	a = n1+n2

	while True:
		print(a)
		t += 1
		a = str(a)
		if a == a[::-1]:
			print("You got a cycle number by reverse adding %d times!" % (t))
			t = 0
			while True:
				answer = input("Wanna try again? type y/n:")
				if answer in ('y','n'):
					break
				print ('I mean that You should type either y or n, it stands for yes and no!')
			if answer == 'y':
				a = input()
				n1 = int(a)
				n2 = int(a[::-1])
				a = n1 + n2
				continue
			else:
				print ('Thanks for useing SKA Technology, have a nice day! :)')
				sl = 5
				while sl != 0:
					print('Closing in %d second' % (sl))
					sl -= 1
					time.sleep(1)
				break
		else:
			n1 = int(a)
			n2 = int(a[::-1])
			a = n1+n2
			continue


			
			
#Ask number.
print('Welcome to use SKA useless cycle machine v 1.0.0!')
print("What number did you want to try?")
Number = input()
Main(Number)