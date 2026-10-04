পাইথনে Set ডাটাস্ট্রাকচারে break এবং continue কীভাবে কাজ করে এবং কেন ব্যাকএন্ড ও সাইবার সিকিউরিটিতে এটি অত্যন্ত গুরুত্বপূর্ণ,
পাইথনের set একটি আন-অর্ডারড (unordered) ডাটাস্ট্রাকচার। এর দুটি বিশেষ বৈশিষ্ট্য রয়েছে:এতে কোনো ডুপ্লিকেট এলিমেন্ট থাকে না।
এর লুকআপ (lookup/search) স্পিড O(1), অর্থাৎ অতি দ্রুত ডাটা ফিল্টার করা যায়।
Set-এ break কীভাবে কাজ করে?লুপ চলার সময় নির্দিষ্ট একটি শর্ত পূরণ হওয়া মাত্র লুপটিকে তাত্ক্ষণিকভাবে বন্ধ করে দেওয়ার জন্য break ব্যবহার করা হয়।

🛡️ সাইবার সিকিউরিটি/ব্যাকএন্ড সিনারিও:
মনে করুন, একটি সার্ভারে আইপি অ্যাড্রেসের তালিকা এসেছে। সেখানে কিছু ব্ল্যাকলিস্টেড (Blacklisted) আইপি সেট আকারে আছে।
ব্যাকএন্ড সিস্টেমটি আইপি চেক করতে করতে যদি কোনো অত্যন্ত বিপজ্জনক বা হাই-রিস্ক আইপি খুঁজে পায়,
তবে সাথে সাথে লুপ থামিয়ে দেবেন (Fail-Fast Principle) যাতে সিপিইউ বা মেমোরি নষ্ট না হয়।


# ব্ল্যাকলিস্টেড ক্ষতিকারক আইপির সেট (O(1) সার্চের জন্য Set ব্যবহার করা হয়েছে)
blacklisted_ips = {"192.168.1.10", "10.0.0.5", "172.16.0.99", "185.220.101.5"}

# ইনকামিং রিকোয়েস্টের তালিকা
incoming_traffic = ["192.168.1.5", "10.0.0.5", "192.168.1.20"]

for ip in incoming_traffic:
    if ip in blacklisted_ips:
        print(f"[SECURITY ALERT] Malicious IP detected: {ip}. Blocking process immediately!")
        break  # বাকি আইপিগুলো প্রসেস না করে সাথে সাথে লুপ বন্ধ করে দিল
    
    print(f"[LOG] Processing normal traffic from: {ip}")


[LOG] Processing normal traffic from: 192.168.1.5
[SECURITY ALERT] Malicious IP detected: 10.0.0.5. Blocking process immediately!




💡 ব্যাকএন্ড ইঞ্জিনিয়ার হিসেবে মনে রাখার মূল বিষয়:Unordered Nature: লিস্টের মতো সেটে নির্দিষ্ট ইন্ডেক্স (0, 1, 2) থাকে না। 
তাই সেটে লুপ চালানোর সময় উপাদানগুলো যেকোনো ক্রমানুসারে আসতে পারে
Fail-Fast Concept: কোনো থ্রেট বা অনাকাঙ্ক্ষিত ডাটা পাওয়ার সাথে সাথে break করে দেওয়া সিস্টেম সিকিউরিটি এবং পারফরম্যান্সের জন্য 
একটি ভালো প্র্যাকটিস।Efficiency: লিস্টের বদলে set ব্যবহার করার প্রধান কারণ হলো if ip in blacklisted_ips এই চেকটি O(1) টাইমে শেষ হয়,
যা ব্যাকএন্ডের রেসপন্স টাইম কমিয়ে দেয়।




🛡️ সিচুয়েশন: Automated Botnet & Rate-Limiter Blocker
প্রেক্ষাপট: ব্যাকএন্ড এপিআই-তে হঠাৎ প্রচুর ফেক রিকোয়েস্ট আসছে (DDoS বা Botnet Attack)। 
আপনার কাছে একটি Known Threat Hash/IP-এর Set আছে। লুপের মাধ্যমে ইনকামিং রিকোয়েস্ট আইপি স্ক্যান করার সময় যদি
এমন কোনো আইপি পাওয়া যায় যা High-Risk Botnet বা সিকিউরিটি রুল মারাত্মকভাবে ব্রেক করে,
তবে ব্যাকএন্ড সাথে সাথে পুরো প্রসেসিং ব্লক করে লুপ ব্রেক করবে (Fail-Fast Principle)।

import time

# ১. ওয়ান-টাইম ডেঞ্জারাস বটনেট আইপির সেট (O(1) স্পিড ফিল্টারিংয়ের জন্য Set)
HIGH_RISK_BOTNET_IPS = {
    "185.220.101.5",
    "192.0.2.1",
    "198.51.100.44",
    "203.0.113.195"
}

# ২. ইনকামিং ট্রাফিক বা এপিআই রিকোয়েস্টের লিস্ট
incoming_api_requests = [
    {"request_id": "req_001", "ip": "192.168.1.10", "endpoint": "/api/v1/profile"},
    {"request_id": "req_002", "ip": "10.0.0.15", "endpoint": "/api/v1/feed"},
    {"request_id": "req_003", "ip": "185.220.101.5", "endpoint": "/api/v1/login"}, # Critical Threat
    {"request_id": "req_004", "ip": "192.168.1.25", "endpoint": "/api/v1/checkout"}
]

def analyze_incoming_traffic(traffic_logs):
    print("[SYSTEM LOG] Starting Real-time Traffic Inspection...\n")
    
    for req in traffic_logs:
        req_id = req["request_id"]
        client_ip = req["ip"]
        endpoint = req["endpoint"]
        
        # Threat Set-এ চেক করা (Time Complexity: O(1))
        if client_ip in HIGH_RISK_BOTNET_IPS:
            print(f"🚨 [CRITICAL SECURITY ALERT] Threat Detected from IP: {client_ip}")
            print(f"   Details: Request ID '{req_id}' attempted to access '{endpoint}'")
            print("   Action: Initiating Emergency Circuit Breaker. Halting execution!\n")
            
            # লুপ থামিয়ে দেওয়া যাতে মেমোরি ও সিপিইউ ব্লক না হয়
            break
            
        print(f"✅ [ALLOWED] Request {req_id} from {client_ip} processed successfully.")
        time.sleep(0.1)  # প্রসেসিং টাইম সিমুলেশন

# ফাংশন এক্সিকিউশন
analyze_incoming_traffic(incoming_api_requests)

[SYSTEM LOG] Starting Real-time Traffic Inspection...

