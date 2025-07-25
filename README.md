# AI Perceptions — OLS & ANOVA

This repository contains an analytical exploration of public perceptions about Artificial Intelligence (AI) applied in job using the **AI questions dataset** from the [European Union Open Data Portal](https://data.europa.eu/data/datasets/s3222_101_4_sp554_eng?locale=en). The dataset consists of survey responses collected by the EU, focusing on attitudes, awareness, and opinions regarding AI.

## Project Overview

The EU's prior work with this dataset has been limited to descriptive statistics. This project expands on their analysis by applying statistical modeling techniques such as **Ordinary Least Squares (OLS) regression** and **Analysis of Variance (ANOVA)** to uncover deeper insights and relationships within the data.

### Goals

- Move beyond descriptive analysis to inferential statistics
- Identify significant factors that shape public perceptions about AI
- Demonstrate the use of OLS and ANOVA in social sciences data analysis

## Data Source

- **Dataset Title:** AI questions from Eurobarometer survey
- **Access Link:** [EU Open Data Portal](https://data.europa.eu/data/datasets/s3222_101_4_sp554_eng?locale=en)
- **Description:** The dataset contains survey responses from EU citizens on various questions related to artificial intelligence, technology adoption, trust, and perceived risks and benefits.

## Methodology

1. **Data Cleaning & Preparation:**  
   Handling missing values by using KNNImputer and created a new organized dataset for analysis.

2. **Inferential Statistics:**  
   - **OLS Regression:** To model how the education level of a country predict perceptions about AI.
   - **ANOVA:** To assess whether perceptions about AI differ significantly across education levels.
   - **OLS vs ANOVA**
     - ANOVA checks if average opinions about AI differ between countries with different education levels.
     - OLS regression goes further. It tells us how much each education level (like Master's or Doctorate) affects those opinions.
     
We work with country-level data, not individuals. Both the AI perception and education values are proportions (e.g., 0.65 = 65% of people asked from that country).
These methods help us find meaningful patterns, not just describe the data.

## Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/ersa-mezuraj9/AI-Perceptions---OLS-ANOVA.git
    ```

2. Download the dataset from the [EU Open Data Portal](https://data.europa.eu/data/datasets/s3222_101_4_sp554_eng?locale=en) and place it in the project directory as specified in the analysis notebooks/scripts.

3. Run the analysis scripts

## Requirements

- Python 3.x
- pandas
- numpy
- statsmodels
- matplotlib / seaborn (for visualization)

## Results

The project will provide:

- OLS regression models identifying significant predictors of AI perceptions
- Interpretation of findings in the context of public policy and AI adoption in job

For detailed statistics and regression outputs, see [`results_summary.md`](results_summary.md)
For correlation and standard deviation analysis, see [`correlation_std_analysis.md`](correlation_std_analysis.md)

## License

This project is for academic and research purposes. The original dataset is © European Union, used under their open data license.

## Acknowledgements

- European Commission for providing the dataset via the EU Open Data Portal.
- Eurobarometer survey organizers and participants.

---

Feel free to open issues or contribute improvements!
