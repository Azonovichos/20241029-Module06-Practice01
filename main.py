# Module 6 Practice 1

class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
#        self.food = food
        if food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


#Выполняемый код(для проверки):

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a2.name)
print(p2.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.