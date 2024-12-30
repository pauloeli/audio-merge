import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from pydub import AudioSegment


class AudioMergerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Audio Merger')
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QtGui.QIcon('audio_icon.png'))
        self.center()

        layout = QtWidgets.QVBoxLayout()

        self.file_list = QtWidgets.QListWidget()
        layout.addWidget(self.file_list)

        self.add_button = QtWidgets.QPushButton('Add Audio Files')
        self.add_button.clicked.connect(self.add_files)
        layout.addWidget(self.add_button)

        self.remove_button = QtWidgets.QPushButton('Remove Selected')
        self.remove_button.clicked.connect(self.remove_selected)
        layout.addWidget(self.remove_button)

        self.quality_label = QtWidgets.QLabel('Select Output Quality (kbps):')
        layout.addWidget(self.quality_label)

        self.quality_combo = QtWidgets.QComboBox()
        self.quality_combo.addItems(['64', '128', '192', '256', '320'])
        layout.addWidget(self.quality_combo)

        self.merge_button = QtWidgets.QPushButton('Merge and Export')
        self.merge_button.clicked.connect(self.merge_files)
        layout.addWidget(self.merge_button)

        self.setLayout(layout)

    def add_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, 'Select Audio Files', '', 'Audio Files (*.mp3 *.ogg *.wav)')
        if files:
            for file in files:
                self.file_list.addItem(file)

    def remove_selected(self):
        for item in self.file_list.selectedItems():
            self.file_list.takeItem(self.file_list.row(item))

    def merge_files(self):
        if self.file_list.count() < 2:
            QMessageBox.warning(self, 'Warning', 'Please add at least two audio files to merge.')
            return

        files = [self.file_list.item(i).text() for i in range(self.file_list.count())]
        quality = int(self.quality_combo.currentText())

        try:
            combined = AudioSegment.from_file(files[0])
            for file in files[1:]:
                audio = AudioSegment.from_file(file)
                combined += audio

            output_path, _ = QFileDialog.getSaveFileName(self, 'Save Merged File', '', 'MP3 Files (*.mp3)')
            if output_path:
                combined.export(output_path, format='mp3', bitrate=f'{quality}k')
                QMessageBox.information(self, 'Success', 'Audio files merged successfully!')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred while merging files: {str(e)}')

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = AudioMergerApp()
    window.show()
    sys.exit(app.exec_())
