from samba.dcerpc.security import security

from IMPULSE.components.ai import BaseAI


from IMPULSE.components.hacker import Hacker
from IMPULSE.components.equipment import Equipment
from IMPULSE.components.cyberware import Cyberware
from IMPULSE.components.ai import Idle, MeleeEnemy,RangedEnemy,Angel, charger, chaser
from IMPULSE.components.fighter import Fighter
from IMPULSE.components import consumable, equippable, bodymod, description
from IMPULSE.components.inventory import  Inventory
from IMPULSE.components.level import Level
from IMPULSE.components.status import Status
from IMPULSE.entity import Actor, Item, Station
from IMPULSE.components.controller import Controller
from IMPULSE import virus
from IMPULSE.damage_types import DamageType
from IMPULSE.components import consumable


player = Actor(char="@",
               color = (255,255,255),
               name= "Player",
               ai_cls=BaseAI,
               fighter=Fighter(hp=15, fp=8,base_defense=2, base_power=1,base_speed=5,base_focus=1,base_accuracy=0,base_reflex=1,),
               inventory=Inventory(capacity=12),
               level=Level(level_up_base=200),
               equipment=Equipment(),
               cyberware=Cyberware(),
               hacker = Hacker(virus.std_viruses),
               status=Status(),
               controller=Controller()

               )
doll = Actor(char="d",
               color = (69,200,255),
               name= "doll",
               ai_cls=Idle,
               fighter=Fighter(hp=30, base_defense=1, base_power=5,base_speed=5,base_focus=1,base_accuracy=0),
               inventory=Inventory(capacity=0),
               level=Level(level_up_base=200),

               cyberware=Cyberware(),
               status=Status(),
                desc=description.doll()
               )


angel= Actor(char="A",
               color = (255,255,255),
               name= "ANGEL",
               ai_cls=Angel,
              equipment=Equipment(),
               fighter=Fighter(hp=40, base_defense=2, base_power=7,base_speed=8,base_focus=20,base_accuracy=0),
               inventory=Inventory(capacity=4),
               level=Level(xp_given=1000),
                cyberware=Cyberware(),
                status=Status(),
                desc=description.angel()
               )

corpo_drone= Actor(char="C",
               color = (127,0,127),
               name= "Corpo Drone",
               ai_cls=MeleeEnemy,
               fighter=Fighter(hp=16, base_defense=1, base_power=4,base_speed=2,base_focus=0,base_accuracy=0),
               inventory=Inventory(capacity=0),
               level=Level(xp_given=250),
                cyberware=Cyberware(),
                status=Status(),
                desc=description.corpo_drone()

               )
corpo_sentry = Actor(char="C",
                    color=(127, 0, 127),
                    name="Corpo Drone",
                    ai_cls=MeleeEnemy,
                    fighter=Fighter(hp=16, base_defense=1, base_power=4, base_speed=2, base_focus=0, base_accuracy=0,base_range=4),
                    inventory=Inventory(capacity=0),
                    level=Level(xp_given=250),
                    cyberware=Cyberware(),
                    status=Status(),
                    desc=description.corpo_sentry()

                    )

big_goop = Actor(char="S",
               color = (10,255,10),
                name="Slime",
                 ai_cls=MeleeEnemy,
                 fighter=Fighter(hp=20, base_defense=2, base_power=6, base_speed=2, base_focus=0, base_accuracy=0, base_shock_resist=20),
                 inventory=Inventory(capacity=0),
                 level=Level(xp_given=10),
                 status=Status(),
                 desc=description.big_goop())
small_goop = Actor(char="s",
               color = (10,255,10),
                   name="Slime",
                   ai_cls=MeleeEnemy,
                   fighter=Fighter(hp=10, base_defense=2, base_power=6, base_speed=2, base_focus=0, base_accuracy=0, base_shock_resist=20),
                   inventory=Inventory(capacity=0),
                   level=Level(xp_given=100),
                   status=Status(),
                   desc=description.goop())

combat_doll =  Actor(char="d",
                     color=(255,10,10),
                     name="Combat Doll",
                     ai_cls=MeleeEnemy,
                     fighter=Fighter(hp=30, base_defense=1, base_power=8, base_speed=7, base_focus=8, base_accuracy=0,base_dodge=5),
                    inventory=Inventory(capacity=0),
                     level=Level(xp_given=500),
                     status=Status(),
                     desc=description.combat_doll())

