    # 1
class Square:
    def __init__(self, side):
        self.side = side
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = self.radius * 2

class CircleInSquare(Square, Circle):
    def __init__(self):
        Square.__init__(self, side=10)
        Circle.__init__(self, radius=5)

cis = CircleInSquare()
print(f'Сторона квадрата: {cis.side} \n'
      f'Радиус круга: {cis.radius} \n'
      f'Диаметр круга: {cis.diameter}\n')

    # 2
class door:
    def __init__(self):
        self.name = "passenger_door"
        self.material = "steel"
        self.color = "White"
class wheel:
    def __init__(self):
        self.namewheel = "sport_wheel"
        self.size = "X6"
        self.radius = "40cm"
class motor:
    def __init__(self):
        self.namemotor = "XPl_235SA"
        self.powerhourse = "500"
        self.bulk = "120_l"
class control_box:
    def __init__(self):
        self.namebox = "1X2l_AAA_Class"
        self.speed = "6"
        self.drive = "all-wheel"

class Auto(control_box, motor, wheel, door):
    def __init__(self):
        self.carname = "BMW"
        control_box.__init__(self)
        wheel.__init__(self)
        motor.__init__(self)
        door.__init__(self)
    def __str__(self):
        return  (f'Название: {self.carname} \n'
                 f'Комплектация: \n'
                 f'***********************************\n'
                 f'Коробка передач: {self.namebox}\n'
                 f'Кол-во скоростей: {self.powerhourse}\n'
                 f'Привод: {self.drive}\n'
                 f'***********************************\n'
                 f'Название мотора: {self.namemotor}\n'
                 f'Лошадинные силы: {self.powerhourse}\n'
                 f'Объем: {self.bulk}\n'
                 f'***********************************\n'
                 f'Название колес: {self.namewheel}\n'
                 f'Размер колес: {self.size}\n'
                 f'Радиус колес: {self.radius}\n'
                 f'***********************************\n'
                 f'Название двери: {self.name}\n'
                 f'Материал двери: {self.material}\n'
                 f'Цвет двери: {self.color}\n'
                 f'***********************************\n')

autoObj = Auto()
print(autoObj)

    # 3
class HomePets:
    def __init__(self, name):
        self.name = name
    def Sound(self):
        print(f'Издаваемый звук: ')
    def Show(self):
        print(f"Имя животного: {self.name}")
    def Type(self):
        print(f'Подвид')
class Dog(HomePets):
    def __init__(self, breed, sound):
        super().__init__("Собака")
        self.breed = breed
        self.sound = sound
    def Sound(self):
        return(f'Издаваемый звук: {self.sound}')
    def Type(self):
        return(f'Подвид: {self.breed}')
    def Show(self):
        return(f"Имя животного: {self.name}")
class Cat(HomePets):
    def __init__(self, breed):
        super().__init__('Кошка')
        self.breed = breed
    def Sound(self):
        return('Издаваемый звук: Мяу')
    def Type(self):
        return(f'Подвид: {self.breed}')
    def Show(self):
        return(f"Имя животного: {self.name}")
class Parrot(HomePets):
    def __init__(self, breed):
        super().__init__('Попугай')
        self.breed = breed
    def Sound(self):
        return('Издаваемый звук: Кар')
    def Type(self):
        return(f'Подвид: {self.breed}')
    def Show(self):
        return(f"Имя животного: {self.name}")
class Hamster(HomePets):
    def __init__(self, breed):
        super().__init__("Хомяк")
        self.breed = breed
    def Sound(self):
        return('Издаваемый звук: Фр')
    def Type(self):
        return(f'Подвид: {self.breed}')
    def Show(self):
        return(f"Имя животного: {self.name}")

dog = Dog('Овчарка', 'Гав, Гав!')
cat = Cat('Сфинкс')
parrot = Parrot('Пиратский')
hamster = Hamster('Маленький хомячок')

for class2 in (dog, cat, parrot, hamster):
    print(class2.Show())
    print(class2.Type())
    print(class2.Sound())
    print('*'*13)


    # 4, 5
class Employer:
    def __init__(self):
        self.name = "Employer"
        self.age = 22
    def Print(self):
        print(f"This is {self.name} class")
    def __str__(self):
        return f"This is {self.name} class"
    def __int__(self):
        return self.age
class President(Employer):
    def __init__(self):
        self.name = "President"
        self.salary = 150000
        self.work = "Department management"
        self.age = 50
    def Print(self):
        print(f"This is {self.name} \n"
              f"Duties: {self.work} \n"
              f"Salary: {self.salary}")
class Manager(Employer):
    def __init__(self):
        self.name = "Manager"
        self.salary = 45000
        self.work = "Managing the Goods and Services Department"
        self.age = 30
    def Print(self):
        print(f"This is {self.name} \n"
              f"Duties: {self.work} \n"
              f"Salary: {self.salary}")
class Worker(Employer):
    def __init__(self):
        self.name = "Worker"
        self.salary = 25000
        self.work = "Transportation of goods and warehousing"
        self.age = 35
    def Print(self):
        print(f"This is {self.name} \n"
              f"Duties: {self.work} \n"
              f"Salary: {self.salary}")

employer = Employer()
worker = Worker()
manager = Manager()
president = President()
for class1 in (worker, manager, president, employer):
    class1.Print()
    print(class1) # переопредление метода str
    print(int(class1)) # переопредление метода int
    print("*"*15)


