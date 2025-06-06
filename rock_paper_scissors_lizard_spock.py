import random

def rock_paper_scissors_lizard_spock():
    options = {
        1: {'name': 'Rock', 'emoji': '✊'},
        2: {'name': 'Paper', 'emoji': '✋'},
        3: {'name': 'Scissors', 'emoji': '✌️'},
        4: {'name': 'Lizard', 'emoji': '🦎'},
        5: {'name': 'Spock', 'emoji': '🖖'}
    }
    
    rules = {
        1: [3, 4],  # Rock crushes Scissors and Lizard
        2: [1, 5],   # Paper covers Rock and disproves Spock
        3: [2, 4],   # Scissors cut Paper and decapitate Lizard
        4: [2, 5],   # Lizard eats Paper and poisons Spock
        5: [1, 3]    # Spock vaporizes Rock and smashes Scissors
    }
    
    action_descriptions = {
        (1, 3): "Rock crushes Scissors",
        (1, 4): "Rock crushes Lizard",
        (2, 1): "Paper covers Rock",
        (2, 5): "Paper disproves Spock",
        (3, 2): "Scissors cut Paper",
        (3, 4): "Scissors decapitate Lizard",
        (4, 2): "Lizard eats Paper",
        (4, 5): "Lizard poisons Spock",
        (5, 1): "Spock vaporizes Rock",
        (5, 3): "Spock smashes Scissors"
    }
    
    print("================================")
    print("Rock Paper Scissors Lizard Spock")
    print("================================")
    print()
    
    for num, data in options.items():
        print(f"{num}) {data['emoji']}")
    
    while True:
        try:
            choice = int(input("Pick a number: "))
            if choice in options:
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")
    
    cpu_choice = random.randint(1, 5)
    
    print(f"\nYou chose: {options[choice]['emoji']}")
    print(f"CPU chose: {options[cpu_choice]['emoji']}")
    
    if choice == cpu_choice:
        print("It's a tie!")
    else:
        if cpu_choice in rules[choice]:
            # player wins
            action = action_descriptions.get((choice, cpu_choice), "")
            print(f"You win! {action}")
        else:
            # CPU wins
            action = action_descriptions.get((cpu_choice, choice), "")
            print(f"CPU wins! {action}")

rock_paper_scissors_lizard_spock()