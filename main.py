from PyQt5.Qt import *
from untitled import Ui_Form
import requests
class Window(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel的学习")
        self.resize(500, 500)
        self.setAttribute(Qt.WA_StyledBackground, True)#显示背景图
        self.setupUi(self)
        self.textBrowser.setText("显示屏")
        self.headers={
            'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
        }
        self.url='http://fanyi.youdao.com/translate?'
    def slot1(self):
        try:
            self.textBrowser.clear()
            text=self.textEdit.toPlainText()
            print(text)
            formdata = {
                "i": text,
                "from": "AUTO",
                "to": "AUTO",
                "smartresult": "dict",
                "client": "fanyideskweb",
                "salt": "15535006036559",
                "sign": "9d1694c4ff862813ab7b48095a529634",
                "ts": "1553500603655",
                "bv": "bbb3ed55971873051bc2ff740579bb49",
                "doctype": "json",
                "version": "2.1",
                "keyfrom": "fanyi.web",
                "action": "FY_BY_REALTlME",
                "typoResult": "false",
            }
            response=requests.post(self.url,data=formdata,headers=self.headers)
            dict=response.json()
            print(dict)
            dict=dict['translateResult']
            text = " "
            for texts in dict:
                for i in texts:
                    text+= i['tgt']
                self.textBrowser.setText(text)
        except Exception:
            pass
    def clear(self):
        self.textEdit.clear()


if __name__ == '__main__':
        import sys
        app = QApplication(sys.argv)

        window = Window()
        window.show()

        sys.exit(app.exec_())
        

