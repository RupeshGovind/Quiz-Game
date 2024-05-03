print("Choose options using both uppercase and lowercase letters:")
def run_quiz(questions):
    score = 0
    skipped_count = 0
    for question, answer in questions.items():
        print(question)
        user_answer = input("Choose the correct options: ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            print(" ")
            score += 1
        elif user_answer == "":
            skipped_count = skipped_count+1
            print("|--------------------------|")
            print(f"|You Skipped {skipped_count} Questions   |")
            print("|--------------------------|")
            print(" ")
            continue
        else:
            print("Incorrect!")
            print(" ")
    print("Quiz complete! You scored {}/{}.".format(score, len(questions)))


quiz_questions = {

    "What color is the sky during the day?\nA: Red       B: Pink\nC: Yellow    D: Blue": "D",
    "How many continents are there on Earth?\nA: 5        B: 6\nC: 7        D: 8": "C",
    "Which planet is known as the Red Planet?\nA: Mars    B: Jupiter\nC: Saturn   D: Venus": "A",
    "What is the capital of the United States?\nA: New York City  B: Los Angeles\nC: Washington, D.C.  D: Chicago": "C",
    "What is the largest mammal in the world?\nA: Elephant      B: Giraffe\nC: Blue whale       D: Lion": "C",
    "What is the chemical symbol for oxygen?\nA: O            B: H\nC: O2           D: N": "A",
    "What is the primary language spoken in Brazil?\nA: Spanish   B: Portuguese\nC: English      D: French": "B",
    "What is the tallest mountain in the world?\nA: Mount Kilimanjaro   B: Mount Everest\nC: K2          D: Mount Fuji": "B",
    "How many sides does a triangle have?\nA: 3         B: 4\nC: 5         D: 6": "A",
    "What is the chemical symbol for gold?\nA: Ag        B: Au\nC: Fe        D: Cu": "B"
}
run_quiz(quiz_questions)