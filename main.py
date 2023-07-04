
def find_all_possibilities(lst, i):
    if (i > u) or (len(lst) == o):
        possibilities.append(lst)

    if (i not in [_[0] for _ in lst]):
        for myitem in range(1, u + 1):
            if (myitem not in [_[1] for _ in lst]):
                if len([0 for p in lst if abs(p[0] - i) == abs(p[1] - myitem)]) == 0:
                    find_all_possibilities(lst + [[i, myitem]], i + 1)


def start(n, k):
    global possibilities, u, o
    u = n
    o = k
    possibilities = []
    find_all_possibilities([], 1)
    return possibilities
answers= start(8, 8)


pages=[]
page = 1
resetHandel=page
for u in range(2,93):
    pages.append("page"+str(u))
pages.append("page1")

def next():
    global page
    global label
    page +=1
    if(page==93):page=1
    label.config(text=pages[page-2])
    show(0)
    label.pack()

def previous():
    global page
    global label
    page -=1
    if(page==-91):page=1
    label.config(text=pages[page-2])
    show(1)
    label.pack()

def reset():
    global page
    global label
    global resetHandel
    if(page!=1):
        resetHandel = page
        label.config(text="page1")
        page = 1
        show(2)
        label.pack()

def show(a):
    global page
    global pages
    global resetHandel
    print(page,resetHandel)

    for x in range(0, 8):
        canvas_window.create_rectangle(60 * (answers[page - 1][x][1] - 1), 60 * (answers[page - 1][x][0] - 1),
                                       60 * (answers[page - 1][x][1]), 60 * (answers[page - 1][x][0]), fill="yellow",tags=pages[page-1])

    if(a==0):#next
        canvas_window.delete(pages[page-2])
    if(a==1):#previous
        canvas_window.delete(pages[page])
    if(a==2):
        canvas_window.delete(pages[resetHandel-1])


from tkinter import *
window = Tk()
window.title('8vazir')
window.geometry('600x650')
window.resizable(0, 0)
label = Label(window, text="page1", background="black", fg="white", font="Times 20  bold",padx=200,pady=5)
label.pack()
canvas_window = Canvas(window, width=480 ,height=480)
canvas_window.pack()
image_file1 = PhotoImage(file='1.png')
canvas_window.create_image(240,240 , image=image_file1)
Button(window, text="     NEXT     ",bg="yellow",fg="black",command=next,font="Times 12  bold",padx=195).pack()
Button(window, text="PREVIOUS",bg="yellow",fg="black",command=previous,font="Times 12  bold",padx=195).pack()
Button(window, text="   RESET    ",bg="yellow",fg="black",command=reset,font="Times 12  bold",padx=195).pack()
show(0)
window.mainloop()
