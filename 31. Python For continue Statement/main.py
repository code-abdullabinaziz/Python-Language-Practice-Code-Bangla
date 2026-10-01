Python-এ continue স্টেটমেন্ট হলো একটি লুপ কন্ট্রোল স্টেটমেন্ট (Loop Control Statement)। 
এর মূল কাজ হলো: লুপের বর্তমান ইটারেশনের (round) বাকি অংশটুকু স্কিপ করে সরাসরি লুপের পরবর্তী ইটারেশনে চলে যাওয়া।

মৌলিক ধারণা (Basic Concept): 
সাধারণভাবে একটি লুপের ভেতর থাকা সব কোড ওপর থেকে নিচে ক্রমান্বয়ে এক্সিকিউট হয়।
কিন্তু কোনো নির্দিষ্ট কন্ডিশনে যদি  লুপকে থামিয়ে না দিয়ে (যা break করে), শুধু ওই রাউন্ডের কোডটুকু এড়িয়ে যেতে চান, তখন continue ব্যবহৃত হয়।


break বনাম continue:

break পেলে পুরো লুপটিই চিরতরে বন্ধ হয়ে যায়।

আর continue পেলে শুধু বর্তমান ইটারেশনটি বা বাদ পড়ে, কিন্তু লুপ চলতে থাকে।


বেসিক উদাহরণ (Basic Examples)

উদাহরণ ১: জোড় সংখ্যা বাদ দিয়ে শুধু বিজোড় সংখ্যা প্রিন্ট করা (for loop)

for num in range(1, 10):
    if num % 2 == 0:
        continue  # সংখ্যাটি জোড় হলে নিচের print() স্কিপ হয়ে যাবে
    print(f"Odd Number: {num}")

Odd Number: 1
Odd Number: 3
Odd Number: 5
Odd Number: 7
Odd Number: 9


while লুপে continue-এর সঠিক ব্যবহার
while লুপে continue ব্যবহারের সময় কাউন্টার ইনক্রিমেন্ট/ডিক্রিমেন্ট কোথায় করছেন সেদিকে খেয়াল রাখা জরুরি।
continue-এর নিচে ইনক্রিমেন্ট রাখলে লুপটি Infinite Loop-এ আটকে যাবে।

❌ ভুল কোড (Infinite Loop তৈরি করবে):

i = 0
while i < 5:
    if i == 3:
        continue  # i-এর মান ৩ হলে i += 1 এর সুযোগ পাবে না, অসীম লুপে পড়ে যাবে!
    print(i)
    i += 1


✅ সঠিক কোড:

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # ৩ নম্বর স্কিপ হবে
    print(f"Current Value: {i}")

Current Value: 1
Current Value: 2
Current Value: 4
Current Value: 5



for i in range(1, 6):
    if i == 3:
        continue
    print(i)





List Comprehension-এ continue-এর বিকল্প (Pythonic Way)
Pythonic কোডে অনেক সময় লুপে explicit continue ব্যবহারের বদলে List Comprehension-এর ভেতরে if ফিল্টার ব্যবহার করা হয়।

লুপ ও continue দিয়ে:

numbers = [1, -2, 3, -4, 5]
positive_numbers = []

for num in numbers:
    if num < 0:
        continue
    positive_numbers.append(num)


List Comprehension দিয়ে (Pythonic & Cleaner):

numbers = [1, -2, 3, -4, 5]
positive_numbers = [num for num in numbers if num >= 0]




ডেটা প্রসেসিং ও ইনভ্যালিড ডেটা ফিল্টারিং (Data Cleaning)
বাস্তব জীবনের ডেটাসেটে প্রায়ই অসম্পূর্ণ বা ক্রুটিপূর্ণ ডেটা থাকে। প্রসেস করার সময় কন্ডিশন ম্যাচ না করলে continue দিয়ে স্কিপ করা হয়।

raw_data = ["100", "200", "N/A", "300", None, "400", "INVALID"]

cleaned_data = []
for entry in raw_data:
    # None টাইপ বা টেক্সট ডেটা বাদ দেওয়া
    if entry is None or not str(entry).isdigit():
        continue
    cleaned_data.append(int(entry))

print(cleaned_data)  # Output: [100, 200, 300, 400]




নেটওয়ার্ক ও এপিআই রিকোয়েস্ট রিট্রাই লজিক (Retry / Error Handling)
নেটওয়ার্ক কল বা এপিআই থেকে রেসপন্স না পেলে লুপ না থামিয়ে ক্র্যাশ এড়াতে পরবর্তী ধাপে যাওয়ার ক্ষেত্রে:

import time

servers = ["server1.com", "server2.com", "server3.com"]

for server in servers:
    response_code = 500  # ধরলাম সার্ভার ২ কাজ করছে না (Simulated)
    if server == "server2.com":
        print(f"Warning: {server} is down. Skipping...")
        continue  # ডাউন সার্ভার স্কিপ করে পরের সার্ভারে যাবে
    
    print(f"Successfully connected to {server}")




বাস্তব জীবনের ব্যাকএন্ড প্রজেক্ট বা ডেটা ক্লিনিংয়ের সময় continue দিয়ে অপ্রয়োজনীয় ডেটা ফিল্টার করা হয়।
ধরা যাক, একটি সিস্টেমের ইউজারের লিস্ট থেকে শুধু ভ্যালিড ইউজারদের প্রসেস করতে হবে এবং কোনো ফাঁকা বা None ভ্যালু পেলে তা স্কিপ করতে হবে:

users = ["Abdullah", "Rahim", None, "Karim", "Sakib"]

for user in users:
    if user is None:
        # যদি ইউজার না থাকে বা ডেটা করাপ্টেড হয়, তবে প্রসেস স্কিপ করো
        continue  
    
    print(f"Processing data for: {user}")

# English comment: Filter out None values using continue in user processing pipeline

