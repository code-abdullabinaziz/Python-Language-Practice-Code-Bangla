break হলো একটা keyword, যেটা for বা while loop এর ভিতরে ব্যবহার করলে loop টা 
সেই মুহূর্তেই শেষ হয়ে যায় এবং প্রোগ্রাম loop এর পরের লাইনে চলে যায়।

যখন কোনো লুপ (for লুপ বা while লুপ) চলতে থাকে, তখন স্বাভাবিক নিয়মে লুপটি তার শেষ পর্যন্ত চলার কথা। 
কিন্তু  যদি এমন কোনো শর্ত বা কন্ডিশন তৈরি করে দেন যেখানে লুপটি আর চালাতে চাচ্ছেন না,
তখন break ব্যবহার করলে পাইথন তাৎক্ষণিকভাবে সেই লুপটিকে থামিয়ে দেয় এবং লুপ থেকে পুরোপুরি বের হয়ে কোডের পরবর্তী লাইনে চলে যায়।


সাধারণ সিনট্যাক্স (Syntax):

for item in sequence:
    if condition:
        break  # শর্ত মিলে গেলে লুপ এখানেই থেমে যাবে



অ্যাকাউন্ট লকআউট সিস্টেম (Login Attempt Limit)
ব্যবহার: সিকিউরিটি সিস্টেম বা ব্যাকএন্ডে ইউজারকে ভুল পাসওয়ার্ড দিলে আবার দিতে বলা হয়, কিন্তু ৩ বার ভুল হলে অ্যাকাউন্ট লক করে বের করে দেওয়া হয়।


stored_password = "python123"
attempts = 0
max_attempts = 3

while True:  # ইনফিনিট লুপ (যতক্ষণ না break হচ্ছে চলতেই থাকবে)
    user_input = input("Enter your password: ")
    attempts += 1
    
    if user_input == stored_password:
        print("Login successful! Welcome to the dashboard.")
        break  # সঠিক পাসওয়ার্ড পেলে লুপ থামবে
    
    if attempts == max_attempts:
        print("Account locked! Too many failed attempts.")
        break  # ৩ বার ভুল করলে লুপ থামবে
        
    print(f"Incorrect password. Attempts left: {max_attempts - attempts}")


ব্যাখ্যা:

while True দিয়ে লুপটি শুরু করা হয়েছে কারণ ইউজার কতবারে সঠিক পাসওয়ার্ড দেবে তা আগে থেকে অজানা।

প্রথম breakটি কাজ করবে যখন ইউজার সঠিক পাসওয়ার্ড দেবে।

দ্বিতীয় breakটি কাজ করবে যখন ইউজার সর্বোচ্চ ৩ বার ভুল করবে, যাতে সে সারাদিন ভুল পাসওয়ার্ড ট্রাই করতে না পারে।


অনলাইন পেমেন্ট বা API কানেকশন রিট্রাই (Connection Retry)
ব্যবহার: ব্যাংকিং পেমেন্ট গেটওয়ে বা সার্ভারের সাথে কানেক্ট করার সময় নেটওয়ার্ক ড্রপ করলে ব্যাকএন্ড অটোমেটিক আবার চেষ্টা করে। কানেক্ট হয়ে গেলে লুপ থামিয়ে দেয়।

import random
import time

attempts = 0

while True:
    attempts += 1
    print(f"Attempting to connect to payment gateway... (Attempt {attempts})")
    
    # ডামি নেটওয়ার্ক রেসপন্স (র্যান্ডমলি True বা False তৈরি করছে)
    connection_success = random.choice([False, False, True])
    
    if connection_success:
        print("Payment processed successfully!")
        break  # পেমেন্ট সফল হলে সাথে সাথে লুপ বন্ধ
    
    if attempts == 5:
        print("Payment failed after 5 retries. Please try again later.")
        break  # ৫ বার চেষ্টা করে ব্যর্থ হলে থামবে
        
    time.sleep(1)  # ১ সেকেন্ড অপেক্ষা করে আবার চেষ্টা করবে


ব্যাখ্যা:

সার্ভারে বারবার ট্রাই করা হচ্ছে। connection_success == True হওয়া মাত্রই break দিয়ে লুপ থামিয়ে দেওয়া হয় যাতে নেটওয়ার্ক কানেকশন অযথা চালু না থাকে।

ব্যাকএন্ডে রিসোর্স বা মেমোরি বাঁচানোর জন্য এটি খুব গুরুত্বপূর্ণ প্র্যাকটিস।



