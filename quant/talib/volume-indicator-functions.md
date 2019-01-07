# Volume Indicator Functions

## AD - Chaikin A/D Line 

TODO\(not finish reading yet\)

### Introduction <a id="introduction"></a>

Developed by Marc Chaikin, the Accumulation Distribution Line is a volume-based indicator designed to measure the cumulative flow of money into and out of a security. Chaikin originally referred to the indicator as the Cumulative Money Flow Line. As with cumulative indicators, the Accumulation Distribution Line is a running total of each period's Money Flow Volume. First, a multiplier is calculated based on the relationship of the close to the high-low range. Second, the Money Flow Multiplier is multiplied by the period's volume to come up with a Money Flow Volume. A running total of the Money Flow Volume forms the Accumulation Distribution Line. Chartists can use this indicator to affirm a security's underlying trend or anticipate reversals when the indicator diverges from the security price.

### Calculation <a id="calculation"></a>

There are three steps to calculating the Accumulation Distribution Line \(ADL\). First, calculate the Money Flow Multiplier. Second, multiply this value by volume to find the Money Flow Volume. Third, create a running total of Money Flow Volume to form the Accumulation Distribution Line \(ADL\).

```text
               
  1. Money Flow Multiplier = [(Close  -  Low) - (High - Close)] /(High - Low) 

  2. Money Flow Volume = Money Flow Multiplier x Volume for the Period

  3. ADL = Previous ADL + Current Period's Money Flow Volume
```

The Money Flow Multiplier fluctuates between +1 and -1. As such, it holds the key to the Money Flow Volume and the Accumulation Distribution Line. The multiplier is positive when the close is in the upper half of the high-low range and negative when in the lower half. This makes perfect sense. Buying pressure is stronger than selling pressure when prices close in the upper half of the period's range \(and vice versa\). The Accumulation Distribution Line rises when the multiplier is positive and falls when the multiplier is negative.

