class ComponentPlayer():

    """
    Interface - Component for defining operation method which can be modified by decorator.
    """

    def operation(self):
        raise NotImplementedError


class PlayerAtk(ComponentPlayer):

    """
    Concrete Component to represent some object - in this case Player stats in Attack
    """

    def operation(self):
        return "Player stats:"


class DecorateComponentPlayer(ComponentPlayer):

    """
    Base for all concrete decorators - which will be decorate Component Player class
    """

    _player_component = None

    def __init__(self, player_component):
        self._player_component = player_component

    def operation(self):
        return self._player_component.operation()


class AddGoals(DecorateComponentPlayer):

    """
    Concrete decorator to add/change operation method (decorate) base on their needs
    """

    _goals = 7

    def operation(self):
        return f"{self._player_component.operation()} scored {self._goals} goals"


class AddAssist(DecorateComponentPlayer):
    """
    Concrete decorator to add/change operation method (decorate) base on their needs
    """

    _assist = 11

    def operation(self):
        return f"{self._player_component.operation()} assisted {self._assist} times"


if __name__ == '__main__':
    player_1 = PlayerAtk()
    print(player_1.operation())
    print(AddGoals(player_1).operation())
    print(AddAssist(player_1).operation())
    print(AddGoals(AddAssist(player_1)).operation())

    access = False
    # access = True

# decorate function

    def player_info(func):
        def inner():
            print(f"Check accesses, configuration...")
            if access:
                print(f"OK.")
                print(f"Player Name ")
                func()
            else:
                print(f"Accesses error!")

        return inner


    @player_info
    def add_age():
        print("25 years old.")


    add_age()
