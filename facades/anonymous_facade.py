from .facade_base import FacadeBase


class AnonymousFacade(FacadeBase):
    def __init__(self):
        super().__init__()


    def login(self, username, password):
        pass


    def add_customer(self):
        pass