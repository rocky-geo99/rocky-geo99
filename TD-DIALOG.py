# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TD-DIALOG.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TimeDepthDialog(object):
    def setupUi(self, TimeDepthDialog):
        TimeDepthDialog.setObjectName("TimeDepthDialog")
        TimeDepthDialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(TimeDepthDialog)
        self.gridLayout.setContentsMargins(10, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.MainFrame = QtWidgets.QFrame(TimeDepthDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainFrame.sizePolicy().hasHeightForWidth())
        self.MainFrame.setSizePolicy(sizePolicy)
        self.MainFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MainFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Timeframe = QtWidgets.QFrame(self.MainFrame)
        self.Timeframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Timeframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Timeframe.setObjectName("Timeframe")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Timeframe)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Timelabel = QtWidgets.QLabel(self.Timeframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Timelabel.sizePolicy().hasHeightForWidth())
        self.Timelabel.setSizePolicy(sizePolicy)
        self.Timelabel.setObjectName("Timelabel")
        self.verticalLayout_2.addWidget(self.Timelabel)
        self.TimelineEdit = QtWidgets.QLineEdit(self.Timeframe)
        self.TimelineEdit.setText("")
        self.TimelineEdit.setObjectName("TimelineEdit")
        self.verticalLayout_2.addWidget(self.TimelineEdit)
        self.horizontalLayout.addWidget(self.Timeframe)
        self.DepthFrame = QtWidgets.QFrame(self.MainFrame)
        self.DepthFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DepthFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DepthFrame.setObjectName("DepthFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.DepthFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.DepthLabel = QtWidgets.QLabel(self.DepthFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DepthLabel.sizePolicy().hasHeightForWidth())
        self.DepthLabel.setSizePolicy(sizePolicy)
        self.DepthLabel.setObjectName("DepthLabel")
        self.verticalLayout.addWidget(self.DepthLabel)
        self.DepthlineEdit = QtWidgets.QLineEdit(self.DepthFrame)
        self.DepthlineEdit.setText("")
        self.DepthlineEdit.setObjectName("DepthlineEdit")
        self.verticalLayout.addWidget(self.DepthlineEdit)
        self.horizontalLayout.addWidget(self.DepthFrame)
        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)
        self.NOTElabel = QtWidgets.QLabel(TimeDepthDialog)
        self.NOTElabel.setObjectName("NOTElabel")
        self.gridLayout.addWidget(self.NOTElabel, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(TimeDepthDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 1)
        self.AddpushButton = QtWidgets.QPushButton(TimeDepthDialog)
        self.AddpushButton.setObjectName("AddpushButton")
        self.gridLayout.addWidget(self.AddpushButton, 2, 0, 1, 1)
        self.RemovepushButton = QtWidgets.QPushButton(TimeDepthDialog)
        self.RemovepushButton.setObjectName("RemovepushButton")
        self.gridLayout.addWidget(self.RemovepushButton, 3, 0, 1, 1)

        self.retranslateUi(TimeDepthDialog)
        self.buttonBox.accepted.connect(TimeDepthDialog.accept)
        self.buttonBox.rejected.connect(TimeDepthDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TimeDepthDialog)

    def retranslateUi(self, TimeDepthDialog):
        _translate = QtCore.QCoreApplication.translate
        TimeDepthDialog.setWindowTitle(_translate("TimeDepthDialog", "TimeDepthPair"))
        self.Timelabel.setText(_translate("TimeDepthDialog", "Time (s): "))
        self.TimelineEdit.setPlaceholderText(_translate("TimeDepthDialog", "0.6"))
        self.DepthLabel.setText(_translate("TimeDepthDialog", "Depth - SubSea (m):"))
        self.DepthlineEdit.setPlaceholderText(_translate("TimeDepthDialog", "200"))
        self.NOTElabel.setText(_translate("TimeDepthDialog", "NOTE: AT LEAST TWO PAIRS ARE NEEDED"))
        self.AddpushButton.setText(_translate("TimeDepthDialog", "Add Row"))
        self.RemovepushButton.setText(_translate("TimeDepthDialog", "Remove Row"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TimeDepthDialog = QtWidgets.QDialog()
    ui = Ui_TimeDepthDialog()
    ui.setupUi(TimeDepthDialog)
    TimeDepthDialog.show()
    sys.exit(app.exec_())