latex_drone =Actor(char="D",
                   color=(100,0,150),
                   name="Hypno Drone",
                   ai_cls=MeleeEnemy,
                   fighter=Fighter(hp=20, base_defense=1, base_power=6, base_speed=6, base_focus=0, base_accuracy=0, base_dodge=2, base_shock_resist=30),
                   inventory=Inventory(capacity=0),
                   level=Level(xp_given=200),
                   status=Status(),
                   desc=description.hypno_drone())

latex_sentry =Actor(char="S",
    color = (100, 0, 150),
    name = "Latex Sentry",
    ai_cls = RangedEnemy,
    fighter = Fighter(hp=20, base_defense=0, base_attack=6, base_speed=5, base_focus=0, base_accuracy=2,base_range=4, base_shock_resist=30),
    inventory = Inventory(capacity=0),
    level = Level(xp_given=200),
    status = Status(),
desc=description.latex_sentry()
             )

exterminator = Actor(char="E",
                     color=(200,0,0),
                     name="Exterminator",
                     ai_cls=RangedEnemy,
                     fighter=Fighter(hp=20,base_defense=2,base_attack=6, base_speed=5, base_focus=4,base_accuracy=3,base_range=2, base_burn_resist=90),
                     damage_type=DamageType.FIRE,
                     inventory=Inventory(capacity=0),
                     level=Level(xp_given=400),
                     status=Status(),
                     cyberware=Cyberware(),
                         desc=description.exterminator())

security_bot = Actor(char="B",
                     color=(200,200,0),
                     name="Security Bot",
                     ai_cls=RangedEnemy ,
                fighter=Fighter(hp=25,base_defense=4,base_attack=6, base_speed=5, base_focus=4,base_accuracy=3,base_range=5,),
                     damage_type=DamageType.SHOCK,
                     inventory=Inventory(capacity=0),
                     level=Level(xp_given=400),
                     status=Status(),
                     cyberware=Cyberware(),
                        desc=description.security_bot())

security_enforcer = Actor(char="B",
                     color=(250,200,0),
                     name="Security Enforcer",
                     ai_cls=MeleeEnemy ,
                fighter=Fighter(hp=25,base_defense=6,base_attack=10, base_speed=5, base_focus=4,base_accuracy=3,base_shock_resist=20,base_burn_resist=20,),
                     damage_type=DamageType.SHOCK,
                     inventory=Inventory(capacity=0),
                     level=Level(xp_given=400),
                     status=Status(),
                        cyberware=Cyberware(),
                        desc=description.security_enforcer())
charger = Actor(char="F",
                color=(204, 85, 0),
                name="Evil Forklift",
                ai_cls=charger,
                fighter = Fighter(hp=10, base_defense=6, base_attack=10,  base_speed=3, base_focus=3, base_accuracy=10, base_burn_resist=20, base_range=6 ),
                damage_type = DamageType.SHOCK,
                inventory = Inventory(capacity=0),
                level = Level(xp_given=400),
                status = Status(),
                cyberware=Cyberware(),
                desc = description.charger())


#suicider = Actor(char="S",
               #  color=(100,80,200),
             #    ai_cls=charger,
           # #     fighter=Fighter(hp=10, base_defense=1, base_power=1, base_speed=7, base_focus=1, base_accuracy=0,),
           #      inventory=Inventory(capacity=0),
            #     level=Level(xp_given=200),
            #     status=Status(),
            #     )

chaser = Actor(char="c",
               name="Chaser",
               color=(205,204,1),
               ai_cls=chaser,
               fighter=Fighter(hp=10, base_defense=1, base_power=1, base_speed=5, base_focus=0,base_range=7),
               inventory=Inventory(capacity=0),
               level=Level(xp_given=100),
               status=Status(),
               desc=description.chaser())



health_potion = Item(
    char="!",
    color=(127,127,0),
    name="Bandage",
    consumable=consumable.HealingConsumable(amount=4),
    desc=description.bandage()
)
fp_potion = Item(
    char="!",
    color=(0,255,255),
    name="Glomp-Star Energy",
    consumable=consumable.FocusConsumable(amount=4),
    desc=description.energy_drink()
)


