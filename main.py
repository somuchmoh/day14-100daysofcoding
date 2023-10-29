import game_data
import random
import art 


def first_choice():
    choice_a = choice_list_final[counter]
    print(f"Compare A: {choice_a['name']}, {choice_a['description']}, from {choice_a['country']} has {choice_a['follower_count']}")
    return choice_a

def second_choice():
    choose_personality()
    choice_b = choice_list_final[counter+1]
    print(f"Against B: {choice_b['name']}, {choice_b['description']}, from {choice_b['country']}, has {choice_b['follower_count']}")
    return choice_b
    
def choose_personality():
    for i in range(1):
        r = random.choice(game_data.data)
        if r not in choice_list_final:
            choice_list_final.append(r)


game_play = True
choice_list_final = []
counter = 0 
score = 0 
print(art.logo)
while game_play:
    choose_personality()
    choice_a = first_choice()
    print(art.vs)
    choice_b = second_choice()
    user_answer = input("Who has more followers? Type 'A' or 'B':  \n")
    if choice_a['follower_count'] > choice_b['follower_count']:
        if user_answer == 'A':
            print("You are right")
            choice_a = choice_a
            counter += 1
            score += 1
        elif user_answer == 'B':
            print(f"You are wrong. Final score: {score}")
            game_play = False
    elif choice_a['follower_count'] < choice_b['follower_count']:
        if user_answer == 'A':
            print(f"You are wrong. Final score: {score}")
            game_play = False
        elif user_answer == 'B':
            print("You are right")
            choice_a = choice_b
            counter += 1
            score += 1
