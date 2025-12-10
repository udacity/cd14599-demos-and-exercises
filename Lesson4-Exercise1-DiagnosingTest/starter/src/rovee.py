class Rover:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.orientation = 'NORTH'
        self._compass = ['NORTH', 'EAST', 'SOUTH', 'WEST']

    def turn_right(self):
        """Rotates the rover 90 degrees clockwise."""
        current_idx = self._compass.index(self.orientation)
        self.orientation = self._compass[(current_idx + 1) % 4]

    def move(self, direction, distance):
        if direction == 'NORTH':
            self.y += distance
        elif direction == 'SOUTH':
            self.y -= distance
        elif direction == 'EAST':
            self.x += distance
        elif direction == 'WEST':
            self.x -= distance

    def execute_sequence(self, commands):
        for command in commands:
            parts = command.split()
            action = parts[0]

            if action == 'MOVE':
                direction = parts[1]
                distance = int(parts[2])
                self.move(direction, distance)
            # BUG: Logic for 'TURN' is missing here!
            elif action == 'TURN':
                if parts[1] == 'RIGHT':
                    self.turn_right()
