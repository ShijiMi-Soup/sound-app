import flet as _ft

from .. import components as _comp
from .. import model as _model


def get_audio_srcs():
    return [
        _model.AudioSource("夢", "https://amachamusic.chagasi.com/mp3/yume.mp3"),
        _model.AudioSource(
            "静止した宇宙",
            "https://amachamusic.chagasi.com/mp3/seishishitauchu.mp3",
        ),
        _model.AudioSource(
            "夏休みの探検",
            "https://amachamusic.chagasi.com/mp3/natsuyasuminotanken.mp3",
        ),
    ]


def get_audio_players(page: _ft.Page, srcs: list[_model.AudioSource]):
    return [_comp.AudioPlayer(page, src) for src in srcs]
