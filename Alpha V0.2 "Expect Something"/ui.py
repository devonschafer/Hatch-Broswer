from tkinter import *
from tkinter import filedialog
from dds import DDS
from export import Export
from server import ServerSide


class UI:
    def __init__(self, master):

        self.ddsp = '''server dialog::300,,200,,Log In,,Server Name / IP,,Username,,Password / Key,,GO
                        DDS Editor::800,,800,,DDS Editor,,File,,Save Local,,Load Local,,Publish,,Test Page
                        DDS Browser::File,,Open Server,,Exit,,Edit,,DDS Editor,,Help,,Help Server,,Search,,Status bar,,
                    '''

        def open_server():
            self.window = Toplevel()
            self.window.geometry('%sx%s' % (DDS.virtualRead(self.ddsp, (1,1), 'read'), DDS.virtualRead(self.ddsp, (1,2), 'read')))
            self.window.title(DDS.virtualRead(self.ddsp, (1,3), 'read'))
            self.name_label = Label(self.window, text=DDS.virtualRead(self.ddsp, (1,4), 'read'))
            self.name_label.pack(side=TOP)
            self.server_name = Entry(self.window, width=40)
            self.server_name.pack(side=TOP, padx=5, pady=5)
            self.server_name.focus_set()

            self.user_label = Label(self.window, text=DDS.virtualRead(self.ddsp, (1,5), 'read'))
            self.user_label.pack(side=TOP)
            self.user_name = Entry(self.window, width=40)
            self.user_name.pack(side=TOP, padx=5, pady=5)

            self.key_label = Label(self.window, text=DDS.virtualRead(self.ddsp, (1,6), 'read'))
            self.key_label.pack(side=TOP)
            self.server_key = Entry(self.window, width=40, show='*')
            self.server_key.pack(side=TOP, padx=5, pady=5)

            self.enter_button = Button(self.window, text=DDS.virtualRead(self.ddsp, (1,7), 'read'), relief=FLAT,command=lambda: submit(self.server_name.get(),
                                                                                                  self.user_name.get(),
                                                                                                  self.server_key.get()))
            self.enter_button.pack(side=TOP, fill=X)
            Export.url = self.url.get()

        def submit(h, u, k):
            Export.host = h
            Export.user = u
            Export.key = k
            ServerSide.surf()

        def navigate():
            Export.url = self.url.get()
            ServerSide.surf()
            

        def dds_editor():
            self.window = Toplevel()
            self.window.geometry('%sx%s' % (DDS.virtualRead(self.ddsp, (2,1), 'read'), DDS.virtualRead(self.ddsp, (2,2), 'read')))
            self.window.title(DDS.virtualRead(self.ddsp, (2,3), 'read'))

            self.menubar = Menu(self.window, relief=FLAT)
            self.file_menu = Menu(self.menubar, tearoff=False, relief=FLAT)

            self.menubar.add_cascade(menu=self.file_menu, label=DDS.virtualRead(self.ddsp, (2,4), 'read'))
            self.file_menu.add_command(label=DDS.virtualRead(self.ddsp, (2,5), 'read'), command=lambda: save_local(self.body.get('1.0', 'end')))
            self.file_menu.add_command(label=DDS.virtualRead(self.ddsp, (2,6), 'read'), command=load_local)
            self.file_menu.add_command(label=DDS.virtualRead(self.ddsp, (2,7), 'read'), command=lambda: publish_web_page(self.body.get('1.0', 'end')))
            self.file_menu.add_command(label=DDS.virtualRead(self.ddsp, (2,8), 'read'), command=lambda: test_webpage(self.body.get('1.0', 'end')))
            
            self.body = Text(self.window, wrap=WORD, relief=FLAT)
            self.body.pack(side=TOP, expand=True, fill=BOTH, padx=5, pady=5)
            self.body.focus()

            self.window.config(menu=self.menubar)

        def save_local(string):
            saveFile = filedialog.asksaveasfilename()
            DDS.writeFile('%s' % saveFile, string, 'save')

        def load_local():
            openFile = filedialog.askopenfilename()
            Export.publish_path = openFile
            self.body.delete('1.0', 'end')
            self.body.insert(END, DDS.readFile('%s' % openFile, 'all', None))

        def publish_web_page(string):
            Export.publish = '%s' % string
            ServerSide.publish_page()
            #DDS.appendFile('testing.dds', string, 'save')

        def test_webpage(string):
            Export.virtual_webpage = ''
            Export.refresh = 1
            Export.virtual_webpage = string

        def exit_app():
            master.destroy()

        def test2():
            print('Help menu')

        def surf():
            print('surf')
        
        self.controls_frame = Frame()
        self.controls_frame.pack(side=TOP, fill=X, anchor='n')

        self.text_frame = Frame()
        self.text_frame.pack(side=TOP, expand=True, fill=BOTH)

        self.status_frame = Frame()
        self.status_frame.pack(side=TOP, fill=X, anchor='s')

        self.menubar = Menu(relief=FLAT)
        self.file_menu = Menu(self.menubar, tearoff=False, relief=FLAT)
        self.edit_menu = Menu(self.menubar, tearoff=False, relief=FLAT)
        self.help_menu = Menu(self.menubar, tearoff=False, relief=FLAT)

        self.menubar.add_cascade(menu=self.file_menu, label=DDS.virtualRead(self.ddsp, (3,1), 'read'))
        self.file_menu.add_command(label=DDS.virtualRead(self.ddsp, (3,2), 'read'), command=open_server)
        self.file_menu.add_command(label=DDS.virtualRead(self.ddsp, (3,3), 'read'), command=exit_app)

        self.menubar.add_cascade(menu=self.edit_menu, label=DDS.virtualRead(self.ddsp, (3,4), 'read'))
        self.edit_menu.add_command(label=DDS.virtualRead(self.ddsp, (3,5), 'read'), command=dds_editor)

        self.menubar.add_cascade(menu=self.help_menu, label=DDS.virtualRead(self.ddsp, (3,6), 'read'))
        self.help_menu.add_command(label=DDS.virtualRead(self.ddsp, (3,7), 'read'), command=test2)

        master.config(menu=self.menubar)

        self.url = Entry(self.controls_frame, relief=FLAT)
        self.url.pack(side=TOP, fill=X, padx=5, pady=2)
        self.url.insert('end', 'welcome.dds')
        self.url.focus_set()

        self.search = Button(self.controls_frame, text=DDS.virtualRead(self.ddsp, (3,8), 'read'), command=navigate, relief=FLAT)
        self.search.pack(side=TOP, fill=X, padx=5, pady=2)

        self.sb = Scrollbar(self.text_frame, orient=VERTICAL, relief=FLAT)
        self.sb.pack(side=RIGHT, fill=Y)
        self.page_view = Text(self.text_frame, wrap=WORD, relief=FLAT)
        self.page_view.pack(side=TOP, expand=True, fill=BOTH, padx=5, pady=5)
        self.sb.config(command=self.page_view.yview)

        self.status_bar = Label(self.status_frame, text=DDS.virtualRead(self.ddsp, (3,9), 'read'))
        self.status_bar.pack(side=BOTTOM, fill=X)

    def update(self):
        if Export.refresh == 1:
            self.page_view.delete('1.0', 'end')
            for a in range(DDS.virtualLines(Export.virtual_webpage, 'all', 'count')):
                t = DDS.virtualRead(Export.virtual_webpage, (a+1,1), 'read')
                self.page_view.insert('end', f'{t}\n')
                tag_font = f'font_{a}'
                tag_color = f'color_{a}'
                tag_position = f'pos_{a}'
                tag_under_line = f'under_{a}'
                self.page_view.tag_configure(tag_font, font=(DDS.virtualRead(Export.virtual_webpage, (a+1,2), 'read'), int(DDS.virtualRead(Export.virtual_webpage, (a+1,3), 'read'))))
                self.page_view.tag_add(tag_font, f'{a+1}.0', f'{a+1}.end')
                
                self.page_view.tag_configure(tag_color, foreground=(DDS.virtualRead(Export.virtual_webpage, (a+1,4), 'read'))) 
                self.page_view.tag_add(tag_color, f'{a+1}.0', f'{a+1}.end')

                self.page_view.tag_configure(tag_position, justify=(DDS.virtualRead(Export.virtual_webpage, (a+1,5), 'read'))) 
                self.page_view.tag_add(tag_position, f'{a+1}.0', f'{a+1}.end')

                self.page_view.tag_configure(tag_under_line, foreground=(DDS.virtualRead(Export.virtual_webpage, (a+1,4), 'read')), underline=(DDS.virtualRead(Export.virtual_webpage, (a+1,6), 'read')))
                self.page_view.tag_add(tag_under_line, f'{a+1}.0', f'{a+1}.end')
                
            Export.refresh = 0

        self.page_view.after(1000, self.update)

        
