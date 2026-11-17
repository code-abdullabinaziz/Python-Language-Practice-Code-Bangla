লজিক্যাল অপারেটর ব্যবহার করা হয় একাধিক শর্ত (condition) যুক্ত করতে এবং বুলিয়ান (True/False) ভ্যালু নিয়ে কাজ করতে।

এগুলো কন্ডিশনাল স্টেটমেন্ট (if-else) এবং লুপ-এ সবচেয়ে বেশি ব্যবহৃত হয়।

পাইথনে ৩টি লজিক্যাল অপারেটর আছে:



অপারেটর	                 কাজ

and (অ্যান্ড)                দুটি শর্তই সত্য হলে True

or (অর)                   যেকোনো একটি শর্ত সত্য হলে True

not (নট)                   শর্তকে উল্টে দেয় (True → False, False → True)


সবার আগে কাজ করে: not (এর প্রায়োরিটি বা শক্তি সবচেয়ে বেশি)

তারপরে কাজ করে: and (এর প্রায়োরিটি মাঝারি)

সবার শেষে কাজ করে: or (এর প্রায়োরিটি সবচেয়ে কম)





result = True or False and not True


ধাপ ১: সবার আগে not এর কাজ

এক্সপ্রেশনের শেষের দিকে রয়েছে not True।

আমরা জানি, not True-এর ফলাফল হলো False।

এবার কোডের অবশিষ্টাংশ দেখতে এমন দাঁড়াল:True or False and False

ধাপ ২: এরপর and এর কাজ

এখন নিয়ম অনুযায়ী and এর কাজ আগে হবে (অর্থাৎ মাঝখানের False and False হিসাব হবে)।

False and False-এর ফলাফল হলো False।

এবার কোডটি সংক্ষেপে ছোট হয়ে দাঁড়াল:True or False

ধাপ ৩: সবার শেষে or এর কাজ

এখন একদম শেষের কাজটি বাকি রইল: True or False।

or-এর নিয়ম অনুযায়ী যেকোনো একটি True হলেই পুরো ফলাফল True হয়ে যায়।

চূড়ান্ত মান হলো: True



#  and এর কাজ আগে হোক:
result = True or (False and not True)

#  or এর কাজ আগে হোক:
result = (True or False) and (not True)





x = 0
y = 10

result = (x != 0) and (y / x > 2) or (y == 10)
print("Result:", result)


১. প্রথম অংশ (and এর আগের ও মাঝের অংশ): (x != 0) and (y / x > 2)

প্রথমে দেখা যাক x != 0 এর মান কী? যেহেতু x = 0, তাই 0 != 0 হলো False।

এবার আসে পাইথনের Short-Circuit (অলস মূল্যায়ন) এর জাদু! and অপারেটরের নিয়ম হলো বাম দিকের শর্ত যদি False হয়ে যায়,

তবে সে আর ডান দিকের শর্ত চেকই করে না। যদি ডান দিক (y / x > 2 অর্থাৎ 10 / 0 > 2) চেক করতে যেত, 

তবে পাইথন জিরো দিয়ে ভাগের কারণে ZeroDivisionError দিয়ে ক্র্যাশ করত! কিন্তু শর্ট-সার্কিটের কারণে পাইথন ডান দিকে যাওয়ার আগেই থেমে গেল এবং প্রথম অংশের ফলাফল দিল False।



২. অবশিষ্টাংশ মূল্যায়ন:

এখন পুরো এক্সপ্রেশনটি ছোট হয়ে দাঁড়াল: False or (y == 10)

দ্বিতীয় অংশ (or এর ডানপাশ): y == 10 হিসাব করলে দাঁড়ায় 10 == 10, যার মান হলো True।



৩. চূড়ান্ত হিসাব:

False or True এর ফলাফল হলো True।

আউটপুট: Result: True (কোনো এরর ছাড়াই কোড রান করবে!)





x = 0
y = 10
result = (y / x > 2)


ধাপ ১: মান বসানো (Substitution)

y এর জায়গায় বসল 10

x এর জায়গায় বসল 0

ভেতরের অংশটি দাঁড়াল: (10 / 0 > 2)

