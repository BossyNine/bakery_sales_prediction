# Baseline Model

## Erstellen eines Scripts für ein 'BaselineModel' inklusive Erweiterung, um die Performance des Modells zu verbessern. (Skript bisher in 0_DataPreparation hinterlegt)



**Feature Selection**

Our initial feature set was comprehensive and only included 'Umsatz ~ Temperatur * Bewoelkung + C(Warengruppe)' (0.686) and then '+ C(season) (0.697). We chose these features because they had higher correlation values in the correlation matrix together with the sales column than others and therefore could potentially influence the target variable.

During the process of improving the R-squared value, we used try-and-error method and tried different combinations to improve the model and get a higher R-squared. The variables were added progressively to observe changes in R-squared values. It turned out that interaction terms between variables could capture the combined effect of mutliple features on our target value and improved the result. For example, the combination of all the included weather variables as interacting terms and then also the "Warengruppe"-"Wochentag"-"Monat"- interaction helped the model perform as well. 

By gradually adding features and interaction terms, we observed an increase in R-squared value, indicating the incremental contribution of each set of features to the model’s explanatory power and we ended with an R-squared value of 0.869. This was when the value did not improve so much more when adding more variables or changing to more interaction terms, but the computational costs rose very fast so that we decided to stop.

In the end, we used the following formula including the following features:

    Continuous variables: Temperatur, Niederschlag, Bewoelkung, Windgeschwindigkeit, temp_dv
    Categorical variables: Wettercode, Warengruppe, weekday, month, day_month, year, season, Ferientage, Feiertage, KielerWoche

    Formula: 'Umsatz ~ Temperatur * Niederschlag * C(Wettercode) * Bewoelkung * Windgeschwindigkeit * temp_dv + C(Warengruppe) * C(weekday) * C(month) + C(day_month) + C(year) + C(season) + C(Ferientage) + C(Feiertage) + C(KielerWoche)'



**Implementation**

We implemented the linear regression model using OLS from statsmodels library.
We set up the regression formula gradually and slowly fitted the model as described above.

Please find the accoridng notebook containing the model code here: 
"/workspaces/bakery_sales_prediction/2_BaselineModel/BaseLine_LinearRegression.ipynb"


**Evaluation**

OLS Regression Results:                           
==============================================================================
Dep. Variable:                 Umsatz   R-squared:                       0.869
Model:                            OLS   Adj. R-squared:                  0.854
Method:                 Least Squares   F-statistic:                     54.82
Date:                Tue, 25 Jun 2024   Prob (F-statistic):               0.00
Time:                        18:16:37   Log-Likelihood:                -50165.
No. Observations:                9334   AIC:                         1.024e+05
Df Residuals:                    8322   BIC:                         1.096e+05
Df Model:                        1011                                         
Covariance Type:            nonrobust   

R-squared:
The R-squared and Adjusted R-squared metrics indicate the proportion of variance in the dependent variable explained by the model. The R-squared of 0.869 means that 86.9% of the variance in "Umsatz" is explained by our model which we are very satisfied with. Adjusted R-squared accounts for the number of predictors and adjusts for the degrees of freedom and is very good as well with 0.854.

F-statistic:
The F-statistic tests the overall significance of the model and the high value, together with a very low p-value (<< 0.05) (Prob (F-statistic) indicates that the model is statistically significant. It seems a bit strange that the p-value is 0.00 though.

Coefficient Significance:
The t-values anf p-values of the individual coefficients suggest that some weather codes are less significant and some more. Mostly codes that have to do with snowfall or fog, so rather seldom weather phenomenons, have a lower f- and higher p-value and are therefore very weak predctors of our target variable.
Somehow the 'year' variable show very low p-values and thereby higher significance. That could be because of the inflation, that every year differs to the one before in the height of the sales.
Holidays are very important for the forecast - "Feriantage" has a f-value of 14.146 and p-value 0.00 and "Feiertage" 9.227/0.00 and also the Kieler Woche identifies as an important event with  6.974/0.00.
For the "Warengruppe*Wochentag" it can be observed that especially breadrolls (10.653/0.000), croissants (4.910/0.000), pastries (5.395/0.000), and cake (4.467/0.000) have high significance together with weekend.
For the cobination of "Warengruppe*Monat" mostly groups 2 (bredrolls) and 3 (croissants) have significant values. 

Cross validation:
The result from a cross validation shows that the model seems to be robust and not overfitted since the R-squared values from the validation are at similar values and not so much lower than the R-squared from the model. The mean cross-validation R-squared (0.816) is only 0.053 lower than the one of the model (0.869) which is very good.

    Cross-Validation R-squared Scores: [0.7831129910709567, 0.8690670919135706, 0.856027214024433, 0.7263895318087165, 0.8454007611017007]
    Mean Cross-Validation R-squared: 0.8159995179838754

We resume our baseline model is valid and significant and is a good start for the neural network implementation.