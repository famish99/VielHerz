"""
Card Catalog module
"""
from game.models.card import CardCatalog, Card


class TantoCardCatalog(CardCatalog):
    """
    Tanto specific Card Catalog stuff
    """

    #def __init__(self, *args, **kwargs):
    #    super(TantoCardCatalog, self).__init__(*args, **kwargs)

    def load_catalog(self, card_module):
        """
        Load cards from module into database
        """
        from card_module import CARD_LIST
        
        for card in CARD_LIST:
            pass

