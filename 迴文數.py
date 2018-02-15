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
			print("You got a Palindromic number by reverse adding %d times!" % (t))
			t = 0
			while True:
				answer = input("Wanna try again? type y/n:")
				if answer in ('y','n'):
					break
				print ('I mean that You should type either y or n, it stands for yes and no!')
			if answer == 'y':
				a = input('The number I want to try is:')
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
print('Welcome to use SKA useless Palindromic Number machine v 1.0.1!')
print('By:Iron_Peach')
print('If you have bug, please report that to Iron_Peach@protonmail.com')
while True:
	answer = input('Did you know what is Palindromic number? y/n:')
	if answer in ('y','n'):
		break
	print('I think you should put lower case y or n for the answer...')
if answer == 'y':
	print ('Good, now go to the main part! And I\'m gonna ask you:')
else:
	print('Palindromic number mean the number that is the same either fromm left to right, and right to left. For example, 1234567654321 is a Palindromic number because both side are the same!3883 can be one, 77 is one too! The way you change a number to Palindromic number is that you add the number with its opposite, for example, 32 would add 23 because it\'s opposite, 32 + 23 = 55! It\'s a Palindromic! If you don\'t get a Palindromic number, try again with your new number Like 67 + 76 = 143 ; 143 + 341 = 484. But there is some number that can\'t be Palindromic(Maybe, who knows?), those are called Lychrel Number, 196 is the most likely the smallest Lychrel (BTW, the world record of Palindromic is 1186060307891929990, it takes add 261 times to make it Palindromic. Maybe you can be the next world record holder! Keep useign our tools! ^_^). Now, go to the main part and I\'m gonna ask you:')
print("what number did you want to try?")
Number = input()
Main(Number)
#1186060307891929990! What a magical number! It take 261 times to make a Palindromic!