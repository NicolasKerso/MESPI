# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:44:45 2022

@author: leleu
"""

import dbm
import sys
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,
                             QApplication, QMainWindow, QWidget ,QLabel,QRadioButton,
                             QCheckBox)
from PyQt5.QtGui import QPixmap , QIcon
from qtwidgets  import AnimatedToggle
from PyQt5 import QtCore 
import json
import urllib.request

class FenetreLumieres(QWidget) : 
    def __init__(self , faccueil):
        super().__init__()  

        self.setStyleSheet("background-color: rgb(230,230,230);")
        
        self.labellampe1 = QLabel(self)
        self.chklampe1 = AnimatedToggle(
            checked_color="#5ED5CF",
            pulse_checked_color="#44FFB000"
        )

        
        self.labellampe2 = QLabel(self)
        self.chklampe2 = AnimatedToggle(
            checked_color="#5ED5CF",
            pulse_checked_color="#44FFB000"
        )
        
        self.label = QLabel(self)
        self.pixmap = QPixmap('photolumieres.png')
        self.label.setPixmap(self.pixmap)     
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        
        
        self.faccueil = faccueil
        self.init_ui()
        
        self.chklampe1.clicked.connect(self.chkl1_click)
        self.chklampe2.clicked.connect(self.chkl2_click)
        
    
    def init_ui(self):
        
        
         #BEGIN TEST
        v_lampe = QVBoxLayout()
        v_lampe.addWidget(self.labellampe1)
        
        v_chk = QVBoxLayout()
        v_chk.addWidget(self.chklampe1)
        url = "http://172.16.201.100:5000"
        data = urllib.request.urlopen(url).read().decode()
        valJson = json.loads(data)
        etat1 = valJson["lampe1"]
        etat2 = valJson["lampe2"]
        print(data)
        print(valJson["lampe1"])
        print(valJson["lampe2"])
        self.labellampe1.setText("Lampe 1 = "+str(etat1))
       
        self.labellampe2.setText("Lampe 2 = "+str(etat2))


        if etat1==0:
            self.chklampe1.setChecked(False) 
            self.labellampe1.setText("Lampe 1 = "+str(etat1) + "lampe éteinte")
            self.pixmapl1e = QPixmap('photolumieresteinte.png')
            self.label2.setPixmap(self.pixmapl1e)
   
            
            
        else:
            self.chklampe1.setChecked(True)
            self.labellampe1.setText("Lampe 1 = "+str(etat1) + "lampe allumée")
            self.pixmapl1a = QPixmap('photolumieresallumee.png')
            self.label2.setPixmap(self.pixmapl1a)


        
        if etat2==0:
             self.chklampe2.setChecked(False) 
             self.labellampe2.setText("Lampe 2 = "+str(etat2) + "lampe éteinte")
             self.pixmapl2e = QPixmap('photolumiereseteinte.png')
             self.label3.setPixmap(self.pixmapl2e)
             

        else:
             self.chklampe2.setChecked(True) 
             self.labellampe2.setText("Lampe 2 = "+str(etat2) + "lampe allumée")
             self.pixmapl2a = QPixmap('photolumieresallumee.png')
             self.label3.setPixmap(self.pixmapl2a)
            
    
      
    
        
        #END TEST
        
        #v_photo.addWidget(self.label)
        
        
        v_photo = QVBoxLayout()
        v_photo.addWidget(self.label)

        v_box = QHBoxLayout()
        v_box.addWidget(self.labellampe1)
        v_box.addWidget(self.chklampe1)
        v_box.addWidget(self.label2)
        v_box.addStretch()
        
        v_deux = QHBoxLayout()
        v_deux.addWidget(self.labellampe2)
        v_deux.addWidget(self.chklampe2)
        v_deux.addWidget(self.label3)
        v_deux.addStretch()
        

        
        
        h_box = QVBoxLayout()
        h_box.addLayout(v_photo)
        h_box.addLayout(v_box)
        h_box.addLayout(v_deux)
        
        self.setLayout(h_box) 
        
        
        self.setGeometry(600,400,500,200)
        self.setWindowTitle('Domo : Lumieres')
        self.setWindowIcon(QIcon('photolumieres.png'))
        
    def chkl1_click(self) : 
        if self.chklampe1.isChecked() == True:
            self.labellampe1.setText("Lampe 1 = " + "lampe allumée")
            self.pixmapl1a = QPixmap('photolumieresallumee.png')
            self.label2.setPixmap(self.pixmapl1a) 
            

        else : 
            self.labellampe1.setText("Lampe 1 = " + "lampe éteinte")
            self.pixmapl1e = QPixmap('photolumiereseteinte.png')
            self.label2.setPixmap(self.pixmapl1e) 
            
    def chkl2_click(self):
        if self.chklampe2.isChecked() == True:
            self.labellampe2.setText("Lampe 2 = " + "lampe allumée")
            self.pixmapl2a = QPixmap('photolumieresallumee.png')
            self.label3.setPixmap(self.pixmapl2a)
        else : 
            self.labellampe2.setText("Lampe 2 = " + "lampe éteinte")
            self.pixmapl2e = QPixmap('photolumiereseteinte.png')
            self.label3.setPixmap(self.pixmapl2e)
        
        
        
        
        
        
        