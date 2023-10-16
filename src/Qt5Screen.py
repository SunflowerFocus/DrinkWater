import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

# 创建一个小窗口并显示
window = QWidget()
window.show()

# 获取屏幕信息并打印
desktop = app.desktop()
screen_rect = desktop.screenGeometry()
print(screen_rect)

sys.exit(app.exec_())
