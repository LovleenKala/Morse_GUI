import RPi.GPIO as GPIO
import time
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("450x350")
window.title("Morse Code Machine")
window.configure(bg='#f5f6f7')  # Soft gray background

frame = Frame(window, bg='#f5f6f7')
frame.pack(pady=20, padx=20, expand=True, fill=BOTH)

heading_label = Label(frame, text="Morse Code Machine", font=("Arial", 24, "bold"), bg='#f5f6f7', fg='#3498db')  # Modern font, blue text
heading_label.grid(row=0, column=0, columnspan=2, pady=20)

textInput = StringVar()

LED = 18
unit = 0.5

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

def dot():
    GPIO.output(LED, True)
    time.sleep(unit)
    GPIO.output(LED, False)
    time.sleep(unit)

def dash():
    GPIO.output(LED, True)
    time.sleep(unit * 3)
    GPIO.output(LED, False)
    time.sleep(unit)

def newChar():
    time.sleep(unit * 2)

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..'
}

def convertToCode():
    MorseText = textInput.get().upper()
    if len(MorseText) > 12:
        messagebox.showinfo("Info", "Please limit your input to 12 characters.")
        return
    for char in MorseText:
        if char == ' ':
            time.sleep(unit * 6)
        elif char in morse_code:
            code = morse_code[char]
            for symbol in code:
                if symbol == '.':
                    dot()
                elif symbol == '-':
                    dash()
                time.sleep(unit)
            newChar()

# A function to display the Morse code for each letter as user reference
def show_morse_code():
    morse_window = Toplevel(window)
    morse_window.title("Morse Code Chart")
    Label(morse_window, text="\n".join([f"{char}: {code}" for char, code in morse_code.items()]), font=("Arial", 12)).pack(padx=10, pady=10)

showCodeButton = Button(frame, text="Show Morse Code", command=show_morse_code, bg='#3498db', fg='white', relief=FLAT, font=("Arial", 10))
showCodeButton.grid(row=1, column=1, sticky='E', padx=5)

textEntry = Entry(frame, width=25, textvariable=textInput, font=("Arial", 14), bg='#ecf0f1', fg='#2c3e50')
textEntry.grid(row=1, column=0, pady=20, padx=5)

convertButton = Button(frame, text="Convert to Morse Code", command=convertToCode, bg='#3498db', fg='white', relief=FLAT, font=("Arial", 12, "bold"), padx=20, pady=10)
convertButton.grid(row=2, column=0, columnspan=2, pady=20)

window.mainloop()
