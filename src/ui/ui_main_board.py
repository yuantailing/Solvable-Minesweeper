# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_board.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 205)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 192, 192))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 192, 192))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 192, 192))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 192, 192))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setEnabled(True)
        self.frame_1.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setLineWidth(6)
        self.frame_1.setMidLineWidth(0)
        self.frame_1.setObjectName("frame_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_1)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MinenumTimeWigdet = QtWidgets.QFrame(self.frame_1)
        self.MinenumTimeWigdet.setMinimumSize(QtCore.QSize(0, 0))
        self.MinenumTimeWigdet.setStyleSheet("")
        self.MinenumTimeWigdet.setFrameShape(QtWidgets.QFrame.Panel)
        self.MinenumTimeWigdet.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.MinenumTimeWigdet.setLineWidth(4)
        self.MinenumTimeWigdet.setMidLineWidth(0)
        self.MinenumTimeWigdet.setObjectName("MinenumTimeWigdet")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MinenumTimeWigdet)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = mineNumLabel(self.MinenumTimeWigdet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_11.setAutoFillBackground(False)
        self.label_11.setLineWidth(0)
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("media/test.png"))
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.label_12 = mineNumLabel(self.MinenumTimeWigdet)
        self.label_12.setMinimumSize(QtCore.QSize(0, 0))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_12.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_12.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_12.setAcceptDrops(False)
        self.label_12.setLineWidth(0)
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("media/test.png"))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.label_13 = mineNumLabel(self.MinenumTimeWigdet)
        self.label_13.setLineWidth(0)
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("media/test.png"))
        self.label_13.setIndent(-1)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = StatusLabel(self.MinenumTimeWigdet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_2.setLineWidth(0)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_31 = QtWidgets.QLabel(self.MinenumTimeWigdet)
        self.label_31.setLineWidth(0)
        self.label_31.setText("")
        self.label_31.setPixmap(QtGui.QPixmap("media/test.png"))
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_4.addWidget(self.label_31, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_32 = QtWidgets.QLabel(self.MinenumTimeWigdet)
        self.label_32.setLineWidth(0)
        self.label_32.setText("")
        self.label_32.setPixmap(QtGui.QPixmap("media/test.png"))
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_4.addWidget(self.label_32, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_33 = QtWidgets.QLabel(self.MinenumTimeWigdet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setMinimumSize(QtCore.QSize(0, 0))
        self.label_33.setLineWidth(0)
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap("media/test.png"))
        self.label_33.setScaledContents(False)
        self.label_33.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_4.addWidget(self.label_33, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.MinenumTimeWigdet)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label = mineLabel(self.frame_1)
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(4)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.frame_1)
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_info.setFont(font)
        self.label_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_info.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.verticalLayout_2.addWidget(self.label_info)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 946, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionnew_game = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.actionnew_game.setFont(font)
        self.actionnew_game.setObjectName("actionnew_game")
        self.actionchu_ji = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.actionchu_ji.setFont(font)
        self.actionchu_ji.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionchu_ji.setObjectName("actionchu_ji")
        self.actionzhogn_ji = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.actionzhogn_ji.setFont(font)
        self.actionzhogn_ji.setObjectName("actionzhogn_ji")
        self.actiongao_ji = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.actiongao_ji.setFont(font)
        self.actiongao_ji.setObjectName("actiongao_ji")
        self.actionzi_ding_yi = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.actionzi_ding_yi.setFont(font)
        self.actionzi_ding_yi.setObjectName("actionzi_ding_yi")
        self.actiontui_chu = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.actiontui_chu.setFont(font)
        self.actiontui_chu.setObjectName("actiontui_chu")
        self.actionyouxi_she_zhi = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.actionyouxi_she_zhi.setFont(font)
        self.actionyouxi_she_zhi.setObjectName("actionyouxi_she_zhi")
        self.actiongaun_yv = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.actiongaun_yv.setFont(font)
        self.actiongaun_yv.setObjectName("actiongaun_yv")
        self.actionxis = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.actionxis.setFont(font)
        self.actionxis.setObjectName("actionxis")
        self.actionrumjc = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.actionrumjc.setFont(font)
        self.actionrumjc.setObjectName("actionrumjc")
        self.action_kuaijiejian = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.action_kuaijiejian.setFont(font)
        self.action_kuaijiejian.setObjectName("action_kuaijiejian")
        self.actionopen = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.actionopen.setFont(font)
        self.actionopen.setObjectName("actionopen")
        self.menu.addAction(self.actionopen)
        self.menu.addSeparator()
        self.menu.addAction(self.actionnew_game)
        self.menu.addSeparator()
        self.menu.addAction(self.actionchu_ji)
        self.menu.addAction(self.actionzhogn_ji)
        self.menu.addAction(self.actiongao_ji)
        self.menu.addAction(self.actionzi_ding_yi)
        self.menu.addSeparator()
        self.menu.addAction(self.actiontui_chu)
        self.menu_2.addAction(self.actionyouxi_she_zhi)
        self.menu_2.addAction(self.action_kuaijiejian)
        self.menu_3.addAction(self.actionxis)
        self.menu_3.addAction(self.actionrumjc)
        self.menu_3.addAction(self.actiongaun_yv)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_info.setText(_translate("MainWindow", "预留、备用"))
        self.menu.setTitle(_translate("MainWindow", "游戏"))
        self.menu_2.setTitle(_translate("MainWindow", "设置"))
        self.menu_3.setTitle(_translate("MainWindow", "帮助"))
        self.actionnew_game.setText(_translate("MainWindow", "新游戏"))
        self.actionnew_game.setShortcut(_translate("MainWindow", "N"))
        self.actionchu_ji.setText(_translate("MainWindow", "初级"))
        self.actionchu_ji.setShortcut(_translate("MainWindow", "B"))
        self.actionzhogn_ji.setText(_translate("MainWindow", "中级"))
        self.actionzhogn_ji.setShortcut(_translate("MainWindow", "I"))
        self.actiongao_ji.setText(_translate("MainWindow", "高级"))
        self.actiongao_ji.setShortcut(_translate("MainWindow", "E"))
        self.actionzi_ding_yi.setText(_translate("MainWindow", "自定义"))
        self.actionzi_ding_yi.setShortcut(_translate("MainWindow", "C"))
        self.actiontui_chu.setText(_translate("MainWindow", "退出"))
        self.actiontui_chu.setShortcut(_translate("MainWindow", "X"))
        self.actionyouxi_she_zhi.setText(_translate("MainWindow", "游戏设置"))
        self.actionyouxi_she_zhi.setShortcut(_translate("MainWindow", "S"))
        self.actiongaun_yv.setText(_translate("MainWindow", "关于"))
        self.actiongaun_yv.setShortcut(_translate("MainWindow", "A"))
        self.actionxis.setText(_translate("MainWindow", "词典"))
        self.actionxis.setShortcut(_translate("MainWindow", "D"))
        self.actionrumjc.setText(_translate("MainWindow", "入门教程"))
        self.actionrumjc.setShortcut(_translate("MainWindow", "R"))
        self.action_kuaijiejian.setText(_translate("MainWindow", "其它设置"))
        self.action_kuaijiejian.setShortcut(_translate("MainWindow", "Z"))
        self.actionopen.setText(_translate("MainWindow", "打开"))
        self.actionopen.setShortcut(_translate("MainWindow", "O"))
from ui.mineLabel import mineLabel
from ui.mineNumLabel import mineNumLabel
from ui.uiComponents import StatusLabel
