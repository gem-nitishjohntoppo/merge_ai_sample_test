class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}! Welcome from Branch A.")

def main():
    user = Greeter("Alice")
    user.greet()

def find_duplicates(lst):
    duplicates = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):  # O(n²) complexity
            if lst[i] == lst[j] and lst[i] not in duplicates:
                duplicates.append(lst[i])
    return duplicates

if __name__ == "__main__":
    main()
