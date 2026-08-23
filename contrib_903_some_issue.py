"""Some Issue (fix for issue #903)"""

import random

class RandomCatFacts:
    """A simple provider of random cat facts."""

    def __init__(self, facts=None):
        # Default list of cat facts; can be overridden for testing.
        self.facts = facts or [
            "Cats are the Bees knees.",
            "A group of cats is called a clowder.",
            "Cats have five toes on their front paws and four on their back paws.",
            "The technical term for a cat's hairball is a 'bezoar'.",
            "Cats can make over 100 different vocal sounds, while dogs can make about 10.",
            "A cat's whiskers are sensitive to air currents and help them navigate."
        ]

    def get_random_fact(self):
        """Return a random cat fact."""
        if not self.facts:
            raise ValueError("No cat facts available.")
        return random.choice(self.facts)

    def add_fact(self, fact):
        """Add a new cat fact."""
        self.facts.append(fact)

    def get_all_facts(self):
        """Return a copy of the list of all cat facts."""
        return list(self.facts)

