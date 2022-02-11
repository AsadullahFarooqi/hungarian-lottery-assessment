import sys

def main(file_name):
    """
    file_name: players data file name
    """

    print("READY")
    
    # open the players data file
    with open(file_name, 'r') as players_df:
        # reading lottery org nums 
        lottery_nums = input("").strip().split(" ")

        # defining the winner's table
        winners = [0 for i in range(6)]

        # while the number of lottery_nums is equal to 5
        while len(lottery_nums) == 5:
            # reading the file line by line
            for line in players_df:
                # players nums
                player_nums = line.strip().split(" ")
                
                # number of matches in the lottery_nums
                matches = sum([1 for i in range(len(player_nums)) if player_nums[i] == lottery_nums[i]])                   
                winners[matches] += 1

            # print the winners
            print("{} {} {} {}".format(winners[2], winners[3], winners[4], winners[5]))

            # reasking for the lottery_nums
            lottery_nums = input("").strip().split(" ")

            # reset the winners table
            winners = [0 for i in range(6)]

            # seek back to the start of the file
            players_df.seek(0)


if __name__ == '__main__':
    file_name = sys.argv[1]
    main(file_name)