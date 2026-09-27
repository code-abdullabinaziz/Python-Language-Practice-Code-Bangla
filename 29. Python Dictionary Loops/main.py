সাধারণত পাইথনে ডিকশনারির ওপর লুপ চালানোর জন্য for লুপ ব্যবহার করাটাই সবচেয়ে জনপ্রিয় এবং পাইথনিক নিয়ম (যেমন: for k, v in dict.items():)।

তবে রিয়েল-লাইফ প্রজেক্টে বা ব্যাকএন্ড ডেভেলপমেন্টের কিছু বিশেষ ক্ষেত্রে (যেমন: টাস্ক কিউ প্রসেসিং, ব্যাকগ্রাউন্ড জব হ্যান্ডলিং, বা যখন ডিকশনারি থেকে ডেটা প্রসেস করার সাথে সাথে সেগুলো ডিলিট করতে হয়) 
while লুপ দারুণভাবে কাজে লাগে।

ব্যাকগ্রাউন্ড টাস্ক কিউ প্রসেসিং (Task Queue Processing using .popitem())
ব্যাকএন্ড প্রজেক্টে প্রায়ই এমন হয় যে, একটি ডিকশনারির মধ্যে অনেকগুলো কাজ বা রিকোয়েস্ট জমে থাকে। while লুপের মাধ্যমে
একটি একটি করে কাজ প্রসেস করে ডিকশনারি খালি করে ফেলা হয়। 


# Background task queue stored as a dictionary {task_id: task_name}
task_queue = {
    'task_1': 'Send Welcome Email', 
    'task_2': 'Process Payment', 
    'task_3': 'Generate Monthly Report'
}

print("Starting background task processing...\n")

# The while loop runs as long as the task_queue dictionary is NOT empty
while task_queue:
    # .popitem() removes and returns the last (key, value) pair as a tuple
    task_id, task_name = task_queue.popitem()
    print(f"Processing [{task_id}] -> {task_name}...")

print("\nAll tasks completed and queue is now empty!")

Starting background task processing...

Processing [task_3] -> Generate Monthly Report...
Processing [task_2] -> Process Payment...
Processing [task_1] -> Send Welcome Email...

All tasks completed and queue is now empty!

.popitem() একদম শেষের টাস্ক থেকে শুরু করে উল্টো দিক থেকে প্রসেস করতে করতে ডিকশনারিটিকে পুরোপুরি খালি করে ফেলে, 
আর while task_queue চেক করে যে ডিকশনারিতে ডেটা আছে কি না।



ইনডেক্স ভিত্তিক ট্র্যাডিশনাল while লুপ (list ও index ব্যবহার করে)
যদি কখনো আপনার কোডের লজিক অনুযায়ী ইনডেক্স ধরে ধরে ডিকশনারির কি এবং ভ্যালু এক্সেস করার প্রয়োজন পড়ে, 
তবে কিগুলোকে লিস্টে রূপান্তর করে while লুপ চালানো যায়।


student_scores = {
    'math': 85, 
    'english': 78, 
    'science': 92, 
    'history': 88
}

# 1. Convert dictionary keys into a list
keys_list = list(student_scores.keys())
index = 0

print("Iterating through dictionary using a while loop:\n")

# 2. Running the while loop based on the length of the list
while index < len(keys_list):
    current_key = keys_list[index]
    current_value = student_scores[current_key]
    
    print(f"Subject: {current_key.capitalize()} | Score: {current_value}")
    
    # Increment the index to avoid an infinite loop
    index += 1


Iterating through dictionary using a while loop:

Subject: Math | Score: 85
Subject: English | Score: 78
Subject: Science | Score: 92
Subject: History | Score: 88


Dictionary থেকে Key-Value একটা একটা করে সরিয়ে প্রসেস করা (Queue এর মতো)

tasks = {"task1": "ইমেইল পাঠাও", "task2": "রিপোর্ট বানাও", "task3": "মিটিং সেট করো"}

while tasks:
    task_id, task_desc = tasks.popitem()
    print(f"প্রসেস হচ্ছে: {task_id} -> {task_desc}")

print("সব task শেষ হয়ে গেছে")


এখানে কী হচ্ছে:

while tasks: → যতক্ষণ tasks dictionary খালি না হয় (খালি dictionary মানে False)
popitem() → একটা task সরিয়ে প্রসেস করছে
Dictionary খালি হয়ে গেলে loop নিজে থেকেই থেমে যাবে

