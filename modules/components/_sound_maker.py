import flet as ft
import numpy as np
import sounddevice as sd


class SoundMakerField:
    def __init__(self, value: float):
        self.value = value
        self.control = ft.TextField(f"{value}", on_change=self.on_change)

    def on_change(self, e):
        new_value = e.control.value
        try:
            self.value = float(new_value)
            self.control.value = str(new_value)
        except ValueError:
            pass
        self.control.update()


class SoundMakerFields:
    sample_rate = 44100

    # TODO: 周波数、長さ、音量
    def __init__(self):
        self.freq = SoundMakerField(440)
        self.duration = SoundMakerField(1)
        self.amp = SoundMakerField(0.5)

    @property
    def values(self):
        return [self.freq, self.duration, self.amp]

    @property
    def controls(self):
        return [val.control for val in self.values]

    @property
    def time(self):
        return np.linspace(
            0,
            self.duration.value,
            int(self.sample_rate * self.duration.value),
            endpoint=False,
        )

    @property
    def sound(self):
        return self.amp.value * np.sin(2 * np.pi * self.freq.value * self.time)

    def play(self):
        sd.play(self.sound, self.sample_rate)
        sd.wait()


class SoundMaker(ft.Column):
    def __init__(self):
        # テキストフィールドを追加
        self.fields = SoundMakerFields()
        self.button = ft.ElevatedButton("Play", on_click=self.on_click)

        # 親クラスのコンストラクタを呼び出す
        super().__init__(
            controls=[*self.fields.controls, self.button],
            alignment=ft.alignment.center,
            expand=True,
        )

    def on_click(self, e):
        self.fields.play()
