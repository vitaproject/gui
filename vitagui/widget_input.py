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
        QVBoxLayout, QCheckBox)


class WidgetInput(QWidget):
    def __init__(self, parent=None):
        super(WidgetInput, self).__init__(parent)

        self.createTopGroup()
        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createtopLeftTabWidget()
        self.createBottomRightGroupBox()
        self.createProgressBar()

        mainLayout = QGridLayout()
        mainLayout.addLayout(self.topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftTabWidget, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomLeftGroupBox, 2, 0)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Input data")

        self.workflowComboBox.activated[str].connect(self.changeWorkflow)
        self.machineComboBox.activated[str].connect(self.changeMachine)
        self.equilibriumButton1.toggled.connect(self.toggleEquilibriumStatic)
        self.equilibriumButton2.toggled.connect(self.toggleEquilibriumSweeping)
        self.equilibriumButton3.toggled.connect(self.toggleEquilibriumMultiple)

    def setResources(self, inputResources):
        self.machineComboBox.addItems(inputResources['machines'])
        self.equilibrium_dict = inputResources['equilibrium']
        self.equilibriumComboBox.clear()
        self.equilibriumComboBox.addItems(self.equilibrium_dict
                                          [self.machineComboBox.currentText()])
        self.textEditResources.setPlainText(str(inputResources))

    def setData(self, inputData):
        self.data = inputData
        self.textEditData.setPlainText(str(self.data))
        if 'heating' in self.data['plasma-settings']:
            aux_power = 0.0
            if 'NBI-power' in self.data['plasma-settings']['heating'] : 
                aux_power += self.data['plasma-settings']['heating']['NBI-power']
            if 'rf-power' in self.data['plasma-settings']['heating'] : 
                aux_power += self.data['plasma-settings']['heating']['rf-power']
            if 'Ohmic-power' in self.data['plasma-settings']['heating'] : 
                aux_power += self.data['plasma-settings']['heating']['Ohmic-power']
            self.pauxDSB.setValue(aux_power)


    def changeWorkflow(self, styleName):
        print("Workflow set to", self.workflowComboBox.currentText())
        
    def changeMachine(self, styleName):
        print("Machine set to", self.machineComboBox.currentText())
        self.equilibriumComboBox.clear()
        self.equilibriumComboBox.addItems(self.equilibrium_dict
                                          [self.machineComboBox.currentText()])
        
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
        self.idNumber = QSpinBox()
        self.idNumber.setRange(0,9999)
        self.idNumber.setValue(1234)
        self.idLabel = QLabel("&ID:")
        self.idLabel.setBuddy(self.idNumber)

        self.workflowComboBox = QComboBox()
        self.workflowComboBox.addItems(["Concept", "Detail", "Operations", 
                                   "Sensitivity"])
        self.workflowLabel = QLabel("&Workflow:")
        self.workflowLabel.setBuddy(self.workflowComboBox)

        self.machineComboBox = QComboBox()
        # self.machineComboBox.addItems(["ST40_P3", "ST140"])
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
        self.topLeftTabWidget = QTabWidget()
        # self.topLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
                # QSizePolicy.Ignored)

        tab1 = QWidget()
        # tableWidget = QTableWidget(10, 10)
        tab1hbox = QGridLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        # tab1hbox.addWidget(tableWidget)

        isotopeLabel = QLabel("Isotopes")
        self.hydrogenButton = QRadioButton("H/D")
        self.DTButton = QRadioButton("D-T")
        self.hydrogenButton.setChecked(True)


        bottomLeftGroupBoxPower = QGroupBox("SOL Power")
        # self.lambdaLabel = QLabel("&Lambda_q (mm):")
        self.pauxBox = QCheckBox("Paux (MW)")
        self.pauxDSB = QDoubleSpinBox()
        self.pauxBox.setChecked(True)
        self.pradBox = QCheckBox("Prad:")
        self.pradfractionButton = QRadioButton("Ratio (%)")
        self.pradfractionDSB = QDoubleSpinBox()
        self.pradvalueButton = QRadioButton("Value (MW)")
        self.pradvalueDSB = QDoubleSpinBox()
        self.pradBox.setChecked(True)
        self.pradvalueButton.setChecked(True)


        layout = QGridLayout()
        # layout.addWidget(self.lambdaLabel,       0, 0, 1, 2)
        layout.addWidget(self.pauxBox,            1, 0)
        layout.addWidget(self.pauxDSB,            1, 1)
        layout.addWidget(self.pradBox,            2, 0)
        layout.addWidget(self.pradfractionButton, 3, 0)
        layout.addWidget(self.pradfractionDSB,    3, 1)
        layout.addWidget(self.pradvalueButton,    4, 0)
        layout.addWidget(self.pradvalueDSB,       4, 1)
        bottomLeftGroupBoxPower.setLayout(layout)

        bottomLeftGroupBoxOther = QGroupBox("Target fractions")
        # self.lambdaLabel = QLabel("&Lambda_q (mm):")
        self.shareButton = QRadioButton("Manual")
        self.drsepButton = QRadioButton("DRsep")
        self.shareButton.setChecked(True)
        self.uhfsLabel = QLabel("Up HFS")
        self.uhfsDSB = QDoubleSpinBox()
        self.uhfsLabel.setBuddy(self.uhfsDSB)
        self.ulfsLabel = QLabel("Up LFS")
        self.ulfsDSB = QDoubleSpinBox()
        self.ulfsLabel.setBuddy(self.ulfsDSB)
        self.dhfsLabel = QLabel("Down HFS")
        self.dhfsDSB = QDoubleSpinBox()
        self.dhfsLabel.setBuddy(self.dhfsDSB)
        self.dlfsLabel = QLabel("down HFS")
        self.dlfsDSB = QDoubleSpinBox()
        self.dlfsLabel.setBuddy(self.dlfsDSB)
        
        layout = QGridLayout()
        # layout.addWidget(self.lambdaLabel,       0, 0, 1, 2)
        layout.addWidget(self.shareButton,      1, 0)
        layout.addWidget(self.drsepButton,      1, 1)
        layout.addWidget(self.uhfsLabel,        2, 0)
        layout.addWidget(self.uhfsDSB,          2, 1)
        layout.addWidget(self.ulfsLabel,        3, 0)
        layout.addWidget(self.ulfsDSB,          3, 1)
        layout.addWidget(self.dhfsLabel,        4, 0)
        layout.addWidget(self.dhfsDSB,          4, 1)
        layout.addWidget(self.dlfsLabel,        5, 0)
        layout.addWidget(self.dlfsDSB,          5, 1)
        bottomLeftGroupBoxOther.setLayout(layout)

        tab1hbox.addWidget(isotopeLabel,   1, 0)
        tab1hbox.addWidget(self.hydrogenButton, 1, 1)
        tab1hbox.addWidget(self.DTButton, 1, 2)
        tab1hbox.addWidget(bottomLeftGroupBoxPower, 2, 0, 1, 3)
        tab1hbox.addWidget(bottomLeftGroupBoxOther, 3, 0, 1, 3)
        tab1.setLayout(tab1hbox)

        tab2 = QWidget()
        self.textEditData = QTextEdit()

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(self.textEditData)
        tab2.setLayout(tab2hbox)

        tab3 = QWidget()
        self.textEditResources = QTextEdit()

        tab3hbox = QHBoxLayout()
        tab3hbox.setContentsMargins(5, 5, 5, 5)
        tab3hbox.addWidget(self.textEditResources)
        tab3.setLayout(tab3hbox)

        self.topLeftTabWidget.addTab(tab1, "Parameters")
        self.topLeftTabWidget.addTab(tab2, "Input data")
        self.topLeftTabWidget.addTab(tab3, "Local resources")

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("SOL parameters")

        topRightGroupBoxLambda = QGroupBox("Lambda_q (mm)")
        # self.lambdaLabel = QLabel("&Lambda_q (mm):")
        self.mmButton = QRadioButton("MM 2011")
        self.mmDSB = QDoubleSpinBox()
        self.eichButton = QRadioButton("Eich #15")
        self.eichDSB = QDoubleSpinBox()
        self.lambdaManualButton = QRadioButton("Manual")
        self.lambdaManualDSB = QDoubleSpinBox()
        self.lambdaManualButton.setChecked(True)

        layout = QGridLayout()
        # layout.addWidget(self.lambdaLabel,       0, 0, 1, 2)
        layout.addWidget(self.mmButton,          1, 0)
        layout.addWidget(self.mmDSB,             1, 1)
        layout.addWidget(self.eichButton,        2, 0)
        layout.addWidget(self.eichDSB,           2, 1)
        layout.addWidget(self.lambdaManualButton,3, 0)
        layout.addWidget(self.lambdaManualDSB,   3, 1)
        topRightGroupBoxLambda.setLayout(layout)

        topRightGroupBoxS = QGroupBox("S (mm)")
        # self.sLabel = QLabel("&S (mm):")
        self.sFractionButton = QRadioButton("Fraction")
        self.sFractionDSB = QDoubleSpinBox()
        self.sManualButton = QRadioButton("Manual")
        self.sManualDSB = QDoubleSpinBox()
        self.sManualButton.setChecked(True)

        layout = QGridLayout()
        # layout.addWidget(self.sLabel,            4, 0, 1, 2)
        layout.addWidget(self.sFractionButton,    5, 0)
        layout.addWidget(self.sFractionDSB,       5, 1)
        layout.addWidget(self.sManualButton,     6, 0)
        layout.addWidget(self.sManualDSB,        6, 1)
        topRightGroupBoxS.setLayout(layout)

        layout = QVBoxLayout()
        layout.addWidget(topRightGroupBoxLambda)
        layout.addWidget(topRightGroupBoxS)

        self.topRightGroupBox.setLayout(layout)

    def createtopLeftTabWidget(self):
        self.bottomLeftGroupBox = QGroupBox("Equilibrium")

        self.equilibriumButton1 = QRadioButton("Static")
        self.equilibriumButton2 = QRadioButton("Sweeping")
        self.equilibriumButton3 = QRadioButton("Multiple")
        self.equilibriumButton1.setChecked(True)

        self.equilibriumComboBox = QComboBox()
        # self.equilibriumComboBox.addItems(["eq002", "eq003"])
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
        self.bottomLeftGroupBox.setLayout(layout)    

    def createBottomRightGroupBox(self):
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

        self.bottomRightGroupBox = QGroupBox("Group 3")
        self.bottomRightGroupBox.setCheckable(True)
        self.bottomRightGroupBox.setChecked(True)
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