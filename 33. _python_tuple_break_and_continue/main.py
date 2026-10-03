টুপল হলো ইনমিউটেবল (Immutable) বা অপরিবর্তনযোগ্য ডাটা স্ট্রাকচার। ব্যাকএন্ডে ফিক্সড কনফিগারেশন, 
রিড-অনলি রেকর্ড বা ডাটাবেস রো (Row) প্রসেস করার সময় লুপ থামানোর জন্য break ব্যবহৃত হয়।

💡 টুপলে break-এর কাজ:
লুপ চলার সময় নির্দিষ্ট কোনো শর্ত মিলে গেলে break পুরো লুপকে সাথে সাথে থামিয়ে দেয় এবং লুপের বাইরে চলে আসে।




টিউপল থেকে নির্দিষ্ট আইটেম খুঁজে পাওয়া এবং লুপ থামানো
ধরা যাক, আমাদের কাছে কিছু পণ্যের দামের একটি টিউপল আছে।
লুপ চালিয়ে দামগুলো চেক করব এবং যখনই নির্দিষ্ট কোনো দাম মিলে যাবে, তখনই break দিয়ে লুপটি চিরতরে বন্ধ করে দেব।

# A tuple containing product prices
prices = (100, 250, 500, 750, 1000)

# Iterate through the tuple using a for loop
for price in prices:
    if price == 500:
        print("Target price 500 found! Breaking the loop.")
        break  # Stop the loop immediately when 500 is found
    
    print(f"Checked price: {price}")

# English comment: Loop through the tuple and break execution upon finding the target value


Checked price: 100
Checked price: 250
Target price 500 found! Breaking the loop.




সিস্টেম ইউজার নেম চেক করা (Security Check)
সাইবার সিকিউরিটি বা ব্যাকএন্ড ডেভেলপমেন্টের একটি সাধারণ কাজ হলো অনুমোদিত ইউজারদের লিস্ট চেক করা। 
ধরুন আপনার সিস্টেমে ব্লক করা বা সাসপিসিয়াস (Suspicious) ইউজারের একটি টিউপল আছে। 
আপনি ইউজারের লিস্ট স্ক্যান করার সময় যখনই ব্লকড ইউজার পাবেন, তখনই সিকিউরিটি অ্যালার্ট দিয়ে লুপ ব্রেক করে দেবেন।


# A tuple of restricted or blocked usernames
blocked_users = ("hacker99", "admin_fake", "attacker_x", "spam_bot")

# Incoming login attempts or user list
incoming_users = ("john_doe", "alice", "attacker_x", "bob")

for user in incoming_users:
    if user in blocked_users:
        print(f"Alert! Blocked user found: {user}. Stopping further check.")
        break  # Stop checking immediately for security reasons
    
    print(f"User {user} is safe.")

# English comment: Iterate through incoming users and break the loop if a security threat (blocked user) is detected


User john_doe is safe.
User alice is safe.
Alert! Blocked user found: attacker_x. Stopping further check.


  

ডেটা সার্চিং এবং পজিশন বা ইনডেক্স খুঁজে বের করা
ধরুন একটি গেমের লেভেলের স্কোরের টিউপল থেকে কোনো একটি বিশেষ স্কোর বা টার্গেট খুঁজে বের করতে চান এবং পেলে লুপ বন্ধ করে দিতে:

# A tuple of player scores across different stages
scores = (45, 60, 85, 90, 100, 75)

target_score = 90

for score in scores:
    if score == target_score:
        print(f"Target score {target_score} achieved! Stopping the game session.")
        break  # Exit the loop once the target is reached
    
    print(f"Current score evaluated: {score}")

# English comment: Search for a target score inside a score tuple and break when found


Current score evaluated: 45
Current score evaluated: 60
Current score evaluated: 85
Target score 90 achieved! Stopping the game session.



শপিং কার্ট বা ই-কমার্স ইনভেন্টরি চেক (Stock Out Check)
ধরুন কোনো ই-কমার্স সাইটে কোনো পণ্যের সাইজ বা ভ্যারিয়েন্ট স্টক আউট (Stock out) আছে কি না তা চেক করা হচ্ছে।
টিউপলের ভেতরে স্টক স্ট্যাটাস দেওয়া আছে (True মানে অ্যাভেইলেবল, False মানে স্টক শেষ)। 
যখনই কোনো আইটেম False পাবে, লুপ থামিয়ে অর্ডার প্রসেসিং হোল্ড করে দেওয়া হবে।


# A tuple representing stock availability of product sizes (Small, Medium, Large, XL)
stock_status = (True, True, False, True)

size_names = ("Small", "Medium", "Large", "XL")

# Loop through the stock status tuple
for i in range(len(stock_status)):
    if stock_status[i] == False:
        print(f"Sorry! Size {size_names[i]} is out of stock. Stopping order process.")
        break  # Stop checking further sizes if one item is out of stock
    
    print(f"Size {size_names[i]} is available.")

# English comment: Check stock availability from a tuple and break the loop if an item is out of stock

Size Small is available.
Size Medium is available.
Sorry! Size Large is out of stock. Stopping order process.



পাসওয়ার্ড বা পিন কোড ভ্যালিডেশন (Max Attempts Limit)
ব্যাংকিং সিস্টেম বা লগইন পোর্টালে অনেক সময় ইউজার ভুল পিন বা পাসওয়ার্ড দিলে একটি নির্দিষ্ট লিমিটের পর লক করে দেওয়া হয়। 
ধরুন সঠিক পিনের একটি টিউপল সিকিউরড সিস্টেমে সেভ করা আছে, 
এবং ইউজার ইনপুট ম্যাচ না করলে বা ভুল পিন বারবার দিলে সিকিউরিটির জন্য লুপ ব্রেক করে দেওয়া হয়।


# A tuple of predefined valid system passcodes or keys
valid_keys = (1024, 2048, 4096)

# User input attempts sequence
user_attempts = (1111, 2048, 4096)

for attempt in user_attempts:
    if attempt not in valid_keys:
        print(f"Invalid key attempt: {attempt}. Security alert triggered, breaking loop.")
        break  # Break the loop on the first invalid/unauthorized attempt
    
    print(f"Access granted for key: {attempt}")

# English comment: Validate user attempts against a tuple of valid keys and break on security violation


Invalid key attempt: 1111. Security alert triggered, breaking loop.


সার্ভার রেসপন্স কোড চেক (API Status Checking)
ব্যাকএন্ড ডেভেলপমেন্টে আমরা প্রায়ই থার্ড-পার্টি এপিআই (API) বা সার্ভার থেকে সিকোয়েন্সিয়াল রেসপন্স কোড পাই। যদি কোনো কারণে সার্ভার থেকে ৫০০ বা তার বেশি কোনো এরর কোড (500 Internal Server Error) আসে, 
তবে আর সামনে না এগিয়ে সাথে সাথে প্রসেসিং বন্ধ করে দেওয়া উচিত।


# A tuple of server response status codes from sequential API requests
response_codes = (200, 200, 201, 500, 200)

for code in response_codes:
    if code >= 500:
        print(f"Server Error detected (Status: {code}). Breaking connection pipeline.")
        break  # Stop processing further requests if a server crash or critical error occurs
    
    print(f"Request successful with status: {code}")

# English comment: Process server response codes from a tuple and break on server error

Request successful with status: 200
Request successful with status: 200
Request successful with status: 201
Server Error detected (Status: 500). Breaking connection pipeline.


ফাইল আপলোড সিকিউরিটি স্ক্যান (File Extension Validation)
ওয়েব অ্যাপ্লিকেশনে ইউজাররা যখন ফাইল আপলোড করে, তখন সাইবার সিকিউরিটির অংশ হিসেবে ফাইলের এক্সটেনশন চেক করতে হয়। 
যদি কোনো ক্ষতিকারক এক্সটেনশন (যেমন—.exe বা .bat) পাওয়া যায়, তবে আপলোড প্রসেস সাথে সাথে টার্মিনেট বা ব্লক করে দিতে হয়।


# A tuple representing uploaded file names in a web application
uploaded_files = ("index.html", "script.js", "malware.exe", "style.css")

# A tuple of restricted or malicious file extensions
restricted_extensions = (".exe", ".bat", ".sh")

for file in uploaded_files:
    if file.endswith(restricted_extensions):
        print(f"Security Alert! Malicious file extension detected: {file}. Stopping upload.")
        break  # Terminate the upload process immediately for security
    
    print(f"File {file} is safe to process.")

# English comment: Scan files in a tuple and break the loop if a restricted extension is found

File index.html is safe to process.
File script.js is safe to process.
Security Alert! Malicious file extension detected: malware.exe. Stopping upload.

  

সিস্টেম কনফিগারেশন চেকার (Critical Security Check)
সার্ভার স্টার্ট হওয়ার আগে ফিক্সড এনভায়রনমেন্টাল ভ্যালু চেকের সময় কোনো সিকিউরিটি রিস্ক পাওয়া গেলে লুপ থামিয়ে দেওয়া:

# রিড-অনলি সিস্টেম কনফিগারেশন টুপল
server_configs = (
    ("PORT", 8080),
    ("SSL_ENABLED", True),
    ("DEBUG_MODE", True),  # 🚨 প্রোডাকশনে DEBUG মোড True থাকা সিকিউরিটি রিস্ক!
    ("DATABASE_URL", "postgres://...")
)

for key, value in server_configs:
    if key == "DEBUG_MODE" and value is True:
        print(f"🚨 Security Alert: {key} is enabled! Shutting down server startup.")
        break  # কনফিগারেশন ঝুঁকিপূর্ণ তাই লুপ থামিয়ে দেওয়া হলো
        
    print(f"✅ Verified config: {key} = {value}")


