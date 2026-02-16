import unittest

def count_long_names(prenoms):
    """
    Compte les prénoms ayant strictement plus de sept lettres.
    Cette fonction se concentre uniquement sur le calcul.
    """
    # Utilisation d'une liste en compréhension pour être plus "Pythonic" et lisible
    long_names = [prenom for prenom in prenoms if len(prenom) > 7]
    return len(long_names)

class TestNamesMethod(unittest.TestCase):
    def test_count_long_names(self):
        # Données de test
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        
        # Action
        resultat = count_long_names(prenoms)
        
        # Assertion (Le test doit être PASSANT : 4 prénoms > 7 lettres)
        # Guillaume (9), Juliette (8), François (8), Cassandre (9)
        self.assertEqual(resultat, 4)

if __name__ == '__main__':
    unittest.main()

