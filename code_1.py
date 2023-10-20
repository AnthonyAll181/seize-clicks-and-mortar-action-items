def main():
    return data
import random

if __name__ == "__main__":
    main()
    for item in data:
        print(f"Random Number: {item}")
    data = generate_random_data()

    data = [random.randint(1, 100) for _ in range(10)]

def generate_random_data():
