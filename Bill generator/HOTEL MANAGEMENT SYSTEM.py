from tkinter import *

#Creating Main Window And Configuring It
root = Tk()
root.title("Coffee And Tea Shop")
root.geometry("500x650")
UI_Footer_Count_label = Label(root,text = "00",state= 'disabled',fg = "Black",bg = "white", font = "Times 14 bold")
UI_Footer_Count_label.place(x=380,y=550)
root.configure(bg = "white")

#List To Hold Each Items Count
items_list = [ 0, 0, 0, 0, 0, 0]

def cleanup():
    
    items_list[0] = 0
    items_list[1] = 0
    items_list[2] = 0
    items_list[3] = 0
    items_list[4] = 0
    items_list[5] = 0

    UI_Footer_Count_label.configure(text = "00")

    return


'''
Function To Print Bill
'''
def printReceipt():
    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel(root)
  
    # sets the title of the
    # Toplevel widget
    newWindow.title("Receipt")
  
    # sets the geometry of toplevel
    newWindow.geometry("300x500")

    #Configuring Background
    newWindow.configure(bg = "white")

    total_price = 0

    if items_list[0] > 0:
        total_price = total_price + (items_list[0] * 300)
    
    if items_list[1] > 0:
        total_price = total_price + (items_list[1] * 350)
    
    if items_list[2] > 0:
        total_price = total_price + (items_list[2] * 450)
    
    if items_list[3] > 0:
        total_price = total_price + (items_list[3] * 500)
    
    if items_list[4] > 0:
        total_price = total_price + (items_list[4] * 150)
    
    if items_list[5] > 0:
        total_price = total_price + (items_list[5] * 250)

    totalItems = UI_Footer_Count_label['text']
    result = """
Coffee

 Espresso         --------------------    """+str(items_list[0])+"""
Latte               --------------------    """+str(items_list[1])+"""
Cappuccino     --------------------   """+str(items_list[2])+"""
 
Tea

English Breakfast    -------------    """+str(items_list[3])+"""\nGreen Tea        --------------------    """+str(items_list[4])+"""\nMatcha Gold    --------------------    """+str(items_list[5]

)

    label = Label(newWindow,text = result , fg = "Black",bg = "white", font = "Times 14 bold italic")
    label.grid(row= 0 , column= 0)

    new_string = """------------------------------------------------\n\nTotal Price  = """+"Rs " + str(total_price) 
    label_price = Label(newWindow , text = new_string, fg = "Black",bg = "white", font = "Times 14 bold italic")
    label_price.grid(row = 5,column= 0)


    cleanup()

    return

'''
Function to increase items count,each items count can't go more than 25
'''
def increaseCount(counter):

    flag = False

    if counter == 0:
        if items_list[0] < 25:
            items_list[0] += 1
            flag = True
            
    if counter == 1:
        if items_list[1] <= 25:
            items_list[1] += 1
            flag = True

    if counter == 2:
        if items_list[2] <= 25:
            items_list[2] += 1
            flag = True

    if counter == 3:
        if items_list[3] <= 25:
            items_list[3] += 1
            flag = True

    if counter == 4:
        if items_list[4] <= 25:
            items_list[4] += 1
            flag = True

    if counter == 5:
        if items_list[5] <= 25:
            items_list[5] += 1
            flag = True


    if flag:
        temp = int(UI_Footer_Count_label['text'])
        if temp < 9:
            UI_Footer_Count_label.configure(text= "0"+str(temp+1))
        else:
            UI_Footer_Count_label.configure(text= str(temp+1))

    return 

'''
Function to decrease item count,each item count can't go less than 0
'''
def decreaseCount(counter):

    flag = False

    if counter == 0:
        if items_list[0] > 0:
            items_list[0] -= 1
            flag = True
    
    if counter == 1:
        if items_list[1] > 0:
            items_list[1] -= 1
            flag = True
    
    if counter == 2:
        if items_list[2] > 0:
            items_list[2] -= 1
            flag = True
    
    if counter == 3:
        if items_list[3] > 0:
            items_list[3] -= 1
            flag = True
    
    if counter == 4:
        if items_list[4] > 0:
            items_list[4] -= 1
            flag = True

    if counter == 5:
        if items_list[5] > 0:
            items_list[5] -= 1
            flag = True

    if flag:
        temp = int(UI_Footer_Count_label['text'])
        temp -= 1

        if temp < 10:
            UI_Footer_Count_label.configure(text = "0"+str(temp))
        else:
            UI_Footer_Count_label.configure(text = str(temp))
        
    return 

