def search_exoplanets(df, year=None, facility=None):

    result = df

    if year is not None:
        result = result[result["Discovery Year"] == year]

    if facility is not None:
        result = result[result["Discovery Facility"] == facility]

    return result