"""Describes gene, transcript, and protein objects."""


class Gene:
    def __init__(self, name: str):
        self.name = name


class Transcript:
    def __init__(self, name: str, parent_gene: Gene):
        self.name = name
        self.parent_gene = parent_gene


class Protein:
    def __init(self, name: str, parent_trs: Transcript):
        self.name = name
        self.parent_trs = parent_trs
