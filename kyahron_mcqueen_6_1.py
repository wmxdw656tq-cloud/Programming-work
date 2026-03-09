
import re


# Function: validate_phone

def validate_phone(phone):

    pattern = r"\d{3}-\d{3}-\d{4}"

    if re.fullmatch(pattern, phone):
        return True
    else:
        return False

# Function: validate_ssn

def validate_ssn(ssn):

    pattern = r"\d{3}-\d{2}-\d{4}"

    if re.fullmatch(pattern, ssn):
        return True
    else:
        return False




# Checks if ZIP code is valid
# Format: 12345
def validate_zip(zip_code):

    pattern = r"\d{5}"

    if re.fullmatch(pattern, zip_code):
        return True
    else:
        return False



# Tests the functions with valid and invalid
# examples to make sure they work
def test_data():

    print("\nTesting Phone Numbers")
    print("123-456-7890:", validate_phone("123-456-7890"))
    print("111-22-3333:", validate_phone("111-22-3333"))

    print("\nTesting SSN")
    print("123-45-6789:", validate_ssn("123-45-6789"))
    print("123456789:", validate_ssn("123456789"))

    print("\nTesting ZIP Codes")
    print("12345:", validate_zip("12345"))
    print("12A45:", validate_zip("12A45"))



# Function: main
# Gets input from the user and shows results

def main():

    print("Validator Program\n")

    phone = input("Enter phone number (123-456-7890): ")
    ssn = input("Enter SSN (123-45-6789): ")
    zip_code = input("Enter ZIP code (12345): ")

    if validate_phone(phone):
        print("Phone number is valid")
    else:
        print("Phone number is NOT valid")

    if validate_ssn(ssn):
        print("SSN is valid")
    else:
        print("SSN is NOT valid")

    if validate_zip(zip_code):
        print("ZIP code is valid")
    else:
        print("ZIP code is NOT valid")

   
    test_data()



main()
