from collections import defaultdict

class DocumentStore:

    def __init__(self):
        self._documents = defaultdict(dict)

    def update(self, id_image: str, partial_doc: dict):
        self._documents[id_image].update(partial_doc)
        return self._documents[id_image]