def main():
    UI_String = "Welcome To Our Coffee Shop"
    UI_menu = "----------------------    SHOP MENU    ---------------------"
    UI_Margin = "--------------------------------------------------------------------"
    UI_Footer_text = "Total Items                    ............................"

    UI__title_label = Label(root,text = UI_String, fg = "red",bg = "white", font = "Times 18 bold")
    UI__title_label.place(x = 80,y = 10)

    UI_MenuTitle_label = Label(root, text = UI_menu, fg = "Black",bg = "white", font = "Times 16 bold italic")
    UI_MenuTitle_label.place( x = 20, y = 80)

    UI_Footer_Margin = Label(root,text=UI_Margin,fg = "Black",bg = "white", font = "Times 16 bold italic")
    UI_Footer_Margin.place(x=10,y=520)

    UI_Footer_Label = Label(root,text=UI_Footer_text,fg = "Black",bg = "white", font = "Times 14 bold italic")
    UI_Footer_Label.place(x=10,y=550)

    UI_checkout_button = Button(root,text = "Checkout", fg = "Black", font = "Times 14 bold",width = 15 , command=printReceipt)
    UI_checkout_button.place( x = 170 , y = 600)

    UI_menuItem = '1)Espresso                    .............................\n\n'+'\n2)Latte                          .............................\n\n'+'\n3)Cappuccino               .............................\n\n'+'\n4)English Breakfast       ...........................\n\n'+'\n5)Green Tea                  ............................\n\n'+'\n6)Matcha Gold              ............................'

    UI_Menu_label = Label(root, text= UI_menuItem,fg="black",bg = "white",font="times 14 bold italic")
    UI_Menu_label.place(x = 10, y = 150)

    UI_Espresso_Plus_Button = Button(root,text = "+",font="Times 14 bold",relief="groove" , height = 1,width = 1,command = lambda: increaseCount(0))
    UI_Espresso_Plus_Button.place(x = 370, y = 150)
    UI_Espresso_Minus_Button = Button(root,text = "--",font="Times 14 bold",relief="groove", height = 1,width = 1,command = lambda: decreaseCount(0))
    UI_Espresso_Minus_Button.place(x = 400, y = 150)

    UI_Latte_Plus_Button = Button(root,text = "+",font="Times 14 bold",relief="groove" , height = 1,width = 1,command = lambda: increaseCount(1))
    UI_Latte_Plus_Button.place(x = 370, y = 210)
    UI_Latte_Minus_Button = Button(root,text = "--",font="Times 14 bold",relief="groove", height = 1,width = 1,command = lambda: decreaseCount(1))
    UI_Latte_Minus_Button.place(x = 400, y = 210)

    UI_Cappicuno_Plus_Button = Button(root,text = "+",font="Times 14 bold",relief="groove" , height = 1,width = 1,command = lambda: increaseCount(2))
    UI_Cappicuno_Plus_Button.place(x = 370, y = 280)
    UI_Cappicuno_Minus_Button = Button(root,text = "--",font="Times 14 bold",relief="groove", height = 1,width = 1,command = lambda: decreaseCount(2))
    UI_Cappicuno_Minus_Button.place(x = 400, y = 280)

    UI_EB_Plus_Button = Button(root,text = "+",font="Times 14 bold",relief="groove" , height = 1,width = 1,command = lambda: increaseCount(3))
    UI_EB_Plus_Button.place(x = 370, y = 350)
    UI_EB_Minus_Button = Button(root,text = "--",font="Times 14 bold",relief="groove", height = 1,width = 1,command = lambda: decreaseCount(3))
    UI_EB_Minus_Button.place(x = 400, y = 350)

    UI_GT_Plus_Button = Button(root,text = "+",font="Times 14 bold",relief="groove" , height = 1,width = 1,command = lambda: increaseCount(4))
    UI_GT_Plus_Button.place(x = 370, y = 420)
    UI_GT_Minus_Button = Button(root,text = "--",font="Times 14 bold",relief="groove", height = 1,width = 1,command = lambda: decreaseCount(4))
    UI_GT_Minus_Button.place(x = 400, y = 420)

    UI_MG_Plus_Button = Button(root,text = "+",font="Times 14 bold",relief="groove" , height = 1,width = 1,command = lambda: increaseCount(5))
    UI_MG_Plus_Button.place(x = 370, y = 480)
    UI_MG_Minus_Button = Button(root,text = "--",font="Times 14 bold",relief="groove", height = 1,width = 1,command = lambda: decreaseCount(5))
    UI_MG_Minus_Button.place(x = 400, y = 480)

    root.mainloop()

main()
