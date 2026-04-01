from __future__ import annotations

from IMPULSE.components import bodymod


class Description:
    def __init__(self, line1: str="", line2:str="", line3:str=""):
        self.line1=line1
        self.line2=line2
        self.line3=line3
        self.text_lines=list([line1,line2,line3])

default_description = Description("placeholder1",
                                  "placeholder2",
                                  "placeholder3")


# ______________________ACTORS________________________
class doll(Description):
    def __init__(self)->None:
        super().__init__(
        line1="A doll",
        line2="This is a test of the description system.",
        line3="It loves you very much."
    )
class sentry(Description):
    def __init__(self)->None:
        super().__init__(
        line1="A sentry",
        line2="This is a test of the description system.",
        line3="It hates you very much."
    )
class angel(Description):

    def __init__(self) -> None:
        super().__init__(
        line1="An ancient being that burns with ritcheous fury",
        line2="The mistake of prometheus shall not be repeated",
        line3="It fucking hates your pussy."
    )
class cybork(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="A cyber orc. She's been helping me test almost every system",
            line2="I love her so much.",
            line3="She hates you very much."
        )

class corpo_drone(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="A discarded tool from the search for surplus value",
            line2="Engineered to commune with large language models",
            line3="Will stop at nothing for a little treat")

class corpo_sentry(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="A discarded tool from the search for surplus value",
            line2="Engineered to commune with large language models",
            line3="This one has a gun")

class goop(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="An amorphous blob with a drive to kill",
            line2="Evolved from mint gum and discarded electronics ",
            line3="Might survive if cut in half")

class big_goop(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="An amorphous blob with a drive to kill",
            line2="Evolved from mint gum and discarded electronics ",
            line3="Might survive if cut in half")

class combat_doll(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="A robot girl that fiercely guards this facility",
            line2="A living weapon with a dead look in its eyes",
            line3="Its greatest pleasure is to cut targets to ribbons")

class hypno_drone(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="A latex-clad guardian whose only thought is security",
            line2="Hypnotically conditioned, it has no cyberware installed",
            line3="Far beyond anyone's help")

class latex_sentry(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="A latex-clad guardian with perfect aim",
            line2="Spiral spiral through the sights, onto the target",
            line3="Pull the trigger and feel at peace...")


class exterminator(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="A robotic pest exterminator",
            line2="Cyber-roaches proving too resilient, it cleanses with fire",
            line3="Shielded from being burned by its own flames")

class security_bot(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="The answer to all threats against property-rights",
            line2="Kills without discretion or mercy",
            line3="Shouts ads for sports-betting while shooting you")


class security_enforcer(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="The answer to all threats against property-rights",
            line2="Kills without discretion or mercy",
            line3="Shouts ads for some chatbot while chocking you")

class charger(Description):
    def __init__(self) -> None:
        super().__init__(
        line1="A rouge forklift that thinks you're a palette",
        line2="Will attempt to charge and stun you!",
        line3="Someone put googly-eyes on it some time ago")

class chaser(Description):
    def __init__(self) -> None:
        super().__init__(
        line1="Some asshole who really wants to fuck",
        line2="Hangs around the old auto-docs looking for the lonely and desperate",
        line3="Or maybe he followed you? Ugh..")


#_____________________Ammo___________________________

class pistol_ammo(Description):
    def __init__(self)->None:
        super().__init__(
            line1="9mm ammo for a pistol",
            line2="Use this to automatically reload a held pistol",
            line3="The game attempts to consolidate stacks of ammo",

        )


class assault_ammo(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="5.57 ammo for an assault rifle",
            line2="Use this to automatically reload a held assault rifle",
            line3="The game attempts to consolidate stacks of ammo",

        )
class chain_ammo(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="20mm ammo for a chain gun",
            line2="Use this to automatically reload a held chain gun",
            line3="The game attempts to consolidate stacks of ammo",

        )


#______________________Consumables________________________




class bandage(Description):
    def __init__(self) -> None:
        super().__init__(
        line1="A neo-gauze packet laced with hyper-sporin",
        line2="Eventually is subsumed into your tissues",
        line3="Restores 4 HP",
        )


class energy_drink(Description):
    def __init__(self) -> None:
        super().__init__(
        line1="An energy drink that tastes better than it should",
        line2="Refreshes you and gives a nice energy boost",
        line3="Restores 4 FP",)


class estrogen(Description):
    def __init__(self) -> None:
        super().__init__(
        line1="2 mg Estradiol Valerate",
        line2="Spring-loaded syringe that injects intramuscular",
        line3="Removes DYSPHORIA and adds EUPHORIA, +1 to POWER REFLEX AND FOCUS",)


class weed(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="A weed cigarette, or a bunt",
            line2="And yes, it is a weed bunt",
            line3="Clears negative status effects", )


