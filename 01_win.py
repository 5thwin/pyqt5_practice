#EX01 pyqt 창띄우기 + icon 넣기

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('종료', self) #QPushButton의 인스턴스 생성, arg{버튼이 표시될 텍스트, 버튼이 위치할 부모 위젯}
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        #버튼을 클릭하면 clicked 시그널 발생
        #QCoreApplication.instance()은 app이라는 변수가 바인딩 하고 있는 동일한 객체를 반환함
        #clicked' 시그널은 어플리케이션을 종료하는 quit() 메서드에 연결됩니다.
        #이렇게 발신자 (Sender)와 수신자 (Receiver), 두 객체 간에 커뮤니케이션이 이루어집니다.
        #이 예제에서 발신자는 푸시버튼 (btn)이고, 수신자는 어플리케이션 객체 (app)입니


        self.setWindowTitle("My first GUI")    #윈도우 창의 title 지정
        self.setWindowIcon(QIcon('img/ice.jpg')) #윈도우 아이콘 설정, Qicon({이미지경로})
        self.setGeometry(300, 300, 300, 200)    #move와 resize를 합쳐놓음
        #self.move(300, 300)
        #self.resize(300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv) # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 함
    ex = MyApp()
    sys.exit(app.exec_())