বাস্তব ব্যবহার: Backend এ Task Queue বা Job Processing System এ এই প্যাটার্ন ব্যবহার হয় — যতক্ষণ কাজ বাকি আছে, ততক্ষণ প্রসেস করতে থাকা।


নির্দিষ্ট Key খুঁজে বের করা পর্যন্ত Loop চালানো 

users = {101: "Rahim", 205: "Karim", 309: "Salma", 412: "Fatema"}
user_ids = list(users.keys())

index = 0
target_id = 309
found = False

while index < len(user_ids) and not found:
    current_id = user_ids[index]
    if current_id == target_id:
        print(f"পাওয়া গেছে: {users[current_id]}")
        found = True
    index += 1

if not found:
    print("ইউজার পাওয়া যায়নি")


বাস্তব ব্যবহার: কোনো নির্দিষ্ট ইউজার খুঁজে বের করা, একটা সীমার মধ্যে (যদিও বাস্তবে সরাসরি if target_id in users ব্যবহার করা
আরও efficient, কিন্তু while দিয়ে manually search করার logic এটা)।




Retry Logic — Dictionary তে ডেটা না পাওয়া পর্যন্ত চেষ্টা করা

cache = {}  # শুরুতে খালি cache
attempts = 0
max_attempts = 3
key_to_find = "user_data"

while key_to_find not in cache and attempts < max_attempts:
    print(f"চেষ্টা #{attempts + 1}: ডেটা আনার চেষ্টা হচ্ছে")
    
    # ধরে নিচ্ছি ৩য় চেষ্টায় ডেটা পাওয়া যায় (বাস্তবে API/DB call হতো)
    if attempts == 2:
        cache[key_to_find] = "ইউজারের তথ্য পাওয়া গেছে"
    
    attempts += 1

if key_to_find in cache:
    print(f"ফলাফল: {cache[key_to_find]}")
else:
    print("ডেটা আনা যায়নি")


বাস্তব ব্যবহার: Backend এ caching system এ এই প্যাটার্ন ব্যবহার হয় — cache তে ডেটা না থাকলে, নির্দিষ্ট সংখ্যক বার চেষ্টা করে আনার চেষ্টা করা।



Dictionary এর সব Value যোগ করা (Total বের করা) — while দিয়ে

product_prices = {"pen": 10, "book": 50, "bag": 500, "pencil": 5}

keys = list(product_prices.keys())
total = 0
i = 0

while i < len(keys):
    product = keys[i]
    total += product_prices[product]
    i += 1

print(f"সব পণ্যের মোট দাম: {total}")
বাস্তব ব্যবহার: Shopping cart এর মোট দাম বের করা, backend এ order total calculate করা।



Stock/Inventory Management — নির্দিষ্ট পরিমাণ না হওয়া পর্যন্ত

inventory = {"apple": 50, "banana": 30, "mango": 20}
required_apples = 100
current_apples = inventory["apple"]

while current_apples < required_apples:
    print(f"বর্তমান apple: {current_apples}, আরও লাগবে")
    inventory["apple"] += 10   # প্রতিবার ১০টা করে নতুন স্টক আসছে ধরে নিচ্ছি
    current_apples = inventory["apple"]

print(f"পর্যাপ্ত apple হয়ে গেছে: {current_apples}")

বাস্তব ব্যবহার: E-commerce backend এ Inventory/Stock management সিস্টেমে এই ধরনের logic ব্যবহার হয়।





User Input নিয়ে Dictionary Update করতে থাকা (যতক্ষণ ইউজার থামতে না বলে)

student_marks = {}

while True:
    name = input("ছাত্রের নাম দাও (থামতে 'exit' লেখো): ")
    
    if name == "exit":
        break
    
    marks = int(input(f"{name} এর নম্বর দাও: "))
    student_marks[name] = marks
    print(f"{name} যোগ করা হলো")

print("চূড়ান্ত ফলাফল:", student_marks)

বাস্তব ব্যবহার: Data entry system, admin panel এ একের পর এক তথ্য ইনপুট নেওয়া।


Rate Limiting Simulation (Dictionary দিয়ে ইউজার ট্র্যাক করা)

request_counts = {}
user_id = "user_123"
max_requests = 5

request_counts[user_id] = 0

while request_counts[user_id] < max_requests:
    request_counts[user_id] += 1
    print(f"রিকোয়েস্ট #{request_counts[user_id]} প্রসেস হলো")

