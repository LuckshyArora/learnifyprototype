import random
import matplotlib.pyplot as plt

class SimpleTutor:
    def __init__(self):
        self.responses = {
            "correct": ["Great job!", "Excellent!", "You're doing well!"],
            "incorrect": ["Not quite, try again.", "Close, but not correct.", "Let's review this."]
        }

    def evaluate_answer(self, student_answer, correct_answer):
        if student_answer.lower().strip() == correct_answer.lower().strip():
            return random.choice(self.responses["correct"])
        else:
            return random.choice(self.responses["incorrect"])


class AdaptiveMathModule:
    def __init__(self):
        self.difficulty = 1
        self.max_difficulty = 5
        self.scores = []

    def generate_question(self):
        a = random.randint(1, 10 * self.difficulty)
        b = random.randint(1, 10 * self.difficulty)
        return f"{a} + {b}", a + b

    def adjust_difficulty(self, correct):
        if correct and self.difficulty < self.max_difficulty:
            self.difficulty += 1
        elif not correct and self.difficulty > 1:
            self.difficulty -= 1

    def record_score(self, correct):
        self.scores.append(1 if correct else 0)


# Usage
tutor = SimpleTutor()
math_module = AdaptiveMathModule()

for _ in range(10):  # 10 questions
    question, answer = math_module.generate_question()
    try:
        student_input = input(f"{question} ").strip()
        feedback = tutor.evaluate_answer(student_input, str(answer))
        print(feedback)
        correct = student_input == str(answer)
        math_module.adjust_difficulty(correct)
        math_module.record_score(correct)
        print(f"Current difficulty: {math_module.difficulty}")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Visualize scores
plt.figure(figsize=(10, 5))
plt.plot(range(1, len(math_module.scores) + 1), math_module.scores, marker='o', linestyle='-')
plt.xlabel("Attempt Number")
plt.ylabel("Correct (1) / Incorrect (0)")
plt.title("Student Performance Over Time")
plt.grid(True)
plt.show()
