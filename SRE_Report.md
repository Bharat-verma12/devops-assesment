SLI,Slo and error budget for Login Api

1. SLI = percentage of successful eligible login request returning HTTP 2xx

Formula: 
Sli = (Successful request/totla eligible request)*100
sli = (99,950/1000,000)*100 = 99.95%

2. Slo = the login API must achieve 99.9% successful eligible login requests per month

3. monthly error budget

error budget = 100% - slo
error budget = 100%-99.9% = 0.1%

4. Error Budget Exhaustion

when the error budget is exhausted
. Pause new releases.
. Prioritize reliability improvements
. Perform root cause analysis.

5. Conclusion


Sli measures service reliability, SLO defines the reliability target, and the error budget
determines the acceptable number of failures
