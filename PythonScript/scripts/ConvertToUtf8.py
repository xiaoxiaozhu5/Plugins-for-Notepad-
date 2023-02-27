import os;
import sys;
from Npp import notepad

encodingMap = { BUFFERENCODING.COOKIE : 'UTF-8 without BOM', BUFFERENCODING.ENC8BIT : 'ANSI', BUFFERENCODING.UTF8: 'UTF-8' }

filePathSrc=notepad.prompt('Paste path to top-level folder to process:', '', '')
if filePathSrc != None and len(filePathSrc) > 0:
    for root, dirs, files in os.walk(filePathSrc):
        for fn in files:
                notepad.open(root + "\\" + fn)
                if editor.getLexerLanguage() == 'cpp':
                    if notepad.getEncoding() != BUFFERENCODING.COOKIE and notepad.getEncoding() != BUFFERENCODING.UTF8:
                        console.write(root + "\\" + fn + " not UTF8 encoded" + "\r\n")
                        notepad.runMenuCommand("Encoding", "Convert to UTF-8")
                        notepad.save()
                notepad.close()