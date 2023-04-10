from tkinter import *

window_screen = Tk()
window_screen.title('Codeunderscored')

theFrame = Frame(
    window_screen,
    width=500,
    height=400
    )
theFrame.pack(expand=True, fill=BOTH)

theCanvas=Canvas(
    theFrame,
    bg='#4A7A8C',
    width=500,
    height=400,
    scrollregion=(0,0,700,700)
    )

vertibar=Scrollbar(
    theFrame,
    orient=VERTICAL
    )
vertibar.pack(side=RIGHT,fill=Y)
vertibar.config(command=theCanvas.yview)

horibar=Scrollbar(
    theFrame,
    orient=HORIZONTAL
    )
horibar.pack(side=BOTTOM,fill=X)
horibar.config(command=theCanvas.xview)

theCanvas.config(width=500,height=400)

theCanvas.config(
    xscrollcommand=horibar.set,
    yscrollcommand=vertibar.set
    )
theCanvas.pack(expand=True,side=LEFT,fill=BOTH)

window_screen.mainloop()