শপিং কার্ট বা মেমোরি ক্লিয়ার প্রসেস (Item Processing)
ব্যবহার: অনলাইন শপে কাস্টমার অর্ডার কনফার্ম করলে ব্যাকএন্ড কার্ট থেকে একটা একটা করে আইটেম ডাটাবেজে স্টোর করে আর কার্ট খালি করে।

cart_items = ["Laptop", "Mouse", "Keyboard", "Headphone"]

while True:
    if len(cart_items) == 0:
        print("All items processed and order completed!")
        break  # কার্ট খালি হয়ে গেলে লুপ শেষ
        
    current_item = cart_items.pop(0)  # তালিকা থেকে প্রথম আইটেম বের করে নিচ্ছে
    print(f"Processing order for: {current_item}")


ব্যাখ্যা:

len(cart_items) == 0 হওয়া মাত্রই break ফায়ার করছে।

ব্যাকএন্ডে কিউ (Queue) বা ব্যাকগ্রাউন্ড জব প্রসেস করার ক্ষেত্রে এই লজিকটি প্রতিনিয়ত ব্যবহার করা হয়।




মূল শিক্ষণীয় বিষয় (Key Takeaways for Future):
১. while True এর সাথে সবসময় break রাখবেন: নতুবা প্রোগ্রাম কখনো থামবে না এবং সার্ভার ক্র্যাশ করতে পারে (Infinite Loop issue)।

২. শর্ত দুটি হতে পারে: ১) কাজ সফলভাবে সম্পন্ন হলে break, ২) সর্বোচ্চ চেষ্টায় ব্যর্থ হলে break (Fail-safe)।




এটিএম থেকে টাকা তোলা (ATM Cash Withdrawal)
ব্যবহার: আপনি যখন এটিএম বুথ থেকে টাকা তুলতে চান, ব্যাংকের ব্যাকএন্ড চেক করে আপনার অ্যাকাউন্টে পর্যাপ্ত ব্যালেন্স আছে কি না।

account_balance = 50000  # অ্যাকাউন্টে ৫০,০০০ টাকা আছে

while True:
    withdraw_amount = int(input("Enter withdrawal amount (0 to exit): "))
    
    if withdraw_amount == 0:
        print("Transaction cancelled. Have a nice day!")
        break  # ইউজার ০ চাপলে লেনদেন বাতিল হবে
        
    if withdraw_amount > account_balance:
        print("Insufficient balance! Try a lower amount.")
    else:
        account_balance -= withdraw_amount
        print(f"Please collect your cash: {withdraw_amount}")
        print(f"Remaining balance: {account_balance}")
        break  # টাকা তোলা সফল হলে লুপ থামবে


ব্যাখ্যা:

ইউজার ভুলবশত নিজের ব্যালেন্সের চেয়ে বেশি টাকা চাইলে তাকে আবার ইনপুট দিতে বলা হয় (লুপ থামে না)।

টাকা সঠিক থাকলে ব্যালেন্স থেকে বিয়োগ করে break দিয়ে এটিএম স্ক্রিন স্বাভাবিক মোডে নিয়ে আসা হয়।



সেন্সর ডাটা রিডিং / আইওটি (Temperature Warning System)
ব্যবহার: সার্ভার রুমের থার্মোমিটার সেন্সর প্রতি সেকেন্ডে তাপমাত্রা মাপতে থাকে। তাপমাত্রা বিপদসীমা অতিক্রম করলেই অ্যালার্ম দিয়ে মনিটরিং থামিয়ে দেয়।

import random

danger_temperature = 80  # ৮০ ডিগ্রি সেলসিয়াসের ওপরে গেলে ডেঞ্জার

while True:
    # সেন্সর থেকে ডামি তাপমাত্রা রিড করা হচ্ছে (৫০ থেকে ৯০ এর মধ্যে)
    current_temp = random.randint(50, 90)
    print(f"Current Server Temp: {current_temp}°C - Normal Operations")
    
    if current_temp >= danger_temperature:
        print(f"CRITICAL WARNING! Temperature reached {current_temp}°C. Shutting down server!")
        break  # তাপমাত্রা ৮০ ছাড়িয়ে গেলেই সার্ভার শাটডাউন লুপ ট্রিগার করবে

ব্যাখ্যা:

সার্ভারের তাপমাত্রা সেন্সর প্রতিনিয়ত ডাটা মাপছে (while True)।

বিপদসীমা (danger_temperature) স্পর্শ করা মাত্রই break ফায়ার করে জরুরি ব্যবস্থা গ্রহণ করে।