ধাপ ২: ভাগের হিসাব করা (Division)

পাইথন প্রথমে ব্র্যাকেটের ভেতরের ভাগ কাজটি করতে যায়: 10 / 0

এখানেই বিপত্তি ঘটে! গণিতের নিয়মে কোনো সংখ্যাকে 0 দিয়ে ভাগ করা যায় না। তাই পাইথন এখানে এসেই ZeroDivisionError: division by zero এরর দিয়ে ক্র্যাশ করবে।








# ডাটাবেজে ইউজার পাওয়া যায়নি, তাই user = None
user = None 

# নিরাপদ চেক: প্রথমে দেখবে user আছে কি না, তারপর তার স্ট্যাটাস চেক করবে
# যদি user = None হয়, তবে পাইথন আর ডানের অংশে যাবে না, ফলে এরর বাঁচবে!
if user and user.get("is_active"):
    print("User is active and allowed.")
else:
    print("Access Denied: User not found or inactive.")












and অপারেটর (সবগুলো শর্ত সত্য হতে হবে)

উভয় পাশের শর্ত সত্য (True) হলেই কেবল পুরোটার উত্তর True হবে। যেকোনো একটা মিথ্যা হলে উত্তর False হয়ে যাবে।

and অপারেটরের মূল নিয়ম (The Core Rule)

সাধারণ গণিত বা লজিকে and-এর সহজ অর্থ হলো "এবং"।

দুটি বা ততধিক শর্তের সবকটি যদি সত্য (True) হয়, তবেই কেবল চূড়ান্ত ফলাফল সত্য (True) হবে।

একটি শর্তও যদি মিথ্যা (False) হয়ে যায়, তবে পুরো ফলাফল মুহূর্তেই মিথ্যা (False) হয়ে যাবে।



age = 25

has_nid = True

# এখানে উভয় শর্ত সত্য হতে হবে
is_eligible = (age >= 18) and (has_nid == True)
print(is_eligible)  # আউটপুট: True




# AND এর ট্রুথ টেবিল

print(True and True)   # True

print(True and False)  # False

print(False and True)  # False

print(False and False) # False


কোনো স্কলারশিপের জন্য বয়স ২০-এর কম হতে হবে এবং প্রাপ্ত নম্বর ৮০-এর বেশি হতে হবে।

age = 18
score = 85

# দুটো শর্ত একসাথে চেক করা হচ্ছে
can_get_scholarship = (age < 20) and (score > 80)

print("Scholarship Eligible Output:", can_get_scholarship)

Scholarship Eligible Output: True


মেলায় ঢুকতে হলে আপনার কাছে টিকিট থাকতে হবে এবং মাস্ক পরা থাকতে হবে।

has_ticket = True
has_mask = False

# দুটোই True না হলে ঢোকা যাবে না
can_enter = has_ticket and has_mask

print("Can Enter Output:", can_enter)

Can Enter Output: False


অফারে ফ্রি মিনিট চালু করার শর্ত: অ্যাকাউন্ট অ্যাক্টিভ থাকতে হবে এবং ব্যালেন্স ৫ টাকার বেশি হতে হবে।

is_active = True
balance = 10

# দুটোই সত্য হতে হবে
can_activate_offer = is_active and (balance > 5)

print("Offer Activation Status:", can_activate_offer)

Offer Activation Status: True



ফ্রি ডেলিভারি পাওয়ার শর্ত: অর্ডারের পরিমাণ ৫০০ টাকার বেশি হতে হবে এবং পেমেন্ট অনলাইনে করতে হবে।

order_amount = 600
payment_method = "Online"

# ৫০০ এর বেশি এবং পেমেন্ট অনলাইন হলে True হবে
free_delivery = (order_amount > 500) and (payment_method == "Online")

print("Free Delivery Output:", free_delivery)




# উদাহরণ: ব্যাংকে লোন পাওয়ার জন্য বয়স ১৮+ এবং ইনকাম ২০০০০+ হতে হবে
age = 25
income = 25000

eligible = (age > 18) and (income > 20000)
print("লোন পাবেন কি না? :", eligible)  # Output: True (কারণ দুটি শর্তই সত্য)



