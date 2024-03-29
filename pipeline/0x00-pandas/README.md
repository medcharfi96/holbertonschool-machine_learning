# 0x00-pandas
 ## 0. From Numpy
* creates a pd.DataFrame from a np.ndarray

## 1. From Dictionary

* created a pd.DataFrame from a dictionary

## 2. From File

* loads data from a file as a pd.DataFrame

## 3. rename

* Rename the column Timestamp to Datetime
* Convert the timestamp values to datatime values
* Display only the Datetime and Close columns

## 4. To Numpy
* take the last 10 rows of the columns High and Close and convert them into a numpy.ndarray

## 5. slice
*  slice the pd.DataFrame along the columns High, Low, Close, and Volume_BTC, taking every 60th row

## 6. Flip it and Switch it

*  the rows and columns are transposed and the data is sorted in reverse chronological order

## 7. Sort
*  sort the pd.DataFrame by the High price in descending order
## 8. Prune

* remove the entries in the pd.DataFrame where Close is NaN

## 9. Fill
 to fill in the missing data points in the pd.DataFrame:

* The column Weighted_Price should be removed
* missing values in Close should be set to the previous row value
* missing values in High, Low, Open should be set to the same row’s Close value
* missing values in Volume_(BTC) and Volume_(Currency) should be set to 0

## 11. Concat
index the pd.DataFrames on the Timestamp columns and concatenate them:

* Concatenate the start of the bitstamp table onto the top of the coinbase table
* Include all timestamps from bitstamp up to and including timestamp 1417411920
* Add keys to the data labeled bitstamp and coinbase respectively

## 12. Hierarchy

earrange the MultiIndex levels such that timestamp is the first level:

* Concatenate th bitstamp and coinbase tables from timestamps 1417411980 to 1417417980, inclusive
* Add keys to the data labeled bitstamp and coinbase respectively
* Display the rows in chronological order

##  13. Analyze
*  calculate descriptive statistics for all columns in pd.DataFrame except Timestamp

## 14. Visualize
visualize the pd.DataFrame:

The column Weighted_Price should be removed
Rename the column Timestamp to Date
Convert the timestamp values to date values
Index the data frame on Date
Missing values in Close should be set to the previous row value
Missing values in High, Low, Open should be set to the same row’s Close value
Missing values in Volume_(BTC) and Volume_(Currency) should be set to 0
Plot the data from 2017 and beyond at daily intervals and group the values of the same day such that:

High: max
Low: min
Open: mean
Close: mean
Volume(BTC): sum
Volume(Currency): sum
## What i learned from this chapter

-    What is pandas?
-    What is a pd.DataFrame? How do you create one?
-    What is a pd.Series? How do you create one?
-    How to load data from a file
-    How to perform indexing on a pd.DataFrame
-    How to use hierarchical indexing with a pd.DataFrame
-    How to slice a pd.DataFrame
-    How to reassign columns
-    How to sort a pd.DataFrame
-    How to use boolean logic with a pd.DataFrame
-    How to merge/concatenate/join pd.DataFrames
-    How to get statistical information from a pd.DataFrame
-    How to visualize a pd.DataFrame

## Author
* **Mouhamed Charfi** - [medcharfi96](https://github.com/medcharfi96)