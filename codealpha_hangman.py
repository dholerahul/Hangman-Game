import random

# ------------------------ ASCII HANGMAN ------------------------ #
HANGMAN_PICS = [
    """
       
           
      
    """,
    """
       
           
           O
           
      
    """,
    """
       
           
           O
           |
      
    """,
    """
       
           
           O
          /|
      
    """,
    """
       
           
           O
          /|\\
          
    """,
    """
       
           
           O
          /|\\
          / 
    """,
    """
       
          
           O
          /|\ 
          / \\
      
         
    """
]

# ------------------------ BUILT-IN WORD LIST ------------------------ #
WORD_MEANING = {
    # EASY (3–5 letters)
    "apple": "a sweet fruit",
    "chair": "a piece of furniture used for sitting",
    "books": "a collection of printed works",
    "plant": "a living organism that grows in soil",
    "light": "brightness from a source",
    "table": "a piece of furniture with flat top",
    "bread": "a common baked food",
    "smile": "a facial expression of happiness",
    "phone": "a device used for communication",

    # MEDIUM (6–8 letters)
    "python": "a programming language",
    "hangman": "a classic word guessing game",
    "country": "a nation with its own government",
    "healthy": "being free from illness",
    "airport": "a place where aircraft operate",
    "teacher": "a person who teaches",
    "library": "a place containing books",
    "picture": "a drawing or image",
    "diamond": "a precious gemstone",

    # HARD (9+ letters)
    "beautiful": "pleasing to the senses",
    "important": "of great significance",
    "chocolate": "a sweet food made from cocoa",
    "programmer": "a person who writes software",
    "motivation": "the reason for acting or behaving",
    "university": "an educational institution",
    "scientific": "related to science",
    "assignment": "a task given to someone",
    "leadership": "ability to lead a group"
}

# ------------------------ SPLIT BY DIFFICULTY ------------------------ #

def split_difficulty(word_meaning):
    diff = {"easy": [], "medium": [], "hard": []}

    for word in word_meaning:
        L = len(word)
        if 3 <= L <= 5:
            diff["easy"].append(word)
        elif 6 <= L <= 8:
            diff["medium"].append(word)
        else:
            diff["hard"].append(word)

    return diff


# ------------------------ PLAY ROUND ------------------------ #

def play_round(words, meanings):
    secret = random.choice(words)
    guessed = ["_"] * len(secret)
    used = set()
    wrong = 0

    print(f"\nNew round started! The word has {len(secret)} letters.")

    while wrong < 6 and "_" in guessed:
        print(HANGMAN_PICS[wrong])
        print("Word: ", " ".join(guessed))
        print("Used letters:", " ".join(sorted(used)))
        print("Wrong attempts left:", 6 - wrong)

        letter = input("Enter a letter: ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("❗ Please enter a single alphabet letter.")
            continue

        if letter in used:
            print("⚠ You already guessed that letter.")
            continue

        used.add(letter)

        if letter in secret:
            print("✔ Correct!")
            for i, ch in enumerate(secret):
                if ch == letter:
                    guessed[i] = letter
        else:
            print("✖ Wrong guess!")
            wrong += 1

    # End of round
    print("\nFinal Hangman:")
    print(HANGMAN_PICS[wrong])
    print("The word was:", secret)
    print("Meaning:", meanings.get(secret, "Meaning not found."))

    return "_" not in guessed  # Did the player win?


# ------------------------ MAIN GAME ------------------------ #

def main():
    diff_words = split_difficulty(WORD_MEANING)
    score = 0

    print("\n🎮 HANGMAN GAME (Difficulty + Diagram + Meaning + Score)")
    
    while True:
        print("\nChoose difficulty:")
        print(" easy   → 3–5 letters")
        print(" medium → 6–8 letters")
        print(" hard   → 9+ letters")
        choice = input("Enter difficulty or 'quit': ").lower()

        if choice == "quit":
            break

        if choice not in diff_words or not diff_words[choice]:
            print("❗ Invalid difficulty choice.")
            continue

        won = play_round(diff_words[choice], WORD_MEANING)

        if won:
            print("🎉 You WIN! +10 points")
            score += 10
        else:
            print("💀 You lost the round!")

        print("Current Score:", score)

        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            break

    print("\n Final Score:", score)
    print("Thanks for playing Hangman!")


if __name__== "__main__":
    main()