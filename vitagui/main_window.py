#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:30:31 2019

@author: daniel
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow, QWidget, QMenu, QMessageBox,
                             QVBoxLayout, QDockWidget, QTreeWidget)
from matplotlib_widget import staticMplCanvas
from widget_input import WidgetInput

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 Qt.CTRL + Qt.Key_Q)
        self.help_menu = QMenu('&Help', self)
        self.help_menu.addAction('&About', self.about)

        self.menuBar().addMenu(self.file_menu)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)
        
        self.setInitialLayout()

        self.statusBar().showMessage("VitaGUI initialized", 2000)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QMessageBox.about(self, "About",
                                    """vitaGUI.py 
Copyright 2019 Daniel Iglesias.

This program provides access to the vitaproject workflows via GUI.

It may be used and modified with no restriction; raw copies as well as
modified versions may be distributed under the LGPL license.

Checkout the Github repository at www.github.com/vitaproject"""
                                )
    def setInitialLayout(self):
        self.inputWidget = WidgetInput()

        self.plot_widget = QWidget(self)
        l = QVBoxLayout(self.plot_widget)
        sc = staticMplCanvas(self.plot_widget, width=5, height=5, dpi=100)
        sc2 = staticMplCanvas(self.plot_widget, width=5, height=5, dpi=100)
        l.addWidget(sc)
        l.addWidget(sc2)

        # self.plot_widget.setFocus()
        self.setCentralWidget(self.inputWidget)
        
        self.createDockWidget(self.plot_widget)
        self.dockWidget.hide()
        self.inputWidget.plotPushButton.clicked.connect(self.updatePlot)
        
    def updatePlot(self):
        self.dockWidget.show()
        
    def createDockWidget(self, theWidget):
        self.dockWidget = QDockWidget(self)
        self.dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = theWidget
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.addDockWidget(Qt.DockWidgetArea(2), self.dockWidget)
        self.dockWidget.setMinimumWidth(500)
        
        # self.dockWidgetContents.setObjectName("dockWidgetContents")
        # self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        # self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        # self.verticalLayout.setObjectName("verticalLayout")
        # self.treeWidget = QTreeWidget(self.dockWidgetContents)
        # self.treeWidget.setObjectName("treeWidget")
        # self.treeWidget.headerItem().setText(0, "1")
        # self.treeWidget.header().setVisible(False)
        # self.verticalLayout.addWidget(self.treeWidget)
        # self.dockWidget.setWidget(self.dockWidgetContents)
