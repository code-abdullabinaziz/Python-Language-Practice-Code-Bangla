রিয়েল-লাইফ প্রজেক্ট বা ব্যাকএন্ড ডেভেলপমেন্টের কাজে ডিকশনারি কমপ্রিহেনশন (Dictionary Comprehension) অত্যন্ত কাজের একটি ফিচার। 
এটি দিয়ে খুব সহজেই এক লাইনে লজিক চালিয়ে কোনো ডিকশনারি ফিল্টার (Filter) করা যায় অথবা 
ডেটা রূপান্তর (Transform) করা যায়।

নিচে একটি রিয়েল-ওয়ার্ল্ড উদাহরণ দেওয়া হলো, 
যেখানে কিছু পণ্যের দাম (USD) থেকে নির্দিষ্ট শর্তে ফিল্টার করব এবং সেগুলোকে অন্য কারেন্সিতে (BDT) রূপান্তর।

# Original product prices in USD
prices_usd = {
    'laptop': 1200, 
    'mouse': 25, 
    'keyboard': 75, 
    'monitor': 300,
    'usb_cable': 10
}

# Task: 
# 1. Filter out products that cost more than $50 (if price > 50)
# 2. Convert their prices into BDT (multiplying by 120)
# 3. Store them in a new dictionary

converted_prices_bdt = {
    product: price * 120 
    for product, price in prices_usd.items() 
    if price > 50
}

print("Original USD Prices:", prices_usd)
print("\nFiltered & Converted BDT Prices (> $50):")
print(converted_prices_bdt)


Original USD Prices: {'laptop': 1200, 'mouse': 25, 'keyboard': 75, 'monitor': 300, 'usb_cable': 10}

Filtered & Converted BDT Prices (> $50):
{'laptop': 144000, 'keyboard': 9000, 'monitor': 36000}


ডিকশনারি কমপ্রিহেনশনের সাধারণ স্ট্রাকচারটি হলো:
{key_expression: value_expression for item in iterable if condition}

১. prices_usd.items(): .items() মেথডের মাধ্যমে আমরা একসাথে কি (পণ্যের নাম) এবং ভ্যালু (দাম) দুটোই লুপে নিয়ে আসি।
2. if price > 50: এটি ফিল্টার হিসেবে কাজ করে। কম দামি পণ্যগুলো (mouse, usb_cable) বাদ পড়ে যায়।
3. product: price * 120: এটি ট্রান্সফর্মেশন হিসেবে কাজ করে। কি ঠিক থাকে, কিন্তু ভ্যালুর সাথে ১২০ গুণ হয়ে নতুন ডিকশনারিতে বসে যায়।




কি (Key) এবং ভ্যালু (Value) পজিশন বদলানো (Inverting a Dictionary)
অনেক সময় ডিকশনারির কি এবং ভ্যালুগুলোকে উল্টে দেওয়ার প্রয়োজন পড়ে (যেমন: ইউজারনেম থেকে রোল বের করা ছিল, 
এখন রোল থেকে ইউজারনেম বের করতে হবে)।


# Original dictionary: Role -> Username
user_roles = {'admin': 'Abdullah', 'editor': 'Rahim', 'viewer': 'Karim'}

# Swapping keys and values using dictionary comprehension
inverted_roles = {username: role for role, username in user_roles.items()}

print("Original Roles:", user_roles)
print("Inverted (Username -> Role):", inverted_roles)


Original Roles: {'admin': 'Abdullah', 'editor': 'Rahim', 'viewer': 'Karim'}
Inverted (Username -> Role): {'Abdullah': 'admin', 'Rahim': 'editor', 'Karim': 'viewer'}




দুটি আলাদা লিস্ট থেকে ডিকশনারি তৈরি করা (zip সহ)
পাইথনের পূর্বের টপিক zip() ফাংশনটি এখানে দারুণভাবে কাজে লাগাতে পারেন। দুটি ভিন্ন লিস্টকে এক লাইনে ডিকশনারিতে রূপান্তর করা যায়।

subjects = ['Python', 'JavaScript', 'C++', 'Database']
scores = [90, 85, 75, 88]

# Creating a dictionary by zipping keys and values together
exam_results = {sub: score for sub, score in zip(subjects, scores)}

print("Combined Exam Results Dictionary:")
print(exam_results)

Combined Exam Results Dictionary:
{'Python': 90, 'JavaScript': 85, 'C++': 75, 'Database': 88}




শর্ত সাপেক্ষে মান পরিবর্তন করা (Conditional Expression inside Comprehension)
যদি নম্বরের ওপর ভিত্তি করে পাস বা ফেইল (Pass/Fail) স্ট্যাটাস দিয়ে নতুন ডিকশনারি বানাতে, 
তবে কমপ্রিহেনশনের ভেতরেই if-else কন্ডিশন ব্যবহার করা যায়।

student_marks = {'Math': 85, 'English': 42, 'Python': 95, 'History': 38}

# Assigning 'Pass' if marks >= 40, otherwise 'Fail'
result_status = {
    subject: ('Pass' if mark >= 40 else 'Fail') 
    for subject, mark in student_marks.items()
}

print("Original Marks:", student_marks)
print("Result Status:", result_status)


