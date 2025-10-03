#!/usr/bin/env python3
"""
Simple script to run the Streamlit Data Fusion Application
"""

import subprocess
import sys
import os

def main():
    """Run the Streamlit application"""
    try:
        # Check if streamlit is installed
        try:
            import streamlit
            print("✅ Streamlit is installed")
        except ImportError:
            print("❌ Streamlit is not installed. Please run: pip install -r requirements.txt")
            return
        
        # Check if app.py exists
        if not os.path.exists("app.py"):
            print("❌ app.py not found in current directory")
            return
        
        print("🚀 Starting Data Fusion Application...")
        print("📱 The app will open in your browser at http://localhost:8501")
        print("🛑 Press Ctrl+C to stop the application")
        print("-" * 50)
        
        # Run streamlit
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
        
    except KeyboardInterrupt:
        print("\n🛑 Application stopped by user")
    except Exception as e:
        print(f"❌ Error running application: {e}")

if __name__ == "__main__":
    main()
