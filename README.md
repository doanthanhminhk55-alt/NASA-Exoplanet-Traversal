# 🚀 NASA Exoplanet Traversal

Explore thousands of **exoplanets discovered outside our solar system**
using data from the **NASA Exoplanet Archive**.

This application allows users to efficiently **query, filter, sort, and
visualize exoplanet discoveries** using an interactive web interface.

------------------------------------------------------------------------

## 🌌 Overview

Since **1992**, more than **4,000 exoplanets** have been discovered
beyond our solar system.

The **NASA Exoplanet Traversal** application enables users to:

-   Search exoplanets by **Discovery Year**
-   Filter by **Discovery Facility**
-   View results in a **sortable table**
-   Dynamically **add or remove columns**
-   Visualize planet **mass differences using graphical spheres**

The application focuses on **efficient data loading**, **fast
querying**, and **clean UI interaction**.

------------------------------------------------------------------------

# ✨ Features

## 🔍 Query Panel

Users can filter the dataset using:

-   **Discovery Year**
-   **Discovery Facility**

Actions available:

-   **Search** → Retrieve matching planets\
-   **Clear** → Reset filters and results

If the user clicks **Search without selecting filters**, an **error
message** will be displayed.

------------------------------------------------------------------------

# 📊 Results Panel

Matching exoplanets are displayed in a **tabular results panel**.

### Default Fields

  Field                          Description
  ------------------------------ ------------------------------------------
  Discovery Year                 Year the planet was discovered
  Discovery Facility             Telescope or facility that discovered it
  Planet Name                    Name of the exoplanet
  Planet Radius (Earth Radius)   Planet radius relative to Earth
  Planet Mass (Earth Mass)       Planet mass relative to Earth

### Table Features

-   Only **10 rows visible at a time**
-   **Scrollable results panel**
-   Columns support **ascending / descending sorting**
-   Fast rendering using **Streamlit DataFrame**

------------------------------------------------------------------------

# ⭐ Bonus Features

## ➕ Dynamic Column Management

Users can **add additional columns** to the results table.

Available fields:

-   **Host Name**
-   **Number of Planets**
-   **Number of Stars**

Features:

-   Add new columns dynamically
-   Remove previously added columns
-   Table header updates automatically
-   Data values update in real-time

------------------------------------------------------------------------

## 🪐 Planet Mass Visualization (Superpower Feature)

A **graphical representation of the planets** currently visible in the
**10-row results panel** is displayed in a separate pane.

Each planet is represented as a **sphere** where:

-   Sphere size corresponds to **planet mass**
-   Larger mass → **larger sphere**

Visualization is implemented using **Matplotlib**.

------------------------------------------------------------------------

# 🏗 Architecture

The project follows a **clean modular structure** separating backend
data logic and frontend UI.

NASA-Exoplanet-Traversal │ ├── backend │ ├── loader.py \# Loads and
preprocesses CSV data │ └── search.py \# Implements search and filtering
logic │ ├── frontend │ └── app.py \# Streamlit UI application │ ├── data
│ └── exoplanets.csv \# NASA dataset │ ├── requirements.txt └──
README.md

------------------------------------------------------------------------

# ⚡ Performance Strategy

To ensure fast startup and querying:

### Efficient Data Loading

-   Dataset loaded once using **Pandas**
-   Cached using **Streamlit `@st.cache_data`**
-   Only required fields retained in memory

### Fast Query Execution

Filtering is performed **in-memory** using optimized DataFrame
operations.

Example:

results = df\[ (df\["disc_year"\] == year) & (df\["disc_facility"\] ==
facility)\]

This approach ensures **fast query performance**.

------------------------------------------------------------------------

### Performance Optimization
- Cached data loading using Streamlit caching
- In-memory DataFrame filtering for fast queries
- Minimal column selection to reduce memory footprint

# 📦 Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/NASA-Exoplanet-Traversal.git
cd NASA-Exoplanet-Traversal

Install dependencies:

pip install -r requirements.txt

------------------------------------------------------------------------

# ▶ Running the Application

Start the Streamlit application:

python -m streamlit run frontend/app.py

Then open:

http://localhost:8501

------------------------------------------------------------------------

# 🧰 Technologies Used

-   Python
-   Pandas
-   Streamlit
-   Matplotlib
-   CSV Data Processing

------------------------------------------------------------------------

# 📚 Data Source

NASA Exoplanet Archive

https://exoplanetarchive.ipac.caltech.edu/

------------------------------------------------------------------------

# 👨‍💻 Author

**Doan Thanh Minh**
