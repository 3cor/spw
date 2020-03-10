# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import modules.passgen as pg
import modules.mongodb as mg
import modules.xcrypt as xc


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageWC = QtWidgets.QWidget()
        self.pageWC.setObjectName("pageWC")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.pageWC)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.wcPushButtonSignin = QtWidgets.QPushButton(self.pageWC)
        self.wcPushButtonSignin.setObjectName("wcPushButtonSignin")
        self.gridLayout_2.addWidget(self.wcPushButtonSignin, 10, 0, 1, 1)
        self.wcLineEditPass = QtWidgets.QLineEdit(self.pageWC)
        self.wcLineEditPass.setObjectName("wcLineEditPass")
        self.gridLayout_2.addWidget(self.wcLineEditPass, 9, 0, 1, 1)
        self.wcLineEditUser = QtWidgets.QLineEdit(self.pageWC)
        self.wcLineEditUser.setText("")
        self.wcLineEditUser.setObjectName("wcLineEditUser")
        self.gridLayout_2.addWidget(self.wcLineEditUser, 8, 0, 1, 1)
        self.wcPushButtonSignup = QtWidgets.QPushButton(self.pageWC)
        self.wcPushButtonSignup.setObjectName("wcPushButtonSignup")
        self.gridLayout_2.addWidget(self.wcPushButtonSignup, 11, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.pageWC)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 7, 0, 1, 1)
        self.stackedWidget.addWidget(self.pageWC)
        self.pageRG = QtWidgets.QWidget()
        self.pageRG.setObjectName("pageRG")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.pageRG)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.pageRG)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.rgLineEditUser = QtWidgets.QLineEdit(self.pageRG)
        self.rgLineEditUser.setObjectName("rgLineEditUser")
        self.verticalLayout.addWidget(self.rgLineEditUser)
        self.rgLineEditPass = QtWidgets.QLineEdit(self.pageRG)
        self.rgLineEditPass.setObjectName("rgLineEditPass")
        self.verticalLayout.addWidget(self.rgLineEditPass)
        self.rgLineEditConfirm = QtWidgets.QLineEdit(self.pageRG)
        self.rgLineEditConfirm.setObjectName("rgLineEditConfirm")
        self.verticalLayout.addWidget(self.rgLineEditConfirm)
        self.rgPushButtonSubmit = QtWidgets.QPushButton(self.pageRG)
        self.rgPushButtonSubmit.setObjectName("rgPushButtonSubmit")
        self.verticalLayout.addWidget(self.rgPushButtonSubmit)
        self.rgPushButtonBack = QtWidgets.QPushButton(self.pageRG)
        self.rgPushButtonBack.setObjectName("rgPushButtonBack")
        self.verticalLayout.addWidget(self.rgPushButtonBack)
        self.stackedWidget.addWidget(self.pageRG)
        self.pageGEN = QtWidgets.QWidget()
        self.pageGEN.setObjectName("pageGEN")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.pageGEN)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.pageGEN)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 2)
        self.tabGenerate = QtWidgets.QTabWidget(self.pageGEN)
        self.tabGenerate.setObjectName("tabGenerate")
        self.tabPassword = QtWidgets.QWidget()
        self.tabPassword.setObjectName("tabPassword")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabPassword)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.tabPassword)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.tabPassword)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEditDG = QtWidgets.QLineEdit(self.tabPassword)
        self.lineEditDG.setObjectName("lineEditDG")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditDG)
        self.checkBoxSymbol = QtWidgets.QCheckBox(self.tabPassword)
        self.checkBoxSymbol.setChecked(True)
        self.checkBoxSymbol.setObjectName("checkBoxSymbol")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.checkBoxSymbol)
        self.lineEditSymbol = QtWidgets.QLineEdit(self.tabPassword)
        self.lineEditSymbol.setObjectName("lineEditSymbol")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditSymbol)
        self.lineEditNC = QtWidgets.QLineEdit(self.tabPassword)
        self.lineEditNC.setObjectName("lineEditNC")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditNC)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.pushButtonGenWord = QtWidgets.QPushButton(self.tabPassword)
        self.pushButtonGenWord.setObjectName("pushButtonGenWord")
        self.verticalLayout_2.addWidget(self.pushButtonGenWord)
        self.textEditPassword = QtWidgets.QPlainTextEdit(self.tabPassword)
        self.textEditPassword.setObjectName("textEditPassword")
        self.verticalLayout_2.addWidget(self.textEditPassword)
        self.tabGenerate.addTab(self.tabPassword, "")
        self.tabPassphrase = QtWidgets.QWidget()
        self.tabPassphrase.setObjectName("tabPassphrase")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabPassphrase)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.lineEditNW = QtWidgets.QLineEdit(self.tabPassphrase)
        self.lineEditNW.setObjectName("lineEditNW")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditNW)
        self.label_7 = QtWidgets.QLabel(self.tabPassphrase)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.pushButtonGenPhrase = QtWidgets.QPushButton(self.tabPassphrase)
        self.pushButtonGenPhrase.setObjectName("pushButtonGenPhrase")
        self.verticalLayout_3.addWidget(self.pushButtonGenPhrase)
        self.textEditPassphrase = QtWidgets.QPlainTextEdit(self.tabPassphrase)
        self.textEditPassphrase.setObjectName("textEditPassphrase")
        self.verticalLayout_3.addWidget(self.textEditPassphrase)
        self.tabGenerate.addTab(self.tabPassphrase, "")
        self.gridLayout_5.addWidget(self.tabGenerate, 1, 0, 1, 1)
        self.pushButtonBackToManager = QtWidgets.QPushButton(self.pageGEN)
        self.pushButtonBackToManager.setObjectName("pushButtonBackToManager")
        self.gridLayout_5.addWidget(self.pushButtonBackToManager, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.pageGEN)
        self.pageEntry = QtWidgets.QWidget()
        self.pageEntry.setObjectName("pageEntry")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.pageEntry)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButtonGen = QtWidgets.QPushButton(self.pageEntry)
        self.pushButtonGen.setObjectName("pushButtonGen")
        self.gridLayout_4.addWidget(self.pushButtonGen, 3, 3, 1, 1)
        self.pushButtonDelete = QtWidgets.QPushButton(self.pageEntry)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.gridLayout_4.addWidget(self.pushButtonDelete, 3, 2, 1, 1)
        self.pushButtonEdit = QtWidgets.QPushButton(self.pageEntry)
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.gridLayout_4.addWidget(self.pushButtonEdit, 3, 1, 1, 1)
        self.pushButtonNew = QtWidgets.QPushButton(self.pageEntry)
        self.pushButtonNew.setObjectName("pushButtonNew")
        self.gridLayout_4.addWidget(self.pushButtonNew, 3, 0, 1, 1)
        self.pushButtonLock = QtWidgets.QPushButton(self.pageEntry)
        self.pushButtonLock.setObjectName("pushButtonLock")
        self.gridLayout_4.addWidget(self.pushButtonLock, 3, 4, 1, 1)
        self.tableEntry = QtWidgets.QTableWidget(self.pageEntry)
        self.tableEntry.setRowCount(0)
        self.tableEntry.setColumnCount(0)
        self.tableEntry.setObjectName("tableEntry")
        self.gridLayout_4.addWidget(self.tableEntry, 5, 0, 1, 5)
        self.label_8 = QtWidgets.QLabel(self.pageEntry)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 5)
        self.stackedWidget.addWidget(self.pageEntry)
        self.pageEntryCUD = QtWidgets.QWidget()
        self.pageEntryCUD.setObjectName("pageEntryCUD")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.pageEntryCUD)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.detLineEditURL = QtWidgets.QLineEdit(self.pageEntryCUD)
        self.detLineEditURL.setObjectName("detLineEditURL")
        self.gridLayout_6.addWidget(self.detLineEditURL, 5, 0, 1, 1)
        self.detOK = QtWidgets.QPushButton(self.pageEntryCUD)
        self.detOK.setObjectName("detOK")
        self.gridLayout_6.addWidget(self.detOK, 6, 0, 1, 1)
        self.detLineEditName = QtWidgets.QLineEdit(self.pageEntryCUD)
        self.detLineEditName.setObjectName("detLineEditName")
        self.gridLayout_6.addWidget(self.detLineEditName, 1, 0, 1, 1)
        self.detCancel = QtWidgets.QPushButton(self.pageEntryCUD)
        self.detCancel.setObjectName("detCancel")
        self.gridLayout_6.addWidget(self.detCancel, 7, 0, 1, 1)
        self.detLineEditUser = QtWidgets.QLineEdit(self.pageEntryCUD)
        self.detLineEditUser.setObjectName("detLineEditUser")
        self.gridLayout_6.addWidget(self.detLineEditUser, 2, 0, 1, 1)
        self.detLineEditConfirm = QtWidgets.QLineEdit(self.pageEntryCUD)
        self.detLineEditConfirm.setObjectName("detLineEditConfirm")
        self.gridLayout_6.addWidget(self.detLineEditConfirm, 4, 0, 1, 1)
        self.detLineEditPass = QtWidgets.QLineEdit(self.pageEntryCUD)
        self.detLineEditPass.setObjectName("detLineEditPass")
        self.gridLayout_6.addWidget(self.detLineEditPass, 3, 0, 1, 1)
        self.detLabelEntry = QtWidgets.QLabel(self.pageEntryCUD)
        self.detLabelEntry.setObjectName("detLabelEntry")
        self.gridLayout_6.addWidget(self.detLabelEntry, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.pageEntryCUD)
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        self.labelOutput = QtWidgets.QLabel(self.centralwidget)
        self.labelOutput.setText("")
        self.labelOutput.setObjectName("labelOutput")
        self.gridLayout.addWidget(self.labelOutput, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabGenerate.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.wcPushButtonSignin.setText(_translate("MainWindow", "Sign in"))
        self.wcLineEditPass.setPlaceholderText(_translate("MainWindow", "Password"))
        self.wcLineEditUser.setPlaceholderText(_translate("MainWindow", "Username"))
        self.wcPushButtonSignup.setText(_translate("MainWindow", "Sign up"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Simple Password Manager</span></p><p align=\"center\"><span style=\" font-size:8pt; font-style:italic;\">Developed by Nitis Monburinon</span></p><p align=\"center\"><br/></p><p align=\"center\">Welcome to Simple Passsword Manager!</p><p align=\"center\">Simple Password Manager helps you to create your own password database and store it on MongoDB Atlas. </p><p align=\"center\">Please sign in using your registed username or sign up for a new account.</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Create new account</p><p><span style=\" font-size:11pt;\">Your password will be a master key.</span></p><p><span style=\" font-size:11pt;\">Master key is used to encrypt and decrypt your password database.</span></p><p><span style=\" font-size:11pt;\">If you lose your password, you cannot unlock your database!</span></p></body></html>"))
        self.rgLineEditUser.setPlaceholderText(_translate("MainWindow", "Username"))
        self.rgLineEditPass.setPlaceholderText(_translate("MainWindow", "Password"))
        self.rgLineEditConfirm.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
        self.rgPushButtonSubmit.setText(_translate("MainWindow", "Submit"))
        self.rgPushButtonBack.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Simple Password Generator</span></p><p align=\"center\"><br/></p><p align=\"center\">Simple password generator helps your generate cryptographically strong random password.</p><p align=\"center\"><br/></p><p>Here you have to options:</p><p>1. Generate random password from alphabet characters, numbers, or symbols.</p><p>2. Genrate random passphrase from wordlists. </p><p>This option is easier to remember. However, it is more susceptible to dictionary attack.</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Number of characters"))
        self.label_6.setText(_translate("MainWindow", "Minimum digits"))
        self.lineEditDG.setText(_translate("MainWindow", "3"))
        self.checkBoxSymbol.setText(_translate("MainWindow", "Include symbols"))
        self.lineEditSymbol.setText(_translate("MainWindow", "{}()[].,:;+-*/&|<>=~$"))
        self.lineEditNC.setText(_translate("MainWindow", "8"))
        self.pushButtonGenWord.setText(_translate("MainWindow", "Generate password"))
        self.tabGenerate.setTabText(self.tabGenerate.indexOf(self.tabPassword), _translate("MainWindow", "Password"))
        self.label_7.setText(_translate("MainWindow", "Number of words"))
        self.pushButtonGenPhrase.setText(_translate("MainWindow", "Generate passphrase"))
        self.tabGenerate.setTabText(self.tabGenerate.indexOf(self.tabPassphrase), _translate("MainWindow", "Passphrase"))
        self.pushButtonBackToManager.setText(_translate("MainWindow", "Back to manager"))
        self.pushButtonGen.setText(_translate("MainWindow", "Generate Pass"))
        self.pushButtonDelete.setText(_translate("MainWindow", "Delete entry"))
        self.pushButtonEdit.setText(_translate("MainWindow", "Edit entry"))
        self.pushButtonNew.setText(_translate("MainWindow", "New entry"))
        self.pushButtonLock.setText(_translate("MainWindow", "Lock"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/><span style=\" font-size:36pt;\">Password manager</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Manage your password database</span></p><p align=\"center\">All data are encrypted with your masterkey when they are uploaded to the cloud</p><p align=\"center\"><br/></p></body></html>"))
        self.detLineEditURL.setPlaceholderText(_translate("MainWindow", "URL"))
        self.detOK.setText(_translate("MainWindow", "OK"))
        self.detLineEditName.setPlaceholderText(_translate("MainWindow", "Name"))
        self.detCancel.setText(_translate("MainWindow", "Cancel"))
        self.detLineEditUser.setPlaceholderText(_translate("MainWindow", "Username"))
        self.detLineEditConfirm.setPlaceholderText(_translate("MainWindow", "Password"))
        self.detLineEditPass.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
        self.detLabelEntry.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">ENTRY</span></p></body></html>"))

        # DO NOT MODIFY GENERATED UI CODE PAST HERE 
        self.config()

    # TODO Remove or replace
    user = None
    pwd = None

    def config(self):

        # TODO Hide input password

        # Add signal to buttons
        self.wcPushButtonSignin.clicked.connect(self.signIn)
        self.wcPushButtonSignup.clicked.connect(self.signUp)

        self.rgPushButtonSubmit.clicked.connect(self.rgSubmit)
        self.rgPushButtonBack.clicked.connect(self.rgBack)

        self.pushButtonNew.clicked.connect(self.etNew)
        self.pushButtonEdit.clicked.connect(self.etEdit)
        self.pushButtonDelete.clicked.connect(self.etDelete)
        self.pushButtonGen.clicked.connect(self.etGenerate)
        self.pushButtonLock.clicked.connect(self.etLockDB)
        
        self.detOK.clicked.connect(self.detClickOK)
        self.detCancel.clicked.connect(self.detClickCancel)

        self.pushButtonGen.clicked.connect(self.goToGen)
        self.pushButtonGenWord.clicked.connect(self.genPassword)
        self.pushButtonGenPhrase.clicked.connect(self.genPassphrase)
        self.pushButtonBackToManager.clicked.connect(self.backToManager)

        # Config table
        self.tableEntry.setRowCount(0)
        self.tableEntry.setColumnCount(4)
        self.tableEntry.setHorizontalHeaderLabels("Name;Username;Password;URL".split(";"))
        self.tableEntry.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        header = self.tableEntry.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

    def output(self, msg):
        msg = '> ' + msg
        print(msg)
        self.labelOutput.setText(msg)

    def display(self, i):
        self.stackedWidget.setCurrentIndex(i)

    def checkUser(self, usr, pwd):
        db = mg.connect()
        result = mg.get_user(db, usr, pwd)
        print(result)
        if result > 0:
            return True
        else:
            return False

    def encrypt(self, msg):
        result = xc.password_encrypt(msg.encode(), self.pwd).decode('utf-8')
        print(result)
        return result

    def decrypt(self, msg):
        result = xc.password_decrypt(bytes(msg, 'utf-8'), self.pwd).decode()
        print(result)
        return result

    # pageWC

    def signIn(self):

        usr = self.wcLineEditUser.text()
        pwd = self.wcLineEditPass.text()

        print('signIn()')
        print('Username:' + usr)
        print('Password:' + pwd)

        if usr.strip() != '' and pwd.strip() != '':
            if self.checkUser(usr, pwd):
                # If user is found
                self.user = usr
                self.pwd = pwd
                self.syncTable()
                self.display(3)
            else:
                print("Wrong Username/Password")
        else:
            print("Please enter Username/Password")
        
    def signUp(self):
        print('signUp()')
        self.display(1)

    # pageRG

    def rgSubmit(self):
        # TODO Check credentials and connect td db
        usr = self.rgLineEditUser.text()
        pwd = self.rgLineEditPass.text()
        cfp = self.rgLineEditConfirm.text()
        print('rgSubmit()')
        print('Username:' + usr)
        print('Password:' + pwd)
        print('Confirm Password:' + cfp)

        if usr.strip() != '' and pwd.strip() != '':
            if pwd == cfp:
                if not self.checkUser(usr, pwd):
                    # If user is not found
                    self.user = usr
                    self.pwd = pwd
                    self.addUser(usr, pwd)
                    self.syncTable()
                    self.display(3)
                else:
                    print("Username is already used!")
            else:
                print("Password is not match!")
        else:
            print("Please enter Username/Password")

    def rgBack(self):
        print('rgBack()')
        self.display(0)

    def addUser(self, usr, pwd):
        db = mg.connect()
        mg.add_user(db, usr, pwd)

    # pageEntry

    def etNew(self):
        self.etMode = 'new'
        self.detLineEditName.setText('')
        self.detLineEditPass.setText('')
        self.detLineEditConfirm.setText('')
        self.detLineEditURL.setText('')
        self.display(4)

    def etEdit(self):
        row = self.tableEntry.currentRow()
        self.etMode = 'edit'
        self.detLineEditName.setText(self.tableEntry.item(row, 0).text()) 
        self.detLineEditUser.setText(self.tableEntry.item(row, 1).text()) 
        self.detLineEditPass.setText(self.tableEntry.item(row, 2).text()) 
        self.detLineEditConfirm.setText(self.tableEntry.item(row, 2).text()) 
        self.detLineEditURL.setText(self.tableEntry.item(row, 3).text()) 
        self.display(4)

    def etDelete(self):
        self.etMode = 'delete'
        self.deleteEntry()

    def etGenerate(self):
        self.display(2)

    def etLockDB(self):
        self.user = None
        self.pwd = None
        self.display(0)

    # pageEntryCUD

    def syncTable(self):
        self.tableEntry.setRowCount(0)
        database = mg.connect()
        result = mg.findall(database, self.user)
        for r in result:
            entry = [
                r['name'],
                r['user'],
                r['pass'],
                r['url']
            ]
            entry = [self.decrypt(e) for e in entry]
            self.table_appender(self.tableEntry, *entry)
            # print(r)

    def detClickOK(self):
        name = self.detLineEditName.text()
        usr = self.detLineEditUser.text()
        pwd = self.detLineEditPass.text()
        pcf = self.rgLineEditConfirm.text()
        url = self.detLineEditURL.text()

        print('detOK()')
        print('Name:' + name)
        print('Username:' + usr)
        print('Password:' + pwd)
        print('Confirm Password:' + pcf)
        print('URL:' + url)

        if '' not in (e.strip() for e in (name, usr, pwd, pcf, url)):
            if pwd != pcf:
                
                # Conditions passed!
                if self.etMode == 'new':
                    self.addEntry(name, usr, pwd, url)
                if self.etMode == 'edit':
                    self.editEntry(name, usr, pwd, url)

            else:
                print("Password is not match!")
        else:
            print("All field must be filled!")
        
        

    def detClickCancel(self):
        self.display(3)

    def addEntry(self, name, usr, pwd, url):

        entry = {
            'owner': self.user,
            'name': name,
            'user': usr,
            'pass': pwd,
            'url': url
        }

        # Encrypt every entry
        for k, v in entry.items():
            if k != 'owner':
             entry[k] = self.encrypt(v)

        db = mg.connect()
        ret = mg.add_entry(db, self.user, entry)
        print(ret.inserted_id)
        self.syncTable()
        self.display(3)

    def editEntry(self, name, usr, pwd, url):

        curr = self.getCurrentRow()

        entry = {
            'owner': self.user,
            'name': name,
            'user': usr,
            'pass': pwd,
            'url': url
        }
        db = mg.connect()
        mg.edit_entry(db, self.user, curr, entry)
        self.syncTable()
        self.display(3)
        
    def deleteEntry(self):

        curr = self.getCurrentRow()

        db = mg.connect()
        mg.delete_entry(db, self.user, curr)
        self.syncTable()

        
    def getCurrentRow(self):
        # get selected row
        row = self.tableEntry.currentRow()
        selected = (self.tableEntry.item(row, 0).text())
        return selected

    def table_appender(self, widget, *args):

        def set_columns(len, pos):
            if pos == len-1:
                widget.setItem(widget.rowCount()-1, pos, QtWidgets.QTableWidgetItem(args[pos]))
            else:
                widget.setItem(widget.rowCount()-1, pos, QtWidgets.QTableWidgetItem(args[pos]))
                set_columns(len, pos+1)
        widget.insertRow(widget.rowCount())
        set_columns(widget.columnCount(), 0)

    def goToGen(self):
        self.display(2)

    # pageGen

    def genPassword(self):
        
        n = int(self.lineEditNC.text())
        digit = int(self.lineEditDG.text())
        with_symbol = self.checkBoxSymbol.isChecked()
        symbols = self.lineEditSymbol.text()
        result = pg.secure(n, digit, with_symbol, symbols)

        self.textEditPassword.setPlainText(result)

    def genPassphrase(self):

        n = int(self.lineEditNW.text())
        result = pg.passphrase(n, 'data/words.txt')

        self.textEditPassword.setPlainText(result)

    def backToManager(self):
        display(3)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

