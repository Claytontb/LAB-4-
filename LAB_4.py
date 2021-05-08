""" 
This program allows a user three tries to guess the correct ansewer to the question 
question = "What is the capital of California". The anser is "Sacramento".

We first set max_tries = 3. Then we create a loop to iterate three times. For each iteration, 
we ask the user for the anser (user input). Then based on the answer the user gives we check
to se if the user input matches the anser. If so, print "Correct!", then terminate the loop with a 
break statement.

if the user could not guess the correct anser within the max_tries, then print 
"You have used up your allotment of guesses", then print "The correct answer is "Sacramento" 
"""

"""

main 
    question = "what is the capital of California"
    answer = "Sacramento"
    ask(question, answer)

ask
    tries = 0 
    loop three times 
        increment tries by 1 
        ask user input()
        check to see of user input is equal to anser 
            if so print "Correct" the exit loop
    if not correct 
        print to the user "you have used uo your allotment of guesses."
        print the correct answer "The correct answer is "Sacramento"

main 
"""

def main():
    question = "what is the capital of California"
    answer = "Sacramento"
    ask(question, answer)

def ask(question, answer, max_tries =3)
    tries = 0
    ans = ""
    while tries < max_tries:
        tries += 1
        ans = input(question)
        if ans == answers 
            print("Correct!")
            break
    if ans != answer:
        print ("You hav used up your allotment of guesses.")


main()