Processing data for: Abdullah
Processing data for: Rahim
Processing data for: Karim
Processing data for: Sakib




বাস্তব ব্যবহার — Invalid Data বাদ দিয়ে প্রসেস করা

scores = [85, -1, 92, -1, 78, 45]

for score in scores:
    if score == -1:
        continue   # -1 মানে invalid/missing data, এটা বাদ
    print("Processing score:", score)

Processing score: 85
Processing score: 92
Processing score: 78
Processing score: 45




বাস্তব ব্যবহার — Form Validation (একাধিক ফিল্ড চেক করা)

user_data = {"name": "Rahim", "email": "", "age": 25, "city": None}

for field, value in user_data.items():
    if value == "" or value is None:
        print(f"Skipping empty field: {field}")
        continue
    print(f"Processing {field}: {value}")

Processing name: Rahim
Skipping empty field: email
Processing age: 25
Skipping empty field: city


FastAPI/Backend এ continue কোথায় লাগবে
Invalid/missing data বাদ দিয়ে বাকি ডেটা প্রসেস করা (data cleaning)
Filtering: নির্দিষ্ট শর্ত না মিললে সেই item বাদ দেওয়া
Batch processing: কিছু item এ error হলে সেটা skip করে বাকিগুলো চালিয়ে যাওয়া
Validation: একাধিক field চেক করার সময় খালি/ভুল field বাদ দেওয়া

orders = [{"id": 1, "status": "cancelled"}, {"id": 2, "status": "completed"}, {"id": 3, "status": "cancelled"}]

for order in orders:
    if order["status"] == "cancelled":
        continue
    print("Processing order:", order["id"])




ইউজার ইনপুট ভ্যালিডেশন (Backend/CLI Tools)
ব্যাকএন্ড বা কমান্ড-লাইন টুলে ব্যবহারকারীর থেকে সঠিক ইনপুট না পাওয়া পর্যন্ত লুপ চালাতে হয়। ভুল ইনপুট দিলে continue দিয়ে লুপের শুরুতে পাঠিয়ে দেওয়া হয়।

while True:
    age_input = input("আপনার বয়স লিখুন (অথবা বের হতে 'exit' লিখুন): ").strip()
    
    if age_input.lower() == 'exit':
        print("প্রোগ্রাম শেষ হচ্ছে...")
        break
        
    if not age_input.isdigit():
        print("❌ ভুল ইনপুট! শুধুমাত্র সংখ্যা লিখুন।\n")
        continue  # ভুল ইনপুট হলে নিচের প্রসেসিং স্কিপ করে আবার ইনপুট চাইবে
        
    age = int(age_input)
    if age < 18:
        print("⚠️ আপনার বয়স ১৮-এর কম, অ্যাক্সেস নিষিদ্ধ।\n")
        continue  # বয়স ১৮-এর কম হলে আবার নতুন ইনপুট চাইবে
        
    print("✅ সফলভাবে অ্যাক্সেস দেওয়া হলো!\n")
    break  # সঠিক ইনপুট পেলে লুপ শেষ


এপিআই / সার্ভার কানেকশন রিট্রাই (Networking & Cyber Security)
সাইবার সিকিউরিটি বা ব্যাকএন্ডে অনেক সময় কোনো সার্ভারে বারবার কানেক্ট করার চেষ্টা করা হয়। সার্ভার ডাউন থাকলে continue দিয়ে পরবর্তী চেকিংয়ে যাওয়া হয়।


import time

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    attempts += 1
    print(f"চেষ্টা নম্বর {attempts}: সার্ভারে পিং করা হচ্ছে...")
    
    # সিমুলেশন: ৩ নম্বর চেষ্টায় কানেকশন ফেল করবে
    connection_failed = (attempts == 3)
    
    if connection_failed:
        print("⚠️ কানেকশন ফেল করেছে! ২ সেকেন্ড পর আবার চেষ্টা করা হচ্ছে...\n")
        time.sleep(2)
        continue  # পরের লাইনের প্রসেসিং স্কিপ করে সরাসরি লুপের শুরুতে গিয়ে পরবর্তী চেষ্টা করবে
        
    print("✅ সফলভাবে সার্ভারের সাথে কানেক্টেড হয়েছে!\n")
    break



স্ট্রিমিং ডেটা প্যাকেট প্রসেসিং (Data Stream & Cyber Security)
সাইবার সিকিউরিটিতে নেটওয়ার্ক প্যাকেট অ্যানালাইসিস বা লগ ফাইল চেক করার সময় ক্ষতিকারক/অপ্রয়োজনীয় প্যাকেট এলে তা continue দিয়ে স্কিপ করে বাকি নিরাপদ প্যাকেট প্রসেস করা হয়।

network_packets = [
    {"ip": "192.168.1.1", "status": "CLEAN"},
    {"ip": "10.0.0.5", "status": "MALICIOUS"}, # এটি ক্ষতিকারক
    {"ip": "192.168.1.2", "status": "CLEAN"},
    {"ip": "172.16.0.1", "status": "CORRUPTED"}  # এটি কারাপ্টেড
]

index = 0
while index < len(network_packets):
    packet = network_packets[index]
    index += 1  # while লুপে ইনক্রিমেন্ট continue-এর আগেই করতে হবে
    
    # খারাপ বা ড্যামেজড প্যাকেট স্কিপ করা
    if packet["status"] != "CLEAN":
        print(f"🛡️ স্কিপ করা হলো: IP {packet['ip']} ({packet['status']})")
        continue
        
    # শুধুমাত্র নিরাপদ প্যাকেট প্রসেস করা
    print(f"📦 প্রসেস করা হচ্ছে নিরাপদ প্যাকেট: IP {packet['ip']}")



