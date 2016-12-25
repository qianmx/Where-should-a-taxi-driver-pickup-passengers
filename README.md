# Where-should-a-taxi-driver-pickup-passengers
**Key Word: Cluster Analysis, Python, Google Maps API**

##Introduction

This project aims to analyze taxi data in New York City. It uses cluster anaysis to identify the locations with most pick-ups, and the locations generating most lucrative trips. The results are presented using google maps API. It can help taxi drivers to determine where they should wait for the passengers. 

##Data
NYC cab data is available from the NYC Taxi & Limousine Commission’s Trip Record Data site: http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml. 

In the demonstration code, March 2016 'Green cabs' data downloaded from above link is used. 

##Analysis

Use k-means cluster analysis to identify: 

* Pick-up locations with most pick-ups.
* Pick-up locations of Most lucrative trips.

_Here we define lucrative trips as those generating the highest fare for least amount time spent._

Code:

1. cluster_analysis.py --> location csv files; 2. cat heatmap-start.txt > heatmap.html 3. python latlng.py location1.csv >> heatmap.html 4. cat heatmap-end.txt >> heatmap.html 5. open heatmap.html

##Output
The interactive output can be found in googlemap repository.

* Pick-up locations with most pick-ups.
![us_map 1](https://github.com/qianmx/Where-should-a-taxi-driver-pickup-passengers/blob/master/screenshot/most_pickup1.png)


* Pick-up locations of Most lucrative trips.

![us_map 3](https://github.com/qianmx/Where-should-a-taxi-driver-pickup-passengers/blob/master/screenshot/lucrative_location1.png)


_Reference: https://github.com/parrt/msan692/blob/master/notes/sfpd.md_