✅ [ALLOWED] Request req_001 from 192.168.1.10 processed successfully.
✅ [ALLOWED] Request req_002 from 10.0.0.15 processed successfully.
🚨 [CRITICAL SECURITY ALERT] Threat Detected from IP: 185.220.101.5
   Details: Request ID 'req_003' attempted to access '/api/v1/login'
   Action: Initiating Emergency Circuit Breaker. Halting execution!

💡 কেন এই লজিকটি ভবিষ্যতে ইন্টারভিউ ও রিয়েল প্রজেক্টে কাজে দেবে?
Circuit Breaker Pattern: ৩ নম্বর রিকোয়েস্টে মারাত্মক থ্রেট পাওয়ার পর লুপটি req_004-কে চেক না করেই বন্ধ হয়ে গেছে। এটি সার্ভার ডাউন হওয়া থেকে বাঁচায়।

Set Optimization: ব্যাকএন্ডে হাজার হাজার আইপি বা হ্যাশ চেক করার সময় List-এর বদলে Set ব্যবহার করলে লুকআপ টাইম O(N) থেকে কমে O(1)-এ চলে আসে, 
যা মিলিসেকেন্ডের বদলে মাইক্রোসেকেন্ডে এক্সিকিউট হয়।



Example Start break----


🛡️ সহজ রিয়েল-লাইফ উদাহরণ: ক্ষতিকারক আইপি ব্লক করা
প্রেক্ষাপট: ধরুন আপনার ব্যাকএন্ডে কিছু ওয়েবসাইট ভিজিটরের আইপির লিস্ট এলো। আপনার কাছে একটি ক্ষতিকারক আইপির সেট (Set) আছে। 
সিস্টেম এক এক করে আইপি চেক করবে, আর যদি কোনো বিপজ্জনক আইপি পেয়ে যায়, সাথে সাথে break মেরে সিস্টেম থামিয়ে দেবে।


# ১. বিপজ্জনক আইপির সেট (O(1) স্পিডে খোঁজার জন্য Set ব্যবহার করা হয়েছে)
bad_ips = {"10.0.0.5", "185.220.101.5", "172.16.0.99"}

# ২. ইনকামিং আইপি রিকোয়েস্টের তালিকা
incoming_ips = ["192.168.1.1", "10.0.0.5", "192.168.1.50"]

print("--- SECURITY SCAN STARTED ---")

# ৩. লুপ ব্যবহার করে প্রতিটি আইপি চেক করা হচ্ছে
for ip in incoming_ips:
    
    # সেটের ভেতর দ্রুত আইপি আছে কিনা চেক করা (Fast Check in Set)
    if ip in bad_ips:
        print(f"🚨 [ALERT] Malicious IP detected: {ip}")
        print("🔒 [ACTION] Halting execution immediately. Connection terminated!")
        break  # থ্রেট পাওয়া মাত্রই লুপ বন্ধ করা হচ্ছে
    
    print(f"✅ [SUCCESS] Safe IP processed: {ip}")

print("--- SCAN COMPLETED ---")


💡 সহজে বোঝার ৩টি মূল পয়েন্ট:
১. প্রথম আইপি (192.168.1.1): এটি bad_ips সেটের ভেতর নেই, তাই সাধারণ সার্ভিস চালু রেখে মেসেজ প্রিন্ট করল।

২. দ্বিতীয় আইপি (10.0.0.5): এটি সেটের ভেতর মিলে গেছে! তাই if সত্য হয়ে break কাজ করল।

৩. তৃতীয় আইপি (192.168.1.50): break হয়ে যাওয়ায় লুপ আগেই থেমে গেছে, 
ফলে ৩ নম্বর আইপি পর্যন্ত কোড আর পৌঁছালই না। এতে সার্ভারের মেমোরি ও সময় বাঁচল।

পরে যখন ফাংশন শিখবেন, এই পুরো ব্লকটিকেই একটা ফাংশনের ভেতরে রেখে দিতে পারবেন—মূল লজিক কিন্তু হুবহু এমনই থাকবে!



পাসওয়ার্ড বা টোকেন স্প্রে আক্রমণ স্ক্যানার (Auth Security)
প্রেক্ষাপট: একজন হ্যাকার একের পর এক জাল টোকেন বা এপিআই কী পাঠাচ্ছে। 
আপনার ব্যাকএন্ডে বিপজ্জনক টোকেনগুলোর একটি Set আছে। লুপের মাধ্যমে চেক করার সময় যদি একটিও ব্লকড টোকেন ধরা পড়ে, 
সাথে সাথে লুপ ব্রেক করে পুরো কানেকশন ড্রপ করে দেওয়া হবে।

# ১. রিভোকড বা ব্লক হওয়া সিকিউরিটি টোকেনের সেট (O(1) স্পিড ফিল্টারিং)
revoked_tokens = {"token_x99", "token_bad_88", "token_hack_01"}

# ২. ইনকামিং ট্রাফিক থেকে আসা টোকেনের তালিকা
incoming_requests = ["token_valid_1", "token_valid_2", "token_hack_01", "token_valid_3"]

print("--- AUTHENTICATION SCAN STARTED ---")

# ৩. ফর-লুপ দিয়ে একেকটি টোকেন যাচাই করা
for token in incoming_requests:
    
    # সেটের মাধ্যমে খুব দ্রুত চেক করা
    if token in revoked_tokens:
        print(f"🚨 [UNAUTHORIZED] Revoked token detected: {token}")
        print("🔒 [ACTION] Session terminated immediately! IP added to firewall blocklist.")
        break  # ক্ষতিকারক টোকেন পাওয়ামাত্রই প্রসেস ব্রেক করা হলো
    
    print(f"✅ [AUTHORIZED] Valid token processed: {token}")

print("--- AUTHENTICATION SCAN COMPLETED ---")


--- AUTHENTICATION SCAN STARTED ---
✅ [AUTHORIZED] Valid token processed: token_valid_1
✅ [AUTHORIZED] Valid token processed: token_valid_2
🚨 [UNAUTHORIZED] Revoked token detected: token_hack_01
🔒 [ACTION] Session terminated immediately! IP added to firewall blocklist.
--- AUTHENTICATION SCAN COMPLETED ---



ক্ষতিকারক ফাইল আপলোড ফিল্টার (File Upload Security)
প্রেক্ষাপট: ইউজার সার্ভারে একাধিক ফাইল আপলোড করছে। সিকিউরিটির জন্য আপনার ব্যাকএন্ড প্রতিটি ফাইলের এক্সটেনশন চেক করছে। 
যদি কোনো ফাইল ব্ল্যাকলিস্টেড বা বিপজ্জনক এক্সটেনশন সেটে (Set) মিলে যায়, 
সাথে সাথে আপলোড প্রসেস ব্রেক করে বাকি ফাইলগুলো প্রসেস করা বন্ধ করে দেওয়া হবে।

