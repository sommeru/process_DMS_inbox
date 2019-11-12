#!./venv/bin/python3

import os
import subprocess
import glob
import os.path

"""You may need to install pip and gnureadline first"""
#try:
import gnureadline as readline
#except ImportError:
#    import readline


DMSdirectory = '/Users/sommeru/Documents/DMS/'
"""DMSdirectory = '/Users/sommeru/Desktop/test/'"""
doctypes = ['rechnung', 'kontoauszug', 'beitrag', 'entgeltabrechnung', 'bewirtungsbeleg']
DEFAULT_TEXT = ''
docid = 190000
docid_old = 190000

docdate = 20190101


def doctype_completer(text, state):
    options = [x for x in doctypes if x.startswith(text)]
    try:
        return options[state]
    except IndexError:
        return None

def docpath_completer(text, state):
    try:
        return [x for x in
                glob.glob(text+'*[\-_A-Za-z0-9][\-_A-Za-z0-9][\-_A-Za-z0-9][\-_A-Za-z0-9]')][state] + '/'
    except IndexError:
        return None


def input_with_prefill(prompt, text):
    def hook():
        readline.insert_text(text)
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    try:
        result = input(prompt)
    except :
        result = ''
    readline.set_pre_input_hook()
    return result

readline.set_completer_delims('')

if 'libedit' in readline.__doc__:
    readline.parse_and_bind("bind ^I rl_complete")
else:
    readline.parse_and_bind("tab: complete")

os.chdir(DMSdirectory + 'Documents')



for (dirpath, dirnames, filenames) in os.walk(DMSdirectory+'inbox'):
    for name in filenames:
        filename_old = os.path.join(dirpath, name)
        if name.endswith(".pdf"):
            print ('Processing: ' + filename_old)

            subprocess.call(["/usr/bin/open", "-a", "/System/Applications/Preview.app", filename_old])
            subprocess.call(['osascript', '-e', 'tell application "Preview" to set bounds of front window to {0, 0, 720, 870}'])
            subprocess.call(['osascript', '-e', 'activate application "iTerm"'])


            """Read docdate"""
            readline.set_completer()
            docdate = input_with_prefill("Enter docdate: ",str(docdate))

            """Read docid"""
            readline.set_completer()

            docid = input_with_prefill("Enter id: ",str(docid_old + 1))
            if  (docid != ""):
                print ('a number: remembering docid')
                docid_old = int(docid)

            """Read docpath"""
            readline.set_completer(docpath_completer)
            docpath = input('Enter docpath: ')

            """Read docdesc"""
            readline.set_completer(doctype_completer)
            docdesc = input('Enter docdesc:')


            """Set new filename"""
            filename_new = DMSdirectory + "Documents/" + docpath + str(docdate) + "-" + str(docid) + "-" + docdesc + ".pdf"
            #print ('Moving to: ' + filename_new)
            move_command = 'mv "' + filename_old + '" "' + filename_new + '"'
            print (move_command)
            subprocess.call(['mv',filename_old, filename_new])
            """subprocess.Popen(move_command)"""







            subprocess.call(['osascript', '-e', 'tell application "Preview" to quit'])

        else:
            print ('Ignoring: ' + filename_old)
        print ('----------------------------------------------------------------')


