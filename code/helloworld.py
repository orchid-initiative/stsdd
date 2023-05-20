#print("Hello, World!")
import json
from re import A

# Read the file
with open(r"C:\Users\kylep\source\repos\stsdd\data\1678867185.run",'r') as filename:
    game_data = json.load(filename)


# Get the data you need from the file
date = game_data["local_time"]
uppercharacter = game_data["character_chosen"]
finalscore = game_data["score"]

# Write the output
# all things to do with date
year = date[0:4]
month = date[4:6]
day = date[6:8]
# day suffix assigment
if day in [1, 21, 31]:
    suffix = 'st'
elif day in [2, 22]:
    suffix = 'nd'
elif day in [3, 23]:
    suffix = 'rd'
else:
    suffix = 'th'
# assigning number of month to month letters
import calendar
lettermonth = calendar.month_name[int(month)]

# lowercases the character
character = uppercharacter.title()

# Open a file in write mode
file = open("output.txt", "w")

# Write to the file
file.write(f"""Slay the Spire {lettermonth} {day}{suffix}, {year} Daily - {character} | {{Manual text}}

Hi All! This is my attempt at the {lettermonth} {day}{suffix}, {year} Daily with the {character}. The [Initial Deck] run starts at .
The modifiers for this daily are:

1. [Category 1 modifier]: [Category 1 modifier description].
2. [Category 2 modifier]: [Category 2 modifier description].
3. [Category 3 modifier]: [Category 3 modifier description].

My final score was {finalscore}, which was {{Manual text}}. I perfected [*Number of perfected Elites*]/[*Number of total Elites*] possible Elites and [Number of perfected Bosses]/3 of the bosses.

Slay the Spire is a game created and developed by Mega Crit Games. An Early Access version was released in November 2017, and was updated almost weekly until the full release on January 23, 2019. Version 2.0 was released on January 14, 2020, which included many added relics, potions, and most importantly, the fourth character.

"We fused card games and roguelikes together to make the best single player deckbuilder we could. Craft a unique deck, encounter bizarre creatures, discover relics of immense power, and Slay the Spire!" - Steam Store Page (https://store.steampowered.com/app/646570/Slay_the_Spire)

The Friends mod I use at the beginning can be found here: https://steamcommunity.com/sharedfiles/filedetails/?id=2945101786
Thanks again Stephen!

00:00 Intro
[*Initial Deck modifiers*]
{{Manual text}} Act I
{{Manual text}} Act I boss fight
{{Manual text}} Act II
{{Manual text}} Act II boss fight
{{Manual text}} Act III
{{Manual text}} Act III boss fight
{{Manual text}} Recap

#LetsPlay #SlayTheSpire #SlayTheSpireDaily

{character}, The {character}, {lettermonth} {day}{suffix}, {year} daily, {lettermonth} {day}{suffix}, {year}, {lettermonth} {day}{suffix}, {month}{day}, {day}{month}, {month}.{day}.{year}, {day}.{month}.{year}, {month}.{day}, {day}.{month}, [Category 1 modifier], [Category 2 modifier], [Category 3 modifier]
""")


# Close the file
file.close()