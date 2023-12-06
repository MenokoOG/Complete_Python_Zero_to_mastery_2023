"gun project, Menoko OG, 11/2023"
class Gun:
    """
    Class representing a Gun.

    Attributes:
    - name: str
        The name of the gun.
    - caliber: str
        The caliber of the gun.
    - ammunition: int
        The number of ammunition the gun has.

    Methods:
    - __init__(name: str, caliber: str, ammunition: int)
        Constructor to instantiate the Gun class.
    - shoot()
        Method to simulate shooting the gun.
    - reload(ammunition: int)
        Method to reload the gun with ammunition.
    """

    def __init__(self, name: str, caliber: str, ammunition: int):
        """
        Constructor to instantiate the Gun class.

        Parameters:
        - name: str
            The name of the gun.
        - caliber: str
            The caliber of the gun.
        - ammunition: int
            The number of ammunition the gun has.
        """
        self.name = name
        self.caliber = caliber
        self.ammunition = ammunition

    def shoot(self):
        """
        Method to simulate shooting the gun.

        Returns:
        - str:
            A message indicating the gun has been shot.
        """
        if self.ammunition > 0:
            self.ammunition -= 1
            return f"The {self.name} has been shot!"
        else:
            return f"The {self.name} is out of ammunition."

    def reload(self, ammunition: int):
        """
        Method to reload the gun with ammunition.

        Parameters:
        - ammunition: int
            The number of ammunition to reload.
        """
        self.ammunition += ammunition

# Unit tests for Gun class.

import unittest

class TestGun(unittest.TestCase):

    # Setup method to instantiate the object before each test.
    def setUp(self):
        self.gun = Gun("Pistol", "9mm", 10)

    # Tests for __init__
    def test_gun_attributes(self):
        """
        Tests if gun attributes are correctly set during initialization.
        """
        self.assertEqual(self.gun.name, "Pistol")
        self.assertEqual(self.gun.caliber, "9mm")
        self.assertEqual(self.gun.ammunition, 10)

    # Tests for shoot
    def test_shoot_with_ammunition(self):
        """
        Tests shooting the gun when it has ammunition.
        """
        self.assertEqual(self.gun.shoot(), "The Pistol has been shot!")
        self.assertEqual(self.gun.ammunition, 9)

    def test_shoot_without_ammunition(self):
        """
        Tests shooting the gun when it is out of ammunition.
        """
        self.gun.ammunition = 0
        self.assertEqual(self.gun.shoot(), "The Pistol is out of ammunition.")
        self.assertEqual(self.gun.ammunition, 0)

    # Tests for reload
    def test_reload_ammunition(self):
        """
        Tests reloading the gun with ammunition.
        """
        self.gun.reload(5)
        self.assertEqual(self.gun.ammunition, 15)

# Example of using the Gun class:

# Example 1: Creating and using a gun
gun = Gun("Shotgun", "12 gauge", 6)
print(f"Gun: {gun.name}, Caliber: {gun.caliber}, Ammunition: {gun.ammunition}")

print(gun.shoot())  # Shoot the gun
print(f"Ammunition left: {gun.ammunition}")

gun.reload(4)  # Reload the gun
print(f"Ammunition after reloading: {gun.ammunition}")