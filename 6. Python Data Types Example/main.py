# --- Fixed / Personal Information ---
NAME = "Mohammad Abdullah"
DOB = "15-06-1997"
BLOOD_GROUP = "B+"
RELIGION = "Islam"
COUNTRY = "Bangladesh"
NID_NUMBER = "1997541258745"
BIRTH_PLACE = "Rangpur"

# --- Variable Data ---
age = 30
cgpa = 3.50
address = "Gongachora, Rangpur"
subject = "Backend Engineering"
married = False
account_balance = 89.5982145897
gmail = "programmeraziz216@gmail.com"
phone = "01568451112"
skills = "C, JavaScript, C++, Python"
hobbies = "Coding, Reading, Traveling"
session = "2025-26"
current_status = "Student & Programmer"
language = "Bengali, English"

# --- Formatted Printing ---
print("=" * 55)
print(f"{'SYSTEM PROFILE CARD':^55}")
print("=" * 55)

print(f"{'Name:':<18} {NAME}")
print(f"{'DOB:':<18} {DOB}")
print(f"{'Age:':<18} {age}")
print(f"{'Blood Group:':<18} {BLOOD_GROUP}")
print(f"{'Religion:':<18} {RELIGION}")
print(f"{'Country:':<18} {COUNTRY}")
print(f"{'Birth Place:':<18} {BIRTH_PLACE}")
print(f"{'NID Number:':<18} {NID_NUMBER}")
print(f"{'Status:':<18} {'Married' if married else 'Unmarried'}")
print(f"{'Current Status:':<18} {current_status}")
print(f"{'Subject:':<18} {subject}")
print(f"{'Session:':<18} {session}")
print(f"{'CGPA:':<18} {cgpa:.2f}")
print(f"{'Skills:':<18} {skills}")
print(f"{'Email:':<18} {gmail}")
print(f"{'Phone:':<18} {phone}")
print(f"{'Address:':<18} {address}")
print(f"{'Language:':<18} {language}")
print(f"{'Hobbies:':<18} {hobbies}")
print(f"{'Balance:':<18} ${account_balance:.2f}")

print("=" * 55)

(এখানে :<20 মানে হলো টেক্সটটিকে বামপাশে রেখে ২০ স্পেস জায়গা নেওয়া, ঠিক ljust(20) এর মতো।)

'Name:' কথাটির দৈর্ঘ্য হলো ৫ অক্ষর।

:<10 এর মানে হলো, পাইথন এই শব্দটির জন্য মোট ১০টি স্পেসের জায়গা বরাদ্দ করবে এবং লেখাটিকে বামপাশে (Left-align) রাখবে।

ফলে 'Name:'-এর পর স্বয়ংক্রিয়ভাবে ৫টি খালি স্পেস তৈরি হবে এবং তারপর 
নাম (Mohammad Abdullah) প্রিন্ট হবে। টেবিল বা লিস্ট সোজা করার জন্য এই : কোলন ফরম্যাটিং দারুণ কার্যকরী!




. কমা (,) ব্যবহার করে (যদি আলাদা আর্গুমেন্ট পাঠাতে চান):
print() ফাংশনে একাধিক অংশ কমা দিয়ে আলাদা করা যায়:

name = "Abdullah"
print("Name".ljust(20), f"{name}")


প্লাস (+) ব্যবহার করে (দুইটি স্ট্রিং জোড়া দেওয়া):

name = "Abdullah"
print("Name".ljust(20) + f" {name}")




print("-" * 30)

print(f"{'SYSTEM PROFILE CARD':^30}")

print("-" * 30)


১. প্রথম লাইন: print("-" * 30)
"-": এটি একটি হাইফেন ক্যারেক্টার।

* 30: পাইথনে কোনো স্ট্রিংকে সংখ্যা দিয়ে গুণ করলে তা ততবার পুনরাবৃত্তি (repeat) হয়। 
এখানে হাইফেনটি ৩০ বার ডুপ্লিকেট হয়ে ------------------------------ এরকম একটি লম্বা লাইন তৈরি করবে।

print(...): এটি টার্মিনালে ৩০টি হাইফেনের একটি বর্ডার বা রেখা প্রিন্ট করে।



২. দ্বিতীয় লাইন: print(f"{'SYSTEM PROFILE CARD':^30}")
f"...": এটি পাইথনের f-string, যার ভেতরে সরাসরি ফরম্যাটিং করা যায়।

'SYSTEM PROFILE CARD': এটি সেই মূল টেক্সট যা প্রিন্ট হবে।

:^30: এখানেই আসল কারসাজি!

: দিয়ে ফরম্যাটিং শুরু হয়েছে।

^ সাইনটি নির্দেশ করে টেক্সটটিকে একদম মাঝখানে (Center-aligned) বসাতে হবে।

30 মানে হলো পাইথন মোট ৩০টি ক্যারেক্টারের জায়গা বরাদ্দ করবে এবং তার ঠিক মাঝখানে 
টেক্সটটি বসিয়ে বাকি জায়গাগুলোতে ডানে-বামে অটোমেটিক স্পেস বা খালি জায়গা তৈরি করে দেবে।

