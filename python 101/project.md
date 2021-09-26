# Text RPG Project
We want to create an RPG game. This game is about a strong hero that traveling around the world and fights against monsters.  
All the game processes are divided into two parts - hero action and world action.   
There is common information about the expected program. You are free for implementation and additional functions.  
All that we needs:
  * A Hero
  * An Enemies
  * A Map 
  * A Quests
  * A Treasures


# Hero
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
It not may be upgraded.  
For more fun, you may set a random value in the given range.  
#### Weapon has:
  * Name `: str`
  * Value `: str`
  * RequiredLevel `: int`

## Armor
Only Hero may use armor.  
The Armor has the required level for using or dressing it.  
It not may be upgraded.  
For more fun, you may set a random value in the given range.  
#### Armor has:
  * Name `: str`
  * Value `: str`
  * RequiredLevel `: int`
