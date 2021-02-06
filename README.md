### Assignment

For this challenge, you will create a program to play Rock, Paper, Scissors. A program that picks at random will usually win 50% of the time. To pass this challenge your program must play matches against four different bots, winning at least 60% of the games in each match.


### Solution

Your bot has to play 1000 games and win 60% of the time(or more!). You might thing that a 50% chance of winning is awlays there since both players just choose randomly and over large amount of games it evens out.
What happens when your program your bot to memorise human(or other bot) moves? You can now check for patterns as humans(and computers) are predictable.

### Knuth-Morris-Pratt

I've decided to implement my solution using KMP algorithm to check for patterns inside a string of all moves your opponent has played.

The program takes last 3 moves played by opponent and tries to predict the next move using KMP to help us find the patterns.

### Win/Lose

Verses a truly random player that doesn't leave patterns, percentage varies around 50%.
Versus players that make a lot of easy patterns, the bot wins in 70-99 percent of the time.
Versus players that have a more advanced playstyle that also includes patterns, we win in about 60% of the time.

### My bot is located in RPS file, and I've also added 2 other bots.
### All other code is generated from the freeCodeCamp using Repl.it


