#!/usr/bin/env python3
"""Module définissant une classe Square avec property et setter."""


class Square:
    """Classe représentant un carré défini par sa taille."""

    def __init__(self, size=0):
        """Initialise un carré avec sa taille.

        Args:
            size: La taille du carré (entier positif ou nul, 0 par défaut).
        """
        self.__size = 0
        self.size = size

    @property
    def size(self):
        """Récupère la taille du carré.

        Returns:
            La taille actuelle du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Définit la taille du carré, après validation.

        Args:
            value: La nouvelle taille du carré.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est strictement négatif.
        """
        if type(value) is not int:
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Value must be > 0")
        self.__size = value

    def area(self):
        """Retourne l'aire du carré.

        Returns:
            L'aire du carré (size au carré).
        """
        return self.__size ** 2
