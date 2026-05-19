# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtWidgets import (QComboBox, QHeaderView, QLabel, QLineEdit, 
                               QPushButton, QStackedWidget, QTableWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle(u"Kin-Santé Emergency Management System")
        MainWindow.setStyleSheet(u"QMainWindow { background-color: #1e1e2e; }")
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Central multi-page manager (QStackedWidget)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(50, 50, 700, 500))
        
        # ----------------------------------------------------------------------
        # PAGE 0 : MAIN MENU DASHBOARD
        # ----------------------------------------------------------------------
        self.page_menu = QWidget()
        self.page_menu.setObjectName(u"page_menu")
        
        self.label_title = QLabel(self.page_menu)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(150, 40, 400, 50))
        self.label_title.setText(u"KIN-SANTÉ EMERGENCY DASHBOARD")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setStyleSheet(u"font-size: 18px; font-weight: bold; color: #ffffff;")
        
        self.btn_go_to_register = QPushButton(self.page_menu)
        self.btn_go_to_register.setObjectName(u"btn_go_to_register")
        self.btn_go_to_register.setGeometry(QRect(250, 140, 200, 45))
        self.btn_go_to_register.setText(u"Register New Patient")
        
        self.btn_go_to_queue = QPushButton(self.page_menu)
        self.btn_go_to_queue.setObjectName(u"btn_go_to_queue")
        self.btn_go_to_queue.setGeometry(QRect(250, 210, 200, 45))
        self.btn_go_to_queue.setText(u"Monitor Triage Queue")
        
        self.btn_treat_next = QPushButton(self.page_menu)
        self.btn_treat_next.setObjectName(u"btn_treat_next")
        self.btn_treat_next.setGeometry(QRect(250, 280, 200, 45))
        self.btn_treat_next.setText(u"Treat Next Patient")
        
        self.btn_exit = QPushButton(self.page_menu)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(250, 350, 200, 45))
        self.btn_exit.setText(u"Exit System")
        
        self.stackedWidget.addWidget(self.page_menu)
        
        # ----------------------------------------------------------------------
        # PAGE 1 : PATIENT REGISTRATION FORM
        # ----------------------------------------------------------------------
        self.page_register = QWidget()
        self.page_register.setObjectName(u"page_register")
        
        self.label_reg_title = QLabel(self.page_register)
        self.label_reg_title.setObjectName(u"label_reg_title")
        self.label_reg_title.setGeometry(QRect(200, 20, 300, 40))
        self.label_reg_title.setText(u"PATIENT ADMISSION FORM")
        self.label_reg_title.setAlignment(Qt.AlignCenter)
        self.label_reg_title.setStyleSheet(u"font-size: 16px; font-weight: bold; color: #ffffff;")
        
        self.input_name = QLineEdit(self.page_register)
        self.input_name.setObjectName(u"input_name")
        self.input_name.setGeometry(QRect(250, 90, 200, 35))
        self.input_name.setPlaceholderText(u"Patient Full Name")
        
        self.input_id = QLineEdit(self.page_register)
        self.input_id.setObjectName(u"input_id")
        self.input_id.setGeometry(QRect(250, 150, 200, 35))
        self.input_id.setPlaceholderText(u"Patient ID Number")
        
        self.input_condition = QLineEdit(self.page_register)
        self.input_condition.setObjectName(u"input_condition")
        self.input_condition.setGeometry(QRect(250, 210, 200, 35))
        self.input_condition.setPlaceholderText(u"Medical Symptoms / Status")
        
        self.combo_priority = QComboBox(self.page_register)
        self.combo_priority.setObjectName(u"combo_priority")
        self.combo_priority.setGeometry(QRect(250, 270, 200, 35))
        self.combo_priority.addItems([
            u"1 - Non-Urgent", 
            u"2 - Less Urgent", 
            u"3 - Urgent", 
            u"4 - Highly Urgent", 
            u"5 - Critical Emergency"
        ])
        
        self.btn_save_patient = QPushButton(self.page_register)
        self.btn_save_patient.setObjectName(u"btn_save_patient")
        self.btn_save_patient.setGeometry(QRect(190, 350, 140, 45))
        self.btn_save_patient.setText(u"Save Patient")
        
        self.btn_back_from_reg = QPushButton(self.page_register)
        self.btn_back_from_reg.setObjectName(u"btn_back_from_reg")
        self.btn_back_from_reg.setGeometry(QRect(370, 350, 140, 45))
        self.btn_back_from_reg.setText(u"Back to Menu")
        
        self.stackedWidget.addWidget(self.page_register)
        
        # ----------------------------------------------------------------------
        # PAGE 2 : TRIAGE QUEUE MONITOR
        # ----------------------------------------------------------------------
        self.page_queue = QWidget()
        self.page_queue.setObjectName(u"page_queue")
        
        self.label_queue_title = QLabel(self.page_queue)
        self.label_queue_title.setObjectName(u"label_queue_title")
        self.label_queue_title.setGeometry(QRect(200, 15, 300, 30))
        self.label_queue_title.setText(u"LIVE TRIAGE PRIORITY MONITOR")
        self.label_queue_title.setAlignment(Qt.AlignCenter)
        self.label_queue_title.setStyleSheet(u"font-size: 16px; font-weight: bold; color: #ffffff;")
        
        self.table_queue = QTableWidget(self.page_queue)
        self.table_queue.setObjectName(u"table_queue")
        self.table_queue.setGeometry(QRect(40, 60, 620, 320))
        self.table_queue.setColumnCount(4)
        self.table_queue.setHorizontalHeaderLabels([u"Priority Level", u"Patient ID", u"Full Name", u"Condition Status"])
        self.table_queue.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.btn_back_from_queue = QPushButton(self.page_queue)
        self.btn_back_from_queue.setObjectName(u"btn_back_from_queue")
        self.btn_back_from_queue.setGeometry(QRect(280, 400, 140, 45))
        self.btn_back_from_queue.setText(u"Back to Menu")
        
        self.stackedWidget.addWidget(self.page_queue)
        
        QMetaObject.connectSlotsByName(MainWindow)