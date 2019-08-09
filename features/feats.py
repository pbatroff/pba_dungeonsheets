from .features import Feature


# PHB
class GreatWeaponMaster(Feature):
    """You’ve learned to put the weight of a weapon to your advantage, letting its
    momentum empower your strikes. You gain the following benefits:

    -- On your turn, when you score a critical hit with a melee weapon or
    reduce a creature to 0 hit points with one, you can make one melee weapon
    attack as a bonus action.

    -- Before you make a melee attack with a heavy weapon that you are
    proficient with, you can choose to take a -5 penalty to the attack
    roll. If the attack hits, you add +10 to the attack’s damage

    """
    name = "Great Weapon Master"
    source = "Feats"


class Actor(Feature):
    """Skilled at mimicry and dramatics, you gain the following benefits:

    -- Increase your Charisma score by 1, to a maximum of 20.

    -- You have an advantage on Charisma (Deception) and Charisma (Performance) checks when trying to pass yourself off as a different person.

    --You can mimic the speech of another person or the sounds made by other
    creatures. You must have heard the person speaking, or heard the creature
    make the sound, for at least 1 minute. A successful Wisdom (Insight) check
    contested by your Charisma (Deception) check allows a listener to determine
    that the effect is faked.

    """
    name = "Actor"
    source = "Feats"

class Luck(Feature):
    """You have inexplicable luck that seems to kick in at just
        the right moment.

        You have 3 luck points. Whenever you make an attack
        roll, an ability check, or a saving throw, you can spend
        one luck point to roll an additional d20. You can choose
        to spend one of your luck points after you roll the die,
        but before the outcome is determined. You choose which
        of the d20s is used for the attack roll, ability check, or
        saving throw.
        You can also spend one luck point when an attack
        roll is made against you. Roll a d20, and then choose
        whether the attack uses the attacker's roll or yours.
        If more than one creature spends a luck point to
        influence the outcome of a roll, the points cancel each
        other out; no additional dice are rolled.
        You regain your expended luck points when you
        finish a long rest.
    """
    name = "Luck"
    source = "Feats"


class InspiringLeader(Feature):
    """You can spend 10 minutes inspiring your companions,
        shoring up their resolve to fight. When you do so, choose
        up to six friendly creatures (which can include yourself)
        within 30 feet of you who can see or hear you and who
        can understand you. Each creature can gain temporary
        hit points equal to your level + your Charisma modifier.
        A creature can't gain temporary hit points from this feat
        again until it has finished a short or long rest.
    """
    name = "Inspiring Leader"
    source = "Feats"