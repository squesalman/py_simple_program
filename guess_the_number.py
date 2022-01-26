import random



def diff_bet_gen_and_input(num_guess,num_gen):
	if num_guess > num_gen:
		return 'Your guess is too high'
	elif num_guess < num_gen:
		return 'Your guess is too low'
	else:
		return f'Correcto Mundo!{num_guess}'


def compare(num_guess,num_gen):
	if num_guess > num_gen:
		return num_guess - num_gen
	else:
		return num_gen - num_guess

def play_again():
	choice = 'check'

	while choice not in ['Y','N']:

		choice = input("Play again ? -Y or -N")
		if choice.capitalize() not in ['Y','N']:
			print("Enter 'Y' or 'N' only")

	if choice.capitalize() == 'Y':
		return True
	else:
		return False


play = True
check = True
while True:
	while True:
		guessnum = input("Enter Your Guess : ")
		try:
			val = int(guessnum)
			print("It's a valid Number")
			break
		except ValueError:
			print("Not a valid number ")

	start_play ="check"
	
	while start_play not in ['Y','N']:	
		start_play = input("Start play now? -Y or -N only")
		if start_play.capitalize() not in ['Y','N']:
			print("Please enter Y or N only")

	if start_play.capitalize() =='Y':
		game_on = True
	else:
		game_on = False
	
	while game_on:	
		num_gen = random.randint(0,10)
		print(diff_bet_gen_and_input(val,num_gen))		
		print(f"Comparison value : {compare(val,num_gen)}")
		print(f"Your guess :{val} , random gen number : {num_gen} ")
		break
	if not play_again():
		break
# To break if guess correctly
