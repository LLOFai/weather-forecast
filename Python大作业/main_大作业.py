import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import json
import urllib.parse

import API   #使用的第一个文件
import info  #使用的第二个文件

dict1 = {'CITY': ' '}  #使用一个dict将第一个类中输入的结果传到第二个类

class GUI(QWidget):  #第一个窗口

    def __init__(self):
        
        super(GUI, self).__init__()
         
        self.initUI()
         

    def initUI(self):
         
        self.resize(600, 400)       #设置窗口参数
        self.setWindowTitle('天气预报')
        self.setWindowIcon(QIcon('tubiao.jpg'))
        
        self.center()               #将窗口居中
        
        self.title = QLabel('输入你想查询天气的城市名称:')   #设置界面
        self.title.setFont(QFont("Roman times",13))
        self.titleEdit = QLineEdit("")
        Save_Btn = QPushButton('确定')
        Save_Btn.setFont(QFont("Roman times",11))
        self.left = QLabel(self)
        self.right = QLabel(self)
        self.blank = QLabel(' ')

        self.grid = QGridLayout()              #设置界面布局
        self.grid.addWidget(self.blank, 1,0)
        self.grid.addWidget(self.title,1,2)
        self.title.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(self.titleEdit, 2,1,2,3)
        self.grid.addWidget(self.blank, 2,4,2,5)
        self.titleEdit.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(Save_Btn,3,2)
        self.grid.addWidget(self.blank, 4,0)
        
        self.grid.addWidget(self.left,2,0)
        pixmap = QPixmap("左.jpg")    # 按指定路径找到图片
        self.left.setPixmap (pixmap)  # 在label上显示图片

        self.grid.addWidget(self.right,2,5)
        pixmap = QPixmap("右.jpg")     # 按指定路径找到图片
        self.right.setPixmap (pixmap)  # 在label上显示图片  


        self.setLayout(self.grid)
        
        Save_Btn.clicked.connect(self.CityName)
        
        Save_Btn.clicked.connect(self.slot_btn_function) #连接第二个窗口
        
        

    def center(self):       #将窗口居中的函数
         
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    
         
    def CityName(self):

        dict1['CITY'] = self.titleEdit.text()  #将文本框输入的内容储存到dict中传到第二个类



    def slot_btn_function(self):     #连接第二个窗口的函数
        
        self.hide()
        self.s = SecondUi()
        self.s.show()





