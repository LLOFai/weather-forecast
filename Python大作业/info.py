from PyQt5.QtGui import QPixmap
#通过调用API获得的当时天气情况，显示对应天气的图标在界面上
def picture(num):
    
    if num=='00':
        pic=QPixmap('d00.gif')

    elif num=='01':
        pic=QPixmap('d01.gif')

    elif num=='02':
        pic=QPixmap('d02.gif')

    elif num=='03':
        pic=QPixmap('d03.gif')

    elif num=='04':
        pic=QPixmap('d04.gif')

    elif num=='07':
        pic=QPixmap('d07.gif')

    elif num=='08':
        pic=QPixmap('d08.gif')

    elif num=='09':
        pic=QPixmap('d09.gif')

    elif num=='10':
        pic=QPixmap('d10.gif')

    elif num=='18':
        pic=QPixmap('d18.gif')

    elif num=='53':
        pic=QPixmap('d53.gif')

    return pic