# ১. বিপজ্জনক বা নিষিদ্ধ ফাইল এক্সটেনশনের সেট
blocked_extensions = {"exe", "bat", "sh", "php"}

# ২. ইউজারের আপলোড করা ফাইলের তালিকা
uploaded_files = ["document.pdf", "image.png", "malware.exe", "notes.txt"]

print("--- FILE SCAN STARTED ---")

# ৩. ফাইলগুলো একে একে স্ক্যান করা
for file in uploaded_files:
    # ফাইলের এক্সটেনশন বের করা (যেমন: malware.exe থেকে 'exe')
    extension = file.split(".")[-1]
    
    # নিষিদ্ধ সেটের ভেতর এক্সটেনশনটি আছে কিনা দেখা
    if extension in blocked_extensions:
        print(f"🚨 [DANGEROUS FILE] Malicious file extension found: .{extension} in '{file}'")
        print("🔒 [ACTION] Aborting all uploads! Deleting temporary memory buffer.")
        break  # ক্ষতিকারক ফাইল পেলেই লুপ ব্রেক
    
    print(f"✅ [CLEAN] File passed safety checks: {file}")

print("--- FILE SCAN COMPLETED ---")


--- FILE SCAN STARTED ---
✅ [CLEAN] File passed safety checks: document.pdf
✅ [CLEAN] File passed safety checks: image.png
🚨 [DANGEROUS FILE] Malicious file extension found: .exe in 'malware.exe'
🔒 [ACTION] Aborting all uploads! Deleting temporary memory buffer.
--- FILE SCAN COMPLETED ---


💡 এই উদাহরণগুলো কেন গুরুত্বপূর্ণ?

মেমোরি ও সিপিইউ সেভিং: উদাহরণ ২-এ malware.exe পাওয়ার পর notes.txt আর প্রসেস করতেই হয়নি।

Fail-Fast Concept: কোনো থ্রেট পাওয়ার পর ১ মিলিসেকেন্ডও দেরি না করে ব্যাকএন্ড এক্সিকিউশন ব্রেক করে দেওয়া সাইবার সিকিউরিটির মূল নীতি।




ডাটাবেজ রেট-লিমিটিং ও ডিডিওএস (DDoS) প্রতিরোধ
প্রেক্ষাপট: একজন ক্লায়েন্ট আপনার এপিআই-তে প্রসেস করার জন্য অনেকগুলো সার্ভার আইডি পাঠিয়েছে।
ব্যাকএন্ডে বিপজ্জনক বা ওভারলোডেড সার্ভার আইডির একটি Set রাখা আছে। রিকোয়েস্ট প্রসেস করার সময় যদি কোনো ব্লকড সার্ভার আইডি ধরা পড়ে,
সাথে সাথে লুপ break করে প্রসেস থামিয়ে দেওয়া হবে যাতে মূল ডাটাবেজ ক্র্যাশ না করে।

# ১. ব্ল্যাকলিস্টেড বা ডাউন থাকা সার্ভার আইডির সেট (O(1) স্পিডে খোঁজার জন্য Set)
flagged_servers = {"srv_99", "srv_dDos_01", "srv_malicious"}

# ২. ইনকামিং ট্রাফিক থেকে আসা সার্ভার আইডির তালিকা
incoming_server_requests = ["srv_01", "srv_02", "srv_dDos_01", "srv_04"]

print("--- TRAFFIC INSPECTION STARTED ---")

# ৩. ফর-লুপ দিয়ে প্রতিটি সার্ভার রিকোয়েস্ট চেক করা
for server in incoming_server_requests:
    
    # সেটের মাধ্যমে অতি দ্রুত আইডি ম্যাচিং করা
    if server in flagged_servers:
        print(f"🚨 [RATE LIMIT EXCEEDED] Suspicious Server ID detected: {server}")
        print("🔒 [ACTION] Emergency Circuit Breaker triggered. Dropping rest of payload!")
        break  # ক্ষতিকারক বা হাই-রিস্ক আইডি পাওয়ামাত্রই লুপ থামিয়ে দেওয়া হলো
    
    print(f"✅ [SUCCESS] Request from {server} processed successfully.")

print("--- TRAFFIC INSPECTION COMPLETED ---")



--- TRAFFIC INSPECTION STARTED ---
✅ [SUCCESS] Request from srv_01 processed successfully.
✅ [SUCCESS] Request from srv_02 processed successfully.
🚨 [RATE LIMIT EXCEEDED] Suspicious Server ID detected: srv_dDos_01
🔒 [ACTION] Emergency Circuit Breaker triggered. Dropping rest of payload!
--- TRAFFIC INSPECTION COMPLETED ---



ক্ষতিকারক এসকিউএল ইনজেকশন (SQL Injection) কিওয়ার্ড ফিল্টার
প্রেক্ষাপট: ইউজার ফর্ম বা এপিআই দিয়ে কিছু টেক্সট ফিল্ড ইনপুট পাঠিয়েছে। 
সিকিউরিটির জন্য আপনার ব্যাকএন্ড ডাটাবেজে ক্যোয়ারি চালানোর আগে ইনপুট চেক করছে। 
যদি ইনপুটে থাকা কোনো শব্দ বিপজ্জনক SQL Injection কিওয়ার্ডের সেটে (Set) মিলে যায়,
সাথে সাথে break করে ক্যোয়ারি এক্সিকিউশন বাতিল করা হবে।

# ১. বিপজ্জনক SQL ইনজেকশন কিওয়ার্ডের সেট
sql_injection_keywords = {"DROP", "DELETE", "UNION", "OR 1=1"}

# ২. ইউজারের পাঠানো সার্চ ইনপুটের শব্দগুলোর তালিকা
user_input_words = ["SELECT", "username", "FROM", "users", "WHERE", "OR 1=1"]

print("--- QUERY SANITIZATION STARTED ---")

# ৩. ইনপুটের প্রতিটি শব্দ একে একে চেক করা
for word in user_input_words:
    
    # সেটের ভেতর বিপজ্জনক শব্দ আছে কিনা চেক করা (Case-Sensitive Match)
    if word in sql_injection_keywords:
        print(f"🚨 [SQL INJECTION ALERT] Dangerous keyword detected: '{word}'")
        print("🔒 [ACTION] Query execution aborted! Security log entry created.")
        break  # ক্ষতিকারক কিওয়ার্ড পেলেই লুপ সাথে সাথে বন্ধ
    
    print(f"✅ [CLEAN] Keyword verified: '{word}'")

