#GUI library imports 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QLineEdit, QDialogButtonBox, QFormLayout
from PyQt5.uic import loadUi
from pyqtgraph import PlotWidget
import pyqtgraph as pg 
import math 
import bruges as bg 

#well file handling library imports 
import welly
from welly import Well
import pandas as pd
import lasio
import numpy as np

class Ui_MainWindow(object):  
    #Main Woindow setup 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 850)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Mainframe = QtWidgets.QFrame(self.centralwidget)
        self.Mainframe.setGeometry(QtCore.QRect(10, 10, 861, 641))
        self.Mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Mainframe.setObjectName("Mainframe")
        self.wellinfoframe = QtWidgets.QFrame(self.Mainframe)
        self.wellinfoframe.setGeometry(QtCore.QRect(0, 70, 181, 261))
        self.wellinfoframe.setFrameShape(QtWidgets.QFrame.Box)
        self.wellinfoframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wellinfoframe.setLineWidth(2)
        self.wellinfoframe.setObjectName("wellinfoframe")
        self.Well_info_label = QtWidgets.QLabel(self.wellinfoframe)
        self.Well_info_label.setGeometry(QtCore.QRect(50, 10, 70, 20))
        self.Well_info_label.setFrameShape(QtWidgets.QFrame.Box)
        self.Well_info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Well_info_label.setObjectName("Well_info_label")
        self.Track1dropdown = QtWidgets.QLabel(self.wellinfoframe)
        self.Track1dropdown.setGeometry(QtCore.QRect(10, 40, 55, 16))
        self.Track1dropdown.setFrameShape(QtWidgets.QFrame.Box)
        self.Track1dropdown.setObjectName("Track1dropdown")
        self.Track2dropdown = QtWidgets.QLabel(self.wellinfoframe)
        self.Track2dropdown.setGeometry(QtCore.QRect(10, 100, 55, 16))
        self.Track2dropdown.setFrameShape(QtWidgets.QFrame.Box)
        self.Track2dropdown.setObjectName("Track2dropdown")
        self.Track3dropdown = QtWidgets.QLabel(self.wellinfoframe)
        self.Track3dropdown.setGeometry(QtCore.QRect(10, 180, 55, 16))
        self.Track3dropdown.setFrameShape(QtWidgets.QFrame.Box)
        self.Track3dropdown.setObjectName("Track3dropdown")
        self.comboBox_Track1 = QtWidgets.QComboBox(self.wellinfoframe)
        self.comboBox_Track1.setGeometry(QtCore.QRect(10, 70, 151, 21))
        self.comboBox_Track1.setObjectName("comboBox_Track1")
        self.comboBox_Track2 = QtWidgets.QComboBox(self.wellinfoframe)
        self.comboBox_Track2.setGeometry(QtCore.QRect(10, 140, 151, 21))
        self.comboBox_Track2.setObjectName("comboBox_Track2")
        self.comboBox_Track3 = QtWidgets.QComboBox(self.wellinfoframe)
        self.comboBox_Track3.setGeometry(QtCore.QRect(10, 210, 151, 21))
        self.comboBox_Track3.setObjectName("comboBox_Track3")
        self.Track1Frame = QtWidgets.QFrame(self.Mainframe)
        self.Track1Frame.setGeometry(QtCore.QRect(200, 70, 151, 551))
        self.Track1Frame.setAutoFillBackground(True)
        self.Track1Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.Track1Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Track1Frame.setObjectName("Track1Frame")
        self.Track1Graph = PlotWidget(self.Track1Frame)
        self.Track1Graph.setGeometry(QtCore.QRect(0, 0, 151, 551))
        self.Track1Graph.setObjectName("Track1Graph")
        self.label_track1 = QtWidgets.QLabel(self.Mainframe)
        self.label_track1.setGeometry(QtCore.QRect(250, 50, 55, 16))
        self.label_track1.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_track1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_track1.setObjectName("label_track1")
        self.label_track2 = QtWidgets.QLabel(self.Mainframe)
        self.label_track2.setGeometry(QtCore.QRect(410, 50, 55, 16))
        self.label_track2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_track2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_track2.setObjectName("label_track2")
        self.label_track3 = QtWidgets.QLabel(self.Mainframe)
        self.label_track3.setGeometry(QtCore.QRect(570, 50, 55, 16))
        self.label_track3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_track3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_track3.setObjectName("label_track3")
        self.label_track_syngen1 = QtWidgets.QLabel(self.Mainframe)
        self.label_track_syngen1.setGeometry(QtCore.QRect(700, 30, 111, 31))
        self.label_track_syngen1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_track_syngen1.setScaledContents(False)
        self.label_track_syngen1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_track_syngen1.setWordWrap(True)
        self.label_track_syngen1.setObjectName("label_track_syngen1")
        self.Synthetic_Graph_Widget = QtWidgets.QWidget(self.Mainframe)
        self.Synthetic_Graph_Widget.setGeometry(QtCore.QRect(0, 340, 181, 301))
        self.Synthetic_Graph_Widget.setObjectName("Synthetic_Graph_Widget")
        self.wavelet_graph = PlotWidget(self.Synthetic_Graph_Widget)
        self.wavelet_graph.setGeometry(QtCore.QRect(0, 30, 181, 271))
        self.wavelet_graph.setObjectName("wavelet_graph")
        self.wavelet_plot_title = QtWidgets.QLabel(self.Synthetic_Graph_Widget)
        self.wavelet_plot_title.setGeometry(QtCore.QRect(50, 0, 91, 21))
        self.wavelet_plot_title.setAlignment(QtCore.Qt.AlignCenter)
        self.wavelet_plot_title.setObjectName("wavelet_plot_title")
        self.Track2Frame = QtWidgets.QFrame(self.Mainframe)
        self.Track2Frame.setGeometry(QtCore.QRect(360, 70, 151, 551))
        self.Track2Frame.setAutoFillBackground(True)
        self.Track2Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.Track2Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Track2Frame.setObjectName("Track2Frame")
        self.Track2Graph = PlotWidget(self.Track2Frame)
        self.Track2Graph.setGeometry(QtCore.QRect(0, 0, 151, 551))
        self.Track2Graph.setObjectName("Track2Graph")
        self.Track3Frame = QtWidgets.QFrame(self.Mainframe)
        self.Track3Frame.setGeometry(QtCore.QRect(520, 70, 151, 551))
        self.Track3Frame.setAutoFillBackground(True)
        self.Track3Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.Track3Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Track3Frame.setObjectName("Track3Frame")
        self.Track3Graph = PlotWidget(self.Track3Frame)
        self.Track3Graph.setGeometry(QtCore.QRect(0, 0, 151, 551))
        self.Track3Graph.setObjectName("Track3Graph")
        self.TrackSynGen1 = QtWidgets.QFrame(self.Mainframe)
        self.TrackSynGen1.setGeometry(QtCore.QRect(680, 70, 151, 551))
        self.TrackSynGen1.setAutoFillBackground(True)
        self.TrackSynGen1.setFrameShape(QtWidgets.QFrame.Box)
        self.TrackSynGen1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TrackSynGen1.setObjectName("TrackSynGen1")
        self.GenSyn1Graph = PlotWidget(self.TrackSynGen1)
        self.GenSyn1Graph.setGeometry(QtCore.QRect(0, 0, 151, 551))
        self.GenSyn1Graph.setObjectName("GenSyn1Graph")
        self.synthethic_options_frame = QtWidgets.QFrame(self.centralwidget)
        self.synthethic_options_frame.setEnabled(False)
        self.synthethic_options_frame.setGeometry(QtCore.QRect(10, 650, 859, 141))
        self.synthethic_options_frame.setAcceptDrops(False)
        self.synthethic_options_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.synthethic_options_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.synthethic_options_frame.setObjectName("synthethic_options_frame")
        self.Wavelet_Title = QtWidgets.QLabel(self.synthethic_options_frame)
        self.Wavelet_Title.setGeometry(QtCore.QRect(391, 12, 46, 16))
        self.Wavelet_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Wavelet_Title.setObjectName("Wavelet_Title")
        self.wave_length_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.wave_length_label.setGeometry(QtCore.QRect(12, 38, 69, 16))
        self.wave_length_label.setObjectName("wave_length_label")
        self.wave_type_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.wave_type_label.setGeometry(QtCore.QRect(12, 72, 28, 16))
        self.wave_type_label.setObjectName("wave_type_label")
        self.wave_type_comboBox = QtWidgets.QComboBox(self.synthethic_options_frame)
        self.wave_type_comboBox.setGeometry(QtCore.QRect(88, 74, 73, 22))
        self.wave_type_comboBox.setObjectName("wave_type_comboBox")
        self.wave_type_comboBox.addItem("")
        self.wave_type_comboBox.addItem("")
        self.wave_length_comboBox = QtWidgets.QComboBox(self.synthethic_options_frame)
        self.wave_length_comboBox.setGeometry(QtCore.QRect(88, 40, 73, 22))
        self.wave_length_comboBox.setObjectName("wave_length_comboBox")
        self.wave_length_comboBox.addItem("")
        self.wave_length_comboBox.addItem("")
        self.wave_length_comboBox.addItem("")
        self.LCF_slider = QtWidgets.QSlider(self.synthethic_options_frame)
        self.LCF_slider.setGeometry(QtCore.QRect(229, 38, 84, 27))
        self.LCF_slider.setMinimum(1)
        self.LCF_slider.setMaximum(100)
        self.LCF_slider.setProperty("value", 10)
        self.LCF_slider.setOrientation(QtCore.Qt.Horizontal)
        self.LCF_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.LCF_slider.setObjectName("LCF_slider")
        self.LPF_slider = QtWidgets.QSlider(self.synthethic_options_frame)
        self.LPF_slider.setGeometry(QtCore.QRect(229, 72, 84, 27))
        self.LPF_slider.setMinimum(1)
        self.LPF_slider.setMaximum(100)
        self.LPF_slider.setProperty("value", 20)
        self.LPF_slider.setOrientation(QtCore.Qt.Horizontal)
        self.LPF_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.LPF_slider.setObjectName("LPF_slider")
        self.LCF_LCD = QtWidgets.QLCDNumber(self.synthethic_options_frame)
        self.LCF_LCD.setGeometry(QtCore.QRect(320, 38, 64, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LCF_LCD.setFont(font)
        self.LCF_LCD.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LCF_LCD.setLineWidth(1)
        self.LCF_LCD.setMidLineWidth(0)
        self.LCF_LCD.setProperty("intValue", 10)
        self.LCF_LCD.setObjectName("LCF_LCD")
        self.LPF_LCD = QtWidgets.QLCDNumber(self.synthethic_options_frame)
        self.LPF_LCD.setGeometry(QtCore.QRect(320, 72, 64, 23))
        self.LPF_LCD.setProperty("intValue", 20)
        self.LPF_LCD.setObjectName("LPF_LCD")
        self.LCF_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.LCF_label.setGeometry(QtCore.QRect(168, 38, 54, 16))
        self.LCF_label.setObjectName("LCF_label")
        self.LPF_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.LPF_label.setGeometry(QtCore.QRect(168, 72, 53, 16))
        self.LPF_label.setObjectName("LPF_label")
        self.HPF_LCD = QtWidgets.QLCDNumber(self.synthethic_options_frame)
        self.HPF_LCD.setGeometry(QtCore.QRect(545, 38, 64, 23))
        self.HPF_LCD.setProperty("intValue", 40)
        self.HPF_LCD.setObjectName("HPF_LCD")
        self.HCF_LCD = QtWidgets.QLCDNumber(self.synthethic_options_frame)
        self.HCF_LCD.setGeometry(QtCore.QRect(545, 72, 64, 23))
        self.HCF_LCD.setProperty("intValue", 50)
        self.HCF_LCD.setObjectName("HCF_LCD")
        self.HPF_slider = QtWidgets.QSlider(self.synthethic_options_frame)
        self.HPF_slider.setGeometry(QtCore.QRect(454, 38, 84, 27))
        self.HPF_slider.setMinimum(2)
        self.HPF_slider.setMaximum(100)
        self.HPF_slider.setProperty("value", 40)
        self.HPF_slider.setOrientation(QtCore.Qt.Horizontal)
        self.HPF_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.HPF_slider.setObjectName("HPF_slider")
        self.HCF_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.HCF_label.setGeometry(QtCore.QRect(391, 72, 56, 16))
        self.HCF_label.setObjectName("HCF_label")
        self.HCF_slider = QtWidgets.QSlider(self.synthethic_options_frame)
        self.HCF_slider.setGeometry(QtCore.QRect(454, 72, 84, 27))
        self.HCF_slider.setMinimum(3)
        self.HCF_slider.setMaximum(100)
        self.HCF_slider.setProperty("value", 50)
        self.HCF_slider.setOrientation(QtCore.Qt.Horizontal)
        self.HCF_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.HCF_slider.setObjectName("HCF_slider")
        self.HPF_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.HPF_label.setGeometry(QtCore.QRect(391, 38, 55, 16))
        self.HPF_label.setObjectName("HPF_label")
        self.Amp_LCD = QtWidgets.QLCDNumber(self.synthethic_options_frame)
        self.Amp_LCD.setGeometry(QtCore.QRect(783, 38, 64, 23))
        self.Amp_LCD.setProperty("intValue", 1)
        self.Amp_LCD.setObjectName("Amp_LCD")
        self.Phase_LCD = QtWidgets.QLCDNumber(self.synthethic_options_frame)
        self.Phase_LCD.setGeometry(QtCore.QRect(783, 72, 64, 23))
        self.Phase_LCD.setObjectName("Phase_LCD")
        self.Amp_slider = QtWidgets.QSlider(self.synthethic_options_frame)
        self.Amp_slider.setGeometry(QtCore.QRect(692, 38, 84, 27))
        self.Amp_slider.setMinimum(1)
        self.Amp_slider.setMaximum(6)
        self.Amp_slider.setPageStep(1)
        self.Amp_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Amp_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Amp_slider.setObjectName("Amp_slider")
        self.Phase_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.Phase_label.setGeometry(QtCore.QRect(616, 72, 69, 16))
        self.Phase_label.setObjectName("Phase_label")
        self.Phase_slider = QtWidgets.QSlider(self.synthethic_options_frame)
        self.Phase_slider.setGeometry(QtCore.QRect(692, 72, 84, 27))
        self.Phase_slider.setMaximum(360)
        self.Phase_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Phase_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Phase_slider.setTickInterval(30)
        self.Phase_slider.setObjectName("Phase_slider")
        self.Amplitude_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.Amplitude_label.setGeometry(QtCore.QRect(616, 38, 57, 16))
        self.Amplitude_label.setObjectName("Amplitude_label")
        self.Create_Synthetic = QtWidgets.QPushButton(self.synthethic_options_frame)
        self.Create_Synthetic.setGeometry(QtCore.QRect(702, 100, 121, 28))
        self.Create_Synthetic.setObjectName("Create_Synthetic")
        self.LCF_checkBox = QtWidgets.QCheckBox(self.synthethic_options_frame)
        self.LCF_checkBox.setGeometry(QtCore.QRect(190, 100, 101, 20))
        self.LCF_checkBox.setObjectName("LCF_checkBox")
        self.LCF_multiplier = QtWidgets.QLineEdit(self.synthethic_options_frame)
        self.LCF_multiplier.setGeometry(QtCore.QRect(320, 100, 61, 22))
        self.LCF_multiplier.setObjectName("LCF_multiplier")
        self.HPF_multiplier = QtWidgets.QLineEdit(self.synthethic_options_frame)
        self.HPF_multiplier.setGeometry(QtCore.QRect(550, 100, 61, 22))
        self.HPF_multiplier.setObjectName("HPF_multiplier")
        self.HPF_checkbox = QtWidgets.QCheckBox(self.synthethic_options_frame)
        self.HPF_checkbox.setGeometry(QtCore.QRect(420, 100, 101, 20))
        self.HPF_checkbox.setObjectName("HPF_checkbox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        self.menuLoad_Data = QtWidgets.QMenu(self.menubar)
        self.menuLoad_Data.setObjectName("menuLoad_Data")
        self.menuGenerate_Synthetic = QtWidgets.QMenu(self.menubar)
        self.menuGenerate_Synthetic.setObjectName("menuGenerate_Synthetic")
        MainWindow.setMenuBar(self.menubar)
        self.actionLoad_Well_1 = QtWidgets.QAction(MainWindow)
        self.actionLoad_Well_1.setObjectName("actionLoad_Well_1")
        self.actionLoad_Well_2 = QtWidgets.QAction(MainWindow)
        self.actionLoad_Well_2.setObjectName("actionLoad_Well_2")
        self.actionLoad_Seismic = QtWidgets.QAction(MainWindow)
        self.actionLoad_Seismic.setObjectName("actionLoad_Seismic")
        self.actionLoad_Well_Tops = QtWidgets.QAction(MainWindow)
        self.actionLoad_Well_Tops.setObjectName("actionLoad_Well_Tops")
        self.gensynwell_1 = QtWidgets.QAction(MainWindow)
        self.gensynwell_1.setObjectName("gensynwell_1")
        self.gensynwell_2 = QtWidgets.QAction(MainWindow)
        self.gensynwell_2.setObjectName("gensynwell_2")
        self.menuLoad_Data.addAction(self.actionLoad_Well_1)
        self.menuLoad_Data.addAction(self.actionLoad_Well_2)
        self.menuLoad_Data.addAction(self.actionLoad_Seismic)
        self.menuLoad_Data.addAction(self.actionLoad_Well_Tops)
        self.menuGenerate_Synthetic.addAction(self.gensynwell_1)
        self.menuGenerate_Synthetic.addAction(self.gensynwell_2)
        self.menubar.addAction(self.menuLoad_Data.menuAction())
        self.menubar.addAction(self.menuGenerate_Synthetic.menuAction())

        self.retranslateUi(MainWindow)
        self.LCF_slider.valueChanged['int'].connect(self.LCF_LCD.display)
        self.LPF_slider.valueChanged['int'].connect(self.LPF_LCD.display)
        self.HPF_slider.valueChanged['int'].connect(self.HPF_LCD.display)
        self.HCF_slider.valueChanged['int'].connect(self.HCF_LCD.display)
        self.Amp_slider.valueChanged['int'].connect(self.Amp_LCD.display)
        self.Phase_slider.valueChanged['int'].connect(self.Phase_LCD.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        # All data loading parameters for well 1 -- Note: must have self.variable name to initializa the variable
        self.well1name = '' #UWI
        self.dlog_start1 = 0 # depth of loggin start for well 1
        self.well1kb = 0
        self.dblwseisdat1 = 0 # distance below seismic datum 
        self.log_start_time1 = 0 # well 1 log start time (TWT units:s)
        self.well1 = [] # well 1 data 
        self.well1df = []
        self.seis_dat = [] # seismic datum 
        self.repl_vel = [] # seismic velocity 
        self.havesonic1 = False
        self.havedensity1 = False
        self.densitymnemonic1 = None
        self.sonicmnemonic1 = None
        
        
        
        # All data for synthetic generation for well1 
        self.well1df_tdom= None      
        #connection to loading well 1
        #self.actionLoad_Well_1.triggered.connect(lambda : self.setattribute(self.loadwell1))
        self.actionLoad_Well_1.triggered.connect(self.loadwell1)
        #connection to plot data  - well 1 track 1
        self.comboBox_Track1.activated.connect(lambda : self.plotw1t1(self.well1,self.well1df,self.seis_data,self.repl_vel,self.well1df_tdom))
        self.comboBox_Track2.activated.connect(lambda : self.plotw1t2(self.well1,self.well1df,self.seis_data,self.repl_vel,self.well1df_tdom))
        self.comboBox_Track3.activated.connect(lambda : self.plotw1t3(self.well1,self.well1df,self.seis_data,self.repl_vel,self.well1df_tdom))
        
        #connection to generating a synthetic seismogram: 
        self.gensynwell_1.triggered.connect(lambda: self.gensynaction1(self.havesonic1,self.havedensity1,self.well1,self.well1df))
        
                             
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Well_info_label.setText(_translate("MainWindow", "Well Name"))
        self.Track1dropdown.setText(_translate("MainWindow", "Track 1"))
        self.Track2dropdown.setText(_translate("MainWindow", "Track 2"))
        self.Track3dropdown.setText(_translate("MainWindow", "Track 3"))
        self.label_track1.setText(_translate("MainWindow", "Track 1"))
        self.label_track2.setText(_translate("MainWindow", "Track 2"))
        self.label_track3.setText(_translate("MainWindow", "Track 3"))
        self.label_track_syngen1.setText(_translate("MainWindow", "Generated Synthetic 1"))
        self.wavelet_plot_title.setText(_translate("MainWindow", "Wavelet Plot"))
        self.Wavelet_Title.setText(_translate("MainWindow", "Wavelet"))
        self.wave_length_label.setText(_translate("MainWindow", "Length (ms)"))
        self.wave_type_label.setText(_translate("MainWindow", "Type"))
        self.wave_type_comboBox.setItemText(0, _translate("MainWindow", "Ricker"))
        self.wave_type_comboBox.setItemText(1, _translate("MainWindow", "Ormsby"))
        self.wave_length_comboBox.setItemText(0, _translate("MainWindow", "128"))
        self.wave_length_comboBox.setItemText(1, _translate("MainWindow", "256"))
        self.wave_length_comboBox.setItemText(2, _translate("MainWindow", "512"))
        self.LCF_label.setText(_translate("MainWindow", "LCF (Hz):"))
        self.LPF_label.setText(_translate("MainWindow", "LPF (Hz):"))
        self.HCF_label.setText(_translate("MainWindow", "HCF (Hz):"))
        self.HPF_label.setText(_translate("MainWindow", "HPF (Hz):"))
        self.Phase_label.setText(_translate("MainWindow", "Phase (deg)"))
        self.Amplitude_label.setText(_translate("MainWindow", "Amplitude"))
        self.Create_Synthetic.setText(_translate("MainWindow", "Create Synthetic"))
        self.LCF_checkBox.setText(_translate("MainWindow", "LCF Multiple"))
        self.LCF_multiplier.setText(_translate("MainWindow", "1.5"))
        self.HPF_multiplier.setText(_translate("MainWindow", "1.5"))
        self.HPF_checkbox.setText(_translate("MainWindow", "HPF Multiple"))
        self.menuLoad_Data.setTitle(_translate("MainWindow", "Load Data"))
        self.menuGenerate_Synthetic.setTitle(_translate("MainWindow", "Generate Synthetic"))
        self.actionLoad_Well_1.setText(_translate("MainWindow", "Load Well 1"))
        self.actionLoad_Well_2.setText(_translate("MainWindow", "Load Well 2"))
        self.actionLoad_Seismic.setText(_translate("MainWindow", "Load Seismic"))
        self.actionLoad_Well_Tops.setText(_translate("MainWindow", "Load Well Tops"))
        self.gensynwell_1.setText(_translate("MainWindow", "Well 1"))
        self.gensynwell_2.setText(_translate("MainWindow", "Well 2"))
        
        #method to load well 1
    def loadwell1(self):
        #file location 
        floc = QFileDialog.getOpenFileName(None, 'Open File', 'C:\ ')
        #setup to laad the well into a data frame using the LAS library 
        w1 = Well.from_las(floc[0]) 
        
        #data that contains all 
        data = tdinfo()
        seis_dat, repl_vel = data.getInputs()
        seis_dat = float(seis_dat)
        repl_vel = float(repl_vel) 
        
        mnemonics = w1._get_curve_mnemonics()
        
        ### Ask for Despiking and smoothing of Density and Sonic data here 
        
        ### Ask User to select the appropriate sonic and density logs -> to later create a synthetic 
        chosen_sonic = False
        sonic_mnemonics = None
        havesonic = False
        
        chosen_density = False
        density_mnemonics = None
        havedensity = False 
        
        ### Automatically Select the sonic based on the given mnmemonics
        soniclist = ['DT', 'DTC', 'DTCO', 'DTCOMP', 'DELTAT', 'SLOW', 'SLOWNESS', 'TT', 'TIME', 'TIM', 'ITT', 'DTCQI', 'DTCR', 'DTCREP', 'DTCS', 'DTCSG', 'DTCU', 'DTCV0', 'DTCX', 'DTL', 'DTP', 'DTR', 'DTTP', 'DTU', 'DTUM', 'CTIME', 'COTIME', 'COMT', 'DT1A', 'DT1B', 'DT34', 'DT35', 'DT3A', 'DT3B', 'DT45', 'DT46', 'DT56', 'DTC1', 'DTC2', 'DTC3', 'DTCM', 'AC', 'ACCO', 'DELT', 'ACL', 'ACN', 'DT24', 'DT24QI', 'DT24SQA', 'DT41', 'DT4P', 'DT5', 'DTMN', 'DTMX', 'DTSC', 'TTC', 'AC1', 'MSTT', 'DtComp']
        
        if chosen_sonic == False:
            for i in soniclist:
                if i in mnemonics:
                    sonic_mnemonics = i 
                    #print(i)
                    havesonic = True
                    self.havesonic1 = True
                    dt = w1.data[sonic_mnemonics].values # assuming us/m 
                    #print(dt)
                    depth_increment = w1.data[sonic_mnemonics].step # for time-depth relationship 
                    dlog_start = w1.data[sonic_mnemonics].start
                    #print(depth_increment,dlog_start)
        #print(havesonic, sonic_mnemonics) -> validation that filter works
        ###   Automatically Select the density based on the given mnmemonics  
        densitylist = ['RHOB','RHOZ', 'DEN']
        
        if chosen_density == False: 
            for i in densitylist: 
                if i in mnemonics:
                    density_mnemonics = i 
                    havedensity = True
                    self.havedensity1 = True 
        
        w1df = w1.df()
        ## Establishing Time-Depth Relationship 
        ### Determining the depth of log_start (where loggin of data begins) 
        #dlog_start = w1df[mnemonics[0]].keys()[0]
        ### Determining the distance below the seismic datum 
        # Seismic_Datum-Kelly Bushing+log_start = distance below seismic datum 
        dblwseisdat1 = seis_dat-w1.location.ekb+dlog_start 
        self.dblwseisdat1 = dblwseisdat1
        #Log start time (s)
        log_start_time1 = (dblwseisdat1/repl_vel)*2 #have to multiply by 2 b/c of TWT 
        self.log_start_time1 = log_start_time1
        
        
        if havesonic == True:
            dt_iterval = np.nan_to_num(dt)*depth_increment/1e6 
            t_cum = np.cumsum(dt_iterval)*2 #*2 for two way time 
            TWT = t_cum + log_start_time1
            w1df['TWT'] = TWT 
            mnemonics.append('TWT')
            
            #print(t_cum + log_start_time1)
            #print(w1df['TWT'])
        
        # acoustic impedance: 
        if havesonic == True and havedensity == True: 
            #sonic velocity calculate: 
            w1df['Vsonic']=1e6/w1df[sonic_mnemonics].values #units transformed to m/s
            #adding 'Vsonic' to the mnemonics: 
            mnemonics.append('Vsonic')
            #calculatin the Acoustic Impedance
            w1df['AI'] = w1df['Vsonic'].values*w1df[density_mnemonics].values
            #adding 'AI' to the mnemonics: 
            mnemonics.append('AI')
            #calculation of the reflection coefficient 
            Imp = w1df['AI'].values
            Rc = []
            for i in range(len(Imp)-1):
                Rc.append((Imp[i+1]-Imp[i])/(Imp[i]+Imp[i+1])) 
            
            # to adjust vector size copy the last element to the tail
            Rc.append(Rc[-1])
            
            # Let's add Rc into dataframe as new column
            w1df['Rc'] = pd.Series(Rc, index=w1df.index)
            
            mnemonics.append('Rc')
        
        
        #### repopulating data parameters ####
        self.well1 = w1
        self.well1df = w1df
        #print(w1.data[sonic_mnemonics].basis_units) 
        #print(w1.curve[sonic_mnemonics].units)
        self.seis_data = seis_dat
        self.repl_vel = repl_vel
        
        
        self.dlog_start1 = dlog_start # depth of data loggin start 
        
        ### Determining KB from data
        self.well1kb = w1.location.ekb
        
        #####data manipulation for data processing ######
        
        
         
        #connection to populate combo boxes 
        self.popcombobox(mnemonics) 
        
        #print(self.havesonic1,self.havedensity1)
        
        
   

        #method to populate combobox data 
    def popcombobox(self,well_attr): 
        mnemonics = well_attr
        self.comboBox_Track1.addItems(mnemonics)
        self.comboBox_Track2.addItems(mnemonics)
        self.comboBox_Track3.addItems(mnemonics)
        
        
        # method to plot data in Track 1 
    def plotw1t1(self,well1,well1df,seis_dat,repl_vel,well1df_tdom):
        
        self.Track1Graph.clear()
        sel_data = self.comboBox_Track1.currentText()
        #section for only plotting data in tdom 
        tdom_data = ['AI_tdom1','Rc_tdom1']
        if sel_data in tdom_data:
            dplot = well1df_tdom[sel_data]
        else: 
            dplot = well1df[sel_data]
        y = dplot.values #[2,4,6,8,10,math.nan]#
        x = dplot.index.values#[1,2,3,4,5,6]#
        
        # for loop to handle nan values 
        for i in range(len(y)):
            if math.isnan(y[i]) == True :
                y[i] = 0 
                #print(y[i])
                
        
        self.Track1Graph.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        trackplot = pg.PlotCurveItem(y,x,connect='finite',pen=(255, 0, 0))
        self.Track1Graph.addItem(trackplot)
        self.Track1Graph.invertY(True)
        self.Track1Graph.showGrid(x=True,y=True)
        
        
    # method to plot theh data in Track 2    
    def plotw1t2(self,well1,well1df,seis_dat,repl_vel,well1df_tdom):
        self.Track2Graph.clear()
        sel_data = self.comboBox_Track2.currentText()
        tdom_data = ['AI_tdom1','Rc_tdom1']
        if sel_data in tdom_data:
            dplot = well1df_tdom[sel_data]
        else: 
            dplot = well1df[sel_data]
        y = dplot.values #[2,4,6,8,10,math.nan]#
        x = dplot.index.values#[1,2,3,4,5,6]#
        # for loop to handle nan values 
        for i in range(len(y)):
            if math.isnan(y[i]) == True :
                y[i] = 0 
                #print(y[i])
        self.Track2Graph.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        trackplot = pg.PlotCurveItem(y,x,connect='finite',pen=(255, 0, 0))
        self.Track2Graph.addItem(trackplot)
        self.Track2Graph.invertY(True)
        self.Track2Graph.showGrid(x=True,y=True)
      
    # method to plot theh data in Track 3    
    def plotw1t3(self,well1,well1df,seis_dat,repl_vel,well1df_tdom):
        self.Track3Graph.clear()
        sel_data = self.comboBox_Track3.currentText()
        tdom_data = ['AI_tdom1','Rc_tdom1']
        if sel_data in tdom_data:
            dplot = well1df_tdom[sel_data]
        else: 
            dplot = well1df[sel_data]
        y = dplot.values 
        x = dplot.index.values
        # for loop to handle nan values 
        for i in range(len(y)):
            if math.isnan(y[i]) == True :
                y[i] = 0 
                #print(y[i])
        self.Track3Graph.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        trackplot = pg.PlotCurveItem(y,x,connect='finite',pen=(255, 0, 0))
        self.Track3Graph.addItem(trackplot)
        self.Track3Graph.invertY(True)
        self.Track3Graph.showGrid(x=True,y=True)

    
    
    # action to generate a synthetic for well 1 
    def gensynaction1(self,havesonic,havedensity,well1,well1df): #note, AI and RC are automatically calculated already 
        self.wavelet_graph.clear()
        #print(havesonic,havedensity)
        if havesonic == True & havedensity == True:
            data = syninfo()
            dt, t_max, wavelet_type = data.getInputs() # will change once synthetic 
            dt = float(dt)
            t_max = float(t_max)
            #t = well1df['TWT'].values
            #print(t)
            t =  np.arange(0,t_max,dt)# time vector for resampling based on t and dt -> can get TWT from 
            print(well1df['TWT'].values)
            print("")
            AI = well1df.AI.values
            for i in range(len(AI)):
                if math.isnan(AI[i]) == True :
                    AI[i] = 0
            
            for i in range(len(AI)):
                if AI[i] == 0 :
                    AI[i] = np.mean(AI)
            
            print(AI)
            AI_tdom = np.interp(x=t,xp=well1df['TWT'].values,fp=AI)    #resampling to time domain via interpolation 
            import matplotlib.pyplot as plt
            plt.plot(AI_tdom,t)
            plt.show()
            #print(AI_tdom, sep='\n')
            '''
            for i in range(len(AI_tdom)):
                    if math.isnan(AI_tdom[i]) == True :
                        AI_tdom[i] = 0
            #print(AI_tdom, sep='\n')
            '''
            #reflection coefficient in time domain 
            # again Rc calulation but in reampled time domain
            
            Rc_tdom = []
            for i in range(len(AI_tdom)-1):
                Rc_tdom.append((AI_tdom[i+1]-AI_tdom[i])/(AI_tdom[i]+AI_tdom[i+1]))
            # to adjust vector size copy the last element to the tail
            Rc_tdom.append(Rc_tdom[-1])
            plt.plot(Rc_tdom,t)
            plt.show()
            #print(Rc_tdom)
            
            
            #dataframe for plotting items in dataframe 
            tdom_data1 = {'AI_tdom1':AI_tdom,'Rc_tdom1':Rc_tdom}
            well1df_tdom = pd.DataFrame(data =tdom_data1,index=t)
            self.well1df_tdom = well1df_tdom
            self.comboBox_Track1.addItems(['AI_tdom1','Rc_tdom1'])
            self.comboBox_Track2.addItems(['AI_tdom1','Rc_tdom1'])
            self.comboBox_Track3.addItems(['AI_tdom1','Rc_tdom1'])
            
            
            
            '''
            self.t1 = t 
            self.AI_tdom1 = AI_tdom
            self.Rc_tdom1 = Rc_tdom
            '''
            # Ricker Wavelet: 
            if wavelet_type == 'Ricker': 
                ricker_var = rickerinfo()
                wave_len, freq = ricker_var.getInputs()
                wave_len = float(wave_len)
                freq = float(freq) 
                wavelet = bg.filters.wavelets.ricker(wave_len, dt, freq, t=None, return_t=True, sym=True)
                print(wavelet)
                #plotting of wavelet
                wavexplot = wavelet.time
                waveyplot = wavelet.amplitude
                trackplot = pg.PlotCurveItem(wavexplot,waveyplot,connect='finite',pen=(255, 0, 0))
                self.wavelet_graph.addItem(trackplot)
                
                #convolution of data
                 
                for i in range(len(Rc_tdom)):
                    if math.isnan(Rc_tdom[i]) == True :
                        Rc_tdom[i] = 0
                synthetic = np.convolve(wavelet.amplitude, Rc_tdom, mode = 'same')
                #print(synthetic)
                self.GenSyn1Graph.setBackground('w')
                pen = pg.mkPen(color=(255, 0, 0))
                trackplot = pg.PlotCurveItem(synthetic,t,connect='finite',pen=(255, 0, 0))
                self.GenSyn1Graph.addItem(trackplot)
                self.GenSyn1Graph.invertY(True)
                self.GenSyn1Graph.showGrid(x=True,y=True)
                
                
            ## Other wavelets @ https://code.agilescientific.com/bruges/api/bruges.filters.html#module-bruges.filters.wavelets
        elif (havesonic == True) & (havedensity == False): 
            print("Please load a well with a valid density log")
        elif (havesonic == False) & (havedensity == True): 
            print("Please load a well with a valid sonic log")
        else: 
            print("Please load a well with a valid sonic and density log")
       

    #Dialog to determine and acquire seismic datum and replacement velocity
class tdinfo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.first = QLineEdit(self)
        self.first.setText("800")
        self.second = QLineEdit(self)
        self.second.setText("2300")
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);

        layout = QFormLayout(self)
        layout.addRow("Seismic Datum [m]", self.first)
        layout.addRow("Replacement Velocity [m/s]", self.second)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        #self.NonModal(True)
        self.exec()
    #Method to return the input 
    def getInputs(self):
        return [self.first.text(), self.second.text()]
    
    
    #Dialog to determine sampling interval, maximum time, amd type of wavelet (synthetic info 
class syninfo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.first = QLineEdit(self)
        self.first.setText("0.001")
        self.second = QLineEdit(self)
        self.second.setText("1")
        self.third = QtWidgets.QComboBox(self)
        waveletlist = ['Ricker','Ormsby']
        # https://code.agilescientific.com/bruges/api/bruges.filters.html#module-bruges.filters.wavelets -> other wavelets to be implemented 
        self.third.addItems(waveletlist)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);

        layout = QFormLayout(self)
        layout.addRow("Time Interval (s)", self.first)
        layout.addRow("Max Time (s)", self.second)
        layout.addRow("wavelet Type",self.third)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        #self.NonModal(True)
        self.exec()
    #Method to return the input 
    def getInputs(self):
        return [self.first.text(), self.second.text(), self.third.currentText()]
    
    
class rickerinfo(QDialog): 
    def __init__(self, parent=None):
        super().__init__(parent)

        self.first = QLineEdit(self)
        self.first.setText("0.256")
        self.second = QLineEdit(self)
        self.second.setText("20")
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);

        layout = QFormLayout(self)
        layout.addRow("Wavelet Length (s)", self.first)
        layout.addRow("Frequency (Hz)", self.second)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        #self.NonModal(True)
        self.exec()
    #Method to return the input 
    def getInputs(self):
        return [self.first.text(), self.second.text()]
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
