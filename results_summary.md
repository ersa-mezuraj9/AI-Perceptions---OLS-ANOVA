# Education Level and Perceptions of AI

## Summary Conclusion

Overall, the results show that education level plays a significant role in shaping how populations perceive Artificial Intelligence (AI). In general, countries with higher proportions of people holding Master’s or Doctoral degrees tend to have more positive views about the impact and use of AI in the workplace and society. While Master’s education is often linked with more optimistic attitudes toward AI, Doctoral education sometimes predicts greater caution or skepticism, especially regarding decision-making and job security. Bachelor’s education tends to have weaker or less consistent effects. These findings highlight that education shapes the way populations understand and respond to AI technologies.

---
## Multicollinearity Assessment

Variance Inflation Factors (VIF) were calculated to check for multicollinearity among the education predictors:

| Education Level           | VIF    |
|--------------------------|--------|
| Bachelor or equivalent   | 3.40   |
| Master or equivalent     | 7.33   |
| Doctoral or equivalent   | 6.75   |

All VIF values are below 10, indicating that multicollinearity is present but not at a problematic level. While the Master’s and Doctoral education predictors show moderate correlation, they do not affect variance estimates, allowing reliable interpretation of regression coefficients.

## One-Way ANOVA Across Questions

**Hypotheses:**

- **Null Hypothesis (H₀):** All questions have the same mean positive response.
- **Alternative Hypothesis (H₁):** At least one question has a mean positive response that differs significantly.

**ANOVA Results:**

| Source        | Sum of Squares | df   | F-Statistic | p-value        |
|---------------|----------------|------|-------------|----------------|
| Question      | 19.715         | 21   | 150.26      | < 0.001        |
| Residual      | 3.849          | 616  |             |                |

- The p-value is extremely small (`3.55 × 10⁻²²⁶`), far below the standard threshold of 0.05.
- Therefore, we reject the null hypothesis.

There is strong statistical evidence that at least one question has a significantly different mean level of agreement compared to the others.


## OLS & ANOVA Results

### QB1_4 – Perceived Impact of AI at Work

**Survey Question:**  
“In your view, what impact do the most recent digital technologies, including Artificial Intelligence, currently have on your current job?”

**ANOVA:**  
The model is significant (p = 0.0020), showing education levels influence perceptions of AI's impact on work.

**OLS Result:**  
The proportion of Master degree holders is a significant predictor (p < 0.001), with a positive coefficient (0.7621). Countries with higher Master-level populations perceive AI as more positively impactful on jobs.

**Not Significant:**  
Bachelor and Doctoral education levels were not statistically significant.

**Interpretation:**  
In EU countries, a higher proportion of individuals with a Master’s degree is strongly associated with more favorable views of AI’s workplace impact.

---

### QB6_1 – Belief that More Jobs Will Disappear Than Be Created Due to AI and Robots

**Survey Question:**  
“Due to the use of robots and Artificial Intelligence, more jobs will disappear than new jobs will be created.”

**Model Diagnostics:**  
- Initial test detected nonlinearity (Ramsey RESET p = 0.0188).  
- After including quadratic terms, no evidence of nonlinearity (Ramsey RESET p = 0.6575).  
- Residuals are normally distributed, no heteroskedasticity detected.

**ANOVA:**  
Model is significant (p = 0.0469).

**OLS Result:**  
- Doctoral education level is a significant negative linear predictor (coef = –0.0825, p = 0.010).  
- No significant linear or quadratic effects for Bachelor or Master education levels, nor quadratic effects for Doctoral level.

**Interpretation:**  
Countries with higher proportions of Doctoral degree holders tend to disagree more with the idea that AI and robots cause more job losses than gains.

---

### QB6_2 – AI as a Good Thing for Society

**Survey Question:**  
“Robots and Artificial Intelligence are a good thing for society because they help people do their jobs or carry out daily tasks at home.”

**ANOVA:**  
Highly significant (p = 0.0002).

**OLS:**  
Master or equivalent education is a strong positive predictor (p < 0.001; coefficient = 1.2492).

**Not Significant:**  
Other education levels were not significant.

**Interpretation:**  
Countries with more Master’s graduates are more likely to perceive AI as beneficial to society and daily work.

---

### QB6_3 – AI Needs Careful Management

**Survey Question:**  
“Robots and Artificial Intelligence are technologies that require careful management.”

**ANOVA:**  
Significant differences observed (p = 0.0010).

**OLS – Significant Predictors:**
- Bachelor level (p = 0.041)
- Master level (p = 0.026)

**Not Significant:**  
Doctoral level not significant.

