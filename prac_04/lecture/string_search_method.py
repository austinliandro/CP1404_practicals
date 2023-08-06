subject_code = "CP1404, MS110"

if subject_code.startswith("CP"):
    print("That's an IT subject :)")

if subject_code.endswith("CP"):
    print("The subject code end with CP")
else:
    print("The subject code not end with CP")


print(subject_code.find("MS110"))
print(subject_code.find("P"))