

from tkinter import *
from PIL import Image, ImageSequence, ImageTk


""" From http://stackoverflow.com/questions/28531415/tkinter-animation-will-not-work """

class AnimatedGif(object):
    """ Animated GIF Image Container. """
    def __init__(self, image_file_path):
        self.image_file_path = image_file_path
        self._load()

    def __len__(self):
        return len(self._frames)

    def __getitem__(self, frame_num):
        return self._frames[frame_num]

    def _load(self):
        """ Read in all the frames of a gif image. """
        self._frames = []
        img = Image.open(self.image_file_path)
        for frame in ImageSequence.Iterator(img):
            photo = ImageTk.PhotoImage(frame)
            photo.delay = frame.info['duration'] * 2  # add attribute
            self._frames.append(photo)

def update_label_image(label, anigif, frame_num):
    """ Change label image to given frame number of AnimatedGif. """
    global cancel_id
    frame = anigif[frame_num]
    label.configure(image=frame)
    frame_num = (frame_num+1) % len(anigif)  # next frame number
    cancel_id = root.after(
                    frame.delay, update_label_image, label, anigif, frame_num)

def enable_animation():
    """ Start animation of label image. """
    global cancel_id
    cancel_id = root.after(
                    anigif[0].delay, update_label_image, label, anigif, 0)

def cancel_animation():
    """ Stop animation of label image. """
    global cancel_id
    if cancel_id is not None:
        root.after_cancel(cancel_id)
        cancel_id = None

if __name__ == '__main__':
    cancel_id = None
    root = Tk()
    root.title('Animation Demo2')

    image_file_path = 'pictures/box_136px.gif'
    anigif = AnimatedGif(image_file_path)

    label = Label(image=anigif[0])  # display first frame initially
    label.pack()
    start_animation = Button(root, text="start animation", command=enable_animation)
    start_animation.pack()
    stop_animation = Button(root, text="stop animation", command=cancel_animation)
    stop_animation.pack()
    exit_program = Button(root, text="exit", command=root.quit)
    exit_program.pack()

    root.geometry("250x250+100+100")
    root.mainloop()