# Text RPG Project
We want to create an RPG game. This game is about a strong hero that traveling around the world and fights against monsters.  
All the game processes are divided into two parts - hero action and world action.   
There is common information about the expected program. You are free for implementation and additional functions.  
All that we needs:
  * A Hero
  * An Enemies
  * A Map (additional)
  * A Quests (additional)


# Hero
<img src="https://user-images.githubusercontent.com/52273527/137013564-03077421-7ae3-4f04-9429-d305d9d75f51.png" width="100" />

Hero is a player role.  
Before starting a new game player inputs Hero's name and Race.  
We ask the player which action our Hero must do. The hero may do actions while he has actions points.  
The hero may grow up, so we need a system of abilities and for next level needs more experience.  
When Hero level up user may choose which characteristics will grow - health, strength, mana.  Also, Hero may learn one new ability or upgrade old.  
The hero may use Items.  
#### Hero have a custom characteristics: 
  * Name `: str`
  * Race `: str`
#### And also hero have a standart start characteristics:
  * Health `: int = 100`
  * Level `: int = 1`
  * experience `: int`
  * nextLevelExp `: int`
  * Mana `: int = 20`
  * Strength `: int = 10`
  * ActionsPoints `: int`
  * Abilities `: Abillity[]`
  * Bag `: Item[]`
  * Equipment ```: {
      armor : Armor,
      weapon: Weapon
  }```  
  * Quests: `: Quest[]` (additional)  
#### Hero's basic actions:
  * explore
      > This action for finding more about an object
  * attack
  * use Ability
      > This action allows use ability that hero already have
  * use Item
      > Use Item from hero bag
  * drop Item
      > remove item from bag
  * change an Armor
      > Hero may change armor from the bag
  * change a Weapon
      > Hero may change weapon from the bag
  * Show quests (additional)
  * Choose quest (additional)

## Ability
Ability is a player or monster special action.  
To use the ability player or monster spends mana and actions points.  
To learn an ability Hero must be required level or higher.  
Monster doesn't have the ability more than his level.  
If ability upgrades it uprises a value.  
Ability may be used once per reload time.   
#### Ability has:
  * Name `: str`
  * Effect `: str`
  * Value `: int`
  * RequiredLevel `: int`
  * ReloadTime `: int` 

## Item
Item is a thing that helps the characters.  
The hero may have a limited set of items.  
When Hero gets the Item the first time he may dress it up, store it in the bag, or drop it.  
Item has required level for using or dressing it.  
It not may be upgraded.  
For more fun, you may set a random value in the given range.  
When it is used it drops automatically.  
#### Item has:
  * Name `: str`
  * Effect `: str`
  * Value `: int`
  * RequiredLevel `: int`

## Weapon
Hero and some monsters may use a weapon.  
The weapon has the required level for using or dressing it.  
The effect may be used to power Hero's attack. Choose by yourself how it will be implemented. Or you may skip it.  
It not may be upgraded.  
For more fun, you may set a random value in the given range.  
#### Weapon has:
  * Name `: str`
  * Value `: str`
  * Effect: `: str`
  * RequiredLevel `: int`

## Armor
Only Hero may use armor.  
The Armor has the required level for using or dressing it.  
The effect may be used to reduce damage if monster have a specific type. Choose by yourself how it will be implemented. Or you may skip it.  
It not may be upgraded.  
For more fun, you may set a random value in the given range.  
#### Armor has:
  * Name `: str`
  * Value `: str`
  * Effect: `:str`
  * RequiredLevel `: int`

# Enemy
<img src="https://user-images.githubusercontent.com/52273527/137013621-f99b58dd-6ac8-4212-8339-a413f0d6afca.png" width="100" />

It is a common description of the Enemy. In that way, the enemy may have different characteristics.  
The enemy may be founded by a hero anywhere in game world.   
Enemy creates based on Hero level +\- 4.  
To have more fun, some enemies may have limitations of level.  
The enemy gets a random weapon based on his level or doesn't have it  
Type and weakness may be used for additional damage.  
When Hero meets an Enemy he may explore all enemy characteristics if his level is equal to or higher than enemy level. If not, the hero may explore a name and level of the enemy.  
The hero may do three actions - explore, run or fight.  
If Hero defeats the enemy his collects loot. Loot gets random and may be empty.  
If Hero defeats the enemy his gains experience.   
If the Enemy defeats the Hero, Hero loses part of the earned experience on his level, and life decreases to 20%. Enemy removes from game.  

