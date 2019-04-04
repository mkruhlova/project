from tkinter import *
import os

main_screen=Tk()
main_screen.geometry("700x450")
main_screen.title("Account Login")

Label(text="Zaloguj sie", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()


def login_verification():
    print("working...")

def login():
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password__login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password__login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verification).pack()

Button(text="Login", height="2", width="30", command=login).pack()
Label(text="").pack()



root=Tk()
root.title('MagazynPro')
root.geometry('1020x620')

mainmenu = Menu(root)
root.config(menu=mainmenu)
docmenu = Menu(mainmenu, tearoff=0)
magmenu = Menu (mainmenu, tearoff=0)
magmenu2=Menu(magmenu,tearoff=0)
dicmenu = Menu (mainmenu, tearoff=0)
winmenu = Menu (mainmenu, tearoff=0)
logout = Menu (mainmenu, tearoff=0)

mainmenu.add_cascade(label='Dokumenty', menu=docmenu)

docmenu.add_command(label='Dokumenty przychodowe')
docmenu.add_command(label='Dokumenty rozchodowe')
docmenu.add_command(label='Dokumenty inwentaryzacyjne')
docmenu.add_command(label='Zamkniecie miesiaca')


mainmenu.add_cascade(label='Magazyny', menu=magmenu)

magmenu.add_command(label='Kartoteki magazynowe')
magmenu.add_command(label='Bilans otwarcia')
magmenu.add_command(label='Inwentaryzacja')
magmenu.add_cascade(label='Dokumenty magazynowe', menu=magmenu2)

magmenu2.add_command(label='wg dokumentow')
magmenu2.add_command(label='wg indeksow')
magmenu2.add_command(label='wg grup materialowych i indeksow')

mainmenu.add_cascade(label='Slowniki',menu=dicmenu)

dicmenu.add_command(label='Indeksy materialowe')
dicmenu.add_command(label='Kartoteka kontrahentow')
dicmenu.add_command(label='Jdnostki firmy')
dicmenu.add_command(label='Jednostki miary')
dicmenu.add_command(label='Magazyny')
dicmenu.add_command(label='Dokumenty magazynowe')

mainmenu.add_cascade(label='Pomoc', menu=winmenu)
winmenu.add_command(label='O programie')
winmenu.add_command(label='Instrukcja obsugi')

mainmenu.add_command(label='Wyjscie')


main_screen.mainloop()
root.mainloop()