print(...): এটি মাঝখানে সাজানো টেক্সটটি স্ক্রিনে প্রিন্ট করবে।


৩. তৃতীয় লাইন: print("-" * 30)
এটি প্রথম লাইনের ঠিক হুবহু কাজ করে। অর্থাৎ, লেখার নিচে আরেকটি ৩০টি হাইফেনের বর্ডার বা লাইন তৈরি করে, যাতে কার্ডটি দেখতে সুন্দর ও গোছানো লাগে।


------------------------------
     SYSTEM PROFILE CARD      
------------------------------






married = False

account = 12.12341

height = 5.221



print("-" * 20)

print(f"{'System Profile Card':^20}")

print("-" * 20)


print(f"{'Married:':<10} {'Married' if married else "Unmarried"}")
print(f"{'Married:'.ljust(10)} {'Married' if married else 'Unmarried'}")


print(f"{'Account:':<10} {account:.3f}")
print(f"{"Account".ljust(10)} {account:.3f}")


print(f"{'Height:':<10} {height:.1f}")
print(f"{'Height:'.ljust(10)} {height:.1f}")



Template Literals (f-string): জাভাস্ক্রিপ্টে যেভাবে ব্যাকটিক এবং ডলার সাইন দিয়ে `My name is: ${name}` লিখা হত, 
পাইথনে সেটাকে বলা হয় f-string। এটি লেখার নিয়ম হলো স্ট্রিংয়ের শুরুতে একটা f লিখে কোটেশনের ভেতর থার্ড ব্র্যাকেট ব্যবহার করা: f"My name is: {name}"।

# --- Constant Data ---
NAME = "Mohammad Abdullah"
DOB = "15-06-1997"
BLOOD_GROUP = "B+"
RELIGION = "Islam"
COUNTRY = "Bangladesh"
NID_NUMBER = "1997541258745"
BIRTH_PLACE = "Rangpur"

# --- Variable Data ---
age = 30
cgpa = 3.50
address = "Gongachora, Rangpur"
subject = "Backend Engineering"
married = False
account_balance = 89.5982145897
gmail = "programmeraziz216@gmail.com"
phone = "01568451112"
skills = "C, JavaScript, C++, Python"
hobbies = "Coding, Reading, Traveling"
session = "2025-26"
current_status = "Student & Programmer"
language = "Bengali, English"

# --- Complete Output ---
print(f"My name is          : {NAME}")
print(f"My age is           : {age}")
print(f"Date of Birth       : {DOB}")
print(f"Blood Group         : {BLOOD_GROUP}")
print(f"Religion            : {RELIGION}")
print(f"Country             : {COUNTRY}")
print(f"NID Number          : {NID_NUMBER}")
print(f"Birth Place         : {BIRTH_PLACE}")
print("-" * 40) # একটি সুন্দর ডিভাইডার লাইনের জন্য
print(f"CGPA                : {cgpa}")
print(f"Address             : {address}")
print(f"Subject             : {subject}")
print(f"Married Status      : {married}")
print(f"Account Balance     : {account_balance}")
print(f"Gmail               : {gmail}")
print(f"Phone               : {phone}")
print(f"Skills              : {skills}")
print(f"Hobbies             : {hobbies}")
print(f"Session             : {session}")
print(f"Current Status      : {current_status}")
print(f"Language            : {language}")



My name is          : Mohammad Abdullah
My age is           : 30
Date of Birth       : 15-06-1997
Blood Group         : B+
Religion            : Islam
Country             : Bangladesh
NID Number          : 1997541258745
Birth Place         : Rangpur
----------------------------------------
CGPA                : 3.5
Address             : Gongachora, Rangpur
Subject             : Backend Engineering
Married Status      : False
Account Balance     : 89.5982145897
Gmail               : programmeraziz216@gmail.com
Phone               : 01568451112
Skills              : C, JavaScript, C++, Python
Hobbies             : Coding, Reading, Traveling
Session             : 2025-26
Current Status      : Student & Programmer
Language            : Bengali, English






এখানে শুধু age, cgpa, married এবং account_balance ভেরিয়েবলগুলো যেহেতু টেক্সট বা স্ট্রিং নয়,
তাই পাইথনের নিয়ম অনুযায়ী সেগুলোকে str() দিয়ে টেক্সটে রূপান্তর করে নেওয়া হয়েছে যাতে প্লাস (+) চিহ্নটি নিখুঁতভাবে কাজ করে।

# --- Constant Data ---
name = "Mohammad Abdullah"
dob = "15-06-1997"
bloodGroup = "B+"
religion = "Islam"
country = "Bangladesh"
nidNumber = "1997541258745"
birthPlace = "Rangpur"

# --- Variable Data ---
age = 30
cgpa = 3.50
address = "Gongachora, Rangpur"
subject = "Backend Engineering"
married = False
accountBalance = 89.5982145897
gmail = "programmeraziz216@gmail.com"
phone = "01568451112"
skills = "C, JavaScript, C++, Python"
hobbies = "Coding, Reading, Traveling"
session = "2025-26"
currentStatus = "Student & Programmer"
language = "Bengali, English"

