from runner import run_etl


def main():
    df, ranking, model = run_etl()  # type: ignore


if __name__ == "__main__":
    main()
