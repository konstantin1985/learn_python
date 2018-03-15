
# MAIN SOURCE:
# Kasampalis "Mastering Python Patterns" Chapter 8

# USEFUL LINKS:


# GENERAL INFORMATION:

# One of the design principles related to software engineering is the Separation
# of Concerns (SoC) principle. The idea behind the SoC principle is to split an
# application into distinct sections, where each section addresses a separate
# concern. Examples of such concerns are the layers used in a layered design
# (data access layer, business logic layer, presentation layer, and so forth). 

# The Model-View-Controller (MVC) pattern is nothing more than the SoC principle
# applied to OOP. The name of the pattern comes from the three main components
# used to split a software application: the model, the view, and the controller.
# MVC is considered an architectural pattern rather than a design pattern. The
# difference between an architectural and a design pattern is that the former
# has a broader scope than the latter. 

# The model is the core component. It represents knowledge. It contains and manages
# the (business) logic, data, state, and rules of an application. The view is a visual
# representation of the model. Examples of views are a computer GUI, the text output
# of a computer terminal, a smartphone's application GUI, a PDF document, a pie
# chart, and so forth. The view only displays the data, it doesn't handle it. The
# controller is the link/glue between the model and view. All communication between
# the model and the view happens through a controller.

# A typical use of an application that uses MVC after the initial screen is
# rendered to the user is as follows:
# - The user triggers a view by clicking (typing, touching, and so on) a button
# - The view informs the controller about the user's action
# - The controller processes user input and interacts with the model
# - The model performs all the necessary validation and state changes, and
#   informs the controller about what should be done
# - The controller instructs the view to update and display the output
#   appropriately, following the instructions given by the model

# You might be wondering why is the controller part necessary? Can't we just
# skip it? We could, but then we would lose a big benefit that MVC provides: the
# ability to use more than one view (even at the same time, if that's what we want)
# without modifying the model. To achieve decoupling between the model and
# its representation, every view typically needs its own controller. If the model
# communicated directly with a specific view, we wouldn't be able to use multiple
# views (or at least, not in a clean and modular way).

# Django is also an MVC framework, although it uses different naming conventions.
# The controller is called view, and the view is called template.

# Each part has clear roles and responsibilities. The model has access to the data
# and manages the state of the application. The view is a representation of the
# model. The view does not need to be graphical; textual output is also considered
# a totally fine view. The controller is the link between the model and view.
# Proper use of MVC guarantees that we end up with an application that is easy to
# maintain and extend.

# When using MVC, make sure that you creating smart models (core functionality),
# thin controllers (functionality required for the communication between the view
# and the controller), and dumb views (representation and minimal processing).


print("-" * 20 + "# 1 Use Cases" + "-" * 20)

# MVC provides the benefits:
# - The separation between the view and model allows graphics designers to
#   focus on the UI part and programmers to focus on development, without
#   interfering with each other.
# - Because of the loose coupling between the view and model, each part can be
#   modified/extended without affecting the other. For example, adding a new
#   view is trivial. Just implement a new controller for it.
# - Maintaining each part is easier because the responsibilities are clear.

# IMPORTANT:
# When implementing MVC from scratch, be sure that you create:
# - smart models, 
# - thin controllers, 
# - and dumb views 

# A model is considered smart because it:
# - Contains all the validation/business rules/logic
# - Handles the state of the application
# - Has access to application data (database, cloud, and so on)
# - Does not depend on the UI

# A controller is considered thin because it:
# - Updates the model when the user interacts with the view
# - Updates the view when the model changes
# - Processes the data before delivering it to the model/view, if necessary
# - Does not display the data
# - Does not access the application data directly
# - Does not contain validation/business rules/logic

# A view is considered dumb because it:
# - Displays the data
# - Allows the user to interact with it
# - Does only minimal processing, usually provided by a template language
#   (for example, using simple variables and loop controls)
# - Does not store any data
# - Does not access the application data directly
# - Does not contain validation/business rules/logic

# If you are implementing MVC from scratch and want to find out if you
# did it right, you can try answering two key questions:
# - If your application has a GUI, is it skinnable? How easily can you
#   change the skin/look and feel of it? Can you give the user the ability
#   to change the skin of your application during runtime? If this is not
#   simple, it means that something is going wrong with your MVC implementation.
# - If your application has no GUI (for instance, if it's a terminal application),
#   how hard is it to add GUI support? Or, if adding a GUI is irrelevant, is it easy
#   to add views to display the results in a chart (pie chart, bar chart, and so on)
#   or a document (PDF, spreadsheet, and so on)? If these changes are not trivial
#   (a matter of creating a new controller with a view attached to it, without
#   modifying the model), MVC is not implemented properly.


print("-" * 20 + "# 2 Implementation" + "-" * 20)

# The user enters a number and sees the quote related to that number. The
# quotes are stored in a quotes tuple. This is the data that normally exists in
# a database, file, and so on, and only the model has direct access to it.


quotes = ('A man is not complete until he is married. Then he isfinished.', 
          'As I said before, I never repeat myself.',
          'Behind a successful man is an exhausted woman.',
          'Black holes really suck...', 
          'Facts are stubborn things.')

class QuoteModel:
    
    def get_quote(self, n):
        try:
            # Negative values like -2 are accepted here, because of the
            # indexing. It's not very correct.
            value = quotes[n]  
        except IndexError as err:
            value = 'Not found!'
        return value
        
# The view has three methods: show(), which is used to print a quote (or
# the message Not found!) on the screen, error(), which is used to print
# an error message on the screen, and select_quote(), which reads the
# user's selection.

class QuoteTerminalView:
    
    def show(self, quote):
        print("And the quote is: '{}'".format(quote))
    
    def error(self, msg):
        print('Error: {}'.format(msg))
    
    def select_quote(self):
        return raw_input('Which quote number you like to see? ')


# The controller does the coordination. The __init__() method initializes
# the model and view. The run() method validates the quote index given by
# the user, gets the quote by the model, and passes it back to the view
# to be displayed.

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
        
if __name__ == "__main__":
    main()