print("--- QUERY SANITIZATION COMPLETED ---")


--- QUERY SANITIZATION STARTED ---
✅ [CLEAN] Keyword verified: 'SELECT'
✅ [CLEAN] Keyword verified: 'username'
✅ [CLEAN] Keyword verified: 'FROM'
✅ [CLEAN] Keyword verified: 'users'
✅ [CLEAN] Keyword verified: 'WHERE'
🚨 [SQL INJECTION ALERT] Dangerous keyword detected: 'OR 1=1'
🔒 [ACTION] Query execution aborted! Security log entry created.
--- QUERY SANITIZATION COMPLETED ---

💡 ব্যাকএন্ডের মূল টেকঅ্যাওয়ে:Set ব্যবহার করার কারণ: 
ডাটাবেজ বা আইপির সংখ্যা ১০ হাজার হলেও word in sql_injection_keywords বা server in flagged_servers মাত্র ১ ধাপে (O(1)) খুঁজে বের করে ফেলে।
break ব্যবহার করার কারণ: থ্রেট পাওয়ার পর বাকি শত শত আইটেম প্রসেস করে সময় নষ্ট না করে 
১ মিলিসেকেন্ডেই এক্সিকিউশন থামিয়ে দেওয়া ব্যাকএন্ডকে ফাস্ট ও সেফ রাখে।




ব্যাংকিং বা পেমেন্ট গেটওয়েতে স্যাংশনড্ অ্যাকাউন্ট ফ্রড ফিল্টার (FinTech Security)
প্রেক্ষাপট: ইউজার ব্যাকএন্ডে একসাথে অনেকগুলো ব্যাংক অ্যাকাউন্টে টাকা পাঠানোর রিকোয়েস্ট পাঠিয়েছে। 
কিন্তু আন্তর্জাতিক ফান্ড ট্রান্সফারের ক্ষেত্রে কিছু ব্ল্যাকলিস্টেড/স্যাংশনড্ অ্যাকাউন্ট আইডির Set ব্যাকএন্ডে সেভ থাকে। 
টাকা প্রসেস করার সময় যদি একটিও ব্লকড অ্যাকাউন্ট আইডি পাওয়া যায়, তবে ব্যাকএন্ড সাথে সাথে break করে পুরো ট্রানজ্যাকশন ব্যাচ বাতিল করে দেবে।

# ১. আন্তর্জাতিকভাবে ব্লকড বা স্যাংশনড অ্যাকাউন্ট আইডির সেট (O(1) স্পিড চেক)
sanctioned_accounts = {"ACC_8801", "ACC_FRAUD_99", "ACC_SUSPICIOUS_07"}

# ২. ট্রানজ্যাকশনের জন্য আসা অ্যাকাউন্ট আইডিগুলোর তালিকা
pending_payouts = ["ACC_1001", "ACC_1002", "ACC_FRAUD_99", "ACC_1004"]

print("--- PAYMENT TRANSACTION INSPECTION STARTED ---")

# ৩. ফর-লুপ দিয়ে প্রতিটি অ্যাকাউন্ট আইডি চেক করা
for account_id in pending_payouts:
    
    # সেটের মাধ্যমে দ্রুত সার্চ
    if account_id in sanctioned_accounts:
        print(f"🚨 [FINANCIAL THREAT] Sanctioned/Fraudulent account detected: {account_id}")
        print("🔒 [ACTION] Transaction batch frozen immediately! Fraud division notified.")
        break  # ফ্ল্যাগড অ্যাকাউন্ট পাওয়ামাত্রই পেমেন্ট এক্সিকিউশন থামিয়ে দেওয়া হলো
    
    print(f"✅ [SUCCESS] Account {account_id} cleared for payout processing.")

print("--- PAYMENT TRANSACTION INSPECTION COMPLETED ---")


--- PAYMENT TRANSACTION INSPECTION STARTED ---
✅ [SUCCESS] Account ACC_1001 cleared for payout processing.
✅ [SUCCESS] Account ACC_1002 cleared for payout processing.
🚨 [FINANCIAL THREAT] Sanctioned/Fraudulent account detected: ACC_FRAUD_99
🔒 [ACTION] Transaction batch frozen immediately! Fraud division notified.
--- PAYMENT TRANSACTION INSPECTION COMPLETED ---



আইওটি (IoT) বা ডিভাইস ম্যানেজমেন্ট সিকিউরিটি (Device Auth Guard)
প্রেক্ষাপট: আপনার ক্লাউড ব্যাকএন্ডে শত শত স্মার্ট ডিভাইস (যেমন: স্মার্ট ক্যামেরা বা সেন্সর) কানেক্ট হচ্ছে। 
আপনার কাছে ক্ষতিকারক বা কম্প্রোমাইজড ডিভাইস ম্যাক-অ্যাড্রেসের (MAC Address) একটি Set আছে। 
স্ট্রিম ডাটা রিড করার সময় যদি কোনো হ্যাকড ডিভাইসের সিগন্যাল পাওয়া যায়, ব্যাকএন্ড লুপ সাথে সাথে break করে নেটওয়ার্ক ট্রাফিক বিচ্ছিন্ন্ করে দেবে।


# ১. হ্যাকড বা ব্যাকডোর-সংক্রামিত ডিভাইস ম্যাক-অ্যাড্রেসের সেট
compromised_mac_addresses = {"00:1B:44:11:3A:B7", "AA:BB:CC:DD:EE:FF"}

# ২. সার্ভারে ডেটা পাঠানো ডিভাইসগুলোর তালিকা
incoming_device_stream = ["00:1A:2B:3C:4D:5E", "AA:BB:CC:DD:EE:FF", "12:34:56:78:9A:BC"]

print("--- IOT NETWORK GUARDIAN STARTED ---")

# ৩. একে একে ডিভাইস কানেকশন যাচাই করা
for mac in incoming_device_stream:
    
    # সেটের ভেতর ম্যাক-অ্যাড্রেস চেক করা
    if mac in compromised_mac_addresses:
        print(f"🚨 [HARDWARE SECURITY BREACH] Compromised device detected: {mac}")
        print("🔒 [ACTION] Dropping device socket connection. Emergency isolation triggered!")
        break  # আক্রান্ত ডিভাইস পাওয়ার সাথে সাথেই সিকিউরিটি ব্রেক
    
    print(f"✅ [SECURE CONNECTION] Device {mac} authenticated successfully.")

print("--- IOT NETWORK GUARDIAN COMPLETED ---")