পাসওয়ার্ড রিকোয়ারমেন্ট চেক (Cyber Security / Auth)
ব্যবহারকারী যতক্ষণ পর্যন্ত একটি শক্তিশালী পাসওয়ার্ড না দেবেন, লুপটি চলতে থাকবে। পাসওয়ার্ড ছোট বা দুর্বল হলে continue দিয়ে নতুন ইনপুট নেওয়া হবে।

while True:
    password = input("Create a password (min 8 chars, at least 1 digit): ").strip()
    
    # শর্ত ১: পাসওয়ার্ড অন্তত ৮ অক্ষরের হতে হবে
    if len(password) < 8:
        print("❌ Too short! Password must be at least 8 characters long.\n")
        continue  # নিচের কোড স্কিপ করে আবার ইনপুট চাইবে
        
    # শর্ত ২: অন্তত একটি সংখ্যা (digit) থাকতে হবে
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        print("❌ Weak password! Must contain at least one digit (0-9).\n")
        continue  # স্কিপ করে আবার ইনপুট চাইবে
        
    print("✅ Password successfully accepted!")
    break




লগ ফাইল ফিল্টারিং (SysAdmin / Cyber Security)
সার্ভারের শত শত লাইনের লগ ফাইল ফিল্টার করার সময় অপ্রয়োজনীয় সাধারণ বার্তা (INFO) স্কিপ করে শুধুমাত্র WARNING বা CRITICAL মেসেজ প্রসেস করার জন্য:

logs = [
    "INFO: User logged in",
    "WARNING: High memory usage detected",
    "INFO: Database connection stable",
    "CRITICAL: Unauthorized access attempt on port 22!",
    "INFO: User logged out"
]

index = 0
while index < len(logs):
    log_entry = logs[index]
    index += 1  # continue-এর আগেই ইনক্রিমেন্ট করতে হবে
    
    # সাধারণ INFO মেসেজ স্কিপ করা
    if log_entry.startswith("INFO"):
        continue
        
    # শুধুমাত্র সিকিউরিটি বা সিস্টেম অ্যালার্ট প্রোসেস করা
    print(f"🚨 Security Alert Processed: {log_entry}")

🚨 Security Alert Processed: WARNING: High memory usage detected
🚨 Security Alert Processed: CRITICAL: Unauthorized access attempt on port 22!



রেইট লিমিটিং বা থ্রোটলিং সেশন (API & Networking)
সার্ভারে রিকোয়েস্ট পাঠানোর সময় নির্দিষ্ট সীমা (Rate limit) পার হয়ে গেলে লুপটি অপেক্ষা (Wait) করবে এবং continue ব্যবহার করে রিট্রাই সাইকেলে ফিরে যাবে।


import time

requests_sent = 0
max_allowed_per_window = 3

while requests_sent < 5:
    requests_sent += 1
    
    # লিমিট পার হলে ৩ সেকেন্ড পজ নিয়ে রিট্রাই সাইকেল শুরু হবে
    if requests_sent > max_allowed_per_window:
        print(f"⚠️ Rate limit exceeded at request {requests_sent}. Waiting 3s...")
        time.sleep(3)
        max_allowed_per_window += 3  # উইন্ডো রিসেট
        continue  # রিট্রাইয়ের জন্য লুপের শুরুতে যাবে
        
    print(f"✅ Request {requests_sent} sent successfully.")



ডাটাবেস পেজিনেশন থেকে ফাঁকা / Null রেকর্ড স্কিপ করা (Backend)
ডাটাবেস বা এক্সটার্নাল এপিআই থেকে ডেটা ফেচ করার সময় অসম্পূর্ণ রেকর্ড স্কিপ করা:


db_records = [
    {"user_id": 101, "email": "user1@example.com"},
    {"user_id": 102, "email": None},  # মিসিং ইমেইল
    {"user_id": 103, "email": "user3@example.com"},
    {}  # সম্পূর্ণ খালি অবজেক্ট
]

cursor = 0
while cursor < len(db_records):
    record = db_records[cursor]
    cursor += 1
    
    # ইনভ্যালিড বা অসম্পূর্ণ রেকর্ড এলে স্কিপ
    if not record or not record.get("email"):
        print("⚠️ Skipping invalid or missing user record...")
        continue
        
    print(f"📧 Sending email to User ID {record['user_id']}: {record['email']}")


সংক্ষেপে মনে রাখার নিয়ম:
while লুপের ভেতরে continue প্রয়োগ করার আগে পয়েন্টার বা ইনডেক্স (cursor += 1) আপডেট করা বাধ্যতামূলক, অন্যথায় অসীম লুপ (Infinite Loop) তৈরি হবে।

যখন কোনো ডাটা ফিল্টারিং বা ক্যালিডেশন শর্ত ব্যর্থ হবে, তখনই continue দিয়ে বাকি ভারী প্রসেসিং এড়িয়ে চলা কোডের পারফরম্যান্স বাড়ায়।



পোর্ট স্ক্যানিং ফিল্টার (Network & Security Scan)
নেটওয়ার্ক স্ক্যান করার সময় কিছু নির্দিষ্ট রিজার্ভড বা ওয়েল-নোন পোর্ট (যেমন: Port 80, 443) বাদ দিয়ে বাকি পোর্টগুলো মনিটর বা ইনস্পেক্ট করার কাজে continue ব্যবহার করা হয়:


ports_to_scan = [21, 22, 80, 443, 3306, 8080]
index = 0

while index < len(ports_to_scan):
    current_port = ports_to_scan[index]
    index += 1  # continue-এর আগেই ইনডেক্স ইনক্রিমেন্ট নিশ্চিত করতে হবে
    
    # Standard Web Ports (80, 443) স্কিপ করা
    if current_port in [80, 443]:
        print(f"ℹ️ Port {current_port} is standard web traffic. Skipping...")
        continue
        
    print(f"🔍 Deep scanning port {current_port} for unusual activity...")

