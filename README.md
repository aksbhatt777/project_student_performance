# 📚 Student Performance Predictor

[![Deployed on Render](https://img.shields.io/badge/Deployed-Render-blue?logo=render)](https://project-student-performance.onrender.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit)](https://streamlit.io/)

An end-to-end **production ML pipeline** predicting student math scores based on demographic and academic features. Built with modular components, containerized with Docker, and deployed with auto-deploy on Render.

🔗 **Live Demo**: [project-student-performance.onrender.com](https://project-student-performance.onrender.com/)

---

## 🎯 Overview

This project demonstrates a complete **MLOps-ready workflow** for student performance prediction. It takes student data (gender, race/ethnicity, parental education, lunch type, test preparation, reading/writing scores) and predicts their math score with **92% R²** accuracy.

### ✨ Key Features

- 🔮 **Real-time Predictions** – Instant math score predictions via Streamlit UI
- 🏗️ **Modular Architecture** – Separate components for ingestion, transformation, training, and prediction
- 📊 **7 ML Models Evaluated** – XGBoost, CatBoost, Random Forest, Gradient Boosting, AdaBoost, Decision Tree, Linear Regression
- 🎯 **Hyperparameter Tuning** – Grid search optimization for best model selection
- 🐳 **Docker Containerization** – Consistent environment across development and production
- 🚀 **Auto-Deployment** – GitHub → Render auto-deploy pipeline
- 📝 **Logging & Exception Handling** – Production-grade error tracking
- 💾 **Artifact Management** – Versioned model and preprocessor pickles


### Data Flow
Raw Data → Data Ingestion → Data Transformation → Model Training → Prediction Pipeline → Web UI


### Preprocessing Pipeline

| Feature Type | Pipeline Steps |
|--------------|----------------|
| **Numerical** (Reading Score, Writing Score) | SimpleImputer (median) → StandardScaler |
| **Categorical** (Gender, Race, Education, Lunch, Test Prep) | SimpleImputer (most_frequent) → OneHotEncoder → StandardScaler (with_mean=False) |

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| **Language** | Python 3.10 |
| **ML Framework** | Scikit-learn, XGBoost, CatBoost |
| **Data Processing** | Pandas, NumPy, Scipy |
| **Web Interface** | Streamlit |
| **Containerization** | Docker |
| **Deployment** | Render |
| **Version Control** | Git, GitHub |
| **Artifact Storage** | Pickle (model.pkl, preprocessor.pkl) |

---

## 📊 Model Performance

| Model | R² Score |
|-------|----------|
| **Gradient Boosting** | **0.92** ✅ |
| CatBoost | 0.91 |
| XGBoost | 0.89 |
| Random Forest | 0.85 |
| AdaBoost | 0.82 |
| Decision Tree | 0.78 |
| Linear Regression | 0.65 |

> *Gradient Boosting was selected as the best performing model with 92% R² accuracy.*

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- pip
- Git
- Docker (optional)

### Local Setup

```bash
# Clone the repository
git clone https://github.com/aksbhatt777/project_student_performance.git
cd project_student_performance

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Train the model (generates artifacts)
python train_model.py

# Run Streamlit app locally
streamlit run app.py

