# Dataset Characteristics

## 1 Introduction
In this chapter, we explored and analyzed the dataset provided by the course. In addition, we extracted and implemented some additional features and investigated their potential impact on the performance of our baseline and final models.


### 2 DataAnalyse_MissingDates.ipynb
In this Jupyter notebook, we checked for days without any sales at all. The output showed that missing days are most likely *Feiertage* when all shops in Germany have closed like Christmas or January, 1st.


### 3 DataAnalyse_MissingValues.ipynb
In this Jupyter notebook, we explained and analyzed the given dataset regarding missing values, their impact and the evaluation of the entire dataset including added features.

The graphical analysis of missinig values in merged dataset (kiwo.csv, umsatzdaten.csv, wetter.csv) showed that

| Variable           | Missingness Pattern                                                                                     |
|--------------------|---------------------------------------------------------------------------------------------------------|
| *Bewoelkung*         | The pattern suggests it might be MAR or MNAR, depending on whether its missingness can be related to other observed variables or itself.         |
| *Temperatur*         | The missingness seems somewhat random but might be MAR if related to other weather variables.                                                |
| *Windgeschwindigkeit*| Similar to *Temperatur*, it could be MAR if missingness correlates with other weather-related data.                                            |
| *Wettercode*         | The large number of missing values suggests it could be MAR, related to other weather data, or MNAR if it is dependent on specific unobserved conditions. |
| *KielerWoche*        | The missing values follow a pattern, which suggests MNAR.                                                                                      |
| *Warengruppe*        | There is no missing data for overall group *Warengruppe*.                                                                                        |
| *Umsatz*             | There is no missing data for overall group *Umsatz*.                                                                                            |


Please note: The missing data for Umsatz und Warengruppe at the end of the dataset suggests that there was simply no data and therefore, we came to the conclusion that these dates are not of interest for our survey.

Additional visualisation like missingness heatmap and dendogram provided the following relationships:

| Variable             | Correlation with Missing Values in Other Variables                                                                 |
|----------------------|---------------------------------------------------------------------------------------------------------------------|
| *Bewoelkung*           | Moderate correlation (0.5) with missing values in *Temperatur* and moderate correlation (0.5) with missing values in *Windgeschwindigkeit*. |
| *Temperatur*           | Perfect positive correlation (1) with missing values in *Windgeschwindigkeit* and weak correlation (0.1) with missing values in *Wettercode*. |
| *Windgeschwindigkeit*  | Weak correlation (0.1) with missing values in *Wettercode*.                                                           |
| *Wettercode*           | Weak correlation (0.1) with missing values in both *Temperatur* and *Windgeschwindigkeit*.                              |
| *KielerWoche*          | Little to no significant correlation with other columns based on missing values.                                    |
| *Warengruppe*          | This group will be inspected separately at a later stage.                                                           |
| *Umsatz*               | This group will be inspected separately at a later stage.                                                           |


### 4 DataAnalyse_Warengruppe_Umsatz.ipynb
In this Jupyter notebook, we explain the cleaning of the given dataset and the evaluation of the entire cleaned dataset including added features. Cleaned dataset excludes dates without weathercode as we assume that weather might have an input in the sales.

To get an overview, we analysed the dataset first : a general overview for all items in *Warengruppe*. We used a bar chart with confidence intervals to display the relationship between the average sales per day of the week. The days of the week in the chart are sorted from Monday to Sunday. In addition, we examined each *Warengruppe* on its own. However, *Warengruppe Saisonbrot* needed some further investigation as the product has been for sale only for certain time periods (resulting in being taken out for the modelling - at least that was the initial plan but ditched at a later stage due to the impact in the overall solution). 

As expected, sales were in general higher at weekends. *Brot* was quite popular during the week as *Broetchen*, *Croissant*,  *Konditorei*, and *Kuchen* performed best on weekends, especially on Sundays. *Saisonbrot* was only sold during November and December (plus a very few days before and after that period). Therefore, the bar chart was only created for those two months as otherwise the confidence interval would have been of not much value.

The heatmap provided further insight:
The sales of Brot, Broetchen, Croissant, and Kuchen are perfectly correlated with each other (correlation coefficient of 1.00). This indicates that the sales patterns for these items are highly similar across weekdays. When the sales of one of these items increase or decrease, the sales of the others follow the same trend. 
Konditorei has a moderate negative correlation with Brot, Broetchen, Croissant, and Kuchen (correlation coefficients of -0.19). This suggests that there is some inverse relationship, indicating that when the sales of Konditorei items increase, the sales of the other items tend to decrease slightly, and vice versa.

### 5 DataAnalyse_Wetter.ipynb
In this Jupyter notebook, we explored *Wetter* and other features like *Bewoelkung*, *Temperatur*, *Wetterklasse*, and *Windgeschwindigkeit* in detail. We generated scatter plots, bar charts, histograms to visualize their dependencies and interactions. In addition, we tried to figure out if there might be some correlation between *Temperatur* and *Umsatz*. Adding additional features helped which are described in more detail in the next Jupyter notebook.  
In the very beginning of the project, first trials with different features for weather have already been explored in a Jupiter notebook (exploring_weather_data.ipynb) and have been kept for the sake of completeness (**[Link](https://github.com/BossyNine/bakery_sales_prediction/blob/main/1_DatasetCharacteristics/exploting_weather_data.ipynb)**).

### 6 DataAnalyse4AdditionalFeatures.ipynb
In this Jupyter notebook, we investigated additional features which might be worth being implemented.  
These features are:

1. *Ferientage*
2. *Niederschlag*
3. *Season*
4. *Temperaturabweichung*

This investigation delivered some useful insights into sales. Sales were in general higher during holidays. In addition, we created bar charts with confidence intervals for the different seasons. As expected, sales in spring and summer would perform better than in autumn and winter. However, rain does not have the expected impact on the average on sales. This might be due to the fact that people living in Kiel are used to rainy days. The evaluation on *Temperatur* seems to be inconclusive. Apparently, one goes shopping when there is a need regardless of the impact of *Temperatur*. However, this conclusion is negotiable.

### 7 Conclusion
These investigations indicated the complexity of the topic in general and specifically helped to clean data and ensure data quality. This process enabled the selection of the most relevant features and simplified the dataset. A better understanding of the data can lead to simpler models that are easier to interpret and faster to train.






