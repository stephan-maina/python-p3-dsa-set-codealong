class MySet:
    def __init__(self):
        self.elements = []

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)

    def contains(self, element):
        return element in self.elements

    def union(self, other_set):
        new_set = MySet()
        new_set.elements = self.elements.copy()

        for element in other_set.elements:
            if element not in self.elements:
                new_set.elements.append(element)

        return new_set

    def intersection(self, other_set):
        new_set = MySet()

        for element in self.elements:
            if element in other_set.elements:
                new_set.add(element)

        return new_set

    def __str__(self):
        return str(self.elements)


# Example usage:
if __name__ == "__main__":
    set1 = MySet()
    set1.add(1)
    set1.add(2)
    set1.add(3)

    set2 = MySet()
    set2.add(2)
    set2.add(3)
    set2.add(4)

    print("Set 1:", set1)
    print("Set 2:", set2)

    print("Union:", set1.union(set2))
    print("Intersection:", set1.intersection(set2))