ক্লাউড স্টোরেজ ও ম্যালওয়্যার হ্যাশ ফিল্টার (Cybersecurity Hash Verification)
প্রেক্ষাপট: ইউজারের আপলোড করা ফাইল সার্ভারে সেভ করার আগে ব্যাকএন্ড ফাইলের MD5/SHA256 Hash জেনারেট করে চেক করছে। 
আপনার ব্যাকএন্ডে পরিচিত ম্যালওয়্যার হ্যাশের একটি Set রয়েছে। 
স্ক্যান করার সময় যদি কোনো সংক্রামিত ফাইলের হ্যাশ মেলে, সাথে সাথে break করে ফাইল প্রসেসিং এবং সেভিং প্রসেস বাতিল হয়ে যাবে।

# ১. জানা ম্যালওয়্যার হ্যাশের সেট (O(1) ফাস্ট অনুসন্ধানের জন্য Set)
known_malware_hashes = {"e99a18c428cb38d5f260853678922e03", "44d88612fea8a8f36de82e1278abb02f"}

# ২. সার্ভারে প্রসেসিংয়ের জন্য আসা ফাইল হ্যাশের তালিকা
uploaded_file_hashes = [
    "b10a8db164e0754105b7a99be72e3fe5", 
    "44d88612fea8a8f36de82e1278abb02f", 
    "c3499c2729730a794c21f20a57b28f25"
]

print("--- FILE HASH SCANNER STARTED ---")

# ৩. লুপ দিয়ে একে একে ফাইল হ্যাশ স্ক্যান করা
for file_hash in uploaded_file_hashes:
    
    # সেটের ভেতর ম্যালওয়্যার হ্যাশটি আছে কিনা চেক করা
    if file_hash in known_malware_hashes:
        print(f"🚨 [MALWARE DETECTED] Infectious Hash matched: {file_hash}")
        print("🔒 [ACTION] Quarantining file payload. Aborting disk write immediately!")
        break  # ম্যালওয়্যার হ্যাশ পাওয়ামাত্রই লুপ বন্ধ
    
    print(f"✅ [CLEAN] File hash verified safe: {file_hash}")

print("--- FILE HASH SCANNER COMPLETED ---")


--- FILE HASH SCANNER STARTED ---
✅ [CLEAN] File hash verified safe: b10a8db164e0754105b7a99be72e3fe5
🚨 [MALWARE DETECTED] Infectious Hash matched: 44d88612fea8a8f36de82e1278abb02f
🔒 [ACTION] Quarantining file payload. Aborting disk write immediately!
--- FILE HASH SCANNER COMPLETED ---




ডোমেইন নেইম সার্ভিস (DNS) এবং স্প্যাম ফিড ফিল্টার (Network Security)
প্রেক্ষাপট: ব্যাকএন্ড একটি ইমেইল নোটিফিকেশন ইঞ্জিন চালাচ্ছে। সার্ভিসটি ইমেইল ডোমেইনগুলো ভ্যালিডেট করছে।
যদি আপনার ব্যাকএন্ডের স্প্যাম/ফিশিং ডোমেইনের Set-এ থাকা কোনো ডোমেইন ইমেইল লুপে ধরা পড়ে, 
তবে সাথে সাথে সার্কিট ব্রেক করে পুরো ইমেইল কিউ (Queue) পজ করে দেওয়া হবে।

# ১. স্প্যাম ও ফিশিং ডোমেইনের সেট
phishing_domains = {"bad-phish.com", "verify-bank-secure.xyz", "free-money-now.top"}

# ২. আউটগোয়িং ইমেইল পে-লোডের তালিকা
outgoing_emails = ["user1@gmail.com", "user2@yahoo.com", "admin@verify-bank-secure.xyz", "user3@outlook.com"]

print("--- EMAIL DOMAIN AUDIT STARTED ---")

# ৩. লুপ দিয়ে প্রতিটি ইমেইল ডোমেইন আলাদা করে চেক করা
for email in outgoing_emails:
    # ইমেইল থেকে ডোমেইন অংশটি কেটে আলাদা করা (যেমন: admin@bad-phish.com -> bad-phish.com)
    domain = email.split("@")[-1]
    
    # সেটের মাধ্যমে ডোমেইন চেক
    if domain in phishing_domains:
        print(f"🚨 [PHISHING ALERT] Malicious domain encountered: {domain} in '{email}'")
        print("🔒 [ACTION] Halting email dispatch queue. Flagging sender for review.")
        break  # ফিশিং ডোমেইন পেলেই লুপ ব্রেক
    
    print(f"✅ [VERIFIED] Domain '{domain}' cleared for sending.")

print("--- EMAIL DOMAIN AUDIT COMPLETED ---")


--- EMAIL DOMAIN AUDIT STARTED ---
✅ [VERIFIED] Domain 'gmail.com' cleared for sending.
✅ [VERIFIED] Domain 'yahoo.com' cleared for sending.
🚨 [PHISHING ALERT] Malicious domain encountered: verify-bank-secure.xyz in 'admin@verify-bank-secure.xyz'
🔒 [ACTION] Halting email dispatch queue. Flagging sender for review.
--- EMAIL DOMAIN AUDIT COMPLETED ---




ই-কমার্স ডিসকাউন্ট এবং কুপন ফ্রড প্রিভেনশন (Backend E-Commerce Logic)
প্রেক্ষাপট: একজন ইউজার একই কার্টে একাধিক কুপন কোড অ্যাপ্লাই করার চেষ্টা করছে।
ব্যাকএন্ড কুপনগুলো চেক করছে। যদি কোনো কুপন এক্সপায়ার্ড বা ফ্রড কুপনের Set-এ মেলে, 
তবে কুপন প্রসেসর সাথে সাথে break করবে এবং ইউজারের অর্ডারে কোনো ফেক ডিসকাউন্ট যুক্ত হতে দেবে না।


# ১. ফ্রড ও এক্সপায়ার্ড কুপন কোডের সেট
blacklisted_coupons = {"EXPIRED_50", "HACK_DISCOUNT", "INVALID_PROMO"}

# ২. ইউজারের সাবমিট করা কুপনের তালিকা
applied_coupons = ["SUMMER_10", "WELCOME_05", "HACK_DISCOUNT", "FLAT_20"]

print("--- COUPON VALIDATION ENGINE STARTED ---")

