import flet as ft

from .. import components as _components
from .. import controller as _controller

TITLE = "Takahiro App"
WIN_WIDTH = 400
WIN_HEIGHT = 600


class MainView:
    def __init__(self):
        ft.app(self.start_app)

    def start_app(self, page: ft.Page):
        page.title = TITLE
        page.window_width = WIN_WIDTH
        page.window_height = WIN_HEIGHT

        srcs = _controller.get_audio_srcs()

        audio_players = [_components.AudioPlayer(page, src) for src in srcs]
        sound_maker = _components.SoundMaker()

        page.add(
            ft.Container(
                content=ft.Column(
                    [
                        *audio_players,
                        sound_maker,
                    ],
                    expand=True,
                    alignment=ft.alignment.center,
                ),
                expand=True,
            )
        )
