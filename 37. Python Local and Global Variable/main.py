পাইথনে def হলো একটি কি-ওয়ার্ড (Keyword), যার ফুল মিনিং বা পূর্ণরূপ হলো Definition (ডেফিনিশন)।
সহজ কথায়, পাইথনে কোনো ফাংশন তৈরি বা ডিফাইন (Define) করার জন্য এই def কি-ওয়ার্ড ব্যবহার করা হয়।
এটি পাইথন কম্পাইলার বা ইন্টারপ্রেটারকে নির্দেশ দেয় যে এখান থেকে একটি নতুন ফাংশন শুরু হচ্ছে।

পায়থনের LEGB Rule, global keyword, nonlocal keyword এবং মেমোরি মেকানিজমের প্রতিটি দিক উদাহরণসহ:



১. LEGB Rule (পায়থনের স্কোপ খোঁজার সিকোয়েন্স)
পায়থন যখনই কোনো ভ্যারিয়েবল খুঁজে বের করতে চায়, তখন সে একটি নির্দিষ্ট ৪-ধাপের সিকোয়েন্স বা অর্ডার মেনে চলে, যাকে বলা হয় LEGB Rule:

[L]ocal ───► [E]nclosing ───► [G]lobal ───► [B]uilt-in

1. Local (L): ফাংশনের ঠিক ভেতরে ডিক্লেয়ার করা ভ্যারিয়েবল।

2. Enclosing (E): নেস্টেড ফাংশন (Nested/Inner Function)-এর ক্ষেত্রে বাইরের ফাংশনের স্কোপ।

3. Global (G): পায়থন ফাইলের মেইন বা টপ-লেভেলে তৈরি করা ভ্যারিয়েবল।

4. Built-in (B): পায়থনের নিজস্ব বিল্ট-ইন কিওয়ার্ড বা ফাংশন (যেমন: print, len, range)।


----বাকি জটিল নিয়মগুলো (LEGB, nonlocal বা Globals()) যখন বাস্তবে বড় কোনো প্রজেক্ট বা সিকিউরিটি লজিক বানানো হবে, 
তখন প্রয়োজন অনুযায়ী প্র্যাকটিক্যালি দেখে নেওয়া যাবে।-----------------


Local Variable: ফাংশনের ভেতরের ভ্যারিয়েবল—ফাংশন শেষ হলেই মেমোরি থেকে ক্লিয়ার (ডিলিট) হয়ে যায়।

Global Variable: ফাইলের একদম বাইরে তৈরি করা ভ্যারিয়েবল—প্রোগ্রাম বন্ধ না হওয়া পর্যন্ত মেমোরিতে থেকে যায়।

Python Specific Rule: ফাংশনের ভেতর থেকে গ্লোবাল মান পরিবর্তন করতে গেলে global কথাটি লিখতে হয়।




২. Local Variable (লোকাল ভ্যারিয়েবল):

Local Variable হলো এমন variable যেটা একটা Function এর ভিতরে তৈরি করা হয়, 
আর এটা শুধু সেই Function এর ভিতরেই ব্যবহার করা যায় — Function শেষ হয়ে গেলে এই variable আর থাকে না

সীমানা (Scope): এটি শুধুমাত্র ওই ফাংশনের ভেতরেই এক্সেস করা যায়।

লাইফটাইম (Memory Lifetime): ফাংশনটি যখন কল হয়, তখন এটি মেমোরিতে জায়গা পায় (Local Execution Frame) 
এবং ফাংশন শেষ হওয়া মাত্রই মেমোরি থেকে Garbage Collected (মুছে) হয়ে যায়।

def my_function():
    x = 10  # Local Variable
    print(f"Inside function: {x}")

my_function()

# ফাংশনের বাইরে থেকে এক্সেস করার চেষ্টা:
print(x)  # ❌ NameError: name 'x' is not defined


def greet():
    message = "Hello"   # এটা Local variable, শুধু greet() এর ভিতরেই আছে
    print(message)

greet()   # Output: Hello

print(message)   # এখানে এটা access করা যাবে না

....
Local Variable এর Scope (কতক্ষণ পর্যন্ত বাঁচে)

def calculate():
    result = 10 * 5   # Local variable
    print("Inside function:", result)

calculate()
calculate()   # দ্বিতীয়বার কল করলে result আবার নতুন করে তৈরি হয়


ব্যাখ্যা: প্রতিবার Function কল হলে, তার Local variable গুলো নতুন করে তৈরি হয়, 
আর Function শেষ হয়ে গেলে সেগুলো মুছে যায় (destroy হয়)। এক কলের Local variable আরেক কলে প্রভাব ফেলে না।




৩. Global Variable (গ্লোবাল ভ্যারিয়েবল):

Global Variable হলো এমন variable যেটা Function এর বাইরে তৈরি করা হয়, আর এটা পুরো প্রোগ্রামের যেকোনো জায়গা থেকে ব্যবহার করা যায়।

সীমানা (Scope): ফাইল বা প্রোগ্রামের যেকোনো জায়গা থেকে এটি পড়া (Read করা) যায়।

লাইফটাইম (Memory Lifetime): পুরো পায়থনScript বা প্রোগ্রাম চালানো শেষ না হওয়া পর্যন্ত এটি মেমোরিতে থাকে।

y = 50  # Global Variable

def read_global():
    print(f"Inside function: {y}")  # গ্লোবাল ভ্যারিয়েবল পড়তে পারছে

read_global()
print(f"Outside function: {y}")


name = "Abdullah"   # এটা Global variable, Function এর বাইরে তৈরি হয়েছে

def greet():
    print(f"Hello, {name}")   # Function এর ভিতর থেকেও এটা পড়া যাচ্ছে

greet()
print(name)   # Function এর বাইরেও এটা কাজ করছে




একই নাম — Local আর Global দুইটা আলাদা জিনিস

x = 10   # Global variable

def my_function():
    x = 5   # এটা একটা নতুন Local variable, Global x কে স্পর্শ করছে না
    print("Inside function, x =", x)

my_function()
print("Outside function, x =", x)

Inside function, x = 5
Outside function, x = 10



কেন Local Variable ভালো Practice

# খারাপ অভ্যাস - সব কিছু Global
total = 0

def add_item(price):
    global total
    total += price

add_item(100)
add_item(200)
print(total)



# ভালো অভ্যাস - Local variable আর return ব্যবহার করা
def calculate_total(prices):
    total = 0   # Local variable, এখানেই সীমাবদ্ধ
    for price in prices:
        total += price
    return total

result = calculate_total([100, 200])
print(result)

কেন দ্বিতীয়টা ভালো: Global variable বেশি ব্যবহার করলে বড় প্রোগ্রামে bug খুঁজে বের করা কঠিন হয়ে যায়, কারণ যেকোনো Function থেকে সেটা পরিবর্তন হতে পারে।
Local variable + return ব্যবহার করলে প্রতিটা Function স্বাধীন (independent) থাকে, আর কোড বোঝা ও maintain করা সহজ হয়।
এটাই FastAPI/backend কোডেও standard practice।

সংক্ষেপে: Local Variable Function এর ভিতরে তৈরি হয় এবং শুধু সেখানেই থাকে, Function শেষ হলে মুছে যায়। 
Global Variable Function এর বাইরে তৈরি হয় এবং পুরো প্রোগ্রামে ব্যবহার করা যায় — তবে Function এর ভিতর থেকে 
এটা পরিবর্তন করতে হলে global keyword ব্যবহার করতে হয়। সাধারণত বড় প্রোগ্রামে Local variable আর return ব্যবহার করাই ভালো practice, 
কারণ এতে কোড পরিষ্কার ও bug-মুক্ত রাখা সহজ হয়।




৪. global Keyword (ফাংশনের ভেতর থেকে গ্লোবাল মান পরিবর্তন)

পায়থনে গ্লোবাল ভ্যারিয়েবল ফাংশনের ভেতর থেকে পড়া (Read) গেলেও,
সরাসরি পরিবর্তন বা Re-assign করা যায় না। ফাংশনের ভেতর গ্লোবাল ভ্যারিয়েবলের মান পরিবর্তন করতে চাইলে global কিওয়ার্ড ব্যবহার করতে হয়।

❌ ভুল ধারণা / UnboundLocalError:

count = 0  # Global Variable

def increment():
    count = count + 1  # ❌ UnboundLocalError!
    # কারণ পায়থন ধরে নেয় count একটি Local Variable, কিন্তু ডানপাশে ব্যবহারের সময় তার কোনো মান নেই।

increment()


✅ সঠিক উপায় (global কিওয়ার্ড দিয়ে):

count = 0  # Global Variable

def increment():
    global count  # পায়থনকে বলে দেওয়া হলো: "আমি গ্লোবাল count কেই মডিফাই করব"
    count = count + 1

increment()
print(count)  # Output: 1 (গ্লোবাল মান পরিবর্তন হয়েছে)




count = 0   # Global variable

def increase():
    count = count + 1   # এটা error দেবে!
    print(count)

increase()  UnboundLocalError: local variable 'count' referenced before assignment

ব্যাখ্যা: পাইথন যখন দেখে Function এর ভিতরে count = ... লেখা আছে (assignment),
তখন এটা ধরে নেয় count একটা নতুন Local variable হবে। কিন্তু count + 1 করতে গিয়ে প্রথমে পুরনো count এর মান পড়তে চায়,
যেটা তখনও তৈরিই হয়নি (Local হিসেবে) — তাই error আসে।


global Keyword দিয়ে সমাধান

সত্যিই Function এর ভিতর থেকে Global variable পরিবর্তন করতে হয়, তাহলে global keyword ব্যবহার করতে হবে।


count = 0   # Global variable

def increase():
    global count   # বলে দিচ্ছি, এটা Global count, নতুন Local না
    count = count + 1
    print(count)

increase()
increase()
print("Final count:", count)

1
2
Final count: 2


একাধিক Function এর সাথে Global Variable

balance = 1000   # Global variable

def deposit(amount):
    global balance
    balance += amount
    print("After deposit:", balance)

def withdraw(amount):
    global balance
    balance -= amount
    print("After withdraw:", balance)

deposit(500)
withdraw(300)
print("Final balance:", balance)

After deposit: 1500
After withdraw: 1200
Final balance: 1200

ব্যাখ্যা: দুইটা আলাদা Function (deposit, withdraw) একই Global variable balance কে পরিবর্তন করছে, আর সেই পরিবর্তন সবখানে প্রভাব ফেলছে।


একটা গুরুত্বপূর্ণ নিয়ম — শুধু পড়তে (read) চাইলে global লাগে না

price = 100   # Global variable

def show_price():
    print("Price is:", price)   # শুধু পড়া হচ্ছে, global লাগবে না

show_price()  Price is: 100


global keyword শুধু তখনই লাগে যখন Function এর ভিতর থেকে Global variable এর মান পরিবর্তন (assign/modify) করতে চাইলে। শুধু পড়তে চাইলে এটা দরকার নেই।





৫. Enclosing Scope এবং nonlocal Keyword:

ফাংশনের ভেতরে যখন আরেকটা ফাংশন থাকে (Nested Function), তখন বাইরের ফাংশনটিকে বলা হয় Enclosing Scope।

ভেতরের (Inner) ফাংশন থেকে বাইরের (Outer) ফাংশনের ভ্যারিয়েবলকে পরিবর্তন করতে চাইলে nonlocal কিওয়ার্ড ব্যবহার করা হয়।

def outer_function():
    message = "Hello from Outer"  # Enclosing Scope Variable

    def inner_function():
        nonlocal message  # Enclosing Scope-এর ভ্যারিয়েবল পরিবর্তনের অনুমতি নিচ্ছে
        message = "Modified by Inner"

    inner_function()
    print(message)  # Output: Modified by Inner

outer_function()






৬. Python Scope-এর কিছু ব্যতিক্রম ও টেকনিক্যাল সত্য 

১. if-else বা for লুপের কোনো Scope নেই!

জাভাস্ক্রিপ্ট বা C/C++ এ if-else বা for লুপের নিজস্ব Block Scope থাকে, কিন্তু পায়থনে if, for, while, try-except কোনো আলাদা স্কোপ তৈরি করে না!

if True:
    z = 99  # এটি কিন্তু Global Variable!

print(z)  # Output: 99 (পায়থনে লুপ বা শর্তের ব্লক ভেঙে বাইরে চলে আসে)


নোট: পায়থনে কেবল function, class, এবং module নিজস্ব স্কোপ তৈরি করে।


২. Mutable Object-এর ক্ষেত্রে global কিওয়ার্ড লাগে না!

যদি গ্লোবাল ভ্যারিয়েবলটি একটি List, Dictionary বা Set (Mutable Type) হয়, তবে তার ভেতর মান যুক্ত করতে (Mutate করতে) global কিওয়ার্ড লাগে না!

my_list = [1, 2, 3]  # Global List

def add_element():
    my_list.append(4)  # ✅ global কিওয়ার্ড ছাড়াই পরিবর্তন হবে!

add_element()
print(my_list)  # Output: [1, 2, 3, 4]


৩. globals() এবং locals() Built-in Functions
পায়থনের ২টি বিল্ট-ইন ফাংশন দিয়ে বর্তমান মেমোরিতে থাকা সব লোকাল ও গ্লোবাল ভ্যারিয়েবলের ডিকশনারি ভার্সন চেক করা যায়:

a = 100

def check_memory():
    b = 200
    print(locals())   # Output: {'b': 200}
    print(globals()['a'])  # Output: 100

check_memory()



Local Example:

def  user_details():
  name = "Abdullah"
  age = 30
  height = 5.223
  print(f"{'Name:':<10} {name}")
  print(f"{'Age:':<10} {age}")
  print(f"{'Height:':10} {height:.1f}")
  
user_details()



Global Example:

def  user_details():
  name = "Abdullah"
  age = 30
  height = 5.223
  print(f"{'Name:':<10} {name}")
  print(f"{'Age:':<10} {age}")
  print(f"{'Height:':<10} {height:.1f}")
  print(f"{'Subject:':<10} {subject}")
  print(f"{'Village:':<10} {village}")
  
user_details()

print(f"{subject}")

print(f"{village}")
  





# এটি Global Variable (ফাংশনের বাইরে তৈরি করা হয়েছে)
x = 10 


def my_function():
    # এটি Local Variable (ফাংশনের ভেতরে তৈরি করা হয়েছে)
    y = 5 
    print("Local Variable y =", y)
    print("Global Variable x (Inside Function) =", x)


# ফাংশন কল করা
my_function()

# ফাংশনের বাইরে Global Variable ব্যবহার
print("Global Variable x (Outside Function) =", x)

# নিচের লাইনটি ভুল হবে (Error আসবে), কারণ y একটি Local Variable
# print(y)




ফাংশনের ভেতর থেকে কোনো Global Variable-এর মান পরিবর্তন করতে চাইলে global কিওয়ার্ড ব্যবহার করতে হয়:

count = 0  # Global Variable


def increment():
    global count  # পাইথনকে বলে দেওয়া হচ্ছে আমরা বাইরের count ব্যবহার করব
    count = count + 1


increment()
print("Updated Global Count =", count)  # আউটপুট: 1




ফাংশনের মান গণনা ও রিটার্ন (Return Pattern)
ব্যাকএন্ড ডেভেলপমেন্টে গ্লোবাল ভেরিয়েবল সরাসরি পরিবর্তন না করে, 
লোকাল ভেরিয়েবল প্রসেস করে return করা সবচেয়ে ভালো ও নিরাপদ প্র্যাকটিস।


tax_rate = 0.15  # Global Variable (কমন কনফিগারেশন)

def calculate_total(price):
    # local_tax এবং total_price দুটিই Local Variable
    local_tax = price * tax_rate
    total_price = price + local_tax
    return total_price  # লজিক প্রসেস করে লোকাল রেজাল্ট বাইরে পাঠানো হলো

# ব্যবহারের নিয়ম
final_bill = calculate_total(100)
print("Total Bill:", final_bill)  # Output: 115.0



কাউন্টার ও স্ট্যাটাস আপডেট (global কিওয়ার্ড)
সিস্টেম লগইন সংখ্যা গণনা বা সার্ভার স্ট্যাটাস ট্র্যাক করার কাজে গ্লোবাল ভেরিয়েবল আপডেট করতে হয়।

total_logins = 0  # Global Variable

def user_login_event(username):
    global total_logins  # গ্লোবাল ভেরিয়েবল পরিবর্তনের অনুমতি নেওয়া হলো
    total_logins += 1    # মূল ভেরিয়েবলের সাথে ১ যোগ করা হলো
    
    # local_msg একটি Local Variable
    local_msg = f"User '{username}' logged in successfully."
    print(local_msg)

# একাধিক ইউজার লগইন করলে
user_login_event("rahim")
user_login_event("karim")

print("Total Successful Logins:", total_logins)  # Output: 2



কনফিগারেশন পরিবর্তন (সিস্টেম সেটিং)
প্রজেক্টের সেটিংস যেমন—ওয়েবসাইট ব্যাকগ্রাউন্ড মোড বা ডিফোল্ট ল্যাঙ্গুয়েজ পরিবর্তন করতে এই প্যাটার্ন লাগে।

app_theme = "LIGHT"  # Global Variable (ডিফোল্ট সেটিং)

def enable_dark_mode():
    global app_theme
    app_theme = "DARK"  # গ্লোবাল থিম পরিবর্তন করা হলো
    
    status = f"App theme is now updated to {app_theme} mode."  # Local Variable
    print(status)

# অ্যাপ্লিকেশন নাইট মোডে নেওয়া
enable_dark_mode()
print("Current Active Theme:", app_theme)  # Output: DARK


Local Variable: যে ভেরিয়েবল শুধু নির্দিষ্ট ফাংশনের ভেতরের কাজের জন্য তৈরি হয়। ফাংশনের কাজ শেষ হলে এটি মেমোরি থেকে মুছে যায়।

Global Variable: পুরো স্ক্রিপ্টে বা একাধিক ফাংশনে যে ভেরিয়েবলের মান কমন থাকে। ফাংশনের ভেতর থেকে পরিবর্তন করতে হলে global কিওয়ার্ড ব্যবহার করতে হয়।



ভেরিয়েবল শ্যাডোইং (Variable Shadowing)
যদি কোনো লোকাল ভেরিয়েবলের নাম গ্লোবাল ভেরিয়েবলের নামের মতো একই হয়, তবে পাইথন ফাংশনের ভেতরে লোকাল ভেরিয়েবলটিকে প্রাধান্য দেয়
(গ্লোবাল ভেরিয়েবলকে ঢেকে বা "shadow" করে ফেলে)।

# Global Variable
status = "Offline"


def check_server():
    # এখানে লোকাল ভেরিয়েবল তৈরি করা হলো, যার নাম গ্লোবালের মতোই
    status = "Online"
    print("Inside function (Local):", status)  # আউটপুট: Online


check_server()
print("Outside function (Global):", status)  # আউটপুট: Offline



একাধিক ফাংশন থেকে একটি গ্লোবাল ভেরিয়েবল শেয়ার করা
ব্যাকএন্ডে অনেক সময় পুরো অ্যাপ্লিকেশনের জন্য একটি কমন কনফিগারেশন বা ডেটা থাকে, যা বিভিন্ন ফাংশন প্রয়োজনমতো রিড করে।

# Global Variable (পুরো ফাইলের জন্য কমন ডেটা)
current_user_role = "Guest"


def login_as_admin():
    global current_user_role
    current_user_role = "Admin"
    print("Role updated to:", current_user_role)


def check_permission():
    # এটি গ্লোবাল ভেরিয়েবলের বর্তমান মান চেক করবে
    if current_user_role == "Admin":
        print("Access Granted: Welcome Admin!")
    else:
        print("Access Denied: You are a Guest.")


# ফাংশনগুলো রান করে দেখা যাক
check_permission()  # আউটপুট: Access Denied (কারণ তখন role Guest ছিল)

login_as_admin()  # role পরিবর্তন করে Admin করা হলো
check_permission()  # আউটপুট: Access Granted (এখন অনুমোদন পাবে)



গ্লোবাল ভেরিয়েবল সরাসরি পরিবর্তন না করে আর্গুমেন্ট হিসেবে পাস করা (Best Practice)
প্রফেশনাল প্রোগ্রামিংয়ে গ্লোবাল ভেরিয়েবলের মান ফাংশনের ভেতর সরাসরি global দিয়ে পরিবর্তন 
করাকে সবসময় ভালো প্র্যাকটিস হিসেবে ধরা হয় না (এতে কোডে বাগ বা সমস্যা তৈরি হতে পারে)। এর বদলে মান পাস করে দেওয়া নিরাপদ।


# Global Variable
api_version = "v1"


def get_api_endpoint(version, endpoint_name):
    # এখানে গ্লোবাল ভেরিয়েবল সরাসরি না নিয়ে আর্গুমেন্ট হিসেবে ফাংশনে পাঠানো হয়েছে
    return f"https://api.example.com/{version}/{endpoint_name}"


# গ্লোবাল ভেরিয়েবলটি আর্গুমেন্ট হিসেবে পাস করা হলো
url = get_api_endpoint(api_version, "users")
print("Generated URL:", url)  # আউটপুট: https://api.example.com/v1/users


বড় বড় ব্যাকএন্ড প্রজেক্টে বা FastAPI-তে কোড লেখার সময় চেষ্টা করা হয় গ্লোবাল ভেরিয়েবলের ওপর নির্ভরতা কমিয়ে
ফাংশনের প্যারামিটার বা আর্গুমেন্টের মাধ্যমে ডেটা পাস করতে। এতে কোড অনেক বেশি পরিষ্কার এবং নিরাপদ থাকে।

