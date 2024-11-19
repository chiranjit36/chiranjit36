import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Read the quiz data from the Excel file
quiz_data = pd.read_excel('quiz_data.xlsx')

# Extract the first row of data
question = quiz_data.loc[0, 'Question']
option1 = quiz_data.loc[0, 'Option1']
option2 = quiz_data.loc[0, 'Option2']
option3 = quiz_data.loc[0, 'Option3']
option4 = quiz_data.loc[0, 'Option4']
correct_answer = quiz_data.loc[0, 'CorrectAnswer']

# Create the main window
root = tk.Tk()
root.title("Today's Quiz")

# Display the question
question_label = tk.Label(root, text=question)
question_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Function to check the selected answer
def check_answer(selected_option):
    if selected_option == correct_answer:
        messagebox.showinfo("Result", "Right")
    else:
        messagebox.showinfo("Result", "Wrong")

# Create and display the option buttons
button1 = tk.Button(root, text=option1, command=lambda: check_answer(option1))
button1.grid(row=1, column=0, padx=10, pady=10)

button2 = tk.Button(root, text=option2, command=lambda: check_answer(option2))
button2.grid(row=1, column=1, padx=10, pady=10)

button3 = tk.Button(root, text=option3, command=lambda: check_answer(option3))
button3.grid(row=2, column=0, padx=10, pady=10)

button4 = tk.Button(root, text=option4, command=lambda: check_answer(option4))
button4.grid(row=2, column=1, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
