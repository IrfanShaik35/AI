import random

class VacuumCleaner:
    def __init__(self):
        self.location = random.choice(['A', 'B'])  # Start location: randomly choose A or B
        self.status = {'A': random.choice(['Dirty', 'Clean']), 'B': random.choice(['Dirty', 'Clean'])}

    def sense(self):
        return self.status[self.location]

    def clean(self):
        print(f"Vacuum cleaner is cleaning {self.location}")
        self.status[self.location] = 'Clean'

    def move(self):
        print(f"Moving vacuum cleaner from {self.location}... ", end='')
        if self.location == 'A':
            self.location = 'B'
        else:
            self.location = 'A'
        print(f"to {self.location}")

# Main function to simulate the vacuum cleaner operation
def clean_room(vacuum, steps):
    for step in range(steps):
        print(f"\nStep {step + 1}:")
        current_location = vacuum.location
        print(f"Current location: {current_location}, Status: {vacuum.sense()}")
        
        if vacuum.sense() == 'Dirty':
            vacuum.clean()
        else:
            print("No action needed.")
        
        vacuum.move()

# Create a VacuumCleaner object and clean the room
vacuum = VacuumCleaner()
clean_room(vacuum, 5)  # Clean the room in 5 steps