ড্রাইভিং লাইসেন্স পাওয়ার শর্ত: বয়স ১৮ বা তার বেশি হতে হবে এবং চোখের দৃষ্টি ভালো হতে হবে।

age = 20
has_good_eyesight = False

# একটা শর্ত পূর্ণ হলেও অন্যটা মিথ্যা (False)
is_eligible_for_license = (age >= 18) and has_good_eyesight

print("License Eligibility Output:", is_eligible_for_license)

Login Output: Welcome to your profile!





লগইন করার শর্ত: ইমেইল সঠিক হতে হবে এবং পাসওয়ার্ডও সঠিক হতে হবে।

correct_email = "user@gmail.com"
correct_pass = "12345"

entered_email = "user@gmail.com"
entered_pass = "12345"

# শুধু if দিয়ে লেখা
if (entered_email == correct_email) and (entered_pass == correct_pass):
    print("Login Output: Welcome to your profile!")




# and অপারেটর - দুটি শর্তই সত্য হতে হবে

age = 25
has_license = True

# দুটি শর্তই চেক
if age >= 18 and has_license:
    print("You can drive")  # ✅ এইটা প্রিন্ট হবে
else:
    print("You cannot drive")

# আউটপুট: You can drive



একাধিক শর্ত (চেইনিং):

# একাধিক and ব্যবহার
score = 85
attendance = 90
has_homework = True

if score >= 80 and attendance >= 75 and has_homework:
    print("Student passed with honors")  # ✅ প্রিন্ট হবে
else:
    print("Student needs improvement")



শর্ট-সার্কিট ইভ্যালুয়েশন (Short-Circuit):

# and-এ প্রথম শর্ত যদি False হয়, বাকি শর্ত চেক করা হয় না

def check_first():
    print("Checking first condition")
    return False

def check_second():
    print("Checking second condition")
    return True

# দ্বিতীয় ফাংশন কল হবে না কারণ প্রথমটি False
result = check_first() and check_second()
print(result)  # False

# আউটপুট:
# Checking first condition
# False




রিয়েল-ওয়ার্ল্ড উদাহরণ:

# ইউজার লগইন ভ্যালিডেশন
username = "admin"
password = "secret123"
is_active = True

if username == "admin" and password == "secret123" and is_active:
    print("Login successful!")  # ✅
else:
    print("Invalid credentials")

# ই-কমার্স: অর্ডার প্লেস করা যাবে কিনা
product_price = 500
user_balance = 1000
stock_available = 10
user_is_verified = True

if user_balance >= product_price and stock_available > 0 and user_is_verified:
    print("Order placed successfully!")
    user_balance -= product_price
    stock_available -= 1
else:
    print("Cannot place order. Check balance, stock, or verification.")









or অপারেটর (OR)

or অপারেটরের দুই পাশের শর্তগুলোর মধ্যে যেকোনো একটি সত্য (True) হলেই চূড়ান্ত ফলাফল True হয়। 

দুটি শর্তই মিথ্যা হলে কেবল তখনই ফলাফল False হয়।

# OR এর ট্রুথ টেবিল
print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False



# vacancies: জব পাওয়ার জন্য সিএসই ডিগ্রি অথবা ৩ বছরের অভিজ্ঞতা দরকার
has_cse_degree = False
has_experience = True

got_job = has_cse_degree or has_experience
print("জব পাবেন কি না? :", got_job)  # Output: True (কারণ অভিজ্ঞতা আছে, ১টি শর্ত মিলেছে)



বাসে হাফ ভাড়া দেওয়া যাবে যদি আপনি ছাত্র হন অথবা আপনার বয়স ৬০-এর বেশি হয়।

is_student = True
age = 25

# যেকোনো একটি সত্য হলেই True
gets_discount = is_student or (age > 60)

print("Gets Bus Discount:", gets_discount)        Gets Bus Discount: True
(ব্যাখ্যা: বয়স ৬০-এর বেশি না হলেও তিনি একজন ছাত্র, তাই ১টি শর্ত মিলে যাওয়ায় উত্তর এসেছে True)




