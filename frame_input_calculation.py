# -*- coding: utf-8 -*-
import os.path

# Form implementation generated from reading ui file 'Боря гей.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QBrush, QPixmap


class Ui_frame_input(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));")
        self.toolBox.setObjectName("toolBox")
        self.page_cost_forming = QtWidgets.QWidget()
        self.page_cost_forming.setGeometry(QtCore.QRect(0, 0, 456, 526))
        self.page_cost_forming.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.page_cost_forming.setObjectName("page_cost_forming")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_cost_forming)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_cost_forming = QtWidgets.QFrame(self.page_cost_forming)
        self.frame_cost_forming.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cost_forming.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cost_forming.setObjectName("frame_cost_forming")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_cost_forming)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.toolBox_2 = QtWidgets.QToolBox(self.frame_cost_forming)
        self.toolBox_2.setObjectName("toolBox_2")
        self.page_B = QtWidgets.QWidget()
        self.page_B.setGeometry(QtCore.QRect(0, 0, 430, 434))
        self.page_B.setObjectName("page_B")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_B)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frameB = QtWidgets.QFrame(self.page_B)
        self.frameB.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frameB.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameB.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameB.setObjectName("frameB")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameB)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.L_B = QtWidgets.QLabel(self.frameB)
        self.L_B.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.L_B.setObjectName("L_B")
        self.horizontalLayout.addWidget(self.L_B)
        self.frame_B_B_enter = QtWidgets.QLineEdit(self.frameB)
        self.frame_B_B_enter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.frame_B_B_enter.setObjectName("frame_B_B_enter")
        self.horizontalLayout.addWidget(self.frame_B_B_enter)
        self.enter_frame_B = QtWidgets.QPushButton(self.frameB)
        self.enter_frame_B.setObjectName("enter_frame_B")
        self.horizontalLayout.addWidget(self.enter_frame_B)
        self.verticalLayout_5.addWidget(self.frameB)
        self.frame_2 = QtWidgets.QFrame(self.page_B)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5.addWidget(self.frame_2)
        self.toolBox_2.addItem(self.page_B, "")
        self.page_Forming = QtWidgets.QWidget()
        self.page_Forming.setGeometry(QtCore.QRect(0, 0, 430, 434))
        self.page_Forming.setObjectName("page_Forming")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_Forming)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.FrameForming = QtWidgets.QFrame(self.page_Forming)
        self.FrameForming.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameForming.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameForming.setObjectName("FrameForming")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.FrameForming)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_repair_tools = QtWidgets.QFrame(self.FrameForming)
        self.frame_repair_tools.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_repair_tools.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_repair_tools.setObjectName("frame_repair_tools")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_repair_tools)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.L_number_repair_tools = QtWidgets.QLabel(self.frame_repair_tools)
        self.L_number_repair_tools.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.L_number_repair_tools.setObjectName("L_number_repair_tools")
        self.horizontalLayout_5.addWidget(self.L_number_repair_tools)
        self.Enter_number_repair_tools = QtWidgets.QLineEdit(self.frame_repair_tools)
        self.Enter_number_repair_tools.setObjectName("Enter_number_repair_tools")
        self.horizontalLayout_5.addWidget(self.Enter_number_repair_tools)
        self.verticalLayout.addWidget(self.frame_repair_tools)
        self.frame_cost_repair_facilities = QtWidgets.QFrame(self.FrameForming)
        self.frame_cost_repair_facilities.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cost_repair_facilities.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cost_repair_facilities.setObjectName("frame_cost_repair_facilities")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_cost_repair_facilities)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.L_cost_repair_facilities = QtWidgets.QLabel(self.frame_cost_repair_facilities)
        self.L_cost_repair_facilities.setObjectName("L_cost_repair_facilities")
        self.horizontalLayout_4.addWidget(self.L_cost_repair_facilities)
        self.Enter_cost_repair_facilities = QtWidgets.QLineEdit(self.frame_cost_repair_facilities)
        self.Enter_cost_repair_facilities.setObjectName("Enter_cost_repair_facilities")
        self.horizontalLayout_4.addWidget(self.Enter_cost_repair_facilities)
        self.verticalLayout.addWidget(self.frame_cost_repair_facilities)
        self.frame_number_repairmen = QtWidgets.QFrame(self.FrameForming)
        self.frame_number_repairmen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_number_repairmen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_number_repairmen.setObjectName("frame_number_repairmen")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_number_repairmen)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.L_number_repairmen = QtWidgets.QLabel(self.frame_number_repairmen)
        self.L_number_repairmen.setObjectName("L_number_repairmen")
        self.horizontalLayout_3.addWidget(self.L_number_repairmen)
        self.Enter_number_repairmen = QtWidgets.QLineEdit(self.frame_number_repairmen)
        self.Enter_number_repairmen.setObjectName("Enter_number_repairmen")
        self.horizontalLayout_3.addWidget(self.Enter_number_repairmen)
        self.verticalLayout.addWidget(self.frame_number_repairmen)
        self.frame_cost_preparation = QtWidgets.QFrame(self.FrameForming)
        self.frame_cost_preparation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cost_preparation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cost_preparation.setObjectName("frame_cost_preparation")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_cost_preparation)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.L_cost_preparation = QtWidgets.QLabel(self.frame_cost_preparation)
        self.L_cost_preparation.setObjectName("L_cost_preparation")
        self.horizontalLayout_20.addWidget(self.L_cost_preparation)
        self.Enter_cost_preparation = QtWidgets.QLineEdit(self.frame_cost_preparation)
        self.Enter_cost_preparation.setObjectName("Enter_cost_preparation")
        self.horizontalLayout_20.addWidget(self.Enter_cost_preparation)
        self.verticalLayout.addWidget(self.frame_cost_preparation)
        self.button_frame_forming = QtWidgets.QFrame(self.FrameForming)
        self.button_frame_forming.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame_forming.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame_forming.setObjectName("button_frame_forming")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.button_frame_forming)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_frame_forming_enter = QtWidgets.QPushButton(self.button_frame_forming)
        self.button_frame_forming_enter.setObjectName("button_frame_forming_enter")
        self.horizontalLayout_2.addWidget(self.button_frame_forming_enter)
        self.button_frame_forming_next = QtWidgets.QPushButton(self.button_frame_forming)
        self.button_frame_forming_next.setObjectName("button_frame_forming_next")
        self.horizontalLayout_2.addWidget(self.button_frame_forming_next)
        self.verticalLayout.addWidget(self.button_frame_forming)
        self.verticalLayout_4.addWidget(self.FrameForming)
        self.toolBox_2.addItem(self.page_Forming, "")
        self.page_repair_evacuation = QtWidgets.QWidget()
        self.page_repair_evacuation.setGeometry(QtCore.QRect(0, 0, 430, 434))
        self.page_repair_evacuation.setObjectName("page_repair_evacuation")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_repair_evacuation)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_8 = QtWidgets.QFrame(self.page_repair_evacuation)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_submission = QtWidgets.QFrame(self.frame_8)
        self.frame_submission.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_submission.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_submission.setObjectName("frame_submission")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_submission)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.L_submission = QtWidgets.QLabel(self.frame_submission)
        self.L_submission.setObjectName("L_submission")
        self.horizontalLayout_21.addWidget(self.L_submission)
        self.verticalLayout_7.addWidget(self.frame_submission)
        self.frame_number_repair_evacuation = QtWidgets.QFrame(self.frame_8)
        self.frame_number_repair_evacuation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_number_repair_evacuation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_number_repair_evacuation.setObjectName("frame_number_repair_evacuation")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_number_repair_evacuation)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.L_number_repair_evacuation = QtWidgets.QLabel(self.frame_number_repair_evacuation)
        self.L_number_repair_evacuation.setObjectName("L_number_repair_evacuation")
        self.horizontalLayout_6.addWidget(self.L_number_repair_evacuation)
        self.Enter_number_repair_evacuation = QtWidgets.QLineEdit(self.frame_number_repair_evacuation)
        self.Enter_number_repair_evacuation.setObjectName("Enter_number_repair_evacuation")
        self.horizontalLayout_6.addWidget(self.Enter_number_repair_evacuation)
        self.verticalLayout_7.addWidget(self.frame_number_repair_evacuation)
        self.frame_cost_repair_evacuation = QtWidgets.QFrame(self.frame_8)
        self.frame_cost_repair_evacuation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cost_repair_evacuation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cost_repair_evacuation.setObjectName("frame_cost_repair_evacuation")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_cost_repair_evacuation)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.L_cost_repair_evacuation = QtWidgets.QLabel(self.frame_cost_repair_evacuation)
        self.L_cost_repair_evacuation.setObjectName("L_cost_repair_evacuation")
        self.horizontalLayout_7.addWidget(self.L_cost_repair_evacuation)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_cost_repair_evacuation)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_7.addWidget(self.lineEdit_6)
        self.verticalLayout_7.addWidget(self.frame_cost_repair_evacuation)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.frame_enter_repair_evacuation = QtWidgets.QFrame(self.page_repair_evacuation)
        self.frame_enter_repair_evacuation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_enter_repair_evacuation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_enter_repair_evacuation.setObjectName("frame_enter_repair_evacuation")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_enter_repair_evacuation)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Enter_number_repair_evacuation_2 = QtWidgets.QPushButton(self.frame_enter_repair_evacuation)
        self.Enter_number_repair_evacuation_2.setObjectName("Enter_number_repair_evacuation_2")
        self.horizontalLayout_8.addWidget(self.Enter_number_repair_evacuation_2)
        self.button_evacuation_next = QtWidgets.QPushButton(self.frame_enter_repair_evacuation)
        self.button_evacuation_next.setObjectName("button_evacuation_next")
        self.horizontalLayout_8.addWidget(self.button_evacuation_next)
        self.verticalLayout_6.addWidget(self.frame_enter_repair_evacuation)
        self.toolBox_2.addItem(self.page_repair_evacuation, "")
        self.verticalLayout_3.addWidget(self.toolBox_2)
        self.verticalLayout_2.addWidget(self.frame_cost_forming)
        self.toolBox.addItem(self.page_cost_forming, "")
        self.page_cost_repair = QtWidgets.QWidget()
        self.page_cost_repair.setGeometry(QtCore.QRect(0, 0, 456, 526))
        self.page_cost_repair.setObjectName("page_cost_repair")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_cost_repair)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_belt_work = QtWidgets.QFrame(self.page_cost_repair)
        self.frame_belt_work.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_belt_work.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_belt_work.setObjectName("frame_belt_work")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_belt_work)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_belt_work_T = QtWidgets.QFrame(self.frame_belt_work)
        self.frame_belt_work_T.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_belt_work_T.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_belt_work_T.setObjectName("frame_belt_work_T")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_belt_work_T)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.L_frame_belt_work_T = QtWidgets.QLabel(self.frame_belt_work_T)
        self.L_frame_belt_work_T.setObjectName("L_frame_belt_work_T")
        self.horizontalLayout_12.addWidget(self.L_frame_belt_work_T)
        self.Entry_belt_work_T = QtWidgets.QLineEdit(self.frame_belt_work_T)
        self.Entry_belt_work_T.setObjectName("Entry_belt_work_T")
        self.horizontalLayout_12.addWidget(self.Entry_belt_work_T)
        self.verticalLayout_9.addWidget(self.frame_belt_work_T)
        self.frame_belt_work_C_repair = QtWidgets.QFrame(self.frame_belt_work)
        self.frame_belt_work_C_repair.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_belt_work_C_repair.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_belt_work_C_repair.setObjectName("frame_belt_work_C_repair")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_belt_work_C_repair)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.L_frame_belt_work_C_repair = QtWidgets.QLabel(self.frame_belt_work_C_repair)
        self.L_frame_belt_work_C_repair.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.L_frame_belt_work_C_repair.setObjectName("L_frame_belt_work_C_repair")
        self.horizontalLayout_11.addWidget(self.L_frame_belt_work_C_repair)
        self.Entry_belt_work_C_repair = QtWidgets.QLineEdit(self.frame_belt_work_C_repair)
        self.Entry_belt_work_C_repair.setObjectName("Entry_belt_work_C_repair")
        self.horizontalLayout_11.addWidget(self.Entry_belt_work_C_repair)
        self.verticalLayout_9.addWidget(self.frame_belt_work_C_repair)
        self.frame_button_frame_belt_work = QtWidgets.QFrame(self.frame_belt_work)
        self.frame_button_frame_belt_work.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_button_frame_belt_work.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_button_frame_belt_work.setObjectName("frame_button_frame_belt_work")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_button_frame_belt_work)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.button_frame_belt_work = QtWidgets.QPushButton(self.frame_button_frame_belt_work)
        self.button_frame_belt_work.setObjectName("button_frame_belt_work")
        self.horizontalLayout_9.addWidget(self.button_frame_belt_work)
        self.verticalLayout_9.addWidget(self.frame_button_frame_belt_work)
        self.verticalLayout_8.addWidget(self.frame_belt_work)
        self.toolBox.addItem(self.page_cost_repair, "")
        self.page_cost_transportation = QtWidgets.QWidget()
        self.page_cost_transportation.setGeometry(QtCore.QRect(0, 0, 456, 526))
        self.page_cost_transportation.setObjectName("page_cost_transportation")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_cost_transportation)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_cost_transportation = QtWidgets.QFrame(self.page_cost_transportation)
        self.frame_cost_transportation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cost_transportation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cost_transportation.setObjectName("frame_cost_transportation")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_cost_transportation)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.qtool_box_2 = QtWidgets.QToolBox(self.frame_cost_transportation)
        self.qtool_box_2.setObjectName("qtool_box_2")
        self.page_distance_2 = QtWidgets.QWidget()
        self.page_distance_2.setGeometry(QtCore.QRect(0, 0, 430, 456))
        self.page_distance_2.setObjectName("page_distance_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_distance_2)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_cost_kilometer = QtWidgets.QFrame(self.page_distance_2)
        self.frame_cost_kilometer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cost_kilometer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cost_kilometer.setObjectName("frame_cost_kilometer")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_cost_kilometer)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_cost_kilometer = QtWidgets.QLabel(self.frame_cost_kilometer)
        self.label_cost_kilometer.setObjectName("label_cost_kilometer")
        self.horizontalLayout_14.addWidget(self.label_cost_kilometer)
        self.enter_cost_kilometer = QtWidgets.QLineEdit(self.frame_cost_kilometer)
        self.enter_cost_kilometer.setObjectName("enter_cost_kilometer")
        self.horizontalLayout_14.addWidget(self.enter_cost_kilometer)
        self.verticalLayout_12.addWidget(self.frame_cost_kilometer)
        self.frame_distance = QtWidgets.QFrame(self.page_distance_2)
        self.frame_distance.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_distance.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_distance.setObjectName("frame_distance")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_distance)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_moving_distance = QtWidgets.QLabel(self.frame_distance)
        self.label_moving_distance.setTextFormat(QtCore.Qt.AutoText)
        self.label_moving_distance.setObjectName("label_moving_distance")
        self.horizontalLayout_15.addWidget(self.label_moving_distance)
        self.enter_moving_distance = QtWidgets.QLineEdit(self.frame_distance)
        self.enter_moving_distance.setObjectName("enter_moving_distance")
        self.horizontalLayout_15.addWidget(self.enter_moving_distance)
        self.verticalLayout_12.addWidget(self.frame_distance)
        self.frame_button_distance = QtWidgets.QFrame(self.page_distance_2)
        self.frame_button_distance.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_button_distance.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_button_distance.setObjectName("frame_button_distance")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_button_distance)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.button_moving_enter = QtWidgets.QPushButton(self.frame_button_distance)
        self.button_moving_enter.setObjectName("button_moving_enter")
        self.horizontalLayout_13.addWidget(self.button_moving_enter)
        self.button_moving_next = QtWidgets.QPushButton(self.frame_button_distance)
        self.button_moving_next.setObjectName("button_moving_next")
        self.horizontalLayout_13.addWidget(self.button_moving_next)
        self.verticalLayout_12.addWidget(self.frame_button_distance)
        self.qtool_box_2.addItem(self.page_distance_2, "")
        self.page_transportation = QtWidgets.QWidget()
        self.page_transportation.setGeometry(QtCore.QRect(0, 0, 430, 456))
        self.page_transportation.setObjectName("page_transportation")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page_transportation)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_transport = QtWidgets.QFrame(self.page_transportation)
        self.frame_transport.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_transport.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_transport.setObjectName("frame_transport")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_transport)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_distance_transportation = QtWidgets.QFrame(self.frame_transport)
        self.frame_distance_transportation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_distance_transportation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_distance_transportation.setObjectName("frame_distance_transportation")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_distance_transportation)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.L_distance_transportation_km = QtWidgets.QLabel(self.frame_distance_transportation)
        self.L_distance_transportation_km.setObjectName("L_distance_transportation_km")
        self.horizontalLayout_17.addWidget(self.L_distance_transportation_km)
        self.Entry_distance_transportation_km = QtWidgets.QLineEdit(self.frame_distance_transportation)
        self.Entry_distance_transportation_km.setObjectName("Entry_distance_transportation_km")
        self.horizontalLayout_17.addWidget(self.Entry_distance_transportation_km)
        self.verticalLayout_14.addWidget(self.frame_distance_transportation)
        self.frame_cost_transportation_km = QtWidgets.QFrame(self.frame_transport)
        self.frame_cost_transportation_km.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cost_transportation_km.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cost_transportation_km.setObjectName("frame_cost_transportation_km")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_cost_transportation_km)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.L_cost_transportation_km = QtWidgets.QLabel(self.frame_cost_transportation_km)
        self.L_cost_transportation_km.setObjectName("L_cost_transportation_km")
        self.horizontalLayout_18.addWidget(self.L_cost_transportation_km)
        self.Entry_cost_transportation_km = QtWidgets.QLineEdit(self.frame_cost_transportation_km)
        self.Entry_cost_transportation_km.setObjectName("Entry_cost_transportation_km")
        self.horizontalLayout_18.addWidget(self.Entry_cost_transportation_km)
        self.verticalLayout_14.addWidget(self.frame_cost_transportation_km)
        self.frame_number_transport = QtWidgets.QFrame(self.frame_transport)
        self.frame_number_transport.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_number_transport.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_number_transport.setObjectName("frame_number_transport")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_number_transport)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.L_number_transport = QtWidgets.QLabel(self.frame_number_transport)
        self.L_number_transport.setObjectName("L_number_transport")
        self.horizontalLayout_19.addWidget(self.L_number_transport)
        self.Entry_number_transport = QtWidgets.QLineEdit(self.frame_number_transport)
        self.Entry_number_transport.setObjectName("Entry_number_transport")
        self.horizontalLayout_19.addWidget(self.Entry_number_transport)
        self.verticalLayout_14.addWidget(self.frame_number_transport)
        self.frame_button_transport = QtWidgets.QFrame(self.frame_transport)
        self.frame_button_transport.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_button_transport.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_button_transport.setObjectName("frame_button_transport")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_button_transport)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.button_frame_moving_enter = QtWidgets.QPushButton(self.frame_button_transport)
        self.button_frame_moving_enter.setObjectName("button_frame_moving_enter")
        self.horizontalLayout_16.addWidget(self.button_frame_moving_enter)
        self.button_frame_moving_next = QtWidgets.QPushButton(self.frame_button_transport)
        self.button_frame_moving_next.setObjectName("button_frame_moving_next")
        self.horizontalLayout_16.addWidget(self.button_frame_moving_next)
        self.verticalLayout_14.addWidget(self.frame_button_transport)
        self.verticalLayout_13.addWidget(self.frame_transport)
        self.qtool_box_2.addItem(self.page_transportation, "")
        self.verticalLayout_11.addWidget(self.qtool_box_2)
        self.verticalLayout_10.addWidget(self.frame_cost_transportation)
        self.toolBox.addItem(self.page_cost_transportation, "")
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 468, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(2)
        self.toolBox_2.setCurrentIndex(2)
        self.qtool_box_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.L_B.setText(_translate("MainWindow", "B_РП 1-го уровня 1-го типа"))
        self.enter_frame_B.setText(_translate("MainWindow", "Ввести"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_B), _translate("MainWindow", "B"))
        self.L_number_repair_tools.setText(_translate("MainWindow", "количество средств ремонта 1-го типа\n"
"в РП 1-го типа 1-го уровня подчинения"))
        self.L_cost_repair_facilities.setText(_translate("MainWindow", "стоимость средств ремонта 1-го типа\n"
"в РП 1-го типа"))
        self.L_number_repairmen.setText(_translate("MainWindow", "количество ремонтников в РП 1-го типа\n"
" 1-го уровня подчинения"))
        self.L_cost_preparation.setText(_translate("MainWindow", "усреднённая стоимость подготовки\n"
"специалиста-ремонтника\n"
"1-го типа 1--го уровня подчинения "))
        self.button_frame_forming_enter.setText(_translate("MainWindow", "Ввести"))
        self.button_frame_forming_next.setText(_translate("MainWindow", "следующий вид ремонта"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_Forming), _translate("MainWindow", "Стоимость формирования"))
        self.L_submission.setText(_translate("MainWindow", "РП 1-го типа"))
        self.L_number_repair_evacuation.setText(_translate("MainWindow", "Количество ремонтно-эвак\n"
"средств 1-го типа в РО\n"
"1-го уровня"))
        self.L_cost_repair_evacuation.setText(_translate("MainWindow", "Стоимость ремонтно-эвак\n"
"средств 1-го типа"))
        self.Enter_number_repair_evacuation_2.setText(_translate("MainWindow", "следующий уровень/тип"))
        self.button_evacuation_next.setText(_translate("MainWindow", "Следующий тип средств"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_repair_evacuation), _translate("MainWindow", "ремонтно-эвакуационные работы"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_cost_forming), _translate("MainWindow", "стоимость формирования РО"))
        self.L_frame_belt_work_T.setText(_translate("MainWindow", "T_рем 1-го уровня 1-го типа"))
        self.L_frame_belt_work_C_repair.setText(_translate("MainWindow", "Средняя стоимость часа функционирования\n"
"ремонтного подразделения 1-го типа"))
        self.button_frame_belt_work.setText(_translate("MainWindow", "Ввести"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_cost_repair), _translate("MainWindow", "стоимость выполняемых ремонтных работ"))
        self.label_cost_kilometer.setText(_translate("MainWindow", "Стоимость 1 км перещения РПМТ\n"
" 1-й заявке"))
        self.label_moving_distance.setText(_translate("MainWindow", "Расстояние между РО 1-го уровня,\n"
"пройденное РПМТ в ходе выполнения\n"
"ремонта в полевых условиях по\n"
" 1-й заявке"))
        self.button_moving_enter.setText(_translate("MainWindow", "Следующий уровень\n"
"(ввести уровень)"))
        self.button_moving_next.setText(_translate("MainWindow", "следующая заявка\n"
""))
        self.qtool_box_2.setItemText(self.qtool_box_2.indexOf(self.page_distance_2), _translate("MainWindow", "Стоимсоть пермещения РПМТ в ходе выполнения ремонта в полевых условиях"))
        self.L_distance_transportation_km.setText(_translate("MainWindow", "Расстояние между РО 1-го уровня,\n"
"и местонахождением объекта ремонта\n"
"по 1-й заяки"))
        self.L_cost_transportation_km.setText(_translate("MainWindow", "Стоимость одного км транспортировки\n"
"образца средства АТО в РПСТ РО\n"
"1-го уровня по 1-й заявке "))
        self.L_number_transport.setText(_translate("MainWindow", "количество образцов средств АТО,\n"
"направляемых для ремонта в РПСТ\n"
"РО 1-го уровня по 1-й заявке"))
        self.button_frame_moving_enter.setText(_translate("MainWindow", "Следующий уровень\n"
"(ввести уровень)"))
        self.button_frame_moving_next.setText(_translate("MainWindow", "следующая заявка\n"
""))
        self.qtool_box_2.setItemText(self.qtool_box_2.indexOf(self.page_transportation), _translate("MainWindow", "Стоимость транспортировки образцов средств АТО"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_cost_transportation), _translate("MainWindow", "стоимость транспортировки образцов средств АТО и ремонтных органов"))
def resource_path0(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
def resourse_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )

def resourse_path_2(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_frame_input()
    ui.setupUi(MainWindow)
    palette = QPalette()
    path = resource_path0("head.jpg");
    palette.setBrush(QPalette.Background, QBrush(QPixmap(path)))
    MainWindow.setPalette(palette)
    MainWindow.show()
    sys.exit(app.exec_())