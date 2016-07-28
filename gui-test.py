import tkinter as Tkinter


class Application(Tkinter.Frame):
    def __init__(self, master):
        Tkinter.Frame.__init__(self, master)
        self.master.minsize(width=256, height=256)
        self.master.config()
        self.pack()

        self.main_frame = Tkinter.Frame()

        self.some_list = [
            'One',
            'Two',
            'Three',
            'Four'
        ]

        self.some_listbox = Tkinter.Listbox(self.main_frame)

        # bind the selection event to a custom function
        # Note the absence of parentheses because it's a callback function
        self.some_listbox.bind('<<ListboxSelect>>', self.listbox_changed)
        self.some_listbox.pack(fill='both', expand=True)
        self.main_frame.pack(fill='both', expand=True)

        # insert our items into the list box
        for i, item in enumerate(self.some_list):
            self.some_listbox.insert(i, item)

        # make a label to show the selected item
        self.some_label = Tkinter.Label(self.main_frame, text="Welcome to SO!")
        self.some_label.pack(side='top')

        # not really necessary, just make things look nice and centered
        self.main_frame.place(in_=self.master, anchor='c', relx=.5, rely=.5)

    def listbox_changed(self, *args, **kwargs):
        selection_index = self.some_listbox.curselection()
        selection_text = self.some_listbox.get(selection_index, selection_index)
        self.some_label.config(text=selection_text)

root = Tkinter.Tk()
app = Application(root)
app.mainloop()