কেনাকাটার জন্য ক্যাশ টাকা অথবা বিকাশ অ্যাকাউন্ট যেকোনো একটা থাকলেই চলবে।

has_cash = False
has_bkash = True

can_pay = has_cash or has_bkash

print("Can Pay Money:", can_pay)   Can Pay Money: True



আজ ছুটির দিন হবে যদি আজ শুক্রবার হয় অথবা আজ সরকারি ছুটি থাকে।

is_friday = False
is_govt_holiday = False

is_day_off = is_friday or is_govt_holiday

print("Is Today a Holiday:", is_day_off)  Is Today a Holiday: False   

(ব্যাখ্যা: দুটো শর্তের একটিও সত্য নয়, তাই or-এর চূড়ান্ত আউটপুট এসেছে False)



খেলাটি টিভিতে সরাসরি সম্প্রচার করা হচ্ছে অথবা ইউটিউবে লাইভ স্ট্রিম হচ্ছে—যেকোনো একটি মাধ্যম চালু থাকলেই খেলা দেখতে পারবেন।

has_tv = False
has_youtube_live = True

can_watch_game = has_tv or has_youtube_live

print("Can Watch Game:", can_watch_game)  Can Watch Game: True



খাবারের বিলে ছাড় পাবেন যদি কাছে কুপন কোড থাকে অথবা মেম্বারশিপ কার্ড থাকে।

has_coupon = True
has_membership_card = False

gets_discount = has_coupon or has_membership_card

print("Discount Status:", gets_discount)  Discount Status: True



অফিসের দরজা খুলবে যদি আইডি কার্ড পাঞ্চ করেন অথবা ফিঙ্গারপ্রিন্ট সেন্সরে আঙুল দেন।

has_id_card = False
has_fingerprint = False

door_opens = has_id_card or has_fingerprint

print("Door Opens Output:", door_opens) Door Opens Output: False
(ব্যাখ্যা: কার্ডও নেই, ফিঙ্গারপ্রিন্টও ম্যাচ করেনি—দুটোই False হওয়ায় দরজা খুলবে না)



আপনি জামাটি কিনবেন যদি জামাটির রঙ নীল (blue) হয় অথবা কালো (black) হয়।

shirt_color = "blue"

# রঙ নীল হলেও সত্য, কালো হলেও সত্য
is_my_choice = (shirt_color == "blue") or (shirt_color == "black")

if is_my_choice:
    print("Shopping Status: I will buy this shirt!")       Shopping Status: I will buy this shirt!



# or অপারেটর - যেকোনো একটি শর্ত সত্য হলেই হবে

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's weekend!")  # ✅
else:
    print("It's a weekday")

# আউটপুট: It's weekend!



একাধিক শর্ত:

# একাধিক or ব্যবহার
user_role = "editor"

if user_role == "admin" or user_role == "editor" or user_role == "moderator":
    print("User has write access")  # ✅
else:
    print("User has read-only access")



শর্ট-সার্কিট ইভ্যালুয়েশন (OR):

# or-এ প্রথম শর্ত যদি True হয়, বাকি শর্ত চেক করা হয় না

def expensive_operation():
    print("Running expensive operation...")
    return True

def quick_check():
    print("Quick check")
    return True

# প্রথমটি True, তাই expensive_operation() কল হবে না
result = quick_check() or expensive_operation()
print(result)  # True

# আউটপুট:
# Quick check
# True



রিয়েল-ওয়ার্ল্ড উদাহরণ:

# ডিসকাউন্ট চেক - বিভিন্ন শর্তে ডিসকাউন্ট পাওয়া যাবে
is_member = True
has_coupon = False
is_first_order = True
total_amount = 1500

# ডিসকাউন্টের শর্ত: মেম্বার অথবা কুপন অথবা প্রথম অর্ডার
if is_member or has_coupon or is_first_order:
    print("You get a discount!")  # ✅
else:
    print("No discount available")

# ফোন নম্বর ভ্যালিডেশন
phone = "01712345678"
email = "user@example.com"

if phone or email:
    print("Contact info exists")  # ✅
    
# ডিফল্ট ভ্যালু সেট করা
user_input = ""
default_value = "Guest"

