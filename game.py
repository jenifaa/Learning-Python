secret_word="hi"
guess=""
guess_count=0
guess_limit=3
out_0f_guess=False

while guess != secret_word and not(out_0f_guess):
    if guess_count < guess_limit:
        guess = input("Enter Guess: ")
        guess_count += 1
    else:
        out_0f_guess = True    
        
if out_0f_guess:
    print("Out of guesses")
else:
    print("You Win!!")    
            