🔍 Deep scanning port 21 for unusual activity...
🔍 Deep scanning port 22 for unusual activity...
ℹ️ Port 80 is standard web traffic. Skipping...
ℹ️️ Port 443 is standard web traffic. Skipping...
🔍 Deep scanning port 3306 for unusual activity...
🔍 Deep scanning port 8080 for unusual activity...


ফাইল থেকে কমেন্ট ও খালি লাইন বাদ দেওয়া (Config / Text Parsing)
সার্ভারের কনফিগারেশন ফাইল বা যেকোনো টেক্সট ফাইল রিড করার সময় # দিয়ে শুরু হওয়া কমেন্ট লাইন এবং খালি লাইন স্কিপ করার জন্য:

config_lines = [
    "# Database Configuration File",
    "DB_HOST=localhost",
    "",  # খালি লাইন
    "# Port setting",
    "DB_PORT=5432",
    "DB_USER=admin"
]

pointer = 0
while pointer < len(config_lines):
    line = config_lines[pointer].strip()
    pointer += 1
    
    # লাইনটি কমেন্ট (#) দিয়ে শুরু হলে অথবা খালি হলে স্কিপ করা
    if not line or line.startswith("#"):
        continue
        
    print(f"⚙️ Loaded Config: {line}")


⚙️ Loaded Config: DB_HOST=localhost
⚙️ Loaded Config: DB_PORT=5432
⚙️ Loaded Config: DB_USER=admin



সার্ভার সিপিইউ মনিটরিং ও অ্যালার্ট (System Architecture)
সিস্টেমের মেমোরি বা সিপিইউ ইউসেজ মনিটর করার সময় স্বাভাবিক অবস্থার কোনো অ্যালার্ট না দিয়ে শুধুমাত্র নির্দিষ্ট থ্রেশহোল্ড (যেমন: ৮০%-এর বেশি) পার হলে প্রসেস চালানো:


import time

cpu_logs = [45, 60, 30, 88, 92, 50]  # সিপিইউ লোডের পার্সেন্টেজ
cursor = 0

while cursor < len(cpu_logs):
    cpu_usage = cpu_logs[cursor]
    cursor += 1
    
    # সিপিইউ লোড ৮০%-এর কম থাকলে স্বাভাবিক, তাই স্কিপ করা
    if cpu_usage < 80:
        continue
        
    # ৮০%-এর বেশি হলে হেভি কাজ বা অ্যালার্ট ট্রিগার করবে
    print(f"⚠️ HIGH CPU USAGE DETECTED: {cpu_usage}%! Triggering cooling action...")




পেমেন্ট গেটওয়েতে ট্রানজেকশন প্রসেসিং (Backend Logic)
পেমেন্ট সিস্টেমের ব্যাচ প্রসেসিংয়ে যদি কোনো ট্রানজেকশন ইতোমধ্যে CANCELLED বা FAILED থাকে, 
তবে সেটির প্রসেসিং বা মানি ট্রান্সফার স্কিপ করে শুধুমাত্র PENDING ট্রানজেকশন প্রসেস করার জন্য:

transactions = [
    {"id": "TXN101", "amount": 500, "status": "COMPLETED"},
    {"id": "TXN102", "amount": 1200, "status": "PENDING"},
    {"id": "TXN103", "amount": 300, "status": "CANCELLED"},
    {"id": "TXN104", "amount": 2500, "status": "PENDING"}
]

idx = 0
while idx < len(transactions):
    txn = transactions[idx]
    idx += 1
    
    # PENDING না হলে প্রসেস স্কিপ
    if txn["status"] != "PENDING":
        print(f"⏭️ Skipping Transaction {txn['id']} (Status: {txn['status']})")
        continue
        
    print(f"💳 Processing Payment for {txn['id']}: ${txn['amount']}")


ব্যাকএন্ড ইঞ্জিনিয়ারিং ও সিস্টেম ডিজাইনে continue-এর মূল উদ্দেশ্য হলো:

প্রসেসিং টাইম বাঁচানো (Efficiency): অপ্রয়োজনীয় ভারী লজিক বা ফাংশন এক্সিকিউট করা থেকে সিস্টেমকে বিরত রাখা।

ক্লিন কোড স্ট্রাকচার (Clean Code): অতিরিক্ত গভীর if-else নেস্টিং এড়ানো।



ওয়েব স্ক্র্যাপিং ও ডেটা এক্সট্রাকশন (Web Scraping / Data Engineering)
ওয়েবসাইট থেকে তথ্য স্ক্র্যাপ বা এক্সট্র্যাক্ট করার সময় যেসব আর্টিকেলে শিরোনাম নেই বা কনটেন্ট অনেক ছোট (যেমন: ১০০ শব্দের কম), সেগুলো মূল প্রসেসিং থেকে বাদ দিতে:

articles = [
    {"title": "Python 3.12 Features", "word_count": 850},
    {"title": "", "word_count": 500},  # মিসিং টাইটেল
    {"title": "Short Note", "word_count": 45},  # খুব ছোট কনটেন্ট
    {"title": "System Architecture Design", "word_count": 1200}
]

idx = 0
while idx < len(articles):
    article = articles[idx]
    idx += 1  # continue-এর আগেই ইনডেক্স ইনক্রিমেন্ট
    
    # খালি টাইটেল অথবা কম শব্দের লেখা স্কিপ
    if not article["title"] or article["word_count"] < 100:
        print(f"⚠️ Skipping low-quality or invalid article...")
        continue
        
    print(f"📰 Publishing Article: '{article['title']}' ({article['word_count']} words)")



ফাইল সিস্টেম ও এক্সটেনশন ফিল্টারিং (Batch File Processing)
কোনো ফোল্ডারের ফাইলগুলো প্রসেস করার সময় অনাকাঙ্ক্ষিত ফাইলের ধরন (যেমন: .tmp বা .log ফাইল) স্কিপ করে শুধু নির্দিষ্ট দরকারি ফাইল (.pdf বা .png) প্রসেস করার জন্য:

