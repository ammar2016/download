#!/usr/bin/python3

# import Important modules
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

from os import path
import sys
import urllib.request
import os 
import threading
import time
import pafy
import humanize
import posixpath
# import urlparse 
# import UI file
FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),'Downlod.ui'))




class mainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(mainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Ui()
        self.Handel_Button()
        self.calc=Thread_run() # To Take Object And Make Operation On It 
        self.calc.count_changed.connect(self.count_change_process) # To Connect The Signal From Thread To The Funciton In The Main Window
        self.calc.duration.connect(self.count_change_process_Single_label) # To Connect The Signal From Thread To The Funciton In The Main Window
        self.calc.finsish.connect(self.download_finshed_Single) # To Connect The Signal From Thread To The Funciton In The Main Window
        self.calc.error.connect(self.Handel_Error_Single) # To Connect The Signal From Thread To The Funciton In The Main Window
        self.get_data = Thread_GetVideo_Data()
        self.get_data.Quality_Combo_Box.connect(self.get_data_combo)
        self.get_data.video_title.connect(self.get_data_title)
        self.video_download = Thread_Download_Video()
        self.video_download.count_change_Prog.connect(self.count_change_process_video_prog)
        self.video_download.count_change_label.connect(self.count_change_process_video_label)
        self.video_download.finsish_video.connect(self.download_finshed_Video)

        self.video_download_playlist = Thread_play_list()
        self.video_download_playlist.count_progress.connect(self.count_Signal_Prog)
        self.video_download_playlist.count_lcd1.connect(self.count_Signal_lcd1)
        self.video_download_playlist.count_lcd2.connect(self.count_Signal_lcd2)
        self.video_download_playlist.count_label.connect(self.count_change_labelplaylist)
        self.video_download_playlist.finshed_playlist.connect(self.Finshed_Signal)



    def Handel_Ui(self):
        # To Center Window In Screen
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.setWindowTitle("Downloader App")
        self.tabWidget.tabBar().setVisible(False)
        self.progressBar.setValue(0)
        self.progressBar_3.setValue(0)
        #To Center Window In Screen
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.setFixedSize(865,448)
        self.comboBox_2.addItem('1080')
        self.comboBox_2.addItem('720')
        self.comboBox_2.addItem('480')
        self.setWindowIcon(QIcon('Download.png'))
        #Animation
        self.Box_1()
        self.Box_2()
        self.Box_3()
        self.Box_4()




        ######Button #########
    def Handel_Button(self):
        self.pushButton.clicked.connect(self.Main_App)
        self.pushButton_2.clicked.connect(self.Signle_Download)
        self.pushButton_3.clicked.connect(self.Youtube_Download)
        self.pushButton_4.clicked.connect(self.Settings_App)
        self.pushButton_5.clicked.connect(self.Handel_Browse)
        self.pushButton_16.clicked.connect(self.onstart)
        ####
        self.pushButton_10.clicked.connect(self.On_Start_Get)
        self.pushButton_9.clicked.connect(self.Handel_Browse_youtube_1)
        self.pushButton_8.clicked.connect(self.On_Start_Video)
        ####
        self.pushButton_13.clicked.connect(self.On_Start_Video_playlist)
        self.pushButton_12.clicked.connect(self.Handel_Browse_youtube_2)
        ###
        self.pushButton_14.clicked.connect(self.Apply_dark)
        self.pushButton_11.clicked.connect(self.Apply_dark_orange)
        self.pushButton_15.clicked.connect(self.Apply_light_blue)




    ############# Handel Button On TabWidget #############
    def Main_App(self):
        self.tabWidget.setCurrentIndex(0)

    def Signle_Download(self):
        self.tabWidget.setCurrentIndex(1)

    def Youtube_Download(self):
        self.tabWidget.setCurrentIndex(2)


    def Settings_App(self):
        self.tabWidget.setCurrentIndex(3)
####################################################################################################################
################################################# Apply StyleSheet #################################################

    def Apply_dark(self):
        style = open('theme/dark_sheet.css','r')
        style=style.read()
        self.setStyleSheet(style)


    def Apply_dark_blue(self):
        pass

    def Apply_dark_orange(self):
        style = open('theme/dark_orange.css','r')
        style=style.read()
        self.setStyleSheet(style)



    def Apply_light_blue(self):
        style = open('theme/light_blue.css','r')
        style=style.read()
        self.setStyleSheet(style)


#App Animation 


    def Box_1(self):
        box_an1 = QPropertyAnimation(self.groupBox_2,b'geometry')
        box_an1.setDuration(1500)
        box_an1.setStartValue(QRect(0,0,0,0))
        box_an1.setEndValue(QRect(30,40,301,141))
        box_an1.start()
        self.box_an1 = box_an1

    def Box_2(self):
        box_an2 = QPropertyAnimation(self.groupBox_5,b'geometry')
        box_an2.setDuration(1500)
        box_an2.setStartValue(QRect(0,0,0,0))
        box_an2.setEndValue(QRect(30,200,301,131))
        box_an2.start()
        self.box_an2 = box_an2

    def Box_3(self):
        box_an3 = QPropertyAnimation(self.groupBox_6,b'geometry')
        box_an3.setDuration(1500)
        box_an3.setStartValue(QRect(0,0,0,0))
        box_an3.setEndValue(QRect(380,40,321,141))
        box_an3.start()
        self.box_an3 = box_an3

    def Box_4(self):
        box_an4 = QPropertyAnimation(self.groupBox_7,b'geometry')
        box_an4.setDuration(1500)
        box_an4.setStartValue(QRect(0,0,0,0))
        box_an4.setEndValue(QRect(380,200,321,131))
        box_an4.start()
        self.box_an4 = box_an4

######################################################################################################################
#################### This Section For Download Video From YouTube ####################################################
    def Handel_Browse_youtube_1(self): # To 
        # save_file = QFileDialog.getSaveFileName(self,caption='Save As',directory = '.',filter='Allfiles (*.*)')
        save_file =QFileDialog.getExistingDirectory(self ,"Save As")

        # text=(save_file[0])
        return self.lineEdit_3.setText(save_file)#To save File With It Name 



    def On_Start_Video(self):
        self.video_download.video_url = self.lineEdit_4.text()
        self.video_download.save_video = self.lineEdit_3.text()
        self.video_download.indexC = self.comboBox.currentIndex()
        if self.video_download.video_url == '' :
            return QMessageBox.information(self, "Empty URL","Please enter the URL of the file you want to download.")
        elif self.video_download.save_video == '':
            return QMessageBox.information(self, "Empty Save File","Please enter the URL of the file you want to download.")
        self.video_download.start() # To Run The QThread


    def count_change_process_video_prog(self,value):
        self.progressBar_4.setValue(value)



    def count_change_process_video_label(self,Ahmed):
        self.label_7.setText(str('{} Remeaning Minuts '.format(Ahmed)))



    def download_finshed_Video(self):
        self.progressBar_4.setValue(0)
        self.lineEdit_4.setText('')
        self.lineEdit_3.setText('')
        self.comboBox.clear()
        self.lineEdit_7.setText('')
        QMessageBox.information(self,'Download Finished','The Download is Finshed') # To Show MessageBox 

    







################################## This Section For Get Data From Threading About Quality And Make It In ComboBox ####
    def On_Start_Get(self): # To Run The Thread And Make Condition For The Line Edit If It Empty 
        self.get_data.url_video1 = self.lineEdit_4.text()
        if self.get_data.url_video1 == '' :
            return QMessageBox.information(self, "Empty URL","Please enter the URL of the file you want to download.")
        self.get_data.start() # To Run The QThread
        
    
    
    
    def get_data_combo(self,combo): # To Recived Signal From Thread And Make It In ComboBox
        self.comboBox.addItem(combo)

    def get_data_title(self,title):
        self.lineEdit_7.setText(title)

########################################### This Section For Singl Download ##################################

    def Handel_Browse(self): # To Save The File With The Orginal 
        save_file =QFileDialog.getExistingDirectory(self ,"Save As")
        # text=(save_file[0])
        a = self.lineEdit.text()
        path = urllib.parse.urlsplit(a).path
        filename = posixpath.basename(path)
        # self.lineEdit_8.setText(filename)

        b = self.lineEdit_8.setText(filename)
        c = self.lineEdit_2.setText(save_file +'/'+ filename)
        return  c

    def onstart(self): # To Run The Thread And Make Condition For The Line Edit If It Empty 
        self.calc.url_d = self.lineEdit.text()
        self.calc.save_d = self.lineEdit_2.text()
        if self.calc.url_d == '' :
            return QMessageBox.information(self, "Empty URL","Please enter the URL of the file you want to download.")
        elif self.calc.save_d == '':
            return QMessageBox.information(self, "Empty Save File","Please enter the URL of the file you want to download.")
        self.calc.start() # To Run The QThread

    def count_change_process_Single_label(self,Saleh):
        self.label_8.setText(Saleh)


    def Handel_Error_Single(self,error):
        QMessageBox.warning(self,"Erro Downloading",error,QMessageBox.Ok)

    def count_change_process(self,saleh): # To Recived Signal From Thread And Make It In ProgressBar
        self.progressBar.setValue(saleh)

    def download_finshed_Single(self): # To Take Signal From Thread If Download 100% Make That
        self.progressBar.setValue(0)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_8.setText('')
        self.label_8.setText('')
        QMessageBox.information(self,'Download Finished','The Download is Finshed') # To Show MessageBox 
######################################################################################################################
######################################### Download Video PlayList ####################################################

    def Handel_Browse_youtube_2(self): # To 
        # save_file = QFileDialog.getSaveFileName(self,caption='Save As',directory = '.',filter='Allfiles (*.*)')
        save_file =QFileDialog.getExistingDirectory(self ,"Save As")

        # text=(save_file[0])
        return self.lineEdit_6.setText(save_file)#To save File With It Name 



    def On_Start_Video_playlist(self):
        self.video_download_playlist.playlist_url = self.lineEdit_5.text()
        self.video_download_playlist.playlist_save = self.lineEdit_6.text()
        self.video_download_playlist.indexC1 = self.comboBox_2.currentIndex()

        if self.video_download_playlist.playlist_url == '' :
            return QMessageBox.information(self, "Empty URL","Please enter the URL of the file you want to download.")
        elif self.video_download_playlist.playlist_save == '':
            return QMessageBox.information(self, "Empty Save File","Please enter the URL of the file you want to download.")
        self.video_download_playlist.start() # To Run The QThread


    def count_Signal_Prog(self,pro):
        self.progressBar_3.setValue(pro)

    def count_Signal_lcd1(self,numb):
        self.lcdNumber_2.display(numb)



    def count_Signal_lcd2(self,numb1):
        self.lcdNumber_3.display(numb1)



    def Finshed_Signal (self):
        QMessageBox.information(self,'Finish','The Download Is Finished ')

    def count_change_labelplaylist(self,numb2):
        self.label_21.setText(str('{} Remeaning Minuts '.format(numb2)))
       





class Thread_play_list(QThread):

    count_progress = pyqtSignal(int)
    count_lcd1 = pyqtSignal(int)
    count_lcd2 = pyqtSignal(int)
    finshed_playlist = pyqtSignal()
    count_label = pyqtSignal(float)
    def run(self):
        playlist = pafy.get_playlist(self.playlist_url)
        playlist_video = playlist['items']
        # print (playlist_video)
        self.count_lcd1.emit(len(playlist_video))


        #save The Videos In Folder With The Same Name 
        os.chdir(self.playlist_save)
        if os.path.exists(str(playlist['title'])):
            os.chdir(str(playlist['title']))
        

        else :
            os.mkdir(playlist['title'])
            os.chdir(str(playlist['title']))


        current_video_in_download = 1
        quality = self.indexC1
        # print (quality)


        for video in playlist_video:
            #current_video = video['pafy']
            current_video_stream = video['pafy'].streams
            self.count_lcd2.emit(current_video_in_download)

            download = current_video_stream[quality].download(callback=self.Playlist_Progress)

            current_video_in_download +=1
            # if current_video_in_download == len(playlist_video):


    def Playlist_Progress(self,total,recived,ratio,rate,time):
        read_data=recived
        if total > 0 :
            download_percentage = read_data*100/total
            self.count_progress.emit(download_percentage)

            remeaning = round(time/60,2)
            self.count_label.emit(remeaning)















############################################# Single Video Downoad From Youtube #######################################
class Thread_Download_Video(QThread):
    count_change_Prog = pyqtSignal(int)
    count_change_label = pyqtSignal(float)
    finsish_video = pyqtSignal()


    def run (self):
        video = pafy.new(self.video_url)
        video_stream = video.allstreams
        # video_quaity = indexC
        download = video_stream[self.indexC].download(filepath=self.save_video,callback=self.Video_Single_ProgressBar)


    def Video_Single_ProgressBar(self,total,recived,ratio,rate,time):
        read_data=recived
        if total > 0 :
            download_percentage = read_data*100/total
            self.count_change_Prog.emit(download_percentage)
            remeaning = round(time/60,2)
            self.count_change_label.emit(remeaning)
            if download_percentage >= 100:
                self.finsish_video.emit()

class Thread_GetVideo_Data(QThread):

    Quality_Combo_Box = pyqtSignal(str)

    video_title = pyqtSignal(str)


    def run (self):
        video = pafy.new(self.url_video1)
        video_streams = video.allstreams
        # Title = video.title
        self.video_title.emit(video.title)

        for stream in video_streams :
            size =humanize.naturalsize(stream.get_filesize())
            data = '{} - {} - {} - {}'.format(stream.mediatype,stream.extension,stream.quality,size)
            self.Quality_Combo_Box.emit(data)


########## This Threading For ProgressBar SinglDownload File ###########################################################
class Thread_run(QThread):
    #### Signal ####
    count_changed = pyqtSignal(int) # This Signal For ProgressBar 
    # save = pyqtSignal(str) #  This Signal For Get Url From Line EditFrom  Main Window To Thread_run (UrlLib Need It)
    # url = pyqtSignal(str) # This Signal For Get Url From LineEdit From Main Window To Thread_run (Urllib Need It)
    finsish = pyqtSignal() # This Signal To Take Signal From Percent To Show QMessageBox To Show The Download Finshed 
    duration = pyqtSignal(str)
    error = pyqtSignal(str)
    def run (self):
        try:
            d=urllib.request.urlretrieve(self.url_d,self.save_d,self.Handel_ProgressBar)
        except Exception as a :
            self.error.emit(str(a))

    def Handel_ProgressBar(self,block_num,blocksize,totalsize):
        global start_time
        if totalsize>0:
            start_time = time.time()
            duration = time.time() - start_time
            downloaded = block_num*blocksize
            speed = downloaded/(1024*duration)
            percent=(downloaded*100)/totalsize
            self.count_changed.emit(percent)
            a=(" %d%%, %d  MB ,  %s KB/S  , %d  seconds    passed" %(percent, downloaded / (1024 * 1024) , humanize.naturalsize(speed/1024), duration))
            self.duration.emit(str(a))
            if percent >= 100 :
                self.finsish.emit()

####################################### The End Of The Section Of Single Download ##################################





def main():
    app = QApplication(sys.argv)
    window = mainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()