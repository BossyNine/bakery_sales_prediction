import pandas as pd
import statsmodels.formula.api as smf

def main():
    path = '../sourcedata/cleaned_data/5_has_wettercode.csv'

    # Load data
    df = pd.read_csv(path)

    # Make the linear model

    model = smf.ols('Umsatz ~ Temperatur + C(Wettercode)', data=df).fit()

    # Print the summary
    print(model.summary())

    # save the summary to a text file
    with open('./results/linear_regression_summary.txt', 'w') as f:
        f.write(str(model.summary()))

    # save the model
    model.save('./results/linear_regression.pickle')


if __name__ == '__main__':
    main()