# --- Simple Output using + ---
print("Name                : " + name)
print("Age                 : " + str(age))
print("Date of Birth       : " + dob)
print("Blood Group         : " + bloodGroup)
print("Religion            : " + religion)
print("Country             : " + country)
print("NID Number          : " + nidNumber)
print("Birth Place         : " + birthPlace)
print("----------------------------------------")
print("CGPA                : " + str(cgpa))
print("Address             : " + address)
print("Subject             : " + subject)
print("Married Status      : " + str(married))
print("Account Balance     : " + str(accountBalance))
print("Gmail               : " + gmail)
print("Phone               : " + phone)
print("Skills              : " + skills)
print("Hobbies             : " + hobbies)
print("Session             : " + session)
print("Current Status      : " + currentStatus)
print("Language            : " + language)


Name                : Mohammad Abdullah
Age                 : 30
Date of Birth       : 15-06-1997
Blood Group         : B+
Religion            : Islam
Country             : Bangladesh
NID Number          : 1997541258745
Birth Place         : Rangpur
----------------------------------------
CGPA                : 3.5
Address             : Gongachora, Rangpur
Subject             : Backend Engineering
Married Status      : False
Account Balance     : 89.5982145897
Gmail               : programmeraziz216@gmail.com
Phone               : 01568451112
Skills              : C, JavaScript, C++, Python
Hobbies             : Coding, Reading, Traveling
Session             : 2025-26
Current Status      : Student & Programmer
Language            : Bengali, English



🐍 সম্পূর্ণ পাইথন কোড (Simple Comma Method)

# --- Constant Data ---
name = "Mohammad Abdullah"
dob = "15-06-1997"
bloodGroup = "B+"
religion = "Islam"
country = "Bangladesh"
nidNumber = "1997541258745"
birthPlace = "Rangpur"

# --- Variable Data ---
age = 30
cgpa = 3.50
address = "Gongachora, Rangpur"
subject = "Backend Engineering"
married = False
accountBalance = 89.5982145897
gmail = "programmeraziz216@gmail.com"
phone = "01568451112"
skills = "C, JavaScript, C++, Python"
hobbies = "Coding, Reading, Traveling"
session = "2025-26"
currentStatus = "Student & Programmer"
language = "Bengali, English"

# --- Simple Output using Comma (,) ---
print("Name                :", name)
print("Age                 :", age)
print("Date of Birth       :", dob)
print("Blood Group         :", bloodGroup)
print("Religion            :", religion)
print("Country             :", country)
print("NID Number          :", nidNumber)
print("Birth Place         :", birthPlace)
print("----------------------------------------")
print("CGPA                :", cgpa)
print("Address             :", address)
print("Subject             :", subject)
print("Married Status      :", married)
print("Account Balance     :", accountBalance)
print("Gmail               :", gmail)
print("Phone               :", phone)
print("Skills              :", skills)
print("Hobbies             :", hobbies)
print("Session             :", session)
print("Current Status      :", currentStatus)
print("Language            :", language)

Name                : Mohammad Abdullah
Age                 : 30
Date of Birth       : 15-06-1997
Blood Group         : B+
Religion            : Islam
Country             : Bangladesh
NID Number          : 1997541258745
Birth Place         : Rangpur
----------------------------------------
CGPA                : 3.5
Address             : Gongachora, Rangpur
Subject             : Backend Engineering
Married Status      : False
Account Balance     : 89.5982145897
Gmail               : programmeraziz216@gmail.com
Phone               : 01568451112
Skills              : C, JavaScript, C++, Python
Hobbies             : Coding, Reading, Traveling
Session             : 2025-26
Current Status      : Student & Programmer
Language            : Bengali, English


ljust() এর পূর্ণরূপ হলো Left Justify। অর্থাৎ, এটি আসল লেখাকে বাম পাশে ঠিক রেখে,
ডান পাশে ইচ্ছা অনুযায়ী ফাঁকা জায়গা (Space) বা যেকোনো চিহ্ন বসিয়ে লেখাটিকে বড় বা সমান করে দেয়।

