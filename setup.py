#!/usr/bin/env python3
"""
Setup script for the Data Fusion Streamlit Application
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def check_files():
    """Check if all required files exist"""
    required_files = ["app.py", "requirements.txt", "README.md"]
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
        return False
    else:
        print("✅ All required files found")
        return True

def main():
    """Main setup function"""
    print("🔧 Setting up Data Fusion Application...")
    print("=" * 50)
    
    # Check files
    if not check_files():
        print("❌ Setup failed: Missing required files")
        return
    
    # Install requirements
    if not install_requirements():
        print("❌ Setup failed: Could not install requirements")
        return
    
    print("\n🎉 Setup completed successfully!")
    print("\n📖 Next steps:")
    print("1. Run the application: python run.py")
    print("2. Or run directly: streamlit run app.py")
    print("3. Open your browser to http://localhost:8501")
    print("\n📚 Read README.md for detailed usage instructions")

if __name__ == "__main__":
    main()
