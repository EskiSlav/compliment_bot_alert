from __future__ import annotations

from .translate import Translator


class Compliment():
    _translator = Translator()

    def __init__(self, compliment: str, compliment_ua='', usage_number=0) -> None:
        self.compliment = compliment
        self.compliment_ua = compliment_ua
        self.usage_number = usage_number

    def __str__(self) -> str:
        _str = f'<{self.compliment} -> {self.compliment_ua}' + \
               f' | Usage: {self.usage_number}>'
        return _str


class NewCompliment(Compliment):
    def __init__(self, compliment) -> None:
        self.compliment = compliment
        self.usage_number = 0

    @property
    def compliment_ua(self):
        return Compliment._translator.translate_text(self.compliment)

    def __str__(self) -> str:
        return super().__str__()
