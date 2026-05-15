#!/usr/bin/env python3
"""Module définissant une classe Rectangle avec validation des dimensions."""


class Rectangle:
    """Classe représentant un rectangle défini par sa largeur et sa hauteur."""

    def __init__(self, width=0, height=0):
        """Initialise un rectangle avec sa largeur et sa hauteur.

        Args:
            width: La largeur du rectangle (entier positif ou nul, 0 par défaut).
            height: La hauteur du rectangle (entier positif ou nul, 0 par défaut).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Récupère la largeur du rectangle.

        Returns:
            La largeur actuelle du rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur du rectangle, après validation.

        Args:
            value: La nouvelle largeur.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est strictement négatif.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur du rectangle.

        Returns:
            La hauteur actuelle du rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Définit la hauteur du rectangle, après validation.

        Args:
            value: La nouvelle hauteur.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est strictement négatif.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
