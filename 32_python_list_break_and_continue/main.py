String (স্ট্রিং)-এর সাথে সরাসরি break বা continue যুক্ত কোনো স্টেটমেন্ট পাইথনে নেই।

break এবং continue হলো লুপ কন্ট্রোল স্টেটমেন্ট (Loop Control Statements)। অর্থাৎ, এরা কেবল লুপের (for লুপ বা while লুপ) ভেতরেই কাজ করে।

তবে ব্যাকএন্ড ইঞ্জিনিয়ারিংয়ে স্ট্রিং প্রসেস বা ফিল্টার করার সময় লুপের ভেতরে break এবং continue প্রচুর ব্যবহার করা হয়।

ব্যাকএন্ডে স্ট্রিং + লুপ (break/continue) কীভাবে কাজে লাগে?
ব্যাকএন্ডে ইউজারদের পাঠানো টেক্সট/স্ট্রিং ফিল্টার করা, সিকিউরিটি চেক করা বা ফাইল রিড করার সময় এটি লাগে। ৩টি বাস্তব উদাহরণ:


সাইবার সিকিউরিটি: ক্ষতিকারক ক্যারেক্টার (SQL Injection / XSS) ডিটেক্ট করা (break দিয়ে)
ইউজারের পাঠানো টেক্সট বা ইউজারনেমে কোনো বেআইনি/ক্ষতিকারক ক্যারেক্টার থাকলে লুপ থামিয়ে দেওয়া:


user_input = "abdullah'; DROP TABLE users;--"
forbidden_chars = [";", "'", "--", "<script>"]

is_suspicious = False

for char in forbidden_chars:
    if char in user_input:
        is_suspicious = True
        print(f"SECURITY ALERT: Illegal substring '{char}' detected!")
        break  # ক্ষতিকারক লেখা পাওয়ার সাথে সাথে লুপ বন্ধ

if is_suspicious:
    # ব্যাকএন্ডে রিকোয়েস্ট ব্লক করে দেওয়া
    print("400 Bad Request: Malicious Input")



টেক্সট ক্লিনআপ: ইমেইল বা ফোন নম্বরের স্পেস পরিষ্কার করা (continue দিয়ে)
ইউজার ভুল করে ফোন নম্বর বা আইডি কোডের মাঝে স্পেস দিলে বা ড্যাশ দিলে সেগুলো বাদ দিয়ে আসল নম্বর তৈরি করা:


raw_phone_number = "017 123 - 456 78"
clean_number = ""

for char in raw_phone_number:
    # যদি স্পেস বা ড্যাশ হয়, তবে স্কিপ করো
    if char == " " or char == "-":
        continue
    
    clean_number += char

print(f"Cleaned Phone Number: {clean_number}")  # Output: 01712345678


ফাইল বা লগ প্রসেসিং: ফাঁকা ক্যারেক্টার বা কমেন্ট স্কিপ করা
লগ ফাইল থেকে টেক্সট স্ট্রিং পড়ার সময়:


log_line = "# This is a comment line"

for char in log_line:
    if log_line.startswith("#"):
        print("Skipping comment line...")
        break  # কমেন্ট লাইন হলে পুরো লাইন প্রসেস না করে লুপ শেষ



ব্যাকএন্ডের জন্য শর্টকাট (Pythonic Alternative)
অভিজ্ঞ ব্যাকএন্ড ডেভেলপাররা স্ট্রিং ক্লিন করার জন্য লুপের বদলে পাইথনের বিল্ট-ইন স্ট্রিং মেথডও ব্যবহার করে:

# লুপ ছাড়া সরাসরি স্পেস রিমুভ করা
raw_phone = "017 123 - 456 78"
clean_phone = raw_phone.replace(" ", "").replace("-", "")

print(clean_phone)  # Output: 01712345678



স্ট্রিংয়ের (String) প্রতিটি অক্ষরের ওপর for লুপ চালিয়ে ব্যাকএন্ডে break এবং continue ব্যবহার করার ৪টি প্র্যাকটিক্যাল ব্যাকএন্ড ও সিকিউরিটি উদাহরণ:

continue দিয়ে অনাকাঙ্ক্ষিত ক্যারেক্টার ফিল্টার করা (Sanitization)
ইউজার ব্যাকএন্ডে কোনো ফোন নম্বর বা আইডি পাঠালে তার মধ্যে থাকা স্পেস ( ), হাইফেন (-), বা ব্র্যাকেট () স্কিপ করে শুধু নিখাদ সংখ্যা বা ক্যারেক্টার দিয়ে নতুন স্ট্রিং তৈরি করার কাজে:    

raw_phone_number = "+880 (171) 234-5678"
clean_phone_number = ""

for char in raw_phone_number:
    # সংকেত বা স্পেস পেলে স্কিপ করো
    if char in " ()-+":
        continue
        
    clean_phone_number += char

print(f"✅ Cleaned Phone Number: {clean_phone_number}")
# Output: 8801712345678



