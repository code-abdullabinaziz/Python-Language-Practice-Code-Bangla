ভেরিয়েবল:

ভেরিয়েবল হলো একটি নামযুক্ত বাক্স যেখানে ডেটা বা তথ্য সংরক্ষণ করা হয়।
Python variable মানে হলো এমন একটি নামযুক্ত জায়গা, যেখানে কোনো মান রাখা হয় এবং পরে সেই মান ব্যবহার করা যায়। সহজভাবে বললে, variable হলো ডেটা রাখার কন্টেইনারের মতো।


Variable কেন লাগে: 

প্রোগ্রামে ডেটা সংরক্ষণ করতে।

বারবার একই মান লিখতে না হয়ে নাম দিয়ে ব্যবহার করতে।

মান বদলালে সহজে আপডেট করতে।


ভেরিয়েবল তৈরি করা
পাইথনে ভেরিয়েবল ডিক্লেয়ার করার জন্য কোনো কমান্ড নেই। Python-এ ভ্যারিয়েবল ঘোষণা করার সময় আলাদা করে টাইপ লিখতে হয় না। সরাসরি মান দিয়ে দিলেই Python বুঝে নেয়।

ভেরিয়েবলকে কোনো নির্দিষ্ট টাইপ দিয়ে ডিক্লেয়ার করার প্রয়োজন নেই, এবং সেট করার পরেও সেগুলোর টাইপ পরিবর্তন করা যেতে পারে। 
Python-এ ভেরিয়েবল তৈরি করা খুবই সহজ। অন্যান্য অনেক প্রোগ্রামিং ভাষার মতো এখানে ডেটা টাইপ (যেমন: int, string) আগে থেকে ঘোষণা করতে হয় না। 
যখনই কোনো ভেরিয়েবলে মান অ্যাসাইন (Assign) করা হয় , সেটি স্বয়ংক্রিয়ভাবে তৈরি হয়ে যাবে। এর জন্য = (assignment operator) ব্যবহার করা হয়। 

name = "Abdullah"       # এখানে name একটি ভেরিয়েবল, যা টেক্সট (String) ধরে রেখেছে
age = 29                # এখানে age একটি ভেরিয়েবল, যা পূর্ণসংখ্যা (Integer) ধরে রেখেছে
gpa = 3.85              # এখানে gpa একটি ভেরিয়েবল, যা দশমিক সংখ্যা (Float) ধরে রেখেছে

# ভেরিয়েবলগুলো প্রিন্ট 
print(name)
print(age)
print(gpa)




name = "Abdullah"
age = 30
height = 5.2

print("My name is " + name + " and I am " + str(age) + " years old. My height is " + str(height) + " feet.")
print(f"My name is {name} and I am {age} years old. My height is {height} feet.")

২ নম্বর print স্টেটমেন্টে (যাকে বলা হয় f-string) আলাদা করে str() করা লাগেনা, কারণ পাইথন ব্যাকগ্রাউন্ডে নিজের দায়িত্বেই ওই ভেরিয়েবলগুলোকে স্ট্রিং বা টেক্সটে রূপান্তর করে নেয়। 
f-string-এর ভেতরের কার্লি ব্রেসেস {}-এর কাজই এটি।


print(f'''My name is {name} 
and I am {age} years old. 
My height is {height} feet.''')

print(f"""My name is {name} 
and I am {age} years old. 
My height is {height} feet.""")


 ভিতরে Single Quote থাকলে Double ব্যবহার 

text = "He said, 'Python is awesome!'"
print(f'{text}')  # এখানে Double ভালো



ভিতরে Double Quote থাকলে Single ব্যবহার 

text = 'She told me, "Learn Python!"'
print(f'{text}')  # এখানে Single 



মাল্টিলাইন টেক্সট (যেমন ইমেইল বা লম্বা মেসেজ)

message = f'''Dear {name},
Your age is {age} and height is {height} feet.
Thank you!'''
print(message)


f-string-এর ভিতরে f-string (নেস্টেড)

person = "Abdullah"
print(f'My name is {f"Mr. {person}"}')  # ভিতরে Double, বাইরে Single



f-string-এর ভিতরে একই ধরনের Quote ব্যবহার করা যাবে না

