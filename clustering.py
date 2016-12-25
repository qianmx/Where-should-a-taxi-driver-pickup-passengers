import pandas as pd
from sklearn.cluster import KMeans
from collections import Counter
import numpy as np
from sklearn import preprocessing


def top5_filter(x, index_lst):
    if x in index_lst:
        return True
    else:
        return False


def most_pickup_location(df):
    # kmeans analysis
    X = df[['Pickup_longitude', 'Pickup_latitude']]
    k = 20
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    cluster = kmeans.predict(X)
    counter = Counter(cluster).values()
    top5_pickup_index0 = np.array(counter).argsort()[-5:]
    top5_pickup_index = list(reversed(top5_pickup_index0))
    X_label = X.join(pd.DataFrame(cluster))
    X_label.columns = ['Pickup_longitude', 'Pickup_latitude', 'Cluster']
    # output top 5 clusters to csv
    df1 = X_label[X_label['Cluster'].apply(lambda x: top5_filter(x, top5_pickup_index))]
    df1.to_csv('pickup_location.csv', header=0)


def lucrative_location(df):
    # create features
    '''
    Assume lucrative trips as those generating the highest fare for least amount time spent
    , and create a feature- fare per minute
    '''
    pickup_time = df['lpep_pickup_datetime'].apply(pd.to_datetime)
    dropoff_time = df['Lpep_dropoff_datetime'].apply(pd.to_datetime)
    trip_time = (dropoff_time - pickup_time) / np.timedelta64(1, 'm')
    fare_per_time = df['Total_amount'] / trip_time
    longitude = df.loc[:, ['Pickup_longitude']]
    latitude = df.loc[:, ['Pickup_latitude']]
    X = pd.concat([longitude, latitude, fare_per_time], axis=1)
    X.columns = ['longitude', 'latitude', 'fare_per_time']
    X = X[np.isfinite(X['fare_per_time'])]
    print X
    X = X[(X['latitude'] != 0) & (X['longitude'] != 0)]
    X = X.reset_index(drop=1)
    # kmeans analysis
    X1 = preprocessing.StandardScaler().fit_transform(X)
    k = 10
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X1)
    cluster = kmeans.predict(X1)
    X_label = pd.DataFrame(X).join(pd.DataFrame(cluster))
    X_label.columns = ['longitude', 'latitude', 'fare_per_time', 'Cluster']
    far_per_cluster = X_label.groupby(['Cluster'], sort=False)['fare_per_time'].mean()
    far_per_cluster = far_per_cluster.sort_index()
    top5_money_index0 = np.array(far_per_cluster).argsort()[-5:]
    top5_lucrative_index = list(reversed(top5_money_index0))
    # output top 5 clusters to csv
    df2 = X_label[X_label['Cluster'].apply(lambda x: top5_filter(x, top5_lucrative_index))]
    df2.to_csv('lucrative_location.csv', header=0)

if __name__ == "__main__":
    taxi_df = pd.read_csv('green_tripdata_2016-03.csv')
    most_pickup_location(taxi_df)
    lucrative_location(taxi_df)





