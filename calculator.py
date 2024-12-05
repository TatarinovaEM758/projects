import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton
from PyQt6.QtGui import QPalette, QColor
 
 
class Calculator(QWidget):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        grid = QGridLayout()
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        grid.addWidget(self.display, 0, 0, 1, 4)

        grid.addWidget(Color('blue'), 1, 0) # первое строка, второе столбец
        grid.addWidget(Color('blue'), 1, 1)
        grid.addWidget(Color('blue'), 1, 2)
        grid.addWidget(Color('blue'), 1, 3)
        grid.addWidget(Color('blue'), 2, 0)
        grid.addWidget(Color('blue'), 2, 1)
        grid.addWidget(Color('blue'), 2, 2)
        grid.addWidget(Color('blue'), 2, 3)
        grid.addWidget(Color('blue'), 3, 3)
        grid.addWidget(Color('blue'), 4, 3)
        grid.addWidget(Color('blue'), 5, 3)
        grid.addWidget(Color('blue'), 6, 3)
        grid.addWidget(Color('blue'), 6, 0)
        grid.addWidget(Color('blue'), 6, 2)
 


        names = ['%', '√', 'x²', '¹/x',
                 'CE', 'C', 'del', '/',
                 '7', '8', '9', '*',
                 '4', '5', '6', '-',
                 '1', '2', '3', '+',
                 '±', '0', '.', '=',]
 
        positions = [(i, j) for i in range(1, 7) for j in range(4)]



        for position, name in zip(positions, names):
            if name == '=':
                btn = QPushButton(name)
                btn.setStyleSheet("color: blue")
                btn.clicked.connect(self.equals)
                grid.addWidget(btn, *position)
            elif name == '±':
                men = QPushButton(name)
                men.clicked.connect(self.men_zn)
                grid.addWidget(men, *position)
            elif name == 'CE': # what?
                cee = QPushButton(name)
                cee.clicked.connect(self.cee_but)
                grid.addWidget(cee, *position)
            elif name == 'C':   #del all
                bcc = QPushButton(name)
                bcc.clicked.connect(self.c_but)
                grid.addWidget(bcc, *position)
            elif name == 'del': #del 1 symb
                dell = QPushButton(name)
                dell.clicked.connect(self.dell_but)
                grid.addWidget(dell, *position)
            elif name == '%':
                proc = QPushButton(name)
                proc.clicked.connect(self.procc)
                grid.addWidget(proc, *position)
            elif name == '√':
                rad = QPushButton(name)
                rad.clicked.connect(self.radic)
                grid.addWidget(rad, *position)
            elif name == 'x²':
                step = QPushButton(name)
                step.clicked.connect(self.step_kv)
                grid.addWidget(step, *position)
            elif name == '¹/x':
                stof = QPushButton(name)
                stof.clicked.connect(self.step_min)
                grid.addWidget(stof, *position)
            else:
                btn = QPushButton(name)
                btn.clicked.connect(lambda x, b=name: self.append_number(b))
                grid.addWidget(btn, *position)
 
        self.setLayout(grid)
        self.setWindowTitle('Calculator')
        
 
    def append_number(self, b):
        self.display.setText(self.display.text() + b)

    def procc(self):
        try:
            result = float(self.display.text()) * 0.01
            self.display.setText(str(result))
        except:
            self.display.setText('Error')
    
    def radic(self):
        try:
            result = float(self.display.text()) ** 0.5
            self.display.setText(str(result))
        except:
            self.display.setText('Error')
    
    def step_kv(self):
        try:
            result = float(self.display.text()) ** 2
            self.display.setText(str(result))
        except:
            self.display.setText('Error')
    
    def step_min(self):
        try:
            result = float(self.display.text()) ** (-1)
            self.display.setText(str(result))
        except:
            self.display.setText('Error')
    
    def cee_but(self):
        try:
            result = ""
            self.display.setText(str(result))
        except:
            self.display.setText('Error')

    def men_zn(self):
        try:
            result = -(eval(self.display.text()))
            self.display.setText(str(result))
        except:
            self.display.setText('Error')

    def c_but(self):
        try:
            result = eval(self.display.text())
            self.display.setText(str(result))
        except:
            self.display.setText('Error')

    def dell_but(self):
        eval(self.display.text()).backspace()
        try:
            result = self.display.text()
            result = result.edit.baskspace()
            self.display.setText(str(result))
        except:
            self.display.setText('Error')

    def equals(self):
        try:
            result = eval(self.display.text())
            self.display.setText(str(result))
        except:
            self.display.setText('Error')
 
 
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
    