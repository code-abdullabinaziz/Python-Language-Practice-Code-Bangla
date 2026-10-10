পাইথনেও জাভাস্ক্রিপ্ট বা C++ এর মতোই ফাংশনের ভেতরে Default Parameter ব্যবহার করা যায়।

🟢 ১. বেসিক ধারণা (Basic Concept):

যখন কোনো ফাংশন ডেফিনেশনে কোনো প্যারামিটারের সাথে = চিহ্ন দিয়ে আগে থেকেই একটি মান (Default Value) বসিয়ে রাখা হয়, তাকে Default Parameter বলে।

কাজ: ফাংশন কল করার সময় যদি সেই প্যারামিটারের জন্য কোনো ইনপুট (Argument) না দেওয়া হয়, পাইথন কোনো এরর না দিয়ে ওই ডিফল্ট মানটি ব্যবহার করে।


# Function Definition

def connect_server(port=8080, protocol="HTTP"):
    print(f"Connecting via {protocol} on Port: {port}")

# ১. কোনো আর্গুমেন্ট না দিলে ডিফল্ট মান ব্যবহার করবে 

connect_server()  
# Output: Connecting via HTTP on Port: 8080

# ২. মান দিলে পাঠানো মানটি ডিফল্ট মানকে ওভাররাইট (Override) করবে

connect_server(443, "HTTPS")  
# Output: Connecting via HTTPS on Port: 443




⚠️ ৩. সবচেয়ে গুরুত্বপূর্ণ নিয়ম (The Golden Rule):

পাইথনে Default Parameter লেখার সময় একটি বাধ্যতামূলক নিয়ম মানতে হয়—যাদের ডিফল্ট মান দেওয়া নেই (Non-default), 
তারা সবসময় আগে বসবে; আর যাদের ডিফল্ট মান দেওয়া আছে (Default), তারা সবসময় পরে বসবে।

def test(name, role="User"):  # সঠিক! সাধারণ প্যারামিটার আগে, ডিফল্ট পরে।
    pass





কেন এটি ব্যবহার করা হয়? (Why use it?):

১. কোড ছোট করে: বারবার একই মান প্যারামিটারে পাঠানো লাগে না। 
যেমন কোনো সিস্টেমে অধিকাংশ ইউজার যদি সাধারণ "User" হয়, তবে রোল বারবার লিখে না দিয়ে ডিফল্ট হিসেবে role="User" সেট করে দেওয়া যায়।

২. এরর (Error) বাঁচায়: ইউজার যদি কোনো ফিল্ড খালি রেখে ফাংশন কল করে, 
তবে প্রোগ্রাম ক্র্যাশ না করে স্বয়ংক্রিয়ভাবে ডিফল্ট মান নিয়ে কাজ চালিয়ে নেয়।



পরীক্ষার ফলাফল চেক করা (>= অপারেটর)
ধরে নিন, ডিফল্ট পাসের মার্ক হলো ৪০। কিন্তু শিক্ষক চাইলে ডিফল্ট মান পরিবর্তন করে অন্য মার্কও সেট করতে।


def check_result(score, pass_mark=40):
    if score >= pass_mark:
        return "Passed! مبارک ہو"
    else:
        return "Failed! Try again."

# ১. শুধু স্কোর দিলাম (ডিফল্ট pass_mark = 40 ব্যবহার হবে)

print(check_result(45))  
# আউটপুট: Passed! (কারণ 45 >= 40)

# ২. স্কোর এবং নতুন pass_mark দুটোই দিলাম (ডিফল্ট মান ওভাররাইট হলো)

print(check_result(32, pass_mark=30))  
# আউটপুট: Passed! (কারণ 32 >= 30)




গাড়ির গতি বা স্পিড চেক করা (> অপারেটর)
ধরে নিন, রাস্তার ডিফল্ট স্পিড লিমিট হলো ৮০। যদি স্পিড তার চেয়ে বেশি হয়, তবে অ্যালার্ট দিবে।

def speed_checker(current_speed, limit=80):
    if current_speed > limit:
        return "Warning: Over Speeding!"
    else:
        return "Speed is Safe."

# ১. শুধু কারেন্ট স্পিড দিলাম (ডিফল্ট limit = 80 ধরবে)

print(speed_checker(75))  
# আউটপুট: Speed is Safe. (কারণ 75 > 80 নয়)

# ২. হাইওয়ে জোন অনুযায়ী লিমিট বাড়িয়ে দিলাম

print(speed_checker(95, limit=100))  

# আউটপুট: Speed is Safe. (কারণ 95 > 100 নয়)



💡 মূল শিক্ষা:
ফাংশন কল করার সময় যদি দ্বিতীয় মানটি (Default Parameter) না পাঠানো হয়, 
তবে পাইথন স্বয়ংক্রিয়ভাবে আগের থেকে ঠিক করা সংখ্যাটি (যেমন: 40 বা 80) নিয়ে if-else কন্ডিশন চালায়।



ইউজার পারমিশন বা সিকিউরিটি লেভেল চেক করা (Cybersecurity / Backend RBAC)
সাইবার সিকিউরিটিতে যেকোনো সিস্টেমে ইউজারের রোল বা ক্লিয়ারেন্স লেভেল চেক করতে হয়। এখানে ডিফল্টভাবে ন্যূনতম সিকিউরিটি লেভেল ৩ সেট করা থাকল।

