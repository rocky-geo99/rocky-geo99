    #dialog for stretch squeeze dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QFormLayout

# Dialog prompt 
class Ui_TimeDepthDialog(QDialog):
    def __init__(self,parent=None,timelist=None,depthlist=None):
        super().__init__(parent)
        self.timelist = timelist
        self.depthlist = depthlist 
        self.setObjectName("TimeDepthDialog") #TimeDepthDialog.setObjectName("TimeDepthDialog")
        self.resize(400, 300) #TimeDepthDialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(10, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.MainFrame = QtWidgets.QFrame(self)
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
        self.verticalLayout_2.setObjectName("verticalLayout_2") #Layout for time 
        self.Timelabel = QtWidgets.QLabel(self.Timeframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Timelabel.sizePolicy().hasHeightForWidth())
        self.Timelabel.setSizePolicy(sizePolicy)
        self.Timelabel.setObjectName("Timelabel")
        self.verticalLayout_2.addWidget(self.Timelabel)      
        self.horizontalLayout.addWidget(self.Timeframe)
        self.DepthFrame = QtWidgets.QFrame(self.MainFrame)
        self.DepthFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DepthFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DepthFrame.setObjectName("DepthFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.DepthFrame) #Layout for Depth 
        self.verticalLayout.setObjectName("verticalLayout")
        self.DepthLabel = QtWidgets.QLabel(self.DepthFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DepthLabel.sizePolicy().hasHeightForWidth())
        self.DepthLabel.setSizePolicy(sizePolicy)
        self.DepthLabel.setObjectName("DepthLabel")
        self.verticalLayout.addWidget(self.DepthLabel)
        self.horizontalLayout.addWidget(self.DepthFrame)
        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)
        self.NOTElabel = QtWidgets.QLabel(self)
        self.NOTElabel.setObjectName("NOTElabel")
        self.gridLayout.addWidget(self.NOTElabel, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 1)
        self.AddpushButton = QtWidgets.QPushButton(self)
        self.AddpushButton.setObjectName("AddpushButton")
        self.gridLayout.addWidget(self.AddpushButton, 2, 0, 1, 1)
        self.RemovepushButton = QtWidgets.QPushButton(self)
        self.RemovepushButton.setObjectName("RemovepushButton")
        self.gridLayout.addWidget(self.RemovepushButton, 3, 0, 1, 1)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setWindowTitle("TimeDepthPair")
        self.Timelabel.setText("Time (s): ")
        self.DepthLabel.setText("Depth - SubSea (m):")       
        self.NOTElabel.setText( "NOTE: AT LEAST TWO PAIRS ARE NEEDED")
        self.AddpushButton.setText("Add Row")
        self.RemovepushButton.setText("Remove Row")
        
        
        # Controls for creating and removing rows
        self.control_time = []
        self.control_depth = [] 
        #add the first set of field 
        #self.add_field()
        #loading last list iff exist
        self.load_last(timelist,depthlist)
    
        #connection for each button 
        self.AddpushButton.clicked.connect(self.add_field)
        self.RemovepushButton.clicked.connect(self.remove_field)
        
        #temporary connection to Ok and cancel buttons 
        self.buttonBox.accepted.connect(self.get_Inputs)
        #execute class 
        self.exec()

    
    #method to load previously entered timelist and depth list 
    def load_last(self,timelist,depthlist): 
        # if there is data to load - load data
        if timelist != None:
            # for each item in the time list/depth list 
            for i in range(len(timelist)):
                # add it to each of the respected field 
                #self.add_field().addtext(timelist[i],depthlist[i])        
                #adding a row of time 
                timeedit = QLineEdit()
                timeedit.setText(str(timelist[i]))
                self.control_time.append(timeedit)
                self.verticalLayout_2.addWidget(timeedit)
                #adding a row of depth 
                depthedit = QLineEdit()
                depthedit.setText(str(depthlist[i]))
                self.control_depth.append(depthedit)
                self.verticalLayout.addWidget(depthedit)
                
        # otherwise, create an instance of the first field 
        else:
            self.add_field()
                
    # method to remove fields
    def remove_field(self):
        if len(self.control_time) >1:
            #removing the time row
            timeedit = self.control_time.pop()
            self.verticalLayout_2.removeWidget(timeedit)
            #removing the depth row
            depthedit = self.control_depth.pop()
            self.verticalLayout.removeWidget(depthedit)

    
    #method to add fields 
    def add_field(self):
        #adding a row of time 
        timeedit = QLineEdit()
        self.control_time.append(timeedit)
        self.verticalLayout_2.addWidget(timeedit)
        #adding a row of depth 
        depthedit = QLineEdit()
        self.control_depth.append(depthedit)
        self.verticalLayout.addWidget(depthedit)
        
    #method to retreive data 
    def get_Inputs(self):
        time = ', '.join(timeedit.text() for timeedit in self.control_time)#', '.join(edit.text() for edit in self.controls)
        depth = ', '.join(depthedit.text() for depthedit in self.control_depth)
        return time, depth 
