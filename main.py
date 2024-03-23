import sys, os, time
from PySide6 import QtCore, QtWidgets
from src.info import subjects
from src.write_pdf import download_pdf
import objc
from Cocoa import NSObject
from AppKit import NSUserNotificationCenter, NSUserNotification
# Example Link: https://cie.fraft.cn/obj/Fetch/redir/9709_m20_ms_22.pdf
class NotificationDelegate(NSObject):
    def userNotificationCenter_didActivateNotification_(self, center, notification):
        # Handle notification activation
        pass
    
def send_notification(title, subtitle, message):
    delegate = NotificationDelegate.alloc().init()
    center = NSUserNotificationCenter.defaultUserNotificationCenter()
    center.setDelegate_(delegate)

    notification = NSUserNotification.alloc().init()
    notification.setTitle_(title)
    notification.setSubtitle_(subtitle)
    notification.setInformativeText_(message)

    center.deliverNotification_(notification)
    
def main(Paper_Code, Year, Season, Paper_Number, Qp_Ms):
    # FULL year if user only inputs the last two digits of the year number
    if len(Paper_Code) != 4: return "Wrong Paper Code"
    if len(Year) == 2: Year = '20' + Year
    seasons = ''
    seasons = 'm' if Season.lower() in ['march', 'mar', 'feb', 'february', 'spring'] \
        else 's' if Season.lower() in ['may', 'june', 'jun', 'summer'] \
        else 'w' if Season.lower() in ['oct', 'october', 'nov', 'november', 'winter'] \
        else ''
    if seasons == '':
        return 'Wrong Seasons'
    qp_name = f'{Paper_Code}_{seasons}{Year[2:]}_qp_{Paper_Number}'
    ms_name = f'{Paper_Code}_{seasons}{Year[2:]}_ms_{Paper_Number}'
    src_qp= 'https://cie.fraft.cn/obj/Fetch/redir/'+f'{qp_name}.pdf'
    src_ms= 'https://cie.fraft.cn/obj/Fetch/redir/'+f'{ms_name}.pdf'
    
    if Qp_Ms == '':
        try: 
            download_pdf(src_qp, qp_name)
            download_pdf(src_ms, ms_name)
            print(1)
        except ConnectionResetError:
            return "Wrong Network! Please check your network / proxies"
    elif Qp_Ms.lower() == 'qp':
        try:
            download_pdf(src_qp, qp_name)
        except ConnectionResetError:
            return "Wrong Network! Please check your network / proxies"
    elif Qp_Ms.lower() == 'ms': 
        try:
            download_pdf(src_ms, ms_name)
        except ConnectionResetError:
            return "Wrong Network! Please check your network / proxies"
    else:
        return "Wrong QP / MS input!"
    
    return 'Success'
    
def send_notification(title, subtitle, message):
    notification = NSUserNotification.alloc().init()
    notification.setTitle_(title)
    notification.setSubtitle_(subtitle)
    notification.setInformativeText_(message)

    center = NSUserNotificationCenter.defaultUserNotificationCenter()
    center.deliverNotification_(notification)

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

        self.line_edit_1 = QtWidgets.QLineEdit()
        self.line_edit_2 = QtWidgets.QLineEdit()
        self.line_edit_3 = QtWidgets.QLineEdit()
        self.line_edit_4 = QtWidgets.QLineEdit()
        self.line_edit_5 = QtWidgets.QLineEdit()

        self.button = QtWidgets.QPushButton("↓ Download Paper ↓")
        self.exitbutton = QtWidgets.QPushButton("Quit App")
        

        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow(label_1, self.line_edit_1)
        form_layout.addRow(label_2, self.line_edit_2)
        form_layout.addRow(label_3, self.line_edit_3)
        form_layout.addRow(label_4, self.line_edit_4)
        form_layout.addRow(label_5, self.line_edit_5)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.button)
        main_layout.addWidget(self.exitbutton)

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
            
            result = main(paper_code, year, season, paper_number, qp_ms)
            
            send_notification('Get Paper', '', result)
            # 在状态标签中显示获取论文的状态信息

        self.button.clicked.connect(Get_Paper)
        self.exitbutton.clicked.connect(exit)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())