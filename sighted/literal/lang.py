from string import Template

from typing import Iterable
from sighted.language import Language
from sighted.literal.algo import bolded_letters


class Literal(Language):
    def transform(self, template: Template) -> Iterable[str]:
        """transforms the given text into the shape of `template`

        Args:
            template (Template): template (Template): template for bolded literals.

        Returns:
            Iterable[str]: list of words put into `template`.

        Yields:
            Iterator[Iterable[str]]: each serialized word from the given text.
        """

        result = self.processor(self.text)

        for literal in result:
            word, pos, dep = literal.text, literal.pos_, literal.dep_
            bolding_length = bolded_letters(len(word), self.fixation)

            if pos in self.ignore_pos:
                yield word
            else:
                yield template.safe_substitute(
                    pos=pos.lower(),
                    dep=dep,
                    fix=word[0:bolding_length],
                    unfix=word[bolding_length : len(word)],
                )
