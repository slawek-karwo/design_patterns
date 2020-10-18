from abc import ABC, abstractmethod


class Subject(ABC):
    """
    Abstract interface for all observed objects
    """

    @abstractmethod
    def attach(self, observer):
        raise NotImplementedError

    @abstractmethod
    def detach(self, observer):
        raise NotImplementedError

    @abstractmethod
    def update(self, add_value):
        raise NotImplementedError


class Balance(Subject):

    _subscribers = []
    _actual_balance = 0

    def attach(self, observer):
        self._subscribers.append(observer)

    def detach(self, observer):
        self._subscribers.remove(observer)

    def update(self, add_value):
        self._actual_balance = self._actual_balance + add_value
        for sub in self._subscribers:
            sub.update(self._actual_balance)


class Observer(ABC):
    """
    Abstract interface for all observers
    """

    @abstractmethod
    def update(self, new_balance):
        raise NotImplementedError


class Reserve(Observer):

    _balance = None

    def update(self, new_balance):
        print(f'New reserve is {new_balance*0.1}')
        self._balance = new_balance*0.1


class Invest(Observer):

    _to_invest = None

    def update(self, new_balance):
        print(f'New invest amount is {new_balance*0.2}')
        self._to_invest = new_balance*0.2


