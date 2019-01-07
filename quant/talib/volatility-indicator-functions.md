# Volatility Indicator Functions

## ATR - Average True Range

NOTE: The `ATR` function has an unstable period.

**ATR可以用来买入时候止损线，盈利2\*ATR就卖出**

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8047031510bc4cfb0be895e2f1094a2d1d2c65ee)

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/98a42d7fff69644b96c87d554804a78e3c51a933)

The first ATR value is calculated using the arithmetic mean formula:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/c4ec031470cc0c96a76823665a069a0112d17afa)

```python
real = ATR(high, low, close, timeperiod=14)
```

![](../.gitbook/assets/image%20%287%29.png)

{% embed url="https://www.youtube.com/watch?v=whdj-d52hU0" %}

## NATR - Normalized Average True Range

**DESCRIPTION**

Normalized Average True Range \(NATR\) attempts to normalize the average true range values across instruments by using the formula below.

**FORMULA**

NATR = ATR\(n\) / Close \* 100

Where: ATR\(n\) = Average True Range over ‘n’ periods.

## TRANGE - True Range

{% embed url="https://mrjbq7.github.io/ta-lib/func\_groups/volatility\_indicators.html" %}

