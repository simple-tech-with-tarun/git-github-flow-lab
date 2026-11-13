environments = {
    "development": {
        "purpose": "Application development and initial testing",
        "debug": True,
    },
    "staging": {"purpose": "Pre-production validation", "debug": False},
    "production": {"purpose": "Live environment serving end users", "debug": False},
}


def display_environments():
    for name, config in environments.items():
        print(f"Environment: {name}")
        print(f"Purpose: {config['purpose']}")
        print(f"Debug: {config['debug']}")
        print("-" * 40)


if __name__ == "__main__":
    display_environments()
