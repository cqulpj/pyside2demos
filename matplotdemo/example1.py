from PySide2.QtWidgets import QApplication, QLabel

import matplotlib
matplotlib.use('QT5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

if __name__ == '__main__':
    app = QApplication()

    label = QLabel("Hello World")
    label.show()

    canvas = FigureCanvas(Figure(figsize=(5, 3)))
    ax = canvas.figure.subplots()
    ax.plot([1, 2, 3, 4])

    canvas.show()

    app.exec_()