ইনভেন্টরি স্টক আউট চেক (Inventory Management)
ব্যবহার: ই-কমার্স সাইটে কোনো প্রোডাক্ট বিক্রি হতে হতে যখন স্টক শূন্য (Out of Stock) হয়ে যায়, তখন ব্যাকএন্ড লুপ থামিয়ে বাই বাটন ডিসেবল করে দেয়।


stock = 3  # স্টকে ৩টি প্রোডাক্ট আছে

while True:
    if stock == 0:
        print("Product is now OUT OF STOCK!")
        break  # স্টক শেষ হওয়ামাত্রই লুপ বন্ধ
        
    print(f"Product sold! Items left in stock: {stock - 1}")
    stock -= 1

ব্যাখ্যা:

প্রতিবার একটি প্রোডাক্ট বিক্রি হলে stock ১ করে কমে।

যখনই stock == 0 শর্ত সত্য হয়, সাথে সাথে break পুরো কেনাবেচার প্রসেসটি বন্ধ করে দেয়।



ডাটাবেজ ব্যাকআপ ও রেসপন্স টাইমআউট (Database Health Check)
ব্যবহার: ব্যাকএন্ড সার্ভার যখন প্রতিদিন রাতে ডাটাবেজ ব্যাকআপ নেওয়া শুরু করে, তখন ব্যাকআপ ফাইল তৈরি সম্পন্ন হওয়া পর্যন্ত অপেক্ষা করতে থাকে।
তবে ব্যাকআপ প্রসেস যদি নির্দিষ্ট টাইমের বেশি সময় ঝুলিয়ে রাখে, তখন সিস্টেম টাইমআউট কল করে প্রসেসটি কিল করে দেয়।

import time

backup_progress = 0
max_wait_time = 5  # সর্বোচ্চ ৫ সেকেন্ড অপেক্ষা করবে
seconds_passed = 0

while True:
    print(f"Backing up database... ({seconds_passed} seconds passed)")
    
    # ব্যাকআপ শেষ হলে break
    if backup_progress >= 100:
        print("Database backup completed successfully!")
        break
        
    # যদি ব্যাকআপ আটকে যায় এবং টাইমআউট হয়ে যায়
    if seconds_passed >= max_wait_time:
        print("Error: Backup timed out! Cancelling task.")
        break
        
    seconds_passed += 1
    backup_progress += 30  # প্রতি সেকেন্ডে ৩০% করে বাড়ছে
    time.sleep(1)

ব্যাখ্যা:
এখানে ২টি সুরক্ষা ব্যবস্থা আছে:
১. ব্যাকআপ ১০০% শেষ হলে সফলতা বার্তা দিয়ে break করবে।
২. কোনো কারণে ব্যাকআপ প্রসেস হ্যাং করলে ৫ সেকেন্ড পর টাইমআউট হয়ে মেমোরি খালি করার জন্য break করবে।



ইমেইল/ফোন নম্বর ফরম্যাট ভ্যালিডেশন (Valid User Input Collection)
ব্যবহার: রেজিস্ট্রেশন ফর্মে ইউজার যতক্ষণ না একটি সঠিক ইমেইল (যার মধ্যে @ এবং . চিহ্ন আছে) ইনপুট দিচ্ছে, ততক্ষণ তাকে আবার টাইপ করতে বলা হয়।

while True:
    user_email = input("Enter your email address: ").strip()
    
    # ইমেইলে '@' এবং '.' আছে কি না তা যাচাই করা
    if "@" in user_email and "." in user_email:
        print(f"Email '{user_email}' registered successfully!")
        break  # সঠিক ইমেইল পেলে লুপ থেকে বের হবে
    
    print("Invalid email format! Email must contain '@' and '.'. Please try again.\n")


ব্যাখ্যা:

ব্যাকএন্ডে বা সাইট ফর্মে ভুল ফরম্যাটের ডাটা যেন ডাটাবেজে ঢুকে সিস্টেম নষ্ট না করে, তাই ভুল ইনপুট দিলে লুপ চলতেই থাকে।

কেবল শর্ত সম্পূর্ণ সত্য ("@" in user_email and "." in user_email) হলেই break দিয়ে লুপ থামানো হয়।

ব্যাকএন্ডে while ও break ব্যবহারের গোল্ডেন রুলস:
Safety Exit (সেফটি এক্সিট): while True ব্যবহার করলে সব সময় অন্তত একটি break নিশ্চিত করবেন, নতুবা CPU ব্যবহার ১০০% হয়ে সার্ভার ডাউন হয়ে যাবে।