print(f"{user_id} এর জন্য সর্বোচ্চ রিকোয়েস্ট সীমা শেষ")

বাস্তব ব্যবহার: API rate limiting — একজন ইউজার কতবার API call করতে পারবে সেটা track করা, FastAPI backend এ এটা খুব common।



Pagination এর মতো — Dictionary থেকে ব্যাচ (batch) আকারে ডেটা নেওয়া

all_users = {1: "Rahim", 2: "Karim", 3: "Salma", 4: "Fatema", 5: "Nasir"}
user_ids = list(all_users.keys())

batch_size = 2
index = 0

while index < len(user_ids):
    batch = user_ids[index:index + batch_size]
    print("এই ব্যাচে আছে:", [all_users[uid] for uid in batch])
    index += batch_size


আউটপুট:

এই ব্যাচে আছে: ['Rahim', 'Karim']
এই ব্যাচে আছে: ['Salma', 'Fatema']
এই ব্যাচে আছে: ['Nasir']

বাস্তব ব্যবহার: Database থেকে বড় পরিমাণ ডেটা একসাথে না এনে ছোট ছোট ব্যাচে আনা (memory efficient), এটাকে batch processing বলে।



এটি হলো একটি ইন্টারেক্টিভ ডেটা লুকআপ সিস্টেম (Interactive Lookup System), যেখানে while লুপের মাধ্যমে ইউজারের কাছ থেকে ইনপুট নিয়ে ডিকশনারি থেকে ডেটা সার্চ করা হয়:

# Student database (Nested dictionary storing student details)
students_db = {
    'abdullah': {'course': 'Python Backend', 'cgpa': 3.63},
    'rahim': {'course': 'JavaScript', 'cgpa': 3.50},
    'karim': {'course': 'Database', 'cgpa': 3.80}
}

print("--- Student Database Lookup System ---")
print("Type 'exit' to quit the program.\n")

# A while loop that keeps running until the user types 'exit'
while True:
    # Taking input from the user and converting to lowercase for safety
    search_name = input("Enter student name to search: ").strip().lower()
    
    # Check if the user wants to exit the loop
    if search_name == 'exit':
        print("Exiting search system. Goodbye!")
        break
        
    # Safely searching the dictionary using .get()
    student_info = students_db.get(search_name)
    
    if student_info:
        print(f"-> Found! Course: {student_info['course']} | CGPA: {student_info['cgpa']}\n")
    else:
        print("-> Student not found in the database. Please try again.\n")


এই উদাহরণটি কেন গুরুত্বপূর্ণ?
১. while True + break প্যাটার্ন: ব্যাকএন্ড সার্ভার বা সিএলআই (CLI) অ্যাপ্লিকেশনে বারবার কাজ চালানোর জন্য এই লজিকটি সবচেয়ে বেশি ব্যবহার করা হয়।
২. নিরাপদ সার্চ (.get()): ডিকশনারিতে ডেটা না থাকলেও কোড ক্র্যাশ না করে সুন্দরভাবে মেসেজ দেখায়।
৩. নেস্টেড ডিকশনারি (Nested Dictionary): একটি ডিকশনারির ভেতরে আরেকটি ডিকশনারি রেখে কীভাবে রিয়েল-ডেটা ম্যানেজ করতে হয়, তার চমৎকার উদাহরণ এটি।








for------


শুধু Key নিয়ে Loop করা

person = {"name": "Rahim", "age": 25, "city": "Dhaka"}

for key in person:
    print(key)


name
age
city


Key দিয়ে Value বের করা


for key in person:
    print(key, ":", person[key])


name : Rahim
age : 25
city : Dhaka


items() দিয়ে Key আর Value একসাথে (সবচেয়ে বেশি ব্যবহৃত পদ্ধতি)

for key, value in person.items():
    print(f"{key}: {value}")

name: Rahim
age: 25
city: Dhaka


শুধু Value নিয়ে Loop করা

for value in person.values():
    print(value)


Rahim
25
Dhaka



বাস্তব উদাহরণ — একাধিক ইউজারের তথ্য প্রসেস করা (Backend এর কাছাকাছি)

users = {
    101: {"name": "Rahim", "age": 25},
    102: {"name": "Karim", "age": 30},
    103: {"name": "Salma", "age": 22}
}