# ❌ ভুল (ভিতরে-বাইরে একই Quote)
print(f'My name is {name} and I'm {age}')  # Syntax Error!

# ✅ ঠিক (ভিতরে Single, বাইরে Double)
print(f"My name is {name} and I'm {age}")


f-string-এ Escape Character (\) ব্যবহার 

print(f'My name is {name}. I\'m {age} years old.')  # \' দিয়ে Single এস্কেপ




name = "Abdullah"
age = 30
height = 5.2

print("Name:", name)
print("Age:", age)
print("Height:", height)

print("Name:" + name)
print("Age:" + str(age))
print("Height:" + str(height))





ভেরিয়েবলের নাম:

একটি ভেরিয়েবলের সংক্ষিপ্ত নাম (যেমন x এবং y) অথবা আরও বর্ণনামূলক নাম (age, carname, total_volume) থাকতে পারে।


পাইথন ভেরিয়েবলের নিয়মাবলী:

একটি ভেরিয়েবলের নাম অবশ্যই একটি অক্ষর বা আন্ডারস্কোর (underscore) অক্ষর দিয়ে শুরু হতে হবে।
একটি ভেরিয়েবলের নাম কোনো সংখ্যা দিয়ে শুরু হতে পারে না।
একটি ভেরিয়েবলের নামে শুধুমাত্র আলফানিউমেরিক অক্ষর এবং আন্ডারস্কোর (A-z, 0-9, এবং _) থাকতে পারে।
ভেরিয়েবলের নাম কেস-সেনসিটিভ (case-sensitive) হয় (age, Age এবং AGE তিনটি ভিন্ন ভেরিয়েবল)।  Name আর name দুটো আলাদা ভেরিয়েবল! সঠিক: my_var = 10, _var = 5 ভুল: 1st_number = 10

একটি ভেরিয়েবলের নাম পাইথনের কোনো কীওয়ার্ড হতে পারে না। রিজার্ভড কিওয়ার্ড (Reserved Keywords): Python-এর নিজস্ব কিছু সংরক্ষিত শব্দ আছে 
(যেমন: if, else, print, while, for)। এগুলোকে ভেরিয়েবলের নাম হিসেবে ব্যবহার করা যাবে না।


Legal variable names:

myvar = "Abdullah"
my_var = "Abdullah"
_my_var = "Abdullah"
myVar = "Abdullah"
MYVAR = "Abdullah"
myvar2 = "Abdullah"



Illegal variable names:

2myvar = "Abdullah"
my-var = "Abdullah"
my var = "Abdullah"

my_name = "Abdullah"    # ✅ সঠিক
myName = "Abdullah"     # ✅ সঠিক (camelCase)
_name = "Abdullah"      # ✅ সঠিক
2name = "Abdullah"     # ❌ ভুল — সংখ্যা দিয়ে শুরু করা যাবে না
my-name = "Abdullah"  # ❌ ভুল — হাইফেন ব্যবহার করা যাবে না
class = "Abdullah"      # ❌ ভুল — reserved keyword ব্যবহার করা যাবে না



ডাইনামিক টাইপিং (Dynamic Typing)
Python একটি ডাইনামিকালি টাইপড ভাষা। এর মানে হলো,  একটি ভেরিয়েবলে প্রথমে এক ধরণের ডেটা রাখার পর পরবর্তীতে একই ভেরিয়েবলে অন্য ধরণের ডেটা রাখা যায়। 
Python নিজে থেকেই তার টাইপ বদলে নেয়।

x = 10          # x এখন একটি Integer (পূর্ণসংখ্যা)
print(x)

x = "Hello"     # x-এর ভেতরে এবার String (টেক্সট) রাখা হলো 
print(x)



একাধিক শব্দের ভেরিয়েবলের নাম
একাধিক শব্দযুক্ত ভেরিয়েবলের নাম পড়া কঠিন হতে পারে।
এগুলোকে আরও সহজে পঠনযোগ্য করার জন্য কয়েকটি কৌশল ব্যবহার করা যাবে:

ক্যামেল কেস (Camel Case)
প্রথম শব্দটি ছাড়া প্রতিটি শব্দ বড় হাতের অক্ষর দিয়ে শুরু হয়:
myVariableName = "Abdullah"

প্যাসকেল কেস (Pascal Case)
প্রতিটি শব্দ বড় হাতের অক্ষর দিয়ে শুরু হয়:
MyVariableName = "Abdullah"

স্নেক কেস (Snake Case)
প্রতিটি শব্দ একটি আন্ডারস্কোর (underscore) অক্ষর দ্বারা আলাদা করা হয়:
my_variable_name = "Abdullah"


পাইথনে ভেরিয়েবলের নাম লেখার জন্য সবচেয়ে প্রফেশনাল এবং সবচেয়ে বেশি ব্যবহৃত কেস হলো স্নেক কেস (Snake Case)।

পাইথনে অফিসিয়াল কোডিং স্ট্যান্ডার্ড বা নিয়মকানুন যেখানে লেখা আছে, তাকে বলা হয় PEP 8 (Python Enhancement Proposal 8)। 
এই PEP 8-এর নিয়ম অনুযায়ী পাইথনে কোন কেস কোথায় ব্যবহার করা হয়, তার একটি সহজ গাইডলাইন নিচে দেওয়া হলো:


১. স্নেক কেস (Snake Case) ➔ account_balance
নিয়ম: সব অক্ষর ছোট হাতের (Lowercase) হবে এবং দুটি শব্দের মাঝখানে একটি আন্ডারস্কোর (_) বসবে।

কোথায় ব্যবহার করা হয়: পাইথনে যেকোনো ভেরিয়েবল (Variable) এবং ফাংশন (Function)-এর নাম লেখার জন্য এটিই একমাত্র প্রফেশনাল নিয়ম।

# একদম পারফেক্ট ও প্রফেশনাল পাইথন কোড
account_balance = 5000
user_name = "Abdullah"

def calculate_interest():
    pass



২. প্যাসকেল কেস (Pascal Case) বা ক্যামেল কেস ➔ AccountBalance
নিয়ম: প্রতিটা শব্দের প্রথম অক্ষর বড় হাতের (Uppercase) হবে এবং মাঝখানে কোনো স্পেস বা আন্ডারস্কোর থাকবে না। (পাইথনে একে CapWords-ও বলা হয়)।

কোথায় ব্যবহার করা হয়: পাইথনে কোনো ক্লাস (Class) তৈরি করার সময় এই কেসটি ব্যবহার করা হয়। ভেরিয়েবলের জন্য এটি পাইথনে ব্যবহার করা হয় না।

# ক্লাসের নাম লেখার প্রফেশনাল নিয়ম
class BankAccount:
    pass

class UserProfile:
    pass


৩. ক্যামেল কেস (Camel Case) ➔ accountBalance
নিয়ম: প্রথম শব্দের প্রথম অক্ষর ছোট হাতের হবে, কিন্তু পরের প্রতিটা শব্দের প্রথম অক্ষর বড় হাতের হবে।

কোথায় ব্যবহার করা হয়: এটি জাভাস্ক্রিপ্ট (JavaScript) বা জাভা (Java) ল্যাঙ্গুয়েজে ভেরিয়েবলের জন্য সবচেয়ে বেশি ব্যবহৃত হয়। পাইথনে ক্যামেল কেস সাধারণত ব্যবহার করা হয় না। 
যদি পাইথনে accountBalance লিখা হয়, তবে কোড রান করবে ঠিকই,
কিন্তু অন্য কোনো পাইথন ডেভলপার কোড দেখলে বুঝবেন যে জাভাস্ক্রিপ্টের স্টাইলে পাইথন কোড লিখা হয়েছে।


৪. আপারকেস স্নেক কেস (UPPERCASE_SNAKE_CASE) ➔ ACCOUNT_BALANCE
নিয়ম: সব অক্ষর বড় হাতের হবে এবং মাঝখানে আন্ডারস্কোর বসবে।

কোথায় ব্যবহার করা হয়: কোডে কোনো কনস্ট্যান্ট (Constant) বা ফিক্সড মান (যার মান পুরো কোডে কখনো পরিবর্তন হবে না) রাখার জন্য এটি ব্যবহার করা হয়।
    
# পাইথনে কনস্ট্যান্ট লেখার নিয়ম
PI = 3.1416
MAX_WITHDRAW_LIMIT = 25000





একাধিক ভেরিয়েবলে একাধিক মান
পাইথন এক লাইনে একাধিক ভেরিয়েবলে মান অ্যাসাইন করার সুযোগ দেয়:

উদাহরণ: 
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z

a, b, c = 5, 10, 15
print(a) # আউটপুট: 5
print(b) # আউটপুট: 10
print(c) # আউটপুট: 15
      



      
একই মান একাধিক ভেরিয়েবলে 
এবং একই মান এক লাইনে একাধিক ভেরিয়েবলে অ্যাসাইন করা যাবে :

উদাহরণ
x = y = z = "Orange"
print(x)
print(y)
print(z)




x = y = z = "Mango"
print(x) # আউটপুট: Mango
print(y) # আউটপুট: Mango
print(z) # আউটপুট: Mango



একটি কালেকশন আনপ্যাক করা
যদি একটি লিস্ট, টাপল ইত্যাদিতে একাধিক ভ্যালুর একটি কালেকশন থাকে, তাহলে পাইথন সেই ভ্যালুগুলোকে ভেরিয়েবলে বের করে আনার সুযোগ দেয়। একে আনপ্যাকিং বলা হয়।

উদাহরণ

একটি লিস্ট আনপ্যাক:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)



