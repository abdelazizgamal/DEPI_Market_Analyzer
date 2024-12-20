
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
![Project Workflow](Images/WorkFlow.png "WorkFlow")  

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
### **Project System modules**
![Project Solution diagram](Images/Solution_block_diagram.png "Solution block diagram")  
  

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
![Solution Architecture](Images/Solution_Architecture.png "Solution Architecture Diagram")  

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

To simplify the process, you can use the provided shell scripts to manage the servers:

1. **Run the Machine Learning Server**  
   Execute the following script to initialize the ML server:
   ```bash
   ./initialize_ml_server.sh
   ```
2. **Run the Web Server**  
   Execute the following script to start the web server:
   ```bash
   ./initialize_web_server.sh
   ```
3. **Stop All Servers**  
   To stop all running servers, use:
   ```bash
   ./kill_servers.sh
   ```

---

## 🌟 **Key Insights**
### Dashboard Screenshots
#### Home Page  
![Home Page](Images/home.png "Dashboard Home")

#### Sentiment Analysis & Ad Creator  
![Sentiment Analysis](Images/Sentiment_Analyzer.png "Sentiment Analysis")
![Insights Result](Images/Insights.png "Sentiment Analysis Results")
![AD Generation](Images/ad.png "Ad")



#### Price Predictors  
![Price Predictor](Images/Price_Predictor.png "Price Prediction Screenshot")
![Prediction_graph](Images/Prediction_graph.png "Prediction graph Screenshot")


---

## 🔮 **Future Enhancements**
- **Enhanced Web Scraping**: Support for paginated reviews and multiple platforms.
- **Advanced Predictions**: Incorporating external factors like social trends.
- **Trend Discovery**: Using AI to identify emerging product trends.

---

## 🤝 **Contributors**
- Abdelaziz Gamal Ali Mohamed
- Osama Salaheldin Farag Abdulmottaleb
- Ahmad Mohamed Ibrahim Mostafa  
- Moataz Gamal Ali Mohamed  

---

## 📜 **Acknowledgments**
Special thanks to **Digital Egypt Pioneers Initiative** and **Egyptian Ministry of Communications** for their support. Shoutout to our mentor **Mohammed Bekhit** for invaluable guidance!

