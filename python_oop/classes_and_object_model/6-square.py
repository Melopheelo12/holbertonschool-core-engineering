#!/usr/bin/env python3
"""Module définissant une classe Square avec taille, position et affichage."""


class Square:
    """Classe représentant un carré défini par sa taille et sa position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise un carré avec sa taille et sa position.

        Args:
            size: La taille du carré (entier positif ou nul, 0 par défaut).
            position: Tuple de 2 entiers positifs représentant le décalage
                horizontal et vertical pour l'affichage (par défaut (0, 0)).
        """
        self.size = size
        self.position = position

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
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Récupère la position du carré.

        Returns:
            Le tuple (x, y) représentant la position actuelle.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Définit la position du carré, après validation.

        Args:
            value: Tuple de 2 entiers positifs ou nuls.

        Raises:
            TypeError: Si value n'est pas un tuple de 2 entiers positifs.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Retourne l'aire du carré.

        Returns:
            L'aire du carré (size au carré).
        """
        return self.__size ** 2

    def my_print(self):
        """Affiche le carré avec des '#' en tenant compte de la position.

        Si size vaut 0, affiche simplement une ligne vide.
        Sinon, affiche position[1] lignes vides au-dessus, puis size lignes
        composées de position[0] underscores suivis de size '#'.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print("_" * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Retourne la représentation en chaîne du carré.

        Returns:
            Une chaîne vide si size vaut 0, sinon les lignes formant
            le carré avec sa position.
        """
        if self.__size == 0:
            return ""
        lines = []
        for _ in range(self.__position[1]):
            lines.append("")
        for _ in range(self.__size):
            lines.append("_" * self.__position[0] + "#" * self.__size)
        return "\n".join(lines)