class SecondUi(QTabWidget):    #第二个窗口
    
    def __init__(self):
        
        super(SecondUi, self).__init__()

        self.resize(1000, 800)        #设置窗口参数并将其居中
        self.setWindowTitle('天气预报')
        self.setWindowIcon(QIcon('tubiao.jpg'))
        self.center()
        
        self.tab1 = QWidget()         #设置按键文字及子界面字体大小
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.addTab(self.tab1,"实时天气")
        self.addTab(self.tab2,"今日预报")
        self.addTab(self.tab3,"未来预报")
        self.tab1.setFont(QFont("Roman times",12))
        self.tab2.setFont(QFont("Roman times",12))
        self.tab3.setFont(QFont("Roman times",11))
        
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

        
    def center(self):            #将窗口居中的函数
         
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def tab1UI(self):

        forecast = self.Message()  #调用API
       
        layout = QGridLayout()
        
        self.name = QLabel(dict1['CITY'])   #设置字体及底色
        layout.addWidget(self.name,1,0,1,3)
        self.name.setAlignment(Qt.AlignCenter)
        self.name.setFont(QFont("Roman times",15))
        self.name.setStyleSheet('border-width: 1px;border-style: solid;border-color: rgb(199,237,204);background-color: rgb(199,237,204);')
        
        self.pic = QLabel(self)
        layout.addWidget(self.pic,2,1)
        tubiao = info.picture(forecast['result']['realtime']['wid']) # 按指定路径找到图片
        self.pic.setPixmap (tubiao)  # 在label上显示图片
        
        
        self.line1 = QLabel('         天气情况')   #对界面进行布局
        self.line2 = QLabel('           温度')
        self.line3 = QLabel('           湿度')
        self.line4 = QLabel('           风向')
        self.line5 = QLabel('           风力')
        self.line6 = QLabel('       空气质量指数')
        self.line1.setFrameShape(QFrame.Box)
        self.line2.setFrameShape(QFrame.Box)
        self.line3.setFrameShape(QFrame.Box)
        self.line4.setFrameShape(QFrame.Box)
        self.line5.setFrameShape(QFrame.Box)
        self.line6.setFrameShape(QFrame.Box)

        layout.addWidget(self.line1,2,0)
        layout.addWidget(self.line2,3,0)
        layout.addWidget(self.line3,4,0)
        layout.addWidget(self.line4,5,0)
        layout.addWidget(self.line5,6,0)
        layout.addWidget(self.line6,7,0)
        
        self.temperature = QLabel(forecast['result']['realtime']['temperature'])   #显示调用API得到的信息并进行布局
        self.humidity = QLabel(forecast['result']['realtime']['humidity'])
        self.info = QLabel(forecast['result']['realtime']['info'])
        self.direct = QLabel(forecast['result']['realtime']['direct'])
        self.power = QLabel(forecast['result']['realtime']['power'])
        self.aqi = QLabel(forecast['result']['realtime']['aqi'])

        layout.addWidget(self.info,2,2)
        layout.addWidget(self.temperature ,3,2)
        layout.addWidget(self.humidity,4,2)
        layout.addWidget(self.direct,5,2)
        layout.addWidget(self.power,6,2)
        layout.addWidget(self.aqi,7,2)
        
        self.tab1.setLayout(layout)
        

    def tab2UI(self):

        forecast = self.Message()     #调用API
        
        layout = QGridLayout()
      
        self.name = QLabel(dict1['CITY'])     #设置字体及底色
        layout.addWidget(self.name,1,0,1,3)
        self.name.setAlignment(Qt.AlignCenter)
        self.name.setFont(QFont("Roman times",15))
        self.name.setStyleSheet('border-width: 1px;border-style: solid;border-color: rgb(199,237,204);background-color: rgb(199,237,204);')
        

        self.line1 = QLabel('           日期')      #对界面进行布局
        self.line2 = QLabel('           温度')
        self.line3 = QLabel('           风向')
        self.line4 = QLabel('         天气情况')
       
        layout.addWidget(self.line1,2,0)
        layout.addWidget(self.line2,3,0)
        layout.addWidget(self.line3,4,0)
        layout.addWidget(self.line4,5,0)
        
        self.line1.setFrameShape(QFrame.Box)
        self.line2.setFrameShape(QFrame.Box)
        self.line3.setFrameShape(QFrame.Box)
        self.line4.setFrameShape(QFrame.Box)

        self.date = QLabel(forecast['result']['future'][0]['date'])               #显示调用API得到的信息并进行布局
        self.temperature = QLabel(forecast['result']['future'][0]['temperature'])
        self.direct = QLabel(forecast['result']['future'][0]['direct'])
        self.info = QLabel(forecast['result']['future'][0]['weather'])

        layout.addWidget(self.date,2,2)
        layout.addWidget(self.temperature ,3,2)
        layout.addWidget(self.direct,4,2)
        layout.addWidget(self.info,5,2)

      
        self.tab2.setLayout(layout)


    def  tab3UI(self):

        forecast = self.Message()     #调用API
            
        layout = QGridLayout()
        
        self.name = QLabel(dict1['CITY'])    #设置字体及底色
        layout.addWidget(self.name,1,0,2,3)
        self.name.setAlignment(Qt.AlignCenter)
        self.name.setFont(QFont("Roman times",15))
        self.name.setStyleSheet('border-width: 1px;border-style: solid;border-color: rgb(199,237,204);background-color: rgb(199,237,204);')

        self.line1 = QLabel('           日期')    #对界面进行布局
        self.line2 = QLabel('           温度')
        self.line3 = QLabel('         天气情况')
        self.blank1 = QLabel('                    ')

        self.line4 = QLabel('           日期')
        self.line5 = QLabel('           温度')
        self.line6 = QLabel('         天气情况')
        self.blank2 = QLabel('                    ')

        self.line7 = QLabel('           日期')
        self.line8 = QLabel('           温度')
        self.line9 = QLabel('         天气情况')
        self.blank3 = QLabel('                    ')

        layout.addWidget(self.line1,3,0)
        layout.addWidget(self.line2,4,0)
        layout.addWidget(self.line3,5,0)
        layout.addWidget(self.blank1,6,0)
        self.line1.setFrameShape(QFrame.Box)
        self.line2.setFrameShape(QFrame.Box)
        self.line3.setFrameShape(QFrame.Box)
        
        layout.addWidget(self.line4,7,0)
        layout.addWidget(self.line5,8,0)
        layout.addWidget(self.line6,9,0)
        layout.addWidget(self.blank2,10,0)
        self.line4.setFrameShape(QFrame.Box)
        self.line5.setFrameShape(QFrame.Box)
        self.line6.setFrameShape(QFrame.Box)

        layout.addWidget(self.line7,11,0)
        layout.addWidget(self.line8,12,0)
        layout.addWidget(self.line9,13,0)
        layout.addWidget(self.blank3,14,0)
        self.line7.setFrameShape(QFrame.Box)
        self.line8.setFrameShape(QFrame.Box)
        self.line9.setFrameShape(QFrame.Box)

        self.date1 = QLabel(forecast['result']['future'][1]['date'])             #显示调用API得到的信息并进行布局
        self.temperature1 = QLabel(forecast['result']['future'][1]['temperature'])
        self.info1 = QLabel(forecast['result']['future'][1]['weather'])

        layout.addWidget(self.date1,3,2)
        layout.addWidget(self.temperature1 ,4,2)
        layout.addWidget(self.info1,5,2)

        self.date2 = QLabel(forecast['result']['future'][2]['date'])
        self.temperature2 = QLabel(forecast['result']['future'][2]['temperature'])
        self.info2 = QLabel(forecast['result']['future'][2]['weather'])

        layout.addWidget(self.date2,7,2)
        layout.addWidget(self.temperature2 ,8,2)
        layout.addWidget(self.info2,9,2)

        self.date3 = QLabel(forecast['result']['future'][3]['date'])
        self.temperature3 = QLabel(forecast['result']['future'][3]['temperature'])
        self.info3 = QLabel(forecast['result']['future'][3]['weather'])

        layout.addWidget(self.date3,11,2)
        layout.addWidget(self.temperature3 ,12,2)
        layout.addWidget(self.info3,13,2)
        
        self.tab3.setLayout(layout)


    def Message(self):
        city = dict1['CITY']
        forecast = API.diaoyong(city)   #获得调用API的结果
        return forecast
        
         


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    w = GUI()
    w.show()
    sys.exit(app.exec_())
   


