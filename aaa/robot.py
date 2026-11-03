class AIRobot:
    def __init__(self, name: str = "HeroRobot"):
        self.name = name
        self.state = "idle"
        self.battery = 100.0

    def get_status(self) -> dict:
        return {
            "name": self.name,
            "state": self.state,
            "battery": self.battery
        }

    def execute_command(self, command: str) -> str:
        if command == "start":
            self.state = "running"
            return f"{self.name} started."
        elif command == "stop":
            self.state = "stopped"
            return f"{self.name} stopped."
        elif command == "charge":
            self.battery = 100.0
            self.state = "charging"
            return f"{self.name} is charging."
        else:
            return f"Unknown command: {command}"

    def make_decision(self, context: dict) -> str:
        if self.battery < 20.0:
            return "charge"
        return "continue"
