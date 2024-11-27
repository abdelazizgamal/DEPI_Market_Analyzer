
# 🛠️ **Pioneers AI Market Analyzer** 🌟

**Revolutionizing market analysis with AI-driven insights!**  
This toolkit combines advanced data scraping, sentiment analysis, demand and price predictions, and ad creation to empower businesses in making informed decisions.

---

## 🚀 **Features**
- **🔍 Sentiment Analyzer**: Extracts customer sentiments from reviews.
- **📊 Price Predictor**: Forecasts product prices based on historical data.
- **📈 Demand Predictor**: Predicts future demand trends.
- **🖋️ Ad Creator**: Generates compelling ads tailored to customer sentiments.
- **📂 Data Insights**: Interactive visualizations and dashboards for better decision-making.

---
## 🏗️ **Project Organization**

The project is divided into distinct stages, as outlined below:  

1. **Web Scraping**: Extracts product data from e-commerce websites (currently Amazon US).  
2. **Sentiment Analysis**: Analyzes customer reviews to extract sentiments.  
3. **Insight Extraction**: Summarizes key pros and cons from reviews.  
4. **Prediction Models**: Uses historical price and demand data for forecasting.  
5. **Ad Creation**: Generates customizable advertisements based on extracted insights.  
6. **Dashboard**: Displays analysis results interactively.  
7. **Documentation**: Comprehensive project documentation, GitHub README, and presentations.

### **Project Workflow**
![Project Workflow](https://drive.google.com/file/d/1pCKPUo5CiFL2zcT7yNnrTusJpI3hydXp/view?usp=drive_link)  

---

## 🧠 **How It Works**

### 1️⃣ **Data Collection**  
💻 A web scraper collects product data and customer reviews from e-commerce platforms.  

### 2️⃣ **Analysis & Insights**  
🤖 Sentiment Analyzer and Insight Extractor process reviews, identifying strengths, weaknesses, and generating summaries.  

### 3️⃣ **Forecasting**  
📅 Predict future prices and demand trends with **Prophet**, a robust time-series model.  

### 4️⃣ **Ad Generation**  
📢 Create engaging and customizable ads based on insights derived from customer reviews.  

---

## 🛠️ **Technology Stack**
- **Programming Language**: Python 🐍
- **Libraries**: 
  - [Scrapy](https://scrapy.org) for web scraping.
  - [Transformers](https://huggingface.co) for sentiment analysis.
  - [Prophet](https://facebook.github.io/prophet) for demand and price predictions.
- **Cloud**: AWS (EC2, S3, CloudWatch, CloudTrail) ☁️
- **Frontend**: Streamlit for interactive dashboards.

---

## 📋 **Architecture Overview**
![Solution Architecture](images/architecture_diagram.png "Solution Architecture Diagram")  

---

## 💻 **Getting Started**

### Prerequisites
- Python 3.8+
- Virtual Environment (recommended)
- AWS Account (optional for cloud deployment)

### Installation
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo-link
   cd your-repo
   ```

2. Set up a virtual environment:  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

### Running the Modules
- **Web Server**:  
  ```bash
  streamlit run streamlit/home.py
  ```
- **Machine Learning Server**:  
  ```bash
  python ml_server.py
  ```
- **Price Predictor**:  
  ```bash
  python price_predictor.py
  ```

---

## 🌟 **Key Insights**
### Dashboard Screenshots
#### Home Page  
![Home Page](images/home_page.png "Dashboard Home")

#### Sentiment Analysis & Ad Creator  
![Sentiment Analysis](images/sentiment_analysis.png "Sentiment Analysis Results")

#### Price Predictor  
![Price Predictor](images/price_predictor.png "Price Prediction Screenshot")

---

## 🔮 **Future Enhancements**
- **Enhanced Web Scraping**: Support for paginated reviews and multiple platforms.
- **Advanced Predictions**: Incorporating external factors like social trends.
- **Trend Discovery**: Using AI to identify emerging product trends.

---

## 🤝 **Contributors**
- Abdelaziz Gamal Ali Mohamed  
- Ahmad Mohamed Ibrahim Mostafa  
- Mahmoud Ahmed Mahmoud Alfakharany  
- Moataz Gamal Ali Mohamed  
- Mohamed Kamal AbdelHamid Ibrahim  
- Osama Salaheldin Farag Abdulmottaleb  

---

## 📜 **Acknowledgments**
Special thanks to **Digital Egypt Pioneers Initiative** and **Egyptian Ministry of Communications** for their support. Shoutout to our mentor **Mohammed Bekhit** for invaluable guidance!