Original Marks: {'Math': 85, 'English': 42, 'Python': 95, 'History': 38}
Result Status: {'Math': 'Pass', 'English': 'Pass', 'Python': 'Pass', 'History': 'Fail'}




এপিআই থেকে আসা ডেটার কি (Keys) ক্লিন করা
অনেক সময় ফ্রন্টএন্ড বা থার্ড-পার্টি এপিআই থেকে ডেটা আসলে কি-গুলোর মধ্যে অতিরিক্ত স্পেস বা বড় হাতের অক্ষর থাকে, 
যা ডাটাবেজে সেভ করার আগে ক্লিন করতে হয়।


# Raw data received from an API with messy keys (extra spaces and uppercase letters)
raw_api_data = {
    "  USERNAME ": "abdullah_dev",
    " EMAIL ": "abdullah@gmail.com",
    "STATUS": "ACTIVE"
}

# Cleaning keys by stripping spaces and converting them to lowercase
cleaned_data = {
    key.strip().lower(): value 
    for key, value in raw_api_data.items()
}

print("Cleaned API Data:", cleaned_data)

Cleaned API Data: {'username': 'abdullah_dev', 'email': 'abdullah@gmail.com', 'status': 'ACTIVE'}




ইনভেন্টরি থেকে স্টকআউট (Stock out) পণ্য ফিল্টার করে বাদ দেওয়া
ইকমার্স ব্যাকএন্ডে যে পণ্যগুলোর স্টক ফুরিয়ে গেছে (quantity == 0), সেগুলোকে ফিল্টার করে আলাদা বা বাদ দেওয়ার জন্য এটি চমৎকার কাজ করে।

# Product inventory with quantities
inventory = {
    'laptop': 5,
    'mouse': 0,         # Out of stock
    'keyboard': 12,
    'monitor': 0,       # Out of stock
    'headphone': 8
}

# Filtering out products that are out of stock (quantity > 0)
available_products = {
    product: qty 
    for product, qty in inventory.items() 
    if qty > 0
}

print("Available In-Stock Products:", available_products)

Available In-Stock Products: {'laptop': 5, 'keyboard': 12, 'headphone': 8}



ডিকশনারির ভ্যালুর ওপর গাণিতিক অপারেশন চালানো (যেমন: ডিসকাউন্ট হিসাব করা)
কোনো শপের পণ্যের মূল দামের ওপর এক লাইনেই নির্দিষ্ট পারসেন্টেজ ডিসকাউন্ট হিসাব করে নতুন ডিকশনারি বানিয়ে ফেলা।

# Original product prices
original_prices = {'shirt': 1000, 'pant': 2000, 'shoes': 3500}

# Applying a 15% discount on all prices
discounted_prices = {
    item: price - (price * 0.15) 
    for item, price in original_prices.items()
}

print("Original Prices:", original_prices)
print("Prices after 15% Discount:", discounted_prices)

Original Prices: {'shirt': 1000, 'pant': 2000, 'shoes': 3500}
Prices after 15% Discount: {'shirt': 850.0, 'pant': 1700.0, 'shoes': 2975.0}



সেন্সিটিভ ডেটা ফিল্টার করা (Whitelist Filtering for User Profiles)
ব্যাকএন্ড থেকে ফ্রন্টএন্ডে ইউজারের প্রোফাইল পাঠানোর সময় পাসওয়ার্ড বা গোপনীয় ডেটা লুকিয়ে ফেলতে 
হয় এবং শুধু নির্দিষ্ট কিছু ফিল্ড (allowed fields) অ্যালাউ করতে হয়। এটি সিকিউরিটির জন্য দারুণ কাজ করে।


# Raw user data from database containing sensitive info
user_profile = {
    'username': 'abdullah_dev',
    'email': 'abdullah@gmail.com',
    'password': 'super_secret_hashed_password',
    'is_admin': True,
    'ssn': '123-45-6789'
}

# Only allow these safe public fields to be sent
allowed_fields = {'username', 'email', 'is_admin'}

# Filtering the dictionary to keep only allowed keys
safe_public_profile = {
    key: value 
    for key, value in user_profile.items() 
    if key in allowed_fields
}

print("Safe Public Profile:", safe_public_profile)

Safe Public Profile: {'username': 'abdullah_dev', 'email': 'abdullah@gmail.com', 'is_admin': True}



শব্দের লিস্ট থেকে ডিকশনারি তৈরি (Word Length Mapping)
প্রসেসিং বা সার্চ অ্যালগরিদমের কাজে কোনো লিস্টের উপাদানগুলোকে কি (Key) এবং সেগুলোর দৈর্ঘ্য (Length)
বা অন্য কোনো বৈশিষ্ট্যকে ভ্যালু বানিয়ে ডিকশনারি তৈরি করতে হয়।

# A list of programming/tech words
tech_words = ['python', 'backend', 'javascript', 'database', 'api']

# Creating a dictionary where key is the word and value is its length
word_lengths = {
    word: len(word) 
    for word in tech_words 
    if len(word) > 5  # Optional filter: keep words with length greater than 5
}

print("Word Length Dictionary (Length > 5):", word_lengths)

Word Length Dictionary (Length > 5): {'python': 6, 'backend': 7, 'javascript': 10, 'database': 8}
