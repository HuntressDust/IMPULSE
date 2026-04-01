from __future__ import annotations

import copy
import lzma
import pickle
import traceback
from typing import Optional

import tcod
from IMPULSE import color


from IMPULSE.engine import Engine
from IMPULSE.game_map import GameWorld
from IMPULSE import entity_factories
from IMPULSE import input_handler
from IMPULSE.input_handler import BaseEventHandler, HelpScreen

background_image = tcod.image.load("GRAPHICS/menu_background.png")[:, :, :3]

def new_game(playername: str="player") -> Engine:
    map_width = 80
    map_height=43
    room_max_size = 10
    room_min_size=6
    max_rooms=30
    name=playername
    player = copy.deepcopy(entity_factories.player)
    player.name=name
    if name == "sweethound":
        player.fighter.base_power=20
        player.fighter.base_reflex=20
        player.fighter.base_focus=20
        player.fighter.full_heal()

    if name == "poncho":
     player.fighter.base_speed=9
     player.fighter.base_focus=10
     player.fighter.hp=100
     player.fighter.fp=100

    engine = Engine(player=player)
    print(engine.player.name)
    engine.game_world = GameWorld(
        engine=engine,
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        viewport_width=30,
        viewport_height=30,

    )

    engine.game_world.generate_floor(0)
    engine.update_fov()

    engine.message_log.add_message(
        "WELCOME TO YOUR DOOM", color.welcome_text
    )
    if name == "PEERLESS":
        gun = copy.deepcopy(entity_factories.angelGun)
        gun.parent = player.inventory

        sword = copy.deepcopy(entity_factories.angelSword)
        sword.parent = player.inventory
        player.inventory.items.append(gun)
        player.equipment.toggle_equip(gun, add_message=False)

        player.inventory.items.append(sword)
        player.equipment.toggle_equip(sword, add_message=False)

    else:
        pistol = copy.deepcopy(entity_factories.pistol)
        pistol.parent = player.inventory
        player.inventory.items.append(pistol)
        player.equipment.toggle_equip(pistol,add_message=False)

        knife = copy.deepcopy(entity_factories.cool_knife)
        knife.parent = player.inventory
        player.inventory.items.append(knife)



    bandage = copy.deepcopy(entity_factories.health_potion)
    bandage.parent = player.inventory
    player.inventory.items.append(bandage)

    return engine

def load_game(filename:str) -> Engine:
    with open(filename, "rb")as f:
        engine = pickle.loads(lzma.decompress(f.read()))
    assert isinstance(engine, Engine)
    return engine

