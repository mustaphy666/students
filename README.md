# 🎓 Student Performance Prediction Web App

> **A machine learning web application that predicts student writing scores with 95% accuracy based on demographic and academic factors.**

---

## 🧠 What It Does

Teachers and schools often struggle to identify at-risk students early enough to intervene. This app uses a trained regression model to predict a student's writing score based on key factors — giving educators actionable insights before exam day.

**Input factors:**
- Gender
- Race / Ethnicity group
- Parental level of education
- Lunch type (standard vs free/reduced)
- Test preparation course completion

**Output:**
- Predicted writing score (0–100)
- Visual breakdown of contributing factors

---

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| Prediction Accuracy | **95%** |
| Algorithm | Scikit-learn Regression |
| Technique | Feature Engineering |
| Target Variable | Student Writing Score |

---

## 🏗️ Project Structure

```
student-performance-predictor/
├── data/
│   └── StudentsPerformance.csv   # Dataset
├── notebooks/
│   └── exploration.ipynb         # EDA and model training
├── model/
│   ├── train.py                  # Training pipeline
│   └── model.pkl                 # Saved model
├── app.py                        # Streamlit web app
├── requirements.txt
└── README.md
```

---

## 🧰 Tech Stack

| Component | Technology |
|-----------|-----------|
| Machine Learning | Scikit-learn |
| Feature Engineering | Pandas, NumPy |
| Web App | Streamlit |
| Visualisation | Matplotlib, Seaborn |
| Language | Python 3.11+ |

---

## 🛠️ Setup

```bash
git clone https://github.com/mustaphy666/student-performance-predictor.git
cd student-performance-predictor
pip install -r requirements.txt
streamlit run app.py
```

---

## 📁 Dataset

Uses the [Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams) dataset from Kaggle.

---

## 👤 Author

**Saheed Mustapha Olatunji**
- GitHub: [@mustaphy666](https://github.com/mustaphy666)
- LinkedIn: [mustapha-saheed](https://www.linkedin.com/in/mustapha-saheed)
