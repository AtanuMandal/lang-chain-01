from pathlib import Path
from dotenv import dotenv_values


def main():
    
    env_path = Path(__file__).parent / ".env"
    if env_path.exists():
        vals = dotenv_values(env_path)
        if vals:
            print("Loaded variables from .env:")
            for k, v in vals.items():
                print(f"{k}={v}")
        else:
            print(".env found but no variables parsed.")
    else:
        print(".env not found in project root.")


if __name__ == "__main__":
    main()
def main():
    print("Hello from lang-chain-01!")

