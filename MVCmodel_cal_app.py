import sys
from functools import partial
from PyQt5 import QtWidgets,QtCore,QtGui,Qt
ERROR_MSG = "ERROR"
class cal_ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Calculator")
        self.setMinimumSize(250,300)

        self.vlayout = QtWidgets.QVBoxLayout()
        self.main_widget = QtWidgets.QWidget()
        self.main_widget.setLayout(self.vlayout)
        self.setCentralWidget(self.main_widget)

        self.setup_ui()
    def setup_ui(self):

        self.hi_label = QtWidgets.QLabel()
        self.hi_label.setText("SIMPLE CALCULATOR")
        self.myfont = QtGui.QFont()
        self.myfont.setBold(True)
        self.hi_label.setFont(self.myfont)
        self.hi_label.setAlignment(QtCore.Qt.AlignCenter)
        self.vlayout.addWidget(self.hi_label)

        # number 1
        self.number_1 = QtWidgets.QSpinBox()
        self.number_1.setRange(-100000000,100000000)
        self.label1 = QtWidgets.QLabel()
        self.label1.setText("Number 1")
        self.number_1.setMaximumSize(250,25)    

        self.Hlayout_1 = QtWidgets.QHBoxLayout()
        self.Hlayout_1.addWidget(self.label1)
        self.Hlayout_1.addWidget(self.number_1)
        self.widget_1 = QtWidgets.QWidget()
        self.widget_1.setLayout(self.Hlayout_1)

        self.vlayout.addWidget(self.widget_1)

        #number 2

        self.number_2 = QtWidgets.QSpinBox()
        self.number_2.setRange(-100000000,100000000)
        self.label2 = QtWidgets.QLabel()
        self.label2.setText("Number 2")
        self.number_2.setMaximumSize(250,25)

        self.Hlayout_2 = QtWidgets.QHBoxLayout()
        self.Hlayout_2.addWidget(self.label2)
        self.Hlayout_2.addWidget(self.number_2)
        self.widget_2 = QtWidgets.QWidget()
        self.widget_2.setLayout(self.Hlayout_2)

        self.vlayout.addWidget(self.widget_2)

        #Operator

        self.label3 = QtWidgets.QLabel()
        self.label3.setText("Operator")
        self.Operator = QtWidgets.QComboBox()
        self.Operator.addItem("+")
        self.Operator.addItem("-")
        self.Operator.addItem("/")
        self.Operator.addItem("*")
        self.Operator.addItem("%")
        self.Operator.setMaximumSize(50,25)

        self.Hlayout_3 = QtWidgets.QHBoxLayout()
        self.Hlayout_3.addWidget(self.label3)
        self.Hlayout_3.addWidget(self.Operator)
        self.widget_3 = QtWidgets.QWidget()
        self.widget_3.setLayout(self.Hlayout_3)

        self.vlayout.addWidget(self.widget_3)

        #Result

        self.label4 = QtWidgets.QLabel()
        self.label4.setText("Result")
        self.Res = QtWidgets.QLineEdit()

        self.Hlayout_4 = QtWidgets.QHBoxLayout()
        self.Hlayout_4.addWidget(self.label4)
        self.Hlayout_4.addWidget(self.Res)
        self.widget_4 = QtWidgets.QWidget() 
        self.widget_4.setLayout(self.Hlayout_4)

        self.vlayout.addWidget(self.widget_4)
        
        #Odd ? Even
        self.label5 = QtWidgets.QLabel()
        self.label5.setAlignment(QtCore.Qt.AlignRight)
        self.label5.setText("Result is an odd/even")
        self.vlayout.addWidget(self.label5)

        
    def print(self,text):
        self.Res.setText(text)
    
    def odd_even(self,text):
        self.label5.setText(text)

class Control:
    def __init__(self,model,view):
        self._evaluate = model
        self._view = view
        #connect signals
        self._connectSignals()

    def _calculateResult(self):
        a = self._view.number_1.value()
        b = self._view.number_2.value()
        exp = str(a) + self._view.Operator.currentText() + str(b)
        result = self._evaluate.evaluateExpression(self,expression = exp)
        if result == ERROR_MSG :
            self._view.print("ERROR")
            self._view.odd_even("Oops! Wrong Expression")
        else:
            self._view.print(result)
            if float(result) < 0 :
                self._view.odd_even("I don't know")
            else:
                eve_or_odd = float(result) % 2
                if eve_or_odd == 1 : 
                    self._view.odd_even("Result is an odd number")
                elif eve_or_odd == 0 :
                    self._view.odd_even("Result is an even number")
                else:
                    self._view.odd_even("I don't know")

    def _connectSignals(self):
        self._view.number_1.valueChanged.connect(partial(self._calculateResult))
        self._view.number_2.valueChanged.connect(self._calculateResult)
        self._view.Operator.currentTextChanged.connect(self._calculateResult)
      
class Model:
    k = ""
    def __init__(self,expression):
        k=expression
        self.evaluateExpression(k)
    def evaluateExpression(self, expression):
        try: 
            result = str(eval(expression,{},{}))
        except Exception:
            result = ERROR_MSG
        return result
        


def main():
    app = QtWidgets.QApplication(sys.argv)
    view = cal_ui()
    view.show()
    model = Model
    Control(model=model,view=view)
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