files = ["document1.pdf", "cache.tmp", "image1.png", "debug.log", "report.pdf"]

cursor = 0
while cursor < len(files):
    filename = files[cursor]
    cursor += 1
    
    # .tmp এবং .log ফাইল স্কিপ করা
    if filename.endswith(".tmp") or filename.endswith(".log"):
        print(f"🗑️ Skipping temporary/log file: {filename}")
        continue
        
    print(f"📄 Processing valid file: {filename}")



সিকিউরিটি টোকেন ও সেশন এক্সপায়ারি চেক (Cyber Security & Auth)
সার্ভারে সক্রিয় ইউজার সেশনগুলো চেক করার সময় যেগুলোর টোকেন ইতোমধ্যে Expired হয়ে গেছে, সেগুলোর রিকোয়েস্ট এক্সেপ্ট না করে সরাসরি স্কিপ করা:

user_sessions = [
    {"user": "abdullah", "token_valid": True},
    {"user": "guest_1", "token_valid": False},
    {"user": "admin", "token_valid": True}
]

pointer = 0
while pointer < len(user_sessions):
    session = user_sessions[pointer]
    pointer += 1
    
    # ইনভ্যালিড টোকেন হলে স্কিপ
    if not session["token_valid"]:
        print(f"🚫 Unauthorized request from user '{session['user']}'! Skipping...")
        continue
        
    print(f"🔑 Session granted for: {session['user']}")




ডাটাবেস মাইগ্রেশন ও ইউনিক আইডি চেক (Backend & DB Ops)
পুরোনো ডাটাবেস থেকে নতুন ডাটাবেসে ডাটা মাইগ্রেট করার সময় কোনো রো-তে যদি Primary Key (ID) মিসিং থাকে, তাহলে সিস্টেম ক্র্যাশ করা এড়াতে continue ব্যবহার করা হয়:

rows = [
    {"id": 1001, "name": "Server Alpha"},
    {"name": "Server Beta"},  # ID মিসিং!
    {"id": 1003, "name": "Server Gamma"}
]

i = 0
while i < len(rows):
    row = rows[i]
    i += 1
    
    # ID না থাকলে মাইগ্রেশন স্কিপ
    if "id" not in row:
        print("⚠️ Data Corruption Warning: Row without ID found. Skipping row...")
        continue
        
    print(f"💾 Migrating Record ID {row['id']}: {row['name']}")

যখনই লুপের ভেতর কোনো বিষয়কে ইনভ্যালিড (Invalid), মিসিং (Missing), টেম্পোরারি (Temporary) অথবা আনঅথরাইজড (Unauthorized) পাবেন,
তখনই continue বসিয়ে দিবেন। এতে কোড ক্র্যাশ করবে না এবং অতিরিক্ত if-else নেস্টিং ছাড়া সুন্দর ও ক্লিন থাকবে।



মেমোরি ক্যাশ ইনvalidation ও মিসিং কি (Backend & Redis Cache)
ব্যাকএন্ডে Redis বা In-memory ক্যাশ থেকে ডেটা তুলে আনার সময় যদি কোনো কী (Key) পাওয়া না যায় (Cache Miss),
তবে ভারী ডাটাবেস কোয়েরি থেকে সিস্টেম রক্ষা করতে বা ইনভ্যালিড ক্যাশ স্কিপ করতে:

cache_data = [
    {"key": "user_101", "val": "Mohammad"},
    {"key": "user_102", "val": None},  # Cache Miss
    {"key": "user_103", "val": "Abdullah"}
]

index = 0
while index < len(cache_data):
    item = cache_data[index]
    index += 1
    
    # ক্যাশে ভ্যালু না থাকলে স্কিপ
    if item["val"] is None:
        print(f"⚠️ Cache miss for {item['key']}. Skipping fast path...")
        continue
        
    print(f"⚡ Fetched from cache: {item['key']} -> {item['val']}")


ক্লাউড ডেপ্লয়মেন্ট হেলথ চেক (DevOps & Cloud)
ক্লাউড সার্ভারে (যেমন Kubernetes বা AWS) একাধিক মাইক্রোসার্ভিস বা কন্টেইনার চালুর সময় সার্ভিস হেলথ চেক করা হয়। 
কোনো সার্ভিস যদি UNHEALTHY থাকে, তবে সেটি লোড ব্যালেন্সারে যুক্ত না করে স্কিপ করা হয়:

services = [
    {"name": "Auth Service", "status": "HEALTHY"},
    {"name": "Payment Engine", "status": "UNHEALTHY"},
    {"name": "Notification API", "status": "HEALTHY"}
]

ptr = 0
while ptr < len(services):
    service = services[ptr]
    ptr += 1
    
    if service["status"] != "HEALTHY":
        print(f"🚨 Skipping deployment for {service['name']} (Status: {service['status']})")
        continue
        
    print(f"🚀 Deploying to production: {service['name']}")



ডিস্ক স্পেস মনিটরিং ও লগ রোটেশন (System Administration)
সার্ভারের বিভিন্ন পার্টিশনের ডিস্ক স্পেস চেক করার সময় যদি স্পেস ৯০%-এর বেশি পূর্ণ থাকে, তবেই শুধু ডিস্ক ক্লিনআপ বা লগ ফাইল ডিলিট করার কমান্ড দেওয়া হয়:


disk_partitions = [
    {"mount": "/home", "usage": 45},
    {"mount": "/var/log", "usage": 92},
    {"mount": "/tmp", "usage": 30}
]

