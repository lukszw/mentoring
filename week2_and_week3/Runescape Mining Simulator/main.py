# Rock: (lvl, exp)
ROCKS = {'Clay': (1, 801), 'Copper': (1, 17.5), 'Tin': (1, 17.5), 'Iron': (15, 35), 'Silver': (20, 40), 'Coal': (30, 50), 'Gold': (40, 65)}

# LVL: EXP
EXPERIENCE = {1: 0, 2: 83, 3: 174, 4: 276, 5: 388, 6: 512, 7: 650, 8: 801, 9: 969, 10: 1154, 11: 1358, 12: 1584, 13: 1833, 14: 2107, 15: 2411, 16: 2746, 17: 3115, 18: 3523, 19: 3973, 20: 4470, 21: 5018, 22: 5624, 23: 6291, 24: 7028, 25: 7842, 26: 8740, 27: 9730, 28: 10824, 29: 12031, 30: 13363, 31: 14833, 32: 16456, 33: 18247, 34: 20224, 35: 22406, 36: 24815, 37: 27473, 38: 30408, 39: 33648, 40: 37224}


class Miner:
    """
    Miner class
    Attribues:
    - xp: experience
    - level: level of the Miner

    Methods:
    - mine("rock_name")
    """
    def __init__(self, xp: int =0) -> None:
        self._xp = xp
        self._level = next(i for i in range(40, 0, -1) if xp >= EXPERIENCE[i])

    def mine(self, rock: str) -> str:
        if self._level >= ROCKS[rock][0]:
            self._xp += ROCKS[rock][1]
            if self._level < 40 and self._xp >= EXPERIENCE[self._level+1]:
                self._level += 1
                return f"Congratulations, you just advanced a Mining level! Your mining level is now {self._level}."
            return f"You swing your pick at the rock."
        return f"You need a mining level of {ROCKS[rock][0]} to mine {rock}."