আউটপুট ভেরিয়েবল
ভেরিয়েবল আউটপুট করার জন্য প্রায়শই print() ফাংশন ব্যবহার করা হয়।
Example
x = "Python is awesome"
print(x)



print() ফাংশনে, কমা দিয়ে আলাদা করে একাধিক ভেরিয়েবল আউটপুট করা যায়:
 
উদাহরণ
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)




একাধিক ভেরিয়েবল আউটপুট করতে + অপারেটরটিও ব্যবহার করা যায়:

উদাহরণ 
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)




print() ফাংশনে একাধিক ভেরিয়েবল আউটপুট করার সবচেয়ে ভালো উপায় হলো সেগুলোকে কমা দিয়ে আলাদা করা, যা বিভিন্ন ডেটা টাইপও সমর্থন করে:

উদাহরণ
x = 5
y = "Abdullah"
print(x, y)



ভেরিয়েবলের ডেটা টাইপ চেক করা
কোনো ভেরিয়েবলে বর্তমানে কী ধরণের ডেটা আছে তা জানার জন্য type() ফাংশন ব্যবহার করা হয়।

name = "Abdullah"
score = 95
height = 5.8


print(type(name))   # আউটপুট: <class 'str'> (String)
print(type(score))  # আউটপুট: <class 'int'> (Integer)
print(type(height)) # আউটপুট: <class 'float'> (Float)



