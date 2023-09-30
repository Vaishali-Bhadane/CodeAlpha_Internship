import tkinter as tk

class Quiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("500x400") 

        self.questions = []
        self.score = 0
        self.current_question_index = 0
        self.selected_index = None  # Store the selected index

        # Create and configure labels
        self.question_label = tk.Label(root, text="", wraplength=600, font=("Helvetica", 16))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", command=lambda i=i: self.check_answer(i), font=("Helvetica", 14))
            button.pack(pady=10)
            self.option_buttons.append(button)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.result_label.pack(pady=20)

        self.thank_you_label = tk.Label(root, text="Thank you for attending!", font=("Helvetica", 16))
        self.thank_you_label.pack()

        # Hide the thank you label initially
        self.thank_you_label.pack_forget()

    def add_question(self, question, options, correct_answer):
        self.questions.append({
            'question': question,
            'options': options,
            'correct_answer': correct_answer
        })

    def display_question(self):
        question_data = self.questions[self.current_question_index]
        self.question_label.config(text=question_data['question'])
        for i, button in enumerate(self.option_buttons):
            button.config(text=question_data['options'][i])

    def check_answer(self, selected_index):
        self.selected_index = selected_index  # Store the selected index
        question_data = self.questions[self.current_question_index]
        if question_data['options'][selected_index] == question_data['correct_answer']:
            self.score += 1

        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        self.question_label.pack_forget()
        for button in self.option_buttons:
            button.pack_forget()

        result_text = f"Your score: {self.score}/{len(self.questions)}\n\n"
        for i, question_data in enumerate(self.questions):
            result_text += f"Question {i+1}: {question_data['question']}\n"
            if self.selected_index is not None:
                result_text += f"Your answer: {question_data['options'][self.selected_index]}\n"  # Display the selected answer
            result_text += f"Correct answer: {question_data['correct_answer']}\n\n"

        self.result_label.config(text=result_text)
        self.result_label.pack()
        self.thank_you_label.pack()

def main():
    root = tk.Tk()
    quiz = Quiz(root)

    # Add new questions below using the add_question method
    quiz.add_question("What is the capital of Italy?", ["Paris", "Rome", "Madrid", "Berlin"], "Rome")
    quiz.add_question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], "Mars")
    quiz.add_question("Who is the author of 'To Kill a Mockingbird'?", ["Charles Dickens", "Jane Austen", "Harper Lee", "Mark Twain"], "Harper Lee")

    quiz.display_question()
    root.mainloop()

if __name__ == "__main__":
    main()