#### Enemy characteristics:
  * Name `: str`
  * Description `: str`
  * Level `: int`
  * Strength `: int`
  * Weakness `: str`
  * Type `: str`
  * Weapon `: Weapon`
  
#### Enemy actions:
  * attack
  * run (additional)


# Map
<img src="https://user-images.githubusercontent.com/52273527/137013644-3d7bdf73-d797-4361-b520-ef31b6ce9de2.png" width="100" />

It's a map of the game world or a local dungeon.    
Map manage hero's movements.
Hero may see all info from map   

#### Map characteristics:
  * Locations `: Location[]`
  * PlayerPosition  `: Location`

#### Map actions:
  * Move Player
  * Run Location
  * Show map

## Location
Specific place where the hero may find monsters, items, and other objects.     
The hero may visits explore, visit and leave a Location.  
If the hero explores a location - show a description of the Location.  
On hero, visit runs the Run Location script.  
Script May contain quests events, self events, battles, or even little games. If the hero successfully completes the location he gets a reward and experience.   
You must choose how events will be played. 
For more fun, some locations may contain random actions or may be infinite times completed.
Location may have self Map.   
The location contains neighbors which may be visited from it.  

#### Location characterictics:
  * Name `: str`
  * Description: `: str`
  * selfMap `: Map || str`
  * neighbours `: Location[]`
  * selfEvents: `: Event[]`
  * questEvents: `: Event[]`
  * isCompleted `: bool`

#### Location actions:
  * Run Location
  * Go to Neighbour
  * Give a reward


# Quest
<img src="https://user-images.githubusercontent.com/52273527/137013674-a3f2c418-3937-4337-9aad-043a0f9332dc.png" width="100" />

Quest it's a story that is separated by specific events.  
The hero may find a quest in the Locat ion or get it after level up.   
The hero may refuse to take a quest.   
The quest started when the hero take it.  
Quest plays on Event to an Event, when events are over, quest finish and hero take a reward.   

#### Quest characterictics:
  * Name `: str`
  * Description `: str`
  * Events: `: Event[]`
  * CurrentEvent `: Event`
  * Reward: `: Item[] || Ability`

#### Quest actions:
  * Add Event
  * Remove Event
  * Give a reward
  * Show current task

## Event
It's a point where user may know a story and interact with it.   
You may give some rewards to the hero, if you want, when he's completed event.   

#### Event characterictics:
  * Goal: `: str`
  * Place: `: Location.name`

#### Event actions:
  * Set Event
  * Remove Event


# Technical Requirements
<img src="https://user-images.githubusercontent.com/52273527/137013808-50c6cef1-2d5a-4ee3-98c8-417393ced76b.png" width="100"/>

  * [ ] All project must be done in a separate repo   
  * [ ] There is must be the main branch with current working version and additional branches from main with implemented program part     
    For example, branch Hero contains all logic for the hero and may be merged with main when it will work. After merge new branch comes from the main.
  * To merge to the main use Pull Request that contains:
    * What you do
    * Duration for this task
    * Date of completed
  * [ ] All items, abilities, quests, and other game data must be placed in separate files (py, txt, or json)
  * [ ] Player's progress save in separate file
  * [ ] Player may continue, load, or create a new game.
  * [ ] Player's save must be named by the player when the game is creating.
  * [ ] All components of game like Hero, Enemies, Items, and etc. must be placed in separate files.
  * [ ] Create a README.md and place it in root of your repo. It must contains:
    * Game name
    * Game description
    * Main actions 
    * Stucture of files, and how other developer may add new game data

# Additional info
  * [JSON for Python](https://realpython.com/python-json/)
  * [Linked List and Graph](https://realpython.com/linked-lists-python/)
  * [Markdown for .md](https://www.markdownguide.org/basic-syntax/) 
