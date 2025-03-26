import flet as ft
from tinytag import TinyTag
# importing vlc module
import vlc


def MusicPlay():
    media = vlc.MediaPlayer("./Music/MCLS.mp3")
    media.play()