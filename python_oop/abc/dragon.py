#!/usr/bin/env python3
"""Module démontrant l'utilisation des mixins avec la classe Dragon."""


class SwimMixin:
    """Mixin ajoutant la capacité de nager."""

    def swim(self):
        """Affiche que la créature nage."""
        print("The creature swims!")


class FlyMixin:
    """Mixin ajoutant la capacité de voler."""

    def fly(self):
        """Affiche que la créature vole."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Classe Dragon combinant les capacités de nager et de voler."""

    def roar(self):
        """Affiche que le dragon rugit."""
        print("The dragon roars!")
