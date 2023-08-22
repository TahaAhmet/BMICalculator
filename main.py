from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.config(padx=20,pady=20)


weight_label = Label(text="Enter Your Weight(kg)", width=25)
weight_label.pack()

weight_entry = Entry(width=10)
weight_entry.pack()

height_label = Label(text="Enter Your Height(cm)", width=25)
height_label.pack()

height_entry = Entry(width=10)
height_entry.pack()


def calculating_bmi():
    weight_input = weight_entry.get()
    height_input = height_entry.get()

    if not weight_input or not height_input:
        result_label.config(text="Enter both weight and height.")
        return

    try:
        weight = float(weight_input)
        height_cm = float(height_input)
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")
        return

    if weight <= 0 or height_cm <= 0:
        result_label.config(text="Invalid input. Please enter valid values.")
        return

    height_m = height_cm / 100.0
    result_bmi = weight / (height_m * height_m)

    if result_bmi <= 18.5:
        result_explanation = "underweight"
    elif 18.5 < result_bmi < 24.9:
        result_explanation = "normal weight"
    elif 25 <= result_bmi < 29.9:
        result_explanation = "overweight"
    else:
        result_explanation = "obesity"
    result_label.config(text=f"Your BMI: {result_bmi:.2f}. You are {result_explanation}")

calculate_button = Button(text="Calculate", width=10, command=calculating_bmi)
calculate_button.config(padx=10, pady=10)
calculate_button.pack()

result_label = Label()
result_label.pack()

window.mainloop()