for user_id, info in users.items():
    print(f"ID: {user_id}, নাম: {info['name']}, বয়স: {info['age']}")

ID: 101, নাম: Rahim, বয়স: 25
ID: 102, নাম: Karim, বয়স: 30
ID: 103, নাম: Salma, বয়স: 22



শর্ত সহ Loop করা (Filtering)

marks = {"Rahim": 85, "Karim": 45, "Salma": 92, "Nasir": 38}

for name, mark in marks.items():
    if mark >= 40:
        print(f"{name} পাস করেছে (নম্বর: {mark})")
    else:
        print(f"{name} ফেল করেছে (নম্বর: {mark})")


Rahim পাস করেছে (নম্বর: 85)
Karim পাস করেছে (নম্বর: 45)
Salma পাস করেছে (নম্বর: 92)
Nasir ফেল করেছে (নম্বর: 38)


Nested Dictionary এর ভিতরে for loop (Advanced)

students = {
    "student1": {"name": "Rahim", "subjects": ["Math", "Physics"]},
    "student2": {"name": "Karim", "subjects": ["Chemistry", "Biology"]}
}

for student_id, details in students.items():
    print(f"{details['name']} এর বিষয়সমূহ:")
    for subject in details["subjects"]:
        print(f"  - {subject}")


Rahim এর বিষয়সমূহ:
  - Math
  - Physics
Karim এর বিষয়সমূহ:
  - Chemistry
  - Biology



        
Dictionary Comprehension (for দিয়ে এক লাইনে নতুন Dictionary বানানো)

prices = {"pen": 10, "book": 50, "bag": 500}

# ১০% ছাড় দিয়ে নতুন dictionary বানানো
discounted = {item: price * 0.9 for item, price in prices.items()}
print(discounted)   # {'pen': 9.0, 'book': 45.0, 'bag': 450.0}



          
শর্ত সহ Dictionary Comprehension
          
 prices = {"pen": 10, "book": 50, "bag": 500}

# ১০% ছাড় দিয়ে নতুন dictionary বানানো
discounted = {item: price * 0.9 for item, price in prices.items()}
print(discounted)   # {'pen': 9.0, 'book': 45.0, 'bag': 450.0}         
        

Real Backend Example — API Response তৈরি করা (খুবই বাস্তব ব্যবহার)


raw_data = {
    "u1": {"name": "Rahim", "active": True},
    "u2": {"name": "Karim", "active": False},
    "u3": {"name": "Salma", "active": True}
}

active_users = []

for user_id, info in raw_data.items():
    if info["active"]:
        active_users.append(info["name"])

print(active_users)   # ['Rahim', 'Salma']

বাস্তব ব্যবহার: এটা ঠিক FastAPI backend এ database থেকে আসা raw data
থেকে শুধু active users ফিল্টার করে API response তৈরি করার মতো একটা প্যাটার্ন।



        
দুইটা Dictionary মার্জ (merge) করে Loop করা

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = {**dict1, **dict2}   # b এর ক্ষেত্রে dict2 এর মান জিতবে (পরে যা আসে সেটাই থাকে)

for key, value in merged.items():
    print(key, value)



a 1
b 3
c 4

          

enumerate() দিয়ে Dictionary এর items() এ index সহ Loop


scores = {"Rahim": 85, "Karim": 45, "Salma": 92}

for index, (name, score) in enumerate(scores.items()):
    print(f"{index + 1}. {name}: {score}")


1. Rahim: 85
2. Karim: 45
3. Salma: 92



.items() দিয়ে একসাথে Key ও Value (এটাই সবচেয়ে বেশি লাগবে)

student = {"name": "Rahim", "age": 22, "class": "10"}

for key, value in student.items():
    print(key, "->", value)




বাস্তব Backend দৃশ্য — Login Check করা (খুবই গুরুত্বপূর্ণ প্যাটার্ন)

registered_users = {
    "rahim123": "pass123",
    "karim456": "pass456",
    "salma789": "pass789"
}

input_username = "karim456"
input_password = "pass456"

login_success = False

for username, password in registered_users.items():
    if username == input_username and password == input_password:
        login_success = True
        break

if login_success:
    print("লগিন সফল!")
else:
    print("ভুল username অথবা password")


বাস্তব ব্যবহার: এটা ঠিক backend authentication system এর একদম সরলীকৃত (simplified) ভার্সন — ইউজারনেম-পাসওয়ার্ড মেলানো।