pistol_ammo = Item(
    char=":",
    color=(0,0,255),
    name="9mm Rounds",
    consumable=consumable.Ammo(rounds=12, gun_type="Pistol"),
    desc=description.pistol_ammo()
)
rifle_ammo = Item(
    char=":",
    color=(0,10,200),
    name="5.57 Rounds",
    consumable=consumable.Ammo(rounds=24, gun_type="Assualt Rifle"),
    desc=description.assault_ammo()
)
chaingun_ammo = Item(
    char=":",
    color=(0,20,150),
    name="20mm Rounds",
    consumable=consumable.Ammo(rounds=50, gun_type="Chain Gun"),
    desc=description.chain_ammo()
)


estrogen= Item(
char="~",
    color=(255,200,200),
    name="Estrogen",
    consumable=consumable.EstrogenConsumable(duration=100),
    desc=description.estrogen()
)



weed = Item(
char="~",
    color=(10,255,10),
    name="Weed",
    consumable=consumable.WeedConsumable(),
    desc=description.weed()

)

progesterone= Item(
char="~",
    color=(255,10,255),
    name="Progesterone",
    consumable=consumable.ProgesteroneConsumable(duration=100),
    desc=description.prog()



)
poppers = Item(
char="~",
    color=(255,10,10),
    name="Poppers",
    consumable=consumable.PoppersConsumable(duration=100, amount=10),
    desc=description.poppers()


)

amphetamines= Item(
char="~",
    color=(100,100,100),
    name="Amphetamine Salts",
    consumable=consumable.AmphetameineConsumable(duration=100, amount=10),
    desc=description.amphetamines()


)
hypnofile = Item(
char="~",
    color=(200,200,10),
    name="Hypno File",
    consumable=consumable.hypnofileConsumable(duration=100,),
    desc=description.hypnofile()

)
personal_shield=Item(
char="~",
    color=(0,0,200),
    name="Personal Shield",
    consumable=consumable.pocket_shieldConsumable(duration=100,amount=10),
    desc=description.pocket_shield()

)
flare=Item(
char="~",
    color=(200,55,0),
    name="Flare",
    consumable=consumable.flareConsumable(damage=10),
    desc=description.flare()
)
lithium_battery = Item(
    char="~",
    color=(100, 100, 0),
    name="Adrenal Stimulant",
    consumable=consumable.ArcDamageConsumable(damage=6,maximum_range=5),
    desc=description.battery()
)
adrenaline = Item(
    char="~",
    color=(100, 100, 0),
    name="Adrenal Stimulant",
    consumable=consumable.AdrenalineComsumable(duration=100),
    desc=description.adrenaline())

ketamine_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Ketamine Dart",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
    desc=description.ketamine()
)
fire_grenade= Item(
    char="~",
    color=(255, 0, 0),
    name="Molotov Cocktail",
    consumable=consumable.FireExplosionConsumable(damage=12, radius=3),
    desc=description.fire_grenade()
)
frag_grenade= Item(
    char="~",
    color=(255, 255, 0),
    name="Grenade",
    consumable=consumable.FragConsumable(damage=15, radius=3),
    desc=description.frag_grenade()
)


cool_knife=Item(
    char="/", color=(0,191,255), name="Cool Knife", equippable=equippable.cool_knife(), desc=description.knife()
)
shock_claws=Item(
    char="/", color=(0,100,255),name="Shock Claws", equippable=equippable.shock_claws(),desc=description.ShockClaw()
)
misericorde=Item(
    char="/", color=(0,90,255),name="Misericorde", equippable=equippable.misericorde(),desc=description.misiericorde())
labrys=Item(
    char="/", color=(128,0,128), name="Labrys", equippable= equippable.labrys(),desc=description.labrys()
)
rapier=Item(
    char="/", color=(0,191,255), name="Rapier", equippable=equippable.rapier()
)

pistol=Item(
    char="/", color=(255,0,255), name="Pistol", equippable=equippable.pistol(),desc=description.pistol()
)

