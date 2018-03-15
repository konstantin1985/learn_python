
# MAIN SOURCE:
# Kasampalis "Mastering Python Patterns" Chapter 8

# USEFUL LINKS:
# 
# 1) Problem with displaying Tkinter window
#    https://mail.python.org/pipermail/python-list/2013-December/663528.html
#
# 2) Tutorial on Tkinter
#    https://pythonprogramming.net/tkinter-python-3-tutorial-adding-buttons/?completed=/python-3-tkinter-basics-tutorial/
#
# 3) Anchors in Tkinter's labels
#    https://stackoverflow.com/questions/21495367/how-to-align-text-to-the-left
#
# 4) Invoke callbacks in MVC controller
#    https://stackoverflow.com/questions/46188060/how-to-pass-model-action-to-view-button-in-tkinter-mvc
#
# 5) Tkinter and self
#    http://zetcode.com/gui/tkinter/dialogs/


# GENERAL INFORMATION:

# Here there are some modifications of the exercise.

# V Make the program more user-friendly by allowing only indexes of values
#   greater than or equal to 1 to be given by the user. You will also need
#   to modify get_quote().
# V Add a graphical view using a GUI framework such as Tkinter, Pygame, or
#   Kivy. How modular is the program? Can you decide during runtime which
#   view will be used?
# - Give the user an option to view a random quote by typing a key, for
#   example, key r.
# - The index validation is currently done in the controller. Is that a good
#   approach? What happens if you write another view that needs its own
#   controller? Think about the changes required to move index validation
#   in the model to make the code reusable for all controller/view pairs.
# - Extend this example to make it work like a Create, Read, Update, Delete
#   (CRUD) application. You should be able to enter new quotes, delete
#   existing quotes, and modify a quote.

import Tkinter

print("-" * 20 + "# 1 Modified implementation" + "-" * 20)


quotes = ('A man is not complete until he is married. Then he isfinished.', 
          'As I said before, I never repeat myself.',
          'Behind a successful man is an exhausted woman.',
          'Black holes really suck...', 
          'Facts are stubborn things.')

class QuoteModel:
    
    def get_quote(self, n):
        try:
            value = quotes[n-1]  
        except IndexError as err:
            value = 'Not found!'
        return value


class QuoteTerminalView:
    
    def show(self, quote):
        print("And the quote is: '{}'".format(quote))
    
    def error(self, msg):
        print('Error: {}'.format(msg))
    
    def select_quote(self):
        return raw_input('Which quote number you like to see? ')


class QuoteTerminalController:
    
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()
        
    def run(self):
        valid_input = False
        
        while not valid_input:
            n = self.view.select_quote()
            try:
                n = int(n)
                if n < 1:
                    raise ValueError
            except ValueError as err:
                self.view.error("Incorrect Index '{}'".format(n))
            else:
                valid_input = True  # if no exception occurred

        quote = self.model.get_quote(n)
        self.view.show(quote)

def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()


class QuoteTkinterController:
    
    def __init__(self):
        
        self.root = Tkinter.Tk()         # export DISPLAY=":0" then run without sudo in a terminal        
        self.root.geometry("600x150")    # size of the window

        self.model = QuoteModel()
        self.view = QuoteTkinterView(self.root, self)
        
    def run(self):
        self.root.mainloop()

    def process_input(self, n):        
        try:
            n = int(n)
            if n < 1:
                raise ValueError
        except ValueError as err:
            self.view.error("Incorrect Index '{}'".format(n))
        else:
            quote = self.model.get_quote(n)
            self.view.show(quote)


class QuoteTkinterView(Tkinter.Frame):
    
    def __init__(self, master=None, controller=None):
        Tkinter.Frame.__init__(self, master)
        # reference to the master widget, which is the tk window
        self.master = master 
        self.init_window()
        # so we may invoke methods of the controller
        self.controller = controller
    
    def init_window(self):
        
        # allowing the widget to take the full space of the root window
        self.pack(fill=Tkinter.BOTH, expand=1)

        # create an entry (for user input)
        self.inputEntry = Tkinter.Entry(self, width = 10)
        self.inputEntry.place(x=20, y=20)

        # create a button
        showButton = Tkinter.Button(self, text="Show", command=self.select_quote)
        showButton.place(x=20, y=50)

        # create a label (for quote output) 0 - anchor to the west (left)
        self.showLabel = Tkinter.Label(self, width=350, height=4, anchor='w')
        self.showLabel.place(x=20, y=80)
        
    def show(self, quote):
        self.showLabel['text'] = "And the quote is: '{}'".format(quote)
    
    def error(self, msg):
        self.showLabel['text'] = 'Error: {}'.format(msg)
    
    def select_quote(self):
        self.controller.process_input(self.inputEntry.get())

if __name__ == "__main__":
    
    # Select the controller
    valid_input = False
    
    while not valid_input:
        n = raw_input("Select the controller (1-GUI, 2-CLI): ") 
        try:
            n = int(n)
            if n not in [1, 2]:
                raise ValueError
        except ValueError as err:
            print("Incorrect Choice '{}'".format(n))
        else:
            valid_input = True
    
    if n == 1:
        controller = QuoteTkinterController()
    elif n == 2:
        controller = QuoteTerminalController()
    else:
        raise BaseException
    
    # while isn't necessary for GUI controller
    while True:      
        controller.run()
    
    
    