# user_input খালি হলে ডিফল্ট ব্যবহার
name = user_input or default_value
print(name)  # Guest











not অপারেটর (NOT)

এটি একটি ইউনারি অপারেটর  এর কাজ হলো সত্যকে মিথ্যা এবং মিথ্যাকে সত্য বানানো।

# NOT এর ট্রুথ টেবিল
print(not True)   # False
print(not False)  # True



is_raining = False
print("বাইরে যাব কি না? :", not is_raining)  # Output: True (বৃষ্টি হচ্ছে না, তাই যাব)



ধরে নিই বৃষ্টি হচ্ছে না (is_raining = False)। কিন্তু সামনে not বসালে তা সত্য হয়ে যাবে।

is_raining = False

# not ব্যবহারের কারণে False হয়ে যাবে True
go_outside = not is_raining

print("Can Go Outside:", go_outside) Can Go Outside: True



গেমে প্লেয়ারের অবস্থা হলো is_dead = True (প্লেয়ার মারা গেছে)।

is_dead = True

# not এর কারণে True হয়ে যাবে False
is_alive = not is_dead

print("Is Player Alive:", is_alive)  Is Player Alive: False



ইউজার পাসওয়ার্ড ফাঁকা রেখে দিলে সিস্টেম চেক করে পাসওয়ার্ড আছে কি না।

is_password_entered = False

# পাসওয়ার্ড দেওয়া না হলে not দিয়ে শর্তটি সত্য করা হলো
if not is_password_entered:
    print("Warning: Please enter your password!") Warning: Please enter your password!



সুইচ বর্তমানে অন রয়েছে (is_switched_on = True)। সুইচে চাপ দিলে তা বন্ধ হবে।

is_switched_on = True

# সুইচে চাপ দিলে উল্টে যাবে
current_state = not is_switched_on

print("Current Switch State (On = True, Off = False):", current_state)   Current Switch State (On = True, Off = False): False



হোটেলের দরজায় যদি "Do Not Disturb" ঝুলানো না থাকে (False), তবেই বেডরুম ক্লিনার ভেতরে ঢুকতে পারবে।

is_do_not_disturb = False

# not ব্যবহারের কারণে False হয়ে যাবে True
can_clean_room = not is_do_not_disturb

print("Can Clean Room:", can_clean_room)       Can Clean Room: True



ফোনে ওয়াইফাই কানেক্টেড আছে (is_wifi_connected = True)। কিন্তু ইন্টারনেট কাজ করছে না কি না চেক করতে not ব্যবহার করা যায়:

is_wifi_connected = True

# not এর কারণে True হয়ে যাবে False
is_offline = not is_wifi_connected

print("Is Offline Status:", is_offline)        Is Offline Status: False



ইউজার একটি ভুল ইমেইল অ্যাড্রেস দিলে তা চেক করার নিয়ম:

is_email_valid = False

# ইমেইল যদি সঠিক না হয় (not True)
if not is_email_valid:
    print("Email Output: Please provide a valid email address!")     Email Output: Please provide a valid email address!




একটি ভ্যারিয়েবল ফাঁকা বা খালি কি না তা চেক করতে not খুব জনপ্রিয়:

user_name = ""  # খালি স্ট্রিং পাইথনে কিন্তু False হিসেবে কাজ করে

# empty value-র সামনে not দিলে তা True হয়ে যায়
if not user_name:
    print("Form Status: Username cannot be empty!")    Form Status: Username cannot be empty!
 




# not অপারেটর - বুলিয়ান ভ্যালু উল্টে দেয়

is_raining = True

if not is_raining:
    print("Let's go outside!")  # ❌ এইটা প্রিন্ট হবে না
else:
    print("Stay inside, it's raining!")  # ✅

# আউটপুট: Stay inside, it's raining!



বিভিন্ন ডেটা টাইপের সাথে NOT:

# পাইথনে False হিসেবে বিবেচিত হয়:
# - False (বুলিয়ান)
# - 0, 0.0 (সংখ্যা)
# - "" (খালি স্ট্রিং)
# - [] (খালি লিস্ট)
# - {} (খালি ডিকশনারি)
# - () (খালি টাপল)
# - None

