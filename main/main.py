import os

# --------------------------
# QUIZ QUESTIONS
# --------------------------

quiz = {
    'question1': {
        'question': 'Which toy is famously known for the slogan "The toy that smiles back"?',
        'options': ['A. Teddy Bear', 'B. Mr Potato Head', 'C. Barbie', 'D. Play-Doh'],
        'answer': 'A'
    },
    'question2': {
        'question': 'What year was the first LEGO brick produced?',
        'options': ['A. 1932', 'B. 1949', 'C. 1958', 'D. 1965'],
        'answer': 'B'
    },
    'question3': {
        'question': 'In the game Monopoly, which property is the most expensive?',
        'options': ['A. Park Place', 'B. Mayfair', 'C. Boardwalk', 'D. Piccadilly'],
        'answer': 'C'
    },
    'question4': {
        'question': 'Which popular video game features characters called Mario, Luigi, and Princess Peach?',
        'options': ['A. Sonic the Hedgehog', 'B. Donkey Kong', 'C. Super Mario', 'D. Pokémon'],
        'answer': 'C'
    },
    'question5': {
        'question': 'What is the name of the doll that became a cultural icon in 1959 and is known for her blonde hair?',
        'options': ['A. Bratz', 'B. Barbie', 'C. Polly Pocket', 'D. Cabbage Patch Kid'],
        'answer': 'B'
    }
}

# --------------------------
# LOAD LEADERBOARD
# --------------------------

def load_leaderboard():
    leaderboard = {}
    try:
        with open("leaderboard.txt", "r") as file:
            for line in file:
                name, score = line.strip().split(":")
                leaderboard[name] = int(score)
    except FileNotFoundError:
        pass
    return leaderboard


# --------------------------
# SAVE LEADERBOARD
# --------------------------

def save_leaderboard(leaderboard):
    with open("leaderboard.txt", "w") as file:
        for name, score in leaderboard.items():
            file.write(f"{name}:{score}\n")


leaderboard = load_leaderboard()


# --------------------------
# QUIZ FUNCTION
# --------------------------

def start_quiz():
    # Wait for user to press A
    while True:
        begin = input('Press A to begin the quiz: ').strip().upper()
        if begin == 'A':
            break
        else:
            print("Invalid input. Please press A to begin.")

    name = input("Please enter your username: ")

    score = 0

    # Quiz loop
    for index, (key, value) in enumerate(quiz.items(), start=1):
        print(f"\nQuestion {index} of {len(quiz)}:")
        print(value['question'])

        for option in value['options']:
            print(option)

        guess = input("Enter A, B, C or D: ").strip().upper()

        if guess == value['answer']:
            score += 50
            print("Correct!")
        else:
            print(f"Incorrect, the correct answer is: {value['answer']}")

    # Final score (printed ONCE)
    print(f"\n🎉 Thank you for completing the quiz! Your final score is {score}.\n")

    # --------------------------
    # UPDATE LEADERBOARD
    # --------------------------

    # Keep highest score if user exists
    if name in leaderboard:
        if score > leaderboard[name]:
            leaderboard[name] = score
    else:
        leaderboard[name] = score

    # Sort leaderboard highest first
    leaderboard = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True))

    # Save to file
    save_leaderboard(leaderboard)

    # Print leaderboard
    print("🏆 LEADERBOARD 🏆")
    for player, player_score in leaderboard.items():
        print(f"{player}: {player_score}")


# --------------------------
# RUN PROGRAM
# --------------------------

start_quiz()