API Response তৈরি করা — Active Users বের করা


users = {
    "u1": {"name": "Rahim", "is_active": True},
    "u2": {"name": "Karim", "is_active": False},
    "u3": {"name": "Salma", "is_active": True}
}

active_user_names = []

for user_id, details in users.items():
    if details["is_active"]:
        active_user_names.append(details["name"])

print(active_user_names)
        
বাস্তব ব্যবহার: FastAPI তে database থেকে আসা ইউজার লিস্ট থেকে শুধু active ইউজারদের নাম বের করে API response এ পাঠানো — এটা প্রতিনিয়ত হয়।
          


Product Price থেকে Total বের করা (E-commerce এর মতো)

cart = {
    "pen": {"price": 10, "quantity": 3},
    "book": {"price": 50, "quantity": 2},
    "bag": {"price": 500, "quantity": 1}
}

total = 0

for product, details in cart.items():
    item_total = details["price"] * details["quantity"]
    total += item_total
    print(f"{product}: {details['quantity']} x {details['price']} = {item_total}")

print(f"সর্বমোট: {total}")


বাস্তব ব্যবহার: Shopping cart এর total বিল হিসাব করা — E-commerce backend এ এটা অপরিহার্য (essential)।



Validation — সব Field ঠিকভাবে দেওয়া আছে কিনা চেক করা

user_input = {
    "name": "Rahim",
    "email": "",
    "age": 25
}

errors = []

for field, value in user_input.items():
    if value == "" or value is None:
        errors.append(f"{field} খালি রাখা যাবে না")

if errors:
    print("ভুল পাওয়া গেছে:")
    for error in errors:
        print(f"- {error}")
else:
    print("সব ঠিক আছে")

বাস্তব ব্যবহার: এটা ঠিক Pydantic (FastAPI এর validation library) যা করে তার একটা সরলীকৃত ভার্সন —
যেকোনো form/API input validate করার সময় এই ধরনের logic লাগে।




Word Counting (Text Analysis এর জন্য বাস্তব ব্যবহার)

text = "the quick brown fox jumps over the lazy dog the fox runs"
words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f"{word}: {count} বার")


বাস্তব ব্যবহার: Search engine, text analysis, spam detection — এসব জায়গায় শব্দ গণনার এই প্যাটার্ন প্রচুর ব্যবহার হয়।



Grouping — Category অনুযায়ী ডেটা ভাগ করা

products = {
    "apple": "fruit",
    "carrot": "vegetable",
    "banana": "fruit",
    "potato": "vegetable",
    "mango": "fruit"
}

grouped = {}

for product, category in products.items():
    if category not in grouped:
        grouped[category] = []
    grouped[category].append(product)

print(grouped)


{'fruit': ['apple', 'banana', 'mango'], 'vegetable': ['carrot', 'potato']}

বাস্তব ব্যবহার: এই প্যাটার্ন backend এ grouping/categorization করার সময় খুব বেশি ব্যবহার হয় — 
যেমন সব অর্ডারকে status অনুযায়ী ভাগ করা (pending, completed, cancelled)।



ডিকশনারি ডেটা দিয়ে গ্রুপিং বা ক্যাটাগরি তৈরি করা (Grouping Data)
ইকমার্স বা ব্লগিং প্রজেক্টে প্রায়ই বিভিন্ন ক্যাটাগরির পণ্য বা পোস্ট আলাদা করতে হয়। যেমন—
এখানে  একটি ডিকশনারির ডেটা লুপ চালিয়ে প্রাইসের ওপর ভিত্তি করে পণ্যগুলোকে আলাদা ক্যাটাগরিতে ভাগ করব।


# Products and their prices
products = {
    'laptop': 85000,
    'mouse': 800,
    'keyboard': 2500,
    'monitor': 22000,
    'pendrive': 600
}

expensive_products = {}
affordable_products = {}

# Iterating through the dictionary using a for loop to categorize items
for item, price in products.items():
    if price > 5000:
        expensive_products[item] = price
    else:
        affordable_products[item] = price

print("Expensive Products (> 5000 BDT):", expensive_products)
print("Affordable Products (<= 5000 BDT):", affordable_products)


Expensive Products (> 5000 BDT): {'laptop': 85000, 'monitor': 22000}
Affordable Products (<= 5000 BDT): {'mouse': 800, 'keyboard': 2500, 'pendrive': 600}



