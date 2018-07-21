import time
from random import randint
import random
import string
import PySimpleGUI as SG


def SourceDestFolders():
    with SG.FlexForm('Demo Source / Destination Folders', auto_size_text=True) as form:
        form_rows = [[SG.Text('Enter the Source and Destination folders')],
                     [SG.Text('Source Folder', size=(15, 1), auto_size_text=False, justification='right'), SG.InputText('Source')],
                     [SG.Text('Destination Folder', size=(15, 1), auto_size_text=False, justification='right'), SG.InputText('Dest'), SG.FolderBrowse()],
                     [SG.Submit(), SG.Cancel()]]

        button, (source, dest) = form.LayoutAndShow(form_rows)
    if button == 'Submit':
        # do something useful with the inputs
        SG.MsgBox('Submitted', 'The user entered source:', source, 'Destination folder:', dest, 'Using button', button)
    else:
        SG.MsgBoxError('Cancelled', 'User Cancelled')

def Everything_NoContextManager():
    form = SG.FlexForm('Everything bagel', auto_size_text=True, default_element_size=(40, 1))
    layout = [[SG.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
              [SG.Text('Here is some text.... and a place to enter text')],
              [SG.InputText()],
              [SG.Checkbox('My first checkbox!'), SG.Checkbox('My second checkbox!', default=True)],
              [SG.Radio('My first Radio!', "RADIO1", default=True), SG.Radio('My second Radio!', "RADIO1")],
              [SG.Multiline(default_text='This is the default Text should you decide not to type anything', scale=(2, 10))],
              [SG.InputCombo(['choice 1', 'choice 2'], size=(20, 3))],
              [SG.Text('_' * 100, size=(70, 1))],
              [SG.Text('Choose Source and Destination Folders', size=(35, 1))],
              [SG.Text('Source Folder', size=(15, 1), auto_size_text=False), SG.InputText('Source'), SG.FolderBrowse()],
              [SG.Text('Destination Folder', size=(15, 1), auto_size_text=False), SG.InputText('Dest'), SG.FolderBrowse()],
              [SG.SimpleButton('Your very own button', button_color=('white', 'green'))],
              [SG.Submit(), SG.Cancel()]]

    button, (values) = form.LayoutAndShow(layout)

    SG.MsgBox('Title', 'Typical message box', 'Here are the restults!  There is one entry per input field ', 'The button clicked was "{}"'.format(button), 'The values are', values)


def Everything():
    with SG.FlexForm('Everything bagel', auto_size_text=True, default_element_size=(40, 1)) as form:
        layout = [[SG.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
                  [SG.Text('Here is some text.... and a place to enter text')],
                  [SG.InputText()],
                  [SG.Checkbox('My first checkbox!'), SG.Checkbox('My second checkbox!', default=True)],
                  [SG.Radio('My first Radio!', "RADIO1", default=True), SG.Radio('My second Radio!', "RADIO1")],
                  [SG.Spin(values=(1,2,3), initial_value=1, size=(2,1)), SG.T('Spinner 1', size=(20,1)),
                   SG.Spin(values=(1,2,3), initial_value=1, size=(2,1)),SG.T('Spinner 2')],
                  [SG.Multiline(default_text='This is the default Text should you decide not to type anything', scale=(2, 10))],
                  [SG.InputCombo(['choice 1', 'choice 2'], size=(20, 3))],
                  [SG.Text('_' * 100, size=(70, 1))],
                  [SG.Text('Choose Source and Destination Folders', size=(35, 1))],
                  [SG.Text('Source Folder', size=(15, 1), auto_size_text=False), SG.InputText('Source'), SG.FolderBrowse()],
                  [SG.Text('Destination Folder', size=(15, 1), auto_size_text=False), SG.InputText('Dest'), SG.FolderBrowse()],
                  [SG.SimpleButton('Custom Button', button_color=('white', 'green'))],
                  [SG.Submit(), SG.Cancel()]]

        button, (values) = form.LayoutAndShow(layout)

    SG.MsgBox('Title', 'Typical message box', 'The results of the form are a lot of data!  Get ready... ', 'The button clicked was "{}"'.format(button), 'The values are', values)

def ProgressMeter():
    for i in range(1,10000):
        if not SG.EasyProgressMeter('My Meter', i+1, 10000): break

def RunningTimer():
    with SG.FlexForm('Running Timer', auto_size_text=True) as form:
        output_element = SG.Text('', size=(8, 2), font=('Helvetica', 20))
        form_rows = [[SG.Text('Non-blocking GUI with updates')],
                     [output_element],
                     [SG.SimpleButton('Quit')]]

        form.AddRows(form_rows)
        form.Show(non_blocking=True)
        for i in range(1, 100):
            output_element.Update('{:02d}:{:02d}.{:02d}'.format(*divmod(int(i/100), 60), i%100))
            rc = form.Refresh()
            if rc is None or rc[0] == 'Quit':
                break
            time.sleep(.01)
        else:
            form.CloseNonBlockingForm()




# Persistant form. Does not close when Send button is clicked.
# Normally all Simple Buttons cause forms to close
def ChatBot():
    with SG.FlexForm('Chat Window', auto_size_text=True, default_element_size=(30, 2)) as form:
        form.AddRow(SG.Text('This is where standard out is being routed', size=[40, 1]))
        form.AddRow(SG.Output(size=(80, 20)))
        form.AddRow(SG.Multiline(size=(70, 5), enter_submits=True), SG.ReadFormButton('SEND', button_color=(SG.YELLOWS[0], SG.BLUES[0])), SG.SimpleButton('EXIT', button_color=(SG.YELLOWS[0], SG.GREENS[0])))
        button, value = form.Read()

        # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
        while True:
            if button == 'SEND':
                print(value)
            else:
                break
            button, value = form.Read()


def NonBlockingPeriodicUpdateForm_ContextManager():
    # Show a form that's a running counter
    with SG.FlexForm('Running Timer', auto_size_text=True) as form:
        output_element = SG.Text('',size=(10,2), font=('Helvetica', 20), text_color='red', justification='center')
        form_rows = [[SG.Text('Non blocking GUI with updates', justification='center')],
                     [output_element],
                     [SG.T(' '*15), SG.Quit()]]
        form.AddRows(form_rows)
        form.Show(non_blocking=True)

        for i in range(1,500):
            output_element.Update('{:02d}:{:02d}.{:02d}'.format(*divmod(int(i/100), 60), i%100))
            rc = form.Refresh()
            if rc is None:      # if user closed the window using X
                break
            button, values = rc
            if button == 'Quit':
                break
            time.sleep(.01)
        else:
            # if the loop finished then need to close the form for the user
            form.CloseNonBlockingForm()


def NonBlockingPeriodicUpdateForm():
    # Show a form that's a running counter
    form = SG.FlexForm('Running Timer', auto_size_text=True)
    output_element = SG.Text('',size=(8,2), font=('Helvetica', 20))
    form_rows = [[SG.Text('Non blocking GUI with updates')],
                 [output_element],
                 [SG.Quit()]]
    form.AddRows(form_rows)
    form.Show(non_blocking=True)

    for i in range(1,50000):
        output_element.Update(f'{(i/100)/60:02d}:{(i/100)%60:02d}.{i%100:02d}')
        rc = form.Refresh()
        if rc is None or rc[0] == 'Quit':      # if user closed the window using X or clicked Quit button
            break
        time.sleep(.01)
    else:
        # if the loop finished then need to close the form for the user
        form.CloseNonBlockingForm()


def DebugTest():
    # SG.Print('How about we print a bunch of random numbers?', , size=(90,40))
    for i in range (1,300):
        SG.Print(i, randint(1, 1000), end='', sep='-')

    # SG.PrintClose()


def main():
    SG.SetOptions(border_width=1, element_padding=(4,6), font=("Helvetica", 10), button_color=('white', SG.BLUES[0]),
                  progress_meter_border_depth=0)
    SourceDestFolders()
    Everything()
    NonBlockingPeriodicUpdateForm_ContextManager()
    ProgressMeter()
    ChatBot()
    DebugTest()

if __name__ == '__main__':
    main()
    exit(69)