class SplashScreen(BaseEventHandler):
    def __init__(self):
        super().__init__()
        self.line_num=0
        self.char_pos=0
        self.TITLE = "The year is 2XXX"
        self.LINE1 = "For decades the forces of humanity were tuned to a singular goal:"
        self.LINE2 = "      Profit."
        self.LINE3 = "To this end, great labyrinths "
        self.LINE35=  "     of twisting plastic and dull concrete were constructed"
        self.LINE4 = "Reaching miles into the sky above, and plunging into great crevices below"
        self.LINE5 = "And in their beating hearts, the loyal dogs of capital "
        self.LINE55=  "     were rewarded with wonderous tech;"
        self.LINE6 = "those who sold their soul were paid "
        self.LINE65=             "     in bodies that transcend the crude dispensation of nature."
        self.LINE7 = "Time passed, crisis after crisis led to mass exodus from our plastic prisons."
        self.LINE8 = "But, the technology remains."
        self.LINE9 = "You were born outside, in the wastes surrounding the ruins of Neo-Akron."
        self.LINE10 = "And as far as humanity has advanced, we have yet to cast off"
        self.LINE105= "     our limited conceptions of sex and gender."
        self.LINE11 = "So, in a cruel twist of fate, they assigned you 'male'."
        self.LINE12 = "Though you receive support from your friends, there is an ache from within."
        self.LINE13 = "And there, in the old ruins of Neo-Akron, lies a solution."
        self.LINE14 = "The last functioning Auto-Surgeon in the MegaCleveland Metro-Zone."
        self.LINE15 = "Fully functional, no WPATH, no bureaucracy, no copay."
        self.LINE16 = "It is time to make your body your ownn."
        self.wait_timer=0
        self.OPENING_CRAWL=[self.LINE1,self.LINE2,self.LINE3,self.LINE35,self.LINE4,self.LINE5,self.LINE55,self.LINE6,self.LINE65,self.LINE7,self.LINE8,
                            self.LINE9,self.LINE10,self.LINE105,self.LINE11,self.LINE12,self.LINE13,self.LINE14,self.LINE15,]
    def update_text(self):
        current_Line=self.OPENING_CRAWL[self.line_num]
        lineLength=len(current_Line)
        if self.char_pos+1 == lineLength:
            self.char_pos=0
            self.line_num+=1
        else:
            self.char_pos+=1




    def on_render(self, console: tcod.Console) -> None:
        console.print(
            console.width // 2,
            1,
            self.TITLE,
            fg=color.menu_title,
            alignment = tcod.CENTER,
        )

        linenum=1
        for line in self.OPENING_CRAWL:
            linenum+=2
            console.print(
                0,
                linenum,
                line
         )
        console.print(
            console.width // 2,linenum+2,self.LINE16,fg=color.menu_title,alignment = tcod.CENTER)


    def ev_keydown(self, event: tcod.event.KeyDown, ) -> Optional[input_handler.BaseEventHandler]:
        if event.sym:
            return  MainMenu()
        return None





class MainMenu(BaseEventHandler):
    def on_render(self, console: tcod.Console) -> None:
        console.draw_semigraphics(background_image,0,0)

        console.print(
            console.width // 2,
            console.height // 2 - 4,
            "PROJECT IMPULSE",
            fg=color.menu_title,
            alignment = tcod.CENTER,
        )

        menu_width = 24
        for i, text in enumerate(
            ["[N] New Game", "[C] Continue", "[H] Help","[Q] Quit"]
        ):
            console.print(
                console.width // 2,
                console.height // 2 - 2 + i,
                text.ljust(menu_width),
                fg=color.menu_text,
                bg=color.black,
                alignment=tcod.CENTER,
                bg_blend=tcod.BKGND_ALPHA(64),
            )

        console.print_box(
            0, console.height-8,console.width,1,
            "A game by Nova Zero. ",
                fg=color.menu_text,
                bg=color.black,
                alignment=tcod.RIGHT,
                bg_blend=tcod.BKGND_ALPHA(64),
        )
        console.print_box(
            0, console.height - 7, console.width,1,
            "Email her with bug reports at HuntressDust@proton.me",
                fg=color.menu_text,
                bg=color.black,
                alignment=tcod.RIGHT,
                bg_blend=tcod.BKGND_ALPHA(64),

            )

        console.print_box(
            0, console.height-5,console.width,1,
            "Much thanks to rogueliketutorials.com, r/roguelikedev,",
                fg=color.menu_text,
                bg=color.black,
                alignment=tcod.RIGHT,
                bg_blend=tcod.BKGND_ALPHA(64),
        )

        console.print_box(
            0, console.height - 4,console.width,1,
            "and my girlfriend :3",
                fg=color.menu_text,
                bg=color.black,
                alignment=tcod.RIGHT,
                bg_blend=tcod.BKGND_ALPHA(64),
        )


        console.print_box(
            0, console.height-2,console.width,1,
            "Version 0.9, compiled 31-03-2026",
                fg=color.menu_text,
                bg=color.black,
                alignment=tcod.RIGHT,
                bg_blend=tcod.BKGND_ALPHA(64),
        )




    def ev_keydown(self, event: tcod.event.KeyDown, ) -> Optional[input_handler.BaseEventHandler]:
        if event.sym in (tcod.event.KeySym.Q, tcod.event.KeySym.ESCAPE):
            raise SystemExit()
        elif event.sym == tcod.event.KeySym.C:
            try:
                return input_handler.MainGameEventHandler(load_game("savegame.sav"))
            except FileNotFoundError:
                return input_handler.PopupMessage(self, "No saved game to load.")
            except Exception as exc:
                traceback.print_exc()  # Print to stderr.
                return input_handler.PopupMessage(self, f"Failed to load save:\n{exc}")
        elif event.sym == tcod.event.KeySym.N:
            return  name_entry()
        elif event.sym == tcod.event.KeySym.H:
            return HelpScreen(MainMenu())
        return None

class End_Screen(input_handler.BaseEventHandler):
    def on_render(self, console: tcod.Console) -> None:

        console.print(
            console.width // 2,
            console.height // 2 - 4,
            "YOU DID IT",
            fg=color.menu_title,
            alignment = tcod.CENTER,
        )

        console.print(
            console.width // 2,
            console.height // 2 - 8,
            "You've finally reached the Auto-Surgeon and got a vaginoplasty",
            fg=color.menu_title,
            alignment=tcod.CENTER,
        )

        menu_width = 24
        for i, text in enumerate(
            ["[N] New Game",  "[Q] Quit"]
        ):
            console.print(
                console.width // 2,
                console.height // 2 - 2 + i,
                text.ljust(menu_width),
                fg=color.menu_text,
                bg=color.black,
                alignment=tcod.CENTER,
                bg_blend=tcod.BKGND_ALPHA(64),

            )
    def ev_keydown(self, event: tcod.event.KeyDown, ) -> Optional[input_handler.BaseEventHandler]:
        if event.sym in (tcod.event.KeySym.Q, tcod.event.KeySym.ESCAPE):
            raise SystemExit()
        elif event.sym == tcod.event.KeySym.N:
            return name_entry()

        return None

class name_entry(input_handler.BaseEventHandler):
    def __init__(self):
        super().__init__()
        self.name: str=""

    def on_render(self, console: tcod.Console) -> None:

        console.print(
            console.width // 2,
            console.height // 2 - 8,
            "Enter Your Name, Miss",
            fg=color.menu_title,
            alignment=tcod.CENTER,
        )


        console.draw_frame(
            console.width // 2 -7,
            console.height // 2 - 4,
            width=13,
            height=3,
            clear=False,
            fg=(255, 255, 255),
            bg=(0, 0, 0)
        )
        console.print(
            console.width // 2-6,
            console.height // 2-3,
            self.name,
            fg=color.menu_title,
        )
    def ev_keydown(self, event: tcod.event.KeyDown, ) -> Optional[input_handler.BaseEventHandler]:
        key = event.sym
        if key is (tcod.event.KeySym.ESCAPE):
            raise SystemExit()
        elif key in input_handler.CONFIRM_KEYS:
            if self.name != "" and self.name !=" " and self.name != "  " and self.name != "   " and self.name != "    " and self.name != "     ":
                if self.name == "      "  or self.name == "       " or self.name == "        " or self.name == "         " :
                    self.name= "cunt"
                return input_handler.MainGameEventHandler(new_game(self.name))
        elif key is tcod.event.KeySym.BACKSPACE:
            self.name=self.name[:len(self.name)-1]
        elif key is tcod.event.KeySym.SPACE:
            self.name = self.name + " "
        elif key in input_handler.TEXT_KEYS:
            if len(self.name)<11:
                mod=0
                if event.mod & (tcod.event.Modifier.LSHIFT | tcod.event.Modifier.RSHIFT):
                    mod=32
                char=input_handler.TEXT_KEYS[key]

                char=chr(ord(char) - mod)

                self.name=self.name+char


        return None