🐍 সম্পূর্ণ পাইথন কোড (ljust()

# --- Constant Data ---
name = "Mohammad Abdullah"
dob = "15-06-1997"
bloodGroup = "B+"
religion = "Islam"
country = "Bangladesh"
nidNumber = "1997541258745"
birthPlace = "Rangpur"

# --- Variable Data ---
age = 30
cgpa = 3.50
address = "Gongachora, Rangpur"
subject = "Backend Engineering"
married = False
accountBalance = 89.5982145897
gmail = "programmeraziz216@gmail.com"
phone = "01568451112"
skills = "C, JavaScript, C++, Python"
hobbies = "Coding, Reading, Traveling"
session = "2025-26"
currentStatus = "Student & Programmer"
language = "Bengali, English"

# --- ljust(20) দিয়ে প্রতিটি লেখার দৈর্ঘ্য ২০ ক্যারেক্টার করা হয়েছে ---
# এটি JS এর padEnd(20, " ") এর মতো কাজ করছে এবং কোনো কনক্যাট ছাড়াই কমা (,) দিয়ে প্রিন্ট হচ্ছে

print("Name".ljust(20), ":", name)
print("Age".ljust(20), ":", age)
print("Date of Birth".ljust(20), ":", dob)
print("Blood Group".ljust(20), ":", bloodGroup)
print("Religion".ljust(20), ":", religion)
print("Country".ljust(20), ":", country)
print("NID Number".ljust(20), ":", nidNumber)
print("Birth Place".ljust(20), ":", birthPlace)
print("-" * 45) # ডিভাইডার লাইন
print("CGPA".ljust(20), ":", cgpa)
print("Address".ljust(20), ":", address)
print("Subject".ljust(20), ":", subject)
print("Married Status".ljust(20), ":", married)
print("Account Balance".ljust(20), ":", accountBalance)
print("Gmail".ljust(20), ":", gmail)
print("Phone".ljust(20), ":", phone)
print("Skills".ljust(20), ":", skills)
print("Hobbies".ljust(20), ":", hobbies)
print("Session".ljust(20), ":", session)
print("Current Status".ljust(20), ":", currentStatus)
print("Language".ljust(20), ":", language)

টেক্সট ছোট হোক বা বড়, সবগুলোর ডান পাশের কোলন (:) একদম সোজা এক লাইনে পুতুলের মতো সাজানো আসবে:

Name                 : Mohammad Abdullah
Age                  : 30
Date of Birth        : 15-06-1997
Blood Group          : B+
Religion             : Islam
Country              : Bangladesh
NID Number           : 1997541258745
Birth Place          : Rangpur
---------------------------------------------
CGPA                 : 3.5
Address              : Gongachora, Rangpur
Subject              : Backend Engineering
Married Status       : False
Account Balance      : 89.5982145897
Gmail                : programmeraziz216@gmail.com
Phone                : 01568451112
Skills               : C, JavaScript, C++, Python
Hobbies              : Coding, Reading, Traveling
Session              : 2025-26
Current Status       : Student & Programmer
Language             : Bengali, English



১ জাভাস্ক্রিপ্টের toFixed() এবং toPrecision() মেথড দুটি দশমিক সংখ্যা (Float) নিয়ে কাজ করার জন্য দারুণ দুটি টুল।
পাইথনেও ঠিক একই কাজ করার জন্য খুব সহজ এবং চমৎকার কিছু বিল্ট-ইন উপায় আছে।
পাইথনে এই কাজটি করার জন্য ৩টি জনপ্রিয় উপায় আছে:

ক) f-string ফরম্যাটিং (সবচেয়ে বেশি ব্যবহৃত ও আধুনিক)

স্ট্রিংয়ের ভেতর মান বসানোর সময় :.nf লিখে দিলেই দশমিকের পরের ঘর ফিক্সড হয়ে যায় (এখানে n হলো ঘরের সংখ্যা)।

balance = 89.5982145897

# দশমিকের পর ২ ঘর রাখা (toFixed(2) এর মতো)
print(f"{balance:.2f}")  # আউটপুট: 89.60

# দশমিকের পর ৪ ঘর রাখা (toFixed(4) এর মতো)
print(f"{balance:.4f}")  # আউটপুট: 89.5982

accountBalance = 89.5982145897

# দশমিকের পর ২ ঘর দেখাবে এবং শুরুতে $ থাকবে
print(f"Balance: ${accountBalance:.2f}")  
# আউটপুট: Balance: $89.60


খ) বিল্ট-ইন round() ফাংশন

যদি স্ট্রিং বা প্রিন্ট ছাড়া সরাসরি সংখ্যার মান পরিবর্তন করে অন্য ভেরিয়েবলে রাখতে চাওয়া হয়, তবে round(number, digits) ফাংশন ব্যবহার করা লাগবে।

gpa = 3.786

clean_gpa = round(gpa, 2)
print(clean_gpa)  # আউটপুট: 3.79 (টাইপ কিন্তু float-ই থাকবে)


২. JavaScript-এর toPrecision() এর বিকল্প পাইথনে

জাভাস্ক্রিপ্টে toPrecision(n) এর কাজ হলো— দশমিকের আগে এবং পরে মিলিয়ে মোট কয়টি সিগনিফিকেন্ট
ডিজিট বা সার্থক অংক (Significant Digits) থাকবে তা নির্ধারণ করা।

পাইথনে f-string-এর ভেতরে f এর বদলে g ব্যবহার করে হুবহু এই কাজটি করা যায়।

f-string এবং g ফরম্যাট ম্যাজিক

num = 123.4567

# মোট ৪টি সংখ্যা দেখাবে (দশমিকের আগে ৩টি, পরে ১টি)
print(f"{num:.4g}")  # আউটপুট: 123.5

# মোট ২টি সংখ্যা দেখাবে (এটি সায়েন্টিফিক নোটেশনে চলে যাবে JS এর মতোই)
print(f"{num:.2g}")  # আউটপুট: 1.2e+02


