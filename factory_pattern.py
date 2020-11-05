from abc import ABC, abstractmethod


class Player(ABC):

    @abstractmethod
    def players_stats(self):
        raise NotImplementedError


class Goalkeeper(Player):

    def players_stats(self):
        return f"Goalkeeper stats are catching and reflex."


class Playmaker(Player):

    def players_stats(self):
        return f"Playmaker stats are speed and strength."


class PlayerFactory:

    positions = dict(Goalkeeper=Goalkeeper(),
                     Playmaker=Playmaker())

    def create_player(self, position):
        return self.positions[position]


if __name__ == '__main__':
    pos = input("Enter the position to get parameters: ")
    print(PlayerFactory().create_player(pos).players_stats())
