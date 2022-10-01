from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

import sys

from GetRandomWord import RandomWord

class LoadMainUi(QMainWindow):
        
    def __init__(self):
        super(LoadMainUi,self).__init__()
        loadUi("MainFormUi.ui",self)
        self.TempWord=""

        self.scene = QGraphicsScene()
        self.graphicsView_Hangman.setScene(self.scene)
        self.Hangman()

        for buton in self.groupBox_Letters.children():
            buton.setCheckable(True)
            buton.setEnabled(True)
            buton.clicked.connect(lambda :self.pushButton_LetterClicked(buton.text()))

        self.pushButton_Restart.clicked.connect(self.pushButton_Restart_Clicked)

        self.font=self.label_Word.font()
        self.font.setLetterSpacing(QFont.AbsoluteSpacing, 3)
        self.label_Word.setFont(self.font)

        self.groupBox_Letters.show()
        self.groupBox_Letters.setEnabled(True)

        self.label_Defination.hide()

        self.pushButton_Restart.hide()
        self.pushButton_Restart.setEnabled(False)
        
        self.GetWord()
    def GetWord(self):
        randomword.Open()
        while True:
            randomword.GetRandomWord()
            randomword.GetDefination()
            if randomword.word!="" and randomword.defination!="":
                randomword.Close()
                break
        for letter in randomword.word:
            self.TempWord=self.TempWord+"_"
        self.label_Word.setText(self.TempWord)
        self.label_Defination.setText(randomword.defination)
    def pushButton_LetterClicked(self,buton):
        for buton in self.groupBox_Letters.children():
            if buton.isChecked() and buton.isEnabled:
                buton.setEnabled(False)
                buton.setCheckable(False)
                break
        IsletterFound=False
        temp=""
        for i in range(len(randomword.word)):
            if buton.text() ==randomword.word[i].upper():
                IsletterFound=True
                temp=temp+buton.text()
            elif self.TempWord[i]!="_":
                temp=temp+self.TempWord[i]
            else:
                temp=temp+"_"
        self.TempWord=temp
        self.label_Word.setText(self.TempWord)
        if not IsletterFound:
            randomword.GuessCount-=1
            self.Hangman()
        if "_" not in self.TempWord:
            QMessageBox.about(self, "Info", "Win")
            self.EndGame()
        if randomword.GuessCount==0:
            QMessageBox.about(self, "Info", "Game Over")
            self.EndGame()
    def pushButton_Restart_Clicked(self):
        self.TempWord=""
        randomword.GuessCount=6
        self.Hangman()
        for buton in self.groupBox_Letters.children():
            buton.setCheckable(True)
            buton.setEnabled(True)
        self.groupBox_Letters.show()
        self.groupBox_Letters.setEnabled(True)

        self.label_Defination.hide()
        self.pushButton_Restart.hide()
        self.pushButton_Restart.setEnabled(False)
        self.GetWord()
    def EndGame(self):
        self.groupBox_Letters.hide()
        self.groupBox_Letters.setEnabled(False)

        self.label_Defination.setText("The mean of "+randomword.word.capitalize()+" is:"+"\n"+randomword.defination.capitalize())
        self.label_Word.setText(randomword.word.upper())

        self.label_Defination.show()
        self.pushButton_Restart.show()
        self.pushButton_Restart.setEnabled(True)
    def Hangman(self):
        if randomword.GuessCount==6:
        # scene
            self.scene.clear()
            rect_item = QGraphicsRectItem(QRectF(0, 0, 10, 250))            
            rect_item.setBrush(Qt.black)
            self.scene.addItem(rect_item)
            
            rect_item = QGraphicsRectItem(QRectF(0, 0, 80, 10))            
            rect_item.setBrush(Qt.black)
            self.scene.addItem(rect_item)

            rect_item = QGraphicsRectItem(QRectF(-20, 250, 120, 10))            
            rect_item.setBrush(Qt.black)
            self.scene.addItem(rect_item)

            # rope
            rect_item = QGraphicsRectItem(QRectF(80, 0, 0, 40))
            rect_item.setBrush(Qt.black)
            self.scene.addItem(rect_item)
        elif randomword.GuessCount==5:
        # head
            self.scene.addEllipse(60, 40, 40, 40, brush=QColor("black"), pen=QPen(Qt.NoPen))
        elif randomword.GuessCount==4:
        # body
            rect_item = QGraphicsRectItem(QRectF(75, 75, 10, 85))
            rect_item.setBrush(Qt.black)
            self.scene.addItem(rect_item)
        elif randomword.GuessCount==3:
        # right arm
            rect_item = QGraphicsRectItem(QRectF(19, 120, 10, 50))
            rect_item.setBrush(Qt.black)
            rect_item.setRotation(-30)
            self.scene.addItem(rect_item)
        elif randomword.GuessCount==2:
        # left arm
            rect_item = QGraphicsRectItem(QRectF(110, 40, 10, 50))
            rect_item.setBrush(Qt.black)
            rect_item.setRotation(30)
            self.scene.addItem(rect_item)
        elif randomword.GuessCount==1:
        # right leg
            rect_item = QGraphicsRectItem(QRectF(-13, 170, 10, 60))
            rect_item.setBrush(Qt.black)
            rect_item.setRotation(-30)
            self.scene.addItem(rect_item)
        elif randomword.GuessCount==0:
        # left leg
            rect_item = QGraphicsRectItem(QRectF(140, 90, 10, 60))
            rect_item.setBrush(Qt.black)
            rect_item.setRotation(30)
            self.scene.addItem(rect_item)

randomword=RandomWord()

app = QApplication(sys.argv)
window = LoadMainUi()
window.setWindowTitle("Hangman")
window.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting..")