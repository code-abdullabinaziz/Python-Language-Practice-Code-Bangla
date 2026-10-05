ডিকশনারিতে তথ্য থাকে Key: Value জোড়ায়। যখন আমরা লুপ দিয়ে ডিকশনারি স্ক্যান করি, তখন ব্যাকএন্ড ইঞ্জিনিয়ারিংয়ে break ব্যবহার করা হয়
Emergency Circuit Breaker বা Fail-Fast নীতি হিসেবে—অর্থাৎ কোনো জরুরি ঝুঁকি বা ক্ষতিকর অবস্থা দেখলেই পুরো লুপ সাথে সাথে বন্ধ করে দেওয়া।


🛡️ Real-Life Scenario: Multi-Account Brute-Force Detection
প্রেক্ষাপট: আপনার সার্ভারে কয়েকটি অ্যাকাউন্টের লগইন চেষ্টা পর্যবেক্ষণ করা হচ্ছে।
ডিকশনারিতে ইউজারের নাম (Key) এবং তাদের ভুল পাসওয়ার্ড দেওয়ার সংখ্যা বা ফেইল্ড অ্যাটেম্পট (Value) জমা আছে।

যদি লুপ স্ক্যান করার সময় কোনো একটি অ্যাকাউন্টের ব্যর্থ চেষ্টা ৫ বা তার বেশি পাওয়া যায়,
তবে সিকিউরিটি ইনসিডেন্ট ট্রিগার হবে এবং পুরো স্ক্যানিং লুপ সরাসরি বন্ধ (break) হয়ে থ্রেট মেটিগেশন সিস্টেম চালু করবে।


# ১. ইউজারের লগইন ব্যর্থতার ডেটা (Key: Username, Value: Failed Login Count)
user_failed_attempts = {
    "user_alice": 2,
    "user_bob": 1,
    "user_hacker": 6,  # থ্রেট: ৫-এর বেশি অনাকাঙ্ক্ষিত লগইন চেষ্টা
    "user_charlie": 0
}

print("--- SECURITY AUDIT: SCANNING USER ACCOUNTS ---")

# ২. ডিকশনারির Key এবং Value একসাথে পাওয়ার জন্য .items() লুপ ব্যবহার
for username, failed_count in user_failed_attempts.items():
    
    # থ্রেট ডিটেকশন চেক (অ্যাটাক শনাক্ত হলে তাৎক্ষণিক থামানো)
    if failed_count >= 5:
        print(f"🚨 [CRITICAL ALERT] Potential Brute-Force attack detected on user '{username}'! Attempts: {failed_count}")
        print("🚨 [SECURITY BREAKER] Halting account scan immediately and triggering IP lock down!")
        break  # লুপ সাথে সাথে টার্মিনেট হবে, পরের ইউজারদের আর চেক করবে না
    
    # থ্রেট না থাকলে সাধারণ লগ আউটপুট প্রিন্ট হবে
    print(f"✅ [SAFE] User '{username}' log check passed. Failed attempts: {failed_count}")

print("--- SECURITY AUDIT COMPLETED ---")



--- SECURITY AUDIT: SCANNING USER ACCOUNTS ---
✅ [SAFE] User 'alice' log check passed. Failed attempts: 2
✅ [SAFE] User 'bob' log check passed. Failed attempts: 1
🚨 [CRITICAL ALERT] Potential Brute-Force attack detected on user 'user_hacker'! Attempts: 6
🚨 [SECURITY BREAKER] Halting account scan immediately and triggering IP lock down!
--- SECURITY AUDIT COMPLETED ---



💡 ব্যাকএন্ড ইঞ্জিনিয়ারের মূল টেকঅ্যাওয়ে:
items()-এর ব্যবহার: ডিকশনারি থেকে একসাথে Key (Username) এবং Value (Attempts) বের করে প্রসেস করতে .items() ব্যবহার করা হয়।

Fail-Fast in Dictionary: user_hacker-এর ঘরে ৬টি ফেইল্ড অ্যাটেম্পট পাওয়া মাত্রই break এক্সিকিউট হয়েছে।
ফলে ডিকশনারিতে পরবর্তীতে থাকা user_charlie-কে প্রসেস করার পেছনে সার্ভারের বাড়তি মেমোরি ও সময় নষ্ট হয়নি।









