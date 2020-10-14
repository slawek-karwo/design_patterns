from abc import ABC, abstractmethod
import pandas as pd


class Context:
    """
    This is the main class to do the final job
    """

    def __init__(self, strategy_interface):
        self._strategy = strategy_interface

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy_interface):
        self._strategy = strategy_interface

    def return_players_average_height(self):
        data = self._strategy.filter_logic()
        print(data['Height'].mean())


class StrategyInterface(ABC):
    """
    Interface (abstract class) to store methods to be run by Context
    """

    def __init__(self, data):
        self.data = data

    @abstractmethod
    def filter_logic(self):
        pass


class FilterGoalkeepers(StrategyInterface):
    """
    First logic of filter_logic - take only Goalkeepers
    """

    def filter_logic(self):
        filtered_data = self.data[self.data['Position'] == 'Goalkeeper']
        print('Filtering only Goalkeepers!')
        return filtered_data


class FilterWingers(StrategyInterface):
    """
    Second logic of filter_logic - take only Wingers
    """

    def filter_logic(self):
        filtered_data = self.data[self.data['Position'] == 'Winger']
        print('Filtering only Wingers!')
        return filtered_data


if __name__ == '__main__':
    df = pd.read_excel('players.xlsx')
    main_app = Context(FilterGoalkeepers(df))
    print(main_app.strategy)
    main_app.return_players_average_height()
    main_app.strategy = FilterWingers(df)
    print(main_app.strategy)
    main_app.return_players_average_height()
