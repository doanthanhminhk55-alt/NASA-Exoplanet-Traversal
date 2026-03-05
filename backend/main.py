from loader import ExoplanetLoader
from search import search_exoplanets

def main():

    file_path = "../data/exoplanets.csv"

    loader = ExoplanetLoader(file_path)
    df = loader.df

    print("NASA Exoplanet Traversal")
    print("-----------------------")

    year = input("Enter discovery year (or leave empty): ")
    facility = input("Enter discovery facility (or leave empty): ")

    year = int(year) if year.strip() else None
    facility = facility.strip() if facility.strip() else None

    results = search_exoplanets(df, year, facility)

    if results.empty:
        print("No results found.")
    else:
        print(results.head(10))


if __name__ == "__main__":
    main()