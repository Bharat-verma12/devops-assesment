total_request = 100000
successful_request = 99800
slo = 99.9
failed_request = total_request-successful_request
sli =(successful_request/total_request)*100
error_budget = 100-slo
allowed_failures = round(total_request*error_budget/100)
remaining_budget = allowed_failures-failed_request
print("Login API Realiability Report")
print("Total Request:",total_request)
print("Successful Request : ",successful_request)
print("Failed Request : ",failed_request)

print(f"SLI: {sli:.2f}%")
print(f"SLO: {slo}%")
print(f"Error Budget : {error_budget:.1f}%")
print("Allowed Failures:", allowed_failures)
print("Remaining Budget: ",remaining_budget)

if remaining_budget <=0:
    print("Status : Error budget Exhausted")
    print("Actions: pause features release")
    print("Focus on reliability improvemets")
else:
    print("Status: Error Budget available")
    print("Action : Features release can continue")
