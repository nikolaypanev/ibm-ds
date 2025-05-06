device_wattage = 650 #in watts
device_hours = 5 #in hours
device_days = 30 #in days

# Calculate the total energy consumed in kilowatt-hours (kWh)
total_energy_kwh = (device_wattage / 1000) * device_hours * device_days
# Calculate the cost of energy consumed (assuming a rate of $0.12 per kWh)
cost_per_kwh = 0.12
total_cost = total_energy_kwh * cost_per_kwh
# Print the results
print(f"Total energy consumed: {total_energy_kwh:.2f} kWh")
print(f"Total cost of energy consumed: ${total_cost:.2f}")
