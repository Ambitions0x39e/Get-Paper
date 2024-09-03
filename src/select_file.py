def select_file():
    from PySide6.QtWidgets import QApplication, QFileDialog
    import sys
    app = QApplication(sys.argv)

    # file_path, _ = QFileDialog.getOpenFileName(None, "打开文件", "", "所有文件 (*);;文本文件 (*.txt)")
    file_path, _tmp = QFileDialog.getOpenFileName(None, 'Open file', "", "All files(*);; Text Files(*.txt, *.rtf);; Windows Executables(*.exe)")
    
    return file_path