from tkinter import * 
from tkinter import ttk
from tkinter import font
import random
from BubbleSort import bubble_sort
from SelectionSort import select_sort
from MergeSort import merge_sort
from QuickSort import quick_sort

root = Tk()
root.title('Sorting Algorithms Visualizer')

#variables 
HEIGHT = 700
WIDTH = 800
data = []

selected_alg = StringVar()

def StartAlgorithm():
    global data

    if alg_menu.get() == 'Bubble Sort':
        bubble_sort(data, DrawArray, speed.get())
    elif alg_menu.get() == 'Selection Sort':
        select_sort(data, DrawArray, speed.get())
    elif alg_menu.get() == 'Merge Sort':
        merge_sort(data, DrawArray, speed.get())
    elif alg_menu.get() == 'Quick Sort':
        merge_sort(data, DrawArray, speed.get())
        



def DrawArray(data, colorsArr):
    canvas.delete('all')

    c_height = 490
    c_width = 720
    x_width = c_width / (len(data) + 1)
    offset = 20
    spacing = 10

    normalizedData = [ i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 450
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorsArr[i])
        canvas.create_text(x0+5, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()


def Generate():
    global data

    try:
        size = int(sizeEntry.get())
    except:
        size = 10
    
    try:
        minValue = int(minEntry.get())
    except:
        minValue = 1

    try:
        maxValue = int(maxEntry.get())
    except:
        maxValue = 15

    if minValue < 0 : minValue = 0
    if maxValue > 100 : maxValue = 100
    if size > 30 or size < 3: size = 25
    if minValue > maxValue : minValue, maxValue = maxValue, minValue

    data = []
    for _ in range(size):
        data.append(random.randrange(minValue, maxValue + 1))

    DrawArray(data, ['#FFBF00' for x in range(len(data))])

#base layout
base_canvas = Canvas(root, height = HEIGHT, width = WIDTH)
base_canvas.pack()

frame = Frame(base_canvas, bg = '#36454F', bd = 3)
frame.place(relheight = 1, relwidth = 1)

upper_frame = Frame(frame, bd = 5)
upper_frame.place(anchor = 'n', relx = 0.5, rely = 0.05, relwidth = 0.9, relheight = 0.17)

canvas = Canvas(frame, bd = 3)
canvas.place(anchor = 'n', relx = 0.5, rely = 0.25, relwidth = 0.9, relheight = 0.7)

#User Interface Area

#Row0
Label(upper_frame, text="Min Value ", bg='grey').place(relx = 0.05, rely = 0.05, relwidth = 0.1, relheight = 0.4)
minEntry = Entry(upper_frame)
minEntry.place(relx = 0.15, rely = 0.05, relwidth = 0.1, relheight = 0.4)

Label(upper_frame, text="Max Value ", bg='grey').place(relx = 0.3, rely = 0.05, relwidth = 0.1, relheight = 0.4)
maxEntry = Entry(upper_frame)
maxEntry.place(relx = 0.4, rely = 0.05, relwidth = 0.1, relheight = 0.4)

Label(upper_frame, text="Size ", bg='grey').place(relx = 0.55, rely = 0.05, relwidth = 0.1, relheight = 0.4)
sizeEntry = Entry(upper_frame)
sizeEntry.place(relx = 0.65, rely = 0.05, relwidth = 0.1, relheight = 0.4)

Button(upper_frame, text="Generate Data", command=Generate, bg='#B6D0E2').place(relx = 0.8, rely = 0.05, relwidth = 0.15, relheight = 0.4)
#Row1
Label(upper_frame, text = 'Algorithm', bg = 'grey').place(relx = 0.05, rely = 0.5, relwidth = 0.15, relheight = 0.4)
alg_menu = ttk.Combobox(upper_frame, textvariable = selected_alg, values = ['Bubble Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort'])
alg_menu.place(relx = 0.2, rely = 0.5, relwidth = 0.15, relheight = 0.4)
alg_menu.current(0)

speed = Scale(upper_frame, from_ = 0.1, to = 2.0, length = 200, resolution = 0.2, digits = 2, label = "Select Speed", orient = HORIZONTAL)
speed.place(relx = 0.4, rely = 0.5)


Button(upper_frame, text="Start Sorting!", command=StartAlgorithm, bg='#B6D0E2').place(relx = 0.8, rely = 0.5, relwidth = 0.15, relheight = 0.4)


root.mainloop()
