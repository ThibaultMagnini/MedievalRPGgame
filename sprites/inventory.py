class Inventory: 
    def __init__(self, player):
        self.inventory_slots = {}
        self.player = player
        self.display_inventory = False
        self.appendSlots()
        self.addHealingPot(3)
        self.addStaminaPot(3)

    def toggle_inventory(self):
        self.inventory_slots = not self.inventory_slots

    def appendSlots(self):
        self.inventory_slots["Weapon"] = "No weapon"
        self.inventory_slots["Armor"] = "No armor"
        self.inventory_slots["healingpot"] = 0
        self.inventory_slots["staminapot"] = 0
    
    def addHealingPot(self, amount):
        if self.inventory_slots["healingpot"] >= 20:
            print("You have reached the maximum amount of healing potions!")
        else:
            self.inventory_slots["healingpot"] += amount

    def addStaminaPot(self, amount):
        if self.inventory_slots["staminapot"] >= 20:
            print("You have reached the maximum amount of Stamina potions!")
        else:
            self.inventory_slots["staminapot"] += amount
    
    def replaceWeapon(self, weapon):
        if self.inventory_slots["Weapon"] != "No weapon":
            if weapon.damadge >= self.inventory_slots["Weapon"]:
                self.inventory_slots["Weapon"] = weapon
        else: 
            self.inventory_slots["Weapon"] = weapon

    def replaceArmor(self, armor):
        if self.inventory_slots["Armor"] != "No armor":
            if armor.armor_amount >= self.inventory_slots["Armor"]:
                self.inventory_slots["Armor"] = armor
        else: 
            self.inventory_slots["Armor"] = armor
        
    def consumeHealing(self):
        if self.inventory_slots["healingpot"] > 0:
            self.player.health += 20
            self.inventory_slots["healingpot"] -= 1
    
    def consumeStamina(self):
        if self.inventory_slots["staminapot"] > 0:
            self.player.stamina += 20
            self.inventory_slots["staminapot"] -= 1