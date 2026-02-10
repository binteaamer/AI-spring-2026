#task1
class TrafficLightAgent:
    def act(self, traffic):
        if traffic == "Heavy Traffic":
            return "Extend Green Time"
        else:
            return "Normal Green"


agent = TrafficLightAgent()

print("Percept: Heavy Traffic → Action:", agent.act("Heavy Traffic"))
print("Percept: Light Traffic → Action:", agent.act("Light Traffic"))


#task2 
class ClassroomAgent:
    def __init__(self):
        self.model = {
            "students_present": None,
            "light_status": "OFF"
        }

    def act(self, students_present):
        self.model["students_present"] = students_present

        if students_present and self.model["light_status"] == "OFF":
            self.model["light_status"] = "ON"
            action = "Turn Lights ON"

        elif not students_present and self.model["light_status"] == "ON":
            self.model["light_status"] = "OFF"
            action = "Turn Lights OFF"

        else:
            action = "No Action"

        return action

presence_list = [True, True, False, False, True, False, True, False]

agent = ClassroomAgent()

print("Agent: Abeeha\n")

step = 1
for presence in presence_list:
    action = agent.act(presence)

    print("Step", step)
    print("Students Present:", presence)
    print("Action:", action)
    print("Model:", agent.model)
    print("-" * 30)

    step += 1

#task3 
class StudyPlannerAgent:
    def __init__(self):
        self.subjects = ["AI", "Math", "Physics"]

    def study(self):
        for subject in self.subjects:
            print("Studying", subject)
        print("Goal Achieved: All subjects completed")


agent = StudyPlannerAgent()
print("Student: Laiba\n")
agent.study()


#task4 
restaurants = {
    "A": {"distance": 3, "rating": 7},
    "B": {"distance": 5, "rating": 9}
}

utilities = {}

for r in restaurants:
    utility = restaurants[r]["rating"] - restaurants[r]["distance"]
    utilities[r] = utility
    print(f"Restaurant {r} Utility = {utility}")

selected = max(utilities, key=utilities.get)
print("\nSelected Restaurant:", selected)

#task 5 
class LearningAgent:
    def __init__(self):
        self.Q = {"Play": 0, "Rest": 0}

    def update_Q(self, action, reward):
        self.Q[action] += reward


agent = LearningAgent()

# Fixed actions for 10 steps
actions = ["Play", "Play", "Rest", "Play", "Play",
           "Rest", "Play", "Play", "Rest", "Play"]

print("Agent: Aamna\n")

step = 1
for action in actions:
    if action == "Play":
        reward = 5
    else:
        reward = 1

    agent.update_Q(action, reward)
    print(f"Step {step}: Action {action} Reward {reward}")

    step += 1

print("\nQ-table Updated:", agent.Q)

#task6 

class FireEnvironment:
    def __init__(self):
        self.rooms = {
            'a': 'safe', 'b': 'safe', 'c': 'fire',
            'd': 'safe', 'e': 'fire', 'f': 'safe',
            'g': 'safe', 'h': 'safe', 'j': 'fire'
        }

    def display(self):
        grid = []
        for room in ['a','b','c','d','e','f','g','h','j']:
            grid.append('F' if self.rooms[room] == 'fire' else '.')
        print(grid[0:3])
        print(grid[3:6])
        print(grid[6:9])
        print()


class FireRobot:
    def __init__(self, name):
        self.name = name
        self.path = ['a','b','c','d','e','f','g','h','j']

    def act(self, env):
        for room in self.path:
            print(f"{self.name} enters room {room}")

            if env.rooms[room] == 'fire':
                print("Fire detected! Extinguishing...")
                env.rooms[room] = 'safe'
            else:
                print("Room is safe")

            env.display()

        print("All fires extinguished! Mission complete 🚒")


env = FireEnvironment()
robot = FireRobot("Abeeha")

robot.act(env)