# ৩. একে একে কুপন কোডগুলো যাচাই করা
for coupon in applied_coupons:
    
    # সেটে কুপন আছে কিনা ওয়ান-স্টেপে চেক করা
    if coupon in blacklisted_coupons:
        print(f"🚨 [PROMO FRAUD] Invalid or Blacklisted Coupon applied: {coupon}")
        print("🔒 [ACTION] Aborting discount calculation. Reverting checkout process!")
        break  # ক্ষতিকারক কুপন পেলেই প্রসেস ব্রেক
    
    print(f"✅ [APPLIED] Valid coupon code processed: {coupon}")

print("--- COUPON VALIDATION ENGINE COMPLETED ---")


--- COUPON VALIDATION ENGINE STARTED ---
✅ [APPLIED] Valid coupon code processed: SUMMER_10
✅ [APPLIED] Valid coupon code processed: WELCOME_05
🚨 [PROMO FRAUD] Invalid or Blacklisted Coupon applied: HACK_DISCOUNT
🔒 [ACTION] Aborting discount calculation. Reverting checkout process!
--- COUPON VALIDATION ENGINE COMPLETED ---



মাল্টি-ফ্যাক্টর অথেনটিকেশন (MFA/2FA) ডিভাইস ব্লকড ফিল্টার
প্রেক্ষাপট: ইউজার লগইন করার পর ব্যাকএন্ড ডিভাইস আইডেন্টিফায়ার স্ক্যান করছে। 
আপনার সিস্টেমে রিভোকড বা হ্যাক হওয়া ডিভাইস আইডির একটি Set রাখা আছে। 
লগইন পে-লোড ফিল্টার করার সময় যদি কোনো সংক্রামিত ডিভাইস আইডি মেলে, তবে সাথে সাথে সার্কিট ব্রেক করে কানেকশন ডিসকানেক্ট করে দেওয়া হবে।

# ১. রিভোকড বা নিষিদ্ধ ডিভাইস আইডি-র সেট (O(1) স্পিড চেক)
revoked_device_ids = {"DEV_REVOKED_99", "DEV_SUSPICIOUS_01", "DEV_STOLEN_404"}

# ২. ইনকামিং লগইন রিকোয়েস্টের ডিভাইস আইডি তালিকা
incoming_login_devices = ["DEV_MOBILE_01", "DEV_LAPTOP_02", "DEV_SUSPICIOUS_01", "DEV_TABLET_03"]

print("--- MFA DEVICE SCAN STARTED ---")

# ৩. লুপ ব্যবহার করে প্রতিটি ডিভাইস আইডি ভ্যালিডেট করা
for device_id in incoming_login_devices:
    
    # সেটের ভেতর ডিভাইস আইডি চেক করা
    if device_id in revoked_device_ids:
        print(f"🚨 [SECURITY RISK] Revoked or compromised device detected: {device_id}")
        print("🔒 [ACTION] Invalidating session cookies immediately. Connection dropped!")
        break  # ক্ষতিকারক ডিভাইস পাওয়ামাত্রই লুপ থামিয়ে দেওয়া হলো
    
    print(f"✅ [SUCCESS] Device cleared for session authentication: {device_id}")

print("--- MFA DEVICE SCAN COMPLETED ---")


--- MFA DEVICE SCAN STARTED ---
✅ [SUCCESS] Device cleared for session authentication: DEV_MOBILE_01
✅ [SUCCESS] Device cleared for session authentication: DEV_LAPTOP_02
🚨 [SECURITY RISK] Revoked or compromised device detected: DEV_SUSPICIOUS_01
🔒 [ACTION] Invalidating session cookies immediately. Connection dropped!
--- MFA DEVICE SCAN COMPLETED ---



এপিআই রুট এক্সেস ফিল্টার (Forbidden API Endpoints)
প্রেক্ষাপট: একজন ক্লায়েন্ট বা ইন্টার্ন ব্যাকএন্ডের অ্যাডমিন ক্রন-জব রুটগুলোতে হিট করার চেষ্টা করছে।
সিস্টেম ইন্টারনাল ডিরেক্টরি স্ক্যান করছে। আপনার সেটে নিষিদ্ধ বা হাইলি সেনসিটিভ ব্যাকএন্ড রুটগুলোর তালিকা (Set) রয়েছে।
স্ক্যান করার সময় নিষিদ্ধ রুট ধরা পড়লে প্রসেস সাথে সাথে ব্রেক করবে।


# ১. নিষিদ্ধ বা ব্যাকএন্ড সেনসিটিভ এপিআই রুটের সেট
restricted_endpoints = {"/admin/reset-db", "/api/v1/internal-logs", "/config/env"}

# ২. ইনকামিং ট্রাফিকের হিট করা ইউআরএল বা রুটের তালিকা
requested_routes = ["/api/v1/profile", "/api/v1/dashboard", "/config/env", "/api/v1/settings"]

print("--- API ROUTE AUTHORIZATION STARTED ---")

# ৩. ফর-লুপ দিয়ে ইউআরএল রুট স্ক্যান করা
for route in requested_routes:
    
    # সেটের ভেতর অনাকাঙ্ক্ষিত রুট সার্চ করা
    if route in restricted_endpoints:
        print(f"🚨 [UNAUTHORIZED ACCESS] Attempted to hit restricted route: '{route}'")
        print("🔒 [ACTION] Halting request pipeline! Logging incident for security team.")
        break  # নিষিদ্ধ রুট পেলেই সাথে সাথে ব্রেক
    
    print(f"✅ [AUTHORIZED] Route access granted: '{route}'")

print("--- API ROUTE AUTHORIZATION COMPLETED ---")


--- API ROUTE AUTHORIZATION STARTED ---
✅ [AUTHORIZED] Route access granted: '/api/v1/profile'
✅ [AUTHORIZED] Route access granted: '/api/v1/dashboard'
🚨 [UNAUTHORIZED ACCESS] Attempted to hit restricted route: '/config/env'
🔒 [ACTION] Halting request pipeline! Logging incident for security team.
--- API ROUTE AUTHORIZATION COMPLETED ---



ক্লাউড সার্ভার ব্যাকআপ হ্যাং প্রসেস ফিল্টার
প্রেক্ষাপট: সার্ভারে একাধিক ব্যাকগ্রাউন্ড প্রসেস বা ব্যাকআপ জব একসাথে এক্সিকিউট হচ্ছে। 
সার্ভারের ওভারলোড বা ক্র্যাশ ঠেকাতে ব্যাকএন্ড প্রতিনিয়ত প্রসেস আইডিগুলো (PID) ভ্যালিডেট করে।
সেটে থাকা ক্র্যাশড বা হাং প্রসেস আইডি (Set) ধরা পড়লে সঙ্গে সঙ্গে লুপ ব্রেক করা হয়।