ডাটাবেস রেকর্ড অনুসন্ধান (ReadOnly Tuple Search)
ডাটাবেস থেকে আসা একটি নির্দিষ্ট রো (Row)-এর ভেতর টার্গেট ইউজার আইডি পাওয়ার সাথে সাথে স্ক্যান বন্ধ করা:


# ডাটাবেস রো রেকর্ড (ID, Username, Role)
user_records = (
    (101, "sami", "admin"),
    (102, "abdullah", "developer"), # 🎯 টার্গেট আইডি
    (103, "rahim", "guest"),
    (104, "karim", "user")
)

target_id = 102
found_user = None

for user in user_records:
    if user[0] == target_id:
        found_user = user
        print(f"🎯 Target user found: {user[1]} ({user[2]})")
        break  # ইউজার পেয়ে গেছি, তাই বাকি রোগুলো আর খোঁজার দরকার নেই

print(f"Searched Result: {found_user}")


এপিআই রেট লিমিট ব্রেকার (API Quota Protection)
ফিক্সড ডেইলি রিকোয়েস্ট কোটা শেষ হয়ে গেলে ব্যাকএন্ডে এপিআই কল করার লুপ সাথে সাথে বন্ধ করা:

# ৩টি থার্ডপার্টি এপিআই কী-এর ফিক্সড টুপল
api_keys = ("key_alpha", "key_beta", "key_gamma")
max_quota_per_key = 100
current_usage = 100  # কোটা পূর্ণ হয়ে গেছে

for key in api_keys:
    if current_usage >= max_quota_per_key:
        print(f"⚠️ Daily quota limit reached for API key '{key}'! Stopping calls.")
        break  # কোটা শেষ, পরবর্তী রিকোয়েস্ট ব্লক করা হলো


পেমেন্ট গেটওয়ে ফলব্যাক ট্রাই (Payment Channel Recovery)
সার্ভারে একাধিক ব্যাকআপ পেমেন্ট চ্যানেল দিয়ে রিকোয়েস্ট পাঠানোর সময় প্রথম সফল পেমেন্ট পাওয়া মাত্রই লুপ বন্ধ করা:

payment_channels = ("bKash_Gateway", "Nagad_Gateway", "Rocket_Gateway")

for channel in payment_channels:
    print(f"🔄 Attempting transaction via {channel}...")
    
    # ধরি Nagad চ্যানেল দিয়ে পেমেন্ট সফল হয়েছে
    if channel == "Nagad_Gateway":
        print(f"✅ Payment successful using {channel}!")
        break  # পেমেন্ট হয়ে গেছে, তাই পরের চ্যানেলে চেষ্টা করার দরকার নেই


ডেটাবেস কানেকশন পুল ফেলওভার (Connection Pool Failover)
সার্ভার থেকে বিভিন্ন ব্যাকআপ ডেটাবেস হোস্টের ফিক্সড টুপল স্ক্যান করার সময় প্রথম সক্রিয়/লাইভ কানেকশনটি পাওয়া মাত্রই লুপ থামিয়ে দেওয়া:

# অপরিবর্তনযোগ্য (Immutable) ডেটাবেস হোস্ট টুপল
db_hosts = ("db_primary.internal", "db_replica_1.internal", "db_replica_2.internal")

connected_host = None

for host in db_hosts:
    print(f"🔌 Testing connection to {host}...")
    
    # ধরি Replica 1 সার্ভারে কানেকশন সফল হয়েছে
    if host == "db_replica_1.internal":
        connected_host = host
        print(f"✅ Connection established with {host}!")
        break  # কানেকশন পেয়ে গেছি, তাই বাকি হোস্টগুলোতে আর হিট করার প্রয়োজন নেই


ফাইল এক্সটেনশন সিকিউরিটি স্ক্যান (Strict File Whitelist)
ইউজারের আপলোড করা ফাইলের এক্সটেনশন চেক করার সময় যদি এমন কোনো এক্সটেনশন পাওয়া যায় যা অনুমোদিত নয় (যেমন: .exe বা .sh), তবে সিকিউরিটি অ্যালার্ট দিয়ে ফাইল প্রসেসিং লুপ থামিয়ে দেওয়া:

# আপলোড হওয়া ফাইলের মেটাডাটা টুপল (FileName, Extension, Size_KB)
uploaded_file_info = ("user_report", ".exe", 2048)
allowed_extensions = (".pdf", ".docx", ".xlsx", ".png", ".jpg")

file_ext = uploaded_file_info[1]

for ext in allowed_extensions:
    if file_ext not in allowed_extensions:
        print(f"🚨 Dangerous file format detected: '{file_ext}'! Processing terminated.")
        break  # ক্ষতিকর এক্সটেনশন পাওয়ায় প্রসেসিং বন্ধ


ট্রানজেকশন হ্যাশ ম্যাচিং (Cryptographic Hash Audit)
ব্লকচেইন বা ব্যাংকিং লেজারের ফিক্সড ট্রানজেকশন টুপল স্ক্যান করার সময় নির্দিষ্ট ট্রানজেকশন হ্যাশ (Hash) মিলে গেলে স্ক্যানিং বন্ধ করা:

# ফিক্সড ব্লক ট্রানজেকশন টুপল
block_transactions = (
    "0xabc1234...",
    "0x987xyz6...",  # 🎯 টার্গেট ট্রানজেকশন
    "0x456def7...",
    "0x789ghi8..."
)

target_hash = "0x987xyz6..."

for tx_hash in block_transactions:
    if tx_hash == target_hash:
        print(f"🎯 Transaction match found in block: {tx_hash}")
        break  # হ্যাশ মিলে গেছে, তাই পরবর্তী হ্যাশ স্ক্যান করার দরকার নেই


ব্যাকএন্ড লোকলাইজেশন / ভাষা নির্বাচন (Language Preference Fallback)
ক্লায়েন্ট রিকোয়েস্টের হেডার থেকে পাওয়া ইউজারের পছন্দের ভাষার তালিকা স্ক্যান করার সময় ব্যাকএন্ডে প্রথম যে ভাষাটি সাপোর্টেড পাবে, সেটি সেট করে লুপ থেকে বের হয়ে যাওয়া:

# ইউজারের পাঠানো পছন্দের ভাষাগুলোর টুপল
user_languages = ("bn-BD", "en-US", "fr-FR")
supported_languages = ("en-US", "es-ES", "ar-SA")

selected_lang = "en-US"  # Default Fallback

for lang in user_languages:
    if lang in supported_languages:
        selected_lang = lang
        print(f"🌐 Server language set to: {selected_lang}")
        break  # পছন্দের প্রথম ম্যাচ পাওয়া গেছে, লুপ স্টপ


রোল-বেসড এক্সেস কন্ট্রোল (RBAC Admin Permission Check)
ইউজারের পারমিশন টুপল স্ক্যান করার সময় যদি সিস্টেম কোনো ঝুঁকিপূর্ণ বা সুপার-অ্যাডমিন 
পারমিশন (SUPER_ADMIN বা SYSTEM_DELETE) খুঁজে পায়, তবে সাথে সাথে লুপ থামিয়ে সিকিউরিটি অডিট রিপোর্ট তৈরি করা:

# ইউজার পারমিশনের ফিক্সড টুপল
user_permissions = ("READ_DATA", "WRITE_DATA", "SYSTEM_DELETE", "UPDATE_PROFILE")

for perm in user_permissions:
    if perm == "SYSTEM_DELETE":
        print(f"🚨 High-risk permission detected: '{perm}'! Escalating to Security Audit.")
        break  # ঝুঁকিপূর্ণ পারমিশন পাওয়ায় লুপ সাথে সাথে থামানো হলো
        
    print(f"✅ Permission checked: {perm}")


ক্যাশ সার্ভার ফলব্যাক স্ক্যান (Redis/Memcached Fallback)
একাধিক ক্যাশ নোডের ফিক্সড টুপল থেকে ডাটা খোঁজার সময় প্রথম যে ক্যাশ নোডে ডাটা (Cache Hit) পাওয়া যাবে, সেখান থেকে ডাটা নিয়ে সাথে সাথে লুপ বন্ধ করা:

# ফিক্সড ক্যাশ নোড টুপল
cache_nodes = ("cache_node_primary", "cache_node_secondary", "cache_node_backup")

cache_hit = False

for node in cache_nodes:
    print(f"🔍 Searching cached response in {node}...")
    
    # ধরি Secondary ক্যাশ নোডে ডাটা পাওয়া গেছে
    if node == "cache_node_secondary":
        cache_hit = True
        print(f"⚡ Cache Hit on {node}! Returning data to client.")
        break  # ডাটা ক্যাশে পাওয়া গেছে, তাই পরের নোডে হিট করার দরকার নেই


ফায়ারওয়াল আইপি ব্লক লিস্ট চেকার (Blacklisted IP Guard)
ইনকামিং রিকোয়েস্টের মেটাডাটা টুপলে থাকা আইপিগুলোর মধ্যে কোনোটি ব্ল্যাকলিস্টেড পাওয়া গেলে সাথে সাথে ব্যাকএন্ড সার্ভিস রিকোয়েস্ট রিজেক্ট করে লুপ থামিয়ে দেয়:

# ফায়ারওয়ালের ব্ল্যাকলিস্টেড আইপির ফিক্সড টুপল
blacklisted_ips = ("185.220.101.5", "103.20.1.9", "192.168.1.50")
incoming_ip = "103.20.1.9"

