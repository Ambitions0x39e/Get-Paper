import sys, os, time
from src.info import subjects
from src.batch_download import batch_read
from PySide6 import QtCore, QtWidgets
from src.central import paper_download

# Example Link: https://cie.fraft.cn/obj/Fetch/redir/9709_m20_ms_22.pdf
'''
TODO: 
    - Try to predict if a .pdf file is 441bytes (incorrect file existence)
    - Now *DISABLED* subfolder. 
FIXME:

'''


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Get Paper")
        self.resize(400, 300)
        self.setup_ui()
        self.wait_echo()

    def setup_ui(self) -> None:

        listLabel = []
        label_1 = QtWidgets.QLabel("Paper Code")
        label_2 = QtWidgets.QLabel("Year")
        label_3 = QtWidgets.QLabel("Seasons")
        label_4 = QtWidgets.QLabel("Paper Number")
        label_5 = QtWidgets.QLabel("QP / MS")
        self.empty_line = QtWidgets.QLabel(" ")
        self.status_text = QtWidgets.QLabel(" ", alignment=QtCore.Qt.AlignHCenter)

        self.paperCodeInput = QtWidgets.QLineEdit()
        self.yearInput = QtWidgets.QLineEdit()
        self.seasonsInput = QtWidgets.QLineEdit()
        self.paperNumberInput = QtWidgets.QLineEdit()
        self.qpmsInput = QtWidgets.QLineEdit()

        self.button = QtWidgets.QPushButton("Download Paper")
        self.exit_button = QtWidgets.QPushButton("Quit App")
        self.clear_button = QtWidgets.QPushButton("Clear all Papers")
        self.open_button = QtWidgets.QPushButton("Open Folder")
        # self.batch_download = QtWidgets.QPushButton("Batch Download")
        

        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow(label_1, self.paperCodeInput)
        form_layout.addRow(label_2, self.yearInput)
        form_layout.addRow(label_3, self.seasonsInput)
        form_layout.addRow(label_4, self.paperNumberInput)
        form_layout.addRow(label_5, self.qpmsInput)
        
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addWidget(self.clear_button)
        btn_layout.addWidget(self.open_button)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.empty_line)
        main_layout.addWidget(self.status_text)
        main_layout.addWidget(self.empty_line)
        main_layout.addWidget(self.button)
        main_layout.addLayout(btn_layout) # clear and open
        # main_layout.addWidget(self.batch_download)
        main_layout.addWidget(self.exit_button)

        self.setLayout(main_layout)

    def wait_echo(self) -> None:
        self.paperCodeInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.yearInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.seasonsInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.paperNumberInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.qpmsInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)

        @QtCore.Slot()
        def Get_Paper():
            # 获取用户输入的信息
            paper_code = self.paperCodeInput.text()
            year = self.yearInput.text()
            season = self.seasonsInput.text()
            paper_number = self.paperNumberInput.text()
            qp_ms = self.qpmsInput.text()
            
            result , paper_name = paper_download(paper_code, year, season, paper_number, qp_ms)
            
            
            # Suppose the Py version is default python from Apple. 
            # send_notifications('Get Paper', '', result)
            if result == 'Success':
                self.status_text.setText(f'{result}: {paper_name}')
            else:
                self.status_text.setText(f'{result}')
            
            
            # 在状态标签中显示获取论文的状态信息
        def clear_cache():
            os.system("find ~/Downloads/Past_Papers -mindepth 1 -delete >/dev/null 2>&1")
            self.status_text.setText("All Papers cleared!")
        
        def open_folder():
            os.system('open ~/Downloads/Past_Papers')
        
        def batch_download_select():
            file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File")


        self.button.clicked.connect(Get_Paper)
        self.exit_button.clicked.connect(exit)
        self.clear_button.clicked.connect(clear_cache)
        self.open_button.clicked.connect(open_folder)
        # self.batch_download.clicked.connect(batch_download_select)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())