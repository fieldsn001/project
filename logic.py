from PyQt6.QtWidgets import *
from calculatorprojectgui import *
import math

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        '''
        Method to set default button values and connect them to the appropriate functions.
        '''
        super().__init__()
        self.setupUi(self)

        for button in [self.button_0, self.button_1, self.button_2, self.button_3, self.button_4,
                       self.button_5, self.button_6, self.button_7, self.button_8, self.button_9,
                       self.button_add, self.button_subtract, self.button_multiply, self.button_divide]:
            button.clicked.connect(self.button_click)

        self.button_enter.clicked.connect(self.calculate)
        self.button_clear.clicked.connect(self.clear)
        self.button_area.clicked.connect(self.toggle_area_calculator)
        self.button_submit.clicked.connect(self.area_submit)

        self.hide_area_calculator()
        self.last_calculation = False # flag to track if last action was a calc

    def button_click(self) -> None:
        '''
        Method to add button values clicked to the display
        '''
        button = self.sender()
        if self.last_calculation and button.text() in '0123456789':
            self.display.clear() # clear display if entering a new number after calc
        current = self.display.toPlainText()
        self.display.setPlainText(current + button.text())
        self.last_calculation = False # reset last calc flag

    def calculate (self) -> None:
        '''
        Method to calculate the result and add it to the display.
        '''
        try:
            result = eval(self.display.toPlainText())
            self.display.setPlainText(str(result))
            self.last_calculation = True # set flag to state calc performed
        except Exception as e:
            self.display.setPlainText('Error')
            self.last_calculation = True

    def clear(self) -> None:
        '''
        Method to clear the display by clicking the Clear button.
        '''
        self.display.clear()

    def toggle_area_calculator(self) -> None:
        '''
        Method to show or hide the area calculator.
        '''
        if self.input_base.isVisible():
            self.hide_area_calculator()
        else:
            self.show_area_calculator()
            self.display.clear() # auto clear the display on toggle

    def hide_area_calculator(self) -> None:
        '''
        Method to identify and hide area calculator widgets.
        '''
        for widget in [self.input_base, self.input_height, self.label_input_base, self.label_input_height,
            self.radioButton_circle, self.radioButton_square, self.radioButton_triangle, self.radioButton_rectangle,
            self.button_submit]:
            widget.hide()

    def show_area_calculator(self) -> None:
        '''
        Method to identify and show area calculator widgets.
        '''
        for widget in [self.input_base, self.input_height, self.label_input_base, self.label_input_height,
                       self.radioButton_circle, self.radioButton_square, self.radioButton_triangle,
                       self.radioButton_rectangle,
                       self.button_submit]:
            widget.show()

    def area_submit(self) -> str:
        '''
        Method to calculate and display the area result.
        :return: area result.
        '''
        shape = self.get_selected_shape()
        try:
            base = float(self.input_base.text())
            height = float(self.input_height.text())
        except ValueError:
            self.display.setPlainText('Please enter positive numbers')

        if shape == 'circle':
            area = math.pi * pow(base, 2)
        elif shape == 'square':
            area = pow(base,2)
        elif shape == 'rectangle':
            area = base * height
        elif shape == 'triangle':
            area = 0.5 * (base * height)
        elif shape is None:
            self.display.setPlainText('Please select a shape')
            return
        else:
            self.display.setPlainText('Invalid shape selected')
            return

        self.display.setPlainText(f'Area: {area:.2f}')

    def get_selected_shape(self) -> None:
        '''
        Method to identify the area shape.
        :return: area shape.
        '''
        if self.radioButton_circle.isChecked():
            return 'circle'
        if self.radioButton_square.isChecked():
            return 'square'
        if self.radioButton_rectangle.isChecked():
            return 'rectangle'
        if self. radioButton_triangle.isChecked():
            return 'triangle'
        else:
            return None

