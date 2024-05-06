import sys

questions = {}
answers_correct = 0

# write out each question to Questions and Answers dictionary, else return a statement of an error so the user knows how to reformat.
def read_questions():
    with open('questions.txt', 'r') as file:
        try:
            for line in file:
                # split the line into a question and an answer, using the question mark to separate them
                question, answer = line.strip().split('?')
                # if there is no answer, raise an error
                if answer == '':
                    raise ValueError
                questions[question.strip()] = answer.strip()
        # handling value error, if there is no answer or if the question is formatted incorrectly
        except ValueError:
            print("Make sure the questions and answers are separated by a question mark, and that there is only one answer per question.\nThere can only be ONE question mark per line!")
            sys.exit()

    return questions

def start_game():
    global answers_correct
    questions = read_questions()
# the output of the question will prompt the user to respond with an answer to the question, of which the program will compare to the answer and dictate whether it is correct or not.
    try:
        # loops through each question and answer in the dictionary
        for question, answer in questions.items():
            user_answer = input(question + '? ').strip()
            # determines if the user's answer is correct and increments the correct answer counter, otherwise prints that the answer is incorrect and gives the correct answer.
            if user_answer.lower() == answer.lower():
                print("Correct!")
                answers_correct += 1
            else:
                print(f"Wrong!\nThe correct answer is: {answer}")

        # prints the final score in a percentage.
        print(f"Game Over! Your score is {round((answers_correct/len(questions))*100)}%!")
        sys.exit
    # handles keyboard interrupt, so user can quit the game.
    except KeyboardInterrupt:
        print("\nBye!")
        sys.exit()
    # handles value error, if there are no questions in the file.
    except UnboundLocalError:
        print("Make sure you put questions and answers in the questions.txt file!")
        sys.exit()

def main():
    # prompts player for input on whether they want to play, and starts the game if they do, otherwise exits the program.
    play = (input("Welcome to Quiz Game! Would you like to play a game?(Y/n)")).lower()
    if play in ["y", "yes", ""]:
        start_game()
    else:
        sys.exit()

# runs the program
if __name__ == "__main__":
    main()