class prog(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="100 mg Progesterone Capsule",
            line2="A pregnancy hormone. You need to boof it, by the way.",
            line3="+2 to POWER", )


class poppers(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="Inhalants that relax and numb you",
            line2="A blanket term given to many volatile nitrates.",
            line3="Adds a temporary 10 HP boost", )


class amphetamines(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="Stimulants commonly taken to help with focus",
            line2="Barriers to concentration are obliterated, psyche oned",
            line3="Adds a temporary 10 FP boost", )


class hypnofile(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="A one time use datacard that activates a hypnotic trigger",
            line2="Distractions fall away, spiral, spiral to victory",
            line3="+2 to FOCUS", )

class adrenaline(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="Combination Norepinephrine, Cortisol and Adrenaline",
            line2="Increases heart rate, reaction time, hand-eye coordination",
            line3="+2 to REFLEX")

class flare(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="An emergency phosphorus flare",
            line2="Burns bright, burns hot. ",
            line3="Melee attack an enemy for 10 BURN damage", )


class battery(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="An ancient Lithium-Ion Battery bulging dangerously",
            line2="the dialectric plates would very much like to come into contact",
            line3="Deals 10 SHOCK damage to nearest NPC", )

class frag_grenade(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="A standard fragmentation grenade",
            line2="Simple, Dangerous, Effective",
            line3="Deals 15 damage to all entities within 3 tiles")

class fire_grenade(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="A bomb made of refined petroleum and other fun solvents",
            line2="A popular choice for the revolutionary on a budget",
            line3="Deals 12 BURN damage to all entities within 3 tiles", )


class ketamine(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="A homing dart that injects ketamine intravenously",
            line2="Primarily used for insane lesbian sex",
            line3="Dissociates target for 10 turns", )

class pocket_shield(Description):
    def __init__(self) -> None:
        super().__init__(
            line1="A belt hoster that generates a personal shield",
            line2="Temportary but effective against all kinds of attacks",
            line3="+10 to DEFNESE", )


#_____________________Equipment__________________________
class pistol(Description):
    def __init__(self)->None:
        super().__init__(
        line1="A 9mm handgun. Can be wielded one handed. holds 12 9mm rounds, single-fire",
        line2="Small, reliable. Polished plexsteel body, nyla-max grip. Feels good to hold.",
        line3="Good all-around weapon."
    )

class assault(Description):
    def __init__(self)->None:
        super().__init__(
    line1="A milspec assault rifle, requires 2 hands. holds 24 5.57 rounds, fires in 3 round burts",
    line2="An older but powerful model, probably dropped by some corpo running-dog from the cobalt wars",
    line3="Solid weapon if you can use it.",
    )
class ChainGun(Description):
    def __init__(self)->None:
        super().__init__(
    line1="A hulking beast of a gun. Requiresd two hands, fires 6 rounds of 5.57 per action",
    line2="Designed to rip through crowds of unarmored targets. the noise is overwhelming",
    line3="Kicks like a cyber-mare. Designed to be used by super soldiers"
)
class angelGun(Description):
    def __init__(self)->None:
        super().__init__(
    line1="a gun used by the final boss",
    line2="probably too powerful",
    line3="you naughty cheater >:3"
)
class angelSword(Description):
    def __init__(self)->None:
        super().__init__(
    line1="a sword used by the final boss",
    line2="probably too powerful",
    line3="you naughty cheater >:3"
)
class leather_jacket(Description):
    def __init__(self)->None:
        super().__init__(
    line1="A sturdy Leather Jacket. Real leather, too.",
    line2="Designed of neo-cycle drivers, lots of pockets, and its warm too.",
    line3="Protects against cuts, scraps, and has some insulating properites. Plus you look hot in it"

)
class dress(Description):
    def __init__(self)->None:
        super().__init__(
    line1="A beautiful black dress",
    line2="High quality and elegant, it catches the air and blows all badass.",
    line3="Freedom of movement that pants simply do not allow."

)
class bodysuit(Description):
    def __init__(self)->None:
        super().__init__(
    line1="A latex bodysuit. Insulates you from electicity",
    line2="Impractical? Yes. Sexy? Very Yes.",
    line3="Doesnt Protect from imapact or heat, but it hugs your curves.",
)

class jumpsuit(Description):
    def __init__(self)->None:
        super().__init__(
    line1="A Hi-viz work uniform. Flame and cut resistant",
    line2="Blue with yellow reflective sripes, used by mechanics and therians alike.",
    line3="Decently protective and quite fasionable to the right crowd."
)
class knife(Description):
    def __init__(self)->None:
        super().__init__(
    line1='A big knife. can be wielded in one hand',
    line2="Razor sharp and deadly, from your own personal collection. Girls find it very hot",
    line3="Good for sex and self defense, but not meant for prolonged combats"
)
class misiericorde(Description):
    def __init__(self)->None:
        super().__init__(
    line1="A long dagger like weapon meant to deliver a killing blow",
    line2="Used by security forces for getting around kevlar.",
    line3="Can be used in ine hand can attack twice"
)
class labrys(Description):
    def __init__(self)->None:
        super().__init__(
    line1= "A large two-headed axe. Used with two hands.",
    line2="The traditional weapon of the amazons and those from the Ilse of Lesbos",
    line3="huge and powerful. Probably left by an underground dyke group")
