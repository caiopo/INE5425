# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(879, 784)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_10 = QtWidgets.QFrame(self.groupBox)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_15.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_7 = QtWidgets.QLabel(self.frame_10)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_16.addWidget(self.label_7)
        self.tec1_cb = QtWidgets.QComboBox(self.frame_10)
        self.tec1_cb.setObjectName("tec1_cb")
        self.tec1_cb.addItem("")
        self.tec1_cb.addItem("")
        self.tec1_cb.addItem("")
        self.tec1_cb.addItem("")
        self.tec1_cb.addItem("")
        self.verticalLayout_16.addWidget(self.tec1_cb)
        self.tec1_text = QtWidgets.QLineEdit(self.frame_10)
        self.tec1_text.setObjectName("tec1_text")
        self.verticalLayout_16.addWidget(self.tec1_text)
        self.verticalLayout_15.addLayout(self.verticalLayout_16)
        self.verticalLayout.addWidget(self.frame_10)
        self.frame_8 = QtWidgets.QFrame(self.groupBox)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.frame_8)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_13.addWidget(self.label_6)
        self.tec2_cb = QtWidgets.QComboBox(self.frame_8)
        self.tec2_cb.setObjectName("tec2_cb")
        self.tec2_cb.addItem("")
        self.tec2_cb.addItem("")
        self.tec2_cb.addItem("")
        self.tec2_cb.addItem("")
        self.tec2_cb.addItem("")
        self.verticalLayout_13.addWidget(self.tec2_cb)
        self.tec2_text = QtWidgets.QLineEdit(self.frame_8)
        self.tec2_text.setObjectName("tec2_text")
        self.verticalLayout_13.addWidget(self.tec2_text)
        self.verticalLayout_12.addLayout(self.verticalLayout_13)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_5 = QtWidgets.QFrame(self.groupBox)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.ts1_cb = QtWidgets.QComboBox(self.frame_5)
        self.ts1_cb.setObjectName("ts1_cb")
        self.ts1_cb.addItem("")
        self.ts1_cb.addItem("")
        self.ts1_cb.addItem("")
        self.ts1_cb.addItem("")
        self.ts1_cb.addItem("")
        self.verticalLayout_7.addWidget(self.ts1_cb)
        self.ts1_text = QtWidgets.QLineEdit(self.frame_5)
        self.ts1_text.setObjectName("ts1_text")
        self.verticalLayout_7.addWidget(self.ts1_text)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_3 = QtWidgets.QFrame(self.groupBox)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.ts2_cb = QtWidgets.QComboBox(self.frame_3)
        self.ts2_cb.setObjectName("ts2_cb")
        self.ts2_cb.addItem("")
        self.ts2_cb.addItem("")
        self.ts2_cb.addItem("")
        self.ts2_cb.addItem("")
        self.ts2_cb.addItem("")
        self.verticalLayout_5.addWidget(self.ts2_cb)
        self.ts2_text = QtWidgets.QLineEdit(self.frame_3)
        self.ts2_text.setObjectName("ts2_text")
        self.verticalLayout_5.addWidget(self.ts2_text)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.tef_cb = QtWidgets.QComboBox(self.frame)
        self.tef_cb.setObjectName("tef_cb")
        self.tef_cb.addItem("")
        self.tef_cb.addItem("")
        self.tef_cb.addItem("")
        self.tef_cb.addItem("")
        self.tef_cb.addItem("")
        self.verticalLayout_2.addWidget(self.tef_cb)
        self.tef_text = QtWidgets.QLineEdit(self.frame)
        self.tef_text.setObjectName("tef_text")
        self.verticalLayout_2.addWidget(self.tef_text)
        self.verticalLayout_9.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.groupBox)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.tf_cb = QtWidgets.QComboBox(self.frame_2)
        self.tf_cb.setObjectName("tf_cb")
        self.tf_cb.addItem("")
        self.tf_cb.addItem("")
        self.tf_cb.addItem("")
        self.tf_cb.addItem("")
        self.tf_cb.addItem("")
        self.verticalLayout_8.addWidget(self.tf_cb)
        self.tf_text = QtWidgets.QLineEdit(self.frame_2)
        self.tf_text.setObjectName("tf_text")
        self.verticalLayout_8.addWidget(self.tf_text)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.mean_entity_in_queue_1 = QtWidgets.QLabel(self.groupBox_2)
        self.mean_entity_in_queue_1.setObjectName("mean_entity_in_queue_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.mean_entity_in_queue_1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        self.label_24.setObjectName("label_24")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.mean_entity_in_queue_2 = QtWidgets.QLabel(self.groupBox_2)
        self.mean_entity_in_queue_2.setObjectName("mean_entity_in_queue_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mean_entity_in_queue_2)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.occupation_rate_1 = QtWidgets.QLabel(self.groupBox_2)
        self.occupation_rate_1.setObjectName("occupation_rate_1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.occupation_rate_1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.occupation_rate_2 = QtWidgets.QLabel(self.groupBox_2)
        self.occupation_rate_2.setObjectName("occupation_rate_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.occupation_rate_2)
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setObjectName("label_22")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.mean_time_in_queue = QtWidgets.QLabel(self.groupBox_2)
        self.mean_time_in_queue.setObjectName("mean_time_in_queue")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.mean_time_in_queue)
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.mean_time_in_system = QtWidgets.QLabel(self.groupBox_2)
        self.mean_time_in_system.setObjectName("mean_time_in_system")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.mean_time_in_system)
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.entities_entered = QtWidgets.QLabel(self.groupBox_2)
        self.entities_entered.setObjectName("entities_entered")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.entities_entered)
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.fail_rate_1 = QtWidgets.QLabel(self.groupBox_2)
        self.fail_rate_1.setObjectName("fail_rate_1")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.fail_rate_1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.fail_rate_2 = QtWidgets.QLabel(self.groupBox_2)
        self.fail_rate_2.setObjectName("fail_rate_2")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.fail_rate_2)
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setObjectName("label_28")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.fix_count_1 = QtWidgets.QLabel(self.groupBox_2)
        self.fix_count_1.setObjectName("fix_count_1")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.fix_count_1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.fix_count_2 = QtWidgets.QLabel(self.groupBox_2)
        self.fix_count_2.setObjectName("fix_count_2")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.fix_count_2)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.entities_left = QtWidgets.QLabel(self.groupBox_2)
        self.entities_left.setObjectName("entities_left")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.entities_left)
        self.entities_inside = QtWidgets.QLabel(self.groupBox_2)
        self.entities_inside.setObjectName("entities_inside")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.entities_inside)
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.entities_blocked = QtWidgets.QLabel(self.groupBox_2)
        self.entities_blocked.setObjectName("entities_blocked")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.entities_blocked)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_14.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_19 = QtWidgets.QLabel(self.groupBox_3)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_14.addWidget(self.label_19)
        self.entity_limit = QtWidgets.QLineEdit(self.groupBox_3)
        self.entity_limit.setObjectName("entity_limit")
        self.verticalLayout_14.addWidget(self.entity_limit)
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_14.addWidget(self.label_21)
        self.total_time = QtWidgets.QLineEdit(self.groupBox_3)
        self.total_time.setObjectName("total_time")
        self.verticalLayout_14.addWidget(self.total_time)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.error = QtWidgets.QLabel(self.groupBox_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.error.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.error.setFont(font)
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setObjectName("error")
        self.verticalLayout_3.addWidget(self.error)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_4.addWidget(self.label_17)
        self.time = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.time.setFont(font)
        self.time.setObjectName("time")
        self.horizontalLayout_4.addWidget(self.time)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.progress_bar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progress_bar.setProperty("value", 5)
        self.progress_bar.setObjectName("progress_bar")
        self.verticalLayout_3.addWidget(self.progress_bar)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.nsteps = QtWidgets.QSlider(self.groupBox_5)
        self.nsteps.setMinimum(1)
        self.nsteps.setMaximum(99)
        self.nsteps.setSingleStep(1)
        self.nsteps.setOrientation(QtCore.Qt.Horizontal)
        self.nsteps.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.nsteps.setTickInterval(5)
        self.nsteps.setObjectName("nsteps")
        self.horizontalLayout.addWidget(self.nsteps)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start = QtWidgets.QPushButton(self.groupBox_2)
        self.start.setObjectName("start")
        self.horizontalLayout_2.addWidget(self.start)
        self.stop = QtWidgets.QPushButton(self.groupBox_2)
        self.stop.setObjectName("stop")
        self.horizontalLayout_2.addWidget(self.stop)
        self.complete = QtWidgets.QPushButton(self.groupBox_2)
        self.complete.setObjectName("complete")
        self.horizontalLayout_2.addWidget(self.complete)
        self.step = QtWidgets.QPushButton(self.groupBox_2)
        self.step.setObjectName("step")
        self.horizontalLayout_2.addWidget(self.step)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setEnabled(False)
        self.mainToolBar.setMovable(False)
        self.mainToolBar.setFloatable(False)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setEnabled(False)
        self.statusBar.setSizeGripEnabled(False)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulador"))
        self.groupBox.setTitle(_translate("MainWindow", "Parâmetros"))
        self.label_7.setText(_translate("MainWindow", "Tempo entre chegadas 1"))
        self.tec1_cb.setItemText(0, _translate("MainWindow", "Constante"))
        self.tec1_cb.setItemText(1, _translate("MainWindow", "Exponencial"))
        self.tec1_cb.setItemText(2, _translate("MainWindow", "Normal"))
        self.tec1_cb.setItemText(3, _translate("MainWindow", "Triangular"))
        self.tec1_cb.setItemText(4, _translate("MainWindow", "Uniforme"))
        self.label_6.setText(_translate("MainWindow", "Tempo entre chegadas 2"))
        self.tec2_cb.setItemText(0, _translate("MainWindow", "Constante"))
        self.tec2_cb.setItemText(1, _translate("MainWindow", "Exponencial"))
        self.tec2_cb.setItemText(2, _translate("MainWindow", "Normal"))
        self.tec2_cb.setItemText(3, _translate("MainWindow", "Triangular"))
        self.tec2_cb.setItemText(4, _translate("MainWindow", "Uniforme"))
        self.label_4.setText(_translate("MainWindow", "Tempo de serviço 1"))
        self.ts1_cb.setItemText(0, _translate("MainWindow", "Constante"))
        self.ts1_cb.setItemText(1, _translate("MainWindow", "Exponencial"))
        self.ts1_cb.setItemText(2, _translate("MainWindow", "Normal"))
        self.ts1_cb.setItemText(3, _translate("MainWindow", "Triangular"))
        self.ts1_cb.setItemText(4, _translate("MainWindow", "Uniforme"))
        self.label_3.setText(_translate("MainWindow", "Tempo de serviço 2"))
        self.ts2_cb.setItemText(0, _translate("MainWindow", "Constante"))
        self.ts2_cb.setItemText(1, _translate("MainWindow", "Exponencial"))
        self.ts2_cb.setItemText(2, _translate("MainWindow", "Normal"))
        self.ts2_cb.setItemText(3, _translate("MainWindow", "Triangular"))
        self.ts2_cb.setItemText(4, _translate("MainWindow", "Uniforme"))
        self.label_2.setText(_translate("MainWindow", "Tempo entre falhas"))
        self.tef_cb.setItemText(0, _translate("MainWindow", "Constante"))
        self.tef_cb.setItemText(1, _translate("MainWindow", "Exponencial"))
        self.tef_cb.setItemText(2, _translate("MainWindow", "Normal"))
        self.tef_cb.setItemText(3, _translate("MainWindow", "Triangular"))
        self.tef_cb.setItemText(4, _translate("MainWindow", "Uniforme"))
        self.label_8.setText(_translate("MainWindow", "Tempo de falha"))
        self.tf_cb.setItemText(0, _translate("MainWindow", "Constante"))
        self.tf_cb.setItemText(1, _translate("MainWindow", "Exponencial"))
        self.tf_cb.setItemText(2, _translate("MainWindow", "Normal"))
        self.tf_cb.setItemText(3, _translate("MainWindow", "Triangular"))
        self.tf_cb.setItemText(4, _translate("MainWindow", "Uniforme"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Estatísticas"))
        self.label.setText(_translate("MainWindow", "Número médio de entidades na fila 1:"))
        self.mean_entity_in_queue_1.setText(_translate("MainWindow", "--"))
        self.label_24.setText(_translate("MainWindow", "Número médio de entidades na fila 2:"))
        self.mean_entity_in_queue_2.setText(_translate("MainWindow", "--"))
        self.label_10.setText(_translate("MainWindow", "Taxa de ocupação do servidor 1:"))
        self.occupation_rate_1.setText(_translate("MainWindow", "--"))
        self.label_12.setText(_translate("MainWindow", "Taxa de ocupação do servidor 2:"))
        self.occupation_rate_2.setText(_translate("MainWindow", "--"))
        self.label_22.setText(_translate("MainWindow", "Tempo médio de uma entidade na fila:"))
        self.mean_time_in_queue.setText(_translate("MainWindow", "--"))
        self.label_20.setText(_translate("MainWindow", "Tempo médio de uma entidade no sistema:"))
        self.mean_time_in_system.setText(_translate("MainWindow", "--"))
        self.label_18.setText(_translate("MainWindow", "Total de entidades que entraram no sistema:"))
        self.entities_entered.setText(_translate("MainWindow", "--"))
        self.label_16.setText(_translate("MainWindow", "Taxa de falha do servidor 1:"))
        self.fail_rate_1.setText(_translate("MainWindow", "--"))
        self.label_14.setText(_translate("MainWindow", "Taxa de falha do servidor 2:"))
        self.fail_rate_2.setText(_translate("MainWindow", "--"))
        self.label_28.setText(_translate("MainWindow", "Contagem de consertos do servidor 1:"))
        self.fix_count_1.setText(_translate("MainWindow", "--"))
        self.label_11.setText(_translate("MainWindow", "Contagem de consertos do servidor 2:"))
        self.fix_count_2.setText(_translate("MainWindow", "--"))
        self.label_9.setText(_translate("MainWindow", "Total de entidades que sairam do sistema:"))
        self.label_13.setText(_translate("MainWindow", "Total de entidades dentro do sistema:"))
        self.entities_left.setText(_translate("MainWindow", "--"))
        self.entities_inside.setText(_translate("MainWindow", "--"))
        self.label_15.setText(_translate("MainWindow", "Total de entidades bloqueadas:"))
        self.entities_blocked.setText(_translate("MainWindow", "--"))
        self.label_19.setText(_translate("MainWindow", "Total de entidades"))
        self.label_21.setText(_translate("MainWindow", "Tempo total de simulação"))
        self.error.setText(_translate("MainWindow", "Erro!"))
        self.label_17.setText(_translate("MainWindow", "Tempo atual:"))
        self.time.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "Unidades de tempo por passo:"))
        self.start.setText(_translate("MainWindow", "Iniciar Simulação"))
        self.stop.setText(_translate("MainWindow", "Cancelar Simulação"))
        self.complete.setText(_translate("MainWindow", "Executar até o final"))
        self.step.setText(_translate("MainWindow", "Avançar 01 unidades de tempo"))