# ১. ক্র্যাশড বা ক্ষতিকারক প্রসেস আইডির (PID) সেট
zombie_pids = {1042, 4096, 8812}

# ২. সার্ভারে প্রসেস হওয়া প্রসেস আইডিগুলোর তালিকা
active_process_queue = [1001, 1002, 4096, 1005]

print("--- PROCESS MONITORING STARTED ---")

# ৩. লুপ চালিয়ে প্রতিটি প্রসেস আইডি স্ক্যান করা
for pid in active_process_queue:
    
    # সেটে প্রসেস আইডিটি আছে কিনা ১ ধাপে চেক
    if pid in zombie_pids:
        print(f"🚨 [SYSTEM CRITICAL] Zombie process ID detected in queue: PID {pid}")
        print("🔒 [ACTION] Killing execution tree! Triggering emergency RAM cleanup.")
        break  # ক্ষতিকারক পিআইডি পেলেই এক্সিকিউশন ব্রেক
    
    print(f"✅ [RUNNING] Process PID {pid} executing safely.")

print("--- PROCESS MONITORING COMPLETED ---")


--- PROCESS MONITORING STARTED ---
✅ [RUNNING] Process PID 1001 executing safely.
✅ [RUNNING] Process PID 1002 executing safely.
🚨 [SYSTEM CRITICAL] Zombie process ID detected in queue: PID 4096
🔒 [ACTION] Killing execution tree! Triggering emergency RAM cleanup.
--- PROCESS MONITORING COMPLETED ---




set continue code start----


break এবং continue-এর লজিক ব্যাকএন্ড ইঞ্জিনিয়ারিং ও সিকিউরিটিতে কীভাবে একে অপরের থেকে আলাদা এবং কার্যকর ভূমিকা রাখে, 
তা বুঝতে এবার continue-এর লজিকটি দেখা প্রয়োজন।

break: থ্রেট পাওয়া মাত্র প্রসেস সম্পূর্ণ বন্ধ করে দেয় (Fail-Fast / Emergency Stop)।

continue: ক্ষতিকারক বা অপ্রয়োজনীয় ডাটাকে স্কিপ (Skip) করে বাকি নিরাপদ অংশগুলোকে প্রসেস করতে থাকে (Filtering / Processing Loop)।



Real-Life Scenario: API Rate-Limiter & Traffic Filter
প্রেক্ষাপট: আপনার এপিআই সার্ভারে অনেকগুলো ইনকামিং ইউজারের রিকোয়েস্ট এসেছে। কিছু ইউজার Suspicious/Rate-Limited Users Set-এর অন্তর্ভুক্ত। 
ব্যাকএন্ড লুপ চালিয়ে সবার রিকোয়েস্ট প্রসেস করবে, 
তবে যারা সেটে থাকবে তাদের স্কিপ (continue) করবে, এবং বৈধ ইউজারদের রিকোয়েস্ট প্রসেস করবে।


# ১. রেট-লিমিটেড বা অস্থায়ীভাবে ব্লক হওয়া ইউজারদের সেট (O(1) ফাস্ট চেক)
rate_limited_users = {"usr_404", "usr_990", "usr_882"}

# ২. এপিআই সার্ভারে আসা ইনকামিং ইউজার রিকোয়েস্টের তালিকা
incoming_requests = ["usr_101", "usr_404", "usr_102", "usr_990", "usr_103"]

print("--- API TRAFFIC PROCESSING STARTED ---")

# ৩. লুপ ব্যবহার করে প্রতিটি ইউজার রিকোয়েস্ট যাচাই করা
for user_id in incoming_requests:
    
    # সেটের ভেতর চেক করা—ইউজার রেট-লিমিটেড কিনা
    if user_id in rate_limited_users:
        print(f"⚠️ [SKIP] User '{user_id}' is rate-limited. Skipping request processing.")
        continue  # কোডের নিচের অংশে না গিয়ে সরাসরি পরবর্তী লুপের আইটেমে চলে যাবে
    
    # শুধুমাত্র বৈধ ইউজারদের জন্য নিচের কোড এক্সিকিউট হবে
    print(f"✅ [PROCESSED] Successfully served payload for User: '{user_id}'")

print("--- API TRAFFIC PROCESSING COMPLETED ---")


--- API TRAFFIC PROCESSING STARTED ---
✅ [PROCESSED] Successfully served payload for User: 'usr_101'
⚠️ [SKIP] User 'usr_404' is rate-limited. Skipping request processing.
✅ [PROCESSED] Successfully served payload for User: 'usr_102'
⚠️ [SKIP] User 'usr_990' is rate-limited. Skipping request processing.
✅ [PROCESSED] Successfully served payload for User: 'usr_103'
--- API TRAFFIC PROCESSING COMPLETED ---


ব্যাকএন্ড ইঞ্জিনিয়ার হিসেবে পার্থক্যটি যেখানে কাজের:
break বনাম continue: usr_404 পাওয়ার পর সিস্টেম পুরো লুপ বন্ধ করেনি; বরং তাকে স্কিপ করে পরবর্তীতে থাকা usr_102 ও usr_103-কে সার্ভিস দিয়েছে।

Resource Optimization: continue ব্যবহার করার ফলে অবৈধ ইউজারদের জন্য নিচের ভারী ডেটাবেজ বা প্রসেসিং লজিক রান হয় না, ফলে সার্ভার সিপিইউ সেভ হয়।




কনটেন্ট মডারেশন ও স্প্যাম ফিল্টার (Spam Content Moderation)
প্রেক্ষাপট: ইউজারের সাবমিট করা কমেন্ট বা মেসেজ প্রসেস করা হচ্ছে। ব্যাকএন্ডে নিষিদ্ধ বা স্প্যাম কিওয়ার্ডের একটি Set রাখা আছে। 
লুপের মাধ্যমে মেসেজ চেক করার সময় যদি কোনো শব্দ স্প্যাম সেটে মিলে যায়, 
তবে সেই স্প্যাম কমেন্টকে স্কিপ (continue) করে দেওয়া হবে এবং পরবর্তী ভালো কমেন্টগুলো ডাটাবেজে সেভ করা হবে।


# ১. স্প্যাম বা নিষিদ্ধ শব্দের সেট (O(1) স্পিড ফিল্টারিং)
spam_keywords = {"buy_now", "free_crypto", "click_here"}

# ২. ইউজারের সাবমিট করা ইনকামিং কমেন্টের তালিকা
incoming_comments = ["hello_there", "click_here", "great_post", "free_crypto", "thanks_for_sharing"]

print("--- CONTENT MODERATION STARTED ---")