assaultRifle=Item(
    char="/", color=(255,0,200), name="Assault Rifle", equippable=equippable.assualtRifle(),desc=description.assault()
)
flameThrower=Item(
    char="/", color=(255,20,20), name="Flame Thrower", equippable=equippable.assualtRifle(), desc=description.assault()
)
angelGun=Item(
    char="/", color=(255,255,255),name="HOLY LIGHT", equippable=equippable.angelGun(),desc=description.angelGun()
)

angelSword=Item(
    char="/", color=(255,255,255),name="DIVINE WRATH    ", equippable=equippable.angelSword(),desc=description.angelSword()
)

chainGun=Item(
    char="/", color=(200,200,200),name="Chain Gun", equippable=equippable.chainGun(),desc=description.ChainGun()
)
latexBodySuit=Item(
    char="[", color=(10,10,10), name="Latex BodySuit", equippable=equippable.latex_bodysuit(),desc=description.bodysuit()
)
leather_jacket=Item(
    char="[", color=(139,69,19), name="Leather Jacket", equippable=equippable.leather_jacket(),desc=description.leather_jacket()

)
jumpsuit=Item(
    char="[",color=(10,10,200), name="Jumpsuit", equippable=equippable.jumpsuit()
)
dress=Item(
    char="[", color=(50,50,50), name="Dress", equippable=equippable.dress()
)

hazard_suit = Item(
    char="[", color=(169,69,69), name="Hazard Suit", equippable= equippable.hazard_suit()
)
#body_armor=Item(
   # char="[", color=(5,5,10), name="Body Armor", equippable=equippable.body_armor(),desc=description.body_armor()
#)
hack_upgrade = Item(
    char="i", color=(255,0,255), name="Hacking Upgrade", bodymod= bodymod.hack_upgrade(),desc=description.hack_upgrade()
)

los_upgrade = Item(
    char="i", color=(200,0,255), name="Long Range Sensors", bodymod= bodymod.los_upgrade(),desc=description.los_upgrade()
)
accuracy_upgrade=Item(
    char="i", color=(150,0,255), name="Integrated Fire Control", bodymod= bodymod.accuracy_upgrade(),desc=description.accuracy_upgrade()
)

control_upgrade=Item(
    char="i",color=(100,0,255), name="Inegrated Fire Control", bodymod= bodymod.control_upgrade(),desc=description.control_upgrade()
)


weapon_slot = Item(
    char="i", color=(255,0,255), name="Hvy Wpn Pltfrm", bodymod= bodymod.weapon_slot(),desc=description.weapon_slot()
)
sheilding = Item(
    char="i", color=(255,0,100), name="Shielding Upgrade", bodymod= bodymod.sheilding(),desc=description.sheilding()
)

electric_sheilding=Item(
    char="i", color=(50,0,255), name="Faraday Suite", bodymod= bodymod.electric_sheilding(),desc=description.electric_sheilding()
)
fire_shielding=Item(
    char="i", color=(0,50,255), name="Rapid Cooling Trunk", bodymod= bodymod.fire_sheilding(),desc=description.fire_sheilding()
)
boobs=Item(
    char="i", color=(50,50,255), name="Breast Forms", bodymod=bodymod.boobs(), desc=description.boobs()
)

reflex_upgrade=Item(
    char="i", color=(100,50,255), name="Rapid Response Servos", bodymod=bodymod.reflex_upgrade(), desc=description.reflex_upgrade()
)


bionic_arm=Item(
    char="i", color=(150,50,255), name="High Tensile Tendons", bodymod=bodymod.bionic_arm(), desc=description.bionic_arm()

)

rocket_fist=Item(
    char="i", color=(200,50,255), name="R.P.F", bodymod=bodymod.rocket_fist(), desc=description.rocket_fist()
)

power_legs=Item(
    char="i", color=(255,50,255), name="Stability Modules", bodymod=bodymod.power_legs(), desc=description.power_legs()
)

carrymod=Item(
    char="i", color=(255,100,255), name=" Carbon Nano-Bones",bodymod=bodymod.carry(), desc=description.carrymod()
)


super_legs = Item(
    char= "i", color=(255,30,100), name="Leg Upgrade", bodymod=bodymod.super_legs(), desc= description.super_legs()
)


MedBay = Station(
    char="X", color=(1,1,1), name="MedBay")