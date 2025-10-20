import os

from src.main_view import MainView


class MainViewModel(MainView):

    def __init__(self, app):
        super().__init__()
        self.app = app

        # initial windows
        self.setWindowTitle('pyside6-starter-training')
        self.resize(300, 300)
        
        self.init_ui()


    def init_ui(self):
        self.setup_ui()

        # signal
        self.button.clicked.connect(self.on_button_clicked)
    
    def on_button_clicked(self):
        print('button clicked')