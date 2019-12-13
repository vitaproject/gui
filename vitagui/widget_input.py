#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 16:43:45 2019

@author: daniel
"""

from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtWidgets import (QApplication, QComboBox, QDateTimeEdit,
        QDial, QWidget, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QDoubleSpinBox, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout)


class WidgetInput(QWidget):
    def __init__(self, parent=None):
        super(WidgetInput, self).__init__(parent)

        self.createTopGroup()
        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftTabWidget()
        self.createBottomRightGroupBox()
        self.createProgressBar()

        mainLayout = QGridLayout()
        mainLayout.addLayout(self.topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Input data")

        self.workflowComboBox.activated[str].connect(self.changeWorkflow)
        self.machineComboBox.activated[str].connect(self.changeWorkflow)
        self.equilibriumButton1.toggled.connect(self.toggleEquilibriumStatic)
        self.equilibriumButton2.toggled.connect(self.toggleEquilibriumSweeping)
        self.equilibriumButton3.toggled.connect(self.toggleEquilibriumMultiple)

    def changeWorkflow(self, styleName):
        print("Workflow set to", self.workflowComboBox.Text)
        
    def toggleEquilibriumStatic(self, state=0):
        print("Equilibrium static set to", state)
        
    def toggleEquilibriumSweeping(self, state=0):
        print("Equilibrium sweeping set to", state)
        if state==True:
            self.sweepAmplitudeLabel.show()
            self.sweepAmplitude.show()
            self.sweepFrequencyLabel.show()
            self.sweepFrequency.show()
        else:
            self.sweepAmplitudeLabel.hide()
            self.sweepAmplitude.hide()
            self.sweepFrequencyLabel.hide()
            self.sweepFrequency.hide()

    def toggleEquilibriumMultiple(self, state=0):
        print("Equilibrium multiple set to", state)
        
    def advanceProgressBar(self):
        curVal = self.progressBar.value()
        maxVal = self.progressBar.maximum()
        self.progressBar.setValue(curVal + (maxVal - curVal) / 100)

    def createTopGroup(self):
        self.idNumber = QLabel("1234567890")
        self.idLabel = QLabel("&ID:")
        self.idLabel.setBuddy(self.idNumber)

        self.workflowComboBox = QComboBox()
        self.workflowComboBox.addItems(["Concept", "Detail", "Operations", 
                                   "Sensitivity"])
        self.workflowLabel = QLabel("&Workflow:")
        self.workflowLabel.setBuddy(self.workflowComboBox)

        self.machineComboBox = QComboBox()
        self.machineComboBox.addItems(["ST40_P3", "ST140"])
        self.machineLabel = QLabel("&Machine settings:")
        self.machineLabel.setBuddy(self.machineComboBox)

        self.topLayout = QHBoxLayout()
        self.topLayout.addWidget(self.idLabel)
        self.topLayout.addWidget(self.idNumber)
        self.topLayout.addStretch(1)
        self.topLayout.addWidget(self.workflowLabel)
        self.topLayout.addWidget(self.workflowComboBox)
        self.topLayout.addStretch(1)
        self.topLayout.addWidget(self.machineLabel)
        self.topLayout.addWidget(self.machineComboBox)

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Equilibrium")

        self.equilibriumButton1 = QRadioButton("Static")
        self.equilibriumButton2 = QRadioButton("Sweeping")
        self.equilibriumButton3 = QRadioButton("Multiple")
        self.equilibriumButton1.setChecked(True)

        self.equilibriumComboBox = QComboBox()
        self.equilibriumComboBox.addItems(["eq002", "eq003"])
        self.equilibriumLabel = QLabel("&Equilibrium file:")
        self.equilibriumLabel.setBuddy(self.equilibriumComboBox)
        
        self.sweepAmplitude = QDoubleSpinBox()
        self.sweepAmplitudeLabel = QLabel("&Sweep Amplitude (mm):")
        self.sweepAmplitudeLabel.setBuddy(self.sweepAmplitude)
        self.sweepFrequency = QDoubleSpinBox()
        self.sweepFrequencyLabel = QLabel("&Sweep Frequency (Hz):")
        self.sweepFrequencyLabel.setBuddy(self.sweepAmplitude)

        layout = QVBoxLayout()
        layout.addWidget(self.equilibriumButton1)
        layout.addWidget(self.equilibriumButton2)
        layout.addWidget(self.equilibriumButton3)
        layout.addWidget(self.equilibriumLabel)
        layout.addWidget(self.equilibriumComboBox)
        layout.addWidget(self.sweepAmplitudeLabel)
        layout.addWidget(self.sweepAmplitude)
        layout.addWidget(self.sweepFrequencyLabel)
        layout.addWidget(self.sweepFrequency)
        
        self.sweepAmplitudeLabel.hide()
        self.sweepAmplitude.hide()
        self.sweepFrequencyLabel.hide()
        self.sweepFrequency.hide()
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)    

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("SOL parameters")

        self.plotPushButton = QPushButton("Default Push Button")
        self.plotPushButton.setDefault(True)

        togglePushButton = QPushButton("Toggle Push Button")
        togglePushButton.setCheckable(True)
        togglePushButton.setChecked(True)

        flatPushButton = QPushButton("Flat Push Button")
        flatPushButton.setFlat(True)

        layout = QVBoxLayout()
        layout.addWidget(self.plotPushButton)
        layout.addWidget(togglePushButton)
        layout.addWidget(flatPushButton)
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QTabWidget()
        self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Ignored)

        tab1 = QWidget()
        tableWidget = QTableWidget(10, 10)

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)

        tab2 = QWidget()
        textEdit = QTextEdit()

        textEdit.setPlainText("Twinkle, twinkle, little star,\n"
                              "How I wonder what you are.\n" 
                              "Up above the world so high,\n"
                              "Like a diamond in the sky.\n"
                              "Twinkle, twinkle, little star,\n" 
                              "How I wonder what you are!\n")

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

        self.bottomLeftTabWidget.addTab(tab1, "&Table")
        self.bottomLeftTabWidget.addTab(tab2, "Text &Edit")

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Group 3")
        self.bottomRightGroupBox.setCheckable(True)
        self.bottomRightGroupBox.setChecked(True)

        lineEdit = QLineEdit('s3cRe7')
        lineEdit.setEchoMode(QLineEdit.Password)

        spinBox = QSpinBox(self.bottomRightGroupBox)
        spinBox.setValue(50)

        dateTimeEdit = QDateTimeEdit(self.bottomRightGroupBox)
        dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        slider = QSlider(Qt.Horizontal, self.bottomRightGroupBox)
        slider.setValue(40)

        scrollBar = QScrollBar(Qt.Horizontal, self.bottomRightGroupBox)
        scrollBar.setValue(60)

        dial = QDial(self.bottomRightGroupBox)
        dial.setValue(30)
        dial.setNotchesVisible(True)

        layout = QGridLayout()
        layout.addWidget(lineEdit, 0, 0, 1, 2)
        layout.addWidget(spinBox, 1, 0, 1, 2)
        layout.addWidget(dateTimeEdit, 2, 0, 1, 2)
        layout.addWidget(slider, 3, 0)
        layout.addWidget(scrollBar, 4, 0)
        layout.addWidget(dial, 3, 1, 2, 1)
        layout.setRowStretch(5, 1)
        self.bottomRightGroupBox.setLayout(layout)

    def createProgressBar(self):
        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, 10000)
        self.progressBar.setValue(0)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetInput()
    gallery.show()
    sys.exit(app.exec_()) 