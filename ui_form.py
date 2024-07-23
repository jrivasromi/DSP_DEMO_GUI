from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDial, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLCDNumber,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QTabWidget, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1514, 798)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(188, 215, 219);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 1px solid black;\n"
"    background: brown;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: silver;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top"
                        "-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.trans = QWidget()
        self.trans.setObjectName(u"trans")
        self.verticalLayout = QVBoxLayout(self.trans)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.trans)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setLayoutDirection(Qt.LeftToRight)
        self.frame_3.setStyleSheet(u"background-color: rgb(43, 33, 48);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(9, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_3)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_17)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.BaseBand_Freq = QVBoxLayout()
        self.BaseBand_Freq.setObjectName(u"BaseBand_Freq")

        self.verticalLayout_18.addLayout(self.BaseBand_Freq)


        self.gridLayout_4.addWidget(self.frame_17, 0, 1, 1, 1)

        self.frame_16 = QFrame(self.frame_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_16)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.Quantized_Freq = QVBoxLayout()
        self.Quantized_Freq.setObjectName(u"Quantized_Freq")

        self.verticalLayout_17.addLayout(self.Quantized_Freq)


        self.gridLayout_4.addWidget(self.frame_16, 1, 1, 1, 1)

        self.frame_15 = QFrame(self.frame_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_15)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.Signal_Tiempo = QVBoxLayout()
        self.Signal_Tiempo.setObjectName(u"Signal_Tiempo")

        self.verticalLayout_16.addLayout(self.Signal_Tiempo)


        self.gridLayout_4.addWidget(self.frame_15, 0, 0, 2, 1)

        self.gridLayout_4.setColumnStretch(0, 3)
        self.gridLayout_4.setColumnStretch(1, 2)

        self.verticalLayout.addWidget(self.frame_3)

        self.tabWidget_3 = QTabWidget(self.trans)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setFocusPolicy(Qt.ClickFocus)
        self.tabWidget_3.setAutoFillBackground(False)
        self.tabWidget_3.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 1px solid black;\n"
"    background: brown;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: silver;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top"
                        "-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}")
        self.tabWidget_3.setDocumentMode(False)
        self.tabWidget_3.setTabsClosable(False)
        self.tabWidget_3.setTabBarAutoHide(False)
        self.PCM = QWidget()
        self.PCM.setObjectName(u"PCM")
        self.horizontalLayout_4 = QHBoxLayout(self.PCM)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.PCM)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color: rgb(43, 33, 48);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_11)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_21)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.Mod_Tiempo = QVBoxLayout()
        self.Mod_Tiempo.setObjectName(u"Mod_Tiempo")

        self.verticalLayout_20.addLayout(self.Mod_Tiempo)


        self.horizontalLayout_7.addWidget(self.frame_21)

        self.frame_20 = QFrame(self.frame_11)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_20)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.Mod_Freq = QVBoxLayout()
        self.Mod_Freq.setObjectName(u"Mod_Freq")

        self.verticalLayout_19.addLayout(self.Mod_Freq)


        self.horizontalLayout_7.addWidget(self.frame_20)


        self.horizontalLayout_4.addWidget(self.frame_11)

        self.tabWidget_3.addTab(self.PCM, "")
        self.Canal = QWidget()
        self.Canal.setObjectName(u"Canal")
        self.horizontalLayout_5 = QHBoxLayout(self.Canal)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.Canal)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(43, 33, 48);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_13)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_19)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.AWGN_Tiempo = QVBoxLayout()
        self.AWGN_Tiempo.setObjectName(u"AWGN_Tiempo")

        self.verticalLayout_23.addLayout(self.AWGN_Tiempo)


        self.horizontalLayout_8.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_18)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.AWGN_Freq = QVBoxLayout()
        self.AWGN_Freq.setObjectName(u"AWGN_Freq")

        self.verticalLayout_24.addLayout(self.AWGN_Freq)


        self.horizontalLayout_8.addWidget(self.frame_18)


        self.horizontalLayout_5.addWidget(self.frame_13)

        self.tabWidget_3.addTab(self.Canal, "")

        self.verticalLayout.addWidget(self.tabWidget_3)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.tabWidget.addTab(self.trans, "")
        self.recep = QWidget()
        self.recep.setObjectName(u"recep")
        self.horizontalLayout_6 = QHBoxLayout(self.recep)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.recep)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color: rgb(43, 33, 48);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_12)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_10 = QFrame(self.frame_12)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_10)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.Signal_ZOH = QVBoxLayout()
        self.Signal_ZOH.setObjectName(u"Signal_ZOH")

        self.verticalLayout_31.addLayout(self.Signal_ZOH)


        self.gridLayout_5.addWidget(self.frame_10, 1, 0, 1, 1)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_14)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.Signal_Dec = QVBoxLayout()
        self.Signal_Dec.setObjectName(u"Signal_Dec")

        self.verticalLayout_30.addLayout(self.Signal_Dec)


        self.gridLayout_5.addWidget(self.frame_14, 0, 1, 1, 1)

        self.frame_8 = QFrame(self.frame_12)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_8)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.H_Filtro = QVBoxLayout()
        self.H_Filtro.setObjectName(u"H_Filtro")

        self.verticalLayout_29.addLayout(self.H_Filtro)


        self.gridLayout_5.addWidget(self.frame_8, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.frame_12)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_9)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.Spec_ZOH = QVBoxLayout()
        self.Spec_ZOH.setObjectName(u"Spec_ZOH")

        self.verticalLayout_32.addLayout(self.Spec_ZOH)


        self.gridLayout_5.addWidget(self.frame_9, 1, 1, 1, 1)


        self.horizontalLayout_6.addWidget(self.frame_12)

        self.tabWidget.addTab(self.recep, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)

        self.horizontalLayout_3.setStretch(0, 4)

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(123, 185, 180);")
        self.label.setTextFormat(Qt.PlainText)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.amplitude = QDoubleSpinBox(self.frame_5)
        self.amplitude.setObjectName(u"amplitude")
        self.amplitude.setSingleStep(0.500000000000000)
        self.amplitude.setValue(2.000000000000000)

        self.gridLayout_2.addWidget(self.amplitude, 0, 1, 1, 1)

        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.label_18, 12, 0, 1, 1)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.label_7, 7, 0, 1, 1)

        self.sampling_factor = QDoubleSpinBox(self.frame_5)
        self.sampling_factor.setObjectName(u"sampling_factor")
        self.sampling_factor.setMinimum(0.100000000000000)
        self.sampling_factor.setSingleStep(0.500000000000000)
        self.sampling_factor.setValue(6.000000000000000)

        self.gridLayout_2.addWidget(self.sampling_factor, 7, 1, 1, 1)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.freq_separation_factor = QDoubleSpinBox(self.frame_5)
        self.freq_separation_factor.setObjectName(u"freq_separation_factor")
        self.freq_separation_factor.setEnabled(True)
        self.freq_separation_factor.setMinimum(0.000000000000000)
        self.freq_separation_factor.setMaximum(5.000000000000000)
        self.freq_separation_factor.setSingleStep(0.500000000000000)

        self.gridLayout_2.addWidget(self.freq_separation_factor, 9, 2, 1, 1)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.label_8, 2, 2, 1, 1)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.label_9, 4, 2, 1, 1)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.line_2 = QFrame(self.frame_5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 10, 0, 1, 3)

        self.wave_type_dropdown = QComboBox(self.frame_5)
        self.wave_type_dropdown.addItem("")
        self.wave_type_dropdown.addItem("")
        self.wave_type_dropdown.addItem("")
        self.wave_type_dropdown.addItem("")
        self.wave_type_dropdown.addItem("")
        self.wave_type_dropdown.addItem("")
        self.wave_type_dropdown.setObjectName(u"wave_type_dropdown")
        self.wave_type_dropdown.setEnabled(True)
        self.wave_type_dropdown.setEditable(True)

        self.gridLayout_2.addWidget(self.wave_type_dropdown, 9, 1, 1, 1)

        self.compression_type = QComboBox(self.frame_5)
        self.compression_type.addItem("")
        self.compression_type.addItem("")
        self.compression_type.addItem("")
        self.compression_type.setObjectName(u"compression_type")

        self.gridLayout_2.addWidget(self.compression_type, 11, 1, 1, 1)

        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.label_17, 11, 0, 1, 1)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.label_12, 9, 0, 1, 1)

        self.compression_factor = QComboBox(self.frame_5)
        self.compression_factor.addItem("")
        self.compression_factor.addItem("")
        self.compression_factor.addItem("")
        self.compression_factor.addItem("")
        self.compression_factor.addItem("")
        self.compression_factor.addItem("")
        self.compression_factor.addItem("")
        self.compression_factor.setObjectName(u"compression_factor")

        self.gridLayout_2.addWidget(self.compression_factor, 12, 1, 1, 1)

        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setEnabled(True)
        self.label_14.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_14, 7, 2, 1, 1)

        self.duration = QSpinBox(self.frame_5)
        self.duration.setObjectName(u"duration")
        self.duration.setMinimum(0)
        self.duration.setSingleStep(10)

        self.gridLayout_2.addWidget(self.duration, 4, 1, 1, 1)

        self.frequency = QSpinBox(self.frame_5)
        self.frequency.setObjectName(u"frequency")
        self.frequency.setMinimum(1)
        self.frequency.setValue(60)

        self.gridLayout_2.addWidget(self.frequency, 2, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.label_15 = QLabel(self.frame_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(Qt.LeftToRight)
        self.label_15.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(123, 185, 180);")
        self.label_15.setTextFormat(Qt.PlainText)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_15)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.line = QFrame(self.frame_6)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.line, 4, 0, 1, 2)

        self.quantization_knob = QDial(self.frame_6)
        self.quantization_knob.setObjectName(u"quantization_knob")
        self.quantization_knob.setStyleSheet(u"background-color: rgb(222, 229, 95);\n"
"background-color: rgb(128, 213, 222);")
        self.quantization_knob.setMinimum(1)
        self.quantization_knob.setMaximum(8)
        self.quantization_knob.setSingleStep(21)
        self.quantization_knob.setPageStep(10)
        self.quantization_knob.setValue(1)
        self.quantization_knob.setNotchesVisible(True)

        self.gridLayout_6.addWidget(self.quantization_knob, 2, 1, 1, 1)

        self.quantization_display = QLCDNumber(self.frame_6)
        self.quantization_display.setObjectName(u"quantization_display")
        self.quantization_display.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.quantization_display.setSegmentStyle(QLCDNumber.Filled)

        self.gridLayout_6.addWidget(self.quantization_display, 1, 1, 1, 1)

        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_11, 3, 1, 1, 1)

        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_6.addWidget(self.label_13, 5, 0, 1, 1)

        self.snr_display = QLCDNumber(self.frame_6)
        self.snr_display.setObjectName(u"snr_display")
        self.snr_display.setAutoFillBackground(False)
        self.snr_display.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.snr_display.setSegmentStyle(QLCDNumber.Filled)

        self.gridLayout_6.addWidget(self.snr_display, 1, 0, 1, 1)

        self.channel_cod_dropdown = QComboBox(self.frame_6)
        self.channel_cod_dropdown.addItem("")
        self.channel_cod_dropdown.addItem("")
        self.channel_cod_dropdown.addItem("")
        self.channel_cod_dropdown.setObjectName(u"channel_cod_dropdown")
        self.channel_cod_dropdown.setEditable(False)

        self.gridLayout_6.addWidget(self.channel_cod_dropdown, 5, 1, 1, 1)

        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_10, 3, 0, 1, 1)

        self.snr_knob = QDial(self.frame_6)
        self.snr_knob.setObjectName(u"snr_knob")
        self.snr_knob.setStyleSheet(u"background-color: rgb(222, 229, 95);\n"
"background-color: rgb(128, 213, 222);")
        self.snr_knob.setMinimum(1)
        self.snr_knob.setMaximum(10)
        self.snr_knob.setSingleStep(10)
        self.snr_knob.setPageStep(10)
        self.snr_knob.setValue(1)
        self.snr_knob.setSliderPosition(1)
        self.snr_knob.setNotchesVisible(True)

        self.gridLayout_6.addWidget(self.snr_knob, 2, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setLayoutDirection(Qt.LeftToRight)
        self.label_16.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(123, 185, 180);\n"
"")
        self.label_16.setTextFormat(Qt.PlainText)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_16)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_22 = QFrame(self.frame_7)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.update = QPushButton(self.frame_22)
        self.update.setObjectName(u"update")
        self.update.setGeometry(QRect(0, 0, 271, 141))
        self.update.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 127);")

        self.verticalLayout_4.addWidget(self.frame_22)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 17)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 10)

        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_23 = QFrame(self.frame)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"background-color: rgb(43, 33, 48);")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_23)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.PCM_OUT = QTextBrowser(self.frame_23)
        self.PCM_OUT.setObjectName(u"PCM_OUT")
        self.PCM_OUT.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(43, 33, 48);\n"
