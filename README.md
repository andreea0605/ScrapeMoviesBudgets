# 🎬 Movie Budget and Revenue Analysis

This project scrapes budget and revenue data for movies from [The Numbers](https://www.the-numbers.com/movie/budgets/all), cleans the dataset, and analyzes trends related to movie production budgets and box office performance.

## 📂 Project Structure

- `main.py` – Python script using **Selenium** and **BeautifulSoup** to scrape data across multiple pages, and save it as a CSV file.
- `seaborn_and_linear_Regression.ipynb` – Jupyter notebook for:
  - cleaning and preparing the dataset
  - handling missing or malformed data (e.g. `NaT` dates)
  - converting column types (e.g. `Release Date` to datetime, budgets to integers)
  - performing visual and statistical analysis (e.g. budget vs revenue)
  - making some predictions using linear regression from skitlearn to see the relationship between production budget and worldwide gross (only for learning purpose because they aren't related too good as it can be saw in the final chart)

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/movie-budget-analysis.git
cd movie-budget-analysis