ক্লাউড সার্ভার রিসোর্স মনিটরিং (CPU Overload Protection)
প্রেক্ষাপট: একটি ক্লাউড ডাটা সেন্টারে একাধিক মাইক্রোসার্ভিস চলছে। 
ডিকশনারিতে প্রতিটি সার্ভারের নাম (Key) এবং বর্তমান CPU ব্যবহারের শতাংশ (Value) জমা আছে। 
মনিটরিং ইঞ্জিন লুপ চালিয়ে চেক করার সময় যদি কোনো সার্ভারের CPU ব্যবহার ৯০% বা তার বেশি পায়, 
তবে সিস্টেম পুরো স্ক্যানিং লুপ থামিয়ে (break) দিবে এবং ইমার্জেন্সি লোড ব্যালেন্সার ট্রিগার করবে।


# ১. সার্ভার নোডের তথ্য (Key: Server Name, Value: CPU Usage Percentage)
server_cpu_usage = {
    "node_alpha": 45,
    "node_beta": 62,
    "node_gamma": 94,  # বিপদসীমা: ৯০%-এর বেশি CPU ব্যবহার
    "node_delta": 30
}

print("--- INFRASTRUCTURE HEALTH CHECK STARTED ---")

# ২. ডিকশনারির items() ব্যবহার করে সার্ভার এবং তার CPU মান লুপে বের করা
for server_name, cpu_percent in server_cpu_usage.items():
    
    # সিপিইউ ব্যবহার ৯০%-এর বেশি হলে সিস্টেম প্রটেকশন ট্রিগার
    if cpu_percent >= 90:
        print(f"🚨 [HIGH CPU ALERT] Critical load on '{server_name}': {cpu_percent}% CPU!")
        print("🚨 [CIRCUIT BREAKER] Halting health check. Initiating autoscaling protocol!")
        break  # তাৎক্ষণিক লুপ বন্ধ, পরবর্তী সার্ভার স্ক্যান হবে না
    
    print(f"✅ [HEALTHY] Server '{server_name}' CPU usage is normal: {cpu_percent}%")

print("--- INFRASTRUCTURE HEALTH CHECK COMPLETED ---")



--- INFRASTRUCTURE HEALTH CHECK STARTED ---
✅ [HEALTHY] Server 'node_alpha' CPU usage is normal: 45%
✅ [HEALTHY] Server 'node_beta' CPU usage is normal: 62%
🚨 [HIGH CPU ALERT] Critical load on 'node_gamma': 94% CPU!
🚨 [CIRCUIT BREAKER] Halting health check. Initiating autoscaling protocol!
--- INFRASTRUCTURE HEALTH CHECK COMPLETED ---



মেমোরি ক্যাশ থ্রোটলিং (Memory Limit Enforcement)
প্রেক্ষাপট: ইন-মেমোরি ক্যাশ (যেমন Redis) ডেটা লেয়ার স্ক্যান করা হচ্ছে। 
ডিকশনারিতে সেশন টোকেন (Key) এবং মেমোরির আকার কেবি-তে (Value) আছে। 
ক্যাশ স্ক্যানার স্ক্যান করতে করতে যদি কোনো সেশনের মেমোরি সাইজ ১০২৪ KB (1 MB) পার হয়ে যায়, 
তবে থ্রোটলিং মেকানিজম লুপ বন্ধ (break) করে মেমোরি ওভারফ্লো বন্ধ করবে।


# ১. ইন-মেমোরি সেশন ডাটা (Key: Session Token, Value: Memory Size in KB)
active_sessions_memory = {
    "sess_token_a1": 128,
    "sess_token_b2": 256,
    "sess_token_c3": 1536,  # মেমোরি ওভারফ্লো থ্রেট: ১০২৪ KB-এর বেশি
    "sess_token_d4": 64
}

print("--- MEMORY BUFFER SCAN STARTED ---")

