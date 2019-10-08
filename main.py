# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui6.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os

from MIRFgui import PlotWidget
from MIRFheaders import *
from MIRFhelpers import MIRFdata, MIRFheader
from MIRFfilters import bandpass


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1153, 801)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget_2 = QtWidgets.QListWidget(self.frame)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout.addWidget(self.listWidget_2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listWidget_3 = QtWidgets.QListWidget(self.frame)
        self.listWidget_3.setObjectName("listWidget_3")
        self.verticalLayout.addWidget(self.listWidget_3)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.plotWidget = PlotWidget(self.frame_3)
        self.plotWidget.setObjectName("plotWidget")
        self.gridLayout_3.addWidget(self.plotWidget, 1, 0, 1, 1)
        self.toolFrame = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolFrame.sizePolicy().hasHeightForWidth())
        self.toolFrame.setSizePolicy(sizePolicy)
        self.toolFrame.setMinimumSize(QtCore.QSize(0, 40))
        self.toolFrame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.toolFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toolFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolFrame.setObjectName("toolFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.toolFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.toolFrame)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.checkBox = QtWidgets.QCheckBox(self.toolFrame)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_4.addWidget(self.checkBox)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.toolFrame)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.toolFrame)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.checkBox_2 = QtWidgets.QCheckBox(self.toolFrame)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_3.addWidget(self.checkBox_2)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.toolFrame)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_4.addWidget(self.line_4, 0, 3, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.toolFrame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.toolFrame)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 0, 4, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line = QtWidgets.QFrame(self.toolFrame)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.label_5 = QtWidgets.QLabel(self.toolFrame)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.comboBox_2 = QtWidgets.QComboBox(self.toolFrame)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 5, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.toolFrame)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 0, 6, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.toolFrame)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.checkBox_4 = QtWidgets.QCheckBox(self.toolFrame)
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_6.addWidget(self.checkBox_4)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 0, 7, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.toolFrame)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_4.addWidget(self.line_5, 0, 8, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.toolFrame)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.lineEdit = QtWidgets.QLineEdit(self.toolFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.toolFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.toolFrame)
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout.addWidget(self.checkBox_3)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 9, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.line_6 = QtWidgets.QFrame(self.toolFrame)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_7.addWidget(self.line_6)
        self.label_10 = QtWidgets.QLabel(self.toolFrame)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.checkBox_5 = QtWidgets.QCheckBox(self.toolFrame)
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_7.addWidget(self.checkBox_5)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 0, 10, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(308, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 11, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.toolFrame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 0, 12, 1, 1)
        self.gridLayout_3.addWidget(self.toolFrame, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1153, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #--------------------------
        
        self.actionOpen.triggered.connect(self.openFile)
        self.pushButton.clicked.connect(self.plotButton)
        
        #---------------------------

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "General Header"))
        self.label_2.setText(_translate("MainWindow", "Trace Headers"))
        self.label_3.setText(_translate("MainWindow", "File Info"))
        self.label_7.setText(_translate("MainWindow", "REF"))
        self.label_8.setText(_translate("MainWindow", "AUX"))
        self.label_4.setText(_translate("MainWindow", "Twig"))
        self.comboBox.setItemText(0, _translate("MainWindow", "ALL"))
        self.comboBox.setItemText(1, _translate("MainWindow", "VZ"))
        self.comboBox.setItemText(2, _translate("MainWindow", "HX"))
        self.comboBox.setItemText(3, _translate("MainWindow", "HY"))
        self.comboBox.setItemText(4, _translate("MainWindow", "NONE"))
        self.label_5.setText(_translate("MainWindow", "Geo"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "ALL"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "NONE"))
        self.label_9.setText(_translate("MainWindow", "Overlay"))
        self.label_6.setText(_translate("MainWindow", "Filter"))
        self.lineEdit.setText(_translate("MainWindow", "3"))
        self.lineEdit_2.setText(_translate("MainWindow", "150"))
        self.label_10.setText(_translate("MainWindow", "Picks"))
        self.pushButton.setText(_translate("MainWindow", "Plot"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def openFile(self):
        
        fileName = QtWidgets.QFileDialog.getOpenFileName(None,
                                                        "Open Rcd file",
                                                        "C:/Users",
                                                        "Rcd files (*.rcd)"
                                                        )
        self.filePath = fileName[0] #convert from tuple to string
        
        #make header and trace objects
        header = MIRFheader(self.filePath)
        traces = MIRFdata(self.filePath)
        
        #fill tables and plot traces
        self.populateHeaderTable(header)
        self.populateTraceTable(traces)
        self.populateFileInfo(header)
        self.clearPlots()
        self.updateComboBox(header)
        self.updatePlots(header, traces)

        #dynamically clear and then fill the geo combo box according to number of recievers taken from header
        
        self.comboBox_2.clear()
        self.comboBox_2.insertItem(0, "ALL")
        self.comboBox_2.insertItem(1, "NONE")
        
        for i in range(header.Number_of_receivers):
            self.comboBox_2.insertItem(2+i, str(i+1))
        
    def plotButton(self):
        print("Plot button pressed...")

        header = MIRFheader(self.filePath)
        traces = MIRFdata(self.filePath)
        self.clearPlots()
        self.updatePlots(header, traces)
        
    
    def populateHeaderTable(self, header):
        
        self.header = header
        
        self.listWidget_2.clear() #clear the lsit wiudget before adding items
                
        for attr, value in self.header.__dict__.items():
            self.listWidget_2.addItem("{}, {}".format(attr,str(value)))
        
        print("Populating header table...")
        

    def populateTraceTable(self, traces):
        
        self.traces = traces
        self.listWidget_3.clear() #clear the lsit wiudget before adding items

        i, k = 0, 1
        
        for j in range(len(self.traces)):

            self.listWidget_3.addItem("{} {}".format("TRACE",str(k)))
            self.listWidget_3.addItem("-----------------------------------")
            
            i += 1
            k += 1

            for attr, value in self.traces[j].__dict__.items():
                if attr != 'Raw_data':
                    self.listWidget_3.addItem("{}, {}".format(attr,str(value)))
                    i += 1
            
            self.listWidget_3.addItem("")
        
        print("Populating trace table...")


    def populateFileInfo(self, header):
        self.header = header

        self.listWidget.clear()
        
        head, tail = os.path.split(self.filePath)
        size = os.path.getsize(self.filePath)

        self.listWidget.addItem("File Name: {}".format(tail))
        self.listWidget.addItem("Folder: {}".format(head))
        self.listWidget.addItem("File Size: {}KB".format(int(size/1024)))

        #self.listWidget.addItem("File Size: {}").format(self.filePath)
        
        datetime = "{}/{}/{} {}:{}:{}".format(self.header.Year, self.header.Month, self.header.Day, self.header.Hour, self.header.Minute, self.header.Second)
        self.listWidget.addItem("Date/Time: {}".format(datetime))


    def clearPlots(self):
        
        self.plotWidget.clear()
        self.data = []
        print("Clearing old plots...")


    def updateComboBox(self, header):

        self.header = header
        self.comboBox_2.clear()
        self.comboBox_2.insertItem(0, "ALL")
        self.comboBox_2.insertItem(1, "NONE")
        
        for i in range(self.header.Number_of_receivers):
            self.comboBox_2.insertItem(2+i, str(i+1))


    def updatePlots(self, header, traces):
        self.header = header
        self.traces = traces
        self.live_channels = len(self.traces)
        self.SI = self.header.SIus


        #check if REF is checked.
        #---------------------------------------------------------------------
        if self.checkBox.isChecked() == False:
            print("REF: No")
        else:
            print("REF: Yes")
            for i in range(self.live_channels):
                if self.traces[i].Owner == -1:
                    self.data.append(self.traces[i])


        #check if AUX is checked.
        #---------------------------------------------------------------------
        if self.checkBox_2.isChecked() == False:
            print("AUX: No")
        else:
            print("AUX: Yes")
            for i in range(self.live_channels):
                if self.traces[i].Owner == -2:
                    self.data.append(self.traces[i])


        #check Geos
        #---------------------------------------------------------------------
        geo_combo_text = self.comboBox_2.currentText()
        geo_combo_index = self.comboBox_2.currentIndex()
        twig_combo_text = self.comboBox.currentText()
        twig_combo_index = self.comboBox.currentIndex()

        #plot all geos
        if geo_combo_text == "ALL" and twig_combo_text == "ALL":

            print("Geo: {}".format(geo_combo_text))
            print("Twig: {}".format(twig_combo_text))

            for i in range(self.live_channels):
                if self.traces[i].Owner > 0:
                    self.data.append(self.traces[i])
        
        elif geo_combo_text == "ALL" and twig_combo_text == "VZ":
            
            print("Geo: {}".format(geo_combo_text))
            print("Twig: {}".format(twig_combo_text))

            for i in range(self.live_channels):
                if self.traces[i].Owner > 0 and self.traces[i].Descriptor == 1:
                    self.data.append(self.traces[i])
        
        elif geo_combo_text == "ALL" and twig_combo_text == "HX":
            
            print("Geo: {}".format(geo_combo_text))
            print("Twig: {}".format(twig_combo_text))

            for i in range(self.live_channels):
                if self.traces[i].Owner > 0 and self.traces[i].Descriptor == 2:
                    self.data.append(self.traces[i])

        elif geo_combo_text == "ALL" and twig_combo_text == "HY":
            
            print("Geo: {}".format(geo_combo_text))
            print("Twig: {}".format(twig_combo_text))

            for i in range(self.live_channels):
                if self.traces[i].Owner > 0 and self.traces[i].Descriptor == 3:
                    self.data.append(self.traces[i])
        
        elif geo_combo_text == "ALL" and twig_combo_text == "NONE":
            
            print("Geo: {}".format(geo_combo_text))
            print("Twig: {}".format(twig_combo_text))

        
        
        #single geo selected
        #-----------------------------------------------------------------
        
        elif geo_combo_index > 1 and twig_combo_text == "ALL":
            
            print("Geo: {}".format(geo_combo_text))
            print("Twig: {}".format(twig_combo_text))
            
            for i in range(self.live_channels):
                
                if self.traces[i].Owner == int(geo_combo_text):
                        self.data.append(self.traces[i])
                        
        
        elif geo_combo_index > 1 and twig_combo_text == "VZ":
            
            print("Geo: {}".format(geo_combo_text))
            print("Twig: {}".format(twig_combo_text))
            
            for i in range(self.live_channels):
                
                if self.traces[i].Owner == int(geo_combo_text) and self.traces[i].Descriptor == 1:
                        self.data.append(self.traces[i])
        
        elif geo_combo_index > 1 and twig_combo_text == "HX":
            
            print("Geo: {}".format(geo_combo_text))
            print("Twig: {}".format(twig_combo_text))
            
            for i in range(self.live_channels):
                
                if self.traces[i].Owner == int(geo_combo_text) and self.traces[i].Descriptor == 2:
                        self.data.append(self.traces[i])
        
        elif geo_combo_index > 1 and twig_combo_text == "HY":
            
            print("Geo: {}".format(geo_combo_text))
            print("Twig: {}".format(twig_combo_text))
            
            for i in range(self.live_channels):
                
                if self.traces[i].Owner == int(geo_combo_text) and self.traces[i].Descriptor == 3:
                        self.data.append(self.traces[i])
        
        # no geos selected
        #-----------------------------------------------------------------
        elif geo_combo_text == "NONE":
            print("Geo: {}".format(geo_combo_text))
        

        #Check Filter
        #---------------------------------------------------------------------
        if self.checkBox_3.isChecked() == False:
            print("Filter: No")
        
        else:
            bandwidth_start = int(self.lineEdit.text())
            bandwidth_end = int(self.lineEdit_2.text())

            sample_frequency = 1/(self.SI/1000000)
            #bandwidth_start = 3
            #bandwidth_end = 150
            

            for i in range(len(self.data)):


                raw_data = self.data[i].Raw_data
                filtered_data = bandpass(raw_data, bandwidth_start, bandwidth_end, sample_frequency, 4)
                self.data[i].Raw_data = filtered_data
            
            print("Filter: Yes, {} {}".format(bandwidth_start, bandwidth_end))
        

        #Check Picks
        #---------------------------------------------------------------------
        if self.checkBox_5.isChecked() == False:
            print("Picks: No")
            self.picks = False
        
        else:
            print("Picks: Yes")
            self.picks = True

        print("Number of data channels to plot: {}".format(len(self.data)))
        
        
        #Check Overlay
        #---------------------------------------------------------------------
        if self.checkBox_4.isChecked() == True:
            print("Overlay: Yes")
            
            if twig_combo_text != "ALL":
                self.plotWidget.standardView(self.data, self.SI, self.picks)
            else:
                self.plotWidget.overlayView(self.data, self.SI, self.picks)

        else:
            print("Overlay: No")
            self.plotWidget.standardView(self.data, self.SI, self.picks)
            

        print("Updating plots...")
        print("")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
