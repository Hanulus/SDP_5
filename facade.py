from subsystems.lighting import LightingSystem
from subsystems.climate import ClimateControl
from subsystems.security import SecuritySystem
from subsystems.entertainment import EntertainmentSystem


# FACADE - main pattern class
class SmartHomeFacade:
    """
    Facade Pattern: simplifies interaction with multiple subsystems.
    Instead of 10+ method calls - one simple method does everything.
    """
    
    def __init__(self):
        # Initialize all subsystems
        self.lights = LightingSystem()
        self.climate = ClimateControl()
        self.security = SecuritySystem()
        self.entertainment = EntertainmentSystem()
    
    # Scenario 1: Leaving home
    def leave_home(self):
        print("\n===== LEAVING HOME =====")
        self.lights.turn_off()
        self.climate.turn_off_heating()
        self.security.lock_doors()
        self.security.arm_alarm()
        self.entertainment.turn_off_tv()
        self.entertainment.stop_music()
        print("Home is secured!\n")
    
    # Scenario 2: Coming back home
    def come_home(self):
        print("\n===== WELCOME HOME =====")
        self.security.disarm_alarm()
        self.security.unlock_doors()
        self.lights.turn_on()
        self.climate.set_temperature(22)
        print("Welcome back!\n")
    
    # Scenario 3: Movie evening
    def watch_movie(self):
        print("\n===== MOVIE TIME =====")
        self.lights.dim_lights(20)
        self.entertainment.turn_on_tv()
        self.climate.set_temperature(21)
        print("Ready to watch!\n")
    
    # Scenario 4: Sleep time
    def go_to_sleep(self):
        print("\n===== GOOD NIGHT =====")
        self.lights.turn_off()
        self.entertainment.turn_off_tv()
        self.entertainment.stop_music()
        self.climate.set_temperature(18)
        self.security.lock_doors()
        self.security.arm_alarm()
        print("Sweet dreams!\n")
    
    # Scenario 5: Party time
    def party_mode(self):
        print("\n===== PARTY MODE =====")
        self.lights.turn_on()
        self.entertainment.play_music()
        self.climate.set_temperature(20)
        print("Let's party!\n")