cursor = 0
while cursor < len(disk_partitions):
    partition = disk_partitions[cursor]
    cursor += 1
    
    # ৯০%-এর নিচে থাকলে ক্লিনআপ স্কিপ
    if partition["usage"] < 90:
        continue
        
    print(f"🧹 Clearing logs for {partition['mount']} (Disk usage at {partition['usage']}%)")


মেসেজ কিউ প্রসেসিং ও ডেড লেটার ফিল্টারিং (System Architecture & RabbitMQ/Kafka)
মেসেজ ব্রোকার বা কিউ (Queue) থেকে ব্যাকগ্রাউন্ড জব প্রসেস করার সময় যদি মেসেজটিতে কোনো বিষাক্ত ডেটা (Poison Pill) থাকে বা ডুপ্লিকেট রিপ্লে বার্তা হয়, তবে তা স্কিপ করা হয়:

queue_messages = [
    {"msg_id": 1, "payload": "Process Image", "retries": 0},
    {"msg_id": 2, "payload": "Corrupted Job", "retries": 5},  # ব্যাকঅফ লিমিট পার
    {"msg_id": 3, "payload": "Send Email", "retries": 1}
]

i = 0
while i < len(queue_messages):
    msg = queue_messages[i]
    i += 1
    
    # ৩বারের বেশি রিট্রাই হওয়া মেসেজ স্কিপ
    if msg["retries"] > 3:
        print(f"❌ Moving Message #{msg['msg_id']} to Dead Letter Queue (Too many retries)")
        continue
        
    print(f"⚙️ Executing Worker Task: {msg['payload']}")




for -----------

পাইথনে for লুপের সাথে continue স্টেটমেন্ট হলো ডাটা প্রসেসিং, ব্যাকএন্ড ইঞ্জিনিয়ারিং, এবং সাইবার সিকিউরিটির অন্যতম শক্তিশালী হাতিয়ার।

while লুপের সাথে for লুপের বড় সুবিধা হলো: এখানে আপনাকে ম্যানুয়ালি ইনডেক্স ইনক্রিমেন্ট (i += 1) নিয়ে চিন্তা করতে হয় না।
পাইথন নিজে থেকেই লিস্ট, ডিকশনারি, ফাইল বা রেঞ্জের ওপর দিয়ে অটোমেটিক ইটারেট করে।

ব্যাকএন্ডে লিস্ট ফিল্টারিং ও স্কিপিং (Backend & Data Processing)
ইউজার লিস্ট বা কোনো অবজেক্টের অ্যাররে প্রসেস করার সময় ইনঅ্যাক্টিভ বা ব্যানড অ্যাকাউন্টগুলো স্কিপ করে শুধু অ্যাক্টিভ ইউজারদের নোটিফিকেশন পাঠানোর কাজে:

users = [
    {"username": "abdullah", "status": "active", "email": "abdullah@example.com"},
    {"username": "hacker99", "status": "banned", "email": "hacker@example.com"},
    {"username": "rafiq", "status": "inactive", "email": "rafiq@example.com"},
    {"username": "sami", "status": "active", "email": "sami@example.com"}
]

for user in users:
    # অ্যাক্টিভ না হলে স্কিপ
    if user["status"] != "active":
        print(f"⏭️ Skipping {user['username']} (Status: {user['status']})")
        continue
        
    # শুধু অ্যাক্টিভ ইউজারদের ইমেইল প্রসেস করা
    print(f"📧 Sending notification email to: {user['email']}")



সাইবার সিকিউরিটি: আইপি ব্ল্যাকলিস্ট চেকিং (Cyber Security)
সার্ভারের ইনকামিং ট্রাফিক বা নেটওয়ার্ক রিকোয়েস্ট চেক করার সময় ব্ল্যাকলিস্টেড বা ক্ষতিকারক আইপি স্কিপ বা ব্লক করা:


blacklisted_ips = {"10.0.0.5", "192.168.1.100"}

incoming_requests = [
    {"ip": "192.168.1.15", "path": "/login"},
    {"ip": "10.0.0.5", "path": "/admin"},      # Malicious IP
    {"ip": "172.16.0.2", "path": "/dashboard"}
]

for req in incoming_requests:
    if req["ip"] in blacklisted_ips:
        print(f"🛡️ BLOCKED: Request from blacklisted IP {req['ip']} to {req['path']}")
        continue  # ব্ল্যাকলিস্টেড আইপির রিকোয়েস্ট প্রসেস না করে সরাসরি পরের রিকোয়েস্টে চলে যাবে
        
    print(f"✅ Allowed access to {req['path']} for IP {req['ip']}")




ফাইল রিডিং ও লাইন ফিল্টারিং (File I/O & System Admin)
কোনো টেক্সট বা লিনাক্স সার্ভিস ফাইল রিড করার সময় যেসব লাইন # দিয়ে শুরু (কমেন্ট লাইন) বা ফাঁকা ব্ল্যাঙ্ক লাইন, সেগুলো স্কিপ করার জন্য:


log_lines = [
    "# System Log File - 2026",
    "2026-10-01 10:00:01 - Server started",
    "",  # Blank line
    "# Maintenance window",
    "2026-10-01 10:05:22 - Database connected"
]

for line in log_lines:
    clean_line = line.strip()
    
    # কমেন্ট বা ব্ল্যাঙ্ক লাইন স্কিপ
    if not clean_line or clean_line.startswith("#"):
        continue
        
    print(f"📝 Processing Log: {clean_line}")



ডিকশনারি ও কি-ভ্যালু পেয়ার ভ্যালিডেশন (API Development)
JSON ডেটা বা API Payload রিসিভ করার সময় যেসব ফিল্ড None বা খালি, সেগুলো স্কিপ করে শুধু ভ্যালিড ডেটা প্রসেস করতে:


payload = {
    "title": "Backend Engineering Roadmap",
    "description": None,  # Missing
    "tags": "python, dsa, security",
    "views": 0,
    "author": ""  # Empty string
}

