def delivery_fee_calculator(distance_km, rate_per_km):
    total_fee = distance_km * rate_per_km
    return f"₱{total_fee:.2f}"

distance = float(input("Enter the distance in kilometers: "))
rate = float(input("Enter the rate per kilometer (₱): "))

print("Total Delivery Fee:", delivery_fee_calculator(distance, rate))