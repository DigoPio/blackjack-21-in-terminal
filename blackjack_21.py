from art import logo
import random

keep_playing = True
while keep_playing:
    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    pc_cards = []
    show_pc_second_card = False
    get_card = 'n'

    def start():
        user_cards.extend(random.sample(cards, 2))
        pc_cards.extend(random.sample(cards, 2))


    def user_get_a_card():
        user_cards.extend(random.sample(cards, 1))


    def pc_get_a_card():
        pc_cards.extend(random.sample(cards, 1))


    def user_score():
        sum_user = sum(user_cards)
        if sum_user > 21:
            if 11 in user_cards:
                ace_change = user_cards.index(11)
                user_cards[ace_change] = 1
                return sum_user
            else:
                return sum_user
        else:
            return sum_user


    def pc_score():
        if show_pc_second_card:
            sum_pc = sum(pc_cards)
        else:
            sum_pc = pc_cards[0]
        if sum_pc > 21:
            if 11 in pc_cards:
                ace_change2 = pc_cards.index(11)
                pc_cards[ace_change2] = 1
                return sum_pc
            else:
                return sum_pc
        return sum_pc


    def blackjack():
        if user_score() == 21:
            return True
        elif pc_score() == 21:
            return True
        else:
            return False


    def is_over():
        if blackjack() and user_score() == 21:
            print('BlackJack! You Win')
            return True
        else:
            if user_score() > 21:
                print('You Lose!')
                return True
            if pc_score() > 21:
                print('You Win!')
                return True
            if get_card == 'n':
                if user_score() < 21 and pc_score() >= 17:
                    compare()
                    return True


    def compare():
        if user_score() > pc_score():
            print('You Win!')
            return True
        if user_score() < pc_score():
            print('You Lose!')
            return True
        if user_score() == pc_score():
            print('It is a draw')
            return True




    start()

    print(f'Player Cards: {user_cards}\nUser Score: {user_score()}\n\n\nComputer Cards: {pc_cards[0]}\nComputer Score: {pc_cards[0]}')

    blackjack()
    while not is_over():
        get_card = input('Get a new card? y or n? ')
        print(80 * "\n")
        if get_card == 'y':
            user_get_a_card()
            user_score()
            print(f'Player Cards: {user_cards}\nUser Score: {user_score()}\n\n\nComputer Cards: {pc_cards[0]}\nComputer Score: {pc_cards[0]}')

        else:
            show_pc_second_card = True
            pc_score()
            while pc_score() < 17:
                pc_get_a_card()
            print(50 * "\n")
            print(f'Player Cards: {user_cards}\nUser Score: {user_score()}\n\n\nComputer Cards: {pc_cards}\nComputer Score: {pc_score()}')

    keep_going = input('Play another game? y or n? ')
    if keep_going == 'y':
        print(50 * "\n")
        keep_playing = True
    else:
        keep_playing = False
