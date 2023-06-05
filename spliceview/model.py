"""Specifies models to hold transcript-related information for all transcripts."""


class Model:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_csv(cls):
        pass

    @classmethod
    def from_kallisto(cls):
        pass

    @classmethod
    def from_salmon(cls):
        pass

    @staticmethod
    def yell():
        print('I AM A MODEL!!!!!!!!!!!')
