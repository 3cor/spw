# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.detLineEditURL = QtWidgets.QLineEdit(Dialog)
        self.detLineEditURL.setObjectName("detLineEditURL")
        self.gridLayout.addWidget(self.detLineEditURL, 6, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 7, 0, 1, 1)
        self.detLineEditPass = QtWidgets.QLineEdit(Dialog)
        self.detLineEditPass.setObjectName("detLineEditPass")
        self.gridLayout.addWidget(self.detLineEditPass, 4, 0, 1, 1)
        self.detLineEditUser = QtWidgets.QLineEdit(Dialog)
        self.detLineEditUser.setObjectName("detLineEditUser")
        self.gridLayout.addWidget(self.detLineEditUser, 3, 0, 1, 1)
        self.detLineEditName = QtWidgets.QLineEdit(Dialog)
        self.detLineEditName.setObjectName("detLineEditName")
        self.gridLayout.addWidget(self.detLineEditName, 0, 0, 1, 1)
        self.detlineeditconfirm = qtwidgets.qlineedit(dialog)
        self.detlineeditconfirm.setobjectname("detlineeditconfirm")
        self.gridlayout.addwidget(self.detlineeditconfirm, 5, 0, 1, 1)

        self.retranslateui(dialog)
        self.buttonbox.accepted.connect(dialog.accept)
        self.buttonbox.rejected.connect(dialog.reject)
        qtcore.qmetaobject.connectslotsbyname(dialog)

    def retranslateui(self, dialog):
        _translate = qtcore.qcoreapplication.translate
        dialog.setwindowtitle(_translate("dialog", "dialog"))
        self.detlineediturl.setplaceholdertext(_translate("dialog", "url"))
        self.detlineeditpass.setplaceholdertext(_translate("dialog", "confirm password"))
        self.detlineedituser.setplaceholdertext(_translate("dialog", "username"))
        self.detlineeditname.setplaceholdertext(_translate("dialog", "name"))
        self.detlineeditconfirm.setplaceholdertext(_translate("dialog", "password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
