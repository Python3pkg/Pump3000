# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui_files/Settings.ui'
#
# Created: Fri Dec 19 19:55:27 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(548, 416)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(548, 416))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setToolTip("")
        self.tabWidget.setStatusTip("")
        self.tabWidget.setObjectName("tabWidget")
        self.Plunger_Properties = QtGui.QWidget()
        self.Plunger_Properties.setToolTip("")
        self.Plunger_Properties.setStatusTip("")
        self.Plunger_Properties.setWhatsThis("")
        self.Plunger_Properties.setObjectName("Plunger_Properties")
        self.gridLayout = QtGui.QGridLayout(self.Plunger_Properties)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.refresh_interval = QtGui.QLabel(self.Plunger_Properties)
        self.refresh_interval.setFrameShape(QtGui.QFrame.StyledPanel)
        self.refresh_interval.setObjectName("refresh_interval")
        self.horizontalLayout_11.addWidget(self.refresh_interval)
        spacerItem1 = QtGui.QSpacerItem(24, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.refresh_interval_edit = QtGui.QLineEdit(self.Plunger_Properties)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh_interval_edit.sizePolicy().hasHeightForWidth())
        self.refresh_interval_edit.setSizePolicy(sizePolicy)
        self.refresh_interval_edit.setMinimumSize(QtCore.QSize(123, 0))
        self.refresh_interval_edit.setMaximumSize(QtCore.QSize(123, 16777215))
        self.refresh_interval_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.refresh_interval_edit.setWhatsThis("")
        self.refresh_interval_edit.setText("")
        self.refresh_interval_edit.setFrame(True)
        self.refresh_interval_edit.setPlaceholderText("")
        self.refresh_interval_edit.setObjectName("refresh_interval_edit")
        self.horizontalLayout_11.addWidget(self.refresh_interval_edit)
        self.refresh_interval_button = QtGui.QPushButton(self.Plunger_Properties)
        self.refresh_interval_button.setEnabled(False)
        self.refresh_interval_button.setObjectName("refresh_interval_button")
        self.horizontalLayout_11.addWidget(self.refresh_interval_button)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.noRefresh = QtGui.QCheckBox(self.Plunger_Properties)
        self.noRefresh.setObjectName("noRefresh")
        self.horizontalLayout_12.addWidget(self.noRefresh)
        spacerItem3 = QtGui.QSpacerItem(44, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem3)
        self.refresh_now_button = QtGui.QPushButton(self.Plunger_Properties)
        self.refresh_now_button.setObjectName("refresh_now_button")
        self.horizontalLayout_12.addWidget(self.refresh_now_button)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setObjectName("formLayout_2")
        self.Position = QtGui.QLabel(self.Plunger_Properties)
        self.Position.setFrameShape(QtGui.QFrame.NoFrame)
        self.Position.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Position.setObjectName("Position")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.Position)
        self.Position_Edit = QtGui.QLineEdit(self.Plunger_Properties)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Position_Edit.sizePolicy().hasHeightForWidth())
        self.Position_Edit.setSizePolicy(sizePolicy)
        self.Position_Edit.setFrame(False)
        self.Position_Edit.setReadOnly(True)
        self.Position_Edit.setObjectName("Position_Edit")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.Position_Edit)
        self.Top_Velocity = QtGui.QLabel(self.Plunger_Properties)
        self.Top_Velocity.setObjectName("Top_Velocity")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.Top_Velocity)
        self.Top_Velocity_Edit = QtGui.QLineEdit(self.Plunger_Properties)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Top_Velocity_Edit.sizePolicy().hasHeightForWidth())
        self.Top_Velocity_Edit.setSizePolicy(sizePolicy)
        self.Top_Velocity_Edit.setFrame(False)
        self.Top_Velocity_Edit.setReadOnly(True)
        self.Top_Velocity_Edit.setObjectName("Top_Velocity_Edit")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.Top_Velocity_Edit)
        self.Cutoff_Velocity = QtGui.QLabel(self.Plunger_Properties)
        self.Cutoff_Velocity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Cutoff_Velocity.setObjectName("Cutoff_Velocity")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.Cutoff_Velocity)
        self.Cutoff_Velocity_Edit = QtGui.QLineEdit(self.Plunger_Properties)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cutoff_Velocity_Edit.sizePolicy().hasHeightForWidth())
        self.Cutoff_Velocity_Edit.setSizePolicy(sizePolicy)
        self.Cutoff_Velocity_Edit.setFrame(False)
        self.Cutoff_Velocity_Edit.setReadOnly(True)
        self.Cutoff_Velocity_Edit.setObjectName("Cutoff_Velocity_Edit")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.Cutoff_Velocity_Edit)
        self.Actual_Position = QtGui.QLabel(self.Plunger_Properties)
        self.Actual_Position.setStatusTip("")
        self.Actual_Position.setObjectName("Actual_Position")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.Actual_Position)
        self.Actual_Position_Edit = QtGui.QLineEdit(self.Plunger_Properties)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Actual_Position_Edit.sizePolicy().hasHeightForWidth())
        self.Actual_Position_Edit.setSizePolicy(sizePolicy)
        self.Actual_Position_Edit.setFrame(False)
        self.Actual_Position_Edit.setReadOnly(True)
        self.Actual_Position_Edit.setPlaceholderText("")
        self.Actual_Position_Edit.setObjectName("Actual_Position_Edit")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.Actual_Position_Edit)
        self.Start_Velocity = QtGui.QLabel(self.Plunger_Properties)
        self.Start_Velocity.setObjectName("Start_Velocity")
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.Start_Velocity)
        self.Start_Velocity_Edit = QtGui.QLineEdit(self.Plunger_Properties)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Start_Velocity_Edit.sizePolicy().hasHeightForWidth())
        self.Start_Velocity_Edit.setSizePolicy(sizePolicy)
        self.Start_Velocity_Edit.setFrame(False)
        self.Start_Velocity_Edit.setReadOnly(True)
        self.Start_Velocity_Edit.setObjectName("Start_Velocity_Edit")
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.Start_Velocity_Edit)
        self.Backlash_Steps = QtGui.QLabel(self.Plunger_Properties)
        self.Backlash_Steps.setObjectName("Backlash_Steps")
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.Backlash_Steps)
        self.Backlash_Steps_Edit = QtGui.QLineEdit(self.Plunger_Properties)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Backlash_Steps_Edit.sizePolicy().hasHeightForWidth())
        self.Backlash_Steps_Edit.setSizePolicy(sizePolicy)
        self.Backlash_Steps_Edit.setFrame(False)
        self.Backlash_Steps_Edit.setReadOnly(True)
        self.Backlash_Steps_Edit.setObjectName("Backlash_Steps_Edit")
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.Backlash_Steps_Edit)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Plunger_Properties, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setObjectName("formLayout")
        self.Position_2 = QtGui.QLabel(self.tab_2)
        self.Position_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.Position_2.setObjectName("Position_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.Position_2)
        self.Start_Velocity_2 = QtGui.QLabel(self.tab_2)
        self.Start_Velocity_2.setObjectName("Start_Velocity_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.Start_Velocity_2)
        self.Firmware_Version = QtGui.QLabel(self.tab_2)
        self.Firmware_Version.setObjectName("Firmware_Version")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.Firmware_Version)
        self.Firmware_Checksum = QtGui.QLabel(self.tab_2)
        self.Firmware_Checksum.setObjectName("Firmware_Checksum")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.Firmware_Checksum)
        self.Fluid_Sensor_Edit = QtGui.QLineEdit(self.tab_2)
        self.Fluid_Sensor_Edit.setFrame(False)
        self.Fluid_Sensor_Edit.setReadOnly(True)
        self.Fluid_Sensor_Edit.setObjectName("Fluid_Sensor_Edit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.Fluid_Sensor_Edit)
        self.Buffer_Status_Edit = QtGui.QLineEdit(self.tab_2)
        self.Buffer_Status_Edit.setFrame(False)
        self.Buffer_Status_Edit.setReadOnly(True)
        self.Buffer_Status_Edit.setObjectName("Buffer_Status_Edit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.Buffer_Status_Edit)
        self.Version_Edit = QtGui.QLineEdit(self.tab_2)
        self.Version_Edit.setFrame(False)
        self.Version_Edit.setReadOnly(True)
        self.Version_Edit.setObjectName("Version_Edit")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.Version_Edit)
        self.Checksum_Edit = QtGui.QLineEdit(self.tab_2)
        self.Checksum_Edit.setFrame(False)
        self.Checksum_Edit.setReadOnly(True)
        self.Checksum_Edit.setObjectName("Checksum_Edit")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.Checksum_Edit)
        self.horizontalLayout_6.addLayout(self.formLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh_interval.setText(QtGui.QApplication.translate("Dialog", "Refresh Interval", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh_interval_edit.setToolTip(QtGui.QApplication.translate("Dialog", "Enter the Refresh Interval in Seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh_interval_edit.setStatusTip(QtGui.QApplication.translate("Dialog", "Set the refresh Interval in microseconds", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh_interval_button.setText(QtGui.QApplication.translate("Dialog", "Do it", None, QtGui.QApplication.UnicodeUTF8))
        self.noRefresh.setText(QtGui.QApplication.translate("Dialog", "No Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh_now_button.setText(QtGui.QApplication.translate("Dialog", "Refresh Now", None, QtGui.QApplication.UnicodeUTF8))
        self.Position.setText(QtGui.QApplication.translate("Dialog", "Position [steps]", None, QtGui.QApplication.UnicodeUTF8))
        self.Top_Velocity.setText(QtGui.QApplication.translate("Dialog", "Top Velocity [kHz/s]", None, QtGui.QApplication.UnicodeUTF8))
        self.Cutoff_Velocity.setText(QtGui.QApplication.translate("Dialog", "Cutoff Velocity [kHz/s]", None, QtGui.QApplication.UnicodeUTF8))
        self.Actual_Position.setToolTip(QtGui.QApplication.translate("Dialog", "Reports the actual position of the Plunger", None, QtGui.QApplication.UnicodeUTF8))
        self.Actual_Position.setText(QtGui.QApplication.translate("Dialog", "Actual Position [steps]", None, QtGui.QApplication.UnicodeUTF8))
        self.Start_Velocity.setText(QtGui.QApplication.translate("Dialog", "Start Velocity [kHz/s]", None, QtGui.QApplication.UnicodeUTF8))
        self.Backlash_Steps.setText(QtGui.QApplication.translate("Dialog", "Backlash Steps", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Plunger_Properties), QtGui.QApplication.translate("Dialog", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.Position_2.setText(QtGui.QApplication.translate("Dialog", "Fluid Sensor", None, QtGui.QApplication.UnicodeUTF8))
        self.Start_Velocity_2.setText(QtGui.QApplication.translate("Dialog", "Buffer Status", None, QtGui.QApplication.UnicodeUTF8))
        self.Firmware_Version.setText(QtGui.QApplication.translate("Dialog", "Firmware Version", None, QtGui.QApplication.UnicodeUTF8))
        self.Firmware_Checksum.setText(QtGui.QApplication.translate("Dialog", "Firmware CheckSum", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))