for key, value in payload.items():
    # ভ্যালু None বা খালি স্ট্রিং হলে স্কিপ
    if value is None or value == "":
        print(f"⚠️ Missing or empty field: '{key}'. Skipping...")
        continue
        
    print(f"🔹 Processing Field -> {key}: {value}")



সিকিউরিটি: পাসওয়ার্ড ক্র্যাকিং বা ডিকশনারি অ্যাটাক ফিল্টারিং (Cyber Security)
সাইবার সিকিউরিটিতে পাসওয়ার্ড অ্যানালাইসিস বা হ্যাশ ম্যাচিং করার সময় নির্দিষ্ট পলিসি (যেমন: অত্যন্ত ছোট বা সাধারণ শব্দ) স্কিপ করে প্রসেসিং টাইম বাঁচানোর জন্য:

passwords_wordlist = ["123456", "admin", "P@ssw0rd2026!", "qwerty", "Secure#System99"]

for pwd in passwords_wordlist:
    # ৮ অক্ষরের চেয়ে ছোট বা সাধারণ খুব দুর্বল পাসওয়ার্ড প্রসেস না করে স্কিপ
    if len(pwd) < 8 or pwd.lower() in ["12345678", "password"]:
        print(f"⏩ Skipping weak dictionary entry: '{pwd}'")
        continue
        
    print(f"🔑 Testing strong candidate password: '{pwd}'")



    
ডেটা সাইন্স & মেশিন লার্নিং: আউটলায়ার (Outlier) বাদ দেওয়া (Data Engineering)
কোনো সেন্সর ডেটা বা সার্ভার রেসপন্স টাইম ফিল্টার করার সময় অস্বাভাবিক বা ভুল মান (Outlier) বাদ দিতে:

response_times_ms = [120, 150, 4500, 110, -5, 130]  # ৪৫০০ms (অস্বাভাবিক) ও -৫ms (ভুল ডেটা)

for time in response_times_ms:
    # ঋণাত্মক সময় বা ৪০০০ms-এর বেশি লেটেন্সি স্কিপ করা
    if time < 0 or time > 4000:
        print(f"⚠️ Anomaly detected ({time}ms). Skipping outlier...")
        continue
        
    print(f"📊 Valid Response Time: {time}ms")



নেটওয়ার্কিং: সিকিউর প্রোটোকল ম্যাচিং (Networking & HTTP/HTTPS)
কোনো ইউআরএল (URL) লিস্টের ওপর ইটারেট করে অনিরাপদ http:// লিঙ্ক স্কিপ করে শুধুমাত্র এনক্রিপ্টেড https:// লিঙ্ক প্রসেস করতে:


urls = [
    "http://insecure-site.com",
    "https://secure-bank.com",
    "http://test-api.org",
    "https://api.github.com"
]

for url in urls:
    if not url.startswith("https://"):
        print(f"⚠️ Unencrypted HTTP URL skipped: {url}")
        continue
        
    print(f"🔒 Establishing secure connection to: {url}")



for লুপে continue-এর গোল্ডেন রুলস:
পারফরম্যান্স অপটিমাইজেশন: লুপের ভেতরে ভারী কোনো ফাংশন, ডাটাবেস কল বা এপিআই রিকোয়েস্ট থাকলে তার আগেই কন্ডিশন চেক করে continue বসালে প্রসেসিং টাইম বহুগুণ বেঁচে যায়।

ক্লিন স্ট্রাকচার: এটি অতিরিক্ত গভীর if-else নেস্টিং এড়ায়, যার ফলে কোড সহজে রিড করা যায়।



অ্যাসিনক্রোনাস ব্যাকএন্ড জবস (AsyncIO & API Rate Limit Handling)
অ্যাসিঙ্ক লুপ ব্যবহার করে একাধিক এক্সটার্নাল সার্ভিস চেক করার সময় যদি কোনো নির্দিষ্ট সার্ভিস 429 Too Many Requests বা HTTP এরর দেয়, 
তখন সেই সার্ভিসটির এক্সিকিউশন স্কিপ করে পরবর্তী টাস্কে চলে যাওয়ার জন্য:


import asyncio

async def fetch_status(service_name):
    # সিমুলেটেড এপিআই রেসপন্স
    mock_responses = {
        "Auth Service": 200,
        "Payment Gateway": 429,  # Rate limited
        "Notification API": 200
    }
    await asyncio.sleep(0.1)
    return mock_responses.get(service_name, 500)

async def process_services():
    services = ["Auth Service", "Payment Gateway", "Notification API"]
    
    for service in services:
        status = await fetch_status(service)
        
        # ৪২৯ রেসপন্স পেলে স্কিপ করা
        if status == 429:
            print(f"⚠️ Rate limit hit for '{service}'. Skipping for now...")
            continue
            
        print(f"✅ Successfully processed job for '{service}' (Status: {status})")

# Async Loop Execution
asyncio.run(process_services())



সাইবার সিকিউরিটি: প্যাকেটের গভীরতা মেপে থ্রেট অ্যানালাইসিস (Packet Depth Analysis)
সার্ভারের নেটওয়ার্ক সিকিউরিটিতে প্রতিটি সেশনের প্যাকেটের বাইট অ্যানালাইসিস করার সময় নির্দিষ্ট থ্রেশহোল্ড ম্যাচ না করলে ভারী ডিক্রিপশন প্রসেস স্কিপ করা:


network_streams = [
    {"stream_id": 1, "bytes": b"GET /index.html", "encrypted": False},
    {"stream_id": 2, "bytes": b"\x00\x01\x02\x03", "encrypted": True}, # Encrypted
    {"stream_id": 3, "bytes": b"POST /admin/login", "encrypted": False}
]

