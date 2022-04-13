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
        MainWindow.resize(1852, 851)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Mainframe_well1 = QtWidgets.QFrame(self.centralwidget)
        self.Mainframe_well1.setGeometry(QtCore.QRect(10, 10, 841, 641))
        self.Mainframe_well1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Mainframe_well1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Mainframe_well1.setObjectName("Mainframe_well1")
        self.wellinfoframe = QtWidgets.QFrame(self.Mainframe_well1)
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
        self.Track1Frame = QtWidgets.QFrame(self.Mainframe_well1)
        self.Track1Frame.setGeometry(QtCore.QRect(200, 70, 151, 571))
        self.Track1Frame.setAutoFillBackground(True)
        self.Track1Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.Track1Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Track1Frame.setObjectName("Track1Frame")
        self.Track1Graph = PlotWidget(self.Track1Frame)
        self.Track1Graph.setGeometry(QtCore.QRect(0, 0, 151, 571))
        self.Track1Graph.setObjectName("Track1Graph")
        self.label_track1 = QtWidgets.QLabel(self.Mainframe_well1)
        self.label_track1.setGeometry(QtCore.QRect(250, 50, 55, 16))
        self.label_track1.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_track1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_track1.setObjectName("label_track1")
        self.label_track2 = QtWidgets.QLabel(self.Mainframe_well1)
        self.label_track2.setGeometry(QtCore.QRect(410, 50, 55, 16))
        self.label_track2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_track2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_track2.setObjectName("label_track2")
        self.label_track3 = QtWidgets.QLabel(self.Mainframe_well1)
        self.label_track3.setGeometry(QtCore.QRect(570, 50, 55, 16))
        self.label_track3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_track3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_track3.setObjectName("label_track3")
        self.label_track_syngen1 = QtWidgets.QLabel(self.Mainframe_well1)
        self.label_track_syngen1.setGeometry(QtCore.QRect(700, 30, 111, 31))
        self.label_track_syngen1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_track_syngen1.setScaledContents(False)
        self.label_track_syngen1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_track_syngen1.setWordWrap(True)
        self.label_track_syngen1.setObjectName("label_track_syngen1")
        self.Synthetic_Graph_Widget = QtWidgets.QWidget(self.Mainframe_well1)
        self.Synthetic_Graph_Widget.setGeometry(QtCore.QRect(0, 340, 181, 301))
        self.Synthetic_Graph_Widget.setObjectName("Synthetic_Graph_Widget")
        self.wavelet_graph = PlotWidget(self.Synthetic_Graph_Widget)
        self.wavelet_graph.setGeometry(QtCore.QRect(0, 30, 181, 271))
        self.wavelet_graph.setObjectName("wavelet_graph")
        self.wavelet_plot_title = QtWidgets.QLabel(self.Synthetic_Graph_Widget)
        self.wavelet_plot_title.setGeometry(QtCore.QRect(50, 0, 91, 21))
        self.wavelet_plot_title.setAlignment(QtCore.Qt.AlignCenter)
        self.wavelet_plot_title.setObjectName("wavelet_plot_title")
        self.Track2Frame = QtWidgets.QFrame(self.Mainframe_well1)
        self.Track2Frame.setGeometry(QtCore.QRect(360, 70, 151, 571))
        self.Track2Frame.setAutoFillBackground(True)
        self.Track2Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.Track2Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Track2Frame.setObjectName("Track2Frame")
        self.Track2Graph = PlotWidget(self.Track2Frame)
        self.Track2Graph.setGeometry(QtCore.QRect(0, 0, 151, 571))
        self.Track2Graph.setObjectName("Track2Graph")
        self.Track3Frame = QtWidgets.QFrame(self.Mainframe_well1)
        self.Track3Frame.setGeometry(QtCore.QRect(520, 70, 151, 571))
        self.Track3Frame.setAutoFillBackground(True)
        self.Track3Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.Track3Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Track3Frame.setObjectName("Track3Frame")
        self.Track3Graph = PlotWidget(self.Track3Frame)
        self.Track3Graph.setGeometry(QtCore.QRect(0, 0, 151, 571))
        self.Track3Graph.setObjectName("Track3Graph")
        self.TrackSynGen1 = QtWidgets.QFrame(self.Mainframe_well1)
        self.TrackSynGen1.setGeometry(QtCore.QRect(680, 70, 151, 571))
        self.TrackSynGen1.setAutoFillBackground(True)
        self.TrackSynGen1.setFrameShape(QtWidgets.QFrame.Box)
        self.TrackSynGen1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TrackSynGen1.setObjectName("TrackSynGen1")
        self.GenSyn1Graph = PlotWidget(self.TrackSynGen1)
        self.GenSyn1Graph.setGeometry(QtCore.QRect(0, 0, 151, 571))
        self.GenSyn1Graph.setObjectName("GenSyn1Graph")
        self.synthethic_options_frame = QtWidgets.QFrame(self.centralwidget)
        self.synthethic_options_frame.setEnabled(True)
        self.synthethic_options_frame.setGeometry(QtCore.QRect(10, 650, 1034, 151))
        self.synthethic_options_frame.setAcceptDrops(False)
        self.synthethic_options_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.synthethic_options_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.synthethic_options_frame.setObjectName("synthethic_options_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.synthethic_options_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.LCF_checkBox = QtWidgets.QCheckBox(self.synthethic_options_frame)
        self.LCF_checkBox.setObjectName("LCF_checkBox")
        self.gridLayout.addWidget(self.LCF_checkBox, 3, 2, 1, 2)
        self.Wavelet_Title = QtWidgets.QLabel(self.synthethic_options_frame)
        self.Wavelet_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Wavelet_Title.setObjectName("Wavelet_Title")
        self.gridLayout.addWidget(self.Wavelet_Title, 0, 5, 1, 1)
        self.wave_type_comboBox = QtWidgets.QComboBox(self.synthethic_options_frame)
        self.wave_type_comboBox.setObjectName("wave_type_comboBox")
        self.wave_type_comboBox.addItem("")
        self.wave_type_comboBox.addItem("")
        self.wave_type_comboBox.addItem("")
        self.wave_type_comboBox.addItem("")
        self.gridLayout.addWidget(self.wave_type_comboBox, 0, 1, 1, 1)
        self.Phase_slider = QtWidgets.QSlider(self.synthethic_options_frame)
        self.Phase_slider.setMaximum(360)
        self.Phase_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Phase_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Phase_slider.setTickInterval(30)
        self.Phase_slider.setObjectName("Phase_slider")
        self.gridLayout.addWidget(self.Phase_slider, 2, 9, 1, 1)
        self.HCF_slider = QtWidgets.QSlider(self.synthethic_options_frame)
        self.HCF_slider.setMinimum(3)
        self.HCF_slider.setMaximum(100)
        self.HCF_slider.setProperty("value", 50)
        self.HCF_slider.setOrientation(QtCore.Qt.Horizontal)
        self.HCF_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.HCF_slider.setObjectName("HCF_slider")
        self.gridLayout.addWidget(self.HCF_slider, 2, 6, 1, 1)
        self.Amp_LCD = QtWidgets.QLCDNumber(self.synthethic_options_frame)
        self.Amp_LCD.setProperty("intValue", 1)
        self.Amp_LCD.setObjectName("Amp_LCD")
        self.gridLayout.addWidget(self.Amp_LCD, 1, 10, 1, 1)
        self.wave_length_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.wave_length_label.setObjectName("wave_length_label")
        self.gridLayout.addWidget(self.wave_length_label, 1, 0, 1, 1)
        self.LPF_LCD = QtWidgets.QLCDNumber(self.synthethic_options_frame)
        self.LPF_LCD.setProperty("intValue", 20)
        self.LPF_LCD.setObjectName("LPF_LCD")
        self.gridLayout.addWidget(self.LPF_LCD, 2, 4, 1, 1)
        self.HPF_slider = QtWidgets.QSlider(self.synthethic_options_frame)
        self.HPF_slider.setMinimum(2)
        self.HPF_slider.setMaximum(100)
        self.HPF_slider.setProperty("value", 40)
        self.HPF_slider.setOrientation(QtCore.Qt.Horizontal)
        self.HPF_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.HPF_slider.setObjectName("HPF_slider")
        self.gridLayout.addWidget(self.HPF_slider, 1, 6, 1, 1)
        self.max_time_comboBox = QtWidgets.QComboBox(self.synthethic_options_frame)
        self.max_time_comboBox.setObjectName("max_time_comboBox")
        self.max_time_comboBox.addItem("")
        self.max_time_comboBox.addItem("")
        self.max_time_comboBox.addItem("")
        self.gridLayout.addWidget(self.max_time_comboBox, 2, 1, 1, 1)
        self.Phase_LCD = QtWidgets.QLCDNumber(self.synthethic_options_frame)
        self.Phase_LCD.setObjectName("Phase_LCD")
        self.gridLayout.addWidget(self.Phase_LCD, 2, 10, 1, 1)
        self.max_time_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.max_time_label.setObjectName("max_time_label")
        self.gridLayout.addWidget(self.max_time_label, 2, 0, 1, 1)
        self.LCF_multiplier = QtWidgets.QLineEdit(self.synthethic_options_frame)
        self.LCF_multiplier.setObjectName("LCF_multiplier")
        self.gridLayout.addWidget(self.LCF_multiplier, 3, 4, 1, 1)
        self.Create_Synthetic = QtWidgets.QPushButton(self.synthethic_options_frame)
        self.Create_Synthetic.setObjectName("Create_Synthetic")
        self.gridLayout.addWidget(self.Create_Synthetic, 0, 7, 1, 1)
        self.Amp_slider = QtWidgets.QSlider(self.synthethic_options_frame)
        self.Amp_slider.setMinimum(1)
        self.Amp_slider.setMaximum(6)
        self.Amp_slider.setPageStep(1)
        self.Amp_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Amp_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Amp_slider.setObjectName("Amp_slider")
        self.gridLayout.addWidget(self.Amp_slider, 1, 9, 1, 1)
        self.HCF_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.HCF_label.setObjectName("HCF_label")
        self.gridLayout.addWidget(self.HCF_label, 2, 5, 1, 1)
        self.HPF_LCD = QtWidgets.QLCDNumber(self.synthethic_options_frame)
        self.HPF_LCD.setProperty("intValue", 40)
        self.HPF_LCD.setObjectName("HPF_LCD")
        self.gridLayout.addWidget(self.HPF_LCD, 1, 7, 1, 1)
        self.LPF_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.LPF_label.setObjectName("LPF_label")
        self.gridLayout.addWidget(self.LPF_label, 2, 2, 1, 1)
        self.sample_rate_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.sample_rate_label.setObjectName("sample_rate_label")
        self.gridLayout.addWidget(self.sample_rate_label, 3, 0, 1, 1)
        self.sample_rate_comboBox = QtWidgets.QComboBox(self.synthethic_options_frame)
        self.sample_rate_comboBox.setObjectName("sample_rate_comboBox")
        self.sample_rate_comboBox.addItem("")
        self.sample_rate_comboBox.addItem("")
        self.sample_rate_comboBox.addItem("")
        self.gridLayout.addWidget(self.sample_rate_comboBox, 3, 1, 1, 1)
        self.LPF_slider = QtWidgets.QSlider(self.synthethic_options_frame)
        self.LPF_slider.setMinimum(1)
        self.LPF_slider.setMaximum(100)
        self.LPF_slider.setProperty("value", 20)
        self.LPF_slider.setOrientation(QtCore.Qt.Horizontal)
        self.LPF_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.LPF_slider.setObjectName("LPF_slider")
        self.gridLayout.addWidget(self.LPF_slider, 2, 3, 1, 1)
        self.Amplitude_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.Amplitude_label.setObjectName("Amplitude_label")
        self.gridLayout.addWidget(self.Amplitude_label, 1, 8, 1, 1)
        self.HPF_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.HPF_label.setObjectName("HPF_label")
        self.gridLayout.addWidget(self.HPF_label, 1, 5, 1, 1)
        self.LCF_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.LCF_label.setObjectName("LCF_label")
        self.gridLayout.addWidget(self.LCF_label, 1, 2, 1, 1)
        self.HPF_checkbox = QtWidgets.QCheckBox(self.synthethic_options_frame)
        self.HPF_checkbox.setObjectName("HPF_checkbox")
        self.gridLayout.addWidget(self.HPF_checkbox, 3, 5, 1, 2)
        self.wave_length_comboBox = QtWidgets.QComboBox(self.synthethic_options_frame)
        self.wave_length_comboBox.setObjectName("wave_length_comboBox")
        self.wave_length_comboBox.addItem("")
        self.wave_length_comboBox.addItem("")
        self.wave_length_comboBox.addItem("")
        self.gridLayout.addWidget(self.wave_length_comboBox, 1, 1, 1, 1)
        self.Phase_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.Phase_label.setObjectName("Phase_label")
        self.gridLayout.addWidget(self.Phase_label, 2, 8, 1, 1)
        self.HCF_LCD = QtWidgets.QLCDNumber(self.synthethic_options_frame)
        self.HCF_LCD.setProperty("intValue", 50)
        self.HCF_LCD.setObjectName("HCF_LCD")
        self.gridLayout.addWidget(self.HCF_LCD, 2, 7, 1, 1)
        self.wave_type_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.wave_type_label.setObjectName("wave_type_label")
        self.gridLayout.addWidget(self.wave_type_label, 0, 0, 1, 1)
        self.LCF_slider = QtWidgets.QSlider(self.synthethic_options_frame)
        self.LCF_slider.setEnabled(True)
        self.LCF_slider.setMinimum(1)
        self.LCF_slider.setMaximum(100)
        self.LCF_slider.setProperty("value", 10)
        self.LCF_slider.setOrientation(QtCore.Qt.Horizontal)
        self.LCF_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.LCF_slider.setObjectName("LCF_slider")
        self.gridLayout.addWidget(self.LCF_slider, 1, 3, 1, 1)
        self.HPF_multiplier = QtWidgets.QLineEdit(self.synthethic_options_frame)
        self.HPF_multiplier.setObjectName("HPF_multiplier")
        self.gridLayout.addWidget(self.HPF_multiplier, 3, 7, 1, 1)
        self.LCF_LCD = QtWidgets.QLCDNumber(self.synthethic_options_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LCF_LCD.setFont(font)
        self.LCF_LCD.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LCF_LCD.setLineWidth(1)
        self.LCF_LCD.setMidLineWidth(0)
        self.LCF_LCD.setProperty("intValue", 10)
        self.LCF_LCD.setObjectName("LCF_LCD")
        self.gridLayout.addWidget(self.LCF_LCD, 1, 4, 1, 1)
        self.wavelet_well_sel_label = QtWidgets.QLabel(self.synthethic_options_frame)
        self.wavelet_well_sel_label.setObjectName("wavelet_well_sel_label")
        self.gridLayout.addWidget(self.wavelet_well_sel_label, 0, 8, 1, 1)
        self.wavelet_well_sel_comboBox = QtWidgets.QComboBox(self.synthethic_options_frame)
        self.wavelet_well_sel_comboBox.setObjectName("wavelet_well_sel_comboBox")
        self.wavelet_well_sel_comboBox.addItem("")
        self.wavelet_well_sel_comboBox.addItem("")
        self.gridLayout.addWidget(self.wavelet_well_sel_comboBox, 0, 9, 1, 1)
        self.Mainframe_2 = QtWidgets.QFrame(self.centralwidget)
        self.Mainframe_2.setGeometry(QtCore.QRect(870, 10, 861, 641))
        self.Mainframe_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Mainframe_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Mainframe_2.setObjectName("Mainframe_2")
        self.label_track2_2 = QtWidgets.QLabel(self.Mainframe_2)
        self.label_track2_2.setGeometry(QtCore.QRect(380, 50, 55, 16))
        self.label_track2_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_track2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_track2_2.setObjectName("label_track2_2")
        self.label_track3_2 = QtWidgets.QLabel(self.Mainframe_2)
        self.label_track3_2.setGeometry(QtCore.QRect(220, 50, 55, 16))
        self.label_track3_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_track3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_track3_2.setObjectName("label_track3_2")
        self.label_track_syngen_2 = QtWidgets.QLabel(self.Mainframe_2)
        self.label_track_syngen_2.setGeometry(QtCore.QRect(30, 30, 111, 31))
        self.label_track_syngen_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_track_syngen_2.setScaledContents(False)
        self.label_track_syngen_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_track_syngen_2.setWordWrap(True)
        self.label_track_syngen_2.setObjectName("label_track_syngen_2")
        self.Track2Frame_2 = QtWidgets.QFrame(self.Mainframe_2)
        self.Track2Frame_2.setGeometry(QtCore.QRect(330, 70, 151, 571))
        self.Track2Frame_2.setAutoFillBackground(True)
        self.Track2Frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.Track2Frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Track2Frame_2.setObjectName("Track2Frame_2")
        self.Track2Graph_2 = PlotWidget(self.Track2Frame_2)
        self.Track2Graph_2.setGeometry(QtCore.QRect(0, 0, 151, 571))
        self.Track2Graph_2.setObjectName("Track2Graph_2")
        self.Track3Frame_2 = QtWidgets.QFrame(self.Mainframe_2)
        self.Track3Frame_2.setGeometry(QtCore.QRect(170, 70, 151, 571))
        self.Track3Frame_2.setAutoFillBackground(True)
        self.Track3Frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.Track3Frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Track3Frame_2.setObjectName("Track3Frame_2")
        self.Track3Graph_2 = PlotWidget(self.Track3Frame_2)
        self.Track3Graph_2.setGeometry(QtCore.QRect(0, 0, 151, 571))
        self.Track3Graph_2.setObjectName("Track3Graph_2")
        self.TrackSynGen2 = QtWidgets.QFrame(self.Mainframe_2)
        self.TrackSynGen2.setGeometry(QtCore.QRect(10, 70, 151, 571))
        self.TrackSynGen2.setAutoFillBackground(True)
        self.TrackSynGen2.setFrameShape(QtWidgets.QFrame.Box)
        self.TrackSynGen2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TrackSynGen2.setObjectName("TrackSynGen2")
        self.GenSyn2Graph = PlotWidget(self.TrackSynGen2)
        self.GenSyn2Graph.setGeometry(QtCore.QRect(0, 0, 151, 571))
        self.GenSyn2Graph.setObjectName("GenSyn2Graph")
        self.wellinfoframe2 = QtWidgets.QFrame(self.Mainframe_2)
        self.wellinfoframe2.setGeometry(QtCore.QRect(660, 70, 181, 261))
        self.wellinfoframe2.setFrameShape(QtWidgets.QFrame.Box)
        self.wellinfoframe2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wellinfoframe2.setLineWidth(2)
        self.wellinfoframe2.setObjectName("wellinfoframe2")
        self.Well_info_label2 = QtWidgets.QLabel(self.wellinfoframe2)
        self.Well_info_label2.setGeometry(QtCore.QRect(50, 10, 70, 20))
        self.Well_info_label2.setFrameShape(QtWidgets.QFrame.Box)
        self.Well_info_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.Well_info_label2.setObjectName("Well_info_label2")
        self.Track1dropdown2 = QtWidgets.QLabel(self.wellinfoframe2)
        self.Track1dropdown2.setGeometry(QtCore.QRect(10, 40, 55, 16))
        self.Track1dropdown2.setFrameShape(QtWidgets.QFrame.Box)
        self.Track1dropdown2.setObjectName("Track1dropdown2")
        self.Track2dropdown2 = QtWidgets.QLabel(self.wellinfoframe2)
        self.Track2dropdown2.setGeometry(QtCore.QRect(10, 100, 55, 16))
        self.Track2dropdown2.setFrameShape(QtWidgets.QFrame.Box)
        self.Track2dropdown2.setObjectName("Track2dropdown2")
        self.Track3dropdown2 = QtWidgets.QLabel(self.wellinfoframe2)
        self.Track3dropdown2.setGeometry(QtCore.QRect(10, 180, 55, 16))
        self.Track3dropdown2.setFrameShape(QtWidgets.QFrame.Box)
        self.Track3dropdown2.setObjectName("Track3dropdown2")
        self.comboBox_Track1_well2 = QtWidgets.QComboBox(self.wellinfoframe2)
        self.comboBox_Track1_well2.setGeometry(QtCore.QRect(10, 70, 151, 21))
        self.comboBox_Track1_well2.setObjectName("comboBox_Track1_well2")
        self.comboBox_Track2_well2 = QtWidgets.QComboBox(self.wellinfoframe2)
        self.comboBox_Track2_well2.setGeometry(QtCore.QRect(10, 140, 151, 21))
        self.comboBox_Track2_well2.setObjectName("comboBox_Track2_well2")
        self.comboBox_Track3_well2 = QtWidgets.QComboBox(self.wellinfoframe2)
        self.comboBox_Track3_well2.setGeometry(QtCore.QRect(10, 210, 151, 21))
        self.comboBox_Track3_well2.setObjectName("comboBox_Track3_well2")
        self.Synthetic_Graph_Widget_2 = QtWidgets.QWidget(self.Mainframe_2)
        self.Synthetic_Graph_Widget_2.setGeometry(QtCore.QRect(660, 340, 181, 301))
        self.Synthetic_Graph_Widget_2.setObjectName("Synthetic_Graph_Widget_2")
        self.wavelet_graph_2 = PlotWidget(self.Synthetic_Graph_Widget_2)
        self.wavelet_graph_2.setGeometry(QtCore.QRect(0, 30, 181, 271))
        self.wavelet_graph_2.setObjectName("wavelet_graph_2")
        self.wavelet_plot_title_2 = QtWidgets.QLabel(self.Synthetic_Graph_Widget_2)
        self.wavelet_plot_title_2.setGeometry(QtCore.QRect(50, 0, 91, 21))
        self.wavelet_plot_title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.wavelet_plot_title_2.setObjectName("wavelet_plot_title_2")
        self.Track1Frame_2 = QtWidgets.QFrame(self.Mainframe_2)
        self.Track1Frame_2.setGeometry(QtCore.QRect(490, 70, 151, 571))
        self.Track1Frame_2.setAutoFillBackground(True)
        self.Track1Frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.Track1Frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Track1Frame_2.setObjectName("Track1Frame_2")
        self.Track1Graph_2 = PlotWidget(self.Track1Frame_2)
        self.Track1Graph_2.setGeometry(QtCore.QRect(0, 0, 151, 571))
        self.Track1Graph_2.setObjectName("Track1Graph_2")
        self.label_track1_2 = QtWidgets.QLabel(self.Mainframe_2)
        self.label_track1_2.setGeometry(QtCore.QRect(540, 50, 55, 16))
        self.label_track1_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_track1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_track1_2.setObjectName("label_track1_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1852, 26))
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

        
        self.synthethic_options_frame.setEnabled(False)
        
        # All data loading parameters for well 1 
        self.well1name = '' #UWI
        self.dlog_start1 = 0 # depth of loggin start for well 1
        self.well1kb = 0
        self.dblwseisdat1 = 0 # distance below seismic datum 
        self.log_start_time1 = 0 # well 1 log start time (TWT units:s)
        self.well1 = [] # well 1 data 
        self.well1df = []
        self.seis_data1 = [] # seismic datum 
        self.repl_vel1 = [] # seismic velocity 
        self.havesonic1 = False
        self.havedensity1 = False
        self.densitymnemonic1 = None
        self.sonicmnemonic1 = None
        
        #All data loading parameters for well 2
        self.well2name = '' #UWI
        self.dlog_start2 = 0 # depth of loggin start for well 1
        self.well2kb = 0
        self.dblwseisdat2 = 0 # distance below seismic datum 
        self.log_start_time2 = 0 # well 1 log start time (TWT units:s)
        self.well2 = [] # well 1 data 
        self.well2df = []
        self.seis_data2 = [] # seismic datum 
        self.repl_vel2 = [] # seismic velocity 
        self.havesonic2 = False
        self.havedensity2 = False
        self.densitymnemonic2 = None
        self.sonicmnemonic2 = None
        
        
        
        # All data for synthetic generation for well 1 and 2
        self.well1df_tdom= pd.DataFrame()
        self.well2df_tdom= pd.DataFrame()
        #connection to loading well 1
        #self.actionLoad_Well_1.triggered.connect(lambda : self.setattribute(self.loadwell1))
        self.actionLoad_Well_1.triggered.connect(self.loadwell1)
        self.actionLoad_Well_2.triggered.connect(self.loadwell2)
        #connection to plot data  - well 1 
        self.comboBox_Track1.activated.connect(lambda : self.plotw1t1(self.well1,self.well1df,self.seis_data1,self.repl_vel1,self.well1df_tdom))
        self.comboBox_Track2.activated.connect(lambda : self.plotw1t2(self.well1,self.well1df,self.seis_data1,self.repl_vel1,self.well1df_tdom))
        self.comboBox_Track3.activated.connect(lambda : self.plotw1t3(self.well1,self.well1df,self.seis_data1,self.repl_vel1,self.well1df_tdom))
        #connection to plot data  - well 2 
        self.comboBox_Track1_well2.activated.connect(lambda : self.plotw2t1(self.well2,self.well2df,self.seis_data2,self.repl_vel2,self.well2df_tdom))
        self.comboBox_Track2_well2.activated.connect(lambda : self.plotw2t2(self.well2,self.well2df,self.seis_data2,self.repl_vel2,self.well2df_tdom))
        self.comboBox_Track3_well2.activated.connect(lambda : self.plotw2t3(self.well2,self.well2df,self.seis_data2,self.repl_vel2,self.well2df_tdom))
        
        #connection to generating a synthetic seismogram: 
        #self.gensynwell_1.triggered.connect(lambda: self.gensynaction2(self.havesonic1,self.havedensity1,self.well1,self.well1df))
        self.gensynwell_1.triggered.connect(self.gensynactionbutton)#enables the gui for synthetic creation 
        self.Create_Synthetic.clicked.connect(lambda: self.gensynaction(self.havesonic1,self.havedensity1,self.well1,self.well1df,self.havesonic2,self.havedensity2,self.well2,self.well2df)) #plots and create the synthetic for well 1
        
        #connection to change available wavelet types
        self.wave_type_comboBox.currentTextChanged.connect(self.wavelet_win)
        
        
                             
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
        self.LCF_checkBox.setText(_translate("MainWindow", "LCF Multiple"))
        self.Wavelet_Title.setText(_translate("MainWindow", "Wavelet"))
        self.wave_type_comboBox.setItemText(0, _translate("MainWindow", "Ormsby"))
        self.wave_type_comboBox.setItemText(1, _translate("MainWindow", "Ricker"))
        self.wave_type_comboBox.setItemText(2, _translate("MainWindow", "Berlage"))
        self.wave_type_comboBox.setItemText(3, _translate("MainWindow", "Generalized"))
        self.wave_length_label.setText(_translate("MainWindow", "Length (ms)"))
        self.max_time_comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.max_time_comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.max_time_comboBox.setItemText(2, _translate("MainWindow", "4"))
        self.max_time_label.setText(_translate("MainWindow", "Max Time (s)"))
        self.LCF_multiplier.setText(_translate("MainWindow", "1.5"))
        self.Create_Synthetic.setText(_translate("MainWindow", "Create Synthetic"))
        self.HCF_label.setText(_translate("MainWindow", "HCF (Hz):"))
        self.LPF_label.setText(_translate("MainWindow", "LPF (Hz):"))
        self.sample_rate_label.setText(_translate("MainWindow", "Sample (s)"))
        self.sample_rate_comboBox.setItemText(0, _translate("MainWindow", "0.001"))
        self.sample_rate_comboBox.setItemText(1, _translate("MainWindow", "0.002"))
        self.sample_rate_comboBox.setItemText(2, _translate("MainWindow", "0.004"))
        self.Amplitude_label.setText(_translate("MainWindow", "Amplitude"))
        self.HPF_label.setText(_translate("MainWindow", "HPF (Hz):"))
        self.LCF_label.setText(_translate("MainWindow", "LCF (Hz):"))
        self.HPF_checkbox.setText(_translate("MainWindow", "HPF Multiple"))
        self.wave_length_comboBox.setItemText(0, _translate("MainWindow", "128"))
        self.wave_length_comboBox.setItemText(1, _translate("MainWindow", "256"))
        self.wave_length_comboBox.setItemText(2, _translate("MainWindow", "512"))
        self.Phase_label.setText(_translate("MainWindow", "Phase (deg)"))
        self.wave_type_label.setText(_translate("MainWindow", "Type"))
        self.HPF_multiplier.setText(_translate("MainWindow", "1.5"))
        self.wavelet_well_sel_label.setText(_translate("MainWindow", "Well"))
        self.wavelet_well_sel_comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.wavelet_well_sel_comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.label_track2_2.setText(_translate("MainWindow", "Track 2"))
        self.label_track3_2.setText(_translate("MainWindow", "Track 3"))
        self.label_track_syngen_2.setText(_translate("MainWindow", "Generated Synthetic 2"))
        self.Well_info_label2.setText(_translate("MainWindow", "Well Name"))
        self.Track1dropdown2.setText(_translate("MainWindow", "Track 1"))
        self.Track2dropdown2.setText(_translate("MainWindow", "Track 2"))
        self.Track3dropdown2.setText(_translate("MainWindow", "Track 3"))
        self.wavelet_plot_title_2.setText(_translate("MainWindow", "Wavelet Plot"))
        self.label_track1_2.setText(_translate("MainWindow", "Track 1"))
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
        densitylist = ['RHOB','RHOZ']
        
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
        self.seis_data1 = seis_dat
        self.repl_vel1 = repl_vel
        self.dlog_start1 = dlog_start # depth of data loggin start 
        ### Determining KB from data
        self.well1kb = w1.location.ekb
        ### UWI from Data ## 
        self.well1name = w1.uwi
        self.Well_info_label.setText(w1.uwi)
        #connection to populate combo boxes 
        self.popcombobox1(mnemonics) 
    
    
    #method to load well 2
    def loadwell2(self):
        #file location 
        floc = QFileDialog.getOpenFileName(None, 'Open File', 'C:\ ')
        #setup to laad the well into a data frame using the LAS library 
        w2 = Well.from_las(floc[0]) 
        #data that contains all 
        data = tdinfo()
        seis_dat, repl_vel = data.getInputs()
        seis_dat = float(seis_dat)
        repl_vel = float(repl_vel) 
        mnemonics = w2._get_curve_mnemonics()
        
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
                    self.havesonic2 = True
                    dt = w2.data[sonic_mnemonics].values # assuming us/m 
                    #print(dt)
                    depth_increment = w2.data[sonic_mnemonics].step # for time-depth relationship 
                    dlog_start = w2.data[sonic_mnemonics].start
                    #print(depth_increment,dlog_start)
        #print(havesonic, sonic_mnemonics) -> validation that filter works
        ###   Automatically Select the density based on the given mnmemonics  
        densitylist = ['RHOB','RHOZ']
        
        if chosen_density == False: 
            for i in densitylist: 
                if i in mnemonics:
                    density_mnemonics = i 
                    havedensity = True
                    self.havedensity2 = True 
        
        w2df = w2.df()
        ## Establishing Time-Depth Relationship 
        ### Determining the depth of log_start (where loggin of data begins) 
        #dlog_start = w1df[mnemonics[0]].keys()[0]
        ### Determining the distance below the seismic datum 
        # Seismic_Datum-Kelly Bushing+log_start = distance below seismic datum 
        dblwseisdat2 = seis_dat-w2.location.ekb+dlog_start 
        self.dblwseisdat2 = dblwseisdat2
        #Log start time (s)
        log_start_time2 = (dblwseisdat2/repl_vel)*2 #have to multiply by 2 b/c of TWT 
        self.log_start_time2 = log_start_time2
        
        
        if havesonic == True:
            dt_iterval = np.nan_to_num(dt)*depth_increment/1e6 
            t_cum = np.cumsum(dt_iterval)*2 #*2 for two way time 
            TWT = t_cum + log_start_time2
            w2df['TWT'] = TWT 
            mnemonics.append('TWT')
            
        
        # acoustic impedance: 
        if havesonic == True and havedensity == True: 
            #sonic velocity calculate: 
            w2df['Vsonic']=1e6/w2df[sonic_mnemonics].values #units transformed to m/s
            #adding 'Vsonic' to the mnemonics: 
            mnemonics.append('Vsonic')
            #calculatin the Acoustic Impedance
            w2df['AI'] = w2df['Vsonic'].values*w2df[density_mnemonics].values
            #adding 'AI' to the mnemonics: 
            mnemonics.append('AI')
            #calculation of the reflection coefficient 
            Imp = w2df['AI'].values
            Rc = []
            for i in range(len(Imp)-1):
                Rc.append((Imp[i+1]-Imp[i])/(Imp[i]+Imp[i+1])) 
            # to adjust vector size copy the last element to the tail
            Rc.append(Rc[-1])
            # Let's add Rc into dataframe as new column
            w2df['Rc'] = pd.Series(Rc, index=w2df.index)
            mnemonics.append('Rc')
        
        #### repopulating data parameters ####
        self.well2 = w2
        self.well2df = w2df
        self.seis_data2 = seis_dat
        self.repl_vel2 = repl_vel
        self.dlog_start2 = dlog_start # depth of data loggin start 
        ### Determining KB from data
        self.well2kb = w2.location.ekb
        ### UWI from Data ## 
        self.well2name = w2.uwi
        self.Well_info_label.setText(w2.uwi)
        #connection to populate combo boxes 
        self.popcombobox2(mnemonics) 


        #method to populate combobox data for well1
    def popcombobox1(self,well_attr): 
        mnemonics = well_attr
        self.comboBox_Track1.addItems(mnemonics)
        self.comboBox_Track2.addItems(mnemonics)
        self.comboBox_Track3.addItems(mnemonics)
        

    #method to populate combobox data for well2
    def popcombobox2(self,well_attr): 
        mnemonics = well_attr
        self.comboBox_Track1_well2.addItems(mnemonics)
        self.comboBox_Track2_well2.addItems(mnemonics)
        self.comboBox_Track3_well2.addItems(mnemonics)
        
        # method to plot data in Track 1 - well1
    def plotw1t1(self,well1,well1df,seis_dat,repl_vel,well1df_tdom):
        
        self.Track1Graph.clear()
        sel_data = self.comboBox_Track1.currentText()
        #section for only plotting data in tdom 
        tdom_data = ['AI_tdom','Rc_tdom']
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
                
        
        self.Track1Graph.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        trackplot = pg.PlotCurveItem(y,x,connect='finite',pen=(255, 0, 0))
        self.Track1Graph.addItem(trackplot)
        self.Track1Graph.invertY(True)
        self.Track1Graph.showGrid(x=True,y=True)
        
        
    # method to plot theh data in Track 2 - well 1
    def plotw1t2(self,well1,well1df,seis_dat,repl_vel,well1df_tdom):
        self.Track2Graph.clear()
        sel_data = self.comboBox_Track2.currentText()
        tdom_data = ['AI_tdom','Rc_tdom']
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
      
    # method to plot theh data in Track 3 - well 1
    def plotw1t3(self,well1,well1df,seis_dat,repl_vel,well1df_tdom):
        self.Track3Graph.clear()
        sel_data = self.comboBox_Track3.currentText()
        tdom_data = ['AI_tdom','Rc_tdom']
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
        
        
     # method to plot data in Track 1 - well1
    def plotw2t1(self,well2,well2df,seis_dat,repl_vel,well2df_tdom):
        
        self.Track1Graph_2.clear()
        sel_data = self.comboBox_Track1_well2.currentText()
        #section for only plotting data in tdom 
        tdom_data = ['AI_tdom','Rc_tdom']
        if sel_data in tdom_data:
            dplot = well2df_tdom[sel_data]
        else: 
            dplot = well2df[sel_data]
        y = dplot.values #[2,4,6,8,10,math.nan]#
        x = dplot.index.values#[1,2,3,4,5,6]#
        
        # for loop to handle nan values 
        for i in range(len(y)):
            if math.isnan(y[i]) == True :
                y[i] = 0 
                
        
        self.Track1Graph_2.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        trackplot = pg.PlotCurveItem(y,x,connect='finite',pen=(255, 0, 0))
        self.Track1Graph_2.addItem(trackplot)
        self.Track1Graph_2.invertY(True)
        self.Track1Graph_2.showGrid(x=True,y=True)
        
    # method to plot data in Track 2 - well1
    def plotw2t2(self,well2,well2df,seis_dat,repl_vel,well2df_tdom):
        
        self.Track2Graph_2.clear()
        sel_data = self.comboBox_Track2_well2.currentText()
        #section for only plotting data in tdom 
        tdom_data = ['AI_tdom','Rc_tdom']
        if sel_data in tdom_data:
            dplot = well2df_tdom[sel_data]
        else: 
            dplot = well2df[sel_data]
        y = dplot.values #[2,4,6,8,10,math.nan]#
        x = dplot.index.values#[1,2,3,4,5,6]#
        
        # for loop to handle nan values 
        for i in range(len(y)):
            if math.isnan(y[i]) == True :
                y[i] = 0 
                
        
        self.Track2Graph_2.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        trackplot = pg.PlotCurveItem(y,x,connect='finite',pen=(255, 0, 0))
        self.Track2Graph_2.addItem(trackplot)
        self.Track2Graph_2.invertY(True)
        self.Track2Graph_2.showGrid(x=True,y=True)
        
    # method to plot data in Track 1 - well1
    def plotw2t3(self,well2,well2df,seis_dat,repl_vel,well2df_tdom):
        
        self.Track3Graph_2.clear()
        sel_data = self.comboBox_Track3_well2.currentText()
        #section for only plotting data in tdom 
        tdom_data = ['AI_tdom','Rc_tdom']
        if sel_data in tdom_data:
            dplot = well2df_tdom[sel_data]
        else: 
            dplot = well2df[sel_data]
        y = dplot.values #[2,4,6,8,10,math.nan]#
        x = dplot.index.values#[1,2,3,4,5,6]#
        
        # for loop to handle nan values 
        for i in range(len(y)):
            if math.isnan(y[i]) == True :
                y[i] = 0 
                
        
        self.Track3Graph_2.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        trackplot = pg.PlotCurveItem(y,x,connect='finite',pen=(255, 0, 0))
        self.Track3Graph_2.addItem(trackplot)
        self.Track3Graph_2.invertY(True)
        self.Track3Graph_2.showGrid(x=True,y=True)

    
    # Method to activate generate synthetic window
    def gensynactionbutton(self):
        self.synthethic_options_frame.setEnabled(True)
    # Method to change window type based wavelet type selected default: Ormsby
    def wavelet_win(self):
        w_type = self.wave_type_comboBox.currentText()
        if w_type == 'Ricker': # only need 1 frequency 
            self.LCF_slider.setEnabled(False)
            self.HPF_slider.setEnabled(False)
            self.HCF_slider.setEnabled(False)
            self.LCF_checkBox.setEnabled(False)
            self.LCF_multiplier.setEnabled(False)
            self.HPF_checkbox.setEnabled(False)
            self.HPF_multiplier.setEnabled(False)
        elif w_type == 'Ormsby': # need 4 frequencies
            self.LCF_slider.setEnabled(True)
            self.HPF_slider.setEnabled(True)
            self.HCF_slider.setEnabled(True)
            self.LCF_checkBox.setEnabled(True)
            self.LCF_multiplier.setEnabled(True)
            self.HPF_checkbox.setEnabled(True)
            self.HPF_multiplier.setEnabled(True)
        elif w_type == 'Berlage': # only need 1 frequency
            self.LCF_slider.setEnabled(False)
            self.HPF_slider.setEnabled(False)
            self.HCF_slider.setEnabled(False)
            self.LCF_checkBox.setEnabled(False)
            self.LCF_multiplier.setEnabled(False)
            self.HPF_checkbox.setEnabled(False)
            self.HPF_multiplier.setEnabled(False)
        else: #Generalized # only need 1 frequency 
            self.LCF_slider.setEnabled(False)
            self.HPF_slider.setEnabled(False)
            self.HCF_slider.setEnabled(False)
            self.LCF_checkBox.setEnabled(False)
            self.LCF_multiplier.setEnabled(False)
            self.HPF_checkbox.setEnabled(False)
            self.HPF_multiplier.setEnabled(False)
        
    
    #Method to plot data in wells - Default Wavelet: Ormsby 
    def gensynaction(self,havesonic1,havedensity1,well1,well1df,havesonic2,havedensity2,well2,well2df):
        #determining which well will have the 
        well_sel = int(self.wavelet_well_sel_comboBox.currentText())
        
        dt = float(self.sample_rate_comboBox.currentText())
        t_max = float(self.max_time_comboBox.currentText())
        t =  np.arange(0,t_max,dt)
        
        w_type = self.wave_type_comboBox.currentText()
        wave_len = float(self.wave_length_comboBox.currentText())/1000 #(s)
        
        #clearing the current graphs of data: 
        if well_sel == 1: 
            self.GenSyn1Graph.clear()
            self.wavelet_graph.clear()
        else: 
            self.GenSyn2Graph.clear()
            self.wavelet_graph_2.clear()
        print(well_sel)
        # Note: For data that only required 1 frequency, we are using LPF_slider
        
        if well_sel == 1: 
            AI = well1df.AI.values
        else: 
            AI = well2df.AI.values
                
        #Acoustic Impedance manipulation 
        
        for i in range(len(AI)):
            if math.isnan(AI[i]) == True :
                AI[i] = 0

        for i in range(len(AI)):
            if AI[i] == 0 :
                AI[i] = np.mean(AI)
        
        if well_sel == 1: 
            AI_tdom = np.interp(x=t,xp=well1df['TWT'].values,fp=AI)
        else: 
            AI_tdom = np.interp(x=t,xp=well2df['TWT'].values,fp=AI)
        
            #resampling to time domain via interpolation      
        
        #reflection coefficient in time domain 
            # again Rc calulation but in reampled time domain
            
        Rc_tdom = []
        for i in range(len(AI_tdom)-1):
            Rc_tdom.append((AI_tdom[i+1]-AI_tdom[i])/(AI_tdom[i]+AI_tdom[i+1]))
        # to adjust vector size copy the last element to the tail
        Rc_tdom.append(Rc_tdom[-1])
        
        #dataframe for plotting items in dataframe 
        if well_sel == 1: 
            if self.well1df_tdom.empty :
                self.comboBox_Track1.addItems(['AI_tdom','Rc_tdom'])
                self.comboBox_Track2.addItems(['AI_tdom','Rc_tdom'])
                self.comboBox_Track3.addItems(['AI_tdom','Rc_tdom'])
            tdom_data1 = {'AI_tdom':AI_tdom,'Rc_tdom':Rc_tdom}
            well1df_tdom = pd.DataFrame(data =tdom_data1,index=t)
            self.well1df_tdom = well1df_tdom
            
        else:
            if self.well2df_tdom.empty: 
                self.comboBox_Track1_well2.addItems(['AI_tdom','Rc_tdom'])
                self.comboBox_Track2_well2.addItems(['AI_tdom','Rc_tdom'])
                self.comboBox_Track3_well2.addItems(['AI_tdom','Rc_tdom'])
            tdom_data2 = {'AI_tdom':AI_tdom,'Rc_tdom':Rc_tdom}
            well2df_tdom = pd.DataFrame(data =tdom_data2,index=t)
            self.well2df_tdom = well2df_tdom
            
        #wavelet data 
        if w_type == 'Ricker': # only need 1 frequency 
            freq = float(self.LPF_slider.value())
            wavelet = bg.filters.wavelets.ricker(wave_len, dt, freq, t=None, return_t=True, sym=True)

        if w_type == 'Ormsby':
            LCF = float(self.LCF_slider.value())
            LPF = float(self.LPF_slider.value())
            HPF = float(self.HPF_slider.value())
            HCF = float(self.HCF_slider.value())
            # need warning sign that LCF < LPF < HPF < HCF 
            freq = [LCF,LPF,HPF,HCF]
            wavelet = bg.filters.wavelets.ormsby(wave_len, dt, freq, t=None, return_t=True, sym=True)
        if w_type == 'Berlage':
            freq = float(self.LPF_slider.value())
            wavelet = bg.filters.wavelets.berlage(wave_len, dt, freq,n=2,alpha=180, phi=- 1.5707963267948966, t=None, return_t=True, sym=True) 
            #can change data to accept other values of n,alpha,phi 
        else: #Generalized
            freq = float(self.LPF_slider.value())
            wavelet = bg.filters.wavelets.generalized(wave_len, dt, freq, u=1.0, t=None, return_t=True, sym=True)

        #phase rotation of wavelet via Hilbert Transform 
        wavexplot = wavelet.time
        waveyplot = wavelet.amplitude #amplitude of the chosen wavelet
        rotate_phase = float(self.Phase_slider.value()) #degrees 
        if rotate_phase != 0:
            waveyplot = bg.filters.filters.rotate_phase(waveyplot,rotate_phase,degrees=True)

        #plotting of wavelet
        trackplot = pg.PlotCurveItem(wavexplot,waveyplot,connect='finite',pen=(255, 0, 0))
        #clearing the current graphs of data: 
        if well_sel == 1: 
            self.wavelet_graph.addItem(trackplot)
        else: 
            self.wavelet_graph_2.addItem(trackplot)
        
        #convolution of data

        for i in range(len(Rc_tdom)):
            if math.isnan(Rc_tdom[i]) == True :
                Rc_tdom[i] = 0
        synthetic = np.convolve(wavelet.amplitude, Rc_tdom, mode = 'same')
        
        pen = pg.mkPen(color=(255, 0, 0))
        trackplot = pg.PlotCurveItem(synthetic,t,connect='finite',pen=(255, 0, 0))
        
        if well_sel == 1: 
            self.GenSyn1Graph.setBackground('w')
            self.GenSyn1Graph.addItem(trackplot)
            self.GenSyn1Graph.invertY(True)
            self.GenSyn1Graph.showGrid(x=True,y=True)
        else: 
            self.GenSyn2Graph.setBackground('w')
            self.GenSyn2Graph.addItem(trackplot)
            self.GenSyn2Graph.invertY(True)
            self.GenSyn2Graph.showGrid(x=True,y=True)

            """
            based on w_type turn on and off for specific wavelets. 
            Different wavelets: 
            1. bruges.filters.wavelets.ricker(duration, dt, f, t=None, return_t=True, sym=True)[source] 
                need only 1 frequency 
            2. bruges.filters.wavelets.ormsby(duration, dt, f, t=None, return_t=True, sym=True)[source]
                need 4 frequencies 
            3. bruges.filters.wavelets.berlage(duration, dt, f, n=2, alpha=180, phi=- 1.5707963267948966, t=None, return_t=True, sym=True)
                need only 1 frequency 
                    can change other parameters in wavelet setting window to account for other parameters
            4. bruges.filters.wavelets.generalized(duration, dt, f, u=2, t=None, return_t=True, imag=False, sym=True)
                for minimum phase: (duration = 0.256, dt = 0.002, f = 40, u=1.0)
                    can change other parameters in wavelet setting window to account for other parameters
                          
            """
            """
        elif (havesonic == True) & (havedensity == False): 
            print("Please load a well with a valid density log")
        elif (havesonic == False) & (havedensity == True): 
            print("Please load a well with a valid sonic log")
        else: 
            print("Please load a well with a valid sonic and density log") 
            """

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
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    
    
"""
Notes: 
1. Can reduce amount of code in loading well by determining which well we wanted to load 
2. Note that the multiplier isn't functional at the moment 
"""
