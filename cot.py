import matplotlib.pyplot as plt

# Data for number of attempts and their correctness
attempts = list(range(1, 11))
correctness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Create the plot with a specific figure size
plt.figure(figsize=(10, 5))

# Plot the data with markers and a line
plt.plot(attempts, correctness, marker='o', linestyle='-')

# Add labels for the x and y axes
plt.xlabel("Attempt Number")
plt.ylabel("Correct (1) / Incorrect (0)")

# Add a title to the plot
plt.title("Correctness Over Time")

# Enable the grid for better readability
plt.grid(True)

# Display the plot
plt.show()
