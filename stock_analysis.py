"""
Stock Market Analysis for Nifty 50- The Dataset is from 1st January 2000 to 31st March 2021.
The Dataset has been from Kaggle- https://www.kaggle.com/rohanrao/nifty50-stock-market-data
"""

import glob as g
import seaborn as sns
import plotly.graph_objects as go
import pandas as pd
sns.set_style(style='white')


def stocks():
    # Reading and storing all csv files into a single dataframe
    # Data preprocessing steps

    df = pd.concat(map(pd.read_csv, g.glob('Nifty-50-dataset/*.csv')))
    # print(df.head())
    # print(df.columns)
    # print(df.shape)
    # print(df.info)
    # print(df.isnull().sum())
    trades_mean = df['Trades'].mean()
    # print('Mean of trades', trades_mean)
    # print(df['Trades'].fillna(trades_mean, inplace=True))

    deliverables_mean = df['%Deliverble'].mean()
    # print('Deliverables of Mean', deliverables_mean)
    # print(df['%Deliverble'].fillna(deliverables_mean, inplace=True))

    del_volumes_mean = df['Deliverable Volume'].mean()
    # print('Mean of Deliverable Volume', del_volumes_mean)
    # print(df['Deliverable Volume'].fillna(del_volumes_mean, inplace=True))

    # print(df.isnull().sum())

    # Selecting only last 5 days for getting the top 3 companies
    df.Date = pd.to_datetime(df.Date, format="%Y-%m-%d")
    df = df[(df['Date'] > pd.Timestamp(2021, 3, 23))]

    # profit calculation and getting the Top 3 companies based on highest profit.
    df['lowest_cumulative_price'] = df.Close.cummin()
    df['highest_profit'] = df.Close - df['lowest_cumulative_price']
    df = df.sort_values('highest_profit', ascending=False).groupby('Symbol').head(3)
    top3_df = df.drop_duplicates(subset=['lowest_cumulative_price', 'Symbol'], keep='first')
    top3_df = top3_df.reset_index(drop=True)
    print(top3_df.head(50))
    # top3_df = top3_df.to_csv('Stock-Market-Data.csv', index=False, header=True, encoding='utf-8')
    print('Results saved to CSV file')
    return top3_df


def plot_stocks(top3_df):
    # Volume over time
    fig = go.Figure([go.Scatter(x=top3_df.index, y=top3_df['Volume'])])
    fig.update_layout(autosize=False, width=1000, height=500, template='simple_white', title='Volume over time')
    fig.update_xaxes(title="Date")
    fig.update_yaxes(title="Volume")
    fig.write_image("static/volume-over-time1.png")

    # Companies Stocks opened at
    companies = go.Figure([go.Scatter(x=top3_df['Symbol'], y=top3_df['highest_profit'])])
    companies.update_layout(autosize=False, width=1000, height=500, template='simple_white', title='Companies and '
                                                                                                   'their highest '
                                                                                                   'profit')
    companies.update_xaxes(title="Companies")
    companies.update_yaxes(title="highest Profit")
    companies.write_image("static/highest-profit.png")


if __name__ == "__main__":
    plot_stocks(stocks())
