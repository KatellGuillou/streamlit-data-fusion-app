import streamlit as st
import pandas as pd
import json
import io
from datetime import datetime, date
import geopandas as gpd
from shapely.geometry import Point
import tempfile
import os

# Page configuration
st.set_page_config(
    page_title="Data Fusion App",
    page_icon="🔗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Modern CSS styling to match the design
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .via-fusion-tag {
        background-color: #ff6b35;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.9rem;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 2rem;
        text-align: center;
        width: 100%;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
    }
    .upload-section {
        background-color: #f8f9fa;
        border: 2px dashed #dee2e6;
        border-radius: 10px;
        padding: 2rem;
        margin: 1rem 0;
        text-align: center;
    }
    .upload-title {
        font-size: 1.4rem;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    .upload-subtitle {
        color: #6c757d;
        margin-bottom: 1rem;
    }
    .file-upload-area {
        background-color: #f8f9fa;
        border: 2px dashed #dee2e6;
        border-radius: 8px;
        padding: 2rem;
        margin: 1rem 0;
        text-align: center;
        min-height: 120px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .upload-icon {
        font-size: 2rem;
        color: #6c757d;
        margin-bottom: 1rem;
    }
    .upload-text {
        color: #495057;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    .upload-limit {
        color: #6c757d;
        font-size: 0.9rem;
    }
    .browse-button {
        background-color: #6c757d;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        margin-top: 1rem;
    }
    .file-info-box {
        background-color: #e7f3ff;
        border: 1px solid #b3d9ff;
        color: #004085;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        text-align: center;
    }
    .success-message {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 0.75rem;
        border-radius: 0.25rem;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #e7f3ff;
        border: 1px solid #b3d9ff;
        color: #004085;
        padding: 1rem;
        border-radius: 0.25rem;
        margin: 1rem 0;
    }
    .footer {
        text-align: center;
        color: #666;
        margin-top: 2rem;
        padding: 1rem;
        border-top: 1px solid #dee2e6;
    }
    .metric-card {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Main header with Via Fusion tag
    st.markdown('<div class="main-header">🔗 Data Fusion Application</div>', unsafe_allow_html=True)
    st.markdown('<div class="via-fusion-tag">Via Fusion</div>', unsafe_allow_html=True)
    
    # Sidebar for configuration
    with st.sidebar:
        st.markdown("## ⚙️ Configuration")
        
        # Scope Selector
        st.markdown("### 📍 Target Scope Selection")
        scope_options = {
            "Vianova Showcase - 300557 - Dubai UAE - 403825": "403825",
            "Lime - 300066 - Lime Gothenburg - 300109": "300109",
            "Stadt Sindelfingen - 309232 - EV Ladestation Demo - 408444": "408444",
            "Fenix - 304630 - Abu Dhabi - 306669": "306669",
            "BoltEU - 300076 - Bolt Ludwigshafen - 353510": "353510",
            "vianova-feed-management - 1 - test-road-import-over-20k - 403792": "403792",
            "Lime - 300066 - Lime Brussels - 300118": "300118",
            "waytailLive - 10109 - Northindainzia - 404103": "404103",
            "Marseille - 408340 - France - 408340": "408340",
            "Lyon - 408341 - France - 408341": "408341",
            "Paris - 408342 - France - 408342": "408342",
            "Toulouse - 408343 - France - 408343": "408343",
            "Nice - 408344 - France - 408344": "408344",
            "Nantes - 408345 - France - 408345": "408345",
            "Strasbourg - 408346 - France - 408346": "408346",
            "Montpellier - 408347 - France - 408347": "408347",
            "Bordeaux - 408348 - France - 408348": "408348",
            "Lille - 408349 - France - 408349": "408349"
        }
        
        selected_scope = st.selectbox(
            "Target_scope:",
            options=list(scope_options.keys()),
            index=0,  # Default to Vianova Showcase
            placeholder="Choose an option"
        )
        
        scope_number = scope_options[selected_scope]
        st.info(f"Selected Scope: {scope_number}")
        
        # Date Picker
        st.markdown("### 📅 Date Selection")
        selected_date = st.date_input(
            "Select Date:",
            value=date(2025, 9, 29),  # Default to September 29, 2025
            min_value=date(2020, 1, 1),
            max_value=date(2030, 12, 31)
        )
        
        st.info(f"Selected Date: {selected_date}")
        
        # Processing options
        st.markdown("### 🔧 Processing Options")
        merge_strategy = st.selectbox(
            "Merge Strategy:",
            ["Inner Join", "Left Join", "Right Join", "Outer Join"],
            index=0
        )
        
        include_geojson = st.checkbox("Generate GeoJSON Output", value=True)
    
    # Main content area with modern interface
    st.markdown('<div class="section-header">📊 Data Upload</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📊 Data Upload")
        st.markdown("**Upload** CSV **File:**")
        
        # Custom upload area
        st.markdown("""
        <div class="file-upload-area">
            <div class="upload-icon">☁️</div>
            <div class="upload-text">Drag and drop file here</div>
            <div class="upload-limit">Limit 200MB per file • CSV</div>
        </div>
        """, unsafe_allow_html=True)
        
        bms_file = st.file_uploader(
            "Upload BMS CSV File:",
            type=['csv'],
            key="bms_uploader",
            help="Upload your BMS (Battery Management System) data file",
            label_visibility="collapsed"
        )
        
        if bms_file is not None:
            try:
                bms_df = pd.read_csv(bms_file)
                st.success(f"✅ BMS file loaded successfully!")
                st.info(f"📈 BMS Data: {len(bms_df)} rows, {len(bms_df.columns)} columns")
                
                # Show preview
                with st.expander("🔍 BMS Data Preview"):
                    st.dataframe(bms_df.head(10))
                    
            except Exception as e:
                st.error(f"❌ Error loading BMS file: {str(e)}")
                bms_df = None
        else:
            bms_df = None
            st.markdown('<div class="file-info-box">📁 Please upload a CSV file</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🛣️ Road Data Upload")
        st.markdown("**Upload** CSV **File:**")
        
        # Custom upload area
        st.markdown("""
        <div class="file-upload-area">
            <div class="upload-icon">☁️</div>
            <div class="upload-text">Drag and drop file here</div>
            <div class="upload-limit">Limit 200MB per file • CSV</div>
        </div>
        """, unsafe_allow_html=True)
        
        road_file = st.file_uploader(
            "Upload Road CSV File:",
            type=['csv'],
            key="road_uploader",
            help="Upload your road data file",
            label_visibility="collapsed"
        )
        
        if road_file is not None:
            try:
                road_df = pd.read_csv(road_file)
                st.success(f"✅ Road file loaded successfully!")
                st.info(f"📈 Road Data: {len(road_df)} rows, {len(road_df.columns)} columns")
                
                # Show preview
                with st.expander("🔍 Road Data Preview"):
                    st.dataframe(road_df.head(10))
                    
            except Exception as e:
                st.error(f"❌ Error loading Road file: {str(e)}")
                road_df = None
        else:
            road_df = None
            st.markdown('<div class="file-info-box">📁 Please upload a CSV file</div>', unsafe_allow_html=True)
    
    # Data Processing Section
    if bms_df is not None and road_df is not None:
        st.markdown('<div class="section-header">🔄 Data Processing</div>', unsafe_allow_html=True)
        
        # Show data info in cards
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>BMS Records</h3>
                <h2 style="color: #1f77b4;">{len(bms_df)}</h2>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Road Records</h3>
                <h2 style="color: #1f77b4;">{len(road_df)}</h2>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Scope</h3>
                <h2 style="color: #1f77b4;">{scope_number}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        # Find common columns for merging
        common_columns = set(bms_df.columns) & set(road_df.columns)
        if common_columns:
            st.info(f"🔗 Common columns found: {', '.join(common_columns)}")
        else:
            st.warning("⚠️ No common columns found between datasets")
        
        # Merge button
        if st.button("🔗 Combine CSV Files", type="primary", use_container_width=True):
            with st.spinner("Processing data fusion..."):
                try:
                    # Add metadata columns
                    bms_df_processed = bms_df.copy()
                    road_df_processed = road_df.copy()
                    
                    bms_df_processed['data_source'] = 'BMS'
                    bms_df_processed['scope'] = scope_number
                    bms_df_processed['processing_date'] = selected_date
                    
                    road_df_processed['data_source'] = 'Road'
                    road_df_processed['scope'] = scope_number
                    road_df_processed['processing_date'] = selected_date
                    
                    # Perform merge based on strategy
                    if merge_strategy == "Inner Join":
                        merged_df = pd.merge(bms_df_processed, road_df_processed, 
                                           on=list(common_columns), how='inner')
                    elif merge_strategy == "Left Join":
                        merged_df = pd.merge(bms_df_processed, road_df_processed, 
                                           on=list(common_columns), how='left')
                    elif merge_strategy == "Right Join":
                        merged_df = pd.merge(bms_df_processed, road_df_processed, 
                                           on=list(common_columns), how='right')
                    else:  # Outer Join
                        merged_df = pd.merge(bms_df_processed, road_df_processed, 
                                           on=list(common_columns), how='outer')
                    
                    # Store in session state
                    st.session_state['merged_data'] = merged_df
                    st.session_state['bms_data'] = bms_df_processed
                    st.session_state['road_data'] = road_df_processed
                    
                    st.success(f"✅ Data fusion completed! {len(merged_df)} records created")
                    
                except Exception as e:
                    st.error(f"❌ Error during data fusion: {str(e)}")
    
    # Results and Download Section
    if 'merged_data' in st.session_state:
        st.markdown('<div class="section-header">📥 Download Results</div>', unsafe_allow_html=True)
        
        merged_df = st.session_state['merged_data']
        
        # Show results summary in cards
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Total Records</h3>
                <h2 style="color: #1f77b4;">{len(merged_df)}</h2>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Total Columns</h3>
                <h2 style="color: #1f77b4;">{len(merged_df.columns)}</h2>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <h3>BMS Records</h3>
                <h2 style="color: #1f77b4;">{len(merged_df[merged_df['data_source'] == 'BMS'])}</h2>
            </div>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Road Records</h3>
                <h2 style="color: #1f77b4;">{len(merged_df[merged_df['data_source'] == 'Road'])}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        # Show merged data preview
        with st.expander("🔍 Merged Data Preview"):
            st.dataframe(merged_df.head(20))
        
        # Download buttons
        col1, col2 = st.columns(2)
        
        with col1:
            # CSV Download
            csv_buffer = io.StringIO()
            merged_df.to_csv(csv_buffer, index=False)
            csv_data = csv_buffer.getvalue()
            
            st.download_button(
                label="📊 Download CSV",
                data=csv_data,
                file_name=f"merged_data_{scope_number}_{selected_date}.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        with col2:
            if include_geojson:
                # GeoJSON Download
                try:
                    # Create GeoJSON from merged data
                    geojson_data = create_geojson_from_data(merged_df, scope_number)
                    
                    st.download_button(
                        label="🗺️ Download GeoJSON",
                        data=json.dumps(geojson_data, indent=2),
                        file_name=f"merged_data_{scope_number}_{selected_date}.geojson",
                        mime="application/json",
                        use_container_width=True
                    )
                except Exception as e:
                    st.error(f"❌ Error creating GeoJSON: {str(e)}")
                    st.info("💡 GeoJSON creation requires coordinate columns (lat, lon or latitude, longitude)")
    
    # Footer
    st.markdown(f"""
    <div class="footer">
        <p>🔗 Data Fusion Application | Built with Streamlit</p>
        <p>Scope: {scope_number} | Date: {selected_date}</p>
    </div>
    """, unsafe_allow_html=True)

def create_geojson_from_data(df, scope_number):
    """Create GeoJSON from DataFrame with coordinate columns"""
    features = []
    
    # Try to find coordinate columns
    lat_cols = [col for col in df.columns if 'lat' in col.lower()]
    lon_cols = [col for col in df.columns if 'lon' in col.lower() or 'lng' in col.lower()]
    
    if not lat_cols or not lon_cols:
        # If no coordinate columns, create a simple GeoJSON with metadata
        return {
            "type": "FeatureCollection",
            "name": f"merged_data_{scope_number}",
            "features": [{
                "type": "Feature",
                "properties": {
                    "scope": scope_number,
                    "total_records": len(df),
                    "description": "Merged dataset without spatial coordinates"
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [0, 0]  # Default coordinates
                }
            }]
        }
    
    lat_col = lat_cols[0]
    lon_col = lon_cols[0]
    
    for idx, row in df.iterrows():
        try:
            lat = float(row[lat_col])
            lon = float(row[lon_col])
            
            if pd.notna(lat) and pd.notna(lon):
                feature = {
                    "type": "Feature",
                    "properties": {col: row[col] for col in df.columns if col not in [lat_col, lon_col]},
                    "geometry": {
                        "type": "Point",
                        "coordinates": [lon, lat]
                    }
                }
                features.append(feature)
        except (ValueError, TypeError):
            continue
    
    return {
        "type": "FeatureCollection",
        "name": f"merged_data_{scope_number}",
        "features": features
    }

if __name__ == "__main__":
    main()
