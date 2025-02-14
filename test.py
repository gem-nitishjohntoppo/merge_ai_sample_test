class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}! Welcome from Branch A.")

def main():
    user = Greeter("Alice")
    user.greet()

if __name__ == "__main__":
    main()
