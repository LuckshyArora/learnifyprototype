import matplotlib.pyplot as plt

# Data
attempts = list(range(1, 11))
difficulty_levels = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(attempts, difficulty_levels, marker='o', linestyle='-')
plt.xlabel("Attempt Number")
plt.ylabel("Difficulty Level")
plt.title("Difficulty Level Over Time")
plt.grid(True)
plt.show()