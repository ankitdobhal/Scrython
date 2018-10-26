from .catalogs_object import CatalogsObject

class CardNames(CatalogsObject):
    """
    catalogs/card-names

    Catalog object for all known card names.

    Args:
        N/A

    Returns:
        N/A

    Raises:
        N/A

    Examples:
        >>> catalog = scrython.catalog.CardNames()
        >>> catalog.data()
    """
    def __init__(self):
        self._url = 'catalog/card-names?'
        super(CardNames, self).__init__(self._url)
