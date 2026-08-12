test_settings = {
    "test":2
}

def add_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()
    if key in settings:
        return "Setting 'theme' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return "Setting 'volume' added with value 'high' successfully!"

def update_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, pair):
    key = pair
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"
        
def view_settings(settings):
    if not settings:
        return "No settings available."

    preview = "Current User Settings:\n"

    for key, value in settings.items():
        preview += f"{key.capitalize()}: {value}\n"

    return preview
add_setting({'theme': 'light'}, ('THEME', 'dark'))
update_setting({'theme': 'light'}, ('theme', 'dark'))
delete_setting({'theme': 'light'}, 'theme')
view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'})