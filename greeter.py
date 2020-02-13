# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'greeter.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_greeterWindow(object):
    def setupUi(self, greeterWindow):
        greeterWindow.setObjectName("greeterWindow")
        greeterWindow.setWindowModality(QtCore.Qt.NonModal)
        greeterWindow.resize(600, 480)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(greeterWindow.sizePolicy().hasHeightForWidth())
        greeterWindow.setSizePolicy(sizePolicy)
        greeterWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(greeterWindow)
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
        greeterWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(greeterWindow)
        self.statusbar.setObjectName("statusbar")
        greeterWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(greeterWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(greeterWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCreate_a_new_vault = QtWidgets.QAction(greeterWindow)
        self.actionCreate_a_new_vault.setObjectName("actionCreate_a_new_vault")
        self.actionUse_an_existing_vault = QtWidgets.QAction(greeterWindow)
        self.actionUse_an_existing_vault.setObjectName("actionUse_an_existing_vault")

        self.retranslateUi(greeterWindow)
        QtCore.QMetaObject.connectSlotsByName(greeterWindow)

        # Set tab orders
        greeterWindow.setTabOrder(self.createButton, self.openButton)
        greeterWindow.setTabOrder(self.openButton, self.recentListView)
        greeterWindow.setTabOrder(self.recentListView, self.aboutButton)
        greeterWindow.setTabOrder(self.aboutButton, self.settingsButton)
        greeterWindow.setTabOrder(self.settingsButton, self.exitButton)

        # Add functionalites to buttons
        self.openButton.clicked.connect(self.openRecentVaults)

    def retranslateUi(self, greeterWindow):
        _translate = QtCore.QCoreApplication.translate
        greeterWindow.setWindowTitle(_translate("greeterWindow", "MainWindow"))
        self.createButton.setText(_translate("greeterWindow", "Create a new vault"))
        self.exitButton.setText(_translate("greeterWindow", "Exit"))
        self.recentLabel.setText(_translate("greeterWindow", "Recently opened vaults"))
        self.aboutButton.setText(_translate("greeterWindow", "About"))
        self.settingsButton.setText(_translate("greeterWindow", "Settings"))
        self.openButton.setText(_translate("greeterWindow", "Open an existing vault"))
        self.labelTitle.setText(_translate("greeterWindow", "Simple password manager"))
        self.actionExit.setText(_translate("greeterWindow", "Exit"))
        self.actionAbout.setText(_translate("greeterWindow", "About"))
        self.actionCreate_a_new_vault.setText(
            _translate("greeterWindow", "Create a new vault")
        )
        self.actionUse_an_existing_vault.setText(
            _translate("greeterWindow", "Use an existing vault")
        )

    def openRecentVaults(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(
            None, "Open File", "/home", "Images (*.png *.xpm *.jpg)"
        )

        if fileName:
            # TODO Add logic here
            pass


    def open

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    greeterWindow = QtWidgets.QMainWindow()
    ui = Ui_greeterWindow()
    ui.setupUi(greeterWindow)
    greeterWindow.show()
    sys.exit(app.exec_())
