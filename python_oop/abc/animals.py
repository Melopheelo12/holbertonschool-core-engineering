#!/usr/bin/env python3
"""Module définissant une classe abstraite Animal et ses sous-classes."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Classe abstraite représentant un animal."""

    @abstractmethod
    def sound(self) -> str:
        """Retourne le son produit par l'animal."""
        raise NotImplementedError


class Dog(Animal):
    """Classe représentant un chien."""

    def sound(self) -> str:
        return "Bark"


class Cat(Animal):
    """Classe représentant un chat."""

    def sound(self) -> str:
        return "Meow"
