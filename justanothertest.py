import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.om_variable = tk.StringVar(self)

        b1 = tk.Button(self, text="Colors", width=8, command=self.use_colors)
        b2 = tk.Button(self, text="Sizes", width=8, command=self.use_sizes)

        self.om = tk.OptionMenu(self, self.om_variable, ())
        self.om.configure(width=20)
        self.use_colors()

        b1.pack(side="left")
        b2.pack(side="left")
        self.om.pack(side="left", fill="x", expand=True)


    def _reset_option_menu(self, options, index=None):
        '''reset the values in the option menu

        if index is given, set the value of the menu to
        the option at the given index
        '''
        menu = self.om["menu"]
        menu.delete(0, "end")
        for string in options:
            menu.add_command(label=string,
                             command=lambda value=string:
                                  self.om_variable.set(value))
        if index is not None:
            self.om_variable.set(options[index])

    def use_colors(self):
        '''Switch the option menu to display colors'''
        self._reset_option_menu(["red","orange","green","blue", "purple", "black"], 0)

    def use_sizes(self):
        '''Switch the option menu to display sizes'''
        self._reset_option_menu(["x-small", "small", "medium", "large"], 0)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


def on_buttonpress():
    subroot = Tk()
    button1 = ttk.Button(subroot, text="Apply")
    button2 = ttk.Button(subroot, text="Change Mission")
    list = ['Mission1', 'Mission2', 'Mission3']
    listbox1 = tkinter.Listbox(subroot)
    for i, item in enumerate(list):
        listbox1.insert(i, item)
    button1.grid(column=0,row=0)
    button2.grid(column=1,row=0)
    listbox1.grid(columnspan=2,row=1)