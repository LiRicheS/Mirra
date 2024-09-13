# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import res_py.res_rc as res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(519, 634)
        MainWindow.setMinimumSize(QSize(418, 582))
        MainWindow.setMaximumSize(QSize(1000, 1000))
        font = QFont()
        font.setFamilies([u"REM"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setStyleStrategy(QFont.PreferAntialias)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/icons/radio_button_checked_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background: qlineargradient(spread:reflect, x1:0.380682, y1:0.443, x2:1, y2:1, stop:0.153409 rgba(47, 69, 142, 255), stop:1 rgba(191, 87, 175, 255));\n"
"font-family: REM;")
        self.main_widget = QWidget(MainWindow)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setStyleSheet(u"")
        self.mic_on = QPushButton(self.main_widget)
        self.mic_on.setObjectName(u"mic_on")
        self.mic_on.setGeometry(QRect(110, 570, 41, 41))
        self.mic_on.setCursor(QCursor(Qt.PointingHandCursor))
        self.mic_on.setMouseTracking(True)
        self.mic_on.setToolTipDuration(-1)
        self.mic_on.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255,255,255,30);\n"
"	border:1px solid rgba(255,255,255,40);\n"
"	border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(255,255,255,85);\n"
"	opacity:0.2;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/mic_FILL0_wght100_GRAD-25_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mic_on.setIcon(icon1)
        self.mic_on.setIconSize(QSize(45, 45))
        self.mic_on.setAutoDefault(False)
        self.info = QPushButton(self.main_widget)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(10, 20, 31, 31))
        self.info.setCursor(QCursor(Qt.PointingHandCursor))
        self.info.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255,255,255,30);\n"
"	border:1px solid rgba(255,255,255,40);\n"
"	border-radius:14px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(255,255,255,85);\n"
"	opacity:0.2;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/help_FILL0_wght100_GRAD-25_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.info.setIcon(icon2)
        self.info.setIconSize(QSize(30, 30))
        self.mic_off = QPushButton(self.main_widget)
        self.mic_off.setObjectName(u"mic_off")
        self.mic_off.setGeometry(QRect(370, 570, 41, 41))
        self.mic_off.setCursor(QCursor(Qt.PointingHandCursor))
        self.mic_off.setMouseTracking(True)
        self.mic_off.setToolTipDuration(-1)
        self.mic_off.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255,255,255,30);\n"
"	border:1px solid rgba(255,255,255,40);\n"
"	border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(255,255,255,85);\n"
"	opacity:0.2;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/mic_off_FILL0_wght100_GRAD-25_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mic_off.setIcon(icon3)
        self.mic_off.setIconSize(QSize(45, 45))
        self.mic_off.setAutoDefault(False)
        self.listWidget = QListWidget(self.main_widget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(50, 10, 421, 551))
        font1 = QFont()
        font1.setFamilies([u"REM"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.listWidget.setFont(font1)
        self.listWidget.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.listWidget.setStyleSheet(u"QListWidget{\n"
"	background-color: rgba(255,255,255,30);\n"
"	border:2px solid rgba(255,255,255,50);\n"
"	border-radius: 15px;\n"
"}")
        self.clear_poleList = QPushButton(self.main_widget)
        self.clear_poleList.setObjectName(u"clear_poleList")
        self.clear_poleList.setGeometry(QRect(10, 50, 31, 31))
        self.clear_poleList.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_poleList.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255,255,255,30);\n"
"	border:1px solid rgba(255,255,255,40);\n"
"	border-radius:14px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(255,255,255,85);\n"
"	opacity:0.2;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/delete_FILL0_wght100_GRAD-25_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_poleList.setIcon(icon4)
        self.clear_poleList.setIconSize(QSize(33, 30))
        MainWindow.setCentralWidget(self.main_widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u" \u041c\u0438\u0440\u0430 v0.4", None))
#if QT_CONFIG(tooltip)
        self.mic_on.setToolTip(QCoreApplication.translate("MainWindow", u"\u0441\u0442\u0430\u0440\u0442", None))
#endif // QT_CONFIG(tooltip)
        self.mic_on.setText("")
#if QT_CONFIG(tooltip)
        self.info.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0438\u043d\u0441\u0442\u0440\u043a\u0443\u043a\u0446\u0438\u044f \u043a \u0431\u043e\u0442\u0443</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.info.setText("")
#if QT_CONFIG(tooltip)
        self.mic_off.setToolTip(QCoreApplication.translate("MainWindow", u"\u0441\u0442\u043e\u043f", None))
#endif // QT_CONFIG(tooltip)
        self.mic_off.setText("")
#if QT_CONFIG(tooltip)
        self.clear_poleList.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u043e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043f\u043e\u043b\u0435 \u0432\u044b\u0432\u043e\u0434\u0430</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.clear_poleList.setText("")
    # retranslateUi

