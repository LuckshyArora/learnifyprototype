import matplotlib.pyplot as plt

def generate_plot(attempts, difficulty_levels):
    if len(attempts) != len(difficulty_levels):
        raise ValueError("The length of attempts and difficulty_levels must be equal.")

    plt.figure(figsize=(10, 5))
    plt.plot(attempts, difficulty_levels, marker='o', linestyle='-', color='b', label='Difficulty Level')
    plt.xlabel("Attempt Number")
    plt.ylabel("Difficulty Level")
    plt.title("Difficulty Level Over Time")
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    # Data
    attempts = list(range(1, 11))
    difficulty_levels = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]

    # Generate the plot
    generate_plot(attempts, difficulty_levels)

if __name__ == "__main__":
    main()
