class Building:

    total = 0

    def __init__(self, building):
        self.building = building

for i in range(1, 41):
    Building.total = i
    print('Building ', Building.total)