Resource Management: ডাটা পাওয়া মাত্রই বা কাজ শেষ হওয়া মাত্রই break দিয়ে মেমোরি ও প্রোসেসিং পাওয়ার বাঁচাবেন।



ওটিপি (OTP) ও সেশন এক্সপায়ারি ভ্যালিডেশন (OTP Verification)
ব্যবহার: ব্যাংকিং বা লগইনের সময় ফোনে ৪ ডিজিটের OTP পাঠানো হয়। 
ইউজারকে ৩ বার সুযোগ দেওয়া হয় এবং নির্দিষ্ট সময়ের মধ্যে ওটিপি না দিলে বা ভুল দিলে সেশন মেমোরি ক্লিয়ার করে দেওয়া হয়।

correct_otp = "4821"
attempts = 0
max_attempts = 3

while True:
    user_otp = input("Enter the 4-digit OTP sent to your phone: ")
    attempts += 1
    
    if user_otp == correct_otp:
        print("OTP verified successfully! Access granted.")
        break  # ওটিপি সঠিক হলে লুপ থামবে
        
    if attempts == max_attempts:
        print("Maximum OTP attempts reached! Transaction blocked.")
        break  # ৩ বার ভুল দিলে অ্যাকাউন্ট ব্লক করে বের হয়ে যাবে
        
    print(f"Incorrect OTP! Remaining attempts: {max_attempts - attempts}")

ব্যাখ্যা:

ব্যাংক অ্যাপে ভুল ওটিপি দিলে বারবার ট্রাই করতে দেয়, কিন্তু একটি লিমিট স্পর্শ করলেই সিকিউরিটির জন্য break দিয়ে প্রসেস ক্যানসেল করে দেয়।



পেজিনেশন বা ফাইল থেকে ডাটা পড়া (Fetching Data Pages)
ব্যবহার: সোশ্যাল মিডিয়া (যেমন: ফেসবুক বা ইউটিউব) ফিডে স্ক্রোল করার 
সময় ব্যাকএন্ড থেকে ১০টি করে পোস্ট আনা হয়। যখন আর কোনো নতুন পোস্ট থাকে না, তখন ব্যাকএন্ড লুপ থামিয়ে দেয়।


total_posts = 25  # ডাটাবেজে মোট ২৫টি পোস্ট আছে
fetched_posts = 0
page_size = 10    # প্রতিবারে ১০টি করে আনা হবে

while True:
    if fetched_posts >= total_posts:
        print("No more posts available on the server!")
        break  # সব পোস্ট ফেচ করা শেষ হলে লুপ থামবে
        
    fetched_posts += page_size
    print(f"Fetched {page_size} posts. Total posts loaded: {min(fetched_posts, total_posts)}")


ব্যাখ্যা:

ডাটাবেজ থেকে ডাটা চ্যাঙ্ক (Chunk) আকারে আনার সময় যখন
দেখার মতো আর নতুন কিছু থাকে না (fetched_posts >= total_posts), তখন অনর্থক সার্ভার রিকোয়েস্ট পাঠানো বন্ধ করতে break মারা হয়।

সার্ভার হেলথ চেক বা হার্টবিট সিস্টেম (Health Check Monitoring)
ব্যবহার: মূল সার্ভার ঠিকঠাক কাজ করছে কি না, তা দেখার জন্য একটি ব্যাকগ্রাউন্ড সার্ভিস প্রতি সেকেন্ডে চেক করে। 
যদি টানা ৩ বার সার্ভার কোনো রেসপন্স না দেয়, তবে মনিটরিং সিস্টেম ব্যাকআপ সার্ভার চালুর জন্য অ্যালার্ট ট্রিগার করে।

import random

consecutive_failures = 0

while True:
    # সার্ভারের রেসপন্স সিমুলেট করা (True = OK, False = Down)
    server_response = random.choice([True, False])
    
    if server_response:
        print("Server Health: OK")
        consecutive_failures = 0  # রেসপন্স পেলে ব্যর্থতার কাউন্ট জিরো হয়ে যাবে
    else:
        consecutive_failures += 1
        print(f"Server Unresponsive! Failure count: {consecutive_failures}")
        
    if consecutive_failures == 3:
        print("ALERT! Server is DOWN for 3 consecutive checks. Switching to backup server!")
        break  # ৩ বার রেসপন্স না পেলে মনিটরিং লুপ থামিয়ে ব্যাকআপ সার্ভার ট্রিগার করবে

ব্যাখ্যা:

