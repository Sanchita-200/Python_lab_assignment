raw_emails = ["Alice@company.com","bob@gmail.com","CHARLIE@company.com","david@yahoo.com","EVa@Company.com","frank@org.net"]

print("Raw Input Emails:")
print(raw_emails)
print("-" * 75)

# filter() with Lambda: Keep only strings containing '@company.com' (case-insensitive check)
company_emails_only = list(filter(lambda email: "@company.com" in email.lower(), raw_emails))

print("Filtered (Only Company Emails):")
print(company_emails_only)
print("-" * 75)

# map() with Lambda: Normalize the filtered data (lowercase and strip spaces)
cleaned_emails = list(map(lambda email: email.strip().lower(), company_emails_only))

print("Mapped & Cleaned (Standardized Format):")
print(cleaned_emails)
print("-" * 75)

# Combined Approach: Filter and map together in one clean statement
final = list(map(lambda e: e.strip().lower(), filter(lambda e: "@company.com" in e.lower(), raw_emails)))

print("Single Line Execution Result:")
print(final)

"""
Raw Input Emails:
['  Alice@company.com ', 'bob@gmail.com', 'CHARLIE@company.com', 'david@yahoo.com', '  EVa@Company.com  ', 'frank@org.net']
---------------------------------------------------------------------------
Filtered (Only Company Emails):
['  Alice@company.com ', 'CHARLIE@company.com', '  EVa@Company.com  ']
---------------------------------------------------------------------------
Mapped & Cleaned (Standardized Format):
['alice@company.com', 'charlie@company.com', 'eva@company.com']
---------------------------------------------------------------------------
Single Line Execution Result:
['alice@company.com', 'charlie@company.com', 'eva@company.com']
"""
