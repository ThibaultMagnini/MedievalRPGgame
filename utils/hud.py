from config import BLUE, GRAY, GREEN, HEIGHT, RED, WHITE
import pygame as pg
vec = pg.math.Vector2

class Hud:
    def __init__(self, width, height, game):
        self.width = width
        self.height = height
        self.game = game
        self.hud_color = (198, 155, 93, 175)

        self.inventory_surface = pg.Surface((width * 0.30, height * 0.10))
        self.inventory_surface.fill(self.hud_color)

        self.images = self.load_images()
        self.tiles = self.create_inventory_hud()

    def draw(self, screen):
        health = self.game.myfont.render(f"Health: {self.game.player.health}", False, (255, 255, 255))
        stamina = self.game.myfont.render(f"Stamina: {self.game.player.stamina}", False, (255, 255, 255))
        screen.blit(health, (20, HEIGHT - 80))
        screen.blit(stamina, (20, HEIGHT - 50))
        screen.blit(self.inventory_surface, (self.width * 0.35, self.height * 0.89))
        counter = 1
        for tile in self.tiles:
            screen.blit(tile['icon'], tile["rect"].topleft)
            pg.draw.rect(screen, (0,0,0), tile["rect"], 1)
            if tile["name"] in ["healingpot", "staminapot"]:
                textsurface = self.game.myfont.render(str(self.game.player.inventory.inventory_slots[tile["name"]]), False, (0, 0, 0))
                textsurface2 = self.game.myfontbutton.render(str(counter), False, (0, 0, 0))
                screen.blit(textsurface, (tile["rect"].centerx - 8, tile["rect"].centery - 7))
                screen.blit(textsurface2, tile["rect"].topright - vec(11,3))
                counter += 1



    def create_inventory_hud(self):

        renderPos = [self.width * 0.35 + 15, self.height * 0.89 + 7]
        object_width = self.inventory_surface.get_width() // 5

        tiles = []

        for image_name, image in self.images.items():
            pos = renderPos.copy()
            image_tmp = image.copy()
            image_scaled = self.scale_image(image_tmp, w=object_width)
            rect = image_scaled.get_rect(topleft=pos)

            tiles.append(
                {
                    "name": image_name,
                    "icon": image_scaled,
                    "image": self.images[image_name],
                    "rect": rect
                }
            )

            renderPos[0] += image_scaled.get_width() + 10
        
        return tiles

    def load_images(self):
        weapon = pg.image.load("sprites\environment\DAGGER 10.png")
        armor = pg.image.load("sprites\environment\ARMOR 1.png")
        healingpot = pg.image.load("sprites\environment\POTION 6.png")
        staminapot = pg.image.load("sprites\environment\POTION 3.png")
        
        images = {
            "weapon": weapon,
            "armor": armor,
            "healingpot" : healingpot,
            "staminapot" : staminapot
        }

        return images

    def scale_image(self, image, w=None, h=None):

        if w is None and h is None:
            pass
        
        elif h is None:
            scale = w / image.get_width()
            h = scale * image.get_height()
            image = pg.transform.scale(image, (int(w), int(h)))
        elif w is None:
            scale = h / image.get_height()
            w = scale * image.get_width()
            image = pg.transform.scale(image, (int(w), int(h)))
        else:
            image = pg.transform.scale(image, (int(w), int(h)))

        return image

class HealthBar:
    def __init__(self, x, y, hp, max_hp, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        self.hp = hp
        ratio = self.hp / self.max_hp
        pg.draw.rect(self.screen, RED, (self.x, self.y, 200, 20))
        for i in range(4):
            pg.draw.rect(self.screen, GRAY, (self.x-i,self.y-i,203,23), 1)
        pg.draw.rect(self.screen, GREEN, (self.x, self.y, 200 * ratio, 20))


class StaminaBar:
    def __init__(self, x, y, stamina, max_stamina, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.stamina = stamina
        self.max_stamina = max_stamina

    def draw(self, stamina):
        self.stamina = stamina
        ratio = self.stamina / self.max_stamina
        pg.draw.rect(self.screen, RED, (self.x, self.y, 200, 20))
        for i in range(4):
            pg.draw.rect(self.screen, GRAY, (self.x-i,self.y-i,203,23), 1)
        pg.draw.rect(self.screen, BLUE, (self.x, self.y, 200 * ratio, 20))