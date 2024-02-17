class MemoryDevice:
    def printPhysicalSize(self):
        print("medium")

class SDCard(MemoryDevice):
    def printPhysicalSize(self):
        print("small")

sdCard=SDCard()
sdCard.printPhysicalSize()