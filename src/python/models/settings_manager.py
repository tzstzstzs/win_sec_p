import json
import os


class SettingsManager:
    def __init__(self, default_settings_file='config/default_settings.json',
                 user_settings_file='config/user_settings.json'):
        self.default_settings_file = default_settings_file
        self.user_settings_file = user_settings_file
        self.settings = self.load_settings()

    def load_settings(self):
        if not os.path.exists(self.user_settings_file):
            with open(self.default_settings_file, 'r', encoding='utf-8') as file:
                settings = json.load(file)
            with open(self.user_settings_file, 'w', encoding='utf-8') as file:
                json.dump(settings, file, indent=4, ensure_ascii=False)
        else:
            with open(self.user_settings_file, 'r', encoding='utf-8') as file:
                settings = json.load(file)
        return settings

    def get_setting(self, key):
        return self.settings.get(key)

    def update_setting(self, key, value):
        self.settings[key] = value
        with open(self.user_settings_file, 'w', encoding='utf-8') as file:
            json.dump(self.settings, file, indent=4, ensure_ascii=False)
