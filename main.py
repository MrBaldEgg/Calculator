from tkinter import *
import operator



def key_press(event):

    if event.keysym.isdigit():
        button_click(event.keysym)
    elif event.keysym in keyboard_operators.keys():
        button_click(keyboard_operators[str(event.keysym)])
    else:
        print(event.keysym)

def button_click(num):
    global turn
    if str(num).isdigit():
        if statement[turn] == '0':
            statement[turn] = str(num)
        else:
            statement[turn] += str(num)
        result.set(statement[turn])
        
    elif num == 'del':
        statement[turn] = statement[turn][:-1]
        result.set(statement[turn])

    elif num == 'clear':
        statement[turn] = str(0)
        result.set(statement[turn])
    elif num in ('/','*','-','+') and statement[2] == '0' and statement[0] != '0':
        turn = 1
        statement[turn] = num
        turn  = 2  
        result.set(statement[1])
    elif num == '=' and statement[1] != '':
        try:

            result.set( str(operators[statement[1]](int(statement[0]),int(statement[2]))))
            turn = 0
            statement[1] = ''
            statement[2] = '0'
            statement[0] = '0'
        except ZeroDivisionError:
            result.set('Division by zero!')
            turn = 0
            statement[1] = ''
            statement[2] = '0'
            statement[0] = '0'






root = Tk()
statement = ['0','','0']
turn = 0
manip = ''
result = StringVar()
result.set(0)
standart_font = ('Arial', 30)

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

keyboard_operators = {
    "slash": '/',
    "asterisk": '*',
    "minus": '-',
    "plus": '+',
    "Return": '=',
    "BackSpace": 'del', 
    "Delete": 'clear'
}

root.title('Calculator')
root.geometry('400x600')
root.resizable(width=False, height=False)

frame_view = Frame(root, bg = "#202020")
frame_view.place(x=0, y=0, relheight=0.4, relwidth=1)

frame_btns = Frame(root, bg = "#494949", bd = 1)
frame_btns.place(relx = 0, rely= 0.4, relheight=0.6, relwidth=1)


btn_width = 11
btn_height = 5
for i in range(5):
    frame_btns.columnconfigure(index=i, weight=1)
    frame_btns.rowconfigure(index=i, weight=1)

#Numbers
btn_1 = Button(frame_btns, text = '1',     bg = '#202020', fg = "#FFFFFF", bd = 1, width=btn_width, height=btn_height, font=30, command=lambda: button_click(1))
btn_1.grid(row = 2, column=0,)
btn_2 = Button(frame_btns, text = '2',     bg = '#202020', fg = "#FFFFFF", bd = 1, width=btn_width, height=btn_height, font=30, command=lambda: button_click(2) )
btn_2.grid(row = 2, column=1,)
btn_3 = Button(frame_btns, text = '3',     bg = '#202020', fg = "#FFFFFF", bd = 1, width=btn_width, height=btn_height, font=30, command=lambda: button_click(3)  )
btn_3.grid(row = 2, column=2,)
btn_4 = Button(frame_btns, text = '4',     bg = '#202020', fg = "#FFFFFF", bd = 1, width=btn_width, height=btn_height, font=30, command=lambda: button_click(4)  )
btn_4.grid(row = 1, column=0,)
btn_5 = Button(frame_btns, text = '5',     bg = '#202020', fg = "#FFFFFF", bd = 1, width=btn_width, height=btn_height, font=30 , command=lambda: button_click(5) )
btn_5.grid(row = 1, column=1,)
btn_6 = Button(frame_btns, text = '6',     bg = '#202020', fg = "#FFFFFF", bd = 1, width=btn_width, height=btn_height, font=30, command=lambda: button_click(6)  )
btn_6.grid(row = 1, column=2,)
btn_7 = Button(frame_btns, text = '7',     bg = '#202020', fg = "#FFFFFF", bd = 1, width=btn_width, height=btn_height, font=30 , command=lambda: button_click(7) )
btn_7.grid(row = 0, column=0,)
btn_8 = Button(frame_btns, text = '8',     bg = '#202020', fg = "#FFFFFF", bd = 1, width=btn_width, height=btn_height, font=30, command=lambda: button_click(8)  )
btn_8.grid(row = 0, column=1,)
btn_9 = Button(frame_btns, text = '9',     bg = '#202020', fg = "#FFFFFF", bd = 1, width=btn_width, height=btn_height, font=30 , command=lambda: button_click(9) )
btn_9.grid(row = 0, column=2,)
btn_0 = Button(frame_btns, text = '0',     bg = '#202020', fg = "#FFFFFF", bd = 1, width=btn_width, height=btn_height, font=30, command=lambda: button_click(0)  )
btn_0.grid(row = 3, column=1,)

#manipulations
btn_div = Button(frame_btns, text = '/',     bg = '#202020', fg = "#FFFFFF", bd = 1, width=btn_width, height=btn_height, font=30 , command=lambda: button_click('div') )
btn_div.grid(row = 0, column=3,)
btn_mult = Button(frame_btns, text = '*',     bg = '#202020', fg = "#FFFFFF", bd = 1, width=btn_width, height=btn_height, font = 30, command=lambda: button_click('mult')  )
btn_mult.grid(row = 1, column=3,)
btn_min = Button(frame_btns, text = '-',     bg = '#202020', fg = "#FFFFFF", bd = 1, width=btn_width, height=btn_height, font=30 , command=lambda: button_click('min') )
btn_min.grid(row = 2, column=3,)
btn_plus = Button(frame_btns, text = '+',     bg = '#202020', fg = "#FFFFFF", bd = 1, width=btn_width, height=btn_height, font=30, command=lambda: button_click('plus')  )
btn_plus.grid(row = 3, column=3,)

btn_del = Button(frame_btns, text = '<=',     bg = '#202020', fg = "#FFFFFF", bd = 1, width=btn_width, height=btn_height, font=30 , command=lambda: button_click('del') )
btn_del.grid(row = 4, column=0,)
btn_clear = Button(frame_btns, text = 'CLEAR',     bg = '#202020', fg = "#FFFFFF", bd = 1, width=btn_width, height=btn_height, font=('Arial', 10), command=lambda: button_click('clear') )
btn_clear.grid(row = 4, column=1,)
btn_eq = Button(frame_btns, text = '=',     bg = "#FF6262", fg = "#000000", bd = 1, width=btn_width*2, height=btn_height, font=30, command=lambda: button_click('=') )
btn_eq.grid(row = 4, column=2, columnspan=2)




display = Label(frame_view, textvariable=result , bg = '#202020', fg = 'white', font = standart_font )
display.pack(ipadx= 5, side=RIGHT)

root.bind("<KeyPress>", key_press)
root.focus_set()





root.mainloop()