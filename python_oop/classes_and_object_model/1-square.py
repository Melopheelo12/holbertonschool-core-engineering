#!/usr/bin/env python3
"""Module définissant une classe Square avec un attribut privé size."""


class Square:
    """Classe représentant un carré défini par sa taille."""

    def __init__(self, size):
        """Initialise un carré avec sa taille.

        Args:
            size: La taille du carré.
        """
        self.__size = size
