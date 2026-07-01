from pathlib import Path


def main():
    file = Path("outputs/ranking_analysis.json")

    assert file.exists()

    print("Ranking analysis test passed.")


if __name__ == "__main__":
    main()
