# Currency Converter

## Objectives

1. Take the first input – the currency that you have. It is default for all the calculations.
2. Retrieve the data from FloatRates as before.
3. Save the exchange rates for USD and EUR (these are the most popular ones, so it's good to have rates for them in advance).
4. Take the second input – the currency code that you want to exchange money for, and the third input – amount of money you have.
5. Check the cache. Maybe you already have what you need?
6. If you have the currency in your cache, calculate the result.
7. If not, get it from the site, and calculate the result.
8. Save the rate to your cache.
9. Print the result.
10. Repeat steps 4-9 until there is no currency left to process.

## Examples

Example 1:

```commandline
> ILS
> USD
> 45
Checking the cache...
Oh! It is in the cache!
You received 13.84 USD.
> RSD
> 57
Checking the cache...
Sorry, but it is not in the cache!
You received 1684.41 RSD.
> EUR
> 33
Checking the cache...
Oh! It is in the cache!
You received 8.38 EUR.
```

Example 2:

```commandline
> USD
> EUR
> 20
Checking the cache...
Oh! It is in the cache!
You received 16.52 EUR.
> NOK
> 45
Checking the cache...
Sorry, but it is not in the cache!
You received 382.1 NOK.
> SEK
> 75
Checking the cache...
Sorry, but it is not in the cache!
You received 624.66 SEK.
> NOK
> 55
Checking the cache...
Oh! It is in the cache!
You received 467.02 NOK.
> ISK
> 91
Checking the cache...
Sorry, but it is not in the cache!
You received 11708.38 ISK.
```