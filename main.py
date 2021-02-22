class Printer:
    objectCounter = 0

    def __init__(self, brand="Samsung", pace=30, price=200, weight=5,
                  guarantee=2, country="China"):
        self.brand = brand
        self.pace = pace
        self.price = price
        self.weight = weight
        self.guarantee = guarantee
        self.country = country
        Printer.objectCounter += 1

    def __del__(self):
        Printer.objectCounter -= 1

    def __str__(self):
        return f"Printer\n" \
               f"Brand: {self.brand}\n" \
               f"Pace: {self.pace} st/s\n" \
               f"Price {self.price} hryvnias:\n" \
               f"Weight: {self.weight} kg\n" \
               f"Guarantee: {self.guarantee} years\n" \
               f"Country: {self.country}\n"

    @staticmethod
    def getObjectCounter():
        return Printer.objectCounter


def main():
    printers = [Printer("Canon", 20,  10, 15, 5, "Japan"), Printer("Apple", 50 ), Printer()]

    for printer in printers:
        print(printer)

    print("Number of created objects of class Printer:", Printer.getObjectCounter())


if __name__ == "__main__":
    main()