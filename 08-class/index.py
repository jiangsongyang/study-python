class App :
    appName = 'jsy-py'

    def __init__(self) -> None:
        print(self)

    def open():
        print('app open')

    @staticmethod
    def getVersion():
        return 'V1.0.0'


app = App()
print(app.getVersion())