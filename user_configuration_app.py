def add_setting(a,b):
    key = str(b[0]).lower()
    value=str(b[1]).lower()

    if key in a:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    a[key]=value
    return f"Setting '{key}' added with value '{value}' successfully!"
add_setting({'theme': 'light'}, ('volume', 'high'))

def update_setting(a,b):
    key = str(b[0]).lower()
    value=str(b[1]).lower()

    if key in a:
        a[key]=value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
update_setting({'theme': 'light'}, ('theme', 'dark'))

def delete_setting(a,b):
    key = b.lower()

    if key in a:
        del a[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"
delete_setting({'theme': 'light'}, 'theme')
def view_settings(a):
    if not a:
        return "No settings available."
    result = "Current User Settings:\n"
    for key, value in a.items():
        result += f"{key.capitalize()}: {value}\n"
    return result
view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'})
test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high"
}
