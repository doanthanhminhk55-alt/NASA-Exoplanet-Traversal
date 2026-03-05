# NASA Exoplanet Traversal

Since 1992 over 4,000 exoplanets have been discovered outside our solar system. The United States National Aeronautics and Space Administration (NASA) maintains a publicly accessible archive of the data collected on these in comma separated value (CSV) format.

The objective of the NASA Exoplanet Traversal app is to make this data available for simple queries by its users. 

### Requirements & Constraints

- The Developer should implement a means of efficiently loading the exoplanet
  CSV data obtained from NASA to minimize any delays when the application starts.

- Similarly, the Developer should utilize a data structure and search mechanism
  that minimizes the time required to query the exoplanet data and display the
  results.

Notes: The Developer will need to review the Exoplanet Archive documentation to
understand the format of the data fields.

## User Stories

- User can see an query input panel containing dropdowns allowing the
  user to query on year of discovery and discovery facility.

- User can also see 'Clear' and 'Search' buttons in the query input panel.

- User can select a single value from any one or both of the query dropdowns.

- User can click the 'Search' button to search for exoplanets matching all of the selected query values.

- User can see an error message if the 'Search' button was clicked, but no query values were selected.

- User can see the matching exoplanet data displayed in tabular format in an results panel below the query panel.
  
  - The results panel will display headings for display fields. Only the following fields should be displayed: year of discovery, discovery facility, planet name, planet radius (Earth Radius), planet earth, planet mass (Earth Mass).
  
  - Only **ten results** should be visible at one time.

- User can see icons (such as scroll bar symbol) in the results panel.

- User can click on the scroll bar to scroll through the results, which display in the ten row deep, visible panel.
  in ascending order on the values in that column

- User can see icons (such as up and down symbols) in the column headers.

- User can click on the up symbol to sort the rows in the results panel
  in ascending order on the values in that column.

- User can click on the down symbol to sort the rows in the results panel
  in descending order on the values in the column.

- User can click the 'Clear' button to reset the query selections and clear any data displayed in the results panel, if a search had been performed.

## Bonus features

- User can see in the results panels icons allowing the user to add and remove columns to the query results panel.

- User can click on the add symbol to add a column to the results panel
  and select from one of three field names to display in the new column.
  
  - Only the following three fields should be options when a user elects to add a new column: host name, number of planets, number of stars.
  
  - The results panel will display a header for the new field.
  
  - The results panel will display the data for the new field.

- User can click on the remove symbol to remove a column the user previously added to the results panel.

- Superpower: A graphical representation of the planets visible in the **ten deep** results panel will appear in a separate pane.
  
  - The representation will be spheres representing the differences in Mass between the planets visible in the results panel.

## Useful links and resources

- [NASA Exoplanet Archive Data Resources](https://exoplanetarchive.ipac.caltech.edu/docs/data.html))
- [Exoplanet - Wikipedia](https://en.wikipedia.org/wiki/Exoplanet)
- [Big O Notation (Wikipedia)](https://en.wikipedia.org/wiki/Big_O_notation)
- [CSV2JSON](https://github.com/florinpop17/app-ideas/blob/master/Projects/1-Beginner/CSV2JSON-App.md)