# ২. ডিকশনারি স্ক্যান করা
for token, memory_size_kb in active_sessions_memory.items():
    
    # মেমোরি সীমানা অতিক্রম করলে ব্রেক করা
    if memory_size_kb > 1024:
        print(f"⚠️️ [MEMORY OVERFLOW] Session '{token}' exceeded allocation: {memory_size_kb} KB!")
        print("⚠️ [EMERGENCY STOP] Stopping memory audit to prevent server crash!")
        break  # তাৎক্ষণিক মেমোরি বিহেভিয়ার প্রটেকশন
    
    print(f"✅ [ACCEPTED] Session '{token}' memory within limits: {memory_size_kb} KB")

print("--- MEMORY BUFFER SCAN COMPLETED ---")



--- MEMORY BUFFER SCAN STARTED ---
✅ [ACCEPTED] Session 'sess_token_a1' memory within limits: 128 KB
✅ [ACCEPTED] Session 'sess_token_b2' memory within limits: 256 KB
⚠️️ [MEMORY OVERFLOW] Session 'sess_token_c3' exceeded allocation: 1536 KB!
⚠️ [EMERGENCY STOP] Stopping memory audit to prevent server crash!
--- MEMORY BUFFER SCAN COMPLETED ---



এই উদাহরণ দুটির ইঞ্জিনিয়ারিং লজিক:
Resource Saving: সার্ভার ক্র্যাশ করার আগে বা ওভারলোড হওয়ার আগেই break লুপকে থামিয়ে দেয়, যা মেমোরি ও সিপিইউ সাইকেল বাঁচায়।

items() Method: ডিকশনারির নাম ও মান দুটোকেই একসাথে ব্যবহার করে শর্ত যাচাই করতে dict.items() সবচেয়ে ফাস্ট ও ক্লিন মেথড।





(Dictionary) continue-এর লজিক ব্যাকএন্ড ডাটা প্রসেসিং ও ফিল্টারিং



🛡️ Real-Life Scenario: API Rate Limit & Inactive User Filtering
প্রেক্ষাপট: আপনার ব্যাকএন্ডে সাবস্ক্রিপশন সিস্টেমের ইউজারের তালিকা আছে। ডিকশনারিতে ইউজারের নাম (Key) এবং 
তাদের অ্যাকাউন্ট স্ট্যাটাস বা এপিআই রিকোয়েস্ট কাউন্ট (Value) জমা আছে।

লুপের মাধ্যমে ডাটা প্রসেস করার সময় যদি কোনো ইউজারের অ্যাকাউন্ট "inactive" বা "suspended" পাওয়া যায়, 
তবে তাকে স্কিপ (continue) করে দেওয়া হবে, যেন শুধুমাত্র "active" ইউজারদের রিকোয়েস্টই ডাটাবেজে প্রসেস হয়।


# ১. ইউজারের ইউজারনেম এবং তাদের অ্যাকাউন্ট স্ট্যাটাসের ডিকশনারি
user_account_status = {
    "alice": "active",
    "bob": "suspended",     # ইনভ্যালিড ডাটা: স্কিপ করা হবে
    "charlie": "active",
    "david": "inactive",      # ইনভ্যালিড ডাটা: স্কিপ করা হবে
    "eve": "active"
}

print("--- BACKEND BATCH PROCESSING STARTED ---")

# ২. .items() দিয়ে ইউজারনেম (Key) এবং স্ট্যাটাস (Value) লুপে বের করা
for username, status in user_account_status.items():
    
    # অ্যাকাউন্ট অ্যাক্টিভ না হলে স্কিপ করার ফিল্টার শর্ত
    if status != "active":
        print(f"⚠️ [SKIPPED] Account '{username}' status is '{status}'. Bypassing execution!")
        continue  # ইনঅ্যাক্টিভ ইউজার স্কিপ হয়ে পরবর্তী ইউজারের কাছে চলে যাবে
    
    # শুধুমাত্র Active ইউজারদের জন্য নিচের প্রসেসিং রান হবে
    print(f"✅ [PROCESSED] Successfully processed API queue for user: '{username}'")

print("--- BACKEND BATCH PROCESSING COMPLETED ---")




