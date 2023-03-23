# README.md

## Background

Slay the Spire is a rogue-like deckbuilding game. This means that the path is procedurally generated and random every time, and that you get a choice of which cards to add and remove regularly. It is a very popular indie game and has spawned many clones.  The runs of interest are a special game mode called "dailies", since they change every day.

## Task Objective

To automate the creation of a YouTube description for each particular Slay the Spire daily attempt.

## Task Details

The description that has to be printed is always in the same format.  Some of the details need to be filled in manually after the YouTube video is recorded, but most of them can be filled in programmatically with information extracted from a .run text file.

The description template contains three tag types:

- Square brackets [] indicate simple tags that should be filled in programatically as part of the first draft of this task.
- Square brackets with asterisks [**] indicate tags that are more complex and don't need to be done for the first draft.
- Curly brackets {} indicate tags that cannot be filled in programmatically and will have to be left blank.

## Technical Details

All tags can be found and extracted from the .run text file. This file is usually located at the following path:
C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\DAILY
The name of the file is random (or maybe it's a time stamp?), so it might be necessary to access the most recently created or modified file in the folder.

### Simple Tags

- [Date]: A written out date, i.e. March 15th. Found in the "local_time" tag in the .run file. Note that it would be better to use the "timestamp" tag , which shows the number of seconds since 1970 (see https://en.wikipedia.org/wiki/Unix_time), but this is not necessary for the first draft.
- [Character]: One of the 4 possible characters: Ironclad | Silent | Defect | Watcher. Found in the "character_chosen" tag in the .run file.
- [Category 1/2/3 modifier]: See full list below for the text to print. Found in the "daily_mods" tag in the .run file.
- [Initial Deck]: If the Category 1 modifiers are "Draft" or "Sealed Deck", then this tag should print "initial deck is shown at , and the". Otherwise it should be blank.
- [final score]: Found in the "score" tag in the .run file.

### Advanced Tags
- [Number of perfected Bosses]: This identifies how many of the 3 boss fights were completed without taking any damage. This information is found in the "damage_taken" tag in the .run file. Specifically, the first boss can be either "Slime Boss", "Hexaghost", or "Guardian". The second boss can be "Collector", "Bronze Automaton", or "Champ". The third boss is always the last entry of that tag, and can be either "Time Eater", "Awakened One", or "Donu and Deca".

### Modifiers

#### Category 1 Modifiers (9 possible modifiers)

- Draft: Draft a custom starting deck of cards.
- Sealed Deck: Craft a deck from 30 random cards.
- Specialized: Start with 5 copies of a single card ([*Added Card*]).
- Heirloom: Start with 1 Rare relic ([*Added Relic*]).
- All Stars: Start with 5 colorless cards ([*List of added cards*])
- Cursed Run: Whenever you defeat a Boss, become Cursed. Your starting relic is replaced with Cursed Key, Darkstone Periapt, and Du-Vu Doll.
- Insanity: Start with a random deck of 50 cards.
- Shiny: Starting deck is replaced with 1 of every rare card.
- Chimera: Your starting deck is a fusion of 3 characters (3x Strike, 3x Defend, 1x Bash, 1x Survivor, 1x Zap, 1x Eruption).

#### Category 2 Modifiers (12 possible modifiers)

- Certain Future: The map contains only one path.
- Flight: You may ignore paths when choosing the next room to travel to.
- Vintage: Normal Enemies drop relics instead of cards.
- Time Dilation: All enemies start with the Slow debuff.
- Hoarder: Whenever you add a card to your deck, add two additional copies. You can no longer remove cards from your deck at the Merchant.
- Red Cards: Red cards now appear in rewards and shops.
- Green Cards: Green cards now appear in rewards and shops.
- Blue Cards: Blue cards now appear in rewards and shops.
- Purple Cards: Purple cards now appear in rewards and shops.
- Diverse: Cards are not restricted by your character.
- Colorless Cards: Colorless cards now appear in rewards and shops.
- Controlled Chaos: Start with Frozen Eye. At the start of your turn add 10 cards to the bottom of your draw pile.

#### Category 3 Modifiers (7 possible modifiers)

- Deadly Events: ? can now contain Elites but are also more likely to contain Treasure rooms.
- Binary: Card rewards contain only 2 cards.
- Midas: Enemies drop 200% more gold, but you cannot upgrade cards at Rest Sites.
- Night Terrors: Resting at Rest Sites heals 100% of your HP, but costs 5 max HP.
- Terminal: Whenever you enter a new room, lose 1 Max HP. Start each combat with 5 Plated Armor.
- Lethality: You start each combat with +3 Strength. All enemies start combat with +3 Strength.
- Big Game Hunter: Elite enemies are now swarming the Spire and will drop better rewards.

## Future improvements

- Detect whether the run was successfully completed
- Describe [*Added Card*], [*Added Relic*], [*Initial Deck modifiers*], [*Number of perfected Elites*], and [*Number of total Elites*] tags
- Use timestamp tag, rather than local_time tag.
