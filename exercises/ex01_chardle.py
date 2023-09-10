"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730662370"

player_word: str = input("Enter a 5-Character word: ")
player_letter: str = input("Enter a single character: ")

if len(player_word) != 5:
    print("Error: word must contain 5 characters")
    exit()
if len(player_letter) != 1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + player_letter + " in " + player_word)

count: int = 0
if player_word[0] == player_letter:
    print(player_letter + " found at index 0")
    count += 1
if player_word[1] == player_letter:
    print(player_letter + " found at index 1")
    count += 1
if player_word[2] == player_letter:
    print(player_letter + " found at index 2")
    count += 1
if player_word[3] == player_letter:
    print(player_letter + " found at index 3")
    count += 1
if player_word[4] == player_letter:
    print(player_letter + " found at index 4")
    count += 1
if count == 0:
    print("No instances of" + player_letter + " found in " + player_word)
elif count == 1:
    print("1 instance of " + player_letter + " found in" + player_word)
else:
    print(str(count) + " instances of " + player_letter + " found in " + player_word)