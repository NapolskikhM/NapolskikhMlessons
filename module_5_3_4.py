class Building:

    total = 0

    def __init__(self, building):
        self.building = building
        Building.total += 1

a = []
for i in range(40):
    a.append(Building(i))
    print(a[-1])