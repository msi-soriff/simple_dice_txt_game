import random

def roll_dice():
    return random.randint(1, 6)

def print_track(position1, position2, finish_line):
    track = '-' * finish_line
    track = track[:position1] + '1' + track[position1+1:]
    track = track[:position2] + '2' + track[position2+1:]
    print(track)

def main():
    finish_line = 30
    player1_pos = 0
    player2_pos = 0

    print("Welcome to the Racing Game!")
    print(f"First player to reach position {finish_line} wins!\n")

    while player1_pos < finish_line and player2_pos < finish_line:
        input("Player 1, press Enter to roll the dice.")
        move1 = roll_dice()
        player1_pos += move1
        print(f"Player 1 rolls a {move1} and moves to position {player1_pos}")
        print_track(player1_pos, player2_pos, finish_line)

        if player1_pos >= finish_line:
            print("Player 1 wins the race!")
            break

        input("Player 2, press Enter to roll the dice.")
        move2 = roll_dice()
        player2_pos += move2
        print(f"Player 2 rolls a {move2} and moves to position {player2_pos}")
        print_track(player1_pos, player2_pos, finish_line)

        if player2_pos >= finish_line:
            print("Player 2 wins the race!")
            break

    print("Game over. Thanks for playing!")

if __name__ == "__main__":
    main()
