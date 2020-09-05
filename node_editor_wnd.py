from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from node_graphics_scene import QDMGraphicsScene
from node_graphics_view import QDMGraphicsView


class NodeEditorWnd(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # create graphics scene
        self.grScene = QDMGraphicsScene()

        # create graphics view 
        self.view = QDMGraphicsView(self.grScene, self)
        # self.view.setScene(self.grScene)
        self.layout.addWidget(self.view)

        self.setWindowTitle("Node Editor")
        self.show()

        self.addDebugContent()

    def addDebugContent(self):
        greenBrush = QBrush(Qt.green)
        outlinePen = QPen(Qt.black)
        outlinePen.setWidth(2)

        rect = self.grScene.addRect(-100, -100, 80, 100, outlinePen, greenBrush)
        rect.setFlags(QGraphicsItem.ItemIsMovable|QGraphicsItem.ItemIsSelectable)

        text = self.grScene.addText("This is my Awesome text！", QFont("Ubuntu"))
        text.setFlag(QGraphicsItem.ItemIsSelectable)
        text.setFlag(QGraphicsItem.ItemIsMovable)
        text.setDefaultTextColor(QColor.fromRgbF(1.0, 1.0, 1.0))

        line = self.grScene.addLine(-200, -200, 400, -100, outlinePen)
        line.setFlags(QGraphicsItem.ItemIsMovable|QGraphicsItem.ItemIsSelectable)

        widget1 = QPushButton("Hello World")
        proxy1 = self.grScene.addWidget(widget1)
        proxy1.setFlags(QGraphicsItem.ItemIsMovable|QGraphicsItem.ItemIsSelectable)
        proxy1.setPos(0, 100)

        widget2 = QTextEdit()
        proxy2 = self.grScene.addWidget(widget2)
        proxy2.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemIsMovable)
        proxy2.setPos(100, 200)

