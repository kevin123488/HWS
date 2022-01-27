from wiki.pokemon import Pokemon

class Pikatchu(Pokemon):
    no = 25

    def __init__(self, name, lv=5):
        super().__init__(name, lv)
        self.skill = '전기 충격'

    def attack(self):
        return '찌릿 찌릿'
    
    def walk(self):
        return '뚜벅 뚜벅'

class Metamong(Pokemon):
    no = 132

    def __init__(self, name, lv=5):
        super().__init__(name, lv)
        self.skill = '변신'
    
    def attack(self):
        return '메타 메타'

    def eat(self):
        self.kg = 30
        print('메타몽의 냠냠')
        # return '냠냠'

class Child(Pikatchu, Metamong):
    def eat(self):
        super().eat()
        return '우걱우걱'

class Brother(Metamong, Pikatchu):
    pass

p = Child('ㅠㅋ')
print(p.attack())
c = Brother('c')
print(c.attack())
# b = Brother('메타몽?')
# print(b.no, b.eat(), b.walk())
# print(b.attack(), b.skill)
# c = Child('피카츄?')
# print(c.no, c.eat(), c.attack(), c.skill)

# pika = Pikatchu('피카츄')
# meta = Metamong('메타몽')
# print(meta.no, meta.attack())
# print(pika.no)
# print(pika.walk(), pika.lv, pika.attack())
# print(pika.name)
# print(Pokemon.population)
# print(Pikatchu.population)