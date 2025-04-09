
# End-to-End Data Analysis & Visualization Project  
### Technologies Used: JSON | Python | Amazon S3 | Snowflake | PowerBI  

---

## 📊 Project Overview  

This project demonstrates a complete data pipeline and analysis workflow, starting from raw JSON data to generating interactive dashboards. The pipeline showcases the integration of modern cloud-based data storage, processing, and visualization tools.

It reflects real-world scenarios of handling unstructured data, transforming it, storing it securely in the cloud, and deriving actionable insights through business intelligence tools.

---

## 🚀 Tools & Technologies  

| Tool        | Purpose                                     |
|-------------|---------------------------------------------|
| JSON        | Raw data source format                     |
| Python      | Data preprocessing, cleaning & transformation |
| Amazon S3   | Cloud storage for structured & raw data   |
| Snowflake   | Cloud data warehousing & querying         |
| PowerBI     | Data visualization & dashboarding         |

---

## 🔄 Workflow Architecture  

1. Extract JSON Data (Simulated Yelp Dataset)
2. Clean & Transform Data using Python
3. Upload Clean Data to Amazon S3
4. Load Data from S3 into Snowflake
5. Query & Analyze Data within Snowflake
6. Visualize Insights using PowerBI Dashboards

---

## 📝 Project Structure  

```
├── data/
│   └── raw/                      # Original JSON data
│   └── processed/                # Cleaned and transformed data
│
├── scripts/
│   ├── extract_data.py          # Load & Explore JSON data
│   ├── transform_data.py        # Clean & structure data
│   ├── upload_s3.py             # Upload to Amazon S3
│   ├── snowflake_loader.py      # Load into Snowflake
│
├── powerbi/                     # PowerBI dashboard files (.pbix)
│
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── .gitignore
```
## Project Architecture 

![Data Diagram](https://github.com/user-attachments/assets/138e012e-977c-4833-96ed-2fc96f87fa63)

---

## ⚙️ Setup Instructions  

1. Clone the Repository  
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Create Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```

3. Install Dependencies  
```bash
pip install -r requirements.txt
```

4. Configure AWS Credentials  
```bash
aws configure
```

5. Run Python Scripts to Process Data  

---

## 📈 PowerBI Visualization  

The PowerBI dashboard showcases:

- Rating distribution
- Customer sentiment trends
- Top categories by review count
- Geographic distribution of reviews
- Time-series trends analysis  

> *Download the .pbix file from `powerbi/` folder and connect it to Snowflake or use the processed dataset.*

---

## ✍️ Author  

*Name*: Kindoli Edward 
*Role*: Data Analyst | Data Engineer | BI Developer  
*GitHub*: [github.com/Kindoli]([https://github.com/Kindoli])
*LinkedIn*: https://www.linkedin.com/in/kindoli-edward-5058544a/

---