name = "Abdullah"
age = 30
height = 5.222

# ১. সাধারণ স্ট্রিং জোড়া লাগানো (+ চিহ্ন এবং str() দিয়ে)
print("My name is: " + userName + " My age is: " + str(userAge) + " My height is: " + str(userHeight) + " feet")

# ২. round() ফাংশন ব্যবহার করে দশমিকের পর ১ ঘর রাউন্ড করে
print("My name is: " + userName + " My age is: " + str(userAge) + " My height is: " + str(round(userHeight, 1)) + " feet")

# ৩. format() ফাংশন ব্যবহার করে দশমিকের পর ১ ঘর ফিক্সড করে
print("My name is: " + userName + " My age is: " + str(userAge) + " My height is: " + format(userHeight, ".1f") + " feet")

# ৪. আধুনিক f-string ব্যবহার করে (সবচেয়ে সহজ এবং বেস্ট প্র্যাকটিস)
print(f"My name is: {userName} My age is: {userAge} My height is: {userHeight:.1f} feet")

# ৫. কমা (,) ব্যবহার করে (আপনার শেষের লাইনটির সঠিক রূপ)
print("My name is:", userName, "My age is:", userAge, "My height is:", f"{userHeight:.1f}", "feet")

# শেষে ".1f" }) এর পর ডাবল কোটেশন ও ব্র্যাকেট ঠিক করা হয়েছে
print(f"My name {name} my age {age} my height {format(height, '.1f')}")





জাভাস্ক্রিপ্টে যেভাবে .toFixed(2) ব্যবহার করে দশমিকের পরের ঘর ফিক্সড করা হয়, পাইথনেও ঠিক একইভাবে str() ব্যবহার না করে f-string-এর ভেতরেই সংখ্যা বা 
হাইটকে ফরম্যাট (যেমন দশমিকের পর কয় ঘর থাকবে তা ফিক্সড) করা যায়।

