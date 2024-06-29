import flet as ft

from .. import model as _model


class AudioPlayer(ft.Row):
    _is_playing = False

    def __init__(self, page: ft.Page, src: _model.AudioSource, btn_text: str = "Play"):
        # コントロールの作成
        self.text = ft.Text(src)
        self.button = ft.ElevatedButton(btn_text, on_click=self.on_click)

        # Audioを追加
        self.audio = ft.Audio(src=src)
        page.overlay.append(self.audio)

        # 親クラスのコンストラクタを呼び出す
        super().__init__([self.text, self.button])

    def on_click(self, e):
        if self._is_playing:
            self._is_playing = False
            self.audio.pause()
            self.button.text = "Play"
        else:
            self._is_playing = True
            self.audio.resume()
            self.button.text = "Pause"
        self.button.update()
