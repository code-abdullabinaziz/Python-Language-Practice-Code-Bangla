ফাংশন (Function) হলো একটিনির্দিষ্ট কাজ করার জন্য লেখা পুনঃব্যবহারযোগ্য (Reusable) কোড ব্লক।

সোজা বাংলায়: একটি লজিক একবার লিখে একটি নাম দিয়ে সেভ করে রাখলে, 
আর প্রয়োজন অনুযায়ী কেবল নাম ধরে ডাকলে (Call করবেন)—বারবার একই কোড টাইপ করতে হবে না।

❓ ফাংশন কেন ব্যবহার করা হয়? (৩টি প্রধান কারণ)
১. কোড রি-ইউজেবিলিটি (Code Reusability)  

একই লজিক যদি প্রজেক্টের ১০টি জায়গায় দরকার হয়, তবে ১০ বার কোড লেখার প্রয়োজন নেই। 
একবার ফাংশন বানিয়ে ১০ জায়গায় ডাকলেই কাজ শেষ।

২. ড্রাই প্রিন্সিপাল (DRY - Don't Repeat Yourself)
প্রফেশনাল সফটওয়্যার ইঞ্জিনিয়ারিংয়ের মূল নিয়ম হলো "একই কোড বারবার লিখবে না"।
ফাংশন ব্যবহার করলে কোডের পুনরাবৃত্তি বন্ধ হয় এবং সাইজ ছোট থাকে।

৩. মডিউলারেটি ও মেইনটেইনেবিলিটি (Modularity & Easy Debugging)
বড় কোনো সিস্টেমে বাগ (Bug) বা সমস্যা দেখা দিলে পুরো হাজার লাইনের কোড খুঁজতে হয় না। 
শুধু নির্দিষ্ট কাজটির ফাংশনে গিয়ে ভুল ঠিক করলেই পুরো প্রজেক্টে তা আপডেট হয়ে যায়।


💻 রিয়েল-লাইফ তুলনা: ফাংশন ছাড়া vs ফাংশন সহ

ব্যাকএন্ডে ইউজারদের ট্যাক্স বা ভ্যাট (VAT) হিসাব করতে হবে (যেমন: ১৫% ভ্যাট)।

❌ ফাংশন ছাড়া (অনর্থক কোড রিপিটেশন):

# ইউজার ১-এর বিল
price1 = 1000
vat1 = price1 * 0.15
total1 = price1 + vat1
print(f"Total 1: {total1}")

# ইউজার ২-এর বিল (একই লজিক আবার লিখতে হচ্ছে)
price2 = 2500
vat2 = price2 * 0.15
total2 = price2 + vat2
print(f"Total 2: {total2}")


✅ ফাংশন সহ (প্রফেশনাল ও ক্লিন উপায়):

# ১. ফাংশন ডিফাইন করা (def = define)
def calculate_total_bill(price):
    vat = price * 0.15
    total = price + vat
    return total  # প্রসেস করা রেজাল্ট ব্যাক করা

# ২. ফাংশন কল করা (যে কয়বার ইচ্ছা মান পাঠাবো)
user1_total = calculate_total_bill(1000)
user2_total = calculate_total_bill(2500)

print(f"Total 1: {user1_total}")
print(f"Total 2: {user2_total}")


✅ পাইথনের আসল ফাংশন সিনট্যাক্স:


def function_name():
  print("Hello Function")

function_name()


def: এটি পাইথনের নির্দিষ্ট কীওয়ার্ড (Keyword)। পাইথন ইন্টারপ্রেটারকে জানান দেওয়ার জন্য যে—"আমি একটি ফাংশন ডিক্লেয়ার/তৈরি করতে যাচ্ছি।"

function_name: এটি ফাংশনের নাম। এটি আপনার ইচ্ছামতো যেকোনো নাম হতে পারে
(যেমন: check_status, calculate_vat, scan_ip)—তবে নামগুলো ছোট হাতের অক্ষরে 
এবং স্পেসের বদলে আন্ডারস্কোর _ (snake_case) দিয়ে লেখা ভালো অভ্যাস।

(): এটি ফার্স্ট ব্র্যাকেট/প্যারেন্থেসিস। ফাংশনের ভেতর যদি বাইরে থেকে কোনো ইনপুট (Parameters) পাঠাতে,
তবে তা এই ব্র্যাকেটের ভেতরে দিতে হয়। ইনপুট না থাকলে এটি খালি থাকবে।

: (কোলন): এটি অত্যন্ত গুরুত্বপূর্ণ! এই কোলন দিয়েই বোঝানো হয় যে 
ফাংশনের স্টেটমেন্ট শুরু হচ্ছে এবং এর পরের লাইন থেকে ইন্ডেন্টেশন (ফাঁকা জায়গা) দিয়ে Function Body লিখতে হবে।




# ১. ফাংশন ডিফাইন করা (Definition)
def greet_backend_engine():
    print("Hello Function - Welcome to Python Modular Design!")

# -------------------------------------------------------------
# ২. ফাংশন কল করা (Execution)
# ব্র্যাকেট দিয়ে নাম ধরে না ডাকলে ফাংশনের ভেতরের কোড রান হবে না

greet_backend_engine()


🔍 কেন greet_backend_engine() কল করতে হয়?

১. def greet_backend_engine(): — এটি হলো Definition। পাইথনকে শুধু ইনস্ট্রাকশন দিয়ে রাখলেন যে এই নামের একটি কাজ আছে।

২. greet_backend_engine() — এটি হলো Function Call। ফার্স্ট ব্র্যাকেট () দিয়ে যখন নামটা,

পাইথন সাথে সাথে ওই ফাংশনের ভেতরে ঢুকে সব লাইন এক্সিকিউট করা শুরু করবে।


# ১. ফাংশন ডেফিনিশন (Definition)
def greet_backend_engine():
    # ফাংশন বডি (Function Body)
    print("🚀 [SYSTEM LOG] Backend Engine Initialized Successfully!")

# -------------------------------------------------------------
# ২. ফাংশন কল (Function Call)
# এটি না লিখলে ওপরের প্রিন্টটি কখনো কনসোলে দেখাবে না
greet_backend_engine()




def greet():
  print("Hello Programmer!")

greet()
greet()
greet()



def  details():
    """
    This function prints the details of the application.
    """
    print("Application Name: MyApp")
    print("Version: 1.0.0")
    print("Author: Abdullah Aziz")
    print("Description: This is a sample application to demonstrate function usage.")
    
print("Welcome to MyApp!")
details()




def  details(name, age, country):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Country: {country}")
details("Abdullah", 30, "Bangladesh")


১. Function (ফাংশন) কোনটা?

পুরো কোড ব্লকটিই হলো একটি ফাংশন।

def details(name, age, country): থেকে শুরু করে ভেতরের ৩টি print() লাইনসহ পুরো সেটটিই হলো details নামক ফাংশন।

২. Parameter (প্যারামিটার) কোনটা?

ফাংশন তৈরি বা ডিফাইন করার সময় ব্র্যাকেটের ভেতরে যেসব কাল্পনিক বা ভ্যারিয়েবল নাম দেওয়া হয়, সেগুলোই হলো Parameter।

কোডে প্যারামিটার হলো ৩টি: name, age, এবং country

কাজ: এরা হলো খালি বক্সের মতো। ফাংশনের ভেতর এগুলো কী কাজে ব্যবহার হবে (যেমন প্রিন্ট করা), তা আগেই সাজিয়ে রাখা হয়।

৩. Argument (আর্গুমেন্ট) কোনটা?

ফাংশন ডাকার বা কল করার সময় ব্র্যাকেটের ভেতরে যে আসল বা অরিজিনাল ডাটাগুলো পাঠানো হয়, সেগুলোই হলো Argument।

কোডে আর্গুমেন্ট হলো ৩টি: "Abdullah", 30, এবং "Bangladesh"

কাজ: ব্র্যাকেটের ভেতরের এই অরিজিনাল মানগুলো গিয়ে প্যারামিটারের ওই খালি বক্সে বসে যায়

(যেমন: name = "Abdullah", age = 30, country = "Bangladesh")।


def  details(name, age, country):
    print(f"Name: {name}\nAge: {age}\nCountry: {country}")

details("Abdullah", 30, "Bangladesh")




def  my_intro():
  print("I am Abdullah")
  print("I am 30 years old")
  print("I live in Bangladesh")
  print("I am a software Engineer")
  
my_intro()



কোলনের (:) পর চারটা স্পেস বা ট্যাব দিয়ে ভেতরের অংশে যা কিছু লেখা হয়, সেটিকে একাধারে "Block" এবং "Function Body"—দুটিই বলা যায়!

তবে দুটি শব্দের মধ্যে সূক্ষ্ম একটি পার্থক্য আছে:

১. Function Body (ফাংশনের শরীর)

নির্দিষ্ট শব্দ: যখন কোনো কোড শুধুমাত্র def দিয়ে শুরু হওয়া ফাংশনের কোলনের (:) ভেতরে লেখা হয়, তখন সেই নির্দিষ্ট অংশকে বলা হয় Function Body।

২. Block / Code Block (কোড ব্লক)

সাধারণ শব্দ: পাইথনে কোলনের (:) ভেতরে ইন্ডেন্টেশন (চারটা স্পেস বা ট্যাব) দিয়ে যা-ই লেখা হয়, তাকেই Block বলা হয়।

এটি শুধু ফাংশন নয়—if-else, for loop, বা while loop-এর ক্ষেত্রেও প্রযোজ্য।


def check_status():
    # ---------------------------------------------------
    # এই অংশটি হলো 'Function Body' 
    # (কারণ এটি ডিরেক্ট ফাংশনের ভেতরে রয়েছে)
    # ---------------------------------------------------
    status = "Active"
    
    if status == "Active":
        # -----------------------------------------------
        # এই অংশটি হলো 'If Block' 
        # (এটি 'Function Body'-এর ভেতরে থাকা আরেকটি ব্লক)
        # -----------------------------------------------
        print("Server is running smoothly!")



💡 সংক্ষেপে মনে রাখার নিয়ম:

যেকোনো কোলন (:) এর ভেতরের ইন্ডেন্টেড অংশই হলো একেকটি Block।

আর সেই ব্লকটি যদি সরাসরি কোনো ফাংশনের (def) ভেতরে থাকে, তবে সেটিকে বলা হয় Function Body।




def  user_details():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")

    print("\nUser Details:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
    
user_details()



def  user_details():
    name = "Abdullah"
    age = 30
    email = "programmeraziz216@gmail.com"

    print("Name:", name)
    print("Age:", age)
    print("Email:", email)

user_details()