![Chart 1  -  Accumulation Distribution Line](https://d.stockcharts.com/school/data/media/chart_school/technical_indicators_and_overlays/accumulation_distribution_line/acdl-1-rimmexam.png)

The multiplier adjusts the amount of volume that ends up in the Money Flow Volume. Volume is in effect reduced unless the Money Flow Multiplier is at its extremes \(+1 or -1\). The multiplier is +1 when the close is on the high and -1 when the close is on the low. All volume is positive when +1 and all volume is negative when -1. At .50, only half of the volume translates into the period's Money Flow Volume. The table below shows the Money Flow Multipliers, Money Flow Volume and Accumulation Distribution Line for Research-in-Motion \(RIMM\). Notice how the multiplier is between .50 and 1 when the close is strong and between -.50 and -1 when the close is weak.

![Table 1  -  Accumulation Distribution Line](https://d.stockcharts.com/school/data/media/chart_school/technical_indicators_and_overlays/accumulation_distribution_line/acdl-1-rimmsheet.png)

[Click here](https://stockcharts.com/school/lib/exe/fetch.php?media=chart_school:technical_indicators_and_overlays:accumulation_distribution_line:cs-accum.xls) for a calculation of the Accumulation Distribution Line in an Excel Spreadsheet.  


### Interpretation <a id="interpretation"></a>

The Accumulation Distribution Line is a cumulative measure of each period's volume flow, or money flow. A high positive multiplier combined with high volume shows strong buying pressure that pushes the indicator higher. Conversely, a low negative number combined with high volume reflects strong selling pressure that pushes the indicator lower. Money Flow Volume accumulates to form a line that either confirms or contradicts the underlying price trend. In this regard, the indicator is used to either reinforce the underlying trend or cast doubts on its sustainability. An uptrend in prices with a downtrend in the Accumulation Distribution Line suggests underlying selling pressure \(distribution\) that could foreshadow a bearish reversal on the price chart. A downtrend in prices with an uptrend in the Accumulation Distribution Line indicate underlying buying pressure \(accumulation\) that could foreshadow a bullish reversal in prices.

### ADL versus OBV <a id="adl_versus_obv"></a>

The Accumulation Distribution Line and On Balance Volume \(OBV\) are cumulative volume-based indicators that sometimes move in opposite directions because their basic formulas are different. Joe Granville developed [On Balance Volume](https://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:on_balance_volume_obv) \(OBV\) as a cumulative measure of positive and negative volume flow. OBV adds a period's total volume when the close is up and subtracts it when the close is down. A cumulative total of this positive and negative volume flow forms the OBV line. This line can then be compared with the price chart of the underlying security to look for divergences or confirmation.

![Chart 2  -  Accumulation Distribution Line](https://d.stockcharts.com/school/data/media/chart_school/technical_indicators_and_overlays/accumulation_distribution_line/acdl-2-clxobvacdl.png)

As the formula above shows, Chaikin took a different approach by completely ignoring the change from one period to the next. Instead, the Accumulation Distribution Line focuses on the level of the close relative to the high-low range for a given period \(day, week, month\). With this formula, a security could gap down and close significantly lower, but the Accumulation Distribution Line would rise if the close were above the midpoint of the high-low range. The chart above shows Clorox \(CLX\) with a big gap down and a close near the top of the day's high-low range. OBV moved sharply lower because the close was below the prior close. The Accumulation Distribution Line moved higher because the close was near the high of the day.

### Trend Confirmation <a id="trend_confirmation"></a>

Trend confirmation is a pretty straight-forward concept. An uptrend in the Accumulation Distribution Line reinforces an uptrend on the price chart and vice versa. The chart below shows Freeport McMoran \(FCX\) and the Accumulation Distribution Line advancing in February-March, declining from April to June and then advancing from July to January. The Accumulation Distribution Line confirmed each of these price trends.

![Chart 3  -  Accumulation Distribution Line](https://d.stockcharts.com/school/data/media/chart_school/technical_indicators_and_overlays/accumulation_distribution_line/acdl-3-fcxaffrm.png)

### Divergences <a id="divergences"></a>

Bullish and bearish divergences are where it starts getting interesting. A bullish divergence forms when price moves to new lows, but the Accumulation Distribution Line does not confirm these lows and moves higher. A rising Accumulation Distribution Line shows, well, accumulation. Think of this as basically stealth buying pressure. Based on the theory that volume precedes price, chartists should be on alert for a bullish reversal on the price chart.

The chart above shows Nordstrom \(JWN\) with the Accumulation Distribution Line. Notice how it is easy to compare price action when the indicator is placed “behind” the price plot. The indicator \(pink\) and the price trend moved in unison from February to June. Signs of accumulation emerged as the indicator bottomed in early July and started moving higher. JWN moved to a new low in late August. Even though the indicator showed signs of buying pressure, it was important to wait for a bullish catalyst or confirmation on the price chart. This catalyst came as the stock gapped up and surged on big volume.

![Chart 4  -  Accumulation Distribution Line](https://d.stockcharts.com/school/data/media/chart_school/technical_indicators_and_overlays/accumulation_distribution_line/acdl-4-jwnbudd.png)

A bearish divergence forms when price moves to new highs, but the Accumulation Distribution Line does not confirm and moves lower. This shows distribution or underlying selling pressure that can foreshadow a bearish reversal on the price chart.

![Chart 5  -  Accumulation Distribution Line](https://d.stockcharts.com/school/data/media/chart_school/technical_indicators_and_overlays/accumulation_distribution_line/acdl-5-luvbedd.png)

The chart above shows Southwest Airlines \(LUV\) with the Accumulation Distribution Line peaking two months ahead of prices. The indicator not only peaked, but it also moved lower in March and April, which reflected some selling pressure. LUV confirmed weakness with a support break on the price chart and RSI moved below 40 shortly afterward. RSI often trades in bull zones \(40-80\) and bear zones \(20-60\). [RSI](https://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:relative_strength_index_rsi)held in the bull zone until early May and then moved into a bear zone.

### Disconnect with Prices <a id="disconnect_with_prices"></a>

The Accumulation Distribution Line is an indicator based on a derivative of price and volume. This makes it at least two steps removed from the actual price of the underlying security. Moreover, the Money Flow Multiplier does not take into account price changes from period to period. As such, it cannot be expected to always affirm price action or successfully predict price reversals with divergences. Sometimes there is a disconnect between prices and the indicator. Sometimes the Accumulation Distribution Line simply doesn't work. This is why it vitally important to use the Accumulation Distribution Line, and all indicators for that matter, in conjunction with price/trend analysis and/or other indicators.

![Chart 6  -  Accumulation Distribution Line](https://d.stockcharts.com/school/data/media/chart_school/technical_indicators_and_overlays/accumulation_distribution_line/acdl-6-gcidisc.png)

### Conclusions <a id="conclusions"></a>

**The Accumulation Distribution Line can be used to gauge the general flow of volume.** An uptrend indicates that buying pressure is prevailing on a regular basis, while a downtrend indicates that selling pressure is prevailing. Bullish and bearish divergences serve as alerts for a potential reversal on the price chart. As with all indicators, it is important to use the Accumulation Distribution Line in conjunction with other aspects of technical analysis, such as [momentum oscillators](https://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:introduction_to_technical_indicators_and_oscillators#momentum_oscillators) and [chart patterns](https://stockcharts.com/school/doku.php?id=chart_school:chart_analysis:chart_patterns). It is not a standalone indicator.

### Using with SharpCharts <a id="using_with_sharpcharts"></a>

The Accumulation Distribution Line is available in SharpCharts as an indicator. After selecting, the indicator can be positioned above, below or behind the price of the underlying security. Positioning “behind price” makes it easy to compare with the underlying security. Chartists can also add a moving average to the indicator by using the advanced options. [**Click here**](http://stockcharts.com/h-sc/ui?s=IBM&p=D&yr=0&mn=8&dy=0&id=p93414126571&listNum=30&a=222506084) for a live chart with the Accumulation Distribution Line.

![Chart 7  -  Accumulation Distribution Line](https://d.stockcharts.com/school/data/media/chart_school/technical_indicators_and_overlays/accumulation_distribution_line/acdl-7-ibmlive.png)

![SharpCharts  -  Accumulation Distribution Line](https://d.stockcharts.com/school/data/media/chart_school/technical_indicators_and_overlays/accumulation_distribution_line/acdl-8-shch.png)

### Suggested Scans <a id="suggested_scans"></a>

#### Bullish Divergence in OBV and ADL <a id="bullish_divergence_in_obv_and_adl"></a>

This scan starts with a base of stocks that are averaging at least $10 in price and 100,000 daily volume over the last 60 days. Potential bullish divergences are found by looking for stocks where price is BELOW the 65-day SMA and 20-day SMA, but OBV and the Accumulation Distribution Line are ABOVE the 65-day SMA and 20-day SMA.

```text
[type = stock] AND [country = US] 
AND [Daily SMA(60,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 10] 

AND [Daily Close < Daily SMA(65,Daily Close)] 
AND [Daily AccDist > Daily AccDist Signal (65)] 
AND [Daily OBV > Daily OBV Signal(65)] 
AND [Daily Close < Daily SMA(20,Daily Close)] 
AND [Daily AccDist > Daily AccDist Signal (20)] 
AND [Daily OBV > Daily OBV Signal(20)]
```

#### Bearish divergence in OBV and ADL <a id="bearish_divergence_in_obv_and_adl"></a>

This scan starts with a base of stocks that are averaging at least $10 in price and 100,000 daily volume over the last 60 days. Potential bearish divergences are found by looking for stocks where price is ABOVE the 65-day SMA and 20-day SMA, but OBV and the Accumulation Distribution Line are BELOW the 65-day SMA and 20-day SMA.

```text
[type = stock] AND [country = US] 
AND [Daily SMA(60,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 10] 

AND [Daily Close > Daily SMA(65,Daily Close)] 
AND [Daily AccDist < Daily AccDist Signal (65)] 
AND [Daily OBV < Daily OBV Signal(65)] 
AND [Daily Close > Daily SMA(20,Daily Close)] 
AND [Daily AccDist < Daily AccDist Signal (20)] 
AND [Daily OBV < Daily OBV Signal(20)]
```

For more details on the syntax to use for Accumulation Distribution Line scans, please see our [Scanning Indicator Reference](http://stockcharts.com/docs/doku.php?id=scans:indicators#accumulation_distribution) in the Support Center.

**Note**: For the purposes of scanning, daily volume data is incomplete during the trading day. When running scans with volume-based indicators like Accumulation/Distribution, be sure to base the scan on the “Last Market Close.” Examples of other volume-based indicators include Chaikin Money Flow, On Balance Volume, and the PVO.

### Further Study <a id="further_study"></a>

This book covers it all with explanations that are simple and clear. Murphy covers most the major charts patterns and indicators. A complete chapter is devoted to understanding volume and open interest.

{% embed url="https://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:accumulation\_distribution\_line" %}

## Chaikin A/D Oscillator

### Introduction <a id="introduction"></a>

Developed by Marc Chaikin, the Chaikin Oscillator measures the momentum of the Accumulation Distribution Line using the [MACD formula](https://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_average_convergence_divergence_macd). This makes it an indicator of an indicator. The Chaikin Oscillator is the difference between the 3-day EMA of the Accumulation Distribution Line and the 10-day EMA of the Accumulation Distribution Line. Like other momentum indicators, this indicator is designed to anticipate directional changes in the Accumulation Distribution Line by measuring the momentum behind the movements. A momentum change is the first step to a trend change. Anticipating trend changes in the Accumulation Distribution Line can help chartists anticipate trend changes in the underlying security. The Chaikin Oscillator generates signals with crosses above/below the zero line or with bullish/bearish divergences.

### Calculation <a id="calculation"></a>

Calculating the Accumulation Distribution Line \(ADL\) is the first step to the Chaikin Oscillator. This article will cover the basic elements of the Accumulation Distribution Line. See our [ChartSchool article](https://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:accumulation_distribution_line) the details. There are three steps to calculating the Accumulation Distribution Line \(ADL\). First, calculate the Money Flow Multiplier. Second, multiply this value by volume to find Money Flow Volume. Third, create a running total of Money Flow Volume to form the Accumulation Distribution Line \(ADL\). Fourth, take the difference between two moving averages to calculate the Chaikin Oscillator.

```text
               
  1. Money Flow Multiplier = [(Close  -  Low) - (High - Close)] /(High - Low) 

  2. Money Flow Volume = Money Flow Multiplier x Volume for the Period

  3. ADL = Previous ADL + Current Period's Money Flow Volume

  4. Chaikin Oscillator = (3-day EMA of ADL)  -  (10-day EMA of ADL)		
```

The Accumulation Distribution Line rises when the Money Flow Multiplier is positive and falls when negative. This multiplier is positive when the close is in the upper a half of the period's high-low range and negative when the close is in the lower half. As a MACD type oscillator, the Chaikin Oscillator turns positive when the faster 3-day EMA moves above the slower 10-day EMA. Conversely, the indicator turns negative when the 3-day EMA moves below the 10-day EMA.

![Chart 1  -  Chaikin Oscillator](https://d.stockcharts.com/school/data/media/chart_school/technical_indicators_and_overlays/chaikin_oscillator/chosc-1-geexam.png)

The chart above shows the Accumulation Distribution Line \(gray\) with the 3-day EMA in \(blue\) and the 10-day EMA \(red\). The price for General Electric \(GE\) is invisible so we can focus on the relationship between the Accumulation Distribution Line and the Chaikin Oscillator. Notice how the Chaikin Oscillator moves into negative territory as the 3-day EMA moves below the 10-day EMA. Conversely, the oscillator turns positive when the 3-day EMA crosses above the 10-day EMA.

### Interpretation <a id="interpretation"></a>

First and foremost, it is important to remember that the Chaikin Oscillator is an indicator of an indicator. It measures momentum for the Accumulation Distribution Line. This makes it at least three steps removed from the price of the underlying security. First, price and volume are reshaped into the Accumulation Distribution Line. Second, exponential moving averages are applied to the Accumulation Distribution Line. Third, the difference between the [moving averages](https://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_averages) is used to form the Chaikin Oscillator. As the third derivative, the indicator is more prone to disconnect from the price of the underlying security.

![Chart 2  -  Chaikin Oscillator](https://d.stockcharts.com/school/data/media/chart_school/technical_indicators_and_overlays/chaikin_oscillator/chosc-2-msftderiv.png)

Having clarified that, the indicator is designed to measure the momentum behind buying and selling pressure \(Accumulation Distribution Line\). A move into positive territory indicates that the Accumulation Distribution Line is rising and buying pressure prevails. A move into negative territory indicates that the Accumulation Distribution Line is falling and selling pressure prevails. Chartists can anticipate crosses into positive or negative territory by looking for bullish or bearish divergences, respectively.

### Buying/Selling Bias <a id="buying_selling_bias"></a>

The Chaikin oscillator can be used to define a general buying or selling bias simply with positive or negative values. The indicator oscillates above/below the zero line. Generally, buying pressure is stronger when the indicator is positive and selling pressure is stronger when the indicator is negative.

The default settings for the Chaikin Oscillator \(3,10\) often produce a line that frequently crosses zero. Chartists can smooth the indicator by lengthening the moving averages. The example below shows the Chaikin Oscillator \(6,20\). Both moving averages were doubled to maintain the ratio and smooth the indicator.

![Chart 3  -  Chaikin Oscillator](https://d.stockcharts.com/school/data/media/chart_school/technical_indicators_and_overlays/chaikin_oscillator/chosc-3-xcross.png)

The Chaikin Oscillator for US Steel \(X\) crossed the zero line six times over 12 months. There were some good signals, such as the April sell signal and the October buy signal. There were also some bad signals or whipsaws. The key, as with all indicators, is to confirm the oscillator signals with other aspects of technical analysis, such as a pure price momentum oscillator or pattern analysis.

![Chart 4  -  Chaikin Oscillator](https://d.stockcharts.com/school/data/media/chart_school/technical_indicators_and_overlays/chaikin_oscillator/chosc-4-aacross.png)

The chart for Alcoa \(AA\) shows six zero-line crosses in 2010. The first five did not generate good signals, but the sixth was a dandy. Chartists should experiment with the settings and consider adding trend lines to enhance their analysis. Trend line breaks are often earlier than zero line crosses. A trend line also captures the direction of the indicator. A rising Chaikin Oscillator reflects a steady increase in buying pressure. A falling Chaikin Oscillator reflects a steady increase in selling pressure.

### Divergences <a id="divergences"></a>

Bullish and bearish divergences alert chartists to a momentum shift in buying or selling pressure that can foreshadow a trend reversal on the price chart. A bullish divergence forms when price moves to new lows and the Chaikin Oscillator forms a higher low. This higher low shows less selling pressure. It is important to wait for some sort of confirmation, such as an upturn in the indicator or a cross into positive territory. A move into positive territory shows upside momentum in the Accumulation Distribution Line.

The Fastenal \(FAST\) chart shows five divergences for the Chaikin Oscillator in 2010. The default settings \(3,10\) produce a rather sensitive oscillator that will generate many divergences. The key is to differentiate the robust signals from the bogus signals by waiting for confirmation. Even with a bullish divergence, selling pressure outweighs buying pressure until there is a cross above the zero line. Buying pressure dominates until there is a cross into negative territory.

![Chart 5  -  Chaikin Oscillator](https://d.stockcharts.com/school/data/media/chart_school/technical_indicators_and_overlays/chaikin_oscillator/chosc-5-fastbudd.png)

The green lines show the Chaikin Oscillator forming a higher low as the stock forms a lower low for a bullish divergence. The green dotted lines show when the indicator moves into positive territory to confirm the signal. The mid-February, early September and late November signals were great. The mid-June buy signal would have resulted in a whipsaw and there was not much weakness after the October sell signal from the bearish divergence.

A bearish divergence forms when price moves to a new high and the Chaikin Oscillator fails to confirm this higher high. This failure reflects less buying pressure that can sometimes foreshadow a bearish reversal on the price chart. Confirmation comes when the oscillator moves into negative territory.

![Chart 6  -  Chaikin Oscillator ](https://d.stockcharts.com/school/data/media/chart_school/technical_indicators_and_overlays/chaikin_oscillator/chosc-6-kssbedd.png)

The chart for Kohls \(KSS\) shows three bearish divergences and two bullish divergences over a 12 month period. The bearish divergences \(red lines\) were confirmed when the Chaikin Oscillator moved into negative territory to show actual downside momentum in the Accumulation Distribution Line. Remember, the Chaikin Oscillator \(3,10\) turns negative when the 3-day EMA of the Accumulation Distribution Line moves below the 10-day EMA.

### Conclusions <a id="conclusions"></a>

The Chaikin Oscillator is a momentum indicator for the Accumulation Distribution Line. Basically, the Chaikin Oscillator turbo charges the Accumulation Distribution Line by measuring momentum. Signals are more frequent and often easier to quantify using the Chaikin Oscillator. As a money flow oscillator it can be used in conjunction with pure price oscillators, such as MACD or [RSI](https://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:relative_strength_index_rsi). As with all indicators, the Chaikin Oscillator should not be used as a stand-alone indicator.

### Using with SharpCharts <a id="using_with_sharpcharts"></a>

The Chaikin Oscillator can be set as an indicator above, below or behind a security's price plot. It is easy to compare indicator/price movements when the indicator is placed behind the price plot. Once the indicator is chosen from the dropdown list, the default parameter setting appears \(3,10\). These parameters can be adjusted to increase or decrease sensitivity. Users can click on “advanced options” to add a horizontal line or moving average. [Click here for a live example](http://stockcharts.com/h-sc/ui?s=IBM&p=D&yr=0&mn=6&dy=0&id=p43640188268&listNum=30&a=222998125).

![Chart 7  -  Chaikin Oscillator](https://d.stockcharts.com/school/data/media/chart_school/technical_indicators_and_overlays/chaikin_oscillator/chosc-7-ibmlive.png)

![SharpCharts  -  Chaikin Oscillator](https://d.stockcharts.com/school/data/media/chart_school/technical_indicators_and_overlays/chaikin_oscillator/chosc-8-shch.png)

### Suggested Scans <a id="suggested_scans"></a>

#### Chaikin Oscillator Turns Positive and RSI Moves Above 55 <a id="chaikin_oscillator_turns_positive_and_rsi_moves_above_55"></a>

This scan starts with a base of stocks that are averaging at least $10 in price and 100,000 in daily volume over the last 60 days. Upturns on good volume are identified when the Chaikin Oscillator moves above +1000, which is just above its centerline \(0\). This is confirmed with price momentum because RSI is required to move above 55, which is just above its centerline \(50\). This scan is meant as a starting point for further analysis and due diligence.

```text
[type = stock] AND [country = US] 
AND [Daily SMA(60,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 10] 

AND [Daily Chaikin Osc(3,10) crosses 1000] 
AND [Daily RSI(14,Daily Close) crosses 55]
```

#### Chaikin Oscillator Turns Negative and RSI Moves Below 45 <a id="chaikin_oscillator_turns_negative_and_rsi_moves_below_45"></a>

This scan starts with a base of stocks that are averaging at least $10 in price and 100,000 in daily volume over the last 60 days. Downturns on good volume are identified when the Chaikin Oscillator moves below -1000, which is just below its centerline \(0\). This is confirmed with price momentum because RSI is required to move below 45, which is just below its centerline \(50\). This scan is meant as a starting point for further analysis and due diligence.

```text
[type = stock] AND [country = US] 
AND [Daily SMA(60,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 10] 

AND [-1000 crosses Daily Chaikin Osc(3,10)] 
AND [45 crosses Daily RSI(14,Daily Close)]
```

For more details on the syntax to use for Chaikin Oscillator scans, please see our [Scanning Indicator Reference](http://stockcharts.com/docs/doku.php?id=scans:indicators#chaikin_oscillator_chaikin_osc) in the Support Center.

### Further Study <a id="further_study"></a>

This book covers it all with explanations that are simple and clear. Murphy covers most the major charts patterns and indicators. A complete chapter is devoted to understanding volume and open interest.

{% embed url="https://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:chaikin\_oscillator" %}

## On Balance Volume \(OBV\)



### Introduction <a id="introduction"></a>

On Balance Volume \(OBV\) measures buying and selling pressure as a cumulative indicator that adds volume on up days and subtracts volume on down days. OBV was developed by Joe Granville and introduced in his 1963 book, Granville's New Key to Stock Market Profits. It was one of the first indicators to measure positive and negative volume flow. Chartists can look for divergences between OBV and price to predict price movements or use OBV to confirm price trends.

### Calculation <a id="calculation"></a>

The On Balance Volume \(OBV\) line is simply a running total of positive and negative volume. A period's volume is positive when the close is above the prior close. A period's volume is negative when the close is below the prior close.

```text
               
If the closing price is above the prior close price then: 
Current OBV = Previous OBV + Current Volume

If the closing price is below the prior close price then: 
Current OBV = Previous OBV  -  Current Volume

If the closing prices equals the prior close price then:
Current OBV = Previous OBV (no change)
```

{% embed url="https://stockcharts.com/school/doku.php?id=chart\_school:technical\_indicators:on\_balance\_volume\_obv" %}

{% embed url="https://www.youtube.com/watch?v=2-usyKU\_F\_A" %}

{% embed url="https://mrjbq7.github.io/ta-lib/func\_groups/volume\_indicators.html" %}