break দিয়ে ক্ষতিকারক ক্যারেক্টার স্ক্যানিং (Security Check)
ব্যাকএন্ডের কোনো ফিল্ডে (যেমন: Username) যদি বিশেষ কোনো ক্ষতিকারক বা নিষিদ্ধ ক্যারেক্টার (যেমন: <, >, ;, ') থাকে,
তবে প্রথম ক্যারেক্টারটি পাওয়ার সাথে সাথেই break করে লুপ থামিয়ে দেওয়া এবং রিকোয়েস্ট রিজেক্ট করা:


username_input = "abdullah<script>"
forbidden_chars = "<>;'\""

is_invalid = False

for char in username_input:
    # নিষিদ্ধ ক্যারেক্টার পাওয়া মাত্রই চেক থামাও
    if char in forbidden_chars:
        is_invalid = True
        print(f"🚨 Security Violation: Forbidden character '{char}' detected!")
        break  # পুরো স্ট্রিং আর চেক করার দরকার নেই, লুপ থামিয়ে দিলাম

if is_invalid:
    print("❌ 400 Bad Request: Invalid characters in username.")



continue দিয়ে পাসওয়ার্ড পলিসি চেক (Validating Password Strength)
ইউজারের পাসওয়ার্ডের ভেতরে কয়টি স্পেশাল ক্যারেক্টার বা ডিজিট আছে তা গোনার সময় অন্যান্য সাধারণ লেটার স্কিপ করার কাজে:


password_input = "Pass123!"
special_char_count = 0
special_chars = "!@#$%^&*"

for char in password_input:
    # অক্ষরের বাইরে সাধারণ অক্ষর হলে স্কিপ করো
    if char not in special_chars:
        continue
        
    special_char_count += 1

print(f"🔒 Total Special Characters Found: {special_char_count}")
# Output: 1


break দিয়ে ফাইল এক্সটেনশন বা ইমেইলের ডোমেইন চেক
একটি ফাইল নেম স্ট্রিং ব্যাকএন্ডে প্রসেস করার সময় ডট (.) পাওয়ার সাথে সাথে ফাইল নেম আলাদা করা:

filename = "user_report_2026.pdf"
file_title = ""

for char in filename:
    # ডট (.) পাওয়ার সাথে সাথে থেমে যাও, কারণ এরপর এক্সটেনশন শুরু
    if char == ".":
        break
        
    file_title += char

print(f"📄 Extracted File Title: {file_title}")
# Output: user_report_2026


ব্যাকএন্ড সামারি:
continue (ফিল্টারিং): স্ট্রিংয়ের প্রতিটি অক্ষরের মধ্যে যেগুলো ব্যাকএন্ডে লাগবে না (যেমন: স্পেস, ড্যাশ, অনাকাঙ্ক্ষিত সিম্বল), সেগুলো স্কিপ করে শুধু দরকারি অক্ষরগুলো জমায়।

break (ডিটেকশন/সার্চিং): স্ট্রিংয়ের ভেতর অবৈধ কোনো ক্যারেক্টার বা নির্দেশক চিহ্ন (যেমন: SQL injection symbol বা .) পাওয়ার সাথে সাথেই লুপ বন্ধ করে মেমোরি ও প্রসেসিং টাইম বাঁচায়।








লিস্ট (list) ডেটা টাইপের ওপর লুপ ঘুরিয়ে break ব্যবহার করার প্রধান কারণ হলো মেমোরি ও প্রসেসিং টাইম বাঁচানো (Performance Optimization) এবং সার্চিং
ক্রাইটেরিয়া সফল হলে সাথে সাথে লুপ থামিয়ে দেওয়া।


ভবিষ্যতে ব্যাকএন্ড ডেভেলপমেন্ট, সাইবার সিকিউরিটি ও ডাটাবেস হ্যান্ডেল করার সময় যে ৩টি সবচেয়ে গুরুত্বপূর্ণ ক্ষেত্রে break কাজে আসবে:

ডাটাবেস সার্চ অপটিমাইজেশন (Search Until Found)
ধরুন আপনার ডাটাবেসে লাখ লাখ ইউজারের লিস্ট আছে। কোনো নির্দিষ্ট ইউজার আইডি বা ইমেইল খুঁজছেন। 
লিস্টের প্রথম দিকেই যদি ইউজারকে পেয়ে যান, তবে বাকী লাখ লাখ ডাটা লুপ ঘুরিয়ে চেক করার কোনো অর্থ হয় না। break দিয়ে সেখানেই প্রসেসিং থামিয়ে দেওয়া হয়।


                                   
# লাখ লাখ ইউজারের একটি লিস্ট (এখানে উদাহরণ হিসেবে ৪টি দেওয়া হলো)
user_database = [
    {"id": 101, "email": "sami@gmail.com"},
    {"id": 102, "email": "abdullah@gmail.com"},
    {"id": 103, "email": "rahim@gmail.com"},
    {"id": 104, "email": "karim@gmail.com"}
]

target_email = "abdullah@gmail.com"
found_user = None

for user in user_database:
    if user["email"] == target_email:
        found_user = user
        print(f"🎯 User found: ID {user['id']}")
        break  # ২ নম্বর আইটেমেই পাওয়া গেছে! তাই ৩ ও ৪ নম্বর চেক না করে লুপ বন্ধ।

if not found_user:
    print("❌ User not found.")



সাইবার সিকিউরিটি ও থ্রেট ডিটেকশন (Early Exit on Malicious Event)
ফায়ারওয়াল বা এপিআই ব্যাকএন্ডে যখন কোনো ইউজার বা সার্ভার থেকে আসা রিকোয়েস্টের লিস্ট ব্যাকএন্ড চেক করে, 
তখন কোনো ব্ল্যাকলিস্টেড বা ক্ষতিকারক কার্যকলাপ পাওয়ার সাথে সাথেই break দিয়ে লুপ থামিয়ে দেওয়া হয় এবং আইপি ব্লক করা হয়।

# ইউজার রিকোয়েস্ট থেকে আসা প্যারামিটারের লিস্ট
api_payload = ["search_query=python", "page=1", "filter=<script>alert('hack')</script>"]
blacklisted_keywords = ["<script>", "DROP TABLE", "SELECT *"]

has_threat = False

for data in api_payload:
    # চেক করা হচ্ছে কোনো ক্ষতিকারক কি-ওয়ার্ড লিস্টের পে-লোডে আছে কিনা
    for keyword in blacklisted_keywords:
        if keyword in data:
            has_threat = True
            print(f"🚨 Security Threat Detected: '{keyword}' inside payload!")
            break  # থ্রেট পেয়ে গেছি, পুরো রিকোয়েস্ট ব্লক করার জন্য লুপ থামাও
            
    if has_threat:
        break  # বাইরের লুপও বন্ধ করে দেওয়া হলো

if has_threat:
    print("❌ 403 Forbidden: Request Blocked by Firewall.")


পেমেন্ট ও লিমিট ভ্যালিডেশন (Threshold Limits & Payment Failures)
কোনো অ্যাকাউন্টের একাধিক ট্রানজেকশনের লিস্ট থেকে মোট খরচের পরিমাণ হিসাব করার সময় যদি কোনো নির্দিষ্ট লিমিট (Limit) ছাড়িয়ে যায়, 
বা কোনো অবৈধ ট্রানজেকশন ধরা পড়ে, তবে সাথে সাথে প্রসেসিং বন্ধ করতে break লাগে।


# ইউজার একের পর এক ট্রানজেকশন করার চেষ্টা করছে
transactions = [1200, 5000, 3000, 15000, 2000]
daily_limit = 10000

total_spent = 0

for amount in transactions:
    if total_spent + amount > daily_limit:
        print(f"⚠️ Limit Exceeded! Cannot process transaction of {amount} BDT.")
        break  # লিমিট শেষ, তাই পরবর্তী সব ট্রানজেকশন প্রসেস না করে থামিয়ে দেওয়া হলো
        
    total_spent += amount
    print(f"✅ Processed: {amount} BDT. Total: {total_spent} BDT")


💡 সারসংক্ষেপ (Golden Rule for break in List)
ভবিষ্যতে ব্যাকএন্ডে লিস্টের ওপর কাজ করার সময় এই ২টি প্রশ্ন নিজেকে

"আমি কি কোনো নির্দিষ্ট জিনিস খুঁজছি, যা পেয়ে গেলে আর খোঁজার দরকার নেই?" break ব্যবহার।
"কোনো শর্ত পূরণ বা লঙ্ঘন হলে কি পুরো প্রসেস সাথে সাথে থামিয়ে দেওয়া দরকার?"  break ব্যবহার।



লিস্টের সাথে break (নির্দিষ্ট ডাটা পাওয়ার সাথে সাথে থামা)
ধরা যাক, আপনার ডাটাবেস থেকে পাওয়া একটি লিস্টের মধ্যে নির্দিষ্ট কোনো ফাইল বা ইউজারকে খুঁজছেন। 
কাঙ্ক্ষিত আইটেমটি পেয়ে গেলে পুরো লিস্ট বাকিটা আর লুপ ঘুরানোর প্রয়োজন নেই, সময় বাঁচাতে লুপ থামিয়ে দিতে break ব্যবহৃত হয়:


ip_logs = ["192.168.1.1", "10.0.0.5", "172.16.0.2", "192.168.1.100"]
target_ip = "10.0.0.5"

for ip in ip_logs:
    print(f"Checking IP: {ip}")
    if ip == target_ip:
        print(f"🎯 Target IP {target_ip} found! Stopping search.")
        break  # আইপি পাওয়া গেছে, তাই বাকি লিস্ট আর চেক করার দরকার নেই




এপিআই টোকেন ভ্যালিডেশন (Authentication Check)
ইউজার যখন একাধিক হেডার বা টোকেন পাঠায়, ব্যাকএন্ড লিস্টের ভেতরে একটি অবৈধ বা মেয়াদকোীর্ণ টোকেন পাওয়ার সাথে সাথেই চেক করা থামিয়ে দেয় এবং অ্যাক্সেস রিজেক্ট করে:

# ব্যাকএন্ডের সিকিউরিটি চেক
session_tokens = ["valid_token_1", "valid_token_2", "expired_token_99", "valid_token_3"]

access_granted = True

for token in session_tokens:
    if token == "expired_token_99":
        print("❌ Expired token found! Stopping auth check.")
        access_granted = False
        break  # মেয়াদউত্তীর্ণ টোকেন পেয়ে গেছি, বাকীগুলো চেক করা সময় নষ্ট

if not access_granted:
    print("401 Unauthorized: Please log in again.")



প্রথম পর্যাপ্ত রিসোর্স বা সার্ভার খুঁজে বের করা (Load Balancing)
ব্যাকএন্ড থেকে যখন একাধিক সার্ভারের লিস্ট থেকে একটি সচল এবং ফাঁকা (Available) সার্ভার খোঁজা হয়, 
প্রথম সচল সার্ভারটি পাওয়ার সাথে সাথে লুপ থামিয়ে সেখানে রিকোয়েস্ট পাঠানো হয়:


servers = [
    {"name": "Server-A", "status": "busy"},
    {"name": "Server-B", "status": "down"},
    {"name": "Server-C", "status": "available"},
    {"name": "Server-D", "status": "available"}
]

selected_server = None

for server in servers:
    if server["status"] == "available":
        selected_server = server["name"]
        print(f"✅ Route request to: {selected_server}")
        break  # প্রথম সচল সার্ভার (Server-C) পেয়ে গেছি, Server-D আর চেক করার প্রয়োজন নেই

print(f"Connecting to {selected_server}...")



ফাইল আপলোড লিমিট এবং সাইজ চেক (Storage Optimization)
ইউজার যখন একাধিক ফাইল একসাথে আপলোড করে (Bulk Upload), ফাইলগুলোর মোট সাইজ 
যদি অনুমোদিত লিমিট (যেমন: 20 MB) পার করে যায়, তবে সাথে সাথে আপলোড প্রসেস থামিয়ে দেওয়া হয়:

# ফাইল সাইজ মেগাবাইটে (MB)
file_sizes_mb = [3, 5, 8, 12, 4] 
max_upload_limit = 20  # সর্বোচ্চ ২০ এমবি

total_uploaded = 0

for size in file_sizes_mb:
    if total_uploaded + size > max_upload_limit:
        print(f"⚠️ Limit exceeded! File size {size} MB cannot be uploaded.")
        break  # ২০ এমবি পার হয়ে গেছে, বাকী ফাইলগুলো আপলোড প্রসেসে আর যাবে না

    total_uploaded += size
    print(f"Uploaded: {size} MB | Current Total: {total_uploaded} MB")



ডাটাবেস এরর ডিটেকশন (Rollback Transaction)
একসাথে একাধিক ডাটা প্রসেস বা আপডেট করার সময় (Batch Processing), লিস্টের যেকোনো একটি ডাটায় এরর বা ভ্যালিডেশন ফেল করলে 
ব্যাকএন্ড সঙ্গে সঙ্গে লুপ থামায় এবং রোলব্যাক (Rollback) করে:



batch_data = [
    {"user_id": 1, "amount": 100},
    {"user_id": 2, "amount": 250},
    {"user_id": 3, "amount": -50},  # ❌ অবৈধ ঋণাত্মক টাকা!
    {"user_id": 4, "amount": 500}
]

has_error = False

for entry in batch_data:
    if entry["amount"] < 0:
        print(f"🚨 Invalid transaction detected for User ID {entry['user_id']}!")
        has_error = True
        break  # এরর ধরা পড়েছে, বাকী ডাটা প্রসেস করা ঝুঁকিপূর্ণ

if has_error:
    print("🔄 Rolling back all changes. Transaction Failed.")


💡 সারসংক্ষেপ (লিস্টে break কেন ব্যবহার করবেন):
১. সময় বাঁচায়: লাখ লাখ ডাটার মাঝে প্রথম মিল বা এরর পেয়ে গেলে বাকীগুলো প্রসেস করে সিপিইউ (CPU) নষ্ট করে না।
২. নিরাপত্তা দেয়: সিস্টেম ভুল বা ক্ষতিকারক ডাটা দিয়ে আর সামনের দিকে এগোতে পারে না।


ইমেইল বা এসএমএস নোটিফিকেশন কোটা চেক (Rate Limiting)
অনেক থার্ড-পার্টি সার্ভিস (যেমন: SendGrid, Twilio) থেকে ফ্রিতে বা নির্দিষ্ট খরচে দৈনিক একটা লিমিট পর্যন্ত ইমেইল/এসএমএস পাঠানো যায়।
ইউজারদের লিস্টে নোটিফিকেশন পাঠাতে পাঠাতে লিমিট শেষ হয়ে গেলে সাথে সাথে লুপ বন্ধ করে দেওয়া হয়:

users_to_notify = ["user1@mail.com", "user2@mail.com", "user3@mail.com", "user4@mail.com"]
daily_email_quota = 2  # সর্বোচ্চ ২টি ইমেইল পাঠানো যাবে
sent_count = 0

for email in users_to_notify:
    if sent_count >= daily_email_quota:
        print("⚠️ Email quota limit reached! Stopping email queue.")
        break  # কোটা শেষ, তাই বাকী ইউজারদের আর ইমেইল পাঠানো যাবে না

    print(f"📧 Email sent to: {email}")
    sent_count += 1



  এপিআই পেজিনেশন ও প্রথম পেজে ডাটা পাওয়া (Pagination Search)
ব্যাকএন্ডে যখন ডাটা পেজ আকারে (Page 1, Page 2, Page 3...) আসে, নির্দিষ্ট রেজাল্টটি প্রথম পেজের লিস্টেই পেয়ে গেলে পরের পেজের লিস্টগুলো নিয়ে আর লুপ ঘোরানোর দরকার পড়ে না:

# প্রথম পেজের সার্চ রেজাল্ট লিস্ট
page_1_results = [
    {"product_id": 501, "name": "Laptop Keyboard"},
    {"product_id": 502, "name": "Wireless Mouse"},
    {"product_id": 503, "name": "Gaming Headset"}
]

target_product_id = 502
found_item = None

for product in page_1_results:
    if product["product_id"] == target_product_id:
        found_item = product
        print(f"📦 Product found on Page 1: {product['name']}")
        break  # ২ নম্বর আইটেমেই পাওয়া গেছে, তাই প্রোডাক্ট ৩ আর চেক করার দরকার নেই




ফাইল ফরম্যাট ম্যাচিং বা সাপোর্ট চেক (Supported Format Check)
ইউজার যখন একাধিক অ্যাটাচমেন্ট পাঠায়, ব্যাকএন্ড যদি দেখে লিস্টের ভেতরে অন্তত একটি নিষিদ্ধ বা আনসাপোর্টেড ফাইল ফরম্যাট আছে, তবে ব্যাকএন্ড প্রসেস সাথে সাথে থামিয়ে দেয়:

uploaded_files = ["image1.jpg", "document.pdf", "script.exe", "image2.png"]
allowed_extensions = ["jpg", "png", "pdf"]

has_unsupported_file = False

for file in uploaded_files:
    file_ext = file.split(".")[-1] # ফাইলের এক্সটেনশন বের করা
    
    if file_ext not in allowed_extensions:
        print(f"🚨 Unsupported or unsafe file detected: '{file}'")
        has_unsupported_file = True
        break  # unsafe ফাইল পাওয়ার সাথে সাথেই স্ক্যানিং থামাও

if has_unsupported_file:
    print("❌ Upload Rejected: Unsafe file format detected.")



ওটিপি বা পাসওয়ার্ড চেষ্টা লিমিট (Brute-Force Protection)
লগইন সিকিউরিটির জন্য ইউজার যদি ভুল ওটিপি (OTP) বা পাসওয়ার্ড বারবার দিতে থাকে, ৩ বা ৫ বারের বেশি চেষ্টা করার সাথে সাথেই
লুপ বন্ধ করে অ্যাকাউন্ট সাময়িকভাবে লক করে দেওয়া হয়:


attempt_history = ["wrong_otp", "wrong_otp", "wrong_otp", "correct_otp"]
max_allowed_attempts = 3
failed_attempts = 0

for attempt in attempt_history:
    if attempt != "correct_otp":
        failed_attempts += 1
        
    if failed_attempts >= max_allowed_attempts:
        print("🔒 Account Locked! Exceeded maximum failed login attempts.")
        break  # ৩ বার ভুল ওটিপি দেওয়া শেষ, তাই সঠিক ওটিপি থাকলেও আর লুপ চলবে না

if failed_attempts < max_allowed_attempts:
    print("✅ Login Successful!")



🧠 মূল কথা (Core Summary):
লিস্টের ক্ষেত্রে break কেবল ২টি কারণেই সবচেয়ে বেশি লাগে:
১. Performance: যা খুঁজছেন তা পেয়ে গেলে পরেরগুলো চেক না করে সময় বাঁচানো।
২. Protection: এরর, বিপদ বা লিমিট পার হয়ে গেলে সামনের ক্ষতিকর ডাটাগুলো এক্সিকিউট হওয়া থেকে সিস্টেমকে রক্ষা করা।



# কোনো নির্দিষ্ট ইউজার আইডির ইনডেক্স খুঁজে বের করা
user_ids = [101, 204, 305, 408, 512]
search_target = 305
found_index = -1

for index in range(len(user_ids)):
    if user_ids[index] == search_target:
        found_index = index
        break  # উপাদান পাওয়া গেছে, বাকি ইনডেক্সগুলো ঘোরার দরকার নেই

print(f"Target found at index: {found_index}")  # Output: 2



Intermediate (শর্তসাপেক্ষ ফেইলসেফ ও ডিপ ডাটা সার্চ)
ডিটোরে ডিকশনারি যুক্ত লিস্ট (List of Dictionaries) থাকে। এখানে একাধিক ফিল্টার চেক করে ব্যাকএন্ডে প্রথম ম্যাচ করা ডাটাটি বের করা হয়।

# প্রথম খালি (Available) সার্ভার ব্যাকএন্ডের জন্য নির্বাচন করা
servers = [
    {"ip": "10.0.0.1", "status": "busy", "load": 95},
    {"ip": "10.0.0.2", "status": "down", "load": 0},
    {"ip": "10.0.0.3", "status": "healthy", "load": 30},
    {"ip": "10.0.0.4", "status": "healthy", "load": 10}
]

selected_server = None

for server in servers:
    # লোড ৫০% এর কম এবং হেলদি সার্ভার পেলেই বেছে নাও
    if server["status"] == "healthy" and server["load"] < 50:
        selected_server = server["ip"]
        break  # সবচেয়ে উপযুক্ত প্রথম সার্ভারটি পেয়ে গেলে লুপ বন্ধ

print(f"Allocated Server IP: {selected_server}")  # Output: 10.0.0.3


সিঙ্ক্রোনাইজেশন ফেইল-সেফ চেক (System Sync Safeguard)
দুটি ভিন্ন ডাটাবেস বা মাইক্রোসার্ভিসের ডাটা মেলানোর (Syncing) সময় যদি কোনো অসঙ্গতি (Discrepancy) ধরা পড়ে, 
তবে ভুল ডাটা সেভ হওয়া ঠেকাতে লুপ সাথে সাথে থামিয়ে দেওয়া হয়:

# ডাটাবেস এ এবং বি এর ইউজার আইডির লিস্ট
db_a_users = [1001, 1002, 1003, 1004, 1005]
db_b_users = [1001, 1002, 9999, 1004, 1005]  # 9999 ডাটাবেস এ-তে নেই (ম্যাচ করেনি)

sync_successful = True

for index in range(len(db_a_users)):
    if db_a_users[index] != db_b_users[index]:
        print(f"🚨 Data Mismatch at index {index}! DB-A: {db_a_users[index]} vs DB-B: {db_b_users[index]}")
        sync_successful = False
        break  # অমিল পাওয়া মাত্রই সিঙ্ক বাতিল, বাকিগুলো চেক করা ঝুঁকিপূর্ণ

if not sync_successful:
    print("❌ Synchronization Aborted: Database mismatch.")



এপিআই রেট-লিমিটিং স্পাইক প্রোটেকশন (DDoS Protection)
প্রতি মিনিটে এক একজন ইউজারের ট্রাফিক বা রিকোয়েস্ট গণনা করা হয়। কোনো আইপি নির্ধারিত লিমিটের (যেমন: ১০০ রিকোয়েস্ট)
বেশি স্পাইক করলে সাথে সাথে তার ট্রাফিক প্রসেসিং বন্ধ করে ফায়ারওয়ালে সংকেত পাঠানো হয়:



# এক মিনিটে ইউজারের রিকোয়েস্ট ট্র্যাকিং
request_timestamps = [1.2, 2.5, 3.1, 3.8, 4.0, 4.2]  # সেকেন্ড
max_requests_per_window = 5

request_count = 0

for req in request_timestamps:
    request_count += 1
    if request_count > max_requests_per_window:
        print(f"🚨 Rate Limit Exceeded! Request count hit {request_count}.")
        print("❌ Temporarily blocking IP for 15 minutes.")
        break  # লিমিট পার হয়ে গেছে, বাকি রিকোয়েস্টগুলো প্রসেস না করে সরাসরি ব্লক



ফাইল স্ট্রিমিং ও হেডার ভ্যালিডেশন (Malware Magic Byte Scanning)
সাইবার সিকিউরিটিতে কোনো ইউজার ফাইল আপলোড করলে ফাইলের প্রথম কয়েকটি বাইট (Magic Bytes) চেক করা হয়।
ফাইলটি আসল নাকি ভুয়া বা মেলওয়্যার তা চেক করার সময় কোনো ভুল ক্যারেক্টার পাইপলাইনে পেলেই প্রসেসিং থামানো হয়:

# একটি আপলোড করা ফাইলের প্রথম বাইট সিকোয়েন্স (List of bytes)
file_bytes = ["0xFF", "0xD8", "0xFF", "0x00"]  # আসল JPG ফাইলের শুরুর বাইট হতে হয় 0xFF 0xD8 0xFF 0xE0
expected_jpg_header = ["0xFF", "0xD8", "0xFF", "0xE0"]

is_valid_jpg = True

for i in range(len(expected_jpg_header)):
    if file_bytes[i] != expected_jpg_header[i]:
        print(f"🚨 Corrupted or Fake File Header at byte position {i}!")
        is_valid_jpg = False
        break  # ফাইলের হেডার ভুল, আর ভেতরের ডেটা চেক করার দরকার নেই

if not is_valid_jpg:
    print("❌ Security Alert: Upload rejected due to invalid file signature.")


ই-কমার্স স্টক ভ্যালিডেশন (Inventory Checkout Guard)
ইউজার যখন শপিং কার্টে থাকা একাধিক প্রোডাক্ট একসাথে চেকআউট (Buy) করতে চায়, ব্যাকএন্ড লিস্ট ঘুরে চেক করে।
যেকোনো একটা প্রোডাক্টের স্টক যদি 'Out of Stock' হয়, তবে সাথে সাথে কেনাকাটার লুপ বন্ধ করে অর্ডার রিজেক্ট করে দেওয়া হয়:


cart_items = [
    {"product": "Wireless Mouse", "stock": 15},
    {"product": "Mechanical Keyboard", "stock": 0},  # ❌ আউট অফ স্টক
    {"product": "Monitor Stand", "stock": 5}
]

can_checkout = True

for item in cart_items:
    if item["stock"] <= 0:
        print(f"⚠️ Cannot proceed with checkout: '{item['product']}' is out of stock!")
        can_checkout = False
        break  # ১টা প্রোডাক্ট স্টকে না থাকলে পুরো কার্টের কেনাকাটাই থেমে যাবে

if can_checkout:
    print("✅ Order placed successfully!")
else:
    print("❌ Checkout failed due to missing stock.")


ফাংশন (def) ছাড়া, শুধু বেসিক for লুপ, list এবং if-else দিয়ে সাজানো আরও ৪টি রিয়েল-ওয়ার্ল্ড ও ব্যাকএন্ড ইঞ্জিনিয়ারিং উদাহরণ নিচে দেওয়া হলো।

এই কোডগুলোতে কোনো জটিল ফাংশন ব্যবহার করা হয়নি, সাধারণ স্ক্রিপ্ট আকারেই লেখা হয়েছে:

১. সার্ভার মনিটরিং ও ক্র্যাশ অ্যালার্ট (Server Health Scan)
মাল্টিপল সার্ভারের স্টেটাস চেক করার সময় কোনো সার্ভার CRITICAL বা CRASHED পেলে মনিটরিং লুপ থামিয়ে সাথে সাথে সিস্টেম অ্যাডমিনকে অ্যালার্ট পাঠানো হয়:


server_statuses = ["ONLINE", "ONLINE", "HIGH_CPU", "CRITICAL", "ONLINE"]

system_healthy = True

for status in server_statuses:
    print(f"Checking server state: {status}")
    
    if status == "CRITICAL" or status == "OFFLINE":
        print("🚨 EMERGENCY: Critical server failure detected!")
        system_healthy = False
        break  # বাকি সার্ভার স্ক্যান না করে ক্র্যাশ হ্যান্ডলিং শুরু করো

if not system_healthy:
    print("❌ Monitoring stopped. Initiating failover protocol.")



সোশ্যাল মিডিয়া কমেন্ট ফিল্টার ও শ্যাডোব্যান (Spam Detection)
কোনো পোস্টের নিচে আসা কমেন্টের লিস্ট স্ক্যান করার সময় পরপর ক্ষতিকারক বা স্প্যাম লিঙ্ক পাওয়া গেলে সেই ইউজারের মন্তব্য সেকশন লক করে দেওয়া হয়:

user_comments = [
    "Great post!",
    "Thanks for sharing",
    "BUY CHEAP FOLLOWERS NOW -> http://spam.link",
    "Nice article"
]

has_spam = False

for comment in user_comments:
    if "http://" in comment or "BUY CHEAP" in comment:
        print(f"🚨 Spam comment detected: '{comment}'")
        has_spam = True
        break  # স্প্যাম পাওয়া গেছে, বাকি কমেন্ট প্রসেস না করে ইউজারকে ফ্ল্যাগ করো

if has_spam:
    print("❌ Post comments auto-flagged for review.")



পেমেন্ট গেটওয়ে ট্রানজেকশন স্ক্যানার (Suspicious Activity Guard)
গ্রাহকের পর পর হওয়া ট্রানজেকশনের অ্যামাউন্ট চেক করা। যদি কোনো একটা ট্রানজেকশন সিঙ্গেল কার্ড লিমিট (যেমন: ৫০,০০০ টাকা) পার করে যায়, 
তবে সাথে সাথে লুপ থামিয়ে পেমেন্ট গেটওয়ে স্থগিত করা হয়:

transaction_amounts = [1200, 3500, 8000, 75000, 2000]
single_tx_limit = 50000

suspicious_flag = False

for amount in transaction_amounts:
    if amount > single_tx_limit:
        print(f"🚨 Suspicious high-value transaction: {amount} BDT!")
        suspicious_flag = True
        break  # লিমিট ক্রস করেছে, পরবর্তী পেমেন্ট প্রসেসিং সাথে সাথে ব্লক

if suspicious_flag:
    print("❌ Card suspended due to unusual transaction size.")


ওটিপি ম্যাচিং এবং ব্রুট-ফোর্স প্রোটেকশন (OTP Verification)
লগইন সিকিউরিটিতে ডাটাবেসে বা ক্যাশে থাকা ওটিপির সাথে ইউজারদের দেওয়া সাবমিশনের লিস্ট মেলানো। সঠিক ওটিপি পাওয়ার সাথে সাথে লুপ বন্ধ করা:

submitted_otps = ["1122", "3344", "8921", "5566"]
correct_otp = "8921"

is_verified = False

for otp in submitted_otps:
    print(f"Verifying OTP: {otp}")
    
    if otp == correct_otp:
        print("✅ Correct OTP matched!")
        is_verified = True
        break  # সঠিক OTP পাওয়া গেছে, বাকিগুলো আর চেক করার প্রয়োজন নেই

if is_verified:
    print("🔓 User authenticated successfully.")


ফ্রি ট্রায়াল বা সাবস্ক্রিপশন মেয়াদ চেক (Subscription Expiry)
ইউজারের কেনা প্যাকেজগুলোর লিস্ট ব্যাকএন্ডে চেক করা হয়। কোনো একটা প্যাকেজ এক্সপায়ার্ড (Expired) বা ইনভ্যালিড ধরা পড়লে লুপ সাথে সাথে থামিয়ে প্রিমিয়াম ফিচার লক করা হয়:

user_packages = ["basic_plan", "pro_addon", "expired_subscription", "cloud_storage"]

has_expired_package = False

for package in user_packages:
    if "expired" in package:
        print(f"🚨 Invalid package found: '{package}'!")
        has_expired_package = True
        break  # এক্সপায়ার্ড প্যাকেজ পাওয়া গেছে, বাকী ফিচার চেক না করে এক্সেস ব্লক করো

if has_expired_package:
    print("❌ Access Restricted: Renewal Required.")



ইউজার প্রোফাইল পিকচার ফরম্যাট ও ভাইরাস স্ক্যান (File Security)
ইউজার একাধিক ছবি গ্যালারিতে আপলোড করার সময় ব্যাকএন্ড লিস্ট ঘুরে স্ক্যান করে। কোনো একটা ছবিতে আনসাপোর্টেড ফরম্যাট বা ভাইরাসের অস্তিত্ব পেলে সাথে সাথে স্ক্যানিং থামায়:


gallery_files = ["photo1.jpg", "photo2.png", "malicious_code.exe", "photo3.jpg"]
allowed_extensions = ["jpg", "png", "jpeg"]

has_virus = False

for file in gallery_files:
    extension = file.split(".")[-1]
    
    if extension not in allowed_extensions:
        print(f"🚨 Dangerous file type detected: '{file}'")
        has_virus = True
        break  # ঝুঁকিপূর্ণ ফাইল পাওয়ার সাথে সাথেই স্ক্যানার লুপ বন্ধ করে দেবে

if has_virus:
    print("❌ Upload Canceled: Dangerous file detected in list.")




ব্যাংক বা ওয়ালেট ক্যাশ-আউট লিমিট (Daily Withdrawal Limit)
কোনো ইউজার একদিনে যতগুলো ট্রানজেকশন করতে চাইছেন, সেই হিসেব করার সময় যদি দৈনিক উইথড্রয়াল লিমিট (যেমন: ৫০,০০০ টাকা) পার হয়ে যায়, তবে সাথে সাথে লুপ বন্ধ হয়ে যায়:


withdrawal_requests = [10000, 20000, 15000, 10000] # মোট ৫৫,০০০ টাকা
max_daily_limit = 50000

total_withdrawn = 0

for amount in withdrawal_requests:
    if total_withdrawn + amount > max_daily_limit:
        print(f"⚠️ Cannot process {amount} BDT. Daily limit of {max_daily_limit} BDT exceeded!")
        break  # ৫০,০০০ টাকা পার হয়ে যাওয়ায় পরবর্তী পেমেন্ট রিকোয়েস্ট আর যাবে না

    total_withdrawn += amount
    print(f"✅ Processed: {amount} BDT | Total so far: {total_withdrawn} BDT")


লগ ইন হিস্ট্রি থেকে ক্ষতিকারক আইপি ট্রেস (Security Fraud Analysis)
ইউজারের আগের কিছু লগইন আইপির লিস্ট স্ক্যান করে দেখা। কোনো ব্ল্যাকলিস্টেড বা ক্ষতিকারক আইপি দেখা মাত্রই লুপ বন্ধ করে অ্যাকাউন্টে সিকিউরিটি অ্যালার্ট ইমেইল পাঠানো:


login_ip_history = ["103.20.1.5", "103.20.1.9", "185.220.101.5", "103.20.1.12"]
blacklisted_ip = "185.220.101.5" # হ্যাকারের আইপি

suspicious_activity = False

for ip in login_ip_history:
    if ip == blacklisted_ip:
        print(f"🚨 Suspicious login detected from Blacklisted IP: {ip}")
        suspicious_activity = True
        break  # ৩ নম্বর আইপিতেই হুমকি পাওয়া গেছে, ৪ নম্বর চেক করা সময় নষ্ট

if suspicious_activity:
    print("📧 Security Alert Email sent to User!")



শপিং ডিসকাউন্ট কুপন ভ্যালিডেশন (Promotional System)
একজন গ্রাহক চেকআউটের সময় একাধিক কুপন কোড ব্যবহার করার চেষ্টা করছেন। ব্যাকএন্ড চেক করবে—যদি যেকোনো
একটি কুপন সম্পূর্ণ ভুয়া বা মেয়াদউত্তীর্ণ হয়, তবে সাথে সাথে লুপ থামিয়ে দেওয়া হবে এবং ডিসকাউন্ট বাতিল করা হবে:

    

applied_coupons = ["SAVE10", "WELCOME20", "FAKE_DEAL_99", "FREESHIP"]
valid_coupons = ["SAVE10", "WELCOME20", "FREESHIP"]

has_fraud_coupon = False

for coupon in applied_coupons:
    if coupon not in valid_coupons:
        print(f"🚨 Invalid or fraudulent coupon detected: '{coupon}'!")
        has_fraud_coupon = True
        break  # ফেক কুপন পাওয়া গেছে, বাকি কুপন আর চেক করার প্রয়োজন নেই

if has_fraud_coupon:
    print("❌ Checkout Error: Fraudulent coupon rejected.")




অনলাইন গেইমিং রুম ম্যাচমেকিং (Lobby Slot Finder)
অনলাইন গেমে প্লেয়ারকে কোনো ওপেন লবিতে বা রুমে বসানোর সময় সিস্টেম লবির লিস্ট ঘুরবে। 
খালি জায়গা (open) ওয়ালা প্রথম লবিটি পাওয়ার সাথে সাথেই খেলোয়াড়কে সেখানে জয়েন করিয়ে লুপ থামিয়ে দেবে:


game_lobbies = [
    {"room_id": 101, "status": "full"},
    {"room_id": 102, "status": "full"},
    {"room_id": 103, "status": "open"},
    {"room_id": 104, "status": "open"}
]

joined_room = None

for room in game_lobbies:
    if room["status"] == "open":
        joined_room = room["room_id"]
        print(f"🎮 Player connected to Room #{joined_room}")
        break  # রুম ১০৩ ফাকা পাওয়া গেছে, ১০৪ চেক না করে প্লেয়ারকে জয়েন করানো হলো





সার্ভার সিপিইউ লোড ব্যালেন্সিং (High Temperature Alert)
একটি ডেটা সেন্টারের সার্ভার র‍্যাকগুলোর তাপমাত্রা ট্র্যাক করা হচ্ছে। কোনো একটি সার্ভারের তাপমাত্রা বিপৎসীমা (যেমন: ৮৫ ডিগ্রি সেলসিয়াস) পার করলে সাথে সাথে অ্যালার্ম বাজিয়ে লুপ থামিয়ে দেওয়া হয়:

server_temperatures_celsius = [45, 52, 60, 88, 50]  # ৪ নম্বর সার্ভার ৮৮°C
max_safe_temp = 85

overheated = False

for temp in server_temperatures_celsius:
    if temp > max_safe_temp:
        print(f"🔥 DANGER: Server overheating detected at {temp}°C!")
        overheated = True
        break  # ৮৮ ডিগ্রি পাওয়ার সাথে সাথেই লুপ বন্ধ করে কুলিং সিস্টেম অন করো

if overheated:
    print("🚨 Emergency Alert: Emergency cooling fans activated!")




ডাটাবেস মাইগ্রেশন চেক (Schema Version Upgrade)
ডাটাবেসের ফিল্ড আপডেট বা মাইগ্রেশন করার সময় সিস্টেম একের পর এক টেবিল চেক করে। 
কোনো একটা টেবিলে ডাটাবেস করাপশন বা ইনকমপ্যাটিবিলিটি থাকলে প্রসেস সাথে সাথে থামিয়ে দেওয়া হয় যেন ডাটা নষ্ট না হয়:

database_tables = ["users", "orders", "corrupted_payments_table", "products"]

migration_failed = False

for table in database_tables:
    if "corrupted" in table:
        print(f"💥 Migration Error: Cannot update '{table}'!")
        migration_failed = True
        break  # সমস্যাযুক্ত টেবিল পাওয়া গেছে, পরবর্তী টেবিল আপডেট না করে স্টপ করো

if migration_failed:
    print("🔄 Migration Aborted: Restoring backup.")






List data type -continue

break এবং continue-এর মূল পার্থক্য:
break: শর্ত মিললেই লুপকে একদম বন্ধ করে বের করে দেয় (Stop Execution)।

continue: শর্ত মিললে কেবল বর্তমান আইটেমটিকে এড়িয়ে যায় বা স্কিপ করে এবং সাথে সাথে পরবর্তী আইটেমে চলে যায় (Skip & Move to Next)।


ইনভ্যালিড বা খালি ডাটা বাদ দেওয়া (Data Sanitization & Cleaning)
ইউজার বা ডাটাবেস থেকে পাওয়া লিস্টে অনেক সময় None, খালি স্পেস "", বা অবৈধ ডাটা থাকে। continue দিয়ে সেগুলো স্কিপ করে শুধু আসল ডাটা প্রসেস করা হয়:


raw_user_emails = ["sami@gmail.com", None, "", "abdullah@gmail.com", "   ", "karim@gmail.com"]
valid_emails = []

for email in raw_user_emails:
    # ডাটা যদি ফাঁকা (None) হয় বা শুধু স্পেস হয়, তবে স্কিপ করো
    if not email or email.strip() == "":
        continue  # নিচের কোডগুলো না চালিয়ে পরের ইমেইলে চলে যাও
        
    valid_emails.append(email.strip())

print(f"✅ Cleaned Email List: {valid_emails}")
# Output: ['sami@gmail.com', 'abdullah@gmail.com', 'karim@gmail.com']



নির্দিষ্ট রোল ফিল্টার করা (Role-Based Access Filtering)
একটি ইউজার লিস্ট থেকে নির্দিষ্ট রোল ছাড়া (যেমন: শুধু admin ছাড়া সাধারণ ইউজারদের) ইমেইল প্রসেস করতে চাইলে সাধারণ ইউজারদের স্কিপ করা হয়:


system_users = [
    {"username": "sami", "role": "admin"},
    {"username": "rahim", "role": "guest"},
    {"username": "abdullah", "role": "admin"},
    {"username": "karim", "role": "editor"}
]

for user in system_users:
    # ইউজার যদি এডমিন না হয়, তবে তাকে স্কিপ করো
    if user["role"] != "admin":
        continue
        
    print(f"📧 Sending System Report to Admin: {user['username']}")



ফ্রি ও পেইড ইউজার ডিফারেনশিয়েশন (Feature Access Guard)
সিস্টেমে যাদের ফ্রি সাবস্ক্রিপশন, তাদের জন্য হেভি কমপিউটেশনাল প্রসেস স্কিপ করে কেবল প্রিমিয়াম প্রসেস চালানো:

user_requests = [
    {"user": "User_A", "is_premium": True, "file_mb": 50},
    {"user": "User_B", "is_premium": False, "file_mb": 120},  # ❌ ফ্রি ইউজার, স্কিপ হবে
    {"user": "User_C", "is_premium": True, "file_mb": 10}
]

for req in user_requests:
    if not req["is_premium"]:
        print(f"⚠️ Skipping heavy processing for non-premium user: {req['user']}")
        continue  # ফ্রি ইউজার প্রসেস না করে পরের রিকোয়েস্টে যাও
        
    print(f"⚡ Processing HD file ({req['file_mb']} MB) for {req['user']}")


ব্যাচ প্রসেসিংয়ে এরর ওয়াচডগ (Fault-Tolerant Loop)
একাধিক ট্রানজেকশন প্রসেস করার সময় কোনো একটা ট্রানজেকশনে টেকনিক্যাল ভুল থাকলে পুরো প্রসেস না থামিয়ে (ভুল ফাইল স্কিপ করে) বাকি ট্রানজেকশন প্রসেস করা:


transactions = [100, -20, 500, 0, 350]  # -২০ এবং ০ হলো ইনভ্যালিড ট্রানজেকশন

processed_total = 0

for amount in transactions:
    if amount <= 0:
        print(f"🚨 Invalid transaction amount ({amount} BDT) skipped!")
        continue  # অবৈধ টাকা স্কিপ করে লুপ সচল রাখো
        
    processed_total += amount
    print(f"✅ Transaction processed: {amount} BDT")

print(f"💰 Total Successfully Processed: {processed_total} BDT")



লিস্টের সাথে continue (ইনভ্যালিড বা স্কিপ করার মতো ডাটা এড়ানো)
ধরা যাক, আপনার ব্যাকএন্ডে ইউজারদের একটি লিস্ট আছে, যেখানে কিছু ইউজার active, কিছু banned আর কিছু খালি/নাল (None) ডাটা। আপনি শুধু অ্যাক্টিভ ইউজারদের প্রসেস করতে:

users_list = [
    {"username": "abdullah", "role": "admin", "status": "active"},
    None,  # খালি বা ইনভ্যালিড ডাটা
    {"username": "hacker_123", "role": "guest", "status": "banned"},
    {"username": "sami", "role": "user", "status": "active"}
]

for user in users_list:
    # ডাটা ফাঁকা হলে বা ইউজারের স্ট্যাটাস 'active' না হলে স্কিপ করো
    if user is None or user["status"] != "active":
        print("⚠️ Inactive/Invalid user skipped.")
        continue  # লুপের বাকি অংশ স্কিপ করে পরের ইউজারে চলে যাবে
        
    print(f"✅ Processing active user: {user['username']}")


  ✅ Processing active user: abdullah
⚠️ Inactive/Invalid user skipped.
⚠️ Inactive/Invalid user skipped.
✅ Processing active user: sami



ব্যাচ ইমেইল বা নোটিফিকেশন ফিল্টারিং (Unsubscribed User Guard)
বাল্ক (Bulk) ইমেইল পাঠানোর সময় যেসকল ইউজার নোটিফিকেশন "Unsubscribe" বা "Mute" করে রেখেছেন, তাদের ইমেইল প্রসেস না করে স্কিপ করে বাকি ইউজারদের ইমেইল পাঠানো:

user_list = [
    {"name": "Sami", "email": "sami@gmail.com", "is_subscribed": True},
    {"name": "Rahim", "email": "rahim@gmail.com", "is_subscribed": False},  # ❌ Unsubscribed
    {"name": "Abdullah", "email": "abdullah@gmail.com", "is_subscribed": True}
]

for user in user_list:
    # ইউজার সাবস্ক্রাইব না করে থাকলে স্কিপ করো
    if not user["is_subscribed"]:
        print(f"⏩ Skipping {user['name']}: User unsubscribed from mailing list.")
        continue  # পরের ইউজারে চলে যাও
        
    print(f"📧 Promotional Newsletter sent to: {user['email']}")



এপিআই পে-লোড থেকে নির্দিষ্ট ফিল্ড বাদ দেওয়া (Sensitive Data Masking)
ইউজারের প্রোফাইল ডাটা ক্লায়েন্ট বা ফ্রন্টএন্ডে পাঠানোর আগে কিছু সিক্রেট ফিল্ড (যেমন: password, ssn, credit_card) বাদ দিয়ে বাকি ফিল্ডগুলো এক্সপোজ করা:


user_profile_fields = ["username", "email", "password_hash", "phone", "ssn_number"]
sensitive_fields = ["password_hash", "ssn_number"]

public_profile = []

for field in user_profile_fields:
    # সংবেদনশীল ফিল্ড হলে স্কিপ করো
    if field in sensitive_fields:
        print(f"🔒 Hiding sensitive field: {field}")
        continue
        
    public_profile.append(field)

print(f"✅ Public Profile Fields: {public_profile}")
# Output: ['username', 'email', 'phone']


ফাইল প্রসেসিংয়ে হিডেন বা সিস্টেম ফাইল স্কিপ করা (Storage Directory Cleanup)
সার্ভারের কোনো ডিরেক্টরি থেকে ফাইল প্রসেস করার সময় অপারেটিং সিস্টেমের হিডেন ফাইল (যেমন: .DS_Store, .git, .tmp) স্কিপ করে শুধু আসল ফাইলগুলো নিয়ে কাজ করা:

directory_files = ["report_2026.pdf", ".DS_Store", "data.csv", ".tmp_cache", "image.png"]

processed_files = []

for file in directory_files:
    # ডট (.) দিয়ে শুরু হওয়া হিডেন ফাইল বা টেম্পোরারি ফাইল স্কিপ করো
    if file.startswith(".") or file.endswith(".tmp_cache"):
        continue
        
    processed_files.append(file)
    print(f"⚙️ Processing file: {file}")

print(f"📂 Total Valid Files Processed: {len(processed_files)}")


ব্যাকএন্ড ই-কমার্স ইনভেন্টরি অটোমেশন (Skipping Low Profit Margin Products)
প্রোডাক্ট ক্যাটালগে একাধিক আইটেমের ওপর ক্যাশব্যাক বা ডিসকাউন্ট প্রসেস করার সময় যেসব প্রোডাক্টের দাম ১০০০ টাকার নিচে, সেগুলোকে ডিসকাউন্ট ক্যালকুলেশন থেকে স্কিপ করা:

product_prices = [1200, 450, 3200, 800, 5000] # BDT
discounted_prices = []

for price in product_prices:
    # ১০০০ টাকার কম হলে ডিসকাউন্ট স্কিপ করো
    if price < 1000:
        print(f"⏩ Skipping {price} BDT: Not eligible for discount.")
        continue
        
    new_price = price * 0.90  # ১০% ছাড়
    discounted_prices.append(new_price)
    print(f"🎉 Discount Applied: {price} BDT -> {new_price} BDT")


💡 continue শেখার মূল সামারি:
লিস্টের সাথে continue এর একমাত্র কাজ হলো "অপ্রয়োজনীয়, ক্ষতিকারক বা অযোগ্য ডাটাগুলোকে বাদ দিয়ে বাকি ডাটাগুলোর ওপর কাজ চালিয়ে যাওয়া।"



অ্যাডভান্সড ইউজ কেস: ফিল্টারিং বা ডেটা প্রসেসিং (Advanced Level)
বাস্তব জীবনের ব্যাকএন্ড প্রজেক্ট বা ডেটা ক্লিনিংয়ের সময় continue দিয়ে অপ্রয়োজনীয় ডেটা ফিল্টার করা হয়।

ধরা যাক, একটি সিস্টেমের ইউজারের লিস্ট থেকে শুধু ভ্যালিড ইউজারদের প্রসেস করতে হবে এবং কোনো ফাঁকা বা None ভ্যালু পেলে তা স্কিপ করতে হবে:

users = ["Abdullah", "Rahim", None, "Karim", "Sakib"]

for user in users:
    if user is None:
        # যদি ইউজার না থাকে বা ডেটা করাপ্টেড হয়, তবে প্রসেস স্কিপ করো
        continue  
    
    print(f"Processing data for: {user}")

# English comment: Filter out None values using continue in user processing pipeline


for লুপের সাথে continue-এর ব্যবহার (Intermediate Example)
ধরা যাক, আমরা ১ থেকে ৫ পর্যন্ত সংখ্যাগুলো প্রিন্ট করতে চাই, কিন্তু শর্ত হলো ৩ প্রিন্ট করা যাবে না, ৩ আসলে তা স্কিপ করে পরের সংখ্যায় চলে যাবে।

for i in range(1, 6):
    if i == 3:
        continue  # যখন i এর মান ৩ হবে, তখন এই সাইকেল স্কিপ করবে
    print(i)

# English comment: Skip printing when i equals 3 and continue the loop



while লুপের ক্ষেত্রে continue ব্যবহার করার সময় একটি ছোট বিষয়ে খুব সতর্ক থাকতে হয়—তা হলো ইনক্রিমেন্ট বা কাউন্টার আপডেট (increment)। 
আপডেট করার আগেই যদি লুপে continue চলে যায়, তবে লুপটি ইনফিনিট লুপ (Infinite Loop) হয়ে আটকে যেতে পারে।

num = 0

while num < 5:
    num += 1  # প্রথমে কাউন্টার বাড়িয়ে নেওয়া নিরাপদ
    
    if num == 3:
        continue  # ৩ আসলে প্রিন্ট না করে পরের ধাপে যাবে
        
    print(num)

# English comment: Skip printing the number 3 in while loop using continue



অ্যাডভান্সড ইউজ কেস: ফিল্টারিং বা ডেটা প্রসেসিং (Advanced Level)
বাস্তব জীবনের ব্যাকএন্ড প্রজেক্ট বা ডেটা ক্লিনিংয়ের সময় continue দিয়ে অপ্রয়োজনীয় ডেটা ফিল্টার করা হয়।

ধরা যাক, একটি সিস্টেমের ইউজারের লিস্ট থেকে শুধু ভ্যালিড ইউজারদের প্রসেস করতে হবে এবং কোনো ফাঁকা বা None ভ্যালু পেলে তা স্কিপ করতে হবে:

users = ["Abdullah", "Rahim", None, "Karim", "Sakib"]

for user in users:
    if user is None:
        # যদি ইউজার না থাকে বা ডেটা করাপ্টেড হয়, তবে প্রসেস স্কিপ করো
        continue  
    
    print(f"Processing data for: {user}")

# English comment: Filter out None values using continue in user processing pipeline




সিআরএম (CRM) সিস্টেম থেকে ডুপ্লিকেট কন্টাক্ট ফিল্টার করা
ডাটাবেস থেকে পাওয়া ফোন নম্বরের লিস্ট প্রসেস করার সময় যদি কোনো খালি ফোন নম্বর থাকে 
অথবা দেশের কান্ট্রি কোড (+880) দিয়ে শুরু না হয়, তবে সেটা স্কিপ করে শুধু সঠিক নম্বরগুলো ফরম্যাট করা:

phone_numbers = ["+8801711111111", "01822222222", "+8801933333333", "", "+8801544444444"]

formatted_numbers = []

for phone in phone_numbers:
    # ফাঁকা নম্বর বা দেশের কোড ছাড়া নম্বর এলে স্কিপ করো
    if not phone or not phone.startswith("+880"):
        print(f"⚠️ Invalid format skipped: '{phone}'")
        continue  # স্কিপ করে পরবর্তী নম্বরে চলে যাবে
        
    formatted_numbers.append(phone)
    print(f"✅ Verified Phone: {phone}")

print(f"📱 Cleaned Contact List: {formatted_numbers}")


অনলাইন লার্নিং প্ল্যাটফর্মে কোর্স প্রোগ্রেস ক্যালকুলেশন
ইউজার কোন কোন মডিউল শেষ করেছেন তা স্ক্যান করার সময়, যেসব মডিউল ইউজার এখনও শুরু করেননি (NOT_STARTED) 
সেগুলোকে স্কিপ করে শুধু সম্পন্ন করা (COMPLETED) মডিউলগুলোর স্কোর যোগ করা:

course_modules = [
    {"title": "Python Basics", "status": "COMPLETED", "score": 90},
    {"title": "Data Structures", "status": "NOT_STARTED", "score": 0},
    {"title": "Control Flow", "status": "COMPLETED", "score": 85},
    {"title": "Functions", "status": "IN_PROGRESS", "score": 40}
]

total_score = 0
completed_count = 0

for module in course_modules:
    # কমপ্লিট না হওয়া মডিউল স্কোর হিসেব থেকে বাদ দাও
    if module["status"] != "COMPLETED":
        print(f"⏩ Skipping module '{module['title']}': Status is {module['status']}")
        continue
        
    total_score += module["score"]
    completed_count += 1

print(f"🏆 Average Score on Completed Modules: {total_score / completed_count}%")



পেমেন্ট গেটওয়েতে রিফান্ড ক্যাশব্যাক প্রসেসিং
সার্ভারে আগের মাসের মোট ট্রানজেকশনের লিস্ট থেকে যেসব লেনদেন ইতিমধ্যে ক্যানসেলড (CANCELLED) বা রিফান্ডেড (REFUNDED), সেগুলোকে ক্যাশব্যাক ক্যালকুলেশন থেকে স্কিপ করা:

transactions = [
    {"id": "TX101", "amount": 1200, "status": "SUCCESS"},
    {"id": "TX102", "amount": 500, "status": "CANCELLED"},  # ❌ স্কিপ হবে
    {"id": "TX103", "amount": 3000, "status": "SUCCESS"},
    {"id": "TX104", "amount": 1500, "status": "REFUNDED"}   # ❌ স্কিপ হবে
]

cashback_given = 0

for tx in transactions:
    if tx["status"] != "SUCCESS":
        print(f"⏩ Transaction {tx['id']} skipped due to status: {tx['status']}")
        continue  # শুধুমাত্র সাকসেসফুল ট্রানজেকশনে ক্যাশব্যাক দেওয়া হবে
        
    cashback = tx["amount"] * 0.05  # ৫% ক্যাশব্যাক
    cashback_given += cashback
    print(f"🎉 5% Cashback applied to {tx['id']}: {cashback} BDT")

print(f"💰 Total Cashback Disbursed: {cashback_given} BDT")


আইওটি (IoT) সেন্সর ডাটা থেকে ভুল বা নয়েজ ডাটা বাদ দেওয়া
স্মার্ট সিটি বা আবহাওয়া কেন্দ্রের সেন্সর থেকে পাওয়া তাপমাত্রার রিডিং প্রসেস করার সময় সেন্সরের যান্ত্রিক ভুলের কারণে 
আসা চরম ভুল মান (যেমন: -৯৯৯ বা ১৫০ ডিগ্রি) স্কিপ করে আসল গড় তাপমাত্রা বের করা:

temperature_readings = [28.5, 29.1, -999.0, 30.2, 150.0, 27.8]  # -999.0 এবং 150.0 হলো নয়েজ/ভুল ডাটা

valid_readings = []

for temp in temperature_readings:
    # অসম্ভব বা অস্বাভাবিক তাপমাত্রা স্কিপ করো
    if temp < -50 or temp > 60:
        print(f"🚨 Sensor glitch detected! Ignoring reading: {temp}°C")
        continue
        
    valid_readings.append(temp)

avg_temp = sum(valid_readings) / len(valid_readings)
print(f"🌡️ Average Temperature: {avg_temp:.2f}°C")


সার্ভার লগ ফাইল থেকে এরর স্ক্যান করা (Warning and Info Ignore)
সার্ভারের শত শত লাইনের লগের ভেতর থেকে WARNING বা INFO টাইপ মেসেজগুলো স্কিপ করে 
শুধু আসল CRITICAL এবং ERROR মেসেজগুলো প্রিন্ট বা অ্যালার্ট পাঠানোর জন্য continue ব্যবহার করা হয়:

server_logs = [
    "[INFO] Server started on port 8080",
    "[WARNING] High memory usage detected",
    "[ERROR] Database connection failed!",
    "[INFO] User logged in",
    "[CRITICAL] Disk space full!"
]

for log in server_logs:
    # INFO এবং WARNING হলে স্কিপ করো, এগুলো ব্যাকএন্ড থামাবে না
    if log.startswith("[INFO]") or log.startswith("[WARNING]"):
        continue
        
    print(f"🚨 ALERT NEEDED: {log}")



ইউজার প্রোফাইল ডাটা সম্পন্নকরণ (Incomplete Profile Skip)
একটি ই-কমার্স সাইটে যেসকল ইউজারের শিপিং অ্যাড্রেস ফিল আপ করা নেই, তাদের ছাড়ের কুপন 
এসএমএস প্রসেসিং থেকে স্কিপ করে কেবল সঠিক অ্যাড্রেস থাকা ইউজারদের তালিকা তৈরি করা:


users = [
    {"name": "Sami", "address": "Dhaka", "phone": "01711111111"},
    {"name": "Rahim", "address": "", "phone": "01822222222"},      # ❌ অ্যাড্রেস নেই
    {"name": "Karim", "address": "Chittagong", "phone": "01933333333"}
]

for user in users:
    # অ্যাড্রেস না থাকলে স্কিপ করো
    if not user["address"]:
        print(f"⏩ Skipping {user['name']}: Missing delivery address.")
        continue
        
    print(f"📦 Shipping coupon sent to {user['name']} at {user['address']}")


  পাসওয়ার্ড স্ট্রেন্থ চেক (Weak Password Filter)
নতুন ইউজার তৈরির সময় বাল্ক ডাটা থেকে দুর্বল পাসওয়ার্ড (৮ ক্যারেক্টারের কম) থাকা অ্যাকাউন্টগুলোকে সিস্টেমে যুক্ত না করে স্কিপ করা:

user_passwords = ["pass123", "SuperSecure#2026", "12345", "BackendDev@890"]

strong_passwords = []

for password in user_passwords:
    # ক্যারেক্টার সংখ্যা ৮ এর কম হলে স্কিপ করো
    if len(password) < 8:
        print(f"⚠️️ Weak password rejected: '{password}'")
        continue
        
    strong_passwords.append(password)
    print(f"✅ Strong password accepted.")

print(f"Protected Accounts Count: {len(strong_passwords)}")



ই-কমার্স স্টক ডিসপ্লে (Out of Stock Products)
ফ্রন্টএন্ডে বা অ্যাপে প্রোডাক্ট ক্যাটালগ দেখানোর সময় যেসব প্রোডাক্টের স্টক শূন্য (0), সেগুলোকে প্রসেস বা ডিসপ্লে তালিকা থেকে স্কিপ করে শুধু কিনতে পাওয়া যাবে এমন প্রোডাক্ট রাখা:


products = [
    {"name": "Laptop", "stock": 5},
    {"name": "Mouse", "stock": 0},      # ❌ স্টক নেই
    {"name": "Keyboard", "stock": 12},
    {"name": "Monitor", "stock": 0}     # ❌ স্টক নেই
]

display_items = []

for product in products:
    if product["stock"] <= 0:
        continue  # স্টক ০ হলে স্কিপ
        
    display_items.append(product["name"])

print(f"🛒 Available for Purchase: {display_items}")


এপিআই পেজিনেশন এবং সফট-ডিলিটেড ডাটা স্কিপ (Soft-Delete Guard)
ডাটাবেস থেকে ডাটা সরাসরি মুছে না ফেলে অনেক সময় is_deleted = True দিয়ে রাখা হয় (Soft Delete)। 
ব্যাকএন্ড ইউজারকে ডাটা ফেরত পাঠানোর সময় এই সফট-ডিলিটেড ডাটাগুলোকে স্কিপ করে:


user_records = [
    {"id": 1, "name": "Sami", "is_deleted": False},
    {"id": 2, "name": "Rahim", "is_deleted": True},   # ❌ সফট ডিলিটেড ইউজার
    {"id": 3, "name": "Karim", "is_deleted": False}
]

active_users = []

for user in user_records:
    if user["is_deleted"]:
        print(f"⏩ Skipping deleted account ID: {user['id']}")
        continue  # মুছে ফেলা অ্যাকাউন্ট স্কিপ করে পরেরটা প্রসেস করো
        
    active_users.append(user["name"])

print(f"✅ Active User List: {active_users}")


ইউজার আপলোড ফাইল সাইজ ফিল্টারিং (File Size Threshold)
ইউজার যখন একাধিক ফাইল আপলোড করে, যে ফাইলগুলোর সাইজ নির্ধারিত মিনিমাম লিমিটের চেয়ে ছোট (যেমন: ০ বাইটের করাপ্টেড ফাইল বা খালি ফাইল), সেগুলোকে স্কিপ করা:


uploaded_file_sizes_kb = [250, 0, 1024, 5, 512]  # ০ এবং ৫ কেবি খালি/ভুল ফাইল

valid_uploads = []

for size in uploaded_file_sizes_kb:
    # ১০ কেবির চেয়ে ছোট ফাইল হলে স্কিপ করো
    if size < 10:
        print(f"⚠️ Skipping corrupted or empty file ({size} KB)")
        continue
        
    valid_uploads.append(size)

print(f"📂 Valid Uploaded Files: {valid_uploads} KB")



পেমেন্ট মেথড চেক (Unsupported Payment Gateway Skip)
ই-কমার্স চেকআউটের সময় গ্রাহকের নির্বাচিত পেমেন্ট পদ্ধতিটি ব্যাকএন্ডের বর্তমান কান্ট্রিতে সাপোর্টেড কি না চেক করা।
ইনঅ্যাক্টিভ বা আনসাপোর্টেড পেমেন্ট পদ্ধতি স্কিপ করে কেবল সচল চ্যানেলগুলো দেওয়া:

payment_gateways = [
    {"name": "bKash", "is_active": True},
    {"name": "PayPal", "is_active": False},  # ❌ বাংলাদেশে সরাসরি আনসাপোর্টেড
    {"name": "Nagad", "is_active": True}
]

available_methods = []

for gateway in payment_gateways:
    if not gateway["is_active"]:
        print(f"🔒 Gateway '{gateway['name']}' is disabled/unsupported.")
        continue  # অকার্যকর গেটওয়ে স্কিপ করো
        
    available_methods.append(gateway["name"])

print(f"💳 Active Payment Gateways: {available_methods}")


আইপি রেঞ্জ ফিল্টারিং ও লোকাল ট্রাফিক স্কিপ (External Audit Filter)
সার্ভারের ইনকামিং ট্রাফিকের আইপি স্ক্যান করার সময় অভ্যন্তরীণ বা লোকাল আইপি (127.0.0.1 বা localhost) 
প্রসেস না করে স্কিপ করে কেবল বাইরের পাবলিক আইপিগুলো সিকিউরিটি লগে যুক্ত করা:

incoming_ips = ["192.168.1.1", "127.0.0.1", "103.20.1.5", "localhost", "185.220.101.5"]

external_ips = []

for ip in incoming_ips:
    # ইন্টারনাল বা লোকাল আইপি হলে স্কিপ করো
    if ip == "127.0.0.1" or ip == "localhost" or ip.startswith("192.168"):
        continue
        
    external_ips.append(ip)

print(f"🌐 Public External IPs for Audit: {external_ips}")


রেট-লিমিটেড বা স্প্যাম আইপি ফিল্টার (Rate-Limit Skip)
সার্ভারে লগইন করার চেষ্টা করা আইপিগুলোর লিস্ট স্ক্যান করার সময় যেসকল আইপি ব্লকড বা স্প্যাম লিস্টে আছে, সেগুলোকে স্কিপ করে শুধু বৈধ আইপিগুলোর অ্যাক্সেস প্রসেস করা:

login_requests = [
    {"ip": "103.20.1.5", "status": "allowed"},
    {"ip": "185.220.101.5", "status": "blocked"},  # ❌ ব্লকড আইপি
    {"ip": "103.20.1.9", "status": "allowed"}
]

for request in login_requests:
    if request["status"] == "blocked":
        print(f"🚫 Skipping blocked IP: {request['ip']}")
        continue  # ব্লকড আইপি প্রসেস না করে পরের রিকোয়েস্টে চলে যাও
        
    print(f"✅ Processing authentication for IP: {request['ip']}")


ডাটা টাইপ ভ্যালিডেশন (Mixed List Processing)
কোনো এপিআই বা ক্লায়েন্ট থেকে আসা অনিয়মিত লিস্টের ভেতর ভুল বা ভিন্ন ডাটা টাইপ (যেমন: str বা None) থাকলে সেগুলো স্কিপ করে শুধু সংখ্যা (int বা float) নিয়ে হিসাব করা:


raw_metrics = [10.5, "invalid_data", 20.0, None, 15.5]

valid_sum = 0.0

for metric in raw_metrics:
    # যদি ডাটা সংখ্যা (int/float) না হয়, তবে স্কিপ করো
    if not isinstance(metric, (int, float)):
        print(f"⚠️ Non-numeric data skipped: {metric}")
        continue
        
    valid_sum += metric

print(f"📊 Sum of Valid Metrics: {valid_sum}")


ফাইল ব্যাকআপ সিঙ্ক্রোনাইজেশন (Already Synced Skip)
ক্লাউড স্টোরেজে ফাইল ব্যাকআপ নেওয়ার সময় যে ফাইলগুলো ইতিমধ্যে সিঙ্ক (synced) হয়ে গেছে, সেগুলোকে প্রসেস করা থেকে স্কিপ করে শুধু বাকি ফাইলগুলো আপলোড করা:


files_to_sync = [
    {"filename": "db_backup.sql", "synced": True},
    {"filename": "user_avatar.png", "synced": False},
    {"filename": "server_logs.txt", "synced": True}
]

for file_info in files_to_sync:
    if file_info["synced"]:
        continue  # সিঙ্ক করা থাকলে স্কিপ করো
        
    print(f"☁️ Uploading file to cloud: {file_info['filename']}")



ওটিপি রিসেন্ড টাইমআউট গার্ড (Resend Timeout Check)
ইউজারদের ওটিপি (OTP) পাঠনোর অনুরোধ প্রসেস করার সময় যেসব ইউজার গত ৬০ সেকেন্ডের মধ্যে ওটিপি চেয়েছেন, তাদের রিকোয়েস্ট স্কিপ করা (যাতে ওটিপি স্প্যাম না হয়):

otp_requests = [
    {"user_id": 101, "seconds_since_last_otp": 120},
    {"user_id": 102, "seconds_since_last_otp": 25},   # ❌ ৬০ সেকেন্ড পার হয়নি
    {"user_id": 103, "seconds_since_last_otp": 90}
]

for req in otp_requests:
    if req["seconds_since_last_otp"] < 60:
        print(f"⌛ Resend request skipped for User {req['user_id']}: Wait 60s.")
        continue
        
    print(f"📲 Sending new OTP to User {req['user_id']}")



ইউজার প্রোফাইল পিকচার স্ক্যানিংয়ে ডিফল্ট ছবি বাদ দেওয়া
প্রোফাইল পিকচারের পর্নোগ্রাফি বা মেটাডাটা স্ক্যান করার সময় যেসব ইউজার এখনও কোনো ছবি আপলোড 
করেননি (ডিফল্ট default_avatar.png ব্যবহার করছেন), তাদের স্ক্যানার লুপ থেকে স্কিপ করা:

profile_images = ["avatar_101.jpg", "default_avatar.png", "avatar_102.png"]

for img in profile_images:
    if img == "default_avatar.png":
        print("⏩ Skipping image scan: Default system avatar used.")
        continue  # ডিফল্ট ছবি স্ক্যান না করে পরেরটায় যাও
        
    print(f"🔍 Running AI Security Scan on: {img}")


পেমেন্ট মেথড ফিল্টারিং (Currency Mismatch Skip)
গ্রাহক যে কারেন্সিতে (যেমন: BDT) কেনাকাটা করছেন, পেমেন্ট গেটওয়ের লিস্ট থেকে 
অন্যান্য কারেন্সির (যেমন: USD, EUR) গেটওয়েগুলো স্কিপ করে কেবল সঠিক কারেন্সির গেটওয়ে ফিল্টার করা:


available_gateways = [
    {"name": "bKash", "currency": "BDT"},
    {"name": "Stripe_USD", "currency": "USD"},  # ❌ কারেন্সি ম্যাচ করেনি
    {"name": "Nagad", "currency": "BDT"}
]

cart_currency = "BDT"

for gateway in available_gateways:
    if gateway["currency"] != cart_currency:
        print(f"⏩ Skipping {gateway['name']}: Currency mismatch.")
        continue
        
    print(f"💳 Gateway available: {gateway['name']}")



টেক্সট ডাটা প্রসেসিংয়ে কমেন্ট লাইন স্কিপ করা
ডাটাবেস ব্যাকআপ বা কনফিগারেশন ফাইল লাইন বাই লাইন স্ক্যান করার সময় যেসব লাইন কমেন্ট (#) দিয়ে শুরু হয়, সেগুলো প্রসেস না করে স্কিপ করা:

config_lines = [
    "PORT=8080",
    "# This is a comment line",
    "DATABASE_URL=postgres://...",
    "# DEBUG_MODE=True"
]

parsed_config = []

for line in config_lines:
    # হ্যাশ (#) দিয়ে শুরু হওয়া কমেন্ট লাইন স্কিপ করো
    if line.startswith("#"):
        continue
        
    parsed_config.append(line)

print(f"⚙️ Active Configurations: {parsed_config}")
