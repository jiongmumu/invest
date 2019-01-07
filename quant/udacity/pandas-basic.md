# pandas basic

## reading and plot data

```python
tmp = pd.read_csv(symbol_to_path(symbol),parse_dates=True,index_col='Date',na_values='NaN',usecols=['Date','Adj Close']).rename(columns={"Adj Close": symbol})
        df = df.join(tmp,how='inner')
```



**To read multiple stocks into a single dataframe, you need to:**

* Specify a set of dates using [pandas.date\_range](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.date_range.html)
* Create an empty dataframe with dates as index
  * This helps align stock data and orders it by trading date
* Read in a reference stock \(here SPY\) and drop non-trading days using [pandas.DataFrame.dropna](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html)
* Incrementally join dataframes using [pandas.DataFrame.join](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.join.html)

**Once you have multiple stocks, you can:**

* Select a subset of stocks by ticker symbols
* Slice by row \(dates\) and column \(symbols\)
* Plot multiple stocks at once \(still using [pandas.DataFrame.plot](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html)\)
* Carry out arithmetic operations across stocks, e.g. normalize by the first day's price

## numpy

#### Lesson outline <a id="lesson-outline"></a>

_If you're familiar with NumPy \(esp. the following operations\), feel free to skim through this lesson._

* Create a NumPy array:
  * from a pandas dataframe: [pandas.DataFrame.values](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.values.html)
  * from a Python sequence: [numpy.array](http://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html)
  * with constant initial values: [numpy.ones](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ones.html), [numpy.zeros](http://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html)
  * with random values: [numpy.random](http://docs.scipy.org/doc/numpy/reference/routines.random.html)
* Access array attributes: [shape](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.shape.html), [ndim](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.ndim.html), [size](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.size.html), [dtype](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.dtype.html)
* Compute statistics: [sum](http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html), [min](http://docs.scipy.org/doc/numpy/reference/generated/numpy.min.html), [max](http://docs.scipy.org/doc/numpy/reference/generated/numpy.max.html), [mean](http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html)
* Carry out arithmetic operations: [add](http://docs.scipy.org/doc/numpy/reference/generated/numpy.add.html), [subtract](http://docs.scipy.org/doc/numpy/reference/generated/numpy.subtract.html), [multiply](http://docs.scipy.org/doc/numpy/reference/generated/numpy.multiply.html), [divide](http://docs.scipy.org/doc/numpy/reference/generated/numpy.divide.html)
* Measure execution time: [time.time](https://docs.python.org/2/library/time.html#time.time), [profile](https://docs.python.org/2/library/profile.html)
* Manipulate array elements: Using [simple indices and slices](http://docs.scipy.org/doc/numpy/reference/arrays.indexing.html#basic-slicing-and-indexing), [integer arrays](http://docs.scipy.org/doc/numpy/reference/arrays.indexing.html#integer-array-indexing), [boolean arrays](http://docs.scipy.org/doc/numpy/reference/arrays.indexing.html#boolean-array-indexing)



