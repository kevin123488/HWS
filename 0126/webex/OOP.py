# class 대문자로 시작하는 이름
class Person:
    # 클래스 속성
    __population = 0

    # 생성자
    # 특별한 데코레이터가 없는 메서드는
    # 인스턴스 메서드고,
    # 인스턴스의 속성을 혹은 값을 조작하는 행위를 위한 메서드
    # 첫번째 인자로는 인스턴스 자신이 오게 될 것이다.
    # self라는 이름은 관례적인 것이고, 바뀌어도 문제는 없다.
    # 하지만 바꾸지는 않을 것이다.
    def __init__(self, name):
        # 인스턴스 속성
        self.name = name
        # self.population += 1
        # Person.population += 1
        self.increase()

    def __del__(self):
        print('으악')
    
    @classmethod
    def increase(cls):
        cls.__population += 1
        print(cls.__population)

    @staticmethod
    def decrease():
        Person.__population =- 1
        return '인구 감수가 일어나고 있습니다.'

class Human(Person):
    pass

a = Human('휴먼')

# kim = Person('김구현')
# kim 인스턴스는 name 속성을 처음 생성할때 할당되어서 가지게 된다.
# print(kim.name)
# print(type(kim))
# print(Person.name)
# hong = Person('홍길동')
# print(hong.name)
# print(kim.population, hong.population)
# print(Person.population)
# Person.population += 1
# print(Person.population)

# 클래스 메서드지만.. 인스턴스 호출 가능
# kim.increase()
# print(Person.population)

# Person.increase()
# print(Person.population)

# print(a.name)
# print(a.population)
# a.increase()
# print(a.population)
# print(Person.population)
# print(Human.population)
# a.decrease()
# print(Human.population)
# print(Person.population)

# print(Person.population)

p1 = Person('p1')
# p1.decrease()
# Person.__population += 1

# if __name__ == '__main__':