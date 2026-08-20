attendance = float(input("Enter attendance percentage: "))
assignment = float(input("Enter assignment score: "))
internal = float(input("Enter internal marks: "))
study_hours = float(input("Enter daily study hours: "))

score = (
    attendance * 0.30 +
    assignment * 0.20 +
    internal * 0.30 +
    study_hours * 10 * 0.20
)

print("\n===== PERFORMANCE PREDICTION =====")
print("Performance Score:", round(score, 2))

if score >= 80:
    print("Prediction: Excellent Performance")

elif score >= 65:
    print("Prediction: Good Performance")

elif score >= 50:
    print("Prediction: Average Performance")

else:
    print("Prediction: Needs Improvement")
