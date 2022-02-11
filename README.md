# Hungarian Lottery problem

Before getting to the description, I'd like to tell you some of my assumptions.
I assumed that the comparison has to be index wise. The problem can get a little tricky
if the order doesn't matter. For for example if the `lottery-numbers: [3,5,62,9,22]`
and the `player_nums:[55,5,6,44,9]`, there are 2 numbers matching `[5,9]`.
So in that case I'll have to search for that as well. Which won't affect the big-Oh
very much. It'll only add another constant.

So I've added both cases code with comments.
For the 2nd case we can add more improved logic but still it's constant.

The idea is to have a winners table and update the table while reading the lines
from the data file without closing it for the next lottery numbers.

The most efficient point in the solution is the winners table, the number of
matches in the winner table of the current player is the index of the winners table.

Run the below command to run the code:

```bash
python3 <players_data_file>
```

Time complexity =>  O(N): where N is the number of players
Space complexity => O(1): constant.

Improvement ideas:
As we can't generate the result until we don't check all the players numbers in the lottery
numbers. For that reason the only way to speed it up is by reading the players data as fast
as possible. So can store the lines of the file in a list and maybe run multiple functions
concurrently.
