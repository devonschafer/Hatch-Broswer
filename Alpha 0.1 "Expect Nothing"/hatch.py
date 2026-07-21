from tkinter import *
from dds import DDS
import paramiko


class Prop:
    host = ''
    user = ''
    key = ''

def surf():
    page_view.delete('0.0', 'end')
    hostname = Prop.host
    username = Prop.user
    password = Prop.key
    website = url.get()
    command = 'cat /home/hatch/browser/%s' % website

    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Connect to the server
    ssh.connect(hostname, username=username, password=password)

    # Execute the command
    stdin, stdout, stderr = ssh.exec_command(command)

    # Read the output
    virtual = stdout.read().decode()
    error = stderr.read().decode()

    # Close the connection
    ssh.close()
    
    if error:
        #print("Error:", error)
        output.insert('end', 'Error:\n%s' % error)

    for a in range(DDS.virtualLines(virtual, 'all', 'count')):
        t = DDS.virtualRead(virtual, (a+1,1), 'read')
        page_view.insert('end', f'{t}\n')
        tag_font = f'font_{a}'
        tag_color = f'color_{a}'
        tag_position = f'pos_{a}'
        tag_under_line = f'under_{a}'
        page_view.tag_configure(tag_font, font=(DDS.virtualRead(virtual, (a+1,2), 'read'), int(DDS.virtualRead(virtual, (a+1,3), 'read'))))
        page_view.tag_add(tag_font, f'{a+1}.0', f'{a+1}.end')
        
        page_view.tag_configure(tag_color, foreground=(DDS.virtualRead(virtual, (a+1,4), 'read'))) 
        page_view.tag_add(tag_color, f'{a+1}.0', f'{a+1}.end')

        page_view.tag_configure(tag_position, justify=(DDS.virtualRead(virtual, (a+1,5), 'read'))) 
        page_view.tag_add(tag_position, f'{a+1}.0', f'{a+1}.end')

        page_view.tag_configure(tag_under_line, foreground=(DDS.virtualRead(virtual, (a+1,4), 'read')), underline=(DDS.virtualRead(virtual, (a+1,6), 'read')))
        page_view.tag_add(tag_under_line, f'{a+1}.0', f'{a+1}.end')
    

def open_server():
    window = Toplevel()
    window.geometry('300x200')
    name_label = Label(window, text='Server Name / IP')
    name_label.pack(side=TOP)
    server_name = Entry(window, width=40)
    server_name.pack(side=TOP, padx=5, pady=5)
    server_name.focus_set()

    user_label = Label(window, text='Username')
    user_label.pack(side=TOP)
    user_name = Entry(window, width=40)
    user_name.pack(side=TOP, padx=5, pady=5)

    key_label = Label(window, text='Password / Key')
    key_label.pack(side=TOP)
    server_key = Entry(window, width=40, show='*')
    server_key.pack(side=TOP, padx=5, pady=5)

    enter_button = Button(window, text='GO', command=lambda: submit(server_name.get(), user_name.get(), server_key.get()))
    enter_button.pack(side=TOP)

def submit(h, u, k):
    Prop.host = h
    Prop.user = u
    Prop.key = k
    surf()
    
def exit_app():
    root.destroy()

def test1():
    print('edit, open server')

def test2():
    print('help, open server')
    

size = '800x800'
name = 'DDS Browser Alpha 0.1'

root = Tk()
root.geometry(size)
root.title(name)

text_frame = Frame(root)
text_frame.pack(side=BOTTOM, expand=True, fill=BOTH)

menubar = Menu(root, relief=FLAT)
file_menu = Menu(menubar, tearoff=False, relief=FLAT)
edit_menu = Menu(menubar, tearoff=False, relief=FLAT)
help_menu = Menu(menubar, tearoff=False, relief=FLAT)

menubar.add_cascade(menu=file_menu, label='File')
file_menu.add_command(label='Open Server', command=open_server)
file_menu.add_command(label='Exit', command=exit_app)

menubar.add_cascade(menu=edit_menu, label='Edit')
edit_menu.add_command(label='Edit Server', command=test1)

menubar.add_cascade(menu=help_menu, label='Help')
help_menu.add_command(label='Help Server', command=test2)


url = Entry(root, relief=FLAT)
url.pack(side=TOP, fill=X, padx=5, pady=2)
url.insert('end', 'search.dds')
url.focus_set()

search = Button(root, text='Search', command=surf, relief=FLAT)
search.pack(side=TOP, fill=X, padx=5, pady=2)

sb = Scrollbar(text_frame, orient=VERTICAL, relief=FLAT)
sb.pack(side=RIGHT, fill=Y)
page_view = Text(text_frame, wrap=WORD, relief=FLAT)
page_view.pack(side=TOP, expand=True, fill=BOTH, padx=5, pady=5)
sb.config(command=page_view.yview)

root.config(menu=menubar)
root.mainloop()
#root.protocol("WM_DELETE_WINDOW", on_close)