ফ্রিকোয়েন্সি কাউন্টিং বা ওয়ার্ড কাউন্ট (Counting Frequencies)
ব্যাকএন্ড ডেটা অ্যানালিসিস বা সিকিউরিটি লগ চেকিংয়ের সময় কোনো একটি শব্দ বা অ্যাক্টিভিটি কতবার এসেছে (Count)
তা বের করার জন্য ডিকশনারি ও for লুপের এই কম্বিনেশনটি ম্যাজিকের মতো কাজ করে।


# A list of user roles or log actions recorded in a backend system
actions = ['login', 'logout', 'login', 'purchase', 'login', 'purchase', 'logout']

action_counts = {}

# Looping through the list to count occurrences in a dictionary
for action in actions:
    # If the action is already in the dictionary, increase its count by 1
    # If not, initialize it with 1 using .get() for safety
    action_counts[action] = action_counts.get(action, 0) + 1

print("Action Frequency Count Report:")
for act, count in action_counts.items():
    print(f"- {act}: {count} times")

Action Frequency Count Report:
- login: 3 times
- logout: 2 times
- purchase: 2 times



নেস্টেড ডিকশনারি লুপ চালানো (Iterating Through Nested Dictionaries)
ডাটাবেজ বা এপিআই রেসপন্সে অনেক সময় ডিকশনারির ভেতরে আরেকটি ডিকশনারি থাকে। 
তখন মূল ডিকশনারি থেকে ডেটা বের করতে নেস্টেড for লুপ (for লুপের ভেতরে আরেকটি for লুপ) ব্যবহার করতে হয়।

# Nested dictionary storing multiple students' information
classroom = {
    'abdullah': {'age': 30, 'course': 'Python Backend', 'cgpa': 3.63},
    'rahim': {'age': 28, 'course': 'JavaScript', 'cgpa': 3.50}
}

print("Detailed Classroom Report:\n")

# Outer loop to get each student's name and their inner dictionary
for student_name, details in classroom.items():
    print(f"Student: {student_name.capitalize()}")
    
    # Inner loop to get individual keys and values inside the inner dictionary
    for key, value in details.items():
        print(f"  {key.capitalize()}: {value}")
    print("-" * 25)

Detailed Classroom Report:

Student: Abdullah
  Age: 30
  Course: Python Backend
  Cgpa: 3.63



for লুপ ও .items() দিয়ে কন্ডিশন চেক করা (Filtering Data)
ধরুন, আপনার কাছে একটি ডিকশনারিতে অনেক স্টুডেন্টের সিজিপিএ আছে। 
এখন  একটি for লুপ চালিয়ে শুধু তাদেরকেই ফিল্টার করতে চান যাদের সিজিপিএ ৩.৬০ এর বেশি।

student_cgpa = {
    'Abdullah': 3.63,
    'Rahim': 3.45,
    'Karim': 3.80,
    'Tanvir': 3.50,
    'Sabbir': 3.90
}

print("Students with CGPA 3.60 or higher:\n")

# Using a for loop with .items() to iterate through both key and value
for name, cgpa in student_cgpa.items():
    if cgpa >= 3.60:
        print(f"-> {name} has a great CGPA: {cgpa}")


Students with CGPA 3.60 or higher:

-> Abdullah has a great CGPA: 3.63
-> Karim has a great CGPA: 3.80
-> Sabbir has a great CGPA: 3.90



for লুপ দিয়ে ডিকশনারির ভ্যালুগুলোর যোগফল বা টোটাল বের করা (Accumulating Values)
ইকমার্স প্রজেক্টে কার্ট (Cart) বা শপিং ডিকশনারির সমস্ত পণ্যের মোট দাম (Total Price) বের করার জন্য এই প্যাটার্নটি সবচেয়ে বেশি ব্যবহার করা হয়।

# Cart items with their prices
cart_prices = {
    'shirt': 1200,
    'pant': 2200,
    'shoes': 3500,
    'cap': 400
}

total_bill = 0

# Iterating through values to calculate the total price
for price in cart_prices.values():
    total_bill += price

print("Individual Item Prices:")
for item, price in cart_prices.items():
    print(f"- {item}: {price} BDT")

print("----------------------------")
print(f"Total Bill to Pay: {total_bill} BDT")

Individual Item Prices:
- shirt: 1200 BDT
- pant: 2200 BDT
- shoes: 3500 BDT
- cap: 400 BDT