for ip in blacklisted_ips:
    if ip == incoming_ip:
        print(f"🚫 Security Violation! Incoming IP {ip} is blacklisted. Request Terminated.")
        break  # ক্ষতিকর আইপি পাওয়ায় বাকি আইপি প্রসেসিং লুপ সাথে সাথে বন্ধ


ব্যাকগ্রাউন্ড টাস্ক কিউ প্রসেসিং (Worker Limit Exceeded)
টাস্ক কিউ থেকে কাজের লিস্ট প্রসেস করার সময় যদি ব্যাকগ্রাউন্ড ওয়ার্কারের সর্বোচ্চ ধারণক্ষমতা (মেমোরি বা সিপিইউ থ্রেশহোল্ড) পূর্ণ হয়ে যায়, তবে আর কোনো টাস্ক না নিয়ে লুপ বন্ধ করা:

# ফিক্সড টাস্ক প্রায়োরিটি টুপল
pending_tasks = ("TASK_EMAIL_SEND", "TASK_DB_CLEANUP", "TASK_GENERATE_PDF", "TASK_SYNC_LOGS")
max_worker_capacity = 2
processed_count = 0

for task in pending_tasks:
    if processed_count >= max_worker_capacity:
        print(f"⚠️ Worker memory threshold reached ({processed_count} tasks). Stopping task loop!")
        break  # মেমোরি লিমিট পূর্ণ হয়ে যাওয়ায় লুপ থামানো হলো
        
    print(f"⚙️️ Executing: {task}")
    processed_count += 1


এপিআই হেলথ চেক ফিল্টার (First Unhealthy Node Break)
মাইক্রোসার্ভিস আর্কিটেকচারে বেশ কিছু ইন্টারনাল সার্ভার নোডের অবস্থা মনিটর করার সময় যদি প্রথম কোনো সার্ভার 
নোড ডাউন (OFFLINE বা UNHEALTHY) পাওয়া যায়, তবে সাথে সাথে সিস্টেম অ্যাডমিনকে অ্যালার্ট পাঠাতে লুপ বন্ধ করা:

# ফিক্সড মাইক্রোসার্ভিস নোড স্ট্যাটাস টুপল
server_nodes = (
    ("Auth_Service", "HEALTHY"),
    ("Payment_Service", "HEALTHY"),
    ("Notification_Service", "OFFLINE"),  # 🚨 সমস্যা পাওয়া গেছে
    ("Order_Service", "HEALTHY")
)

for node_name, status in server_nodes:
    if status != "HEALTHY":
        print(f"🚨 Critical Failure: Service '{node_name}' is {status}! Aborting health audit.")
        break  # প্রথম আনহেলদি সার্ভিস পাওয়া মাত্রই চেক বন্ধ করে অ্যালার্ট ট্রিগার করা হলো
        
    print(f"✅ Service '{node_name}' status: {status}")


মাল্টি-ফ্যাক্টর অথেন্টিকেশন প্রসেসর (MFA Security Guard)
লগইন করার সময় সিকিউরিটি চ্যালেঞ্জের টুপল (যেমন: SMS OTP, Email Verification, 
Authenticator App) স্ক্যান করার সময় যেকোনো একটিতে ইউজার ভুল পিন বা ব্যর্থ হলে পুরো অথেন্টিকেশন লুপ বাতিল করা:

# সিকিউরিটি ভেরিফিকেশন স্টেপসের ফিক্সড টুপল (Step_Name, Status)
mfa_steps = (
    ("Password_Check", "PASSED"),
    ("SMS_OTP_Check", "FAILED"),  # ❌ ভুল ওটিপি দেওয়া হয়েছে
    ("Authenticator_App", "PENDING")
)

for step, status in mfa_steps:
    if status == "FAILED":
        print(f"🚫 Login Blocked: Security step '{step}' failed! Access denied.")
        break  # একটি স্টেপ ফেইল করায় বাকি স্টেপ প্রসেস করা বন্ধ হলো
        
    print(f"🔒 Step '{step}' verified successfully.")


ফাইল আপলোড সাইজ ও লিমিট গার্ড (Total Upload Payload Exceeded)
ইউজার ব্যাকএন্ডে যে ফাইলগুলো ব্যাচ বা একসাথে আপলোড করতে পাঠিয়েছে, 
সেগুলোর ফাইল সাইজের টুপল প্রসেস করার সময় মোট সাইজ যদি সার্ভার পে-লোড লিমিট (যেমন: ২০ এমবি) অতিক্রম করে, তবে আর নতুন ফাইল না নিয়ে প্রসেসিং বন্ধ করা:

# ফিক্সড ফাইল সাইজ টুপল (Size in MB)
file_sizes_mb = (4, 6, 8, 5, 10)
max_allowed_total_mb = 20
total_size = 0

for size in file_sizes_mb:
    if total_size + size > max_allowed_total_mb:
        print(f"⚠️ Payload Limit Exceeded! Cannot add file of {size} MB. Stopping batch processing.")
        break  # লিমিট পার হয়ে যাওয়ায় পরবর্তী ফাইল প্রসেস করা বন্ধ
        
    total_size += size
    print(f"📂 File of {size} MB added. Current Total: {total_size} MB")


ব্যাকএন্ড কুয়েরি প্যারামিটার স্যানিটাইজার (SQL Injection Attack Guard)
ইউজার বা ক্লায়েন্টের পাঠানো ইউআরএল কোয়েরি প্যারামিটারের ফিক্সড টুপল স্ক্যান করার
সময় যদি কোনো প্যারামিটারে ক্ষতিকারক ক্যারেক্টার (যেমন: ' OR '1'='1) পাওয়া যায়, তবে সাথে সাথে রিকোয়েস্ট ব্লক করা:

# ইনকামিং রিকোয়েস্ট কুয়েরি প্যারামিটারের ফিক্সড টুপল
query_params = ("search_keyword=phone", "category=tech", "filter=' OR '1'='1")

for param in query_params:
    if "OR" in param or "SELECT" in param or "'" in param:
        print(f"🚨 Potential SQL Injection detected in parameter: '{param}'! Request Terminated.")
        break  # ক্ষতিকারক প্যারামিটার পাওয়ায় লুপ থামিয়ে সিকিউরিটি ব্লক তৈরি করা হলো
        
    print(f"✅ Parameter sanitized: {param}")



ইউজার সাবস্ক্রিপশন ও প্রিমিয়াম ফিচার এক্সেস (Trial Expiry Break)
সিস্টেমে ব্যাকগ্রাউন্ড প্রসেসের মাধ্যমে ইউজারদের সাবস্ক্রিপশন সুবিধা টুপল 
স্ক্যান করার সময় কোনো ইউজার অ্যাকাউন্টের স্ট্যাটাস EXPIRED পাওয়া গেলে তার অ্যাক্সেস সাথে সাথে ব্লক করে লুপ থামানো:

# ফিক্সড সাবস্ক্রিপশন ডাটা টুপল (Username, Plan, Status)
user_subscriptions = (
    ("sami", "Premium", "ACTIVE"),
    ("abdullah", "Pro", "ACTIVE"),
    ("rahim", "Trial", "EXPIRED"),  # ❌ মেয়াদ শেষ
    ("karim", "Premium", "ACTIVE")
)

for user, plan, status in user_subscriptions:
    if status == "EXPIRED":
        print(f"🔒 Access Blocked: Subscription for '{user}' has expired! Process stopped.")
        break  # মেয়াদ শেষ হওয়া ইউজার পাওয়ায় পরবর্তী প্রসেসিং লুপ বন্ধ
        
    print(f"✅ Access Granted: User '{user}' on plan '{plan}'.")



নেটওয়ার্ক পিং ও লেটেন্সি টেস্ট (High Ping Timeout)
সার্ভার ক্লাস্টার থেকে বিভিন্ন ডাটা সেন্টারের পিং (Ping) লেটেন্সির ফিক্সড টুপল স্ক্যান 
করার সময় যদি কোনো নেটওয়ার্ক নোডের লেটেন্সি ৩০০ মি.সে.-এর বেশি হয়, তবে সংযোগ স্থাপন না করে লুপ থামানো:

# ফিক্সড নোড লেটেন্সি টুপল (Node_Name, Latency_ms)
node_latencies = (
    ("Asia-East", 45),
    ("Europe-West", 120),
    ("US-Central", 350),  # 🚨 হাই লেটেন্সি!
    ("Asia-South", 20)
)

max_acceptable_latency = 300

for node, latency in node_latencies:
    if latency > max_acceptable_latency:
        print(f"⚠️ Network Warning: Node '{node}' latency is too high ({latency}ms)! Connection attempt halted.")
        break  # লেটেন্সি বেশি পাওয়ায় স্ক্যান থামানো হলো
        
    print(f"🌐 Connected to '{node}' with latency {latency}ms.")



ডাটা মাইগ্রেশন লিমিটার (Batch Migration Limit)
ডাটাবেস মাইগ্রেশনের সময় ফিক্সড টেবিল রেকর্ড টুপল স্ক্যান করতে
গিয়ে নির্ধারিত ব্যাচ লিমিট (যেমন: ১৫টি রেকর্ড) পূর্ণ হয়ে গেলে বর্তমান ব্যাচের মাইগ্রেশন থামানো:

# মাইগ্রেশনের জন্য নির্ধারিত টেবিল রেকর্ডের টুপল (Record_ID)
migration_records = (1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008)
batch_limit = 5
processed_count = 0

for record_id in migration_records:
    if processed_count >= batch_limit:
        print(f"📦 Batch limit ({batch_limit}) reached! Saving progress and pausing migration.")
        break  # লিমিট পূর্ণ, পরবর্তী ব্যাচের জন্য প্রস্তুত হওয়া
        
    print(f"🔄 Migrating Record ID: {record_id}")
    processed_count += 1


