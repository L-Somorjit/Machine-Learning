# Import everything needed to edit video clips
from moviepy.editor import *
	
# loading video dsa gfg intro video
clip = VideoFileClip("ply.mp4")
	
# getting only first 5 seconds
# clip1 = clip.subclip(37859, 37867)

# clip1.write_videofile("1.mp4")

clip2 = clip.subclip(6, 8)

clip2.write_videofile("ply.mp4")

# clip3 = clip.subclip(300, 315)

# clip3.write_videofile("3.mp4")

# clip4 = clip.subclip(500, 515)

# clip4.write_videofile("4.mp4")

# clip5 = clip.subclip(600, 615)

# clip5.write_videofile("5.mp4")
# cutting out some part from the clip
# clip = clip.cutout(3, 10)

# showing clip
# clip.ipython_display(width = 360)