print(not False)   # True
print(not 0)       # True
print(not "")      # True
print(not [])      # True
print(not {})      # True
print(not None)    # True

# True হিসেবে বিবেচিত হয় বাকি সব
print(not 5)       # False
print(not "Hello") # False
print(not [1, 2])  # False



রিয়েল-ওয়ার্ল্ড উদাহরণ:

# ইউজার লগআউট চেক
is_logged_in = True

if not is_logged_in:
    print("Please login first")
else:
    print("Welcome back, user!")  # ✅

# ফাইল খালি কিনা চেক
file_content = ""

if not file_content:
    print("File is empty")  # ✅
else:
    print("File has content")

# খালি লিস্ট চেক
cart = []

if not cart:
    print("Your cart is empty. Add items!")  # ✅
else:
    print(f"You have {len(cart)} items in cart")

# পারমিশন চেক
has_admin_access = False

if not has_admin_access:
    print("Access denied. Admin rights required.")  # ✅
else:
    print("Welcome to admin panel")




কম্বাইনড অপারেটর (Combining Operators)
AND + OR একসাথে:

# একাধিক লজিক্যাল অপারেটর একসাথে

age = 25
has_id = True
is_student = False
is_weekend = True

# জটিল শর্ত
if (age >= 18 and has_id) or (is_student and is_weekend):
    print("Eligible for discount")  # ✅
else:
    print("Not eligible")

# ব্যাখ্যা: 
# (age >= 18 and has_id) = True
# (is_student and is_weekend) = False
# True or False = True



NOT + AND/OR একসাথে:

# not ব্যবহার করে শর্ত উল্টানো

is_logged_in = True
has_permission = False
is_admin = True

# অ্যাডমিন নয় কিন্তু লগইন করা এবং পারমিশন আছে
if not is_admin and is_logged_in and has_permission:
    print("Access granted")
else:
    print("Access denied")  # ✅ (কারণ has_permission False)

# যদি শর্ত পুরোপুরি উল্টাতে চান
is_blocked = False

if not is_blocked:
    print("User is active")  # ✅


অগ্রাধিকার (Precedence) - কোনটা আগে কাজ করে?

# অগ্রাধিকার ক্রম: not > and > or

# ১. not (সর্বোচ্চ অগ্রাধিকার)
# ২. and
# ৩. or (সর্বনিম্ন অগ্রাধিকার)

x = True
y = False
z = True

# পাইথন এভাবে দেখে: not x or y and z
# (not x) or (y and z)
# not x = False
# y and z = False and True = False
# False or False = False
result = not x or y and z
print(result)  # False

# কিন্তু ব্র্যাকেট ব্যবহার করলে পরিষ্কার হয়
result = (not x) or (y and z)
print(result)  # False

# ব্র্যাকেট পরিবর্তন করলে ফলাফল বদলায়
result = not (x or y) and z
# (x or y) = True
# not True = False
# False and True = False
print(result)  # False




Advanced------------

এলইপি (LBYL) vs এএফপি (EAFP)

LBYL (Look Before You Leap) - চেক করে তারপর কাজ:

# LBYL স্টাইল - শর্ত চেক করে তারপর অপারেশন

user_input = "abc123"

# চেক করছে সংখ্যা কিনা
if user_input.isdigit():
    number = int(user_input)
    print(f"Number: {number}")
else:
    print("Invalid number")

# ফাইল আছে কিনা চেক
import os

if os.path.exists("data.txt"):
    with open("data.txt", "r") as f:
        content = f.read()
else:
    print("File not found")





EAFP (Easier to Ask for Forgiveness than Permission) - পরে এরর হ্যান্ডেল:

# EAFP স্টাইল - চেষ্টা করে দেখ, না হলে এরর হ্যান্ডেল

user_input = "abc123"

try:
    number = int(user_input)
    print(f"Number: {number}")
except ValueError:
    print("Invalid number")

# ফাইল পড়ার চেষ্টা
try:
    with open("data.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")



লজিক্যাল অপারেটরের অ্যাডভান্সড ব্যবহার

বুলিয়ান ইন্টিজার হিসেবে ব্যবহার:

# True = 1, False = 0

