from PyQt5.QtWidgets import QApplication,QFileDialog, QMainWindow, QMenuBar, QMenu, QAction
import sys
from PyQt5.QtGui import QIcon,QImage, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        top=400
        left=400
        width=800
        height=600

        #icon="icon.png"

        self.setWindowTitle("Paint Application")
        self.setGeometry(top,left,width,height)
        #self.setWindowIcon(QIcon(icon))

        self.image=QImage(self.size(),QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize=2
        self.brushColor=Qt.black

        self.lastPoint=QPoint()

        mainMenu=self.menuBar()
        fileMenu= mainMenu.addMenu("File")
        brushMenu= mainMenu.addMenu("Brush Size")
        brushColor= mainMenu.addMenu("Brush Color")

        saveAction= QAction("Save",self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        clearAction = QAction("Clear", self)
        clearAction.setShortcut("Ctrl+C")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        threeAction = QAction("3px", self)
        threeAction.setShortcut("Ctrl+3")
        brushMenu.addAction(threeAction)
        threeAction.triggered.connect(self.threepx)

        fiveAction = QAction("5px", self)
        fiveAction.setShortcut("Ctrl+5")
        brushMenu.addAction(fiveAction)
        fiveAction.triggered.connect(self.fivepx)

        sevenAction = QAction("7px", self)
        sevenAction.setShortcut("Ctrl+7")
        brushMenu.addAction(sevenAction)
        sevenAction.triggered.connect(self.sevenpx)

        nineAction = QAction("9px", self)
        nineAction.setShortcut("Ctrl+9")
        brushMenu.addAction(nineAction)
        nineAction.triggered.connect(self.ninepx)




        blackAction=QAction("Black",self)
        blackAction.setShortcut("Ctrl+B")
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.blackcolor)

        greenAction = QAction("Green", self)
        greenAction.setShortcut("Ctrl+G")
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.greencolor)

        redAction = QAction("Red", self)
        redAction.setShortcut("Ctrl+R")
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.redcolor)

        yellowAction = QAction("Yellow", self)
        yellowAction.setShortcut("Ctrl+Y")
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellowcolor)


    def mousePressEvent(self, event):
        if event.button()== Qt.LeftButton:
            self.drawing=True
            self.lastPoint= event.pos()
            print(self.lastPoint)

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) &self.drawing:
            painter=QPainter(self.image)
            painter.setPen(QPen(self.brushColor,self.brushSize,Qt.SolidLine,Qt.RoundCap ))
            painter.drawLine(self.lastPoint,event.pos())
            self.lastPoint=event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button==Qt.LeftButton:
            self.drawing=False

    def paintEvent(self, event):
        canvasPainter=QPainter(self)
        canvasPainter.drawImage(self.rect(),self.image, self.image.rect())


    def save(self):
        filepath,_=QFileDialog.getSaveFileName(self,"Save Iamge","","PNG(*.png);JPEG(*.jpeg);JPG(*.jpg)")
        if filepath=="":
            return
        self.image.save(filepath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()


    def threepx(self):
        self.brushSize=3

    def fivepx(self):
        self.brushSize=5

    def sevenpx(self):
        self.brushSize=7

    def ninepx(self):
        self.brushSize=9

    def blackcolor(self):
        self.brushColor=Qt.black

    def greencolor(self):
        self.brushColor=Qt.green

    def redcolor(self):
        self.brushColor=Qt.red

    def yellowcolor(self):
        self.brushColor=Qt.yellow







if __name__== "__main__":
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    app.exec()

