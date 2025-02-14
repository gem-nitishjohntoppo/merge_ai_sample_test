class Greeter:
    def __init__(self, name):
        self.username = name  # Incorrect attribute name (should be self.name)

    def greet(self):
        # Incorrect variable reference (should be self.name)
        print(f"Hi {self.username}, greetings from Branch B!")

def main():
    user = Greeter()  # Missing argument error (should pass a name)
    user.greet()

if __name__ == "__main__":
    main()
