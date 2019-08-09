"""This file describes the heroic adventurer Faenn "Squid" Sternbaum.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.4"

name = "Faenn 'Squid' Sternbaum"
player_name = "Phil"

# Be sure to list Primary class first
classes = ['Warlock']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [7]  # ex: [10] or [3, 2]
subclasses = ["Hexblade Patron"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Mercenary Veteran"
race = "Half-Elf"
alignment = "Chaotic neutral"

xp = 23000
hp_max = 67
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 12
dexterity = 14
constitution = 16
intelligence = 10
wisdom = 12
charisma = 20

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('insight', 'intimidation', 'investigation', 'perception', 'survival', 'athletics', 'persuasion')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ('Improved Pact Weapon', 'Thirsting Blade', 'Tricksters Escape', 'Eldritch Smite',)

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ('pact of the blade',)

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Elvish, Dwarven"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ["Sword of Sharpness", "Dagger", "Shortsword"]  # Example: ('shortsword', 'longsword')
magic_items = ('Scutum of the Seventh Legion','Sword of sharpness',)  # Example: ('ring of protection',)
armor = "Half Plate"  # Eg "leather armor"
shield = "Shield"  # Eg "shield"

equipment = """Dungeoneers Pack(Backpack, Crowbar, Hammer, 10 Torches, tinderbox, 10 rations, Waterskin, 10 Kletterhacken, 50ft. hemp Rope)
               Decke/Schlafrolle, Component Pouch,Uniform (travelers quality, Rot/Dunkel Blau), Fine Clothing (grün/schwarz), 2 Hemden trav. qual., 
               Spalleder Stiefel, Waffenöl, Strohhut, Winterkleidung, schwarzer Mantel
"""

attacks_and_spellcasting = """HexBlade ist Spellcasting Focus"""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ()  # Todo: Learn some spells

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ()  # Ex: ('ape', 'wolf', 'ankylosaurus')

# Backstory
# Describe your backstory here
personality_traits = """Superstitios. I'm haunted by the memories of war. I can't get the images of violence out of my mind."""

ideals = """Order is well, but when people ollow orders blindly, they embrace a kind of tyrany"""

bonds = """Those who fight besides me are those worth dying for"""

flaws = """Confined spaces remind me of the battlefield fray and leave me quivering with fear"""

features_and_traits = """Hello there."""
