# Economic Growth and Environmental Quality - The Cas of West African Countries (ECOWAS)

## Project Overview

This project explores the relationship between economic growth and environmental quality in West African countries using data-driven analysis. The project primarily focuses on evaluating environmental indicators such as air quality (PM2.5, Ozone) and economic indicators (GDP, nightlight intensity as a proxy for economic activity) across various countries in the region.

## Table of Contents

- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Data Sources](#data-sources)
- [Analysis](#analysis)
- [Plots and Visualizations](#plots-and-visualizations)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Directory Structure

The project is organized into the following directories:

- **database/**: Contains the raw data and processed datasets for various West African countries.
  - **VERSION FINALE/**: Final version of the datasets used in the analysis.
    - Each country has its own folder containing relevant data files, such as:
      - `results.csv`: Results from the analysis for that specific country.
      - `documentation.pdf`: Documentation explaining the data sources and methodology.
      - `.geojson` files: Geospatial data files used for mapping and spatial analysis.

- **plots/**: Contains various visualizations generated during the analysis, such as:
  - `Kuznet-NL_Ozone.png`: A plot showing the relationship between nightlight intensity and ozone levels.
  - `PM2.5.png`: A plot of PM2.5 levels across different regions.
  - And more related visualizations depicting various environmental and economic indicators.

- **scripts/**: (If present) Python and R scripts used for data processing, analysis, and visualization.

## Data Sources

The data used in this project are sourced from reputable databases, including:

- Environmental data (e.g., air quality indices like PM2.5, Ozone).
- Economic data (e.g., GDP, nightlight intensity).
- Geospatial data for mapping and spatial analysis.

Please refer to the `documentation.pdf` files in the `database/VERSION FINALE/` directories for detailed information about each dataset.

## Analysis

The analysis is conducted using a combination of Python and R programming languages. Key analyses include:

- **Environmental Kuznets Curve (EKC)**: Assessing the relationship between economic growth and environmental degradation.
- **Geospatial Analysis**: Mapping and spatial analysis of environmental indicators.
- **Time-Series Analysis**: Evaluating trends over time for economic and environmental indicators.

## Plots and Visualizations

The `plots/` directory contains visual representations of the analysis, including but not limited to:

- The relationship between economic indicators (e.g., GDP, nightlight intensity) and environmental quality (e.g., PM2.5, Ozone).
- Geospatial maps illustrating environmental quality across regions.

## Usage

To replicate the analysis or explore the data:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/economic-growth-environment-west-africa.git
   ```
2. **Install necessary dependencies**:
   - Python: Install required packages using `requirements.txt`.
   - R: Install required libraries using the appropriate package manager (e.g., `install.packages()`).

3. **Run the scripts**:
   - Use the provided scripts in the `scripts/` directory to process data and generate visualizations.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
