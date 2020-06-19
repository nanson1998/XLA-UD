from tkinter import *
from tkinter.colorchooser import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
import lip
from lip import runmain



def getColor():
    color = askcolor()
    a = []
    a = color[0]
    return a
    # ensure a file path was selected
def getimagecolor():
    path1 = filedialog.askopenfilename()
    image1 = cv2.imread(path1)
    return image1
def select_image():
    # grab a reference to the image panels
    global panelA, panelB

    # open a file chooser dialog and allow the user to select an input
    # image
    path = filedialog.askopenfilename()

    # ensure a file path was selected
    if len(path) > 0:
        # load the image from disk, convert it to grayscale, and detect
        # edges in it

        image = cv2.imread(path)
        image1 = getimagecolor()
        runmain(image, image1)



        # OpenCV represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        # kq = Image.fromarray(kq)


        # ...and then to ImageTk format
       # kq = ImageTk.PhotoImage(kq)
     #  imag = ImageTk.PhotoImage(imag)



    # if the panels are None, initialize them
#  if panelA is None or panelB is None:
        # the first panel will store our original image
#        panelA = Label(image=image)
#        panelA.image = image
#        panelA.pack(side="left", padx=10, pady=10)

        # while the second panel will store the edge map
#        panelB = Label(image=imag)
#       panelB.image = imag
#       panelB.pack(side="right", padx=10, pady=10)

    # otherwise, update the image panels
#    else:
        # update the pannels
#        panelA.configure(image=image)
#        panelB.configure(image=imag)
#        panelA.image = image
#        panelB.image = imag




root = Tk()

panelA = None
panelB = None

# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
#btn2 = Button(root, text="Select color image", command=getimagecolor)
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
#btn2.pack(side="bottom", fill="both", expand="yes", padx="20", pady="10")

root.mainloop()