**Interpretation:**  
Both Bachelor- and Master-educated populations are more likely to agree that AI requires careful oversight, suggesting general awareness of the risks associated with technology governance.

---

### QB6_4 – AI Replacing Boring or Repetitive Work

**Survey Question:**  
“Artificial Intelligence is necessary as it can do jobs that are seen as boring or repetitive.”

**ANOVA:**  
Model significant (p = 0.0063).

**OLS:**  
Master education is the only significant predictor (p = 0.001; coefficient = 0.9867).

**Not Significant:**  
Bachelor and Doctoral levels not significant.

**Interpretation:**  
Master-educated populations are more likely to view AI as a solution for automating mundane tasks.

---

### QB6_5 – Agreement that Robots and AI Steal People’s Jobs

**Survey Question:**  
“To what extent do you agree that robots and Artificial Intelligence steal people’s jobs?”

**Model Diagnostics:**  
- Residuals are normally distributed (Shapiro-Wilk p = 0.8479).  
- No evidence of nonlinearity (Ramsey RESET p = 0.0666).  
- Heteroskedasticity detected (Breusch-Pagan p = 0.0010), so robust standard errors (HC1) were used.

**ANOVA:**  
Model is not significant (F p = 0.128).

**OLS Result (with robust errors):**  
- No education level is a statistically significant predictor, though Doctoral education shows a marginal negative effect (coef = –0.0457, p = 0.075).

**Interpretation:**  
There is no strong evidence that education level predicts agreement that AI steals jobs, though higher doctoral education might be weakly associated with less agreement.

---

### QB6_6 – Agreement that AI Increases The Pace of Working

**Survey Question:**  
“To what extent do you agree that robots and Artificial Intelligence increase the pace at which workers complete tasks?”

**Model Diagnostics:**  
- Residuals were initially not normally distributed; after removing 2 outliers, residuals became normal (Shapiro-Wilk p = 0.6821).  
- Nonlinearity detected initially; addressed by adding polynomial and interaction terms in the model formula.  
- Other assumptions (heteroskedasticity, linearity) were met.

**ANOVA:**  
Model is highly significant (F p < 0.0001).

**OLS Results:**  
- Significant predictors include:  
  - Master’s education (linear and quadratic terms)  
  - Doctoral education (quadratic and cubic terms)  
  - Interaction between Bachelor’s and Master’s education levels  
- Model explains ~91% of variance (R² = 0.907).

**Interpretation:**  
Nonlinear relationships and interactions between education levels strongly influence agreement with the statement about increased efficiency due to AI and robots.

---

### QB6_7 – AI and Colleagues

**Survey Question:**  
“To what extent do you agree that AI have a negative impact on communication between colleagues?”

**ANOVA:**  
Model is not significant (p = 0.483).

**OLS Result:**  
No education level is a significant predictor.

**Not Significant:**  
Bachelor (p = 0.549), Master (p = 0.461), Doctoral (p = 0.400)

**Model Diagnostics:**  
- Residuals are normally distributed (Shapiro-Wilk p = 0.6019).  
- No evidence of nonlinearity (Ramsey RESET p = 0.5717).  
- Heteroskedasticity detected (Breusch-Pagan p = 0.0292), so robust standard errors (HC1) were used.

**Interpretation:**  
Agreement that AI have a negative impact on communication between colleagues do not appear to vary significantly by education level across countries. The model has low explanatory power and shows no significant associations.

---

### QB6_8 – AI Makes Accurate Decisions

**Survey Question:**  
“Robots and Artificial Intelligence can be used to make accurate decisions in the workplace.”

**ANOVA:**  
Model highly significant (p = 0.0036).

**OLS – Significant Predictors:**
- Master (p = 0.022)
- Doctorate (p < 0.001; coefficient = –8.3759 → very negative impact)

**Not Significant:**  
Bachelor not significant.

**Interpretation:**  
Master-level education correlates with more trust in AI’s decision-making. However, countries with more doctoral graduates are significantly more skeptical about delegating decision-making to AI.

---

### QB11_1 – Protecting Workers’ Privacy

**Survey Question:**  
“How important, if at all, do you think the following rule would be in addressing risks and maximizing the benefits of digital technologies, including AI, in the workplace?  
→ Protecting workers' privacy”

**ANOVA:**  
Model is significant (p = 0.0344).

**OLS Result:**  
No education level is a statistically significant predictor.  

**Not Significant:**  
Bachelor (p = 0.909), Master (p = 0.100), Doctoral (p = 0.199)

**Interpretation:**  
None of the individual education levels significantly predict support for rules protecting workers’ privacy. However, countries with more Master-level graduates may show a tendency toward viewing this rule as more important, though the result is not statistically conclusive.

---

### QB11_2 – Prohibiting Automated Decision-Making

**Survey Question:**  
“How important, if at all, do you think the following rule would be in addressing risks and maximizing the benefits of digital technologies, including AI, in the workplace?  
→ Prohibiting automated decision-making”

**ANOVA:**  
Model is not significant (p = 0.0771).

**OLS Result:**  
A significant quadratic effect was found for the Doctoral education level (p = 0.033), indicating a non-linear relationship.

**Not Significant:**  
Bachelor (p = 0.391), Master (p = 0.914), Doctoral (linear p = 0.382)  
Quadratic terms for Bachelor and Master were also not significant.

**Model Diagnostics:**  
- Residuals are normally distributed (Shapiro-Wilk p = 0.5443).  
- No evidence of nonlinearity (Ramsey RESET p = 0.9083) after using polynomial regression.  
- Heteroskedasticity not detected (Breusch-Pagan p = 0.3695).

**Interpretation:**  
While the overall model is not statistically significant, the squared term for Doctoral education suggests a curved relationship—potentially indicating that both low and high proportions of Doctoral graduates are associated with stronger views on prohibiting automated decision-making, while moderate levels show less concern.

---

### QB11_3 – Limiting Automated Monitoring of People

**Survey Question:**  
“How important, if at all, do you think the following rule would be in addressing risks and maximizing the benefits of digital technologies, including AI, in the workplace?
→ Automated monitoring of people in the workplace?”

**ANOVA:**  
Model is significant (p = 0.0244).

**OLS Result:**  
No education level was a statistically significant predictor.

**Not Significant:**  
Bachelor (p = 0.498), Master (p = 0.190), Doctorate (p = 0.101)

**Interpretation:**  
Although the overall model is significant, none of the education levels individually predict attitudes toward limiting automated monitoring of workers.

---

### QB11_4 – Handling HR Decision-Making

**Survey Question:**  
“How important, if at all, do you think the following rule would be in addressing risks and maximizing the benefits of digital technologies, including AI, in the workplace?
→ Enforcing more transparency in the use of digital technologies to handle HR decision-making”

**ANOVA:**  
Model is not significant (p = 0.0597).

**Not Significant:**  
Bachelor (p = 0.690), Master (p = 0.527), Doctoral (p = 0.525)  
Bachelor² (p = 0.923), Master² (p = 0.627), Doctoral² (p = 0.083)

**Model Diagnostics:**  
- Residuals are normally distributed (Shapiro-Wilk p = 0.7633).  
- No evidence of nonlinearity (Ramsey RESET p = 0.6988) after using polynomial regression.  
- Heteroskedasticity not detected (Breusch-Pagan p = 0.7569).

**Interpretation:**  
No education level, neither linear nor quadratic terms, significantly predicts agreement that it is important enforcing more transparency in the use of digital technologies. The closest to significance is the squared Doctoral term, suggesting a possible weak non-linear trend. However, the model as a whole does not explain much variance in responses.

**Limitations:**  
The model suffers from a small sample size, reducing statistical power. Additionally, education alone may not fully explain country-level attitudes. Including factors like age, GDP ETC., could improve predictive strength.

---

### QB11_5 – Involving Workers in Technology Design

**Survey Question:**  
“How important, if at all, do you think the following rule would be in addressing risks and maximizing the benefits of digital technologies, including AI, in the workplace? 
→ Involve workers and their representatives in the design and adoption of new technologies?”

**ANOVA:**  
Model is significant (p = 0.0118).

**OLS Result:**  
No education level was a statistically significant predictor.

**Not Significant:**  
Bachelor (p = 0.464), Master (p = 0.117), Doctorate (p = 0.095)

**Interpretation:**  
While the model is statistically significant, no individual education level significantly predicts support for involving workers in technology decision-making. Doctoral-level results approach significance.

---

### QB8_1 – AI for Gathering Information on Applicants

**Survey Question:**  
“To what extent do you view the use of AI to gather additional information on applicants for a job positively?”

**ANOVA:**  
Model is not significant (p = 0.1837).

**OLS Result:**  
Doctoral level is a significant positive predictor (p = 0.033).

**Not Significant:**  
Bachelor (p = 0.999), Master (p = 0.167)

**Interpretation:**  
Countries with more individuals holding Doctoral degrees are more likely to view AI-driven applicant data gathering positively, though the overall model is not statistically strong.

**Limitations:**  
The model suffers from a small sample size, reducing statistical power. Additionally, education alone may not fully explain country-level attitudes. Including factors like age, GDP ETC., could improve predictive strength.

---

### QB8_2 – AI for Selecting Applicants

**Survey Question:**  
“To what extent do you view the use of AI for selecting applicants for a job positively?”

**ANOVA:**  
Model is not significant (p = 0.3222).

**OLS Result:**  
No education level was a statistically significant predictor.

**Not Significant:**  
Bachelor (p = 0.891), Master (p = 0.322), Doctorate (p = 0.069)

**Interpretation:**  
No clear relationship was found between education level and support for AI-based hiring decisions.

**Limitations:**  
The model suffers from a small sample size, reducing statistical power. Additionally, education alone may not fully explain country-level attitudes. Including factors like age, GDP ETC., could improve predictive strength.

---

### QB8_3 – AI for Allocating Tasks or Managing Schedules

**Survey Question:**  
“To what extent do you view the use of AI for allocating tasks or managing work schedules positively?”

**ANOVA:**  
Model is not significant (p = 0.0874).

**OLS Result:**  
Master education level is a significant positive predictor (p = 0.032).

**Not Significant:**  
Bachelor (p = 0.275), Doctorate (p = 0.475)

**Interpretation:**  
Respondents from countries with more Master’s graduates show greater support for AI in managing work schedules.

**Limitations:**  
The model suffers from a small sample size, reducing statistical power. Additionally, education alone may not fully explain country-level attitudes. Including factors like age, GDP ETC., could improve predictive strength.

---

### QB8_4 – AI for Processing Personal Worker Data

**Survey Question:**  
“To what extent do you view the use of AI to collect, process, and store workers’ personal data positively?”

**ANOVA:**  
Model is not significant (p = 0.0900).

**OLS Result:**  
Master education level is a significant positive predictor (p = 0.016).

**Not Significant:**  
Bachelor (p = 0.620), Doctorate (p = 0.090)

**Interpretation:**  
Support for AI in processing personal data is higher among countries with more Master-level graduates, though the full model is not statistically significant.

**Limitations:**  
The model suffers from a small sample size, reducing statistical power. Additionally, education alone may not fully explain country-level attitudes. Including factors like age, GDP ETC., could improve predictive strength.

---

### QB8_5 – AI for Improving Worker Safety and Security

**Survey Question:**  
“To what extent do you view the use of AI to improve workers’ safety and security positively?”

**ANOVA:**  
Model is significant (p = 0.0089).

**OLS Result:**  
Master education level is a significant positive predictor (p = 0.031).

**Not Significant:**  
Bachelor (p = 0.282), Doctorate (p = 0.335)

**Interpretation:**  
Countries with more Master-educated individuals are more supportive of AI in enhancing workplace safety.

---

### QB8_6 – AI for Monitoring Workers

**Survey Question:**  
“To what extent do you view the use of AI to monitor workers positively?”

**ANOVA:**  
Model is not significant (p = 0.3876).  
No significant predictors.

**OLS Result:**  
No education level was a statistically significant predictor.

**Not Significant:**  
Bachelor (p = 0.623), Master (p = 0.476), Doctorate (p = 0.098)

**Interpretation:**  
There is no clear relationship between education level and support for AI-based worker monitoring.

**Limitations:**  
The model suffers from a small sample size, reducing statistical power. Additionally, education alone may not fully explain country-level attitudes. Including factors like age, GDP ETC., could improve predictive strength.

---

### QB8_7 – AI for Assessing Worker Performance

**Survey Question:**  
“To what extent do you view the use of AI to assess workers’ performance positively?”

**ANOVA:**  
Model is not significant (p = 0.1541).

**OLS Result:**  
Doctoral education level is a significant positive predictor (p = 0.038).

**Not Significant:**  
Bachelor (p = 0.313), Master (p = 0.431)

**Interpretation:**  
Support for AI in performance assessment is higher in countries with more Doctoral graduates, though the overall model is not statistically strong.

**Limitations:**  
The model suffers from a small sample size, reducing statistical power. Additionally, education alone may not fully explain country-level attitudes. Including factors like age, GDP ETC., could improve predictive strength.

---

### QB8_8 – AI for Automatically Firing Workers

**Survey Question:**  
“To what extent do you view the use of AI to automatically fire workers positively?”

**ANOVA:**  
Model is significant (p = 0.0053).

**OLS Result:**  
Doctoral level is a significant negative predictor (p = 0.037).  
Bachelor-level education shows borderline significance (p = 0.064).

**Not Significant:**  
Master (p = 0.398)

**Interpretation:**  
Higher levels of Doctoral education are associated with more negative views toward AI used for worker termination decisions.
