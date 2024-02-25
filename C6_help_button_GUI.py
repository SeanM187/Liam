from tkinter import *


class Converter:

    def __init__(self):
        # Initialise variables (such as the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        self.all_calculations = []

        # common format for all buttons
        # arial size 14 bold, with white text
        button_font = ("Arial", "11", "bold")
        button_fg = "#FFFFFF"

        # set up gui frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.button_frame = Frame(padx=30, pady=30)
        self.button_frame.grid(row=0)

        self.to_help_button = Button(self.button_frame, text="Help / Info", bg="#CC6600", fg=button_fg,
                                     font=button_font, width=12, command=self.to_help)
        self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

    @staticmethod
    def to_help():
        DisplayHelp()


class DisplayHelp:

    def __init__(self):
        # setup dialogue box and bg colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg=background, text="Help / Infor",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To use the program, simply enter the temperature you wish to convert and then choose to convert " \
                    "to either degrees Celsius(centigrade) or Fahrenheit..  \n\n " \
                    "Note that -273 degrees C (-459) is absolute zero (the coldest possible temperature that is less " \
                    "than -273 degrees C, you will get an error message. \n\n )" \
                    "To see your calculation history and export it to a text file, please click the " \
                    "'History / Export' button."
        self.help_text_label = Label(self.help_frame, bg=background, text=help_text, wrap=350, justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame, font=("Arial", "12", "bold"), text="Dismiss",
                                     bg="#CC6600", fg="#FFFFFF", command=self.help_box.destroy)
        self.dismiss_button.grid(row=2, padx=10, pady=10)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
