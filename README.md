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