ই-কমার্স ফ্রড ডিটেকশন (Suspicious Order Guard)
একটি অর্ডার প্রসেসিং সিস্টেমে অর্ডার অ্যামাউন্টের টুপল চেকের সময় যদি হঠাৎ
অস্বাভাবিক কোনো বড় অর্ডার (যেমন: ৫০,০০০ টাকার বেশি) দেখা যায়, যা ই-কমার্স পলিসি অনুযায়ী ম্যানুয়াল রিভিউ প্রয়োজন, তবে অটোমেটেড লুপ বন্ধ করা:

# ক্রমান্বয়ে আসা অর্ডার প্রাইসের ফিক্সড টুপল
order_amounts = (1200, 3500, 850, 75000, 2100)  # 🚨 ৭৫,০০০ টাকার সন্দেহজনক অর্ডার

suspicious_limit = 50000

for amount in order_amounts:
    if amount > suspicious_limit:
        print(f"🚨 Fraud Alert! Suspicious transaction amount detected ({amount} BDT). Order processing frozen.")
        break  # হাই-ভ্যালু অর্ডারের জন্য অটো প্রসেসিং লুপ সাথে সাথে থামানো হলো
        
    print(f"🛒 Order processed for amount: {amount} BDT")



ডিস্ক স্পেস ওয়ার্নিং চেকার (Critical Disk Storage Guard)
সার্ভারের বিভিন্ন পার্টিশনের অবশিষ্ট স্পেসের (GB) ফিক্সড টুপল স্ক্যান করার সময় যদি কোনো 
পার্টিশনে ১০ GB-এর কম স্পেস পাওয়া যায়, তবে সিস্টেম ক্র্যাশ এড়াতে লুপ থামিয়ে সাথে সাথে ডিস্ক ক্লিনআপ ট্রিগার করা:


# ফিক্সড ডিস্ক পার্টিশন টুপল (Partition_Name, Free_Space_GB)
disk_partitions = (
    ("/var/log", 45),
    ("/usr/bin", 20),
    ("/data/db", 5),   # 🚨 মাত্র ৫ GB অবশিষ্ট!
    ("/home/user", 100)
)

critical_threshold_gb = 10

for partition, free_space in disk_partitions:
    if free_space < critical_threshold_gb:
        print(f"🚨 Critical Storage Alert: Partition '{partition}' has only {free_space} GB remaining! Halting check.")
        break  # ডিস্ক স্পেস বিপজ্জনক পর্যায়ে পৌঁছানোয় স্ক্যান থামানো হলো
        
    print(f"✅ Storage check passed for '{partition}': {free_space} GB free.")


এইচটিটিপি রিকোয়েস্ট হেডার অডিট (Missing Authorization Header)
ক্লায়েন্ট থেকে আসা ইনকামিং এইচটিটিপি হেডারের ফিক্সড টুপল স্ক্যান করার সময় যদি 
অতি প্রয়োজনীয় Authorization হেডার অনুপস্থিত থাকে, তবে সাথে সাথে লুপ বন্ধ করে 401 Unauthorized রেসপন্স রিটার্ন করা:

# ইনকামিং রিকোয়েস্ট হেডারের ফিক্সড টুপল
http_headers = (
    ("Content-Type", "application/json"),
    ("User-Agent", "Mozilla/5.0"),
    ("Accept-Language", "en-US"),
    # "Authorization" হেডার মিসিং!
)

has_auth_header = False

for header_key, header_val in http_headers:
    if header_key == "Authorization":
        has_auth_header = True
        break

if not has_auth_header:
    print("🚫 Security Error: Authorization header missing from request! Terminating pipeline.")


অটোমেটেড ব্যাকআপ ইন্টিগ্রিটি চেক (Corrupted Archive Guard)
প্রতিদিনের সিস্টেম ব্যাকআপ ফাইলগুলোর ফিক্সড টুপল অডিট করার সময় যদি কোনো ব্যাকআপ
ফাইলের স্ট্যাটাস CORRUPTED পাওয়া যায়, তবে অ্যাডমিনকে মেসেজ পাঠিয়ে সাথে সাথে রিওপেনিং প্রসেস বন্ধ করা:

# ব্যাকআপ আর্কাইভ ফাইলের টুপল (File_Name, Status)
backup_archives = (
    ("backup_2026_10_01.tar.gz", "VALID"),
    ("backup_2026_10_02.tar.gz", "CORRUPTED"),  # ❌ করাপ্টেড ফাইল
    ("backup_2026_10_03.tar.gz", "VALID")
)

for filename, status in backup_archives:
    if status == "CORRUPTED":
        print(f"🚨 Backup Failure: Archive '{filename}' is corrupted! Aborting restoration sequence.")
        break  # নষ্ট ফাইল পাওয়ায় প্রসেস সম্পূর্ণ বন্ধ
        
    print(f"📦 Backup archive '{filename}' verified.")



ইউজার রিকোয়েস্ট উইন্ডো মনিটর (Burst Rate Limit Exceeded)
একই সেকেন্ডে ক্লায়েন্টের পাঠানো পর পর একাধিক রিকোয়েস্টের টাইমস্ট্যাম্প
টুপল স্ক্যান করার সময় যদি প্রতি সেকেন্ডে ৫টির বেশি রিকোয়েস্ট পাওয়া যায়, তবে স্প্যামিং থেকে সার্ভার রক্ষা করতে লুপ বন্ধ করা:

# ১ সেকেন্ডের উইন্ডোতে আসা রিকোয়েস্ট সিরিয়াল টুপল
request_burst_sequence = (1, 2, 3, 4, 5, 6, 7)  # মোট ৭টি রিকোয়েস্ট
max_allowed_burst = 5

for req_num in request_burst_sequence:
    if req_num > max_allowed_burst:
        print(f"⛔ Rate Limit Violation: Burst request #{req_num} exceeds max limit of {max_allowed_burst}! Blocking client.")
        break  # লিমিট অতিক্রম করায় বাকি রিকোয়েস্ট ব্লক করা হলো
        
    print(f"⚡ Processing request #{req_num}")


ডেটাবেস মেমোরি পেজিং গার্ড (Query Memory Limit Guard)
ডাটাবেস থেকে মেমোরিতে ফেচ (Fetch) করা রেকর্ডের আকারের টুপল প্রসেস করার 
সময় যদি ব্যাকএন্ডের সর্বোচ্চ মেমোরি ক্যাপাসিটি (যেমন: ৫০ MB) পার হয়ে যায়, তবে সার্ভার আউট-অফ-মেমোরি (OOM) ক্র্যাশ থেকে রক্ষা করতে সাথে সাথে লুপ বন্ধ করা:

# ফিক্সড মেমোরি পেজিং চ্যাঙ্ক সাইজ টুপল (Size in MB)
page_chunks_mb = (8, 12, 15, 20, 10)
max_allowed_memory_mb = 50
current_memory_usage = 0

for chunk in page_chunks_mb:
    if current_memory_usage + chunk > max_allowed_memory_mb:
        print(f"🚨 OOM Guard Triggered: Adding {chunk} MB exceeds {max_allowed_memory_mb} MB limit! Halting query execution.")
        break  # মেমোরি ওভারফ্লো এড়াতে লুপ বন্ধ
        
    current_memory_usage += chunk
    print(f"📊 Processed memory chunk: {chunk} MB (Total: {current_memory_usage} MB)")


থার্ড-পার্টি সার্ভিস হেলথ পিং (Third-Party Webhook Timeout)
পেমেন্ট বা এসএমএস পাঠানোর জন্য একাধিক থার্ড-পার্টি গেটওয়ের সার্ভিস 
রেসপন্স টাইম (ms) স্ক্যান করার সময় যদি কোনো সার্ভিস ৫০০ ms-এর বেশি লেটেন্সি দেখায় বা টাইমআউট হয়, তবে সিস্টেমে সার্ভিস হ্যাং হওয়া ঠেকাতে লুপ থামিয়ে দেওয়া:


# ফিক্সড সার্ভিস পিং রেসপন্স টাইম টুপল (Gateway_Name, Response_Time_ms)
external_services = (
    ("Twilio_SMS", 120),
    ("SendGrid_Email", 210),
    ("SSLCommerz_Payment", 650),  # 🚨 রেসপন্স টাইম অনেক বেশি!
    ("Firebase_Push", 90)
)

max_timeout_ms = 500

for service, resp_time in external_services:
    if resp_time > max_timeout_ms:
        print(f"⚠️ Gateway Timeout: '{service}' took {resp_time}ms (Max allowed: {max_timeout_ms}ms)! Aborting webhook cycle.")
        break  # সার্ভিস রেসপন্স ধীরগতির হওয়ায় লুপ বন্ধ
        
    print(f"✅ Service '{service}' responding normally ({resp_time}ms).")


ওঅথ (OAuth) টোকেন রিফ্রেশ ও এক্সপায়ারি অডিট (Expired Session Guard)
ইউজারের ওঅথ সিকিউরিটি টোকেনের ফিক্সড লিস্ট স্ক্যান করার সময় যদি কোনো এক্টিভ
সেশন টোকেনের স্ট্যাটাস EXPIRED অথবা REVOKED পাওয়া যায়, তবে সাথে সাথে সেশন কিল করে ইউজারকে রিডাইরেক্ট করতে লুপ থামানো:

# ওঅথ সেশন টোকেনের ফিক্সড টুপল (Session_ID, Status)
session_tokens = (
    ("sess_991823", "ACTIVE"),
    ("sess_991824", "ACTIVE"),
    ("sess_991825", "EXPIRED"),  # ❌ এক্সপায়ার্ড টোকেন
    ("sess_991826", "ACTIVE")
)

for sess_id, status in session_tokens:
    if status != "ACTIVE":
        print(f"🔒 Security Alert: Session '{sess_id}' is {status}! Force logging out user.")
        break  # অবৈধ টোকেন পাওয়া মাত্রই লুপ স্টপ
        
    print(f"🔑 Session '{sess_id}' authenticated.")


ডাটা স্যানিটেশন রিজেকশন (Strict Data Schema Validator)
ক্লায়েন্ট থেকে আসা JSON রেসপন্স স্কিমার ফিক্সড টাইপ টুপল স্ক্যান করার
সময় যদি কোনো ফিল্ডে None বা প্রত্যাশিত ডাটা টাইপ না পাওয়া যায়, তবে ডাটাবেস এরর এড়াতে লুপ থামিয়ে রিকোয়েস্ট রিজেক্ট করা:

# ফিক্সড পে-লোড ফিল্ড ও ভ্যালু টুপল
payload_fields = (
    ("user_id", 1001),
    ("email", "user@example.com"),
    ("phone", None),  # 🚨 অনাকাঙ্ক্ষিত Null ভ্যালু
    ("role", "customer")
)

for field, value in payload_fields:
    if value is None:
        print(f"🚫 Schema Validation Failed: Field '{field}' cannot be Null! Rejecting payload.")
        break  # ইনভ্যালিড ডাটা পাওয়ায় প্রসেসিং বন্ধ
        
    print(f"✅ Field '{field}' validated successfully.")



সার্ভার ফাইল সিংক অডিট (Corrupted Hash Match Break)
মাল্টি-সার্ভার ক্লাস্টারে ফাইল সিংক করার সময় নির্দিষ্ট ফাইলের ক্রিপ্টোগ্রাফিক হ্যাশ (SHA256) চেক করার 
সময় যদি কোনো ক্লাস্টার নোডে হ্যাশ অমিল পাওয়া যায়, তবে ব্যাকএন্ড ডাটা করাপশন এড়াতে সিংক প্রসেস সাথে সাথে বন্ধ করে দেয়:

