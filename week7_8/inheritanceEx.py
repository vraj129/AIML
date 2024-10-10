class Animal: 
    def general(self):
        print("General")

class Dog(Animal):
    def habitat(self):
        self.general()

if __name__ == "__main__":
    d = Dog()
    d.habitat()