x = True
y = False

print(x + y)        # 1 + 0 = 1
print(x * 5)        # 1 * 5 = 5
print(x - y)        # 1 - 0 = 1

# অ্যাডভান্সড: কাউন্টার হিসেবে
tasks = [True, False, True, True, False]
completed = sum(1 for task in tasks if task)  # True গুলো কাউন্ট
print(f"Completed: {completed} out of {len(tasks)}")  # Completed: 3 out of 5

# অথবা সরাসরি
completed = sum(tasks)  # True = 1, False = 0
print(f"Completed: {completed}")  # Completed: 3



এলিস (or) দিয়ে ডিফল্ট ভ্যালু:

# ডিফল্ট ভ্যালু সেট করা

def get_username(user_data):
    # user_data['username'] থাকলে সেটা নেবে, না হলে ডিফল্ট
    return user_data.get('username') or "Anonymous"

# টেস্ট
user1 = {'username': 'john_doe'}
user2 = {}

print(get_username(user1))  # john_doe
print(get_username(user2))  # Anonymous

# আরেকটি উপায়
name = input("Enter name: ") or "Guest"
print(f"Hello, {name}!")  # ইনপুট না দিলে Guest




আন্ড (and) দিয়ে চেকিং:

# and দিয়ে শর্ত চেক

def validate_age(age):
    # age থাকলে এবং 18 এর বেশি হলে True
    return age and age >= 18

print(validate_age(25))   # True
print(validate_age(15))   # False
print(validate_age(None)) # None (কারণ age False)

# প্রোডাক্ট চেক
def get_product_price(product):
    # product থাকলে এবং stock থাকলে প্রাইস রিটার্ন
    if product and product.get('stock', 0) > 0:
        return product.get('price')
    return 0

product1 = {'name': 'Laptop', 'price': 50000, 'stock': 10}
product2 = {'name': 'Mouse', 'price': 500, 'stock': 0}
product3 = None

print(get_product_price(product1))  # 50000
print(get_product_price(product2))  # 0
print(get_product_price(product3))  # 0


অল (all()) এবং যেকোনো (any()) ফাংশন:

# all() - সবগুলো শর্ত সত্য কিনা

numbers = [10, 20, 30, 40]

# সবগুলো ৫ এর বেশি?
print(all(num > 5 for num in numbers))  # True

# সবগুলো ২৫ এর বেশি?
print(all(num > 25 for num in numbers))  # False

# ইউজার ভ্যালিডেশন
user = {
    'name': 'John',
    'email': 'john@example.com',
    'age': 30
}

required_fields = ['name', 'email', 'age']

# সব ফিল্ড আছে কিনা
if all(field in user for field in required_fields):
    print("User data complete")  # ✅
else:
    print("Missing required fields")

# any() - কোনো একটি শর্ত সত্য কিনা

numbers = [1, 3, 5, 7, 9]

# কোনো জোড় সংখ্যা আছে?
print(any(num % 2 == 0 for num in numbers))  # False

# কোনো ৫ এর বেশি সংখ্যা আছে?
print(any(num > 5 for num in numbers))  # True

# ফাইল চেক
files = ['data.txt', 'config.json', 'log.txt']

# কোনো JSON ফাইল আছে?
if any(file.endswith('.json') for file in files):
    print("JSON file found")  # ✅



লিস্ট কম্প্রিহেনশনে ব্যবহার:

# ফিল্টারিং

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# জোড় এবং ৫ এর বেশি
filtered = [x for x in numbers if x % 2 == 0 and x > 5]
print(filtered)  # [6, 8, 10]

# অথবা ৩ বা ৫ দিয়ে বিভাজ্য
filtered = [x for x in range(1, 21) if x % 3 == 0 or x % 5 == 0]
print(filtered)  # [3, 5, 6, 9, 10, 12, 15, 18, 20]

# not ব্যবহার
numbers = [0, 1, 2, 3, 4, 5]
non_zero = [x for x in numbers if not x == 0]
print(non_zero)  # [1, 2, 3, 4, 5]


লজিক্যাল অপারেটরের ব্যাকএন্ড ব্যবহার ----------------জানা লাগবে