পাইথনে এর জন্য কোলন (:) ব্যবহার করতে হয়।

পাইথনে toFixed এর বিকল্প (f-string ফরম্যাটিং)

হাইট যদি হয় 5.8745 এবং যদি চাওয়া হয় দশমিকের পর মাত্র ২ ঘর দেখাবে (JS-এর .toFixed(2)-এর মতো), তবে f-string-এর ভেতর  {height:.2f}।

এখানে:

: মানে হলো ফরম্যাট করতে চাওয়া হসছে।

.2 মানে হলো দশমিকের পর ২ ঘর রাখতে চাওয়া হসছে।

f মানে হলো এটি একটি ফ্লোট বা দশমিক সংখ্যা (Float)।

name = "Abdullah"
age = 25
height = 5.8745  # একটি দশমিক সংখ্যা

# str() ছাড়া এবং দশমিকের পর ২ ঘর ফিক্সড করে প্রিন্ট:
print(f"My name is {name}, I am {age} years old and my height is {height:.2f} feet.")




প্লাস (+) চিহ্ন দিয়ে কোটেশনের ভেতরেও দশমিকের ঘর ফিক্সড করা যায়, তবে সে ক্ষেত্রে পাইথনের বিল্ট-ইন round() ফাংশন অথবা format() ফাংশন ব্যবহার করতে হবে।
যেহেতু প্লাস (+) দিয়ে জোড়া দেওয়ার সময় পাইথনে str() লিখতেই হয়, তাই str()-এর ভেতরেই সংখ্যাটিকে সাইজ করে নিতে হবে।

round() ফাংশন ব্যবহার করে (সবচেয়ে সহজ)

round(height, 2) লিখলে পাইথন সংখ্যাটিকে দশমিকের পর ২ ঘরে নিয়ে আসে। এরপর সেটাকে str() দিয়ে ঘিরে দিলেই কাজ শেষ।

name = "Abdullah"
age = 25
height = 5.8745

print("My name is " + name + ", I am " + str(age) + " years old and my height is " + str(round(height, 2)) + " feet.")


format() ফাংশন ব্যবহার করে (একদম নিখুঁত)

format(height, ".2f") ব্যবহার করলে এটি জাভাস্ক্রিপ্টের .toFixed(2)-এর মতো হুবহু কাজ করে এবং সরাসরি টেক্সট বা স্ট্রিং আউটপুট দেয় (তাই এর বাইরে আলাদা করে আর str() লেখা লাগে না)।

name = "Abdullah"
age = 25
height = 5.8745

print("My name is " + name + ", I am " + str(age) + " years old and my height is " + format(height, ".2f") + " feet.")

⚠️ একটি ছোট পার্থক্য:

যদি হাইট হুবহু 5.80 হতো, তবে round(5.80, 2) করলে পাইথন শেষের শূন্যটি বাদ দিয়ে শুধু 5.8 দেখাবে।

কিন্তু format(5.80, ".2f") ব্যবহার করলে জাভাস্ক্রিপ্টের মতোই জোর করে দশমিকের পর দুই ঘর মিলিয়ে 5.80-ই দেখাবে। তাই দশমিক ফিক্সড করার জন্য format() ব্যবহার করাই সবচেয়ে নিরাপদ।




name = "Abdullah"
age = 25
height = 5.8745

print("My name is {}, I am {} years old and my height is {:.2f} feet.".format(name, age, height))
# আউটপুট: My name is Abdullah, I am 25 years old and my height is 5.87 feet.

এটি পাইথনে f-string (যেমন: f"...") আসার আগের অর্থাৎ পাইথন ২ এবং পাইথন ৩-এর শুরুর দিকের অত্যন্ত জনপ্রিয় একটি নিয়ম। 
যদিও এখন f-string বেশি ব্যবহার করা হয়, তবে বড় বড় প্রজেক্টে বা পুরাতন কোডে এই format() মেথডটি প্রচুর দেখা যাবে।

১. প্লেসহোল্ডার বা খালি ঘর {} এর খেলা

এই লাইনের মূল ট্রিক বা ম্যাজিক হলো সেকেন্ড ব্র্যাকেট বা কার্লি ব্রেসেস {}। পাইথনের ভাষায় একে বলা হয় প্লেসহোল্ডার (Placeholder) বা সহজ বাংলায় "খালি ঘর"।

