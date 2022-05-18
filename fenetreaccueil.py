# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:53:37 2022

@author: LELEU
"""

import dbm
import sys
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,
                             QApplication, QMainWindow, QWidget ,QLabel,QRadioButton,
                             QCheckBox)
from PyQt5.QtGui import QPixmap , QIcon
 
from PyQt5 import QtCore 

from fenetrelumieres import FenetreLumieres

import json
import urllib.request

class View(QWidget):
    def __init__(self):
        super().__init__()
        
        self.faccueil = FenetreLumieres(self)
        
        self.bvolet = QPushButton('Menu Volets')
        self.bvolet.setStyleSheet("background-color: rgb(94,213,207) ; border-style: outset ; border-width: 0 px; border-radius: 5px;  color : white ; padding: 4px")
        self.blumieres = QPushButton('Menu lumières')
        self.blumieres.setStyleSheet("background-color: rgb(94,213,207) ; border-style: outset ; border-width: 0 px; border-radius: 5px ; color : white ; padding: 4px")
        self.bbeeper = QPushButton('Beeper')
        self.bbeeper.setStyleSheet("background-color: rgb(94,213,207) ; border-style: outset ; border-width: 0 px; border-radius: 5px;  color : white ; padding: 4px")
        
        
        self.label = QLabel(self)
        self.pixmap = QPixmap('photointer.png')
        self.label.setPixmap(self.pixmap)     
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        #BEGIN TEST

        #END TEST
        
        
         
        self.init_ui1()
        
        self.blumieres.clicked.connect(self.blumieres_click)
        
        self.show()
        
    def init_ui1(self):
        
       
        
        
        v_photo = QVBoxLayout()
        
        #BEGIN TEST

        #END TEST
        
        v_photo.addWidget(self.label)

        v_box = QHBoxLayout()
        v_box.addWidget(self.bvolet)
        v_box.addWidget(self.blumieres)
        v_box.addWidget(self.bbeeper)
        
        
        h_box = QVBoxLayout()
        h_box.addLayout(v_photo)
        h_box.addLayout(v_box)
        
        self.setLayout(h_box) 
        
        self.setGeometry(400,400    ,500,200)
        self.setWindowTitle('Domo')
        self.setWindowIcon(QIcon('photointer.png'))
        
    def blumieres_click(self):
        self.hide()
        self.faccueil.show()
        
        
 
        
app = QApplication(sys.argv)
interface = View()
sys.exit(app.exec_())            
        
        
        