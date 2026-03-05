import pandas as pd


class ExoplanetLoader:
    """
    ExoplanetLoader loads NASA Exoplanet Archive CSV data
    and provides efficient access for queries.
    """

    def __init__(self, file_path):
        """
        Initialize the loader and read the CSV dataset.
        Only required columns are loaded to reduce memory usage
        and improve application startup time.
        """

        # Load CSV file
        self.df = pd.read_csv(
            file_path,
            comment="#",       # Ignore metadata lines starting with '#'
            low_memory=False
        )

        # Keep only the columns needed by the application
        self.df = self.df[
            [
                "disc_year",
                "disc_facility",
                "pl_name",
                "pl_rade",
                "pl_bmasse",
                "hostname",
                "sy_pnum",
                "sy_snum"
            ]
        ]

        # Handle missing values

        # Remove rows without discovery year to avoid invalid values like 0
        self.df = self.df[self.df["disc_year"].notna()]

        # Convert discovery year to integer
        self.df["disc_year"] = self.df["disc_year"].astype(int)

        # Replace missing discovery facility with "Unknown"
        self.df["disc_facility"] = (
            self.df["disc_facility"]
            .fillna("Unknown")
        )

        # Rename columns to more readable names
        self.df = self.df.rename(columns={
            "disc_year": "Discovery Year",
            "disc_facility": "Discovery Facility",
            "pl_name": "Planet Name",
            "pl_rade": "Planet Radius (Earth Radius)",
            "pl_bmasse": "Planet Mass (Earth Mass)",
            "hostname": "Host Name",
            "sy_pnum": "Number of Planets",
            "sy_snum": "Number of Stars"
        })

        # Convert facility column to categorical type to reduce memory usage
        # and improve filtering performance
        self.df["Discovery Facility"] = self.df["Discovery Facility"].astype("category")

        # Sort dataset to improve query performance
        self.df = self.df.sort_values("Discovery Year")

    def get_dataframe(self):
        """
        Return the loaded DataFrame.
        """
        return self.df

    def get_by_year(self, year):
        """
        Retrieve all exoplanets discovered in a given year.
        """
        return self.df[self.df["Discovery Year"] == year]

    def get_by_facility(self, facility):
        """
        Retrieve exoplanets discovered by a specific facility.
        Search is case-insensitive.
        """
        return self.df[
            self.df["Discovery Facility"]
            .str.contains(facility, case=False, na=False)
        ]

    def top_mass_planets(self, n=10):
        """
        Return the top N planets with the largest mass.
        """
        return (
            self.df
            .sort_values("Planet Mass (Earth Mass)", ascending=False)
            .head(n)
        )

    def top_radius_planets(self, n=10):
        """
        Return the top N planets with the largest radius.
        """
        return (
            self.df
            .sort_values("Planet Radius (Earth Radius)", ascending=False)
            .head(n)
        )

    def count_by_year(self):
        """
        Count number of planets discovered per year.
        """
        return (
            self.df
            .groupby("Discovery Year")
            .size()
            .reset_index(name="Planet Count")
        )