যখন ডাবল কোটের ভেতরে {} লিখা হয়েছে, পাইথনকে বলছেন— এই জায়গাটা এখন খালি রাখো, এখানে পরে একটা ভ্যালু বা মান এসে বসবে।"

২. সিরিয়াল বা ক্রমানুসারে মান বসানো
ডাবল কোটেশনের ঠিক শেষেই ডট দিয়ে লেখা হয়েছে .format(name, age, height)। এর কাজ হলো পেছনের খালি ঘরগুলোতে সিরিয়াল অনুযায়ী মানগুলো সাপ্লাই দেওয়া।

পাইথন একদম বাম দিক থেকে গোনা শুরু করে:

প্রথম খালি ঘর {}-এ গিয়ে বসবে .format()-এর ভেতরের প্রথম ভেরিয়েবল অর্থাৎ name।

দ্বিতীয় খালি ঘর {}-এ গিয়ে বসবে দ্বিতীয় ভেরিয়েবল অর্থাৎ age।

তৃতীয় খালি ঘর {}-এ গিয়ে বসবে তৃতীয় ভেরিয়েবল অর্থাৎ height।






# ১৫টি আইটেমের নাম
i1 = "Miniket Rice (5kg)"
i2 = "Mustard Oil (1L)"
i3 = "Masoor Dal (1kg)"
i4 = "Sugar (1kg)"
i5 = "Salt (1kg)"
i6 = "Rupchanda Oil (2L)"
i7 = "Aata (2kg)"
i8 = "Teaser Tea (400g)"
i9 = "Powder Milk (500g)"
i10 = "Onion (1kg)"
i11 = "Garlic (500g)"
i12 = "Ginger (500g)"
i13 = "Turmeric Powder"
i14 = "Chili Powder"
i15 = "Dish Wash Liquid"

# ১৫টি আইটেমের দাম
p1 = "340.00 tk"
p2 = "220.00 tk"
p3 = "130.00 tk"
p4 = "115.00 tk"
p5 = "42.00 tk"
p6 = "330.00 tk"
p7 = "95.00 tk"
p8 = "125.00 tk"
p9 = "410.00 tk"
p10 = "75.00 tk"
p11 = "90.00 tk"
p12 = "110.00 tk"
p13 = "60.00 tk"
p14 = "65.00 tk"
p15 = "85.00 tk"

# পাইথনে প্রিন্ট করার জন্য f-string ব্যবহার করা হয় (জাভাস্ক্রিপ্টের ব্যাকটিক ` ` এর মতো)
print(f"""Product Name              | Price
--------------------------------------
{i1.ljust(25, ".")} | {p1}
{i2.ljust(25, ".")} | {p2}
{i3.ljust(25, ".")} | {p3}
{i4.ljust(25, ".")} | {p4}
{i5.ljust(25, ".")} | {p5}
{i6.ljust(25, ".")} | {p6}
{i7.ljust(25, ".")} | {p7}
{i8.ljust(25, ".")} | {p8}
{i9.ljust(25, ".")} | {p9}
{i10.ljust(25, ".")} | {p10}
{i11.ljust(25, ".")} | {p11}
{i12.ljust(25, ".")} | {p12}
{i13.ljust(25, ".")} | {p13}
{i14.ljust(25, ".")} | {p14}
{i15.ljust(25, ".")} | {p15}
--------------------------------------""")




name = "Abdullah"
age = 30
height = 5.22
married = False
account = 12.3214123

print(f'{"Field".ljust(10)} | {"Value".rjust(7)}')
print('-' * 22)
print(f"{'Name'.ljust(10)} | {name.rjust(10)}")
print(f"{'Height'.ljust(10)} | {format(height, '.1f').rjust(5)}")
print(f"{"Account".ljust(10)} |   ${format(account, '.3f').rjust(5)}")
print(f"{'Married'.ljust(10)} | {'Yes' if married else 'No'.rjust(4)}")


ljust(10) (Left Adjust): লেখাটিকে বামে বসিয়ে রাখবে এবং ডানে খালি স্পেস যোগ করে মোট ১০ ঘর পূর্ণ করবে।

rjust(10) (Right Adjust): লেখাটিকে ঠেলে ডানে পাঠিয়ে দেবে এবং বামে খালি স্পেস যোগ করে মোট ১০ ঘর পূর্ণ করবে।


