#arquivo exemplo de interface gráfica usando a biblioteca Qt, versão 5, através do pacote PyQt5
#para testar: abrir o arquivo no spyder e clicar o play para executar o código no console.

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 200))    
        self.setWindowTitle("PyQt button example - pythonprogramminglanguage.com") 

        pybutton = QPushButton('Click me', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(100,32)
        pybutton.move(50, 50)        

    def clickMethod(self):
        print('Clicked Pyqt button.')

if __name__ == '__main__':
    import sys
    from PyQt5 import QtWidgets
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance() 
    main = MainWindow()
    main.show()
    app.exec_()
    
#reference:
#1a https://pythonprogramminglanguage.com/pyqt5-hello-world/
#1b https://pythonprogramminglanguage.com/pyqt5-button/
#2 https://github.com/spyder-ide/spyder/issues/4349
#3 https://github.com/spyder-ide/spyder/issues/4639
    