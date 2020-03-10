# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'greeter.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):

    switch_window = QtCore.pyqtSignal()

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.NonModal)
        mainWindow.resize(600, 480)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setObjectName("createButton")
        self.gridLayout.addWidget(self.createButton, 0, 0, 1, 1)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout.addWidget(self.exitButton, 7, 0, 1, 1)
        self.recentLabel = QtWidgets.QLabel(self.centralwidget)
        self.recentLabel.setObjectName("recentLabel")
        self.gridLayout.addWidget(self.recentLabel, 2, 0, 1, 1)
        self.recentListView = QtWidgets.QListView(self.centralwidget)
        self.recentListView.setObjectName("recentListView")
        self.gridLayout.addWidget(self.recentListView, 3, 0, 1, 1)
        self.aboutButton = QtWidgets.QPushButton(self.centralwidget)
        self.aboutButton.setObjectName("aboutButton")
        self.gridLayout.addWidget(self.aboutButton, 4, 0, 1, 1)
        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingsButton.setObjectName("settingsButton")
        self.gridLayout.addWidget(self.settingsButton, 5, 0, 1, 1)
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setObjectName("openButton")
        self.gridLayout.addWidget(self.openButton, 1, 0, 1, 1)
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setTextFormat(QtCore.Qt.AutoText)
        self.labelTitle.setScaledContents(True)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setWordWrap(True)
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout.addWidget(self.labelTitle, 0, 1, 8, 1)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(mainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCreate_a_new_vault = QtWidgets.QAction(mainWindow)
        self.actionCreate_a_new_vault.setObjectName("actionCreate_a_new_vault")
        self.actionUse_an_existing_vault = QtWidgets.QAction(mainWindow)
        self.actionUse_an_existing_vault.setObjectName("actionUse_an_existing_vault")

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        # Set tab orders
        mainWindow.setTabOrder(self.createButton, self.openButton)
        mainWindow.setTabOrder(self.openButton, self.recentListView)
        mainWindow.setTabOrder(self.recentListView, self.aboutButton)
        mainWindow.setTabOrder(self.aboutButton, self.settingsButton)
        mainWindow.setTabOrder(self.settingsButton, self.exitButton)

        mainWindow.switch_window.connect(self.show_window_two)

        # Add functionalites to buttons
        self.openButton.clicked.connect(self.createNewVault)
        self.openButton.clicked.connect(self.openRecentVaults)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.createButton.setText(_translate("mainWindow", "Create a new vault"))
        self.exitButton.setText(_translate("mainWindow", "Exit"))
        self.recentLabel.setText(_translate("mainWindow", "Recently opened vaults"))
        self.aboutButton.setText(_translate("mainWindow", "About"))
        self.settingsButton.setText(_translate("mainWindow", "Settings"))
        self.openButton.setText(_translate("mainWindow", "Open an existing vault"))
        self.labelTitle.setText(_translate("mainWindow", "Simple password manager"))
        self.actionExit.setText(_translate("mainWindow", "Exit"))
        self.actionAbout.setText(_translate("mainWindow", "About"))
        self.actionCreate_a_new_vault.setText(
            _translate("mainWindow", "Create a new vault")
        )
        self.actionUse_an_existing_vault.setText(
            _translate("mainWindow", "Use an existing vault")
        )


    def createNewVault(self):
        # TODO Add function to create new vault
        self.switch_window.emit()

    def openRecentVaults(self):
        # TODO change file extensions here
        fileName = QtWidgets.QFileDialog.getOpenFileName(
            None, "Open File", "/home", "Images (*.png *.xpm *.jpg)"
        )

        if fileName:
            # TODO Add logic here
            pass

class Login(QtWidgets.QWidget, Ui_mainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.pushbutton_handler)

    def pushbutton_handler(self):
        self.switch_window.emit()


class MainWindow(QtWidgets.QWidget, Ui_mainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.pushbutton_handler)

    def pushbutton_handler(self):
        self.switch_window.emit()


class Controller:

    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_main)
        self.login.show()

    def show_main(self):
        self.window = MainWindow()
        self.window.switch_window.connect(self.show_login)
        self.login.close()
        self.window.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    import sys
    main()