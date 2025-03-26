import flet as ft
import vlc
import todo
from tinytag import TinyTag
from tinytag import Image as TTimage
from PIL import Image
import io


def add_clicked(e):
    todo.MusicPlay()

def main(page):
    page.title = "Card Example"
    page.add(
        ft.Card(

            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.ALBUM),
                            title=ft.Text("The Enchanted Nightingale"),
                            subtitle=ft.Text(
                                "Music by Julie Gable. Lyrics by Sidney Stein."
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("Buy tickets", on_click=add_clicked ), ft.TextButton("Listen")],
                            alignment=ft.MainAxisAlignment.END,

                        ),
                    ]

                ),

        )
    )
)

    page.add
ft.app(main)