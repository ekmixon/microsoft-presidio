from typing import Iterable, Iterator, Tuple

from presidio_analyzer.nlp_engine import NlpEngine, NlpArtifacts


class NlpEngineMock(NlpEngine):
    def __init__(self, stopwords=None, punct_words=None, nlp_artifacts=None):
        self.stopwords = stopwords or []
        self.punct_words = punct_words or []
        if nlp_artifacts is None:
            self.nlp_artifacts = NlpArtifacts([], [], [], [], None, "en")
        else:
            self.nlp_artifacts = nlp_artifacts

    def is_stopword(self, word, language):
        return word in self.stopwords

    def is_punct(self, word, language):
        return word in self.punct_words

    def process_text(self, text, language):
        return self.nlp_artifacts

    def process_batch(
        self, texts: Iterable[str], language: str, **kwargs
    ) -> Iterator[Tuple[str, NlpArtifacts]]:
        texts = list(texts)
        for text in texts:
            yield (text, self.nlp_artifacts)
