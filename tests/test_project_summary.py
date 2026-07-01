from pathlib import Path


def main():
    path = Path("outputs/project_summary.json")

    assert path.exists()

    print("Project summary test passed.")


if __name__ == "__main__":
    main()