"font: 7pt \"Cascadia Code\";\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.PCM_OUT)

        self.PCM_RX = QTextBrowser(self.frame_23)
        self.PCM_RX.setObjectName(u"PCM_RX")
        self.PCM_RX.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(43, 33, 48);\n"
"font: 9pt \"Cascadia Code\";\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.PCM_RX)

        self.Compression_Graph = QHBoxLayout()
        self.Compression_Graph.setObjectName(u"Compression_Graph")

        self.verticalLayout_3.addLayout(self.Compression_Graph)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout.addWidget(self.frame_23)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.PCM), QCoreApplication.translate("Widget", u"PCM", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.Canal), QCoreApplication.translate("Widget", u"Canal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.trans), QCoreApplication.translate("Widget", u"Transmisi\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recep), QCoreApplication.translate("Widget", u"Recepci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("Widget", u"DATOS DE LA SE\u00d1AL", None))
        self.label_18.setText(QCoreApplication.translate("Widget", u"Factor", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Factor de Muestreo", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Zoom Horizontal", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Frecuencia", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"Hz", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"ms", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Amplitud", None))
        self.wave_type_dropdown.setItemText(0, QCoreApplication.translate("Widget", u"Seno", None))
        self.wave_type_dropdown.setItemText(1, QCoreApplication.translate("Widget", u"Triangular", None))
        self.wave_type_dropdown.setItemText(2, QCoreApplication.translate("Widget", u"Cuadrada", None))
        self.wave_type_dropdown.setItemText(3, QCoreApplication.translate("Widget", u"Diente de Sierra", None))
        self.wave_type_dropdown.setItemText(4, QCoreApplication.translate("Widget", u"2 Senoidales", None))
        self.wave_type_dropdown.setItemText(5, QCoreApplication.translate("Widget", u"3 Senoidales", None))

        self.compression_type.setItemText(0, QCoreApplication.translate("Widget", u"Ninguna", None))
        self.compression_type.setItemText(1, QCoreApplication.translate("Widget", u"\u03bc", None))
        self.compression_type.setItemText(2, QCoreApplication.translate("Widget", u"A", None))

        self.label_17.setText(QCoreApplication.translate("Widget", u"Compansi\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Vp", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"Funci\u00f3n", None))
        self.compression_factor.setItemText(0, QCoreApplication.translate("Widget", u"0", None))
        self.compression_factor.setItemText(1, QCoreApplication.translate("Widget", u"1", None))
        self.compression_factor.setItemText(2, QCoreApplication.translate("Widget", u"10", None))
        self.compression_factor.setItemText(3, QCoreApplication.translate("Widget", u"100", None))
        self.compression_factor.setItemText(4, QCoreApplication.translate("Widget", u"200", None))
        self.compression_factor.setItemText(5, QCoreApplication.translate("Widget", u"400", None))
        self.compression_factor.setItemText(6, QCoreApplication.translate("Widget", u"1000", None))

        self.label_14.setText(QCoreApplication.translate("Widget", u"Factor", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"PAR\u00c1METROS PCM", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"Niveles de cuantizaci\u00f3n", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"Codificaci\u00f3n Del Canal", None))
        self.channel_cod_dropdown.setItemText(0, QCoreApplication.translate("Widget", u"NRZ-M", None))
        self.channel_cod_dropdown.setItemText(1, QCoreApplication.translate("Widget", u"RZ-M", None))
        self.channel_cod_dropdown.setItemText(2, QCoreApplication.translate("Widget", u"RZ-AMI", None))

        self.label_10.setText(QCoreApplication.translate("Widget", u"SNR (dB)", None))
        self.label_16.setText(QCoreApplication.translate("Widget", u"CONFIRMAR", None))
        self.update.setText(QCoreApplication.translate("Widget", u"Actualizar", None))
    # retranslateUi

