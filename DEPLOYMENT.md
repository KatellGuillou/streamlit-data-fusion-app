# 🚀 Deployment Guide

This guide explains how to deploy your Data Fusion Streamlit Application to various platforms.

## 📋 Prerequisites

- Python 3.8 or higher
- Git repository with your code
- Required packages (see requirements.txt)

## 🌐 Deployment Options

### 1. Streamlit Cloud (Recommended)

**Free hosting for Streamlit apps**

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Add Streamlit Data Fusion App"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file path: `Hackathon/app.py`
   - Click "Deploy"

3. **Configuration**:
   - App URL: `https://your-app-name.streamlit.app`
   - Automatic updates on git push
   - Free tier available

### 2. Heroku

**Popular cloud platform**

1. **Create Heroku app**:
   ```bash
   heroku create your-app-name
   ```

2. **Add Procfile**:
   ```
   web: streamlit run Hackathon/app.py --server.port=$PORT --server.address=0.0.0.0
   ```

3. **Deploy**:
   ```bash
   git push heroku main
   ```

### 3. Railway

**Modern deployment platform**

1. **Connect GitHub**:
   - Go to [railway.app](https://railway.app)
   - Connect your GitHub repository
   - Select the repository

2. **Configure**:
   - Build command: `cd Hackathon && pip install -r requirements.txt`
   - Start command: `cd Hackathon && streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

### 4. Docker Deployment

**Containerized deployment**

1. **Create Dockerfile**:
   ```dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   COPY Hackathon/requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY Hackathon/ .
   
   EXPOSE 8501
   
   CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
   ```

2. **Build and run**:
   ```bash
   docker build -t data-fusion-app .
   docker run -p 8501:8501 data-fusion-app
   ```

### 5. Local Development

**For testing and development**

1. **Navigate to Hackathon folder**:
   ```bash
   cd Hackathon
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run application**:
   ```bash
   streamlit run app.py
   ```

4. **Access**: http://localhost:8501

## 🔧 Configuration

### Environment Variables

Set these in your deployment platform:

```bash
# Optional: Custom configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

### File Size Limits

- **Streamlit Cloud**: 1GB total
- **Heroku**: 500MB slug size
- **Railway**: 1GB storage

### Performance Optimization

1. **Data Processing**:
   - Use smaller datasets for testing
   - Implement data chunking for large files
   - Add progress bars for long operations

2. **Memory Management**:
   - Clear session state when needed
   - Use `st.cache` for expensive operations
   - Monitor memory usage

## 📊 Monitoring

### Health Checks

Add to your app for monitoring:

```python
# Add to app.py
@st.cache
def health_check():
    return {"status": "healthy", "timestamp": datetime.now()}

# Add health endpoint
if st.sidebar.button("Health Check"):
    st.json(health_check())
```

### Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Use in your app
logger.info("Data processing started")
```

## 🛠️ Troubleshooting

### Common Issues

1. **Port Issues**:
   - Ensure port is configurable via environment variable
   - Use `$PORT` for cloud platforms

2. **Memory Issues**:
   - Reduce file size limits
   - Implement data chunking
   - Clear session state regularly

3. **Dependency Issues**:
   - Pin package versions in requirements.txt
   - Test locally before deployment

### Debug Mode

```python
# Add to app.py for debugging
import streamlit as st

if st.sidebar.checkbox("Debug Mode"):
    st.write("Session State:", st.session_state)
    st.write("Available Memory:", psutil.virtual_memory())
```

## 📈 Scaling

### For High Traffic

1. **Load Balancing**: Use multiple instances
2. **Caching**: Implement Redis for session storage
3. **CDN**: Use CloudFlare for static assets
4. **Database**: Store processed data in database

### Cost Optimization

1. **Streamlit Cloud**: Free tier for public repos
2. **Heroku**: Use eco dynos for cost savings
3. **Railway**: Pay-per-use pricing
4. **Self-hosting**: Use VPS for long-term projects

## 🔒 Security

### Best Practices

1. **Environment Variables**: Store secrets securely
2. **File Validation**: Validate uploaded files
3. **Rate Limiting**: Implement request limits
4. **HTTPS**: Always use secure connections

### Example Security Config

```python
# Add to app.py
import streamlit as st

# File size limit
MAX_FILE_SIZE = 200 * 1024 * 1024  # 200MB

def validate_file(file):
    if file.size > MAX_FILE_SIZE:
        st.error("File too large!")
        return False
    return True
```

## 📝 Maintenance

### Regular Tasks

1. **Update Dependencies**: Monthly security updates
2. **Monitor Performance**: Check response times
3. **Backup Data**: Regular data backups
4. **User Feedback**: Collect and address issues

### Version Control

```bash
# Tag releases
git tag -a v1.0.0 -m "Initial release"
git push origin v1.0.0
```

---

**Happy Deploying! 🚀**