for stream in network_streams:
    # যদি স্ট্রিম এনক্রিপ্টেড হয় তবে প্লেইনটেক্সট থ্রেট অ্যানালাইজার স্কিপ করবে
    if stream["encrypted"]:
        print(f"🔐 Stream #{stream['stream_id']} is encrypted. Bypassing plaintext analyzer...")
        continue
        
    payload = stream["bytes"].decode("utf-8")
    print(f"🔍 Analyzing Payload Stream #{stream['stream_id']}: '{payload}'")



ফিল্টারিং: অ্যাপ্লিকেশনের ইনঅ্যাক্টিভ ইউজার বাদ দেওয়া (Backend Logic)
ইউজার লিস্ট প্রসেস করার সময় যারা inactive বা banned, তাদের স্কিপ করে কেবল সক্রিয় ইউজারদের নোটিফিকেশন পাঠাতে:

users = [
    {"username": "abdullah", "status": "active"},
    {"username": "unknown_user", "status": "banned"},
    {"username": "rafiq", "status": "inactive"},
    {"username": "sami", "status": "active"}
]

for user in users:
    # অ্যাক্টিভ না হলে স্কিপ
    if user["status"] != "active":
        print(f"Skipping user {user['username']} (Status: {user['status']})")
        continue
        
    print(f"Sending notification email to {user['username']}...")



সাইবার সিকিউরিটি: ক্ষতিকারক/ব্ল্যাকলিস্টেড আইপি ট্রাফিক স্কিপ করা
সার্ভারের রিকোয়েস্ট লগে থাকা আইপি অ্যাড্রেস চেকিংয়ের সময় ব্ল্যাকলিস্ট করা আইপি এলে তা স্কিপ করে পরবর্তী রিকোয়েস্ট প্রসেস করতে:

blacklisted_ips = {"10.0.0.5", "192.168.1.100"}

incoming_requests = [
    {"ip": "192.168.1.15", "path": "/login"},
    {"ip": "10.0.0.5", "path": "/admin"},      # Malicious IP
    {"ip": "172.16.0.2", "path": "/dashboard"}
]

for req in incoming_requests:
    if req["ip"] in blacklisted_ips:
        print(f"BLOCKED: Request from blacklisted IP {req['ip']} to {req['path']}")
        continue  # ব্ল্যাকলিস্টেড আইপির প্রসেসিং স্কিপ
        
    print(f"Allowed access to {req['path']} for IP {req['ip']}")



ফাইল রিডিং: কমেন্ট ও খালি লাইন এড়ানো (File Parsing)
কনফিগারেশন ফাইল রিড করার সময় # দিয়ে শুরু হওয়া কমেন্ট এবং ফাঁকা লাইনগুলো এড়িয়ে আসল কনফিগ ডেটা পড়তে:


config_lines = [
    "# Database Configuration File",
    "DB_HOST=localhost",
    "",  # Empty line
    "# Port setting",
    "DB_PORT=5432"
]

for line in config_lines:
    clean_line = line.strip()
    
    # কমেন্ট বা খালি লাইন হলে স্কিপ
    if not clean_line or clean_line.startswith("#"):
        continue
        
    print(f"Loaded Config -> {clean_line}")


এপিআই পে লোড ভ্যালিডেশন (API Validation)
JSON ডেটা বা API Payload রিসিভ করার সময় যেসব ফিল্ডে ইনভ্যালিড ডেটা বা None রয়েছে, সেগুলো স্কিপ করে শুধু সঠিক ডেটা দিয়ে ডেটাবেস আপডেট করার জন্য:


user_payload = {
    "name": "Mohammad Abdullah",
    "age": None,  # ইনভ্যালিড/খালি
    "email": "abdullah@example.com",
    "website": "",  # খালি স্ট্রিং
    "role": "developer"
}

clean_payload = {}

for key, value in user_payload.items():
    # ভ্যালু ফাঁকা বা None হলে স্কিপ করা
    if value is None or value == "":
        print(f"⚠️ Field '{key}' is missing or empty. Skipping...")
        continue
        
    clean_payload[key] = value

print(f"✅ Final Clean Payload: {clean_payload}")


          
ট্রাই-এক্সেপ্ট (Try-Except) এর সাথে ক্র্যাশ হ্যান্ডলিং (Error Handling)
লিস্টে একাধিক টাইপের ডেটা থাকলে টাইপ কনভার্সনে ত্রুটি (Error) আসতে পারে। 
কোনো আইটেমে এরর হলে পুরো প্রোগ্রাম ক্র্যাশ না করিয়ে continue দিয়ে ওই আইটেম স্কিপ করা যায়:

mixed_inputs = ["100", "200", "invalid_number", "300", None, "400"]
processed_numbers = []

for item in mixed_inputs:
    try:
        # স্ট্রিংকে ইন্টিজারে রূপান্তর করার চেষ্টা
        number = int(item)
    except (ValueError, TypeError):
        print(f"❌ Failed to parse '{item}'. Skipping error...")
        continue  # এরর এলে স্কিপ করে পরবর্তী আইটেমে যাবে
        
    processed_numbers.append(number)

print(f"📊 Processed Numbers: {processed_numbers}")



ব্যাচ ফাইল এক্সটেনশন ফিল্টারিং (Batch File Processing)
কোনো ফোল্ডারের অনেকগুলো ফাইলের ভেতর থেকে নির্দিষ্ট কিছু ফাইল (যেমন: .tmp বা .bak ব্যাকআপ ফাইল) স্কিপ করে মূল ফাইলগুলো প্রসেস করতে:


filenames = ["data_1.csv", "temp_cache.tmp", "users.json", "old_backup.bak", "logs.txt"]

for fname in filenames:
    # ব্যাকআপ বা টেম্পোরারি ফাইল স্কিপ করা
    if fname.endswith(".tmp") or fname.endswith(".bak"):
        print(f"🗑️ Ignoring system file: {fname}")
        continue
        
    print(f"📁 Processing essential file: {fname}")




                 