class ShockClaw(Description):
    def __init__(self)->None:
        super().__init__(
    line1="Electically charged gauntel tipped with razor sharp claws",
    line2='The claws rip though wire and break through insulating skin, allowing the electicity to be delivered to vulnerable areas',
    line3="Can be painted a varity of fun colors, and you dont have to worry about hangnails ",
)

#______________________CYBERWARE__________________
class hack_upgrade(Description):
    def __init__(self)->None:
        super().__init__(
    line1="A co-processor directly enhancing your mental faculties",
    line2="connects to your brainstem via a series of tubes",
    line3=f"Enhances FOCUS by 5 points",
)

class los_upgrade(Description):
    def __init__(self)->None:
        super().__init__(
    line1="sensors that consinuously sweep your surroundings",
    line2="feeds sonar data directy into your visual cortex",
    line3="Increases the distances at which tiles are revealed by 5 points",
)
class accuracy_upgrade(Description):
    def __init__(self)->None:
        super().__init__(
    line1="Fine-motor control stimulation that enhances your hand-eye coordination",
    line2="Standard issue for corpo sentry drones",
    line3=f"Enhances ranged accuracy by 5 points",
)
class control_upgrade(Description):
    def __init__(self)->None:
        super().__init__(
    line1="networking co processor that handles connection between conciouness",
    line2="Reduces the stress of puppetering immensly",
    line3=f"Allows you to puppet 2 additional beings",
)


class weapon_slot(Description):
    def __init__(self)->None:
        super().__init__(
    line1="Swivel mount for heavy weaponds attached to your side",
    line2="Remeber the butch from Aliens? Its that",
    line3=f"Unlocks an additional weapon slot"

)
class sheilding(Description):
    def __init__(self)->None:
        super().__init__(
    line1="PlexSteel plating embeded in your torso",
    line2="Protects againts all attacks",
    line3=f"Enhnaces HP by  points",
)

class electric_sheilding(Description):
    def __init__(self)->None:
        super().__init__(
    line1="A seriens of conductive pathways embeded between cyberware",
    line2="allows electicity to pass harmlessly to ground",
    line3=f"Enhances SHOCK RESISTANCE by 5 points",
)
class fire_sheilding(Description):
    def __init__(self)->None:
        super().__init__(
    line1="An integrated cooling system throughtout your bodd",
    line2="includings a heat sink near the spine and radiating wings",
    line3=f"Enhances FIRE RESISTANCE by 5 points",
)
class boobs(Description):
    def __init__(self)->None:
        super().__init__(
    line1="K-cup breasts",
    line2="theyre big and bouncy and awesome",
    line3="Grants a permanant state of GENDER EUPHORIA (+1 to POWER, REFLEX, and FOCUS)",
)

class reflex_upgrade(Description):
    def __init__(self)->None:
        super().__init__(
    line1="A network of semi-autonomous computers throughout your arms",
    line2="takes raw sensory data reacts without  waiting on the brain to process it",
    line3=f"Enhances REFLEX by  points",
)

class bionic_arm(Description):
    def __init__(self)->None:
        super().__init__(
    line1="A fully robotic arm",
    line2="made of plexsteel and fiber-optics. Top of the line stuff",
    line3=f"Enhances POWER by 5 points",

)

class rocket_fist(Description):
    def __init__(self)->None:
        super().__init__(
    line1="Rocket. Powered. Fist",
    line2="Not implemented yet.",
    line3="Allows you to make a powerful ranged attack while UNARMED",
)

class power_legs(Description):
    def __init__(self)->None:
        super().__init__(
    line1="Metal Talons that grip the ground with each step",
    line2="provides a solid base from which to strike",
    line3=f"Enhances POWER by ? points",
)
class carrymod(Description):
    def __init__(self)->None:
        super().__init__(
    line1="Enhanced tibia and femurs",
    line2="allows weight to be dstributed more evenly into the ground",
    line3=f"Allows you to carry 6 additional items",
)


class super_legs(Description):
    def __init__(self)->None:
        super().__init__(
    line1="Ultra-light bionic legs",
    line2="includes high-powered motors and rocket boosters",
    line3=f"Enhances SPEED by 2 points",
)

class itchy_legs(Description):
    def __init__(self)->None:
        super().__init__(
        line1 = "A network of semi-autonomous computers throughout your legs",
        line2 = "takes raw sensory data reacts without waiting on the brain to process it",
        line3 = f"Enhances REFLEX by ? points",
        )