# ৩. লুপ দিয়ে একে একে কমেন্ট ফিল্টার করা
for comment in incoming_comments:
    
    # সেটের ভেতর স্প্যাম শব্দটি আছে কিনা চেক করা
    if comment in spam_keywords:
        print(f"⚠️ [SPAM FILTER] Flagged spam word detected: '{comment}'. Skipping database write!")
        continue  # স্প্যাম পাওয়ার পর স্কিপ করে পরবর্তী কমেন্টে চলে যাবে
    
    print(f"✅ [PUBLISHED] Comment cleared and saved: '{comment}'")

print("--- CONTENT MODERATION COMPLETED ---")


--- CONTENT MODERATION STARTED ---
✅ [PUBLISHED] Comment cleared and saved: 'hello_there'
⚠️ [SPAM FILTER] Flagged spam word detected: 'click_here'. Skipping database write!
✅ [PUBLISHED] Comment cleared and saved: 'great_post'
⚠️️ [SPAM FILTER] Flagged spam word detected: 'free_crypto'. Skipping database write!
✅ [PUBLISHED] Comment cleared and saved: 'thanks_for_sharing'


মেমোরি ক্যাশ ইনভাল্যুয়েশন (Redis/In-Memory Cache Filtering)
প্রেক্ষাপট: আপনার ব্যাকএন্ড ইউজারের তথ্যগুলো প্রসেস করে ক্যাশে মেমোরিতে সেভ করছে। 
কিন্তু কিছু ইউজারের ক্যাশ সেশন মেমোরি ইনভ্যালিড সেটে (Set) চলে গেছে। 
প্রসেসর লুপের মাধ্যমে তাদের স্কিপ (continue) করে শুধুমাত্র অ্যাক্টিভ ইউজারদের ক্যাশ ডেটা আপডেট করবে।


# ১. মেয়াদউত্তীর্ণ বা ইনভ্যালিড ক্যাশ সেটের লিস্ট (Set)
invalidated_cache_sessions = {"sess_expired_01", "sess_expired_05"}

# ২. সার্ভারে আসা সেশন আইডিগুলোর তালিকা
active_session_queue = ["sess_active_10", "sess_expired_01", "sess_active_11", "sess_expired_05"]

print("--- CACHE SYNC ENGINE STARTED ---")

# ৩. ফর-লুপ দিয়ে সেশন স্ক্যান করা
for session in active_session_queue:
    
    # সেটের মাধ্যমে দ্রুত স্কিপ চকিং
    if session in invalidated_cache_sessions:
        print(f"⚠️ [CACHE EXPIRED] Session '{session}' is stale. Skipping memory write!")
        continue  # অকার্যকর সেশন স্কিপ করে পরেরটাই যাবে
    
    print(f"✅ [CACHE UPDATED] Successfully updated memory for session: '{session}'")

print("--- CACHE SYNC ENGINE COMPLETED ---")


--- CACHE SYNC ENGINE STARTED ---
✅ [CACHE UPDATED] Successfully updated memory for session: 'sess_active_10'
⚠️ [CACHE EXPIRED] Session 'sess_expired_01' is stale. Skipping memory write!
✅ [CACHE UPDATED] Successfully updated memory for session: 'sess_active_11'
⚠️ [CACHE EXPIRED] Session 'sess_expired_05' is stale. Skipping memory write!
--- CACHE SYNC ENGINE COMPLETED ---


💡 break বনাম continue-এর মূল পার্থক্য:

break: থ্রেট পেলেই পুরো লুপ সাথে সাথে শাটডাউন (যেমন: হ্যাকার বা ম্যালওয়্যার ধরা পড়া)।

continue: ব্যাড ডাটা বা স্প্যাম পেলেই শুধুমাত্র ওই আইটেমটি স্কিপ, লুপ বাকিদের কাজ সম্পন্ন করতে থাকবে (যেমন: ফিল্টারিং বা স্কিপিং)।



ফায়ারওয়াল আইপি ফিল্টারিং (Firewall IP Whitelisting & Filtering)
প্রেক্ষাপট: সার্ভারে হাজার হাজার আইপি থেকে রিকোয়েস্ট আসছে। আপনার সিকিউরিটি সিস্টেমে ব্ল্যাকলিস্টেড বা ক্ষতিকারক আইপির একটি Set আছে।
লুপের মাধ্যমে রিকোয়েস্ট স্ক্যান করার সময় যদি কোনো ক্ষতিকারক আইপি পাওয়া যায়, 
তবে তাকে স্কিপ (continue) করে দেওয়া হবে, যেন সার্ভার বাকি নিরাপদ আইপিগুলোর রিকোয়েস্ট প্রসেস করতে পারে।

# ১. ব্ল্যাকলিস্টেড ক্ষতিকারক আইপির সেট (O(1) স্পিড ফিল্টারিং)
blocked_ip_set = {"198.51.100.1", "203.0.113.5", "192.0.2.99"}

# ২. ইনকামিং ট্রাফিক থেকে আসা আইপিগুলোর তালিকা
incoming_network_traffic = [
    "192.168.1.10", 
    "198.51.100.1",  # ক্ষতিকারক আইপি
    "10.0.0.15", 
    "203.0.113.5",   # ক্ষতিকারক আইপি
    "172.16.0.22"
]

print("--- FIREWALL TRAFFIC SCAN STARTED ---")

# ৩. ফর-লুপ দিয়ে একে একে আইপি ফিল্টার করা
for client_ip in incoming_network_traffic:
    
    # সেটের ভেতর আইপিটি ব্ল্যাকলিস্টেড কিনা দ্রুত চেক করা
    if client_ip in blocked_ip_set:
        print(f"⚠️ [BLOCKED] Malicious traffic skipped from IP: {client_ip}")
        continue  # এই আইপিকে স্কিপ করে সরাসরি পরবর্তী আইপিতে চলে যাবে
    
    # শুধুমাত্র নিরাপদ আইপির জন্য নিচের কোড রান হবে
    print(f"✅ [ALLOWED] Connection established safely for IP: {client_ip}")

print("--- FIREWALL TRAFFIC SCAN COMPLETED ---")


--- FIREWALL TRAFFIC SCAN STARTED ---
✅ [ALLOWED] Connection established safely for IP: 192.168.1.10
⚠️ [BLOCKED] Malicious traffic skipped from IP: 198.51.100.1
✅ [ALLOWED] Connection established safely for IP: 10.0.0.15
⚠️ [BLOCKED] Malicious traffic skipped from IP: 203.0.113.5
✅ [ALLOWED] Connection established safely for IP: 172.16.0.22
--- FIREWALL TRAFFIC SCAN COMPLETED ---

