# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\EHC_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import EHC_Checker, EHC_core

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QPushButton, QDialog, QApplication

import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(778, 537)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 11)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.state = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.state.sizePolicy().hasHeightForWidth())
        self.state.setSizePolicy(sizePolicy)
        self.state.setObjectName("state")
        self.verticalLayout_2.addWidget(self.state)
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.get = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get.sizePolicy().hasHeightForWidth())
        self.get.setSizePolicy(sizePolicy)
        self.get.setObjectName("get")
        self.verticalLayout_2.addWidget(self.get)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.check = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check.sizePolicy().hasHeightForWidth())
        self.check.setSizePolicy(sizePolicy)
        self.check.setObjectName("check")
        self.horizontalLayout.addWidget(self.check)
        self.backup = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backup.sizePolicy().hasHeightForWidth())
        self.backup.setSizePolicy(sizePolicy)
        self.backup.setObjectName("backup")
        self.horizontalLayout.addWidget(self.backup)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.Label = QtWidgets.QLabel(self.tab_2)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.email_user = QtWidgets.QLineEdit(self.tab_2)
        self.email_user.setObjectName("email_user")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.email_user)
        self.Label_2 = QtWidgets.QLabel(self.tab_2)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.password = QtWidgets.QLineEdit(self.tab_2)
        self.password.setObjectName("password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password)
        self.pOPLabel = QtWidgets.QLabel(self.tab_2)
        self.pOPLabel.setObjectName("pOPLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pOPLabel)
        self.pop3_server = QtWidgets.QLineEdit(self.tab_2)
        self.pop3_server.setObjectName("pop3_server")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pop3_server)
        self.Label_3 = QtWidgets.QLabel(self.tab_2)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.requireSubject = QtWidgets.QLineEdit(self.tab_2)
        self.requireSubject.setObjectName("requireSubject")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.requireSubject)
        self.Label_4 = QtWidgets.QLabel(self.tab_2)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.path = QtWidgets.QLineEdit(self.tab_2)
        self.path.setObjectName("path")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.path)
        self.checkBox = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.checkBox)
        self.save = QtWidgets.QPushButton(self.tab_2)
        self.save.setObjectName("save")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.save)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 778, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "emailHomeworkCollector_Beta0.3"))
        self.label.setText(_translate("MainWindow", "学委解放计划之邮箱收作业系统_Beta0.3.a"))
        self.state.setText(_translate("MainWindow", "初始化完成"))
        self.get.setText(_translate("MainWindow", "邮箱收取"))
        self.check.setText(_translate("MainWindow", "遍历统计"))
        self.backup.setText(_translate("MainWindow", "封包备份"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "首页"))
        self.Label.setText(_translate("MainWindow", "邮箱地址"))
        self.Label_2.setText(_translate("MainWindow", "POP授权码"))
        self.pOPLabel.setText(_translate("MainWindow", "POP服务器地址"))
        self.Label_3.setText(_translate("MainWindow", "指定邮件主题"))
        self.Label_4.setText(_translate("MainWindow", "邮件存放路径"))
        self.checkBox.setText(_translate("MainWindow", "收取成功后删除邮件（彻底删除！）"))
        self.save.setText(_translate("MainWindow", "保存"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "设置"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">解放学委计划之</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:14pt; font-weight:600;\">emailHomeworkCollector Beta0.3.a</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:14pt; font-weight:600;\">邮箱收作业系统测试版0.3.a</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">课余乱造，谨慎试用；</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">售价10元，支持下辈子付款。</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "噬月的乱造"))
        self.label_3.setText(_translate("MainWindow", "976534093@qq.com"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "关于"))

