from string import Template

from typing import Iterable
from sighted.language import Language
from sighted.literal.algo import bolded_letters


class Literal(Language):
    def transform(
        self, template: Template, ignored_pos_template: Template = None
    ) -> Iterable[str]:
        """transformer method

        Args:
            template (Template): template for bolded literals.
            ignored_pos_template (Template): template for the ignored parts of speech.
        """

        result = self.processor(self.text)

        for literal in result:
            word, pos = literal.text, literal.pos_
            bolding_length = bolded_letters(len(word), self.fixation)
            if pos in self.ignore_pos:
                yield ignored_pos_template.safe_substitute(id=pos.lower(), text=word)
            else:
                yield template.safe_substitute(
                    id=pos.lower(),
                    bold=word[0:bolding_length],
                    unbold=word[bolding_length : len(word)],
                )