def verify_admin_access(user_level, min_required_level=3):
    if user_level >= min_required_level:
        return "Access Granted: Welcome to Admin Panel."
    else:
        return "Access Denied: Insufficient Privilege (Security Risk)!"

# ১. সাধারণ ইউজার লেভেল দিলাম (ডিফল্ট min_required_level = 3 ধরবে)

print(verify_admin_access(2))  
# আউটপুট: Access Denied! (কারণ 2 >= 3 নয়)

# ২. সুপার-অ্যাডমিন জোন, যেখানে রিকোয়ারমেন্ট বাড়িয়ে ৪ করা হলো

print(verify_admin_access(4, min_required_level=4))  

# আউটপুট: Access Granted! (কারণ 4 >= 4)



সার্ভার লোড বা রেট লিমিটিং চেক করা (System Architecture / API)
ব্যাকএন্ড সিস্টেমে একসাথে কতগুলো রিকোয়েস্ট আসছে তা মাপা হয়। ডিফল্ট ম্যাক্সিমাম লিমি트 ধরা যাক ৫০০। 
এর বেশি হলে সার্ভার ক্র্যাশ ঠেকাতে রিকোয়েস্ট ব্লক করতে হয়।


def check_server_load(active_connections, max_capacity=500):
    if active_connections > max_capacity:
        return "Alert: Server Overloaded! Trigger Rate Limiting."
    else:
        return "Status: Server load is normal. Traffic is safe."

# ১. বর্তমান কানেকশন ৪৫০ (ডিফল্ট capacity = 500)

print(check_server_load(450))  

# আউটপুট: Status: Server load is normal.

# ২. বিশেষ ইভেন্টের দিনে সার্ভার ক্যাপাসিটি বাড়িয়ে ২০০০ করা হলো

print(check_server_load(1200, max_capacity=2000))  

# আউটপুট: Status: Server load is normal. (কারণ 1200 > 2000 নয়)


🧠 কেন এগুলো ফিউচারে কাজে লাগবে?
যখন পাইথনের FastAPI দিয়ে ব্যাকএন্ড API বানাবেন, তখন ইউজারের সিকিউরিটি টোকেন যাচাই করতে বা সার্ভারের ট্রাফিক কন্ট্রোল করতে 
ঠিক এই ধরণের ফাংশন এবং কন্ডিশনাল লজিকগুলোই বারবার লিখতে হবে!




পাসওয়ার্ড লেন্থ বা সিকিউরিটি চেক (Cybersecurity)
সিস্টেমে অ্যাকাউন্ট খোলার সময় পাসওয়ার্ড স্ট্রং কি না তা চেক করতে এটি লাগে। ডিফল্ট মিনিমাম লেন্থ রাখা হলো ৮।

def is_password_secure(password, min_length=8):
    if len(password) >= min_length:
        return "Secure Password!"
    else:
        return "Too Short! Password must be longer."

# ১. সাধারণ রেজিস্ট্রেশন (ডিফল্ট min_length = 8)

print(is_password_secure("secret123"))  
# আউটপুট: Secure Password! (কারণ ৯ >= ৮)

# ২. ব্যাংকিং বা অ্যাডমিন জোন (যেখানে পাসওয়ার্ড মিনিমাম ১২ অক্ষরের হতে হবে)

print(is_password_secure("pass123", min_length=12))  

# আউটপুট: Too Short!


ডিসকাউন্ট বা প্রাইস ক্যালকুলেটর (Backend E-commerce Logic)
ই-কমার্স ওয়েবসাইটে কেনাকাটার বিল বানানোর লজিক। বিশেষ ডিসকাউন্ট না দিলে ডিফল্ট ডিসকাউন্ট ধরা থাকবে ০%।


def calculate_price(amount, discount_percent=0):
    final_price = amount - (amount * discount_percent / 100)
    
    if discount_percent > 0:
        return f"Discount Applied! Final Price: {final_price}"
    else:
        return f"Regular Price: {final_price}"

# ১. সাধারণ দিনে কেনাকাটা (ডিফল্ট discount_percent = 0)
print(calculate_price(1000))  
# আউটপুট: Regular Price: 1000

# ২. অফারের দিনে ২০% ডিসকাউন্ট দিলে
print(calculate_price(1000, discount_percent=20))  
# আউটপুট: Discount Applied! Final Price: 800.0




ডেটাবেস লিমিট কুরি (Database / API Pagination):

ব্যাকএন্ড থেকে যখন ডেটাবেসের ডাটা এনে স্ক্রিনে দেখানো হয়, 
তখন একবারে কতগুলো ডাটা আসবে তার একটা ডিফল্ট লিমিট থাকে। ধরে নিই ডিফল্টভাবে ১০টি ডাটা দেখাবে।



def get_user_list(requested_limit=10, max_allowed=100):
    # যদি হ্যাকার বা ইউজার ১০০টির বেশি ডাটা একবারে টেনে সার্ভার স্লো করতে চায়
    if requested_limit > max_allowed:
        return f"Blocked! You cannot request more than {max_allowed} items."
    else:
        return f"Fetching {requested_limit} users from Database."

# ১. স্বাভাবিক ইউজারের ডাটা রিকোয়েস্ট (ডিফল্ট ১০টি ধরবে)
print(get_user_list())  
# আউটপুট: Fetching 10 users from Database.

# ২. অনিয়মিত বড় রিকোয়েস্ট
print(get_user_list(requested_limit=500))  
# আউটপুট: Blocked! You cannot request more than 100 items.


