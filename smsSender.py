import sys, threading, json
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from base import Ui_MainWindow
from twilio.rest import Client

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.btnSendSMS.clicked.connect(self.Initialize)

        with open('api.txt', 'r') as f:
            rApi =  json.load(f)
        
        self.account_sid = rApi['account_sid']
        self.auth_token = rApi['auth_token']
        self.smsFrom = rApi['phoneNumber']
    
    def Initialize(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)

        if (self.account_sid == 'enter_account_sid' or self.auth_token == 'enter_auth_token' or self.smsFrom == 'enter_phone_number'):
            msgBox.setWindowTitle("API Key Required!")
            msgBox.setText("Please fill up the api.txt with your TWILIO Account details.")
            msgBox.exec()
        else:
            t = threading.Thread(target=self.SEND_SMS)
            t.daemon = True
            t.start()
    
    def SEND_SMS(self):
        phoneNumber = self.tbPhoneNumber.text()
        smsMessage = self.tbMessage.toPlainText()

        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            body=smsMessage,
            from_=self.smsFrom,
            to=phoneNumber
        )
        if (message.status == 'queued'):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle("Message SENT!")
            msgBox.setText("Your Message has been successfully sent!")
            msgBox.exec()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setWindowTitle("ERROR!")
            msgBox.setText("An error has occured! Your message was not sent.")
            msgBox.exec()

if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())