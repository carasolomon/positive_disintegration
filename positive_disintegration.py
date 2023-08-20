# Positive Disintegration Program
# This program asks questions to assess the user's stage in Positive Disintegration Theory

import tkinter as tk

# Define the questions and corresponding stages
questions = [
    ("Are you primarily concerned with satisfying basic needs and desires?", 1),
    ("Do you follow societal norms and expectations without questioning them?", 1),
    ("Do you often feel conflicted without knowing why?", 2),
    ("Do you sometimes question societal norms but find it challenging to follow a different path?", 2),
    ("Have you experienced a significant crisis that has led you to question your values and beliefs?", 3),
    ("Do you feel a deep need to develop a personal moral code?", 3),
    ("Are you actively working to align your life with your own ethical principles?", 4),
    ("Do you feel a responsibility to live authentically, even if it conflicts with societal norms?", 4),
    ("Have you achieved a harmonious integration of your beliefs and values?", 5),
    ("Do you feel that you are living authentically and in harmony with your deeply held values?", 5)
]

def get_stage(responses):
    # Calculate the stage based on user responses
    scores = [0, 0, 0, 0, 0, 0]
    for response, (_, level) in zip(responses, questions):
        answer = response.get()
        if answer == 'yes':
            scores[level] += 2
    stage = scores.index(max(scores))
    return stage

def provide_guidance(stage):
    # Provide guidance text based on the identified stage
    guidance = {
        1: "You are focused on meeting basic needs and conforming to social norms. Consider exploring deeper values and beliefs.",
        2: "You are experiencing internal conflicts and questioning norms. It may be helpful to seek personal development opportunities and reflect on your values.",
        3: "You are in a phase of deep reflection and moral exploration. Continue to nurture your personal ethics and strive for authenticity.",
        4: "You are actively pursuing a life aligned with your ethical beliefs. Keep working on this path and don't be afraid to challenge conventional wisdom.",
        5: "You have achieved harmony between your beliefs and values. Continue to live authentically and inspire others to explore their personal growth journey.",
    }
    return guidance[stage]

def main():
    window = tk.Tk()
    window.title("Positive Disintegration Simulator")
    window.configure(bg='black')

    # Styling
    text_color = 'white'

    # Header
    header_label = tk.Label(window, text="Positive Disintegration Simulator", font=("Helvetica", 16), bg='black', fg=text_color)
    header_label.pack()

    # Instructions
    instructions_label = tk.Label(window, text="Please select 'Yes' or 'No' for each statement:", wraplength=500, bg='black', fg=text_color)
    instructions_label.pack(pady=10)

    # Radio buttons for questions
    responses = []
    for question, _ in questions:
        question_frame = tk.Frame(window, bg='black')
        question_frame.pack(pady=5)
        label = tk.Label(question_frame, text=question, wraplength=450, bg='black', fg=text_color)
        label.pack(side='left')
        response = tk.StringVar(value='no')
        yes_button = tk.Radiobutton(question_frame, text="Yes", variable=response, value='yes', bg='black', fg=text_color, selectcolor='gray')
        yes_button.pack(side='left')
        no_button = tk.Radiobutton(question_frame, text="No", variable=response, value='no', bg='black', fg=text_color, selectcolor='gray')
        no_button.pack(side='left')
        responses.append(response)

    # Label for results
    result_label = tk.Label(window, text="", wraplength=500, bg='black', fg=text_color)
    result_label.pack(pady=10)

    # Button click handler
    def on_calculate():
        stage = get_stage(responses)
        guidance = provide_guidance(stage)
        result_label.config(text=f"You are currently at stage {stage}.\n{guidance}")

    # Calculate button
    calculate_button = tk.Button(window, text="Calculate My Stage", command=on_calculate, bg='gray', fg='black')
    calculate_button.pack(pady=5)


    window.mainloop()

if __name__ == "__main__":
    main()