সিস্টেম টানা ফেল করলে সিস্টেমে ইমার্জেন্সি হ্যান্ডলিং করার জন্য break দিয়ে লুপের বাইরে পাঠিয়ে অ্যালার্ট জেনারেট করা হয়।




while-else স্টেটমেন্ট (পাইথনের একটি স্পেশাল ফিচার)
পাইথনে লুপের সাথেও else ব্লক ব্যবহার করা যায়, যা অন্য অনেক ভাষায় নেই।

নিয়ম: যদি লুপটি স্বাভাবিকভাবে ঘুরে শেষ হয় (অর্থাৎ কোনো break ছাড়াই পুরো লুপ চলে), তবেই কেবল else ব্লকটি এক্সিকিউট হবে।
কিন্তু যদি লুপের ভেতরে break ফায়ার করে, তবে else ব্লক স্কিপ হয়ে যাবে।


# ডাটাবেজে ইউজার খোঁজার অ্যাডভান্সড লজিক:
users = ["monir", "faisal", "abdullah", "sabbir"]
search_user = "abdullah"

for user in users:
    if user == search_user:
        print(f"User '{search_user}' found in database!")
        break
else:
    # এই অংশটি কেবল তখনই চলবে যদি পুরো লুপে কোনো break না ঘটে (অর্থাৎ ইউজার না পাওয়া যায়)
    print(f"User '{search_user}' not found!")





try-except সহ while লুপ (Robust Error Handling)
বাস্তব প্রজেক্টে ইউজার ভুল ডাটা দিলে (যেমন: টেক্সট ইনপুট দিলে যেখানে সংখ্যা পাওয়ার কথা) প্রোগ্রাম যেন ক্র্যাশ না করে, 
তাই while এবং break-এর সাথে Exception Handling ব্যবহার করা হয়।

while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0:
            print(f"Valid age entered: {age}")
            break # ইনপুট সঠিক হলে লুপ থামবে
        else:
            print("Age must be greater than 0.")
    except ValueError:
        print("Invalid input! Please enter numbers only (e.g., 30).")



সাইবার সিকিউরিটি: এপিআই রেইট লিমিটিং (Rate Limiter)
ব্যবহার: ব্যাকএন্ড এপিআই-তে যেন কোনো হ্যাকার সেকেন্ডে হাজার হাজার রিকোয়েস্ট পাঠাতে না পারে (DDoS Attack), 
তাই সাইটে প্রতি মিনিটে ৫০টির বেশি রিকোয়েস্ট পাঠালে ব্লকিং সিস্টেম চালু হয়ে যায়।

request_count = 0
max_allowed_requests = 5  # ডেমো হিসেবে ৫টি ধরলাম

while True:
    # ইউজারের রিকোয়েস্ট আসছে...
    request_count += 1
    
    if request_count > max_allowed_requests:
        print("429 Too Many Requests! IP temporarily blocked for security.")
        break  # রিকোয়েস্ট লিমিট পার হলে তাকে ব্লক করে লুপ বন্ধ করবে
        
    print(f"Request {request_count} processed successfully (200 OK)")



ই-কমার্স কুপন ও ডিসকাউন্ট লিমিট (First 100 Users Discount)
ব্যবহার: কোনো ই-কমার্স প্ল্যাটফর্মে প্রথম ১০০ জন ক্রেতাকে কুপন ডিসকাউন্ট দেওয়া হবে।
কুপন ব্যবহারের কোটা শেষ হয়ে গেলে ব্যাকএন্ড ডিসকাউন্ট অ্যাপ্লাই করা বন্ধ করে দেবে।

available_coupons = 3  # ডেমো হিসেবে ৩টি কুপন দেওয়া হলো

while True:
    if available_coupons == 0:
        print("Sorry! All promotional coupons are claimed.")
        break  # কুপন শেষ হওয়া মাত্রই কুপন প্রসেসিং সিস্টেম থেমে যাবে
        
    print("Coupon applied! $10 discount granted.")
    available_coupons -= 1


রিয়েল-টাইম চ্যাট / নোটিফিকেশন সিস্টেম (Websocket Connection)
ব্যবহার: হোয়াটসঅ্যাপ, মেসেঞ্জার বা ফেসবুক নোটিফিকেশনের ব্যাকএন্ডে ব্যাকগ্রাউন্ডে একটি চ্যানেল সবসময় কানেক্টেড থাকে (while True) 
নতুন মেসেজ চেক করার জন্য। ইউজার যদি "Disconnect" চাপেন বা লগআউট করেন, তখন break দিয়ে কানেকশন কেটে দেওয়া হয়।

user_status = "Online"

