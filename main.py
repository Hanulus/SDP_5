from facade import SmartHomeFacade


# Main function - demonstration
def main():
    # Create facade instance
    home = SmartHomeFacade()
    
    # Use simple commands instead of multiple subsystem calls
    home.come_home()      # Coming home
    home.watch_movie()    # Watching movie
    home.party_mode()     # Party time
    home.go_to_sleep()    # Going to sleep
    home.leave_home()     # Leaving home
    
    # This is the essence of Facade Pattern:
    # Instead of 6+ method calls -> one method does everything!
    print("=" * 40)
    print("FACADE PATTERN DEMO COMPLETED")
    print("=" * 40)


if __name__ == "__main__":
    main()
