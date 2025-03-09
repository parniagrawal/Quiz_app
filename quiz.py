import tkinter as tk
import random
from tkinter import messagebox

questions = {
    "What is the capital of France?": "Paris",
    "What is 5 + 7?": "12",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the chemical symbol for water?": "H2O",
    "Which planet is known as the Red Planet?": "Mars"
}

question_list = list(questions.items())
random.shuffle(question_list)

score = 0
current_question = 0

def check_answer():
    global score, current_question
    user_answer = answer_entry.get().strip()
    correct_answer = question_list[current_question][1]
    
    if user_answer.lower() == correct_answer.lower():
        score += 1
        messagebox.showinfo("Correct!", "Well done!")
    else:
        messagebox.showinfo("Wrong!", f"The correct answer was: {correct_answer}")
    
    current_question += 1
    if current_question < len(question_list):
        load_question()
    else:
        messagebox.showinfo("Quiz Over", f"Your final score is {score}/{len(question_list)}")
        root.quit()

def load_question():
    question_label.config(text=question_list[current_question][0])
    answer_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Quiz Game")
root.geometry("400x300")

question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=350)
question_label.pack(pady=20)

answer_entry = tk.Entry(root, font=("Arial", 12))
answer_entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit Answer", command=check_answer)
submit_button.pack(pady=10)

load_question()
root.mainloop()