while True:
    if user_status == "Offline":
        print("User logged out. Closing chat connection!")
        break  # ইউজার অফলাইন হয়ে গেলে চ্যাট সার্ভিস বন্ধ হবে
        
    print("Listening for new messages...")
    
    # ইউজার হঠাৎ অফলাইন হয়ে যাওয়ার সিমুলেশন
    user_status = "Offline"


  ক্রেডিট কার্ড / ট্রানজেকশন ফ্রড ডিটেকশন (Anti-Fraud System)
ব্যবহার: কোনো ক্রেডিট কার্ড থেকে এক টানা ৩ বার যদি অস্বাভাবিক অঙ্কের বড় লেনদেনের চেষ্টা করা হয়
(যেমন: হঠাৎ ৫০,০০০ টাকার বেশি), ব্যাংক ব্যাকএন্ড নিরাপত্তার খাতিরে কার্ডের ট্রানজেকশন সাময়িকভাবে হোল্ড করে দেয়।

suspicious_attempts = 0

while True:
    transaction_amount = int(input("Enter amount to transfer: "))
    
    if transaction_amount > 50000:
        suspicious_attempts += 1
        print(f"Warning: Large transaction attempt flag! ({suspicious_attempts}/3)")
    else:
        print("Transaction successful!")
        break  # স্বাভাবিক লেনদেন হলে কাজ শেষ
        
    if suspicious_attempts == 3:
        print("SECURITY ALERT! Account flagged for suspicious activity. Card blocked.")
        break  # টানা ৩ বার অস্বাভাবিক লেনদেন হলে কার্ড লক হবে


অ্যাসিঙ্ক ব্যাকগ্রাউন্ড টাস্ক প্রসেসিং (Job Queue Processing)
ব্যবহার: বড় বড় সাইটে (যেমন: ইউটিউবে ভিডিও আপলোডের পর রেন্ডারিং করা) ব্যাকগ্রাউন্ডে লাইন ধরে (Queue) কাজ জমতে থাকে। 
একটি করে কাজ শেষ হয়, আর যখন লাইনে আর কোনো কাজ বাকি থাকে না, তখন Worker প্রসেসটি বন্ধ করতে break মারা হয়।

job_queue = ["Render_Video_1.mp4", "Compress_Audio.mp3", "Send_Welcome_Email"]

while True:
    if len(job_queue) == 0:
        print("All background jobs finished! Queue is empty.")
        break  # কাজের লাইন খালি হয়ে গেলে ব্যাকগ্রাউন্ড প্রসেস বন্ধ
        
    current_job = job_queue.pop(0)  # লাইন থেকে প্রথম কাজ তুলে নেওয়া হচ্ছে
    print(f"Executing job: {current_job}")





উদাহরণ ১: Login (সর্বোচ্চ ৩ বার চেষ্টা)

correct_password = "python123"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")
    if password == correct_password:
        print("Login successful")
        break
    attempts += 1
    print(f"Wrong password. Attempts left: {3 - attempts}")
else:
    print("Account locked")

ব্যাখ্যা:

attempts গোনে কতবার চেষ্টা হয়েছে, while attempts < 3 সর্বোচ্চ ৩ বার সুযোগ দেয়।
password ঠিক হলে "Login successful" print হয় এবং break loop থামিয়ে দেয়।
ভুল হলে attempts ১ বাড়ে এবং কতবার সুযোগ বাকি সেটা দেখানো হয়।
৩ বারই ভুল হলে break চলেনি, তাই while-else এর else চলে এবং "Account locked" print হয়।
ভবিষ্যতে: login system, OTP verify, brute-force আটকানো।



উদাহরণ ২: Menu-driven প্রোগ্রাম

balance = 1000

