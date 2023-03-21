Background:
Slay the Spire is a rogue-like deckbuilding game. This means that the path is procedurally generated and random every time, and that you get a choice of which cards to add and remove regularly. It is a very popular indie game and has spawned many clones. 

Task Objective:
To automate the creation of a YouTube description for each particular Slay the Spire daily attempt.

Task Details:
The runs of interest are a special game mode called "dailies", since they change every day. There are 3 categories of modifiers: Category 1 (9 possible modifiers), Category 2 (12 possible modifiers), and Category 3 (7 possible modifiers). A list of all 28 modifiers is listed below. The description that has to be printed is always in the same format:

{Note: Tags inside square brackets [] are explained below. Tags inside curly brackets {} will have to be left blank. The 2 tags with asterisks [**] are difficult to do and don't need to be done for the first draft.}

Slay the Spire [Date] Daily - [Character] | {Manual text}

Hi All! This is my attempt at the [Date] Daily with the [Character]. The [Initial Deck] run starts at .
The modifiers for this daily are:

1. [Category 1 modifier]: [Category 1 modifier description].
2. [Category 2 modifier]: [Category 2 modifier description].
3. [Category 3 modifier]: [Category 3 modifier description].

My final score was [final score], which was {Manual text}. I perfected [*Number of perfected Elites*]/[*Number of total Elites*] possible Elites and [Number of perfected Bosses]/3 of the bosses.

Slay the Spire is a game created and developed by Mega Crit Games. An Early Access version was released in November 2017, and was updated almost weekly until the full release on January 23, 2019. Version 2.0 was released on January 14, 2020, which included many added relics, potions, and most importantly, the fourth character.

"We fused card games and roguelikes together to make the best single player deckbuilder we could. Craft a unique deck, encounter bizarre creatures, discover relics of immense power, and Slay the Spire!" - Steam Store Page (https://store.steampowered.com/app/646570/Slay_the_Spire)

The Friends mod I use at the beginning can be found here: https://steamcommunity.com/sharedfiles/filedetails/?id=2945101786
Thanks again Stephen!

00:00 Intro
[*Initial Deck modifiers*]
{Manual text} Act I
{Manual text} Act I boss fight
{Manual text} Act II
{Manual text} Act II boss fight
{Manual text} Act III
{Manual text} Act III boss fight
{Manual text} Recap

#LetsPlay #SlayTheSpire #SlayTheSpireDaily

[Character], The [Character], [Date] daily, [Date], [Date as Month Day], [Date as MMDD], [Date as DDMM],  [Date as MM.DD.CCYY], [Date as DD.MM.CCYY], [Date as MM.DD], [Date as DD.MM], [Category 1 modifier], [Category 2 modifier], [Category 3 modifier]

For example:
Slay the Spire March 15th Daily - Watcher | When you get lots of cards, it's hard to draw right ones

Hi All! This is my attempt at the March 15th Daily with the Watcher. The run starts at 3:36.
The modifiers for this daily are:

1. Chimera: Your starting deck is a fusion of 3 characters (3x Strike, 3x Defend, 1x Bash, 1x Survivor, 1x Zap, 1x Eruption).
2. Time Dilation: All enemies start with the Slow debuff.
3. Night Terrors: Resting at Rest Sites heals 100% of your HP, but costs 5 max HP.

My final score was 1414, which was ok. I perfected 7/8 possible Elites and 2/3 of the bosses.

Slay the Spire is a game created and developed by Mega Crit Games. An Early Access version was released in November 2017, and was updated almost weekly until the full release on January 23, 2019. Version 2.0 was released on January 14, 2020, which included many added relics, potions, and most importantly, the fourth character.

"We fused card games and roguelikes together to make the best single player deckbuilder we could. Craft a unique deck, encounter bizarre creatures, discover relics of immense power, and Slay the Spire!" - Steam Store Page (https://store.steampowered.com/app/64...)

The Frienship mod I use at the beginning can be found here: https://steamcommunity.com/sharedfile...
Thanks again Stephen!

00:00 Intro
03:36 Act I
13:07 Act I boss fight
13:50 Act II
29:53 Act II boss fight
34:35 Act III
52:34 Act III boss fight
57:59 Recap

#LetsPlay #SlayTheSpire #SlayTheSpireDaily

Watcher, The Watcher, March 15th daily, March 15th, March 15, 0315, 1503, 03.15.2023, 15.03.2023, 03.15, 15.03, Chimera, Time Dilation, Night Terrors, 

(Also found here: https://www.youtube.com/watch?v=ZNju7QVxoMo)

Technical Details:
All tags can be found and extracted from the attached file. This file is usually located at the following path:
C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\DAILY
The name of the file is random (or maybe it's a time stamp?), so it might be necessary to access the most recently created or modified file in the folder.

Tag description:
[Date]: A written out date, i.e. March 15th. Found in the "local_time" tag in the .run file. Note that it would be better to use the "timestamp" tag , which shows the number of seconds since 1970 (see https://en.wikipedia.org/wiki/Unix_time), but this is not necessary for the first draft. 
[Character]: One of the 4 possible characters: Ironclad | Silent | Defect | Watcher. Found in the "character_chosen" tag in the .run file.
[Initial Deck]: If the Category 1 modifiers are "Draft" or "Sealed Deck", then this tag should print "initial deck is shown at , and the". Otherwise it should be blank.

[Category 1/2/3 modifier]: See full list below for the text to print. Found in the "daily_mods" tag in the .run file.
[final score]: Found in the "score" tag in the .run file.
[Number of perfected Bosses]: This identifies how many of the 3 boss fights were completed without taking any damage. This information is found in the "damage_taken" tag in the .run file. Specifically, the first boss can be either "Slime Boss", "Hexaghost", or "Guardian". The second boss can be "Collector", "Bronze Automaton", or "Champ". The third boss is always the last entry of that tag, and can be either "Time Eater", "Awakened One", or "Donu and Deca".

Category 1 modifiers:
Draft: Draft a custom starting deck of cards.
Sealed Deck: Craft a deck from 30 random cards.
Specialized: Start with 5 copies of a single card ([*Added Card*]).
Heirloom: Start with 1 Rare relic ([*Added Relic*]).
All Stars: Start with 5 colorless cards ([*List of added cards*])
Cursed Run: Whenever you defeat a Boss, become Cursed. Your starting relic is replaced with Cursed Key, Darkstone Periapt, and Du-Vu Doll.
Insanity: Start with a random deck of 50 cards.
Shiny: Starting deck is replaced with 1 of every rare card.
Chimera: Your starting deck is a fusion of 3 characters (3x Strike, 3x Defend, 1x Bash, 1x Survivor, 1x Zap, 1x Eruption).

Category 2 modifiers:
Certain Future: The map contains only one path.
Flight: You may ignore paths when choosing the next room to travel to.
Vintage: Normal Enemies drop relics instead of cards.
Time Dilation: All enemies start with the Slow debuff.
Hoarder: Whenever you add a card to your deck, add two additional copies. You can no longer remove cards from your deck at the Merchant.
Red Cards: Red cards now appear in rewards and shops.
Green Cards: Green cards now appear in rewards and shops.
Blue Cards: Blue cards now appear in rewards and shops.
Purple Cards: Purple cards now appear in rewards and shops.
Diverse: Cards are not restricted by your character.
Colorless Cards: Colorless cards now appear in rewards and shops.
Controlled Chaos: Start with Frozen Eye. At the start of your turn add 10 cards to the bottom of your draw pile.

Category 3 modifiers:
Deadly Events: ? can now contain Elites but are also more likely to contain Treasure rooms.
Binary: Card rewards contain only 2 cards.
Midas: Enemies drop 200% more gold, but you cannot upgrade cards at Rest Sites.
Night Terrors: Resting at Rest Sites heals 100% of your HP, but costs 5 max HP.
Terminal: Whenever you enter a new room, lose 1 Max HP. Start each combat with 5 Plated Armor.
Lethality: You start each combat with +3 Strength. All enemies start combat with +3 Strength.
Big Game Hunter: Elite enemies are now swarming the Spire and will drop better rewards.

Future improvements:
- Detect whether the run was successfully completed
- Describe [*Added Card*], [*Added Relic*], [*Initial Deck modifiers*], [*Number of perfected Elites*], and [*Number of total Elites*] tags
- Use timestamp tag, rather than local_time tag.
