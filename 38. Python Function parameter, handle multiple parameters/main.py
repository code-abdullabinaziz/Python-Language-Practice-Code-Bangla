Python-এ def কিওয়ার্ড ব্যবহার করে ফাংশন (Function) তৈরি করা হয় এবং ফাংশন ব্র্যাকেটের () ভেতরের ইনপুট ভ্যালুগুলোকে প্যারামিটার (Parameter) বলা হয়।

🔍 Parameter বনাম Argument (পার্থক্য)

Parameter (প্যারামিটার): ফাংশন ডিফাইন (তৈরি) করার সময় ব্র্যাকেটের ভেতর যে ভ্যারিয়েবলের নাম লেখা হয় (যেমন: def greet(name):)।

Argument (আর্গুমেন্ট): ফাংশন কল করার সময় ব্র্যাকেটের ভেতর যে আসল ভ্যালু পাঠানো হয় (যেমন: greet("Abdullah"))।



📌 Python-এ Parameter এর ৫টি প্রধান প্রকারভেদ:--


১. Positional Parameters (সাধারণ বা পজিশনাল)

যেভাবে ক্রমানুসারে (Order) প্যারামিটার লেখা হয়, আর্গুমেন্টও ঠিক সেই ক্রমানুসারে পাস করতে হয়।

def student_info(name, age):
    print(f"Name: {name}, Age: {age}")

# সঠিক পজিশন অনুযায়ী মান পাঠানো
student_info("Abdullah", 30) 
# Output: Name: Abdullah, Age: 30



২. Default Parameters (ডিফল্ট মান)

ফাংশন ডিক্লেয়ার করার সময়ই কোনো প্যারামিটারের একটি ডিফল্ট ভ্যালু সেট করে দেওয়া যায়।
ফাংশন কল করার সময় যদি সেই আর্গুমেন্ট না পাঠানো হয়, তবে ডিফল্ট মানটি ব্যবহার হবে।

def greet(name, country="Bangladesh"):
    print(f"Hello {name} from {country}")

greet("Abdullah")                     # Output: Hello Abdullah from Bangladesh
greet("Rakib", "Japan")               # Output: Hello Rakib from Japan

⚠️ নিয়ম: ডিফল্ট প্যারামিটার সবসময় পজিশনাল প্যারামিটারের পরে (ডানে) রাখতে হয়। 
(যেমন: def func(a, b=10): সঠিক, কিন্তু def func(a=10, b): সিনট্যাক্স এরর দেবে)।



৩. Keyword Arguments (নাম ধরে মান পাঠানো)
ফাংশন কল করার সময় প্যারামিটারের নাম উল্লেখ করে মান পাঠানো যায়। এতে ক্রমানুসার (Order) বজায় রাখার প্রয়োজন পড়ে না।

def introduce(first_name, last_name):
    print(f"Full Name: {first_name} {last_name}")

introduce(last_name="Hassan", first_name="Abdullah")
# Output: Full Name: Abdullah Hassan


৪. Arbitrary Positional Arguments (*args)
যদি  আগে থেকে না জানেন ইউজার মোট কতগুলো আর্গুমেন্ট পাঠাবে, 
তবে প্যারামিটারের আগে একটি স্টার (*) ব্যবহার করতে হয়। Python এটিকে ব্যাকগ্রাউন্ডে একটি Tuple হিসেবে রিসিভ করে।


def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(10, 20, 30))       # Output: 60
print(sum_all(5, 15))            # Output: 50


৫. Arbitrary Keyword Arguments (**kwargs)
যদি আনলিমিটেড Key-Value Pair (নাম সহ ভ্যালু) পাঠাতে চান, তবে ডাবল স্টার (**) ব্যবহার করতে হয়। 
Python এটিকে ব্যাকগ্রাউন্ডে একটি Dictionary হিসেবে রিসিভ করে।

def user_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

user_details(Name="Abdullah", Role="Developer", City="Dhaka")
# Output:
# Name: Abdullah
# Role: Developer
# City: Dhaka





