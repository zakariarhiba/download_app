
# import library 
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox
from PyQt5 import uic,QtGui
import sys

import urllib.request


# initialize the MainWindow of our app
class AppDemo(QMainWindow):
    def __init__(self):
        # call init of QMainWindow
        super().__init__()
        # load our design from Qtdesigner 
        uic.loadUi('MainWindow.ui', self) 
        # set up our app functionality 
        self.Set_ui()
        self.buttons()

    def Set_ui(self):
        self.setWindowTitle('first_app')
        self.setFixedSize(543,265)
        self.setWindowIcon(QtGui.QIcon('icon.png'))

    def buttons(self):
            self.pushButton_download.clicked.connect(self.download)
            self.pushButton_browse.clicked.connect(self.browsefiles)
  

    def progressbar(self,pices,pice_size,total_size):
        current_download = pice_size * pices
        if total_size > 0:
            percent = current_download * 100 / total_size
            percent = int(percent)
            self.progressBar.setValue(percent)
            QApplication.processEvents()

    def browsefiles(self):
        save_location = QFileDialog.getSaveFileName(self,caption="Save As", directory="C:\\",filter="All Files (*.*)")
        save_name = save_location[0]
        self.lineEdit_savelocation.setText(save_name)


    def download(self):
        url = self.lineEdit_url.text()
        save_location = self.lineEdit_savelocation.text()
        if self.lineEdit_savelocation.text() == '' or self.lineEdit_url.text()=='':
            QMessageBox.warning(self,"Download failed","Empty url or Save location")
        else:
            try:
                urllib.request.urlretrieve(url,save_location,self.progressbar)
            except Exception:
                QMessageBox.warning(self,"Download Error","Download failed")
                return
            else:
                QMessageBox.information(self,"Download Finished","Download is successfully finishied")
            finally:
                self.lineEdit_url.setText("")
                self.lineEdit_savelocation.setText("")
                self.progressBar.setValue(0)
        
        

        
# if code run from main
if __name__ == '__main__':
    # create app in sys
    app = QApplication(sys.argv)
    # load our MainWindow 
    demo = AppDemo()
    # show the window 
    demo.show()




    # except end process
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Clossing window...')

   

