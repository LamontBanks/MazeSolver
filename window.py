from tkinter import Tk, BOTH, Canvas

class Window():
    """
        width, height - size of window in pixels
    """
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = 'Maze Solver'

        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack()
        self.__window_is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__window_is_running = True
        while self.__window_is_running:
            self.redraw()

    def close(self):
        self.__window_is_running = False
        

