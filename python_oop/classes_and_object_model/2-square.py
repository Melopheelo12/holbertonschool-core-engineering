#!/usr/bin/env python3
"""Module définissant une classe Square avec validation de size."""


class Square:
    """Classe représentant un carré défini par sa taille."""

    def __init__(self, size=0):
        """Initialise un carré avec sa taille, après validation.

        Args:
            size: La taille du carré (entier positif ou nul, 0 par défaut).

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est strictement négatif.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
