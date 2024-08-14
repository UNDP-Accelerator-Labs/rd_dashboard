# R&D Dashboard

## Project Overview

The R&D Dashboard is a web-based visualization tool designed to provide insights into research and development (R&D) activities across various themes and countries. The dashboard includes multiple visualizations, such as gauge charts, bar charts, pie charts, and heatmaps, which offer a comprehensive overview of the distribution and intensity of R&D efforts across the Accelerator Labs.

### Key Features
- **Gauge Charts**: Display the intensity of R&D activities across different themes.
- **Bar Chart**: Compare R&D activities across different regions.
- **Pie Chart**: Visualize the distribution of topics across various themes.
- **Heatmap**: Show the distribution of R&D themes across countries.

## Project Structure

```bash
├── _config.yml          # Jekyll configuration file
├── _data                # Directory containing data files used for visualizations
│   ├── activities_per_country.json
│   ├── themes_per_country.json
│   ├── topics_per_theme.json
├── assets               # Directory for static assets (e.g., CSS, JS)
│   └── ...
├── index.html           # Main HTML file for the dashboard
├── process_data.py      # Python script to process the Excel data and generate JSON files
├── R&D_dashboard_data.xlsx     # The Excel file containing data for the dashboard.
├── README.md            # This README file
└── .github              # GitHub Actions workflow directory
    └── workflows
        └── deploy.yml   # GitHub Actions workflow file for deployment
```

## Setup and Installation

### Prerequisites

- **Python 3.x**: Required for running the data processing script.
- **Jekyll**: Static site generator used to build the dashboard.
- **GitHub Pages**: Hosting platform for the dashboard.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/UNDP-Accelerator-Labs/rd_dashboard.git
   cd rd-dashboard
   ```

2. **Install Python Dependencies**:
   ```bash
   pip install pandas
   ```

3. **Process the Data**:
   Run the Python script to generate the necessary JSON files for the dashboard.
   ```bash
   python process_data.py
   ```

4. **Build the Jekyll Site**:
   Install Jekyll and build the site locally.
   ```bash
   bundle install
   bundle exec jekyll serve
   ```

   Visit `http://localhost:4000` to view the dashboard locally.

## Deployment

This project uses GitHub Actions for continuous deployment to GitHub Pages. The deployment process is triggered automatically on every push to the `main` branch.

### GitHub Actions Workflow

The deployment is managed via a GitHub Actions workflow located in `.github/workflows/jekyll.yml`. The workflow:

1. Checks out the repository.
2. Installs necessary dependencies.
3. Runs the Python script to generate JSON data files.
4. Builds the Jekyll site.
5. Deploys the site to the `gh-pages` branch.

## Usage

After deployment, the R&D Dashboard can be accessed via the (GitHub Pages URL)[https://undp-accelerator-labs.github.io/rd_dashboard/] associated with this repository. The dashboard provides real-time insights into R&D activities, which can be use to monitor and analyze global research trends across the Accelerator labs.

## Updating the Data

The dashboard is powered by data from an [Excel spreadsheet](https://github.com/UNDP-Accelerator-Labs/rd_dashboard/blob/main/R%26D_dashboard_data.xlsx) located in this repository. Contributors can update this spreadsheet directly. After any changes are made, the `process_data.py` script will automatically convert the updated data into JSON files, which are then used for the visualizations displayed on the dashboard.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes.
4. Submit a pull request.

Please ensure that your code adheres to the existing code style and passes all tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Chart.js](https://www.chartjs.org/) - For creating responsive and customizable charts.
- [Plotly](https://plotly.com/) - For data visualization.
- [GitHub Actions](https://github.com/features/actions) - For continuous integration and deployment.
- [Jekyll](https://jekyllrb.com/) - For static site generation.
