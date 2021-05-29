from utils.spritesheet import SpriteSheet
import sys
from os import path
import pygame as pg

def load_character(path1, player_walkup, player_walkdown, player_walk_right, player_walk_left, 
        player_idleup, player_idledown, player_idle_right, player_idle_left):

    sprites_character_folder = path1

    spritesheet_walk_up = SpriteSheet(path.join(sprites_character_folder, 'upwalk.png'))
    spritesheet_walk_down = SpriteSheet(path.join(sprites_character_folder, 'downwalk.png'))
    spritesheet_walk_side = SpriteSheet(path.join(sprites_character_folder, 'sidewalk.png'))
    spritesheet_idle_down = SpriteSheet(path.join(sprites_character_folder, '_down idle.png'))
    spritesheet_idle_up = SpriteSheet(path.join(sprites_character_folder, '_up idle.png'))
    spritesheet_idle_side = SpriteSheet(path.join(sprites_character_folder, '_side idle.png'))

    player_walkup.append(spritesheet_walk_up.get_sprite(0, 0, 64, 64))
    player_walkup.append(spritesheet_walk_up.get_sprite(64, 0, 64, 64))
    player_walkup.append(spritesheet_walk_up.get_sprite(128, 0, 64, 64))
    player_walkup.append(spritesheet_walk_up.get_sprite(192, 0, 64, 64))
    player_walkup.append(spritesheet_walk_up.get_sprite(0, 64, 64, 64))
    player_walkup.append(spritesheet_walk_up.get_sprite(64, 64, 64, 64))

    player_walkdown.append(spritesheet_walk_down.get_sprite(0, 0, 64, 64))
    player_walkdown.append(spritesheet_walk_down.get_sprite(64, 0, 64, 64))
    player_walkdown.append(spritesheet_walk_down.get_sprite(128, 0, 64, 64))
    player_walkdown.append(spritesheet_walk_down.get_sprite(192, 0, 64, 64))
    player_walkdown.append(spritesheet_walk_down.get_sprite(0, 64, 64, 64))
    player_walkdown.append(spritesheet_walk_down.get_sprite(64, 64, 64, 64))

    player_walk_left.append(spritesheet_walk_side.get_sprite(0, 0, 64, 64))
    player_walk_left.append(spritesheet_walk_side.get_sprite(64, 0, 64, 64))
    player_walk_left.append(spritesheet_walk_side.get_sprite(128, 0, 64, 64))
    player_walk_left.append(spritesheet_walk_side.get_sprite(192, 0, 64, 64))
    player_walk_left.append(spritesheet_walk_side.get_sprite(0, 64, 64, 64))
    player_walk_left.append(spritesheet_walk_side.get_sprite(64, 64, 64, 64))

    player_idledown.append(spritesheet_idle_down.get_sprite(0,0,64,64))
    player_idledown.append(spritesheet_idle_down.get_sprite(64,0,64,64))
    player_idledown.append(spritesheet_idle_down.get_sprite(128,0,64,64))
    player_idledown.append(spritesheet_idle_down.get_sprite(192,0,64,64))
    player_idledown.append(spritesheet_idle_down.get_sprite(0,64,64,64))

    player_idleup.append(spritesheet_idle_up.get_sprite(0,0,64,64))
    player_idleup.append(spritesheet_idle_up.get_sprite(64,0,64,64))
    player_idleup.append(spritesheet_idle_up.get_sprite(128,0,64,64))
    player_idleup.append(spritesheet_idle_up.get_sprite(192,0,64,64))
    player_idleup.append(spritesheet_idle_up.get_sprite(0,64,64,64))

    player_idle_left.append(spritesheet_idle_side.get_sprite(0,0,64,64))
    player_idle_left.append(spritesheet_idle_side.get_sprite(64,0,64,64))
    player_idle_left.append(spritesheet_idle_side.get_sprite(128,0,64,64))
    player_idle_left.append(spritesheet_idle_side.get_sprite(192,0,64,64))
    player_idle_left.append(spritesheet_idle_side.get_sprite(0,64,64,64))

    player_idle_right.append(pg.transform.flip(spritesheet_idle_side.get_sprite(0, 0, 64, 64), True, False))
    player_idle_right.append(pg.transform.flip(spritesheet_idle_side.get_sprite(64, 0, 64, 64), True, False))
    player_idle_right.append(pg.transform.flip(spritesheet_idle_side.get_sprite(128, 0, 64, 64), True, False))
    player_idle_right.append(pg.transform.flip(spritesheet_idle_side.get_sprite(192, 0, 64, 64), True, False))
    player_idle_right.append(pg.transform.flip(spritesheet_idle_side.get_sprite(0, 64, 64, 64), True, False))

    player_walk_right.append(pg.transform.flip(spritesheet_walk_side.get_sprite(0, 0, 64, 64), True, False))
    player_walk_right.append(pg.transform.flip(spritesheet_walk_side.get_sprite(64, 0, 64, 64), True, False))
    player_walk_right.append(pg.transform.flip(spritesheet_walk_side.get_sprite(128, 0, 64, 64), True, False))
    player_walk_right.append(pg.transform.flip(spritesheet_walk_side.get_sprite(192, 0, 64, 64), True, False))
    player_walk_right.append(pg.transform.flip(spritesheet_walk_side.get_sprite(0, 64, 64, 64), True, False))
    player_walk_right.append(pg.transform.flip(spritesheet_walk_side.get_sprite(64, 64, 64, 64), True, False))

    return player_walkup, player_walkdown, player_walk_right, player_walk_left, player_idleup, player_idledown, player_idle_right, player_idle_left