# ফিক্সড সার্ভার নোড ও ফাইল হ্যাশ টুপল (Node_Name, File_Hash)
cluster_file_hashes = (
    ("node_us_east", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
    ("node_eu_west", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
    ("node_ap_south", "7d793037a0760186574b0282f2f435e7b1e737714172ed1530d400a0d0ece958"),  # 🚨 অমিল পাওয়া গেছে
    ("node_sa_east", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
)

expected_hash = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

for node, file_hash in cluster_file_hashes:
    if file_hash != expected_hash:
        print(f"🚨 Data Mismatch: Server '{node}' has corrupted file hash! Aborting cluster sync.")
        break  # হ্যাশ অমিল পাওয়ায় লুপ থামিয়ে দেওয়া হলো
        
    print(f"✅ Node '{node}' file hash verified.")



পাসওয়ার্ড অ্যাটেম্পট অ্যান্ড লকআউট (Account Lockout Policy)
ইউজারের সাম্প্রতিক ব্যর্থ লগইন চেষ্টার ফিক্সড টুপল ব্যাকএন্ডে অডিট করার সময় 
যদি ৩টির বেশি ভুল চেষ্টার রেকর্ড পাওয়া যায়, তবে ইউজার অ্যাকাউন্ট সাময়িকভাবে লক করে লুপ বন্ধ করা হয়:

# পর পর লগইন অ্যাটেম্পটের ফিক্সড স্ট্যাটাস টুপল
login_attempts = ("FAILED", "FAILED", "FAILED", "SUCCESS")
max_failed_allowed = 3
failed_count = 0

for attempt in login_attempts:
    if attempt == "FAILED":
        failed_count += 1
        
    if failed_count >= max_failed_allowed:
        print(f"🔒 Account Locked: Reached {failed_count} consecutive failed login attempts! Stopping verification.")
        break  # ৩বার ভুল পাওয়ায় একাউন্ট লক ও লুপ টার্মিনেট
        
    print(f"🔑 Processing attempt status: {attempt}")


  ক্যাশ মেমোরি ইভিকশন স্ক্যান (LRU Cache Eviction Guard)
সার্ভারের ক্যাশ নোড থেকে লিস্ট প্রসেস করার সময় যদি নির্দিষ্ট কোনো 
ক্যাশ বাফারের সাইজ রেডলাইন (যেমন: ১০০ MB) পার হয়ে যায়, তবে প্রসেসিং বন্ধ করে মেমোরি ফ্লাশ করার নির্দেশনা দেওয়া হয়:

# ফিক্সড বাফার ব্লক সাইজ টুপল (Block_ID, Size_MB)
cache_blocks = (
    ("block_01", 25),
    ("block_02", 30),
    ("block_03", 50),  # 🚨 বাফার লিমিট অতিক্রম করবে
    ("block_04", 15)
)

max_buffer_mb = 100
total_buffer_mb = 0

for block_id, size in cache_blocks:
    if total_buffer_mb + size > max_buffer_mb:
        print(f"⚠️ Cache Overflow Warning: Block '{block_id}' ({size} MB) exceeds limit of {max_buffer_mb} MB! Triggering LRU eviction.")
        break  # বাফার ফুল, তাই লুপ বন্ধ
        
    total_buffer_mb += size
    print(f"💾 Buffer loaded '{block_id}': Total {total_buffer_mb} MB")


ব্যাকগ্রাউন্ড জব প্রাইওরিটি প্রসেসর (Emergency Job Interrupt)
ব্যাকগ্রাউন্ড কিউ থেকে প্রসেস হতে থাকা জবগুলোর ফিক্সড টুপল স্ক্যান করার 
সময় যদি অতি জরুরী কোনো ক্রিটিক্যাল টাস্ক (EMERGENCY_SHUTDOWN বা CRITICAL_PATCH) চলে আসে, 
তবে সাধারণ জবের লুপ থামিয়ে আগে জরুরী কাজটি হ্যান্ডেল করা হয়:

# ফিক্সড ব্যাকগ্রাউন্ড কিউ টুপল
job_queue = ("JOB_REPORTS", "JOB_EMAILS", "EMERGENCY_SHUTDOWN", "JOB_CLEANUP")

for job in job_queue:
    if job == "EMERGENCY_SHUTDOWN":
        print(f"🚨 Priority Override: Critical job '{job}' detected! Pausing standard queue processing immediately.")
        break  # জরুরী কাজ থাকায় সাধারণ লুপ বন্ধ
        
    print(f"⚙️ Executing standard job: {job}")


সফটওয়্যার লাইসেন্স চাবি ভ্যালিডেটর (Expired License Guard)
সার্ভার চালু হওয়ার সময় ফিক্সড লাইসেন্স কি ডাটাসটের টুপল স্ক্যান করার 
সময় যদি কোনো লাইসেন্সের মেয়াদের স্ট্যাটাস EXPIRED পাওয়া যায়, তবে অ্যাপ চালু হওয়া ব্লক করে লুপ বন্ধ করা:

# ফিক্সড লাইসেন্স কি মেটাডাটা টুপল (Module_Name, Status)
license_keys = (
    ("Auth_Module", "VALID"),
    ("Core_Engine", "VALID"),
    ("Analytics_Suite", "EXPIRED"),  # ❌ মেয়াদ শেষ
    ("Reporting_Tool", "VALID")
)

for module, status in license_keys:
    if status == "EXPIRED":
        print(f"🚨 License Violation: Module '{module}' license is EXPIRED! Application boot sequence halted.")
        break  # ইনভ্যালিড লাইসেন্স থাকায় বুট প্রসেস বন্ধ
        
    print(f"🔑 Module '{module}' license verified successfully.")


ডাটাবেস ট্রানজেকশন ডেডলক ডিটেক্টর (Deadlock Detector)
ডাটাবেসের অ্যাক্টিভ ট্রানজেকশন লকের ফিক্সড টুপল স্ক্যান করার সময় যদি 
কোনো ট্রানজেকশনের স্ট্যাটাস DEADLOCK পাওয়া যায়, তবে ডাটাবেস হ্যাং হওয়া ঠেকাতে সাথে সাথে রিকভারি ট্রিগার করে লুপ থামানো:

# ট্রানজেকশন স্টেটাসের ফিক্সড টুপল (Tx_ID, Status)
active_transactions = (
    ("TX_1001", "RUNNING"),
    ("TX_1002", "WAITING"),
    ("TX_1003", "DEADLOCK"),  # 🚨 ডেডলক সনাক্ত হয়েছে
    ("TX_1004", "RUNNING")
)

for tx_id, status in active_transactions:
    if status == "DEADLOCK":
        print(f"🚨 Deadlock Detected: Transaction '{tx_id}' is deadlocked! Terminating transaction loop for rollback.")
        break  # ডেডলক পাওয়ায় লুপ সাথে সাথে বন্ধ
        
    print(f"🔄 Transaction '{tx_id}' status: {status}")


এপিআই ভার্সন অবসোলেট ফিল্টার (Deprecated API Guard)
ইনকামিং মোবাইল ক্লায়েন্টের পাঠানো এপিআই ভার্সন রিকোয়েস্টের টুপল স্ক্যান করার 
সময় যদি ভার্সনটি DEPRECATED বা অকার্যকর হিসেবে চিহ্নিত থাকে, তবে সাপোর্ট বন্ধ করে ইউজারকে অ্যাপ আপডেট মেসেজ পাঠাতে লুপ বন্ধ করা:

# ফিক্সড এপিআই ভার্সন স্ট্যাটাস টুপল (Version, Status)
api_versions = (
    ("v3.0", "SUPPORTED"),
    ("v2.5", "SUPPORTED"),
    ("v1.0", "DEPRECATED"),  # ❌ আর সাপোর্ট দেওয়া হয় না
    ("v2.0", "SUPPORTED")
)

for ver, status in api_versions:
    if status == "DEPRECATED":
        print(f"🚫 Deprecated API: Version '{ver}' is no longer supported! Rejecting connection.")
        break  # পুরানো ভার্সন পাওয়ায় প্রসেসিং বন্ধ
        
    print(f"🌐 API Version '{ver}' active and supported.")


রিমোট ডিসাস্টার রিকভারি সাইট পিন (DR Site Fallback)
ডিজাস্টার রিকভারির (DR) জন্য ডাটা সেন্টারের ব্যাকআপ নোডগুলোর টুপল টেস্ট করার সময় 
প্রথম যে ডাটা সেন্টার ব্যাকআপ সাইটটি ONLINE পাওয়া যাবে, সেটি সিলেক্ট করে লুপ থামানো:

# ডিসাস্টার রিকভারি ডাটা সেন্টার টুপল (Site_Name, Status)
dr_sites = (
    ("DR_Singapore", "OFFLINE"),
    ("DR_Frankfurt", "ONLINE"),  # 🎯 লাইভ ব্যাকআপ নোড
    ("DR_Tokyo", "ONLINE")
)

selected_dr = None

for site, status in dr_sites:
    if status == "ONLINE":
        selected_dr = site
        print(f"✅ Active DR Site Found: Connected to '{site}'!")
        break  # অ্যাক্টিভ নোড পাওয়ার সাথে সাথে সার্চ বন্ধ





এখন continue কীভাবে টুপলের সাথে কাজ করে (ডাটা ফিল্টারিং, স্প্যাম স্কিপিং, ইনভ্যালিড ডাটা বাইপাস করা)— করে 
💡 টুপলে continue-এর কাজ:
break-এর মতো পুরো লুপ থামিয়ে দেয় না; বরং কোনো নির্দিষ্ট শর্ত মিলে গেলে বর্তমান ইটারেশন বা চক্করটিকে স্কিপ (Skip) করে সরাসরি পরের ইটারেশনে চলে যায়।

ব্যাকএন্ডে ইনভ্যালিড ডাটা বাইপাস করা, স্প্যাম ছাঁকা বা স্যানিটাইজেশনের কাজে এটি প্রচুর ব্যবহৃত হয়।


🚀 টুপলের সাথে continue ব্যবহারের ৪টি ব্যাকএন্ড উদাহরণ:
১. ইনভ্যালিড ইমেইল স্যানিটাইজার (Email Notification Filter)
ইউজারদের ইমেইল লিস্টের ফিক্সড টুপল স্ক্যান করে নোটিফিকেশন পাঠানোর সময় যেসব ইমেইলে @ নেই বা ফরম্যাট ভুল, সেগুলোকে স্কিপ করে শুধু ভ্যালিড ইমেইলে মেসেজ পাঠানো:

# অপরিবর্তনযোগ্য ইমেইল লিস্টের টুপল
user_emails = ("sami@example.com", "invalid_email_at_gmail", "abdullah@dev.com", "test_user")

for email in user_emails:
    if "@" not in email:
        print(f"⚠️️ Invalid email format: '{email}'. Skipping...")
        continue  # ভুল ইমেইল স্কিপ করে পরের ইমেইলে চলে যাবে
        
    print(f"📧 Sending welcome email to: {email}")



বিডি কান্ট্রি কোড ভ্যালিডেটর (BD Phone Number Sanitizer)
ফোন নম্বরের ফিক্সড টুপল প্রসেস করার সময় দেশের বাইরের বা ইনভ্যালিড লেংথের নম্বর স্কিপ করে কেবল বাংলাদেশের বৈধ নম্বরগুলোতে (১১ ডিজিট, 01 দিয়ে শুরু) এসএমএস প্রসেস করা:


# ফিক্সড ফোন নম্বর টুপল
phone_numbers = ("01712345678", "+14155552671", "01887654321", "01234")

for phone in phone_numbers:
    if not phone.startswith("01") or len(phone) != 11:
        print(f"🚫 Non-BD or Invalid number '{phone}'. Skipping SMS process.")
        continue  # শর্ত পূরণ না করলে পরের নম্বরে চলে যাবে
        
    print(f"📲 Processing OTP SMS for: {phone}")



সার্ভার প্রসেস মনিটর (Skip Suspended Background Tasks)
সার্ভারের চলমান ব্যাকগ্রাউন্ড টাস্কের ফিক্সড টুপল স্ক্যান করার সময় যেসব টাস্কের স্ট্যাটাস INACTIVE বা SUSPENDED, সেগুলোকে স্কিপ করে কেবল RUNNING প্রসেসগুলোতে সিপিইউ রিসোর্স দেয়া:

# টাস্ক মেটাডাটার ফিক্সড টুপল (Task_Name, Status)
background_tasks = (
    ("DB_Backup", "RUNNING"),
    ("Log_Cleanup", "SUSPENDED"), # ⏸️ স্কিপ হবে
    ("Email_Queue", "RUNNING"),
    ("Report_Gen", "INACTIVE")   # ⏸️ স্কিপ হবে
)

for task_name, status in background_tasks:
    if status != "RUNNING":
        print(f"⏸️ Task '{task_name}' is {status}. Skipping execution cycle.")
        continue  # অ্যাক্টিভ না হলে স্কিপ
        
    print(f"⚙️ Executing active process: {task_name}")



ডাটাবেস নাল ভ্যালু ফিল্টার (Database Null/Zero Value Filter)
ডাটাবেসের নির্দিষ্ট রো থেকে পাওয়া টাকার হিসাবের ফিক্সড টুপল হিসাব করার সময় কোনো শূন্য (0) বা None ভ্যালু থাকলে তা স্কিপ করে বাকি আর্নিং বা আয়ের যোগফল বের করা:


# ফিক্সড ডেইলি ট্রানজেকশন টুপল
daily_earnings = (1200, 0, 3500, None, 2100)
total_income = 0

for amount in daily_earnings:
    if amount is None or amount == 0:
        continue  # ০ বা None ভ্যালু স্কিপ করে পরের আইটেমে যাওয়া
        
    total_income += amount

print(f"💰 Total Valid Earnings: {total_income} BDT")



ফাইল ফরম্যাট হোয়াইটলিস্ট স্ক্যানার (Unsupported Format Skip)
ইউজারের আপলোড করা বাল্ক ফাইলের মিডিয়া ফরম্যাট টুপল স্ক্যান করার সময় যেসব ফাইল এক্সটেনশন 
সাপোর্টেড নয় (যেমন: .exe বা .zip), সেগুলোকে স্কিপ করে কেবল অনুমোদিত মিডিয়া ফাইলগুলো ইমেজ প্রসেসিং পাইপলাইনে পাঠানো:

# আপলোড হওয়া ফাইলমডেলের ফিক্সড টুপল
uploaded_files = ("avatar.png", "script.exe", "document.pdf", "backup.zip", "banner.jpg")
allowed_extensions = (".png", ".jpg", ".jpeg")

for file_name in uploaded_files:
    if not file_name.endswith(allowed_extensions):
        print(f"⚠️ Skipping unsupported file: '{file_name}'")
        continue  # অননুমোদিত ফাইল স্কিপ করে পরবর্তী ফাইলে চলে যাবে
        
    print(f"🖼️ Processing image optimization for: {file_name}")



নন-অ্যাডমিন রোল ফিল্টার (Role-Based Notification Bypass)
ইউজার অবজেক্টের ফিক্সড টুপল স্ক্যান করার সময় যেসব ইউজারের রোল admin নয়
(যেমন: guest বা user), তাদের সিকিউরিটি অ্যালার্ট পাঠানো স্কিপ করে কেবল অ্যাডমিনদের ইমেইল পাঠানো:

# ইউজার প্রোফাইল ডাটার ফিক্সড টুপল (Username, Role)
user_profiles = (
    ("sami", "admin"),
    ("rahim", "guest"),     # ⏭️ স্কিপ হবে
    ("abdullah", "admin"),
    ("karim", "user")       # ⏭️ স্কিপ হবে
)

for username, role in user_profiles:
    if role != "admin":
        print(f"⏭️ User '{username}' is a {role}. Skipping admin notification.")
        continue  # অ্যাডমিন না হলে স্কিপ
        
    print(f"🚨 Sending critical system status alert to admin: {username}")


অকার্যকর পেমেন্ট চ্যানেল স্কিপার (Inactive Gateway Bypass)
অ্যাপ্লিকেশনের বিভিন্ন পেমেন্ট গেটওয়ের স্ট্যাটাস টুপল স্ক্যান করার সময় যেসব গেটওয়ে মেইনটেন্যান্সের কারণে DISABLED রয়েছে, 
সেগুলোকে স্কিপ করে কেবল সক্রিয় গেটওয়েগুলোতে চেকআউট অপশন সক্রিয় রাখা:


# পেমেন্ট গেটওয়ে কনফিগারেশন টুপল (Gateway_Name, Status)
payment_gateways = (
    ("bKash", "ACTIVE"),
    ("Nagad", "MAINTENANCE"),  # ⏭️ স্কিপ হবে
    ("Rocket", "ACTIVE"),
    ("Upay", "DISABLED")       # ⏭️ স্কিপ হবে
)

for gateway, status in payment_gateways:
    if status != "ACTIVE":
        print(f"⏸️ Gateway '{gateway}' is {status}. Skipping checkout option.")
        continue  # একটিভ না থাকলে স্কিপ
        
    print(f"💳 Enabling payment option for user: {gateway}")


এপিআই এইচটিটিপি স্ট্যাটাস ফিল্টার (Skip Successful Responses in Log Audit)
সিস্টেম অডিটের সময় সফল রেসপন্স কোডগুলো (200 OK, 201 Created) স্কিপ করে কেবল ক্লায়েন্ট বা সার্ভার এরর কোডগুলো (404, 500, 502) প্রসেস করে লগে ফাইল রাইট করা:

# ইনকামিং রিকোয়েস্ট এইচটিটিপি স্ট্যাটাস কোড টুপল
api_status_codes = (200, 404, 201, 500, 200, 502)

for status_code in api_status_codes:
    if 200 <= status_code < 300:
        continue  # সফল রেসপন্স স্কিপ করে পরবর্তী স্ট্যাটাস কোডে চলে যাবে
        
    print(f"🚨 Error Status Detected: HTTP {status_code}! Writing to error log file.")



স্প্যাম / বট আইপি ফিল্টার (IP Anomaly Whitelist Bypass)
ইনকামিং ক্লায়েন্ট রিকোয়েস্টের আইপি অ্যাড্রেসের ফিক্সড টুপল স্ক্যান করার সময় অভ্যন্তরীণ ব্যাকএন্ড ট্রাস্টেড বা ইন্টারনাল
আইপিগুলোকে (127.0.0.1 বা localhost) সিকিউরিটি অডিট প্রসেসিং থেকে স্কিপ করে বাইরের আইপিগুলো যাচাই করা:

# ফিক্সড ইনকামিং রিকোয়েস্ট আইপি টুপল
incoming_ips = ("127.0.0.1", "103.20.1.9", "localhost", "185.220.101.5")

for ip in incoming_ips:
    if ip == "127.0.0.1" or ip == "localhost":
        print(f"⏩ Internal IP '{ip}' detected. Skipping security firewall scan.")
        continue  # ইন্টারনাল আইপি স্কিপ করে বাইরের আইপিতে চলে যাবে
        
    print(f"🔍 Running deep threat inspection for external IP: {ip}")




ওয়েবহুক ইভেন্ট ফিল্টারিং (Skip Unhandled Event Types)
থার্ড-পার্টি সার্ভিস (যেমন: Stripe, SSLCommerz) থেকে আসা ওয়েবহুক ইভেন্টের 
ফিক্সড টুপল প্রসেস করার সময় অনাকাঙ্ক্ষিত বা অপ্রয়োজনীয় ইভেন্ট (যেমন: payment_intent.created) স্কিপ করে কেবল সফল পেমেন্ট ইভেন্ট প্রসেস করা:


# ফিক্সড ওয়েবহুক ইভেন্ট টাইপ টুপল
webhook_events = (
    "payment_intent.created",
    "charge.succeeded",     # 🎯 প্রসেস করতে হবে
    "customer.created",
    "charge.succeeded"      # 🎯 প্রসেস করতে হবে
)

for event in webhook_events:
    if event != "charge.succeeded":
        print(f"⏩ Event '{event}' is not actionable. Skipping...")
        continue  # প্রয়োজনীয় ইভেন্ট না হলে স্কিপ
        
    print(f"⚡ Fulfilling order for successful event: {event}")



ব্যাকগ্রাউন্ড ক্যাশ টিটিএল অডিট (Skip Active Cache Keys)
ক্যাশ সার্ভার ফ্লাশ করার ব্যাকগ্রাউন্ড টাস্কে ক্যাশ কী-এর ফিক্সড টুপল স্ক্যান করার সময় 
যেগুলোর মেয়াদ (TTL - Time to Live) এখনো শেষ হয়নি (TTL > 0), সেগুলোকে স্কিপ করে কেবল মেয়াদোত্তীর্ণ ক্যাশ ডিলিট করা:

# ফিক্সড ক্যাশ মেটাডাটা টুপল (Cache_Key, Remaining_TTL_sec)
cache_entries = (
    ("user_session_101", 120),
    ("temp_otp_882", 0),       # 🗑️ এক্সপায়ার্ড
    ("product_catalog", 3600),
    ("cart_data_501", -1)      # 🗑️ এক্সপায়ার্ড
)

for key, ttl in cache_entries:
    if ttl > 0:
        continue  # যেসব ক্যাশ এখনো ভ্যালিড সেগুলো স্কিপ
        
    print(f"🗑️ Purging expired cache key: {key} (TTL: {ttl})")


অ্যাপ নোটিফিকেশন সাইলেন্ট আওয়ার্স ফিল্টার (Do Not Disturb Filter)
ইউজার প্রসেসিং ব্যাকএন্ডে সাইলেন্ট আওয়ার্স (DND Mode Enabled) সক্রিয় থাকা ইউজারদের এসএমএস/পুশ নোটিফিকেশন পাঠানো স্কিপ করে বাকিদের নোটিফিকেশন পাঠানো:

# ফিক্সড ইউজার নোটিফিকেশন প্রেফারেন্স টুপল (Username, DND_Enabled)
user_settings = (
    ("sami", False),
    ("abdullah", True),   # 🔕 DND চালু
    ("rahim", False),
    ("karim", True)       # 🔕 DND চালু
)

for username, dnd_status in user_settings:
    if dnd_status is True:
        print(f"🔕 User '{username}' is in DND mode. Skipping push notification.")
        continue  # DND অন থাকলে স্কিপ
        
    print(f"🔔 Sending promotional push notification to: {username}")



ডেটাবেস ট্রানজেকশন আইটেম ভ্যালিডেশন (Skip Invalid / Negative Amounts)
একটি ই-কমার্স পেমেন্ট প্রসেসিং পাইপলাইনে অর্ডারের আইটেম প্রাইসের টুপল হিসাব করার সময় কোনো প্রডাক্টের
দাম যদি ০ বা নেগেটিভ (<= 0) হয়, সেটিকে স্কিপ করে কেবল সঠিক অ্যামাউন্টগুলো টোটাল বিলের সাথে যোগ করা:

# ফিক্সড প্রোডাক্ট প্রাইস টুপল
cart_item_prices = (1200, -50, 450, 0, 890)
grand_total = 0

for price in cart_item_prices:
    if price <= 0:
        print(f"⚠️️ Invalid item price ({price} BDT) detected. Skipping calculation...")
        continue  # ভুল বা নেগেটিভ ভ্যালু স্কিপ
        
    grand_total += price

print(f"💳 Calculated Grand Total: {grand_total} BDT")


সার্ভার ইউটিলাইজেশন অডিট (Skip Normal CPU Load)
সার্ভারের বিভিন্ন প্রসেসরের সিপিইউ লোড স্পাইকের (% CPU Usage) টুপল স্ক্যান করার সময় যেসব
লোড স্বাভাবিক লেভেলে রয়েছে (<= 80%), সেগুলোকে স্কিপ করে কেবল হাই-লোড ইউটিলাইজেশনগুলো অ্যালার্ট লগে রাইট করা:

# ফিক্সড সিপিইউ নোড ইউটিলাইজেশন টুপল (%)
cpu_node_usage = (45, 88, 30, 95, 62)
high_load_threshold = 80

for usage in cpu_node_usage:
    if usage <= high_load_threshold:
        continue  # নরমাল লোড স্কিপ করে পরের নোডে চলে যাবে
        
    print(f"🚨 High CPU Utilization Alert: Node load is at {usage}%!")



অকার্যকর রিফ্রেশ টোকেন বাইপাস (Skip Expired Auth Sessions)
ব্যাকগ্রাউন্ড ক্রন জব (Cron Job)-এর সাহায্যে ইন-মেমোরি সেশন টুপল স্ক্যান করার সময় যেসব সেশনের 
টোকেন এক্সপায়ার্ড নয় (is_expired is False), সেগুলোকে স্কিপ করে কেবল মেয়াদ শেষ হওয়া সেশনগুলো র‍্যাম থেকে ফ্লাশ করা:

# সেশন মেটাডাটা টুপল (Session_ID, Is_Expired)
auth_sessions = (
    ("sess_101", False),
    ("sess_102", True),   # 🗑️ ফ্লাশ করতে হবে
    ("sess_103", False),
    ("sess_104", True)    # 🗑️ ফ্লাশ করতে হবে
)

for session_id, is_expired in auth_sessions:
    if not is_expired:
        continue  # সক্রিয় সেশনগুলো স্কিপ
        
    print(f"🧹 Flushed expired session from memory: {session_id}")


ফাইল পারমিশন অডিট (Skip Non-Executable Files)
সিস্টেম ফাইল স্ক্যানারের মাধ্যমে ব্যাকএন্ডে ডিরেক্টরির ফাইল রিড মোড টুপল প্রসেস করার সময়
যেসব ফাইলের এক্সিকিউটেবল পারমিশন নেই (is_executable is False), সেগুলোকে স্কিপ করে কেবল রান করার উপযোগী ফাইলগুলোতে সার্ভিস ইনিশিয়ালাইজ করা:


# ফাইল পারমিশন মেটাডাটা টুপল (Filename, Is_Executable)
system_scripts = (
    ("boot.sh", True),
    ("config.json", False), # ⏩ স্কিপ হবে
    ("runner.py", True),
    ("notes.txt", False)    # ⏩ স্কিপ হবে
)

for script, is_exec in system_scripts:
    if not is_exec:
        print(f"⏩ File '{script}' is non-executable. Skipping execution cycle.")
        continue  # রান করার অনুমতি না থাকলে স্কিপ
        
    print(f"🚀 Initializing system script: {script}")



জিও-লোকেশন আইপি ব্লকিং (Country Whitelist Bypass)
গ্লোবাল মোবাইল অ্যাপ ব্যাকএন্ডে ক্লায়েন্টের ইনকামিং লোকেশন কান্ট্রি কোডের টুপল স্ক্যান করার সময়
যেসব কান্ট্রি সার্ভিস রিজিয়নের আওতায় নেই, সেগুলোকে স্কিপ করে কেবল অনুমোদিত কান্ট্রি কোডগুলোর জন্য ডাটা প্রসেস করা:

# ইনকামিং রিকোয়েস্ট কান্ট্রি কোডের ফিক্সড টুপল
request_countries = ("BD", "US", "UNKNOWN", "CA", "INVALID")
allowed_countries = ("BD", "US", "CA")

for country in request_countries:
    if country not in allowed_countries:
        print(f"⏩ Country '{country}' is outside service region. Skipping response build.")
        continue  # অননুমোদিত কান্ট্রি স্কিপ
        
    print(f"🌍 Building localized API response for country: {country}")


ডাটাবেস সফট-ডিলিট ফিল্টার (Skip Soft-Deleted Rows)
ডাটাবেস থেকে আসা রেকর্ডের টুপল স্ক্যান করার সময় যেসব রো সফট-ডিলিট (is_deleted = True) হিসেবে ফ্ল্যাগ করা আছে,
সেগুলোকে স্কিপ করে কেবল একটিভ রোগুলো রিপোর্ট জেনারেশনের জন্য নেওয়া:

# ডাটাবেস রেকর্ড টুপল (Record_ID, Title, Is_Deleted)
db_records = (
    (101, "User_Profile_Module", False),
    (102, "Temp_Billing_Log", True),     # 🗑️️ স্কিপ হবে
    (103, "Payment_Gateway_Core", False),
    (104, "Draft_Order_301", True)       # 🗑️ স্কিপ হবে
)

for rec_id, title, is_deleted in db_records:
    if is_deleted:
        continue  # সফট-ডিলিট হওয়া রেকর্ড স্কিপ
        
    print(f"📊 Processing active DB record #{rec_id}: {title}")


পাবলিক ইমেইল ডোমেইন ফিল্টার (Corporate Email Validator)
এন্টারপ্রাইজ বিটুবি (B2B) ব্যাকএন্ড রেজিস্ট্রেশনের সময় ফ্রি বা পাবলিক ইমেইল
ডোমেইনের (gmail.com, yahoo.com) টুপল প্রসেস করার সময় পাবলিক ইমেইলগুলো স্কিপ করে কেবল কর্পোরেট ইমেইলগুলো ভ্যালিডেট করা:


# রেজিস্ট্রেশন আবেদনকারীদের ইমেইল টুপল
applicant_emails = ("sami@company.com", "user123@gmail.com", "abdullah@techcorp.io", "test@yahoo.com")
public_domains = ("gmail.com", "yahoo.com")

for email in applicant_emails:
    domain = email.split("@")[-1]
    
    if domain in public_domains:
        print(f"⚠️ Email '{email}' uses a public domain ({domain}). Skipping enterprise setup.")
        continue  # পাবলিক ডোমেইন স্কিপ
        
    print(f"🏢 Provisioning corporate workspace for: {email}")


মেসেজ ব্রোকার পে-লোড সাইজ স্ক্যানার (Skip Large Queue Messages)
RabbitMQ বা Kafka ব্যাকগ্রাউন্ড মেসেজ কিউ থেকে প্রসেস হওয়া মেসেজ পে-লোড সাইজের (KB) টুপল স্ক্যান করার সময় 
যেসব মেসেজের সাইজ সর্বোচ্চ থ্রেশহোল্ড (যেমন: ১০০০ KB)-এর চেয়ে বড়, সেগুলোকে মূল এক্সিকিউশন লাইন স্কিপ করে ডেড-লেটার কিউতে পাঠানো:

# কিউ মেসেজ সাইজের ফিক্সড টুপল (Message_ID, Size_KB)
queue_messages = (
    ("msg_001", 120),
    ("msg_002", 1500),  # ⚠️ ওভারসাইজ
    ("msg_003", 450),
    ("msg_004", 2048)   # ⚠️ ওভারসাইজ
)

max_payload_kb = 1000

for msg_id, size in queue_messages:
    if size > max_payload_kb:
        print(f"⏩ Message '{msg_id}' ({size} KB) exceeds payload limit! Skipping fast track.")
        continue  # বড় পে-লোড স্কিপ
        
    print(f"⚡ Processing message '{msg_id}' in high-priority worker pool.")


ইনঅ্যাক্টিভ এপিআই কি স্কিপার (Skip Expired / Inactive API Keys)
থার্ড-পার্টি সার্ভিস ডেটা প্রসেস করার সময় ক্লায়েন্টের পাঠানো এপিআই কি মেটাডাটা টুপল স্ক্যান 
করে যেসব কি-এর স্ট্যাটাস INACTIVE বা REVOKED, সেগুলোকে স্কিপ করে কেবল সক্রিয় কি দিয়ে ডাটা সিঙ্ক চালু রাখা:

# এপিআই কি স্ট্যাটাসের ফিক্সড টুপল (Key_ID, Status)
api_keys = (
    ("key_sec_01", "ACTIVE"),
    ("key_sec_02", "INACTIVE"),  # ⏩ স্কিপ হবে
    ("key_sec_03", "ACTIVE"),
    ("key_sec_04", "REVOKED")   # ⏩ স্কিপ হবে
)

for key_id, status in api_keys:
    if status != "ACTIVE":
        print(f"⏩ API key '{key_id}' is {status}. Skipping data sync cycle.")
        continue  # একটিভ না হলে স্কিপ
        
    print(f"🔑 Syncing background metrics for active API Key: {key_id}")


এইচটিটিপি মেথড ভ্যালিডেটর (Skip Read-Only HTTP GET Requests)
স্টেট চেঞ্জিং বা রাইট অপারেশনাল ব্যাকএন্ড রিকোয়েস্ট ট্র্যাকার প্রসেস করার সময় GET রিকোয়েস্টের 
মেথড টুপল স্ক্যান করে রিড-অনলি রিকোয়েস্টগুলো স্কিপ করা, যাতে কেবল ডাটা পরিবর্তনকারী মেথডগুলো (POST, PUT, DELETE) অডিট লগে সেভ হয়:


# ইনকামিং এইচটিটিপি মেথডের ফিক্সড টুপল
incoming_methods = ("GET", "POST", "GET", "DELETE", "PUT")

for method in incoming_methods:
    if method == "GET":
        continue  # রিড-অনলি GET মেথড স্কিপ
        
    print(f"📝 Logging state-changing action for HTTP Method: {method}")


ইডেমপোটেন্সি কি ফিল্টার (Skip Duplicate Request Hashes)
একই রিকোয়েস্ট ব্যাকএন্ডে বারবার আসা ঠেকানোর জন্য রিকোয়েস্ট হ্যাশের ফিক্সড টুপল স্ক্যান করার সময় যেসব
হ্যাশ ইতোমধ্যে প্রসেস বা সেভ করা হয়েছে (is_processed = True), সেগুলোকে স্কিপ করে নতুন হ্যাশ প্রসেস করা

# ইনকামিং রিকোয়েস্ট ইডেমপোটেন্সি হ্যাশ টুপল (Request_Hash, Is_Processed)
request_hashes = (
    ("0x7a8b", False),
    ("0x9c0d", True),   # ⏩ ডুপ্লিকেট স্কিপ
    ("0x3e2f", False),
    ("0x7a8b", True)    # ⏩ ডুপ্লিকেট স্কিপ
)

for req_hash, is_processed in request_hashes:
    if is_processed:
        print(f"⏩ Duplicate payload hash '{req_hash}' already handled. Skipping...")
        continue  # আগে প্রসেস হওয়া রিকোয়েস্ট স্কিপ
        
    print(f"⚡ Processing unique transaction payload: {req_hash}")


ডাটাবেস স্ন্যাপশট স্যানিটাইজার (Skip Pending Snapshots)
ডাটাবেস ব্যাকআপ ভ্যালিডেশনের সময় স্ন্যাপশট স্টেটাসের ফিক্সড টুপল স্ক্যান করে যেগুলোর স্ট্যাটাস PENDING বা IN_PROGRESS, 
সেগুলোকে সিঙ্ক্রোনাইজেশন ক্রন জব থেকে স্কিপ করে কেবল COMPLETED ব্যাকআপ স্ন্যাপশটগুলো রিমোট স্টোরেজে পাঠানো:

# ডাটাবেস স্ন্যাপশট স্টেটাস টুপল (Snapshot_ID, Status)
db_snapshots = (
    ("snap_2026_01", "COMPLETED"),
    ("snap_2026_02", "PENDING"),     # ⏩ স্কিপ হবে
    ("snap_2026_03", "IN_PROGRESS"), # ⏩ স্কিপ হবে
    ("snap_2026_04", "COMPLETED")
)

for snap_id, status in db_snapshots:
    if status != "COMPLETED":
        print(f"⏩ Snapshot '{snap_id}' is still {status}. Skipping remote upload.")
        continue  # অসম্পূর্ণ স্ন্যাপশট স্কিপ
        
    print(f"☁️ Uploading completed snapshot '{snap_id}' to cloud storage.")


