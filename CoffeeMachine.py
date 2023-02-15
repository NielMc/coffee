#write your code below


class CoffeeMachine:
    """
    A class describing a coffee machine

    Properties:
        water_level: int, max value 10, level of water in the tank
        beans_quantity: int, max value 10, quantity of beans in the hopper

    Methods:
        make_coffee: makes a cup of coffee  
        grind_beans: grinds beans
        pump_water: pumps water
        heat_water: heat water
        eject_grounds: ejects coffee grounds
    """
    def __init__(self):
        """Initialise the properties"""
        self._water_level = 10
        self._beans_quantity = 10

    @property
    def water_level(self):
        """ water_level getter """
        return self._water_level

    @water_level.setter
    def water_level(self, new_value):
        """
        water_level setter
        Args:
            new_value: int specifying the quantity

        Returns:
            None

        Raises:
            ValueError: if the value is more than 10
            ValueError: if the value is not an int        
        """
        if isinstance(new_value, int):
            if new_value > 10:
                raise ValueError("Value must be less than or equal to 10")
            else:
                self._water_level = new_value
        else:
            raise ValueError("New value must be an integer")

    @property
    def beans_quantity(self):
        """ beans_quantity getter """
        return self._beans_quantity

    @beans_quantity.setter
    def beans_quantity(self, new_value):
        """
        beans_quantity setter
        Args:
            new_value: int specifying the quantity

        Returns:
            None

        Raises:
            ValueError: if the value is more than 10
            ValueError: if the value is not an int        
        """
        if isinstance(new_value, int):
            if new_value > 10:
                raise ValueError("Value must be less than or equal to 10")
            else:
                self._beans_quantity = new_value
        else:
            raise ValueError("New value must be an integer")

    def _heat_water(self):
        """Heats water"""
        print("heat water")

    def _grind_beans(self):
        """ Grinds the beans """
        print("Grinding beans")

    def _pump_water(self):
        """ Pumps the hot water """
        print("Pumping water")

    def _eject_grounds(self):
        """ Ejects the waste grounds """
        print("Ejecting waste")

    def make_coffee(self):
        """makes coffee"""
        if self.beans_quantity >= 1:
            self._grind_beans()
        else:
            raise ValueError("add more beans")
        if self.water_level >= 1:
            self._heat_water()
        else:
            raise ValueError("add more water")
        self._pump_water()
        self._eject_grounds()
        print("coffee made")


# test code
# coffee_machine = CoffeeMachine()
# coffee_machine.make_coffee()


class PodCoffeeMachine(CoffeeMachine):
    """
    A class describing a pod coffee maker

    Properties:
        No new properties

    Methods:
    pierce_pod: pierces the foil
    eject_waste: eject a used pod
    """
    def __init__(self):
        """Initialise"""
        super().__init__()

    def _pierce_pod(self):
        """pierces pod"""
        print("pierce pod")

    def _eject_waste(self):
        """eject pod"""
        print("pod ejected")

    def make_coffee(self):
        """makes pod coffee"""
        self._heat_water()
        self._pierce_pod()
        self._pump_water()
        self._eject_waste()
        print("made nespresso")


pod_coffee = PodCoffeeMachine()
pod_coffee.make_coffee()


























    