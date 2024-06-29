import flet as ft

from .. import model as _model


class AudioPlayer(ft.Row):
    _is_playing = False
    _icon_play = "play_arrow"
    _icon_pause = "pause"

    def __init__(self, page: ft.Page, src: _model.AudioSource, btn_text: str = "Play"):
        # コントロールの作成
        self.text = ft.Text(src.name, expand=True)
        # self.button = ft.ElevatedButton(btn_text, on_click=self.on_click)
        self.button = ft.IconButton(self._icon_play, on_click=self.on_click)

        # Audioを追加
        self.audio = ft.Audio(src=src)
        page.overlay.append(self.audio)

        # 親クラスのコンストラクタを呼び出す
        super().__init__([self.text, self.button])

    def on_click(self, e):
        if self._is_playing:
            self._is_playing = False
            self.audio.pause()
            self.button.icon = self._icon_play
        else:
            self._is_playing = True
            self.audio.resume()
            self.button.icon = self._icon_pause
        self.button.update()
