# Black-Scholes and Implied Volatility
## Black-Scholes EU Option Price
Needs 5 inputs to work out the Option Price
* Starting Price
* Strike Price
* Risk free interest rate
* Time to expiration
* Volatility

## Implied Volatility  
This is worked out by using a root method similar to binary search. Making a guess as to what the Volatility is and then then halving the range depending on the output  
This also requires 5 inputs:  
* Stock Price
* Exercise Price
* Risk free interest rate
* Time to expiration
* The Option Price

## How to Run  
### main.py is the python file holding the contents and can be imported into your own project and used as an almost library  
#### EuOptionCall Function  
Function which can be called using the parameters specified in the Black-Scholes description above and will return a float that is the option price rounded to 2 decimal places  

#### ImpliedVolatility Function  
Function which can be run as a static function will take the parameters specified in the Implied Volatility heading. It will return a float of the implied Volatility given a tolerance that can be specified in the function called TOLERANCE  

### testScript.py  
Is the test script and can be used as a benchmark if any modifications are made  

## Required Libraries  
#### For main.py  
* scipy.stats
* math  
  
#### For testScript.py  
* unittest
