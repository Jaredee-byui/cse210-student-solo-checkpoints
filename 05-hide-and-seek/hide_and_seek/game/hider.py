import random

# TODO: Define the Hider class here
class Hider:

    def __init__(self):
        self.location = random.randint(1,1000)
        self.distance = [0, 0]

    def watch(self, location):
        distance = abs(self.location - location)
        self.distance.append(distance)

    def get_hint(self):
        hint = "(-.-) Maybe I'll take a nap. "
        if self.distance[-1] == 0:
            hint = "(0_0) you found me! "
        elif self.distance[-1] > self.distance[-2]:
            hint = "(^.^) Getting colder!"
        elif self.distance[-1] < self.distance[-2]:
            hint = "(>_<) Getting Warmer!"
        return hint

    