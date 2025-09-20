def calculate_fare(trips):
    base_fare = 50
    per_km_rate = 10
    trips_rates=[]
    for rate in trips:
        trips_rates.append(base_fare+(rate*per_km_rate))
    return trips_rates
trips=eval(input("Enter the trips: "))
trips_rates=calculate_fare(trips)
for i in range(len(trips_rates)):
    print(f"Trip {i+1}: ${trips_rates[i]}")
print(f"Total Fare: ${sum(trips_rates)}")