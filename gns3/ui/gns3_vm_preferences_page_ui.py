# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/noplay/code/gns3/gns3-gui/gns3/ui/gns3_vm_preferences_page.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GNS3VMPreferencesPageWidget(object):
    def setupUi(self, GNS3VMPreferencesPageWidget):
        GNS3VMPreferencesPageWidget.setObjectName("GNS3VMPreferencesPageWidget")
        GNS3VMPreferencesPageWidget.resize(590, 299)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GNS3VMPreferencesPageWidget.sizePolicy().hasHeightForWidth())
        GNS3VMPreferencesPageWidget.setSizePolicy(sizePolicy)
        GNS3VMPreferencesPageWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(GNS3VMPreferencesPageWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiEnableVMCheckBox = QtWidgets.QCheckBox(GNS3VMPreferencesPageWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiEnableVMCheckBox.sizePolicy().hasHeightForWidth())
        self.uiEnableVMCheckBox.setSizePolicy(sizePolicy)
        self.uiEnableVMCheckBox.setMinimumSize(QtCore.QSize(0, 0))
        self.uiEnableVMCheckBox.setChecked(False)
        self.uiEnableVMCheckBox.setObjectName("uiEnableVMCheckBox")
        self.verticalLayout.addWidget(self.uiEnableVMCheckBox)
        self.uiVirtualizationGroupBox = QtWidgets.QGroupBox(GNS3VMPreferencesPageWidget)
        self.uiVirtualizationGroupBox.setObjectName("uiVirtualizationGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uiVirtualizationGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiGNS3VMEngineComboBox = QtWidgets.QComboBox(self.uiVirtualizationGroupBox)
        self.uiGNS3VMEngineComboBox.setObjectName("uiGNS3VMEngineComboBox")
        self.verticalLayout_2.addWidget(self.uiGNS3VMEngineComboBox)
        self.uiEngineDescriptionLabel = QtWidgets.QLabel(self.uiVirtualizationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiEngineDescriptionLabel.sizePolicy().hasHeightForWidth())
        self.uiEngineDescriptionLabel.setSizePolicy(sizePolicy)
        self.uiEngineDescriptionLabel.setWordWrap(True)
        self.uiEngineDescriptionLabel.setObjectName("uiEngineDescriptionLabel")
        self.verticalLayout_2.addWidget(self.uiEngineDescriptionLabel)
        self.verticalLayout.addWidget(self.uiVirtualizationGroupBox)
        self.uiGNS3VMSettingsGroupBox = QtWidgets.QGroupBox(GNS3VMPreferencesPageWidget)
        self.uiGNS3VMSettingsGroupBox.setObjectName("uiGNS3VMSettingsGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiGNS3VMSettingsGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiVMNameLabel = QtWidgets.QLabel(self.uiGNS3VMSettingsGroupBox)
        self.uiVMNameLabel.setObjectName("uiVMNameLabel")
        self.gridLayout_2.addWidget(self.uiVMNameLabel, 0, 0, 1, 1)
        self.uiVMListComboBox = QtWidgets.QComboBox(self.uiGNS3VMSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVMListComboBox.sizePolicy().hasHeightForWidth())
        self.uiVMListComboBox.setSizePolicy(sizePolicy)
        self.uiVMListComboBox.setObjectName("uiVMListComboBox")
        self.gridLayout_2.addWidget(self.uiVMListComboBox, 0, 1, 1, 1)
        self.uiRefreshPushButton = QtWidgets.QPushButton(self.uiGNS3VMSettingsGroupBox)
        self.uiRefreshPushButton.setObjectName("uiRefreshPushButton")
        self.gridLayout_2.addWidget(self.uiRefreshPushButton, 0, 2, 1, 1)
        self.uiHeadlessCheckBox = QtWidgets.QCheckBox(self.uiGNS3VMSettingsGroupBox)
        self.uiHeadlessCheckBox.setObjectName("uiHeadlessCheckBox")
        self.gridLayout_2.addWidget(self.uiHeadlessCheckBox, 1, 0, 1, 2)
        self.uiShutdownCheckBox = QtWidgets.QCheckBox(self.uiGNS3VMSettingsGroupBox)
        self.uiShutdownCheckBox.setObjectName("uiShutdownCheckBox")
        self.gridLayout_2.addWidget(self.uiShutdownCheckBox, 2, 0, 1, 2)
        self.verticalLayout.addWidget(self.uiGNS3VMSettingsGroupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(GNS3VMPreferencesPageWidget)
        QtCore.QMetaObject.connectSlotsByName(GNS3VMPreferencesPageWidget)

    def retranslateUi(self, GNS3VMPreferencesPageWidget):
        _translate = QtCore.QCoreApplication.translate
        GNS3VMPreferencesPageWidget.setWindowTitle(_translate("GNS3VMPreferencesPageWidget", "GNS3 VM"))
        self.uiEnableVMCheckBox.setText(_translate("GNS3VMPreferencesPageWidget", "Enable the GNS3 VM"))
        self.uiVirtualizationGroupBox.setTitle(_translate("GNS3VMPreferencesPageWidget", "Virtualization software"))
        self.uiEngineDescriptionLabel.setText(_translate("GNS3VMPreferencesPageWidget", "Description"))
        self.uiGNS3VMSettingsGroupBox.setTitle(_translate("GNS3VMPreferencesPageWidget", "Settings"))
        self.uiVMNameLabel.setText(_translate("GNS3VMPreferencesPageWidget", "VM name:"))
        self.uiRefreshPushButton.setText(_translate("GNS3VMPreferencesPageWidget", "&Refresh"))
        self.uiHeadlessCheckBox.setText(_translate("GNS3VMPreferencesPageWidget", "Start VM in headless mode"))
        self.uiShutdownCheckBox.setText(_translate("GNS3VMPreferencesPageWidget", "ACPI shutdown VM when closing GNS3"))

