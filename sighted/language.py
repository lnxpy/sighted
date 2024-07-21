import os
from enum import StrEnum, auto
from typing import List, Self

import spacy

from sighted.parts_of_speech import (
    Adjective,
    Adposition,
    Adverb,
    Auxiliary,
    Conjunction,
    CoordinatingConjunction,
    Determiner,
    EndofLine,
    Interjection,
    Noun,
    Numeral,
    Other,
    Particle,
    Pronoun,
    ProperNoun,
    Punctuation,
    SubordinatingConjunction,
    Symbol,
    Verb,
    WhiteSpace,
)

BASE_URL = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_URL, "en_core_web_sm")


class PoS(StrEnum):
    ADJ: Adjective = auto()
    ADP: Adposition = auto()
    ADV: Adverb = auto()
    AUX: Auxiliary = auto()
    CONJ: Conjunction = auto()
    CCONJ: CoordinatingConjunction = auto()
    DET: Determiner = auto()
    INTJ: Interjection = auto()
    NOUN: Noun = auto()
    NUM: Numeral = auto()
    PART: Particle = auto()
    PRON: Pronoun = auto()
    PROPN: ProperNoun = auto()
    PUNCT: Punctuation = auto()
    SCONJ: SubordinatingConjunction = auto()
    SYM: Symbol = auto()
    VERB: Verb = auto()
    X: Other = auto()
    EOL: EndofLine = auto()
    SPACE: WhiteSpace = auto()


class Language:
    def __init__(
        self: Self,
        text: str,
        ignore_pos: List[PoS] = [],
        fixation: int = 2,
        saccade: int = 0,
    ) -> None:
        """initializer

        Args:
            self (Self): self
            text (str): given text
            ignore_pos (List[PoS], optional): ignored parts of speech. Defaults to [].
            fixation (int, optional): fixation. Defaults to 2.
            saccade (int, optional): saccade. Defaults to 0.
        """
        self.text = text
        self._ignore_pos = ignore_pos
        self.fixation = fixation
        self.saccade = saccade

        self.processor = spacy.load(MODEL_PATH)

    @property
    def ignore_pos(self: Self) -> List[str]:
        return [pos.value.upper() for pos in self._ignore_pos]

    @property
    def fixation(self: Self):
        return self._fixation

    @fixation.setter
    def fixation(self: Self, value: int):
        if value in range(1, 6):
            self._fixation = value
        else:
            raise ValueError("Fixation has to be between 1 and 5.")

    @property
    def saccade(self: Self):
        return self._saccade

    @saccade.setter
    def saccade(self: Self, value: int):
        if value in range(0, 4):
            self._saccade = value
        else:
            raise ValueError("Saccade has to be between 1 and 3.")