while True:
    print("\n1. Check balance")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print("Balance:", balance)
    elif choice == "2":
        amount = int(input("Enter amount: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawn. New balance:", balance)
        else:
            print("Insufficient balance")
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid option")

ব্যাখ্যা:

while True মানে loop নিজে থামবে না, ইউজার যতক্ষণ না Exit বেছে নেয়।
ইউজারের পছন্দ অনুযায়ী if-elif-else দিয়ে কাজ ভাগ হয়।
"3" বেছে নিলে "Goodbye" print হয় এবং break পুরো প্রোগ্রাম থামিয়ে দেয়।
ভবিষ্যতে: CLI tool, ATM/bank simulation, admin menu।


উদাহরণ ৩: Valid input না পাওয়া পর্যন্ত জিজ্ঞেস করা

while True:
    age_text = input("Enter your age: ")

    if not age_text.isdigit():
        print("Please enter numbers only")
        continue

    age = int(age_text)
    if age < 0 or age > 120:
        print("Age must be between 0 and 120")
        continue

    print("Age accepted:", age)
    break

ব্যাখ্যা:

isdigit() দেখে ইনপুট শুধু সংখ্যা কিনা। না হলে error message দিয়ে continue আবার শুরুতে পাঠায়।
সংখ্যা হলে int এ রূপান্তর করে সীমা (০ থেকে ১২০) চেক হয়।
সব ঠিক থাকলে message দেখিয়ে break দিয়ে বের হয়ে যায়।
এখানে continue (ভুল হলে আবার চেষ্টা) আর break (ঠিক হলে থামা) একসাথে কাজ করেছে।
ভবিষ্যতে: form validation, registration input।



উদাহরণ ৪: Retry logic (Server/Database connection)

max_retries = 5
attempt = 1

while attempt <= max_retries:
    print(f"Connecting... attempt {attempt}")
    connected = (attempt == 3)   # ধরে নিচ্ছি ৩য় বারে সফল হয়

    if connected:
        print("Connected successfully")
        break

    print("Connection failed, retrying")
    attempt += 1
else:
    print("Could not connect after all retries")

ব্যাখ্যা:

সর্বোচ্চ ৫ বার সংযোগের চেষ্টা করা হয়।
এখানে connected কে নকল করা হয়েছে; বাস্তবে এখানে database বা API call থাকত।
সফল হলেই break দিয়ে retry বন্ধ হয়।
৫ বারই ব্যর্থ হলে else চলে এবং শেষ message দেখায়।
ভবিষ্যতে: database connect, external API call, email পাঠানো।


উদাহরণ ৫: Pagination (সব page না শেষ হওয়া পর্যন্ত ডেটা আনা)

page = 1
total_items = 0

while True:
    items_in_page = 10 if page <= 3 else 0   # ৩ page পর্যন্ত ডেটা আছে ধরে নেওয়া
    print(f"Page {page}: {items_in_page} items")

    if items_in_page == 0:
        print("No more data")
        break

    total_items += items_in_page
    page += 1

print("Total items:", total_items)

ব্যাখ্যা:

কত page আছে আগে জানা নেই, তাই while True ব্যবহার হয়েছে।
প্রতি page থেকে item আনা হয়; খালি page মানে ডেটা শেষ।
খালি এলে break দিয়ে থামা হয়, নাহলে page বাড়ে।
ভবিষ্যতে: API থেকে পেজ ভিত্তিক ডেটা আনা, বড় database পড়া।


উদাহরণ ৬: List এ প্রথম match খোঁজা

numbers = [3, 8, 12, 5, 20]
index = 0

while index < len(numbers):
    if numbers[index] > 10:
        print("First number greater than 10:", numbers[index])
        break
    index += 1
else:
    print("No number greater than 10")

ব্যাখ্যা:

index দিয়ে list এর একটা একটা করে সংখ্যা দেখা হয়।
12 প্রথম সংখ্যা যেটা 10 এর বেশি, তাই সেটা print করে break করে। 5 ও 20 চেক করা হয় না।
কোনো সংখ্যা না মিললে else চলে।
ভবিষ্যতে: search, প্রথম valid record খোঁজা।



উদাহরণ ৭: Task queue প্রসেস করা

tasks = ["send_email", "generate_report", "STOP", "backup_data"]
index = 0

while index < len(tasks):
    task = tasks[index]
    if task == "STOP":
        print("Stop signal received")
        break
    print("Processing:", task)
    index += 1

Output:

Processing: send_email
Processing: generate_report
Stop signal received


ব্যাখ্যা:

task গুলো একটা একটা করে প্রসেস হয়।
"STOP" এলে প্রসেসিং বন্ধ হয়; "backup_data" আর চলে না।
ভবিষ্যতে: background job, message queue, শর্ত অনুযায়ী প্রসেসিং বন্ধ করা।



উদাহরণ ৮: শর্ত পূরণ হলে থামা (Budget)

budget = 100
total = 0
prices = [30, 25, 20, 40, 10]
i = 0

while i < len(prices):
    if total + prices[i] > budget:
        print("Budget exceeded, stopping")
        break
    total += prices[i]
    print("Added:", prices[i], "Total:", total)
    i += 1

print("Final total:", total)


Output:

Added: 30 Total: 30
Added: 25 Total: 55
Added: 20 Total: 75
Budget exceeded, stopping
Final total: 75

ব্যাখ্যা:

প্রতিবার নতুন দাম যোগ করলে budget পার হবে কিনা আগে চেক হয়।
75 + 40 = 115, যা 100 এর বেশি, তাই break চলে।
ভবিষ্যতে: cart limit, credit limit, API quota।









মনে রাখার নিয়ম: while True + break তখন ব্যবহার করো যখন কতবার loop চলবে আগে থেকে জানা নেই, আর একটা নির্দিষ্ট ঘটনা ঘটলে থামতে চাও।

অনুশীলন: ইউজারের কাছ থেকে বারবার সংখ্যা নাও এবং যোগ করতে থাকো। 0 লিখলে break করে মোট যোগফল print("Total:", total) দিয়ে দেখা

total = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break

    total += number

print("Total:", total)

total = 0	                যোগফল জমা রাখার variable, শুরুতে ০
while True:	loop          নিজে থেকে থামবে না, শুধু break থামাতে পারবে
number = int(input(...))	ইউজারের কাছ থেকে সংখ্যা নিয়ে int এ রূপান্তর করা হয়
if number == 0:         	ইউজার ০ লিখেছে কিনা চেক
break	                    ০ লিখলে loop সাথে সাথে থেমে যায়
total += number	          ০ না হলে সংখ্যাটা total এ যোগ হয়
print("Total:", total)	  loop শেষ হওয়ার পর মোট যোগফল দেখায়


কেন total লুপের বাইরে ০ দিয়ে শুরু করা হয়েছে

total = 0 যদি loop এর ভিতরে লিখতে, তাহলে প্রতিবার আবার ০ হয়ে যেত এবং আগের যোগফল হারিয়ে যেত। তাই এটা loop এর বাইরে থাকে, 
যাতে প্রতিবার আগের মানের সাথে নতুন সংখ্যা যোগ হতে পারে।

একটা উন্নত ভার্সন (ভুল ইনপুট সামলানো)

ইউজার যদি সংখ্যার বদলে অক্ষর লেখে, int() error দেবে। try-except দিয়ে সেটা সামলানো যায়:

total = 0

while True:
    text = input("Enter a number (0 to stop): ")

    try:
        number = int(text)
    except ValueError:
        print("Invalid input. Please enter a number")
        continue

    if number == 0:
        break

    total += number

print("Total:", total)

ব্যাখ্যা:

int(text) ব্যর্থ হলে except চলে, error message দেখায় এবং continue দিয়ে আবার ইনপুট চায়।
সংখ্যা ঠিক হলে আগের মতোই ০ চেক এবং যোগ হয়।
এখানে break (০ এ থামা) আর continue (ভুল ইনপুটে আবার চেষ্টা) একসাথে কাজ করছে।


শেষে মোট কতটা সংখ্যা যোগ হয়েছে সেটাও দেখাতে একটা count variable যোগ করো, যেমন print("Count:", count)।

total = 0
count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break

    total += number
    count += 1

print("Total:", total)
print("Count:", count)

পরিবর্তন	       কাজ
count = 0    	 কয়টা সংখ্যা যোগ হয়েছে সেটা গোনার variable, শুরুতে ০
count += 1	   প্রতিবার একটা সংখ্যা যোগ হলে count ১ বাড়ে
print("Count:", count)	শেষে মোট কয়টা সংখ্যা যোগ হয়েছে দেখায়

count += 1 লেখা হয়েছে total += number এর ঠিক নিচে, if number == 0 এর বাইরে। তাই 0 লিখলে break চলে যায় এবং 0 কে গোনা হয় না। শুধু আসল সংখ্যাগুলোই গোনা হয়।



বোনাস: গড় (average) বের করা

total আর count দুইটা থাকলে সহজেই গড় বের করা যায়। তবে যদি ইউজার প্রথমেই 0 লেখে, তাহলে count = 0 হবে এবং ০ দিয়ে ভাগ করলে error আসবে। তাই আগে চেক করে নিতে হয়:

total = 0
count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break

    total += number
    count += 1

print("Total:", total)
print("Count:", count)

if count > 0:
    print("Average:", total / count)
else:
    print("No numbers were entered")

ব্যাখ্যা:

if count > 0 নিশ্চিত করে যে অন্তত একটা সংখ্যা দেওয়া হয়েছে।
তাহলে total / count দিয়ে গড় দেখানো হয়। উপরের উদাহরণে 18 / 3 = 6.0।
কোনো সংখ্যা না দিলে "No numbers were entered" দেখায়, ফলে ০ দিয়ে ভাগের error আসে না।
