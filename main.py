import sys, os, time
from src.info import subjects
from PySide6 import QtCore, QtWidgets
from src.central import paper_download

# Example Link: https://cie.fraft.cn/obj/Fetch/redir/9709_m20_ms_22.pdf
'''
'''

  

class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Get Paper")
        self.resize(400, 300)
        self.setup_ui()
        self.wait_echo()

    def setup_ui(self) -> None:

        label_1 = QtWidgets.QLabel("Paper Code")
        label_2 = QtWidgets.QLabel("Year ")
        label_3 = QtWidgets.QLabel("Seasons")
        label_4 = QtWidgets.QLabel("Paper Number")
        label_5 = QtWidgets.QLabel("QP / MS")
        self.empty_line = QtWidgets.QLabel(" ")
        self.status_text = QtWidgets.QLabel(" ", alignment=QtCore.Qt.AlignHCenter)

        self.line_edit_1 = QtWidgets.QLineEdit()
        self.line_edit_2 = QtWidgets.QLineEdit()
        self.line_edit_3 = QtWidgets.QLineEdit()
        self.line_edit_4 = QtWidgets.QLineEdit()
        self.line_edit_5 = QtWidgets.QLineEdit()

        self.button = QtWidgets.QPushButton("↓ Download Paper ↓")
        self.exit_button = QtWidgets.QPushButton("Quit App")
        self.clear_button = QtWidgets.QPushButton("Clear all Papers")
        

        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow(label_1, self.line_edit_1)
        form_layout.addRow(label_2, self.line_edit_2)
        form_layout.addRow(label_3, self.line_edit_3)
        form_layout.addRow(label_4, self.line_edit_4)
        form_layout.addRow(label_5, self.line_edit_5)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.empty_line)
        main_layout.addWidget(self.status_text)
        main_layout.addWidget(self.empty_line)
        main_layout.addWidget(self.button)
        main_layout.addWidget(self.exit_button)
        main_layout.addWidget(self.clear_button)

        self.setLayout(main_layout)

    def wait_echo(self) -> None:
        self.line_edit_1.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.line_edit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.line_edit_3.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.line_edit_4.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.line_edit_5.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)

        @QtCore.Slot()
        def Get_Paper():
            # 获取用户输入的信息
            paper_code = self.line_edit_1.text()
            year = self.line_edit_2.text()
            season = self.line_edit_3.text()
            paper_number = self.line_edit_4.text()
            qp_ms = self.line_edit_5.text()
            
            result = paper_download(paper_code, year, season, paper_number, qp_ms)
            
            # Suppose the Py version is default python from Apple. 
            # send_notifications('Get Paper', '', result)
            self.status_text.setText(result)
            time.sleep(5)
            self.status_text.setText(" ")
            
            # 在状态标签中显示获取论文的状态信息
        def clear_cache():
            os.system("find ~/Downloads/Past_Papers -mindepth 1 -delete >/dev/null 2>&1")
            self.status_text.setText("All Papers cleared!")

        self.button.clicked.connect(Get_Paper)
        self.exit_button.clicked.connect(exit)
        self.clear_button.clicked.connect(clear_cache)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())