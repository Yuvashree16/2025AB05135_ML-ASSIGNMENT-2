**2025AB05135_ML-ASSIGNMENT-2**
Implement multiple classification models - Build an interactive Streamlit web application to demonstrate your models - Deploy the app on Streamlit Community Cloud

**a. Problem statement**
The objective of this project is to build and compare multiple machine learning classification models to predict whether an individual's annual income exceeds $50,000 based on demographic and employment-related attributes.
The task is formulated as a supervised binary classification problem, where the target variable indicates whether income is <=50K or >50K.

The project includes:
>Implementing six classification algorithms
>Evaluating performance using multiple metrics
>Comparing model performance
>Deploying the best-performing models using a Streamlit web application

**b. Dataset description**
The Adult Income Dataset is a tabular census dataset collected to help predict whether an individual’s annual income is greater than $50,000 or not based on personal and demographic attributes.It consists of demographic and employment-related features such as:
>Age
>Education
>Occupation
>Marital status
>Workclass
>Hours-per-week
>Capital gain
>Capital loss
>The dataset contains more than 30,000 instances and over 12 features, satisfying the assignment requirements.
>The target variable indicates whether an individual's annual income exceeds $50,000.

**c. Models used:**
Comparison Table with the evaluation metrics calculated for all the 6 models is below:
<img width="494" height="184" alt="comparison table" src="https://github.com/user-attachments/assets/f7490b4d-9cde-4ee1-99d1-ee5afce3ffe7" />
_________________________________________________________________________________________________
|ML Model Name              |Accuracy  | AUC       |Precision |Recall    |F1         |MCC       |
-------------------------------------------------------------------------------------------------
|Logistic Regression        |0.827209  |0.854805   |0.707300  |0.448472  |0.548904   |0.466408  |
|Decision Tree              |0.815437  |0.747748   |0.603661  |0.619214  |0.611339   |0.466408  |
|kNN                        |0.833453  |0.855508   |0.658385  |0.601747  |0.628793   |0.522592  |
|Naive Bayes                |0.806940  |0.860433   |0.681329  |0.331441  |0.445946   |0.378480  |
|Random Forest (Ensemble)   |0.863548  |0.911861   |0.741058  |0.642358  |0.688187   |0.603937  |
|XGBoost (Ensemble)         |0.876241  |0.930469   |0.767707  |0.676856  |0.719424   |0.642529  |
-------------------------------------------------------------------------------------------------
Observations on the performance of each model on the chosen dataset.
_______________________________________________________________________________________________________________________________________________________________________________
|**ML Model Name           | Observation about model performance**                                                                                                            |
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Logistic regression: Logistic Regression performed well and provided stable results. It achieved balanced precision and recall, indicating that the dataset has a reasonably linear decision boundary. However, its performance was slightly lower compared to ensemble models, suggesting that more complex patterns exist in the data.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Decision Tree: The Decision Tree model captured non-linear relationships effectively. However, it showed signs of overfitting when compared to Logistic Regression, as indicated by slightly fluctuating evaluation metrics. Performance depended heavily on tree depth.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
kNN : KNN performed moderately well but was sensitive to feature scaling and the choice of k value. It required more memory since it stores the entire training dataset. Its performance was competitive but not superior to ensemble methods.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Naive Bayes : Naive Bayes performed reasonably well despite its strong independence assumption. However, because some features in the dataset are correlated, its performance was slightly lower than other models. It was computationally efficient and fast.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Random Forest (Ensemble): Random Forest significantly improved performance over single Decision Trees by reducing variance through averaging multiple trees. It achieved high accuracy and better generalization, indicating strong ability to capture complex feature interactions.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
XGBoost (Ensemble) : XGBoost delivered the best overall performance among all models. It handled feature interactions and class imbalance effectively. Due to boosting, it minimized errors sequentially, resulting in improved AUC and F1 scores. It demonstrated strong predictive capability on this dataset.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Model File
**The trained model file were too large for GitHub.** to get the uncomressed model files,
Download it here: [Download all Models](https://drive.google.com/drive/folders/1usMhtuANr2nzEytmf0QbsbF9qoTBTlXi?usp=sharing)
After downloading, place the file inside the `model/` folder.


