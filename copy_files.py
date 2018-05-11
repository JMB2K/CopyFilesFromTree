import os
import shutil
from appJar import gui

def copy_over(new_location, root_location, file_type=None, log=False):
    directory = os.walk(root_location)
    log_msg = 'FILES COPIED\n'
    copy_count = 0
    for fpath, fdir, files in directory:
        log_msg = log_msg + '\n' + fpath + '\n'
        for file in files:
            if file_type == 'all':
                shutil.copy(os.path.join(fpath, file), os.path.join(new_location, file))
                log_msg = log_msg + '\t' + file + '\n'
                copy_count += 1
            else:
                if file.lower().endswith(file_type.lower()):
                    shutil.copy(os.path.join(fpath, file), os.path.join(new_location, file))
                    log_msg = log_msg + '\t' + file + '\n'
                    copy_count += 1
    if log==True:
        with open('C:\\Users\\rciplp\\Desktop\\copy_log.txt', 'w') as f:
            f.write(log_msg)
            f.close()
    if log_msg == 'FILES COPIED\n':
        return app.infoBox('No Files Copied', 'No Files Copied')
    return app.infoBox('Files Copied', f'{copy_count} Files Copied')

def press(btnName):
    if btnName == 'Quit':
        app.stop()
    else:
        new_location = app.getEntry('new_location')
        root_location = app.getEntry('root_location')
        copy_over(new_location, root_location, file_type=app.getEntry('File Type'), log=app.getCheckBox('Save Log File To Desktop'))
        

app=gui()

app.startLabelFrame('Top Folder of Files to Copy')
app.addDirectoryEntry('root_location')
app.stopLabelFrame()

app.startLabelFrame('Folder to Copy Files Into')
app.addDirectoryEntry('new_location')
app.stopLabelFrame()

app.startLabelFrame('Type of Files to Copy')
app.addLabelEntry('File Type')
app.stopLabelFrame()

app.addCheckBox('Save Log File To Desktop')

app.addButtons(['Start', 'Quit'], press)

app.go()