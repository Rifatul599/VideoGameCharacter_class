class VideogameCharacter:
    def __init__(self,name,health,attack_power,level=1):
        self.name=name
        self.health=health
        self.attack_power=attack_power
        self.level=level

    def take_damage(self,amount):
        self.health=max(0,self.health-amount)
        print(f"{self.name} took {amount} damages. Current health {self.health}.")

    def heal(self,amount):
        self.health+=amount
        print(f"{self.name} healed for {amount}. Current health {self.health}.")

    def level_up(self):
        self.level+=1
        self.health+=20
        self.attack_power+=5
        print(f"{self.name} leveled up! Level: {self.level}, Health: {self.health}, Attack: {self.attack_power}")

    def attack(self,enemy):
        if not isinstance(enemy, VideogameCharacter):
            print("Enemy must be a videoGameCharacter")
            return
        if self.is_alive():
            print(f"{self.name} attacks {enemy.name} for {self.attack_power} damage!")
            enemy.take_damage(self.attack_power)
        else:
            print(f"{self.name} cannot attack because they are not alive.")

    def is_alive(self):
        return self.health>0

    def display_status(self):
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack_power}")


hero=VideogameCharacter("Hero",100,20)
enemy=VideogameCharacter("Enemy",50,10)

hero.display_status()
hero.attack(enemy)
enemy.attack(hero)
hero.level_up()
hero.heal(30)
print(f"Is {hero.name} alive? {hero.is_alive()}")