name = "Abdullah"

print(f"{'Field'.ljust(10)} | {'Value'.rjust(7)}")
print("-" * 22)
print(f"{'Name:'.ljust(10)} | {name.rjust(10)}")


Field      |   Value
----------------------
Name:      |   Abdullah


📊 পজিশন ও স্পেস ম্যাপিং:
১.  Field.ljust(10)
'Field' শব্দটিতে ৫টি অক্ষর আছে।

ljust(10) বলায় টেক্সটটি বামে চেপেছে এবং ডানপাশে ৫টি অতিরিক্ত স্পেস যোগ হয়ে মোট ১০ ঘরের জায়গা নিয়েছে:
['F', 'i', 'e', 'l', 'd', ' ', ' ', ' ', ' ', ' ']

২. 'Abdullah'.rjust(10)
'Abdullah' শব্দটিতে ৮টি অক্ষর আছে।

rjust(10) বলায় টেক্সটটি ডানে সরে গেছে এবং বামপাশে ২টি অতিরিক্ত স্পেস যোগ হয়ে মোট ১০ ঘরের জায়গা নিয়েছে:
[' ', ' ', 'A', 'b', 'd', 'u', 'l', 'l', 'a', 'h']


name = "Abdullah"
age = 30
married = False
account = 12.1234123

# টেবিল হেডার
print(f"{'Field'.ljust(10)} | {'Value'.rjust(10)}")
print("-" * 23)

# ডাটা রো (Rows)
print(f"{'Name:'.ljust(10)} | {name.rjust(10)}")
print(f"{'Age:'.ljust(10)} | {str(age).rjust(10)}")
print(f"{'Married:'.ljust(10)} | {str(married).rjust(10)}")
# float সংখ্যা ২ দশমিক ঘর পর্যন্ত সুন্দর করে সাজানো
print(f"{'Account:'.ljust(10)} | {f'{account:.2f}'.rjust(10)}")





center() মেথডের কাজ হলো—টেক্সটটিকে নির্দিষ্ট জায়গায় একদম মাঝখানে (Center Align) এনে বসানো।

ljust(10)বামেডানপাশে স্পেস যোগ হবে 
rjust(10)ডানেবামপাশে স্পেস যোগ হবে
center(10)মাঝখানেডানে ও বামে সমানভাবে স্পেস ভাগ হয়ে যাবে


name = "Abdullah"
age = 30
married = False
account = 12.1234123

# টেবিল হেডার (সবকিছু মাঝখানে থাকবে)
print(f"{'Field'.center(12)} | {'Value'.center(12)}")
print("-" * 27)

# ডাটা রো (Rows)
print(f"{'Name:'.ljust(12)} | {name.center(12)}")
print(f"{'Age:'.ljust(12)} | {str(age).center(12)}")
print(f"{'Married:'.ljust(12)} | {str(married).center(12)}")
print(f"{'Account:'.ljust(12)} | {f'{account:.2f}'.center(12)}")


Field     |    Value    
---------------------------
Name:        |   Abdullah  
Age:         |      30     
Married:     |    False    
Account:     |    12.12



🎨 কাস্টম ক্যারেক্টার দিয়ে ডিজাইন করা:
center() মেথডে খালি স্পেসের বদলে অন্য কোনো চিহ্ন (যেমন: -, *, =) বসিয়ে সুন্দর টাইটেল বা হেডার বর্ডার বানানো যায়:

title = " USER PROFILE "

# ৩০ ঘরের মাঝখানে 'USER PROFILE' বসাবে এবং ডানে-বামে '=' দিয়ে ভরাট করবে
print(title.center(30, "="))


======== USER PROFILE ========


💡 মেমোরিতে কীভাবে স্পেস ভাগ হয় (Dry-Run):"Abdullah".center(12)'Abdullah' শব্দের দৈর্ঘ্য = ৮ ক্যারেক্টার।মোট ঘর দেওয়া হয়েছে = ১২।
অবশিষ্ট খালি ঘর = 12 - 8 = 4 টি।
পাইথন বামে ২টি এবং ডানে ২টি স্পেস বসিয়ে দেবে: [' ', ' ', 'A', 'b', 'd', 'u', 'l', 'l', 'a', 'h', ' ', ' ']
