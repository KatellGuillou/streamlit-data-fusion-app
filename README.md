# 🔗 Data Fusion Streamlit Application

A powerful web application built with Streamlit for combining and processing BMS (Battery Management System) and Road data with advanced features including scope selection, date filtering, and GeoJSON export capabilities.

## ✨ Features

### 🎯 Core Functionality
- **Scope Selector**: Dropdown with scope numbers and city names (default: Vianova Showcase - 300557 - Dubai UAE - 403825)
- **Date Picker**: Set to September 29, 2025 by default
- **Dual CSV Upload**: Drag & drop interfaces for BMS and Road data
- **Smart Data Fusion**: Multiple merge strategies (Inner, Left, Right, Outer Join)
- **Export Options**: CSV and GeoJSON download capabilities

### 🛠️ Technical Features
- **Responsive Design**: Clean, modern UI with custom CSS styling
- **Data Validation**: Automatic error handling and data preview
- **Session Management**: Persistent data across interactions
- **Geospatial Support**: Automatic GeoJSON generation from coordinate data
- **Metadata Tracking**: Automatic addition of scope, date, and source information

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Navigate to the Hackathon folder**:
```bash
cd Hackathon
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run the application**:
```bash
streamlit run app.py
```

4. **Access the app**: Open your browser to `http://localhost:8501`

## 📖 Usage Guide

### Step 1: Configuration
- **Select Scope**: Choose from the dropdown (default: Vianova Showcase - 300557 - Dubai UAE - 403825)
- **Set Date**: Use the date picker (default: September 29, 2025)
- **Choose Merge Strategy**: Select how to combine your datasets

### Step 2: Data Upload
- **BMS Data**: Upload your Battery Management System CSV file
- **Road Data**: Upload your road data CSV file
- **Preview**: Review your data using the expandable preview sections

### Step 3: Data Processing
- **Combine**: Click the "Combine CSV Files" button to merge datasets
- **Review**: Check the merged data preview and statistics
- **Download**: Export results as CSV or GeoJSON

### Step 4: Export Results
- **CSV Export**: Download merged data as CSV file
- **GeoJSON Export**: Download spatial data for mapping applications
- **Metadata**: All exports include scope, date, and source information

## 🔧 Configuration Options

### Scope Options
- Vianova Showcase - 300557 - Dubai UAE - 403825 (default)
- Lime - 300066 - Lime Gothenburg - 300109
- Stadt Sindelfingen - 309232 - EV Ladestation Demo - 408444
- Fenix - 304630 - Abu Dhabi - 306669
- BoltEU - 300076 - Bolt Ludwigshafen - 353510
- vianova-feed-management - 1 - test-road-import-over-20k - 403792
- Lime - 300066 - Lime Brussels - 300118
- waytailLive - 10109 - Northindainzia - 404103
- Plus French cities: Marseille, Lyon, Paris, Toulouse, Nice, Nantes, Strasbourg, Montpellier, Bordeaux, Lille

### Merge Strategies
- **Inner Join**: Only matching records from both datasets
- **Left Join**: All BMS records + matching Road records
- **Right Join**: All Road records + matching BMS records
- **Outer Join**: All records from both datasets

## 📊 Data Requirements

### CSV Format
- **Encoding**: UTF-8 recommended
- **Headers**: First row should contain column names
- **Coordinates**: For GeoJSON export, include 'lat'/'latitude' and 'lon'/'longitude' columns

### Supported File Types
- CSV files (.csv)
- UTF-8 encoding recommended
- Maximum file size: 200MB (Streamlit default)

## 🗺️ GeoJSON Export

The application automatically detects coordinate columns and creates GeoJSON files suitable for:
- **Mapping Applications**: Leaflet, Mapbox, Google Maps
- **GIS Software**: QGIS, ArcGIS
- **Web Development**: Interactive maps and visualizations

### Coordinate Detection
- Latitude columns: `lat`, `latitude`, `Lat`, `LAT`
- Longitude columns: `lon`, `lng`, `longitude`, `Lon`, `LNG`

## 🛠️ Development

### Project Structure
```
Hackathon/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                # This documentation
├── run.py                   # Simple launcher script
├── setup.py                 # Automated setup script
├── .gitignore               # Git ignore file
└── DEPLOYMENT.md            # Deployment guide
```

### Dependencies
- **streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **geopandas**: Geospatial data processing
- **shapely**: Geometric operations
- **plotly**: Interactive visualizations

### Customization
- **Styling**: Modify the CSS in the `st.markdown()` section
- **Scopes**: Add new scope options in the `scope_options` dictionary
- **Merge Logic**: Customize the merge strategies in the processing section

## 🚨 Troubleshooting

### Common Issues

1. **File Upload Errors**:
   - Ensure CSV files are properly formatted
   - Check file encoding (UTF-8 recommended)
   - Verify file size is under 200MB

2. **Merge Failures**:
   - Check for common columns between datasets
   - Verify data types are compatible
   - Review error messages in the interface

3. **GeoJSON Export Issues**:
   - Ensure coordinate columns exist
   - Check coordinate format (decimal degrees)
   - Verify latitude/longitude ranges

### Performance Tips
- Use smaller datasets for testing
- Close other browser tabs to free memory
- Process data in chunks for large files

## 📝 License

This project is part of your existing codebase. Please refer to your project's license terms.

## 🤝 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the error messages in the Streamlit interface
3. Ensure all dependencies are properly installed

---

**Built with ❤️ using Streamlit**
