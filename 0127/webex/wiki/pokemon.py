class Pokemon:
    info = '푸키먼...'
    population = 0
    speicies_population = 0
    
    # 새 포켓몬이 태어난다면...
    def __init__(self, name, lv=0):
        self.name = name
        self.lv = lv + 1
        self.skill = '몸통 박치기'
        # self.info = Pokemon.info + '피카츄'

        Pokemon.population += 1
        # self.increase()

    def attack(self):
        return self.skill

    @classmethod
    def increase(cls):
        cls.speicies_population += 1

# pika = Pokemon('피카츄', 5)
# print(pika.lv, pika.name, pika.info)
# print(pika.attack())
# meta = Pokemon('메타몽')
# print(meta.lv, meta.name, meta.info)