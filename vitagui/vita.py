#############################################################################
##
## Copyright (C) 2016 The Qt Company Ltd.
## Contact: http://www.qt.io/licensing/
##
## This file is part of the Qt for Python examples of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
## $QT_END_LICENSE$
##
#############################################################################

import os
import sys
import argparse
import json

# import pandas as pd
from PyQt5 import QtWidgets

import vita.utility.resource_manager as rm
from vitagui.main_window import MainWindow

progname = os.path.basename(sys.argv[0])
progversion = "0.1"



def main():
    resources = rm.list_resources()
    # print(resources)
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, required=False)
    args = parser.parse_args()
    if args.file:
        input_file = args.file
        print("Opening file", input_file)
    elif os.path.isfile(resources['path']+'/default.json'):
        input_file = resources['path']+'/default.json'
        print ("Opening file", input_file)
        
    # Qt Application
    qApp = QtWidgets.QApplication(sys.argv)
    
    vitawindow = MainWindow()
    vitawindow.setWindowTitle("%s" % progname)
    vitawindow.setResources(resources)
    if input_file:
        with open(input_file, 'r') as fh:
            vita_input = json.load(fh)
        vitawindow.setInputFile(vita_input)
    vitawindow.show()
    sys.exit(qApp.exec_())

if __name__ == '__main__':
    main()