পাইথনে String Literal মানে হলো সহজ কথায়— কোডের ভেতরে  যেভাবে সরাসরি কোটেশন চিহ্ন (' ' বা " ") দিয়ে টেক্সট বা স্ট্রিং লিখা হয় ।
পাইথনের একটি অসাধারণ পাওয়ারফুল বৈশিষ্ট্য হলো, এই স্ট্রিংগুলোর একদম শুরুতে বা বাম পাশে (Prefix হিসেবে) ছোট হাতের বা বড় হাতের কিছু 
নির্দিষ্ট ক্যারেক্টার বা লেটার বসিয়ে স্ট্রিংয়ের পুরো আচরণ বদলে দেওয়া যায়। এগুলোকেই বলা হয় String Prefixes। পাইথনে মূলত ৪টি প্রধান প্রিফিক্স আছে।

১. f বা F (Formatted String / f-string)
পাইথনের সবচেয়ে জনপ্রিয় প্রিফিক্স এটি। জাভাস্ক্রিপ্টের Template Literals (ব্যাকটিক ` এবং ${})-এর মতো
পাইথনে কোনো ভেরিয়েবলের মান স্ট্রিংয়ের ভেতরে সরাসরি ডায়নামিকালি বসানোর জন্য এটি ব্যবহার করা হয়।

name = "Aziz"
age = 28

# f-string এর ব্যবহার
message = f"My name is {name} and next year I will be {age + 1}."
print(message)

My name is Aziz and next year I will be 29.

💡 জাভাস্ক্রিপ্টের সাথে মিল: JavaScript-এ যেভাবে ব্যাকটিকের ভেতর `${age + 1}` লিখে স্ট্রিংয়ের
ভেতরেই যোগ-বিয়োগ করতে পারা যায়, পাইথনে এই {age + 1} হুবহু একই কাজ করছে।


২. r বা R (Raw String)

যে স্ট্রিংয়ের ভেতর \n বা \t দিলে সেগুলো স্পেশাল কাজ (Escape Character) করে। কিন্তু যদি চান 
পাইথন এগুলোকে স্পেশাল কিছু না ভেবে একদম সাধারণ টেক্সট হিসেবে পড়ুক, তখন স্ট্রিংয়ের আগে r বসাতে হয়।

কাজ: এসকেপ ক্যারেক্টারগুলোর পাওয়ার নষ্ট করে দিয়ে সাধারণ টেক্সট হিসেবে প্রিন্ট করা (ফাইল পাথ বা উইন্ডোজ ডিরেক্টরির জন্য বেস্ট)।

# সাধারণ স্ট্রিংয়ে \n লাইন ভেঙে দেয়
print("Hello\nWorld") 

# Raw String ব্যবহারে \n এর পাওয়ার হাওয়া!
print(r"Hello\nWorld")

Hello
World
Hello\nWorld



৩. b বা B (Byte String)
সাধারণত পাইথনের সব স্ট্রিং হলো Unicode (ইউনিকোড) বা টেক্সট ফরম্যাট। কিন্তু  যদি কোনো স্ট্রিংয়ের আগে b বসিয়ে দেন,
তবে সেটি সাধারণ টেক্সট না থেকে কম্পিউটারের সরাসরি বোঝার মতো Bytes (বাইটস)-এ রূপান্তর হয়ে যায়।

কাজ: নেটওয়ার্কে ডেটা পাঠানো, ফাইল হ্যান্ডলিং বা ক্রিপ্টোগ্রাফির মতো 
ব্যাকএন্ডের একদম কোর লেভেলের কাজে এটি লাগে। এর ভেতরে শুধু ASCII ক্যারেক্টার থাকতে পারে।

normal_str = "Hello"
byte_str = b"Hello"

print(type(normal_str))  # আউটপুট: <class 'str'>
print(type(byte_str))    # আউটপুট: <class 'bytes'>


৪. u বা U (Unicode String)
পাইথন ২-এর জামানায় সাধারণ স্ট্রিংগুলো ইউনিকোড ছিল না। 
তখন বাংলা বা অন্যান্য ভাষা সাপোর্ট করানোর জন্য স্ট্রিংয়ের আগে আলাদা করে u লিখতে হতো।

কাজ: পাইথন ৩-এ এটি এখন আর কোনো কাজেই লাগে না! 
কারণ পাইথন ৩-এর সব সাধারণ স্ট্রিং এমনিতেই বাই-ডিফল্ট ইউনিকোড। তবে পুরনো কোডের সাথে মিল রাখার জন্য পাইথন এখনো এটি সাপোর্ট করে 

# দুটির কাজ এখন হুবহু এক, কোনো পার্থক্য নেই
text1 = "বাংলা"
text2 = u"বাংলা"

🔥 অ্যাডভান্সড ট্রিক: একসাথে দুটি প্রিফিক্স ব্যবহার (Prefix Combination)

চাইলে প্রয়োজন অনুযায়ী দুটি প্রিফিক্স একসাথেও ব্যবহার করা যাবে!
যেমন— একই সাথে একটি ফরম্যাটেড স্ট্রিং চান (f) এবং চান সেখানে এসকেপ ক্যারেক্টারগুলোও নিষ্ক্রিয় থাকুক (r)। তখন একসাথে fr"" বা rf"" লিখা যাবে।

১. f (Formatted): পাইথনকে বলে, "ভেতরের সেকেন্ড ব্র্যাকেট {} এর কাজ করো (ভেরিয়েবলের মান বসাও)।"
2. r (Raw): পাইথনকে বলে, "ভেতরের ব্যাকস্ল্যাশ \ এর কোনো পাওয়ার থাকবে না
(যেমন \n দিলে নতুন লাইন তৈরি হবে না, ওটা সাধারণ টেক্সটের মতো বসে থাকবে)।"

যখন এই দুটিকে একসাথে rf বা fr লিখা হবে, তখন পাইথন এই দুটি কাজই একই সাথে একই লাইনে করবে।

folder = "Python_Files"

# একই সাথে f এবং r এর ম্যাজিক
path = rf"C:\Users\{folder}\new_line_\test.txt"
print(path)

C:\Users\Python_Files\new_line_\test.txt

কম্পিউটারে Python_Files নামে একটি ফোল্ডার আছে। সেই ফোল্ডারের ভেতরে থাকা একটি টেক্সট ফাইলের পাথ (Path) বা ঠিকানা প্রিন্ট করতে চাইলে ।

সাধারণত উইন্ডোজ কম্পিউটারে ফোল্ডারের ঠিকানাগুলো দেখতে এমন হয়: C:\Users\Python_Files\new_folder\test.txt 
এই ঠিকানার ভেতর কিন্তু \new_folder লিখতে গিয়ে একটা \n চলে এসেছে!

folder_name = "Python_Files"

# উপায় ১: শুধু 'f' ব্যবহার করলে (সমস্যা হবে!)
# কারণ \n দেখে পাইথন লাইনটা ভেঙে দেবে, ফোল্ডারের নাম ঠিকঠাক বসলেও পাথ নষ্ট হয়ে যাবে।
print(f"C:\Users\{folder_name}\new_folder\test.txt")


# উপায় ২: শুধু 'r' ব্যবহার করলে (আরেক সমস্যা!)
# এবার \n এর পাওয়ার নষ্ট হবে ঠিকই, কিন্তু {folder_name} আর ভেরিয়েবলের মান বসাবে না, সরাসরি ব্র্যাকেটটাই প্রিন্ট হবে।
print(r"C:\Users\{folder_name}\new_folder\test.txt")


# উপায় ৩: 'rf' বা 'fr' একসাথে ব্যবহার করলে (ম্যাজিক! একদম নিখুঁত)
# এটি একই সাথে ভেরিয়েবলের মানও বসাবে, আবার \n কে লাইনও ভাঙতে দেবে না।
print(rf"C:\Users\{folder_name}\new_folder\test.txt")

উপায় ১ এর আউটপুট (লাইন ভেঙে গেছে):
C:\Users\Python_Files
ew_folder\test.txt

উপায় ২ এর আউটপুট (ভেরিয়েবলের মান বসেনি):

C:\Users\{folder_name}\new_folder\test.txt

উপায় ৩ এর আউটপুট (rf কম্বিনেশন - একদম পারফেক্ট):

C:\Users\Python_Files\new_folder\test.txt

একই সাথে ভেরিয়েবলের মানও বসাতে হয় (f), আবার ব্যাকস্ল্যাশের (\) ঝামেলাও এড়াতে হয় (r), তখনই  rf বা fr ব্যবহার করা হয়। 


মিনি প্রজেক্ট 💻 সহজ নিয়মে মিনি স্টুডেন্ট প্রোফাইল

print("=== মিনি স্টুডেন্ট প্রোফাইল ম্যানেজমেন্ট ===")

# --- স্টুডেন্ট ১ এর ডেটা ---
# ১. নাম ও ঠিকানা স্ট্রিং (Immutable) হিসেবে নিলাম
name1 = "Mohammad Abdullah"
address1 = "Gongachora, Rangpur"

# ২. নাম ও ঠিকানাকে একটা টুপলে (Immutable Sequence) লক করলাম
info_student1 = (name1, address1)
age1 = 29
cgpa1 = 3.50


# --- স্টুডেন্ট ২ এর ডেটা ---
name2 = "Aziz"
address2 = "Dhaka, Bangladesh"

info_student2 = (name2, address2)
age2 = 30
cgpa2 = 3.85


# --- ডাটাবেজ (Mutable List) ---
# এবার এই দুইজনের পুরো প্রোফাইলকে আমরা একটি মেইন লিস্টের ভেতর সিরিয়ালি সাজিয়ে রাখলাম
student_database = [info_student1, age1, cgpa1, info_student2, age2, cgpa2]

# --------------------------------------------------
print("\n💻 ডাটাবেজ (List) থেকে ইনডেক্স ধরে ডেটা দেখানো হচ্ছে:\n")

# আমরা যেহেতু সিকোয়েন্সের ইনডেক্সিং [0, 1, 2] শিখেছি, তাই সরাসরি ইনডেক্স ধরে প্রিন্ট করবো
print("👤 ১ম স্টুডেন্টের নাম ও ঠিকানা (টুপল):", student_database[0])
print("🎂 ১ম স্টুডেন্টের বয়স :", student_database[1])
print("🎓 ১ম স্টুডেন্টের CGPA :", student_database[2])

print("-" * 40)

print("👤 ২য় স্টুডেন্টের নাম ও ঠিকানা (টুপল):", student_database[3])
print("🎂 ২য় স্টুডেন্টের বয়স :", student_database[4])
print("🎓 ২য় স্টুডেন্টের CGPA :", student_database[5])


=== মিনি স্টুডেন্ট প্রোফাইল ম্যানেজমেন্ট ===

💻 ডাটাবেজ (List) থেকে ইনডেক্স ধরে ডেটা দেখানো হচ্ছে:

👤 ১ম স্টুডেন্টের নাম ও ঠিকানা (টুপল): ('Mohammad Abdullah', 'Gongachora, Rangpur')
🎂 ১ম স্টুডেন্টের বয়স : 29
🎓 ১ম স্টুডেন্টের CGPA : 3.5
----------------------------------------
👤 ২য় স্টুডেন্টের নাম ও ঠিকানা (টুপল): ('Aziz', 'Dhaka, Bangladesh')
🎂 ২য় স্টুডেন্টের বয়স : 30
🎓 ২য় স্টুডেন্টের CGPA : 3.85





পাইথনে ইউজারের থেকে ইনপুট (input()) নিয়ে কীভাবে বিভিন্ন Data Types-এ রূপান্তর করতে হয় এবং 
এগুলো ভবিষ্যতে ব্যাকএন্ড, ডেটাবেস বা সিকিউরিটি সিস্টেমে কীভাবে কাজে লাগে, তার একদম প্র্যাকটিক্যাল কোড উদাহরণ।

পাইথনে input() ফাংশন দিয়ে ইউজার যা-ই লিখুক না কেন, পাইথন সেটা বাই ডিফল্ট String (str) হিসেবে গ্রহণ করে। 
তাই নিজের প্রয়োজনে ডাটা টাইপ কনভার্ট (Type Conversion) করে নিতে হয়।


user_name = input("Enter your user_name: ")

port = int(input("Enter server port (e.g., 8080): "))

price = float(input("Enter product price: "))

is_active_input = input("Is system active? (True/False): ")
# এখানে টেক্সটকে বুলিয়ানে রূপান্তর করা হচ্ছে
is_active = is_active_input.lower() == "true"


print(f"Data: {user_name} | Type: {type(user_name)}")

print(f"Data: {port} | Type: {type(port)}")

print(f"Data: {price} | Type: {type(price)}")

print(f"Data: {is_active} | Type: {type(is_active)}")

Backend API Development (FastAPI / Flask):
ফ্রন্টএন্ড বা ক্লায়েন্ট থেকে যখন কোনো ইউজার ডাটা পাঠায় (যেমন রেজিস্ট্রেশন ফর্ম বা পেমেন্ট অ্যামাউন্ট), 
তখন ব্যাকএন্ডে সার্ভারকে ঠিক করে দিতে হয় কোন ডাটাটি ইন্টিজার (Integer) হবে আর কোনটা স্ট্রিং (String)।
ভুল ডাটা টাইপ আসলে সার্ভার যেন ক্র্যাশ না করে, তা নিশ্চিত করতে হয়।

২. Cybersecurity & Input Validation:
সিকিউরিটি সিস্টেমে ইনপুট ফিল্ডে হ্যাকাররা যেন ভুল বা ক্ষতিকর কোড (যেমন SQL Injection বা XSS) পাঠাতে না পারে,
সেজন্য ইউজারের ইনপুট কোন ডাটা টাইপে আসছে তা কঠোরভাবে চেক (Type Validation) করতে হয়।





List Data Type (একাধিক আইপি বা ফায়ারওয়াল হোয়াইটলিস্ট তৈরি)
সিকিউরিটি বা ব্যাকএন্ডে অনেক সময় একসাথে একাধিক ডাটা (যেমন: একাধিক অনুমোদিত IP Address বা একাধিক ইউজার রোল) 
ইনপুট হিসেবে নিতে হয়। কমা দিয়ে লেখা টেক্সটকে পাইথনে List-এ রূপান্তর করা হয়।


# ইউজার কমা দিয়ে একাধিক আইপি অ্যাড্রেস ইনপুট দিবে
ip_input = input("Enter allowed IPs (comma separated): ")

# split() মেথড ব্যবহার করে স্ট্রিংগুলোকে কেটে একটি List বানিয়ে ফেলা
ip_list = [ip.strip() for ip in ip_input.split(",")]

print(f"Processed Data: {ip_list}")
print(f"Data Type: {type(ip_list)}")  # আউটপুট: <class 'list'>


ip_input = input('Enter allowed IPS (comma separatd): ')

ip_list =[ip.strip() for ip in ip_input.split(",")]

print(f"Processed Data: {ip_list}")

print(f"Data Type: {type(ip_list)}")

ভবিষ্যতে কোথায় লাগবে: ফায়ারওয়াল কনফিগারেশন বা ব্যাকএন্ডে একাধিক আইডি একসাথে ফিল্টার করার সময় এই টেকনিক ব্যবহার করতে হবে।



Dictionary Data Type (সার্ভার কনফিগারেশন বা ইউজার প্রফাইল)
ব্যাকএন্ড বা ডেটাবেসে কি-ভ্যালু (Key-Value) জোড়ায় ডাটা পাঠানোর জন্য পাইথনের Dictionary অপরিহার্য।

# সার্ভারের বেসিক কনফিগারেশন ডিকশনারি হিসেবে তৈরি করা
setting_key = input("Enter setting name (e.g., max_users): ")
setting_value = input("Enter setting value: ")

# ডিকশনারি (Dictionary) তৈরি
server_config = {setting_key: setting_value}

print(f"Server Config: {server_config}")
print(f"Data Type: {type(server_config)}")  # আউটপুট: <class 'dict'>



setting_key = input("Enter setting name (e.g., max_users): ")      
setting_value = input("Enter setting value: ")                     


1st input (setting_key): maintenance_mode // 1st input (setting_key): db_host

2nd input (setting_value): False //  2nd input (setting_value): localhost


server_config = {setting_key: setting_value}

print(f"Server Config: {server_config}")
print(f"Data Type: {type(server_config)}")


ভবিষ্যতে কোথায় লাগবে: API রেসপন্স তৈরি করতে, জেসন (JSON) ডাটা ফরম্যাট হ্যান্ডেল করতে এবং সার্ভারের সেটিংস কনফিগার করতে এটি কাজে লাগে।




Bytes Data Type (সাইবার সিকিউরিটি ও এনক্রিপশন)
সাইবার সিকিউরিটি বা নেটওয়ার্ক প্রোগ্রামিংয়ে কাজ করার সময় সাধারণ টেক্সট (String) সরাসরি পাঠানো যায় না; সেগুলোকে Bytes-এ রূপান্তর করতে হয়
(যেমন: পাসওয়ার্ড হ্যাশ করার সময় বা ফাইল রিড করার সময়)।

# ইউজার একটি গোপন পাসওয়ার্ড বা মেসেজ লিখবে
raw_message = input("Enter text for network transmission/encryption: ")

# encode() মেথড দিয়ে স্ট্রিং থেকে Bytes-এ রূপান্তর করা
byte_data = raw_message.encode('utf-8')

print(f"Raw Bytes: {byte_data}")
print(f"Data Type: {type(byte_data)}")  # আউটপুট: <class 'bytes'>



raw_message = input("Enter text for network transmission/encryption: ")

byte_data = raw_message.encode('utf-8')

print(f"Raw Bytes: {byte_data}")

print(f"Data Type: {type(byte_data)}")

এই কোডটিতে ইউজার ইনপুটকে কম্পিউটারের বোঝার ভাষা অর্থাৎ Bytes-এ রূপান্তর করা হয়।

💻 কোডটি কি করবে?
১. raw_message = input(...): ইউজার কিবোর্ড থেকে যা লিখবে, পাইথন সেটাকে একটি সাধারণ String (str) হিসেবে রিসিভ করবে।
২. byte_data = raw_message.encode('utf-8'): এটি সবচেয়ে গুরুত্বপূর্ণ লাইন। encode('utf-8') ফাংশনটি '
সাধারণ টেক্সটকে নিয়ে প্রতিটি অক্ষরের বাইনারি বা হেক্সাডেসিমেল বাইট ভ্যালুতে রূপান্তর করে। স্ট্রিংয়ের শুরুতে b যুক্ত হয়ে এটি বাইটস অবজেক্টে পরিণত হয়।
৩. প্রিন্ট অংশ: রূপান্তর করা বাইট ডাটা এবং তার ডাটা টাইপ (<class 'bytes'>) স্ক্রিনে দেখায়।

🧪 প্র্যাকটিক্যাল উদাহরণ (Dry Run)
উদাহরণ ১: সাধারণ ইংরেজি টেক্সট দিলে
যদি আপনি ইনপুটে লেখেন:

Enter text for network transmission/encryption: Cyber

আউটপুট আসবে:

Raw Bytes: b'Cyber'
Data Type: <class 'bytes'>

বিশ্লেষণ: এখানে আউটপুটের সামনে ছোট হাতের b থাকার অর্থ হলো পাইথন এখন এটিকে সাধারণ লেখা হিসেবে না দেখে Raw Bytes বা বাইনারি উপাত্ত হিসেবে দেখছে,
যা নেটওয়ার্কে বা ক্রিপ্টোগ্রাফিতে পাঠানো যায়। প্রতিটি ইংরেজি অক্ষর বাইট আকারে মেমোরিতে ১ বাইট করে জায়গা নেয়।

ভবিষ্যতে কোথায় লাগবে: পাইথন দিয়ে সকেট প্রোগ্রামিং (Network Programming), পাসওয়ার্ড এনক্রিপশন (Cryptography) এবং
ম্যালওয়্যার এনালাইসিসের স্ক্রিপ্ট লেখার সময় বাইটস ডাটা টাইপ নিয়ে কাজ করতে হবে।


