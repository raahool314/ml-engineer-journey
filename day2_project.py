"""
Claude:
Project: Contact Info Cleaner
Real-world scenario — you're given messy user data and need to clean it up. Create day2_project.py:
raw_name  = "   rAHUl sHARma   "
raw_email = "   RAHUL.SHARMA@Company.COM   "
raw_city  = "pune"
raw_phone = "98-765-43210"
Your program must print a clean formatted output like this:
==================================
       CLEANED CONTACT CARD
==================================
Name  : Rahul Sharma
Email : rahul.sharma@company.com
City  : Pune
Phone : 9876543210
==================================

Rules:

Strip all extra whitespace
Name in title case
Email fully lowercase
Phone with all - removed (hint: .replace())
Every value must be cleaned using string methods — no manual retyping of correct values
"""

raw_name  = "   rAHUl sHARma   "
raw_email = "   RAHUL.SHARMA@Company.COM   "
raw_city  = "pune"
raw_phone = "98-765-43210"

print("=" * 32)
print("       CLEANED CONTACT CARD")
print("=" * 32)
print(f"Name  : {raw_name.strip().title()}")
print(f"Email : {raw_email.strip().lower()}")
print(f"City  : {raw_city.strip().title()}")
print(f"Phone : {raw_phone.replace("-","")}")
print("=" * 32)