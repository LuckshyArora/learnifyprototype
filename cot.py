import matplotlib.pyplot as plt

# Data
attempts = list(range(1, 11))
correctness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(attempts, correctness, marker='o', linestyle='-')
plt.xlabel("Attempt Number")
plt.ylabel("Correct (1) / Incorrect (0)")
plt.title("Correctness Over Time")
plt.grid(True)
plt.show()