def add_number(num1, num2):  # num1, num2 হলো Parameter
    print(num1 + num2)
  
add_number(5, 10)            # 5, 10 হলো Argument


🔍 পার্থক্য ও ব্যাখ্যা:

num1 এবং num2 হলো Parameter (প্যারামিটার):

কারণ: যখন  def add_number(num1, num2): লিখে ফাংশনটি তৈরি/ডিক্লেয়ার করা হয়েছে, 

তখন ব্র্যাকেটের ভেতরের ভ্যারিয়েবল দুটিকে Parameter বলে। এগুলো মূলত বাইরের ভ্যালু গ্রহণ করার জন্য খালি পাত্র হিসেবে কাজ করে।

5 এবং 10 হলো Argument (আর্গুমেন্ট):

কারণ: যখন add_number(5, 10) লিখে ফাংশনটিকে কল বা এক্সিকিউট করা হয়,
তখন ব্র্যাকেটের ভেতর যে বাস্তব মান (Actual Values) পাঠানো হসছে, সেগুলোকে Argument বলে।

🧠 মেমোরিতে কীভাবে মান অ্যাসাইন হয় (Execution Flow):
কোড রান হলে num1 = 5 এবং num2 = 10 হিসেবে অ্যাসাইন হবে।

আউটপুট আসবে: 15




def disply_profile(name, cgpa):
  print(f"Student Name: {name}\nAcademic CGPA: {cgpa}")
  
disply_profile("Abdullah_Aziz", 3.63)
disply_profile("Mohammad Arman", 4.76)




def print_name(first_name, middle_name, last_name):
  print(f'{first_name} {middle_name} {last_name}')

print_name("Mohammad", "Abdullah", "Aziz")

print_name("Arman") # Output Error Why

ফাংশনটি তৈরি করার সময় ৩টি বাধ্যতামূলক Positional Parameter (first_name, middle_name, last_name) ডিফাইন করা হয়েছে,
কিন্তু দ্বিতীয়বার কল করার সময় মাত্র ১টি Argument ("Arman") পাঠানো হয়েছে। পাইথন ২টি আর্গুমেন্ট না পেয়ে TypeError দেবে। 

🔍 পাইথন কম্পাইলার / ইন্টারপ্রেটার কীভাবে এরর দিচ্ছে:

TypeError: print_name() missing 2 required positional arguments: 'middle_name' and 'last_name'

পাইথনের নিয়ম হলো—যে কয়টি পজিশনাল প্যারামিটার থাকবে, কোনো ডিফল্ট ভ্যালু সেট করা না থাকলে ঠিক সে কয়টি আর্গুমেন্টই কল করার সময় পাঠাতে হবে।



🛠️ সমাধান: ২টি উপায়ে এটি ঠিক করা যায়ঃ

১. Default Parameters ব্যবহার করে (যাতে ১টি বা ২টি আর্গুমেন্ট দিলেও কাজ করে):

যদি কারও middle_name বা last_name না থাকে, তবে প্যারামিটারে খালি স্ট্রিং "" বা None ডিফল্ট হিসেবে সেট করে রাখা যায়।

# ডিফল্ট ভ্যালু সেট করা হলো
def print_name(first_name, middle_name="", last_name=""):
    print(f'{first_name} {middle_name} {last_name}'.strip())

# ১. ৩টি আর্গুমেন্ট দিয়ে কল
print_name("Mohammad", "Abdullah", "Aziz")
# Output: Mohammad Abdullah Aziz

# ২. ১টি আর্গুমেন্ট দিয়ে কল (এখন আর এরর আসবে না)
print_name("Arman")
# Output: Arman




২. Arbitrary Arguments (*args) ব্যবহার করে (আনলিমিটেড নামের জন্য):

যদি জানা না থাকে ইউজার ১টি, ২টি নাকি ৩টি নাম পাঠাবে, তবে *args ব্যবহার করা সেরা উপায়।

def print_name(*names):
    # *names ব্যাকগ্রাউন্ডে একটি Tuple তৈরি করে
    print(" ".join(names))

print_name("Mohammad", "Abdullah", "Aziz") # Output: Mohammad Abdullah Aziz
print_name("Arman")                        # Output: Arman
print_name("MD", "Arman", "Hossain", "Khan") # Output: MD Arman Hossain Khan





name1 = "Arman"
name2 = "Ebny"
name3 = "Aziz"


def print_name(first_name, middle_name, last_name):
  print(f'{first_name} {middle_name} {last_name}')


print_name("Mohammad", "Abdullah", "Aziz")

print_name(name1, name2, name3)


🧠 ব্যাকগ্রাউন্ডে স্কোপ ও মেমোরি কীভাবে কাজ করছে?

১. গ্লোবাল স্কোপ (Global Scope):

ফাংশনের বাইরে থাকা name1, name2, এবং name3 হলো Global Variables। এগুলো প্রোগ্রামের যেকোনো জায়গা থেকে অ্যাক্সেস করা যায়।

২. লোকাল স্কোপ (Local Scope):

ফাংশনের ভেতরের first_name, middle_name, এবং last_name হলো Local Variables / Parameters।

৩. ম্যাপিং প্রসেস (How parameters get values):

যখন print_name(name1, name2, name3) লিখা হ্য, তখন পাইথন ব্যাকগ্রাউন্ডে ভ্যারিয়েবলগুলোর মান এভাবে পাস করে:

first_name = name1  --"Arman"
middle_name = name2 --"Ebny"
last_name = name3 ---"Aziz"




name1 = "Arman"
name2 = "Ebny"
name3 = "Aziz"

def print_name(first_name, middle_name, last_name):
  print(f'{first_name} {middle_name} {last_name}')


print_name("Mohammad", "Abdullah", "Aziz")

print_name(name1, name2, name3)

print(name1)

print(name2)

print(name3)


"মেমোরির রেফারেন্স পয়েন্ট করে আর ফাংশনের ভেতর লোকাল ভ্যারিয়েবল হিসেবে রিসিভ হয়"—এটির মেমোরি মেকানিজম পাইথনে খুব চমৎকারভাবে কাজ করে।

🧠 ব্যাকগ্রাউন্ড মেমোরিতে আসলে কী ঘটে?

পাইথনে কোনো ভ্যারিয়েবল নিজেই আসল তথ্য ধারণ করে না, বরং ভ্যারিয়েবল হলো RAM-এর মেমোরি অ্যাড্রেসের একটি লেবেল বা নাম (Pointer/Reference)।

১. গ্লোবাল লেভেলে (Global Scope):

যখন লিখা হয় :

name1 = "Arman"

তখন RAM মেমোরির একটি নির্দিষ্ট জায়গায় (যেমন: 0x101 অ্যাড্রেসে) "Arman" স্ট্রিংটি জমা হয়। 
আর name1 ভ্যারিয়েবলটি সেই 0x101 মেমোরি অ্যাড্রেসকে নির্দেশ (Point) করে থাকে।

২. ফাংশন কল করার মুহূর্তে (Pass by Object Reference):

যখন লিখা হয়:

print_name(name1, name2, name3)

তখন পাইথন name1-এর ভেতরের টেক্সট "Arman" কপি করে আলাদা করে পাঠায় না। 
বরং পাইথন name1 যে মেমোরি লোকেশনকে (0x101) পয়েন্ট করছিল, সেই মেমোরি লোকেশনের রেফারেন্স বা লিঙ্কটি ফাংশনের কাছে পাঠিয়ে দেয়।


৩. ফাংশনের ভেতরে (Local Scope):
ফাংশনের ভেতরে থাকা প্যারামিটারগুলো (first_name, middle_name, last_name) হলো Local Variables।

ফাংশনটি রান হওয়া মাত্রই:

লোকাল ভ্যারিয়েবল first_name তৈরি হয়।

এটি গ্লোবাল name1-এর পাঠানো সেই মেমোরি লোকেশনকেই (0x101) পয়েন্ট করা শুরু করে।


[ Global Scope ]                           [ RAM Memory ]                           [ Local Scope ]
    name1   -------------------------->  0x101 ("Arman")  <------------------------   first_name
    name2   -------------------------->  0x102 ("Ebny")   <------------------------   middle_name
    name3   -------------------------->  0x103 ("Aziz")   <------------------------   last_name

💡 তাহলে কেন একে লোকাল ভ্যারিয়েবল বলছি?
১. জীবনকাল (Scope Lifetime):

first_name, middle_name, এবং last_name নামগুলো শুধুমাত্র ফাংশনের ভেতরের দুনিয়াতেই পরিচিত। 
ফাংশনের প্রিন্ট শেষ হওয়া মাত্রই এই ৩টি লোকাল লেবেল বা নাম মেমোরি থেকে মুছে যায়। ফাংশনের বাইরে এসে print(first_name) লিখলে পাইথন NameError দেবে।

২. গ্লোবাল ভ্যারিয়েবল সুরক্ষিত থাকে:

গ্লোবালের name1, name2, name3 কিন্তু মেমোরিতে তাদের জায়গায় বহাল তবিয়তে রয়ে যায়।

📊 সংক্ষেপে সহজ সারসংক্ষেপ:

name1 (Global): স্থায়ী ঠিকানা, ফাংশনের বাইরে থাকে।

first_name (Local): সাময়িক ঠিকানা, যা গ্লোবালের মেমোরি লোকেশন নির্দেশ করে কাজ শেষ করেই মেমোরি থেকে গায়েব হয়ে যায়।




def total(sum1, sum2):
  print(sum1 + sum2)
  
total(2)

total ফাংশনটি তৈরি করার সময় ২টি বাধ্যতামূলক Positional Parameter (sum1 এবং sum2) ডিফাইন করা হয়েছে, 
কিন্তু ফাংশনটি কল করার সময় মাত্র ১টি Argument (2) পাঠানো হয়েছে।

পাইথন ২টি আর্গুমেন্ট না পেয়ে TypeError দেবে।

TypeError: total() missing 1 required positional argument: 'sum2'

🛠️ এরর ছাড়া এটি সমাধান করার ২টি উপায়:
১. কল করার সময় ২টি আর্গুমেন্টই দিয়ে দেয়া:

def total(sum1, sum2):
    print(sum1 + sum2)

total(2, 5)  # Output: 7 (sum1=2, sum2=5)


২. Default Parameter ব্যবহার করা (যদি ১টি আর্গুমেন্ট দিলে অপরটি ০ ধরতে চান):
প্যারামিটারে ডিফল্ট ভ্যালু সেট করে রাখলে কল করার সময় আর্গুমেন্ট না পাঠালেও কোনো এরর আসবে না।

# sum2 এর ডিফল্ট মান 0 সেট করে রাখা হলো
def total(sum1, sum2=0):
    print(sum1 + sum2)

total(2)     # Output: 2 (কারণ sum1=2 এবং sum2=0)
total(2, 5)  # Output: 7 (কারণ sum2-এর ডিফল্ট মান ওভাররাইড হয়ে 5 হয়েছে)




১টি প্যারামিটার দিয়ে ফাংশন তৈরি করে কীভাবে ইউজারের কাছ থেকে input() নিয়ে তা প্রসেস করতে হয়,

# ১. ১টি প্যারামিটার (number) বিশিষ্ট ফাংশন ডিফাইন
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is an Even number.")
    else:
        print(f"{number} is an Odd number.")


# ২. ইউজারের কাছ থেকে ইনপুট নেওয়া
user_input = int(input("Enter a number: "))

# ৩. ইনপুট নেওয়া মানটি আর্গুমেন্ট হিসেবে ফাংশনে পাস করা
check_even_odd(user_input)


🧠 মেমোরি ও এক্সিকিউশন ফ্লো (Execution Flow):
১. input() প্রসেস: ইউজার কিবোর্ড থেকে যে সংখ্যাই টাইপ করবেন (ধরুন 7), int(input()) তা পূর্ণসংখ্যায় রূপান্তর করে user_input নামক গ্লোবাল ভ্যারিয়েবলে সংরক্ষণ করে।

২. প্যারামিটার পাসিং: check_even_odd(user_input) কল করার সময় user_input-এর মানটি (7) ফাংশনের লোকাল প্যারামিটার number-এ চলে যায়।

৩. আউটপুট: ফাংশনটি হিসাব করে স্ক্রিনে দেখাবে:

7 হলো বিজোড় সংখ্যা (Odd Number)।




def check_user(name, status = "Active"):
  print(f"User: {name}\nStatus: {status}")
  
check_user("Abdullah")
check_user("Aziz", "inactive")

User: Abdullah
Status: Active
User: Aziz
Status: inactive



name1 = "Mohammad"
name2 = "Aziz"

def my_name(first_name, last_name):
  last_name = "Rokshana"
  print(f"{first_name} {last_name}")
  
my_name("Abdullah", "Arman")

my_name(name1, name2)




def number(num):
  num = num * 2
  print(num)
  
add = 5

number(add)

print(add)




def number(num):
    num = num * 2
    return num

add = number(5)      # add = 10
add = number(add)    # add-এর নতুন মান হলো 20 (কারণ return-এর মান আপডেট করা হয়েছে)

print(add)           # Output: 20



def number(num):
    return num * 2

add = number(5)       # add = 10

print(number(add))    # সরাসরি প্রিন্টের ভেতর number(10) পাস করা হলো -> Output: 20





# ১. ফাংশন ডিক্লেয়ারেশন (যেখানে নাম ইনপুট নেওয়া হবে)
def get_user_name():
    name = input("Enter your full name: ")
    return name


# ২. ফাংশনটি কল করে রিটার্ন হওয়া নাম একটি ভ্যারিয়েবলে (user_name) স্টোর করা হলো
user_name = get_user_name()

# ৩. আউটপুট প্রিন্ট করা
print(f"Hello, {user_name}! Welcome to Python programming.")



# ১. ফাংশন ডিফাইন (JS-এর function-এর জায়গায় def)
def details(first_name, last_name):
    print(f"User Name: {first_name} {last_name}")


# ২. ইউজারের কাছ থেকে ইনপুট নেওয়া (JS-এর prompt()-এর জায়গায় input())
user_first = input("Enter First Name: ")
user_last = input("Enter Last Name: ")

# ৩. ফাংশন কল করা
details(user_first, user_last)



পাইথনে সিকিউরিটি চেক, return স্টেটমেন্ট এবং ইউজার ইনপুট হ্যান্ডেল করার পাইথন কোড

# ১. ফাংশন ডেফিনিশন (প্যারামিটার: username, password)
def register_user(username, password):
    # পাসওয়ার্ড সিকিউরিটি চেক (len() দিয়ে স্ট্রিংয়ের দৈর্ঘ্য মাপা হয়)
    if len(password) < 8:
        return f"Error: Hi {username}, password must be at least 8 characters long!"
    else:
        return f"Success: Account created successfully for {username}!"


# ২. ইউজার থেকে ইনপুট নেওয়া
input_user = input("Enter your desired Username: ")
input_pass = input("Enter your Password: ")

# ৩. ইনপুট দুটো আর্গুমেন্ট হিসেবে ফাংশনে পাঠিয়ে রেজাল্ট ভ্যারিয়েবলে রাখা
status_message = register_user(input_user, input_pass)

# ৪. আউটপুট দেখানো
print(status_message)



পাসওয়ার্ড ৮ অক্ষরের কম দিলে (< 8):

Enter your desired Username: Arman
Enter your Password: 123
Error: Hi Arman, password must be at least 8 characters long!

পাসওয়ার্ড ৮ অক্ষর বা তার বেশি দিলে (>= 8):

Enter your desired Username: Arman
Enter your Password: mysecretpass123
Success: Account created successfully for Arman!
