import questionary

def main_menu():
    """
    Displays the main menu and returns the user's choice.
    """
    return questionary.select(
        "🎵 Welcome to POTTY Spotify & Music Downloader — Select an option:",
        choices=[
            "Downloads Menu",
            "Management Menu",
            "Automation Menu",
            "Tools Menu",
            "Exit"
        ]
    ).ask()
