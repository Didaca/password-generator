from tkinter import *
import random


PASSWORD_RANGE = 2
CAPITAL_LETTERS_RANGE = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
LETTERS_RANGE = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
SYMBOLS_RANGE = ('@', '$', '*', '#', '^', '&', ')', '(',)
NUMBERS_RANGE = 1, 10


def generate():

    password = ""
    sum_symbols = []

    for _ in range(PASSWORD_RANGE):

        all_letters = ""
        all_numbers = ""

        for _ in range(PASSWORD_RANGE):

            capital_letter = random.choice(CAPITAL_LETTERS_RANGE)
            letter = random.choice(LETTERS_RANGE)
            all_letters += capital_letter + letter

            number = random.randrange(NUMBERS_RANGE[0], NUMBERS_RANGE[1])
            all_numbers += str(number)

        symbol = random.choice(SYMBOLS_RANGE)

        password += all_letters + all_numbers + symbol

    sum_symbols.append(password)

    result = random.choice(sum_symbols)
    value.set(result)


window = Tk()
window.geometry("300x160")
window.title("Password Generator")
window.resizable(False, False)
window.config(bg="#023047")

value = StringVar()
value.set("- - - - - - - - - - - - - -")

label = Label(window, textvariable=value, width=16, height=2)
label.config(bg="#023047", font=("helvetica", 20), fg="white", border=3)
label.pack()

frame = Frame(window)
frame.pack()

btn = Button(frame, text="GENERATE", width=20, command=generate)
btn.config(bg="white", font=("helvetica", 16), fg="#fb8500", borderwidth=3, cursor="hand2")
btn.grid(row=0, column=0)


window.mainloop()
