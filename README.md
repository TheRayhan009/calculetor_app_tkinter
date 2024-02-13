### Code Description

This Python script creates a graphical calculator application using the Tkinter library. The application allows users to perform basic arithmetic operations and includes special functions such as square root and exponentiation.

#### Imports:
- `tkinter`: A Python library for creating GUI applications.
- `os`: A module providing functions for interacting with the operating system.
- `math`: A module providing mathematical functions.

#### GUI Initialization:
- `panel = tkinter.Tk()`: Initializes the main window of the application.

#### Function Definitions:
- `click(event)`: Handles button clicks, performing calculations and updating the display accordingly.

#### Global Variables:
- `strvar`: Holds the string value displayed on the calculator.
- `ans`: Holds the result of calculations.

#### Button Creation:
- Buttons are created using the `Button` class from Tkinter.
- Each button represents a digit or an operation, with specified text, width, height, background color, border, and text color (`fg`).

#### Entry Widget:
- `input_box`: An entry widget for displaying input and output.
- Configured with a specific width, font, and background color.

#### Icon and Window Configuration:
- `panel.iconbitmap("Tkinter_project\logo.ico")`: Sets the application icon.
- `panel.configure(background="#17202A")`: Sets the background color of the main window.
- `panel.geometry("610x630+750+60")`: Sets the initial size and position of the window.
- `panel.title("RAYHAN's CALCULATOR")`: Sets the title of the window.

#### Main Loop:
- `panel.mainloop()`: Starts the main event loop of the application, allowing user interaction.

#### Additional Notes:
- The code includes comments to provide clarity on the purpose of each section.
- Buttons are labeled with digits, mathematical operators, and special symbols.
- Error handling is implemented for certain mathematical operations.
- The appearance of the calculator is customized using colors and sizing to enhance user experience.

### Screenshots

![Calculator Screenshot 1](/Screenshot_3.png)
![Calculator ScreenShot 2](/Screenshot_4.png)
![Calculator ScreenShot 3](/Screenshot_5.png)
