Dictionary হলো পাইথনের একটা ডেটা টাইপ যেটা ডেটা রাখে Key-Value জোড়া (pair) আকারে। List/Tuple/Set এ শুধু value থাকতো, 
index দিয়ে খুঁজতে হতো। কিন্তু Dictionary তে প্রতিটা value এর একটা নাম (key) থাকে, যেটা দিয়ে সরাসরি সেই value খুঁজে বের করা যায়।


পাইথনে ডিকশনারি (Dictionary) হলো পরিবর্তনশীল বা Mutable।

অর্থাৎ, ডিকশনারি তৈরি করার পরেও  এর ভেতরে থাকা যেকোনো ডেটা বা ভ্যালু পরিবর্তন, নতুন Key-Value জোড়া যোগ, অথবা পুরানো কোনো Key মুছে ফেলতে পারবেন।

সহজ কথায়: এটা অনেকটা বাস্তব জীবনের অভিধান (dictionary) এর মতো — যেমন একটা শব্দ (key) দিয়ে তার অর্থ (value) খোঁজা হয়।
Dictionary (dict) হলো Python-এর একটি Built-in Data Type যা Key-Value Pair আকারে ডেটা সংরক্ষণ করে।


পাইথন ডিকশনারি এবং ইনডেক্স (Key) কনসেপ্ট
পাইথনে লিস্ট বা স্ট্রিংয়ের মতো ডিকশনারিতে কোনো সিরিয়াল নম্বর বা ইনডেক্স (0, 1, 2...) থাকে না।
এর পরিবর্তে ডিকশনারি কাজ করে Key-Value Pair (কি এবং ভ্যালু জোড়া) এর ভিত্তিতে। এখানে Key-ই হলো একধরনের কাস্টম ইনডেক্স।



ডিকশনারির কি (Key) হিসেবে কী ব্যবহার করা যায়?
ডিকশনারির key হতে হলে ডেটাকে অবশ্যই Immutable (অপরিবর্তনশীল) এবং Hashable হতে হবে।

ব্যবহার করা যায়:

স্ট্রিং ("name", "id")

সংখ্যা (10, 3.14)

টুপল ((1, 2)) — শর্ত হলো টুপলের ভেতরের উপাদানগুলোও যেন immutable হয়।

ফ্রোসেনসেট (frozenset) — যেহেতু এটি immutable, তাই এটিও ডিকশনারির key হতে পারে।

ব্যবহার করা যায় না:

লিস্ট (list)

সাধারণ সেট (set)

ডিকশনারি (dict)
(কারণ এই ডেটাগুলো Mutable বা পরিবর্তনযোগ্য, তাই পাইথন এদের key বানাতে দিলে TypeError দেখায়।)



frozenset-এর মেথডসমূহ
যেহেতু frozenset হলো Immutable (অপরিবর্তনশীল), তাই এতে কোনো উপাদান যোগ বা বাদ দেওয়ার মেথড (add, remove, update, difference_update ইত্যাদি) নেই।

তবে দুটি বা ততোধিক সেটের মধ্যে তুলনা করার বা নতুন সেট তৈরির জন্য এর বেশ কিছু রিড-অনলি বা Non-mutating মেথড রয়েছে। প্রধান মেথডগুলো নিচে দেওয়া হলো:



কমন অপারেশন বা সেট মেথডসমূহ:
.union(other_set) (বা | অপারেটর): দুটি ফ্রোসেনসেট এক করে নতুন সেট তৈরি করে।

.intersection(other_set) (বা & অপারেটর): দুটি সেটের মধ্যে কমন (মিল আছে এমন) উপাদানগুলো নিয়ে নতুন সেট বানায়।

.difference(other_set) (বা - অপারেটর): প্রথম সেটে আছে কিন্তু দ্বিতীয় সেটে নেই এমন উপাদানগুলো বের করে।

.symmetric_difference(other_set) (বা ^ অপারেটর): দুটি সেটের মধ্যে যে উপাদানগুলো অমিল বা ইউনিক (উভয় সেটে কমন নয়), সেগুলোকে নিয়ে নতুন সেট বানায়।



চেকিং বা বুলিয়ান (Boolean) মেথডসমূহ (True/False রিটার্ন করে):
.issubset(other_set): একটি ফ্রোসেনসেটের সব উপাদান অন্য সেটের ভেতরে আছে কি না চেক করে।

.issuperset(other_set): একটি ফ্রোসেনসেট অন্য সেটটিকে পুরোপুরি ধারণ করে কি না চেক করে।

.isdisjoint(other_set): দুটি ফ্রোসেনসেটের মধ্যে একটি উপাদানেরও মিল নেই কি না চেক করে (মিল না থাকলে True দেয়)।


ইউটিলিটি মেথড:
.copy(): হুবহু একই রকম আরেকটি নতুন frozenset কপি তৈরি করে দেয়।

fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

# union মেথড ব্যবহার
print(fs1.union(fs2))           # আউটপুট: frozenset({1, 2, 3, 4, 5})

# intersection মেথড ব্যবহার
print(fs1.intersection(fs2))    # আউটপুট: frozenset({3})




ডিকশনারি কী এবং বেসিক স্ট্রাকচার

Key-Value Pair: ডিকশনারিতে প্রতিটি ডেটার একটি ইউনিক Key থাকে এবং তার বিপরীতে একটি Value থাকে। এগুলোকে সেকেন্ড ব্র্যাকেট {} দিয়ে লেখা হয়।

Mutable (পরিবর্তনশীল): ডিকশনারি তৈরি করার পরেও এর ভেতর ডেটা যোগ, পরিবর্তন বা ডিলিট করা যায়।

Ordered (অর্ডারড): পাইথনের আধুনিক সংস্করণগুলোতে (Python 3.7+) ডিকশনারি ইনসার্ট করার অর্ডার মনে রাখে।


# একটি বেসিক ডিকশনারি
student = {
    "name": "Arman",
    "age": 30,
    "course": "Python Backend"
}




. Dictionary তৈরি করার নিয়ম

Dictionary লেখা হয় curly bracket { } দিয়ে, প্রতিটা key: value জোড়া কোলন (:) দিয়ে আলাদা করা হয়, আর একাধিক জোড়া কমা (,) দিয়ে আলাদা করা হয়।

# একটি ছাত্রের তথ্য নিয়ে ডিকশনারি
student = {
    "name": "Abdullah",
    "age": 22,
    "cgpa": 3.75,
    "is_active": True
}

print(student)

ডিকশনারির একদম শেষ আইটেমটির ('is_active': True) পরে আর কমা (,) দেওয়ার প্রয়োজন নেই। পাইথনে শেষ লাইনের পরে কমা না দিলেও কোড সুন্দরভাবে কাজ করে।

এখানে "name", "age", "cgpa", "is_active" হলো Keys (চাবি)।

আর "Abdullah", 22, 3.75, True হলো তাদের নিজস্ব Values (মান)।


student = {
    "name": "Arman",
    "age": 22,
    "department": "CSE"
}

"name"       → Key
"Arman"      → Value

"age"        → Key
22           → Value

"department" → Key
"CSE"        → Value


এখানে student কী?

student হলো একটি ভেরিয়েবল (Variable) বা পাত্র, 

যার ভেতরে পুরো ডিকশনারি ডেটাটিকে সংরক্ষণ করে রাখা হয়েছে।  চাইলে student-এর জায়গায় অন্য যেকোনো নাম (যেমন: user, profile, data) দিতে পারতেন।


Key বলতে "name" এবং কোলন (:) কেন দেওয়া হয়?
Key ("name"): ডিকশনারির ভেতরে নির্দিষ্ট কোনো ডেটাকে চেনার বা খোঁজার জন্য যে লেবেল বা নাম দেওয়া হয়, তাকেই Key বলে। 
যেমন—স্টুডেন্টের নাম খোঁজার কি হলো "name", বয়স খোঁজার কি হলো "age"।

কোলন (:) কেন? কোলন (:) হলো সংযোগকারী চিহ্ন। এটি পাইথনকে বলে দেয়:

"বাম পাশের Key-এর বিপরীতে ডান পাশের এই Value-টি যুক্ত করো।"
লেখার নিয়ম হলো: Key: Value


empty_dict = {}                                    # খালি dictionary
person = {"name": "Rahim", "age": 25}               # key-value জোড়া
student = {"id": 1, "name": "Karim", "pass": True}  # বিভিন্ন টাইপের value




# A sample dictionary representing a student

student = {
    "name": "Arman",   # "name" is the Key, "Arman" is the Value
    "age": 30,         # "age" is the Key, 30 is the Value
    "city": "Dhaka"    # "city" is the Key, "Dhaka" is the Value
}



৩টি মূল টার্মের সহজ ব্যাখ্যা:

Key (কি):

এটি কোলন (:) এর বামের অংশ।

ডিকশনারিতে ডেটা খোঁজার বা অ্যাক্সেস করার জন্য এটি লেবেল হিসেবে কাজ করে।

উপরের উদাহরণে: "name", "age", এবং "city" হলো ডিকশনারির Key। (Keys গুলি সবসময় unique বা অদ্বিতীয় হতে হয়)।



Value (ভ্যালু বা মান):

এটি কোলন (:) এর ডানের অংশ।

এটি হলো আসল ডেটা, যা একটি Key-এর বিপরীতে সংরক্ষিত থাকে।

উপরের উদাহরণে: "Arman", 30, এবং "Dhaka" হলো ডিকশনারির Value।



Pair (পায়ার বা কি-ভ্যালু জোড়া):

একটি Key এবং তার সাথে থাকা সংশ্লিষ্ট Value মিলে পুরো সেটটিকে একত্রে Key-Value Pair (বা আইটেম) বলা হয়।

উপরের ডিকশনারিতে মোট ৩টি পেয়ার আছে:

Pair 1: "name": "Arman"

Pair 2: "age": 30

Pair 3: "city": "Dhaka"




student = {
  'name': 'Abdullah',
  'age': 30,
  'subject': 'Programming',
  'height': 5.2,
  'married': True
}

print(student['name'])  # 'name' কি-এর ভেতরে থাকা ভ্যালু প্রিন্ট করবে

কেন এবং কীভাবে এটি কাজ করল?

যখন student['name'] লিখা হয়েছে, তখন পাইথন ডিকশনারির ভেতরে খুঁজে দেখেছে 'name' নামের কোনো কি (Key) আছে কি না।

সে যখন পেল যে 'name' কি-এর বিপরীতে 'Abdullah' মানটি সংরক্ষিত আছে, তখন সে শুধু ওই মানটিই প্রিন্ট করে দিল।

ডিকশনারি থেকে এভাবেই খুব সহজে যেকোনো কি দিয়ে তার কাঙ্ক্ষিত ভ্যালু বের করে আনা যায়।

student = {
  'name': 'Abdullah',
  'age': 30,
  'subject': 'Programming',
  'height': 5.2,
  'marrird': True
}

print(student)

result_access = student['name']

print(result_access)

ডিকশনারির ক্ষেত্রে স্কয়ার ব্র্যাকেট [] কেন ব্যবহার করা হয় এবং এর পেছনের কারণ

ডিকশনারিতে [] কেন ব্যবহার করা হয়?
পাইথনে স্কয়ার ব্র্যাকেট []-কে বলা হয় Indexing বা Accessing Operator। ডিকশনারির ভেতরে কোন নির্দিষ্ট Key-এর বিপরীতে কি মান আছে,
তা খুঁজে বের করার জন্য এই ব্র্যাকেট ব্যবহার করা হয়।

বিষয়টি একটি বাস্তব উদাহরণের সাহায্যে ভাবুন:

অনেকগুলো ওষুধের কৌটা আছে এবং প্রতিটা কৌটার গায়ে আলাদা নাম বা লেবেল লাগানো আছে (যেমন: 'Paracetamol', 'Napa')।

এখন  যদি 'Napa' কৌটাটি দরকার হয়, সব কৌটা খুলবেন? না! সরাসরি 'Napa' লেবেল লেখা কৌটাটি হাত দিয়ে ধরবেন এবং ভেতর থেকে ওষুধ বের করবেন।

পাইথনের ডিকশনারির ক্ষেত্রেও ব্যাপারটি ঠিক তাই:

student হলো পুরো ডিকশনারি বক্স।

'name' হলো কৌটার গায়ে লাগানো লেবেল বা Key।

আর যখন লিখলেন student['name'], তখন পাইথন ওই লেবেল ধরে সরাসরি ভেতর থেকে 'Abdullah' মানটি টেনে বের করে আনল।

রাউন্ড ব্র্যাকেট () বা কার্লি ব্র্যাকেট {} কেন ব্যবহার করা হয় না?
কার্লি ব্র্যাকেট {} ব্যবহার করা হয় ডিকশনারি তরি বা ডিকশনারির সীমানা বোঝাতে (যেমনটা আপনি student = {...} লেখার সময় করেছেন)।

রাউন্ড ব্র্যাকেট () ব্যবহার করা হয় ফাংশন কল করার জন্য (যেমন: print(), dict(), type())।

তাই ডিকশনারি থেকে ডেটা রিড বা অ্যাক্সেস করার সময় পাইথনের নিয়ম অনুযায়ী বাধ্যতামূলকভাবে স্কয়ার ব্র্যাকেট [] ব্যবহার করতে হয়।




ভ্যারিয়েবলে ডেটা রেখে নতুন মান যোগ করা বা পুরনো মান পরিবর্তন করা খুবই সহজ। 
যখন ডিকশনারির কোনো কি (Key)-তে নতুন মান অ্যাসাইন করা হয়,
তখন পাইথন স্বয়ংক্রিয়ভাবে বুঝে নেয়—সেটি নতুন হলে যোগ করতে হবে, আর পুরনো হলে আপডেট করে দিতে হবে।

student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend"
}

print("Old student:", student)

# ১. ভ্যারিয়েবলে নতুন মান রেখে সেটি ডিকশনারিতে যোগ করা

new_city = "Rangpur"

student["city"] = new_city  # এটি একদম শেষে যুক্ত হবে


# ২. ভ্যারিয়েবলে নতুন বয়স রেখে পুরনো বয়স আপডেট করা
updated_age = 31
student["age"] = updated_age  # পুরনো 30 কেটে গিয়ে 31 বসে যাবে


print("পরে (আপডেটের পর):", student)




student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend"
}

print("Old student:", student)

added_city = 'Rangpur'

student['city'] = added_city

print("New student:", student)






পাইথনের আধুনিক ভার্সনগুলোতে (Python 3.7 বা তার পরের সব ভার্সনে) 
ডিকশনারি ইনসার্শন অর্ডার (Insertion Order) মেইনটেইন করে। অর্থাৎ, আপনি নতুন কোনো কি-ভ্যালু যেভাবে যোগ করবেন, 
সেটি ডিকশনারির একদম শেষেই গিয়ে যুক্ত হবে—ঠিক যেমন লিস্টে .append() করলে শেষে যুক্ত হয়।

student = {
  'name' : 'Abdullah',
  'age' : 30,
  'cgpa' : 3.63,
  "course": "Python Backend"
}
print(student)

student["city"] = "Rangpur"

print(student)




⚠️ বিশেষ সতর্কতা (KeyError):

যদি এমন কোনো Key দিয়ে ডিকশনারি থেকে মান খুঁজতে চান যা ডিকশনারির ভেতরে নেই, তবে পাইথন ক্র্যাশ করবে এবং KeyError দিবে। 
এই সমস্যা থেকে বাঁচার জন্য get() মেথড ব্যবহার করা যায়:

student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend"
}

print(student)


student['name'] = 'Mohammad' #Reassigning the value of the key 'name' to 'Mohammad'

print(student)




student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend"
}

# ১. স্কয়ার ব্র্যাকেট দিয়ে ভ্যারিয়েবলে রাখা
student_name = student["name"]
print(student_name)  # আউটপুট: Abdullah


# ২. .get() মেথড ব্যবহার করে ভ্যারিয়েবলে রাখা
student_cgpa = student.get("cgpa")
print(student_cgpa)  # আউটপুট: 3.63


# ৩. এমন একটি Key খোঁজা যা ডিকশনারিতে নেই (.get() এর জাদু)
# যদি 'email' না থাকে, তবে কোড এরর না দিয়ে None রিটার্ন করবে এবং ভ্যারিয়েবলে জমা হবে
student_email = student.get("email")
print(student_email)  # আউটপুট: None


# ৪. .get() এ ডিফল্ট ভ্যালু সেট করে দেওয়া (Key না থাকলে এটি দেখাবে)
student_phone = student.get("phone", "Not Available")
print(student_phone)  # আউটপুট: Not Available



student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend"
}

result = student['fruits'] #program will throw an error because the key 'fruits' does not exist in the dictionary.

print(result)

print(student)



student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend"
}

result_name = student.get('name', 'No name found')

result = student.get('fruits', 'No fruits found')

print(result)

print(student)

print(result_name)




ডিকশনারি থেকে ডেটা ডিলিট করার জন্য মূলত দুটি জনপ্রিয় উপায় রয়েছে: del স্টেটমেন্ট এবং .pop() মেথড।

del স্টেটমেন্ট এবং .pop() মেথড।


student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend",
  "city": "Rangpur"
}

print("Before deletion:", student)

# ১. del ব্যবহার করে সরাসরি নির্দিষ্ট কি-ভ্যালু ডিলিট করা

del student["age"]

print("After deleting 'age':", student)




student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend",
  "city": "Rangpur"
}

print(student)

del student['age']

print(student)



# ২. .pop() ব্যবহার করে ডিলিট করা এবং রিমুভ হওয়া ভ্যালু ভ্যারিয়েবলে রেখে দেওয়া
removed_course = student.pop("course")

print("Removed course value was:", removed_course)
print("After using pop():", student)


এই দুইটির মধ্যে পার্থক্য কী?
del student["age"]: এটি শুধু ডিলিট করে দেয়, রিমুভ হওয়া ভ্যালুটি কোথাও সেভ করে রাখে না।

student.pop("course"): এটি ডিলিট করার পাশাপাশি ওই ভ্যালুটি রিটার্ন করে, 
যা চাইলে কোনো ভ্যারিয়েবলে (removed_course) রেখে দিতে পারেন।


student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend",
  "city": "Rangpur"
}

removed_student = student.pop('city')

print(student)

print(f"Removed city: {removed_student}")




পাইথনে ডিকশনারি (Dictionary) হলো পরিবর্তনশীল বা Mutable।

ডিকশনারি থেকে ডেটা অ্যাক্সেস করার নিয়ম:
লিস্ট বা টিউপলের মতো এখানে ইনডেক্স (student[0]) দিয়ে ডেটা পাওয়া যায় না। ডিকশনারির ডেটা পেতে হলে তার Key ধরে ডাকতে হয়:


# একটি ছাত্রের তথ্য নিয়ে ডিকশনারি
student = {
    "name": "Abdullah",
    "age": 30,
    "cgpa": 3.63,
    "is_active": True
}

print(student)

print(student["name"])  # আউটপুট: Abdullah
print(student["cgpa"])  # আউটপুট: 3.63




Key দিয়ে Value বের করা

Dictionary তে index number না, key দিয়ে value access করতে হয়।

person = {"name": "Rahim", "age": 25, "city": "Dhaka"}

print(person["name"])   # Rahim
print(person["age"])    # 25
print(person["city"])   # Dhaka

⚠️ না থাকা key দিয়ে access করলে Error

print(person["salary"]) KeyError: 'salary'

নিরাপদ পদ্ধতি — get() মেথড ব্যবহার করা

print(person.get("salary"))          # None  (error দেয় না)
print(person.get("salary", "N/A"))   # N/A   (default value দেওয়া যায়)

get() মেথড দিয়ে access করলে key না থাকলেও প্রোগ্রাম crash করে না, বরং None অথবা নিজের দেওয়া default মান রিটার্ন করে। 
এটা backend code এ best practice।

student = {
  'name' : 'Abdullah',
  'age' : 30,
  'cgpa' : 3.63,
  "course": "Python Backend"
}

result = student.get('salary')

print(result)





Dictionary ভেতরে সাধারণ লিস্ট বা স্ট্রিংয়ের মতো ফিক্সড কোনো ইনডেক্স (0, 1, 2...) থাকে না। 

ডিকশনারির ক্ষেত্রে Key ই হলো তার কাস্টম ইনডেক্স।

ডিকশনারির কি-গুলোকে আগে একটি List-এ রূপান্তর করে নিতে হয়। এরপর .index() মেথড ব্যবহার করলেই ইনডেক্স পেয়ে যাবেন।


student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend",
  "city": "Rangpur"
}

all_keys = student.keys()

print(all_keys)    # dict_keys(['name', 'age', 'cgpa', 'course', 'city'])



student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend"
}

keys_list = list(student.keys())   # 1. Convert dictionary keys into a list

print("Keys List:", keys_list)



student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend",
  "city": "Rangpur"
}

keys_list = list(student.keys())

print(keys_list)   #['name', 'age', 'cgpa', 'course', 'city']



student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend",
  "city": "Rangpur"
}


keys_list = list(student.keys())

for key in keys_list:
  print(key)



student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend",
  "city": "Rangpur"
}

keys_list = list(student.keys())

# Dictionary Comprehension দিয়ে মূল ডিকশনারি থেকে ভ্যালু নিয়ে রূপান্তর
new_dict = {key: student[key] for key in keys_list}

print(new_dict)
# আউটপুট: {'name': 'Abdullah', 'age': 30, 'cgpa': 3.63, 'course': 'Python Backend', 'city': 'Rangpur'}




নতুন ভ্যালুর আলাদা লিস্ট থেকে ডিকশনারি তৈরি করা (zip())
যদি কাছে কি-এর লিস্টের পাশাপাশি নতুন ভ্যালুগুলোরও একটি আলাদা লিস্ট থাকে,
তবে zip() ফাংশন ব্যবহার করে সহজেই জোড়া লাগিয়ে ডিকশনারি বানিয়ে ফেলা যায়:

keys_list = ['name', 'age', 'cgpa', 'course', 'city']
values_list = ['Abdullah', 30, 3.63, 'Python Backend', 'Rangpur']

# zip() ব্যবহার করে জোড়া লাগিয়ে ডিকশনারিতে কনভার্ট
reconstructed_dict = dict(zip(keys_list, values_list))

print(reconstructed_dict)
# আউটপুট: {'name': 'Abdullah', 'age': 30, 'cgpa': 3.63, 'course': 'Python Backend', 'city': 'Rangpur'}





ডিফল্ট ভ্যালু বসিয়ে ডিকশনারি তৈরি করা (dict.fromkeys())
যদি কাছে শুধু কি-এর লিস্ট থাকে এবং প্রাথমিক অবস্থায় সবগুলোতে একটি নির্দিষ্ট ডিফল্ট ভ্যালু (যেমন: None বা 0 বা "N/A") সেট করতে:


# সব Key-এর ভ্যালু None সেট হবে
default_dict = dict.fromkeys(keys_list, None)

print(default_dict)
# আউটপুট: {'name': None, 'age': None, 'cgpa': None, 'course': None, 'city': None}




# 2. Find the index of a specific key using .index()


student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend",
  "city": "Rangpur"
}


keys_list = list(student.keys())

course_index = keys_list.index("course")

name_index = keys_list.index("name")

print("Index of 'course':", course_index) # 3
print("Index of 'name':", name_index) # 0


student = {
    "name": "Abdullah",
    "age": 22,
    "cgpa": 3.75
}

# ১. ডিকশনারির সব কি (Keys) গুলোকে একটি লিস্টে রূপান্তর করা
keys_list = list(student.keys())

# ২. এখন সাধারণ লিস্টের মতো index() মেথড ব্যবহার করা
age_index = keys_list.index("age")

print("Age Key Index:", age_index)
# আউটপুট: 1 (কারণ 'age' লিস্টের ২য় অবস্থানে বা 1 ইনডেক্সে আছে)





ডিকশনারি যে Mutable (পরিবর্তনশীল), অর্থাৎ এটি তৈরি করার পরেও এর ভেতরের মান পরিবর্তন করা যায়,

student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend"
}

print("Before modification:", student)

# Modifying existing values (Mutating the dictionary)
student['age'] = 31
student['cgpa'] = 3.80

print("After modification (Mutable property):", student)







মূল ডাটা দেখার মেথডসমূহ (keys, values, items)

ডিকশনারির .keys() মেথড ব্যবহার করে কীভাবে সবকটি Key আলাদা করে বের করা যায়


student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend",
  "city": "Rangpur"
}

print(student)

# Using .keys() to get all the keys from the dictionary
dict_keys = student.keys()

print(dict_keys)


print("\nLooping through keys:")

for key in student.keys():
    print(key)



student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend",
  "city": "Rangpur"
}


print(f"{student['name']} is {student['age']} years old. He has a CGPA of {student['cgpa']} 
and is enrolled in the {student['course']} course. He lives in {student['city']}.")





ডিকশনারির .values() মেথড ব্যবহার করে কীভাবে ডিকশনারির ভেতরে থাকা সবকটি Value আলাদা করে বের করা যায়


student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend",
  "city": "Rangpur"
}

print(student)

# Using .values() to get all the values from the dictionary

dictionary_values = student.values()
print(dictionary_values)

print("\nLooping through values:")
for value in student.values():
    print(value)





.items(): 

ডিকশনারির সবচেয়ে কার্যকরী এবং সবচেয়ে বেশি ব্যবহৃত মেথড হলো .items()।
এটি ডিকশনারির প্রতিটি Key এবং Value-কে জোড়ায় জোড়ায় (Tuple আকারে) রিটার্ন করে। 
লুপ চালানোর সময় এটি দিয়ে খুব সহজেই কি ও ভ্যালু আলাদা করে ফেলা যায়।


student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend",
  "city": "Rangpur"
}

print(student)

# Using .items() to get all key-value pairs as tuples

dictionary_items = student.items()

print(dictionary_items)  # Output: dict_items([('name', 'Abdullah'), ('age', 30), ('cgpa', 3.63), ('course', 'Python Backend'), ('city', 'Rangpur')])

# Iterating through items using a loop (Most commonly used in real projects)
print("\nLooping through items (Key and Value together):")

for key, value in student.items():
    print(f"Key: {key}, Value: {value}")




student = {"name": "Abdullah", "age": 22, "cgpa": 3.75}
print(student.keys())    # আউটপুট: dict_keys(['name', 'age', 'cgpa'])
print(student.values())  # আউটপুট: dict_values(['Abdullah', 22, 3.75])
print(student.items())   # আউটপুট: dict_items([('name', 'Abdullah'), ('age', 22), ('cgpa', 3.75)])





ডাটা আপডেট বা যোগ করার মেথড (update)

ডিকশনারির .update() মেথডটি একসাথে একাধিক ডেটা আপডেট করতে বা নতুন ডেটা যোগ করতে জাদুর মতো কাজ করে।
যদি কি (Key) আগে থেকেই থাকে, 
তবে তার মান আপডেট হয়ে যায়; আর যদি না থাকে, তবে তা নতুন কি-ভ্যালু হিসেবে ডিকশনারির একদম শেষে যুক্ত হয়ে যায়।


user = {"name": "Karim"}
extra_info = {"age": 25, "city": "Dhaka"}

# extra_info ডিকশনারির ডেটা user-এর সাথে যুক্ত করা হলো
user.update(extra_info)

print(user)
# আউটপুট: {'name': 'Karim', 'age': 25, 'city': 'Dhaka'}


student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend"
}

print("Before update:", student)

# Using .update() to modify existing values ('age', 'cgpa') 
# and add new key-value pairs ('city', 'country') at the same time
student.update({
    "age": 31, 
    "cgpa": 3.80, 
    "city": "Rangpur", 
    "country": "Bangladesh"
})

print("After update:", student)


# Base student dictionary
student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63
}

# Additional info dictionary that we want to merge
additional_info = {
    "course": "Python Backend",
    "city": "Rangpur",
    "cgpa": 3.80  # Existing key: will be updated/overwritten
}

print("Before merging:", student)

# Merging 'additional_info' into 'student' using .update()
student.update(additional_info)

print("After merging (Dictionaries combined & updated):", student)


Before merging: {'name': 'Abdullah', 'age': 30, 'cgpa': 3.63}
After merging (Dictionaries combined & updated): {'name': 'Abdullah', 'age': 30, 'cgpa': 3.8, 'course': 'Python Backend', 'city': 'Rangpur'}

১. additional_info ডিকশনারির নতুন কিগুলো (course এবং city) মূল student ডিকশনারির একেবারে শেষে যুক্ত হয়ে গেছে।
২. cgpa কি-টি আগে থেকেই student-এ ছিল (3.63), কিন্তু .update() রান করার পর সেটি ওভাররাইট হয়ে নতুন মান (3.80) হয়ে গেছে।

এভাবেই .update() দিয়ে খুব সহজে একাধিক ডিকশনারি মার্জ করা যায়।





দুটি ডিকশনারি একসাথে জোড়া লাগানো (Merge)
ধরে নিন কাছে ইউজারের বেসিক ইনফো আছে, আর আলাদা একটি ডিকশনারিতে তার প্রফেশনাল ইনফো আছে। 
চাচ্ছেন দুটিকে একত্র করতে:


user_info = {"name": "Abdullah", "age": 22}
job_info = {"role": "Backend Developer", "salary": 50000}

# job_info এর সব ডেটা user_info এর মধ্যে ঢুকিয়ে দেওয়া হলো
user_info.update(job_info)

print(user_info)

{'name': 'Abdullah', 'age': 22, 'role': 'Backend Developer', 'salary': 50000}



কোনো ভ্যালু আপডেট করা বা নতুন কি যুক্ত করা
.update() মেথডের চমৎকার ব্যাপার হলো—যদি ডিকশনারিতে কি-টি আগে থেকেই থাকে,
তবে সেটি নতুন ভ্যালু দিয়ে আপডেট (পরিবর্তন) করে দেয়। আর যদি কি-টি না থাকে, তবে নতুন করে যোগ করে নেয়।

settings = {"theme": "dark", "notifications": True}

# এখানে 'theme' পরিবর্তন হবে (dark থেকে light) এবং নতুন 'language' কি যুক্ত হবে
settings.update({"theme": "light", "language": "bn"})

print(settings)


{'theme': 'light', 'notifications': True, 'language': 'bn'}



কি-ওয়ার্ড আর্গুমেন্ট (Keyword Arguments) দিয়ে আপডেট করা
চাইলে সরাসরি ব্র্যাকেটের ভেতরে ডিকশনারি না লিখে, কি-এর নাম সরাসরি লিখেও .update() ব্যবহার:


profile = {"username": "abdullah_dev", "status": "offline"}

# সরাসরি কি-ভ্যালু দিয়ে আপডেট করা হলো
profile.update(status="online", country="Bangladesh")

print(profile)

{'username': 'abdullah_dev', 'status': 'online', 'country': 'Bangladesh'}






ডিকশনারির .pop() মেথডের মূল কাজ হলো ডিকশনারি থেকে নির্দিষ্ট কোনো Key এবং তার পেছনের Value-কে রিমুভ বা মুছে ফেলা।
এর একটি বিশেষ সুবিধা হলো—ডিকশনারি থেকে কি-টি মুছে ফেলার 
পাশাপাশি এটি চাইলে সেই মুছে ফেলা ভ্যালুটি আপনার জন্য রিটার্নও (ফিরে দিতে) করে, 
যাতে চাইলে সেটি কোনো ভ্যারিয়েবলে সংরক্ষণ করে রাখতে পারেন।


student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63,
  "course": "Python Backend",
  "city": "Rangpur"
}

print("Before pop:", student)

# 1. Using .pop() to remove a specific key and capture its value in a variable
removed_course = student.pop("course")
print("Removed value ('course'):", removed_course)
print("After pop:", student)

# 2. Using .pop() with a default value for a key that does not exist 
# (This prevents a KeyError and returns the default value instead)
removed_phone = student.pop("phone", "Not Available")
print("Result for non-existing key with default:", removed_phone)



student = {
    "name": "Abdullah",
    "age": 22,
    "cgpa": 3.75
}

# "age" কি-টি ডিকশনারি থেকে পপ বা রিমুভ করা হলো
removed_value = student.pop("age")

print("মুছে ফেলা ভ্যালু:", removed_value)
print("বর্তমান ডিকশনারি:", student)


মুছে ফেলা ভ্যালু: 22
বর্তমান ডিকশনারি: {'name': 'Abdullah', 'cgpa': 3.75}


একটি জরুরি ব্যাপার (Key না থাকলে কী হবে?):
আপনি যদি এমন কোনো Key ডিকশনারিতে পপ করতে যান যেটি আদতেই সেখানে নেই, তবে পাইথন KeyError বা এরর দেখাবে।

এই সমস্যা এড়ানোর জন্য .pop()-এর ভেতর একটি ডিফল্ট ভ্যালু সেট করে দেওয়া যায়। কি না থাকলে ক্রাশ না করে ওই ডিফল্ট ভ্যালু রিটার্ন করবে:

student = {"name": "Abdullah", "age": 22}

# 'address' কি-টি ডিকশনারিতে নেই, তাই এরর না দিয়ে "Not Found" প্রিন্ট করবে
result = student.pop("address", "Not Found")

print(result)  # আউটপুট: Not Found





.clear() মেথড
এই মেথডটির কাজ খুব সহজ—এটি একটি ডিকশনারির ভেতরের সমস্ত কি-ভ্যালু জোড়া মুছে ফেলে ডিকশনারিটিকে একদম খালি ({}) করে দেয়।


cart = {"item1": "Laptop", "item2": "Phone"}

# কার্ট বা ঝুড়ি পুরোপুরি খালি করে দেওয়া
cart.clear()

print(cart)
# আউটপুট: {}





.setdefault() মেথড
এই মেথডটির কাজ হলো—ডিকশনারিতে নির্দিষ্ট কোনো কি (Key) আগে থেকে আছে কি না তা চেক করা।
যদি থাকে, তবে তার বর্তমান ভ্যালু রিটার্ন করে। আর যদি না থাকে, 
তবে যে ডিফল্ট ভ্যালু দেবেন সেটি সহ নতুন কি-টি ডিকশনারিতে যুক্ত করে দেয়!


student = {
  'name': 'Abdullah',
  'age': 30,
  'cgpa': 3.63
}

print("Before setdefault:", student)

# 1. Key ALREADY exists ('age' is already in the dict)
# It will return the existing value (30) and do NOT change anything.
returned_age = student.setdefault("age", 25)
print("Returned age for existing key:", returned_age)

# 2. Key does NOT exist ('course' is not in the dict)
# It will add "course": "Python Backend" to the dictionary and return it.
returned_course = student.setdefault("course", "Python Backend")
print("Returned value for new key:", returned_course)

print("After setdefault:", student)



user = {"name": "Abdullah", "role": "student"}

# ১. "role" কি-টি ডিকশনারিতে আগে থেকেই আছে, তাই সেটির বর্তমান ভ্যালুই দেখাবে
print(user.setdefault("role", "admin"))  # আউটপুট: student

# ২. "city" কি-টি ডিকশনারিতে নেই, তাই এটি ডিকশনারিতে যোগ হয়ে যাবে এবং "Dhaka" রিটার্ন করবে
print(user.setdefault("city", "Dhaka"))  # আউটপুট: Dhaka

print(user)
# আউটপুট: {'name': 'Abdullah', 'role': 'student', 'city': 'Dhaka'}


বিশেষ করে যখন ডাটা কাউন্ট (Counting) করতে হয় অথবা গ্রুপিং (Grouping) করতে হয়, 
তখন বারবার if-else লেখার ঝামেলা এটি এক লাইনে মিটিয়ে দেয়।





ফ্রিকোয়েন্সি কাউন্টার বা ডেটা গোনা (Frequency Count)
সার্ভারে বিভিন্ন ইউজার লগইন করছে এবং তাদের রোল (admin, user) ট্র্যাক করা হচ্ছে। এখন দেখতে চান কোন রোল কয়বার এসেছে।

setdefault() না থাকলে বারবার চেক করতে হতো রোলটি ডিকশনারিতে আগে থেকেই আছে কি না। 
কিন্তু এটি দিয়ে কাজটি পানির মতো সহজ হয়ে যায়:


# লগইন করা ইউজারদের রোলগুলোর একটি লিস্ট
roles = ["admin", "user", "admin", "moderator", "user", "admin"]

role_count = {}

for role in roles:
    # যদি 'role' কি-টি ডিকশনারিতে না থাকে, তবে ডিফল্ট ভ্যালু 0 সেট করে দিবে
    role_count.setdefault(role, 0)
    
    # এরপর সেই রোলের কাউন্ট ১ বাড়িয়ে দেবে
    role_count[role] += 1

print(role_count)

{'admin': 3, 'user': 2, 'moderator': 1}
এখানে .setdefault(role, 0) পাইথনকে বলে দিয়েছে: "যদি এই নামের কোনো কি না থাকে, 
তবে তাকে 0 বানিয়ে শুরু করো। আর থাকলে তো কথাই নেই!"



ডেটা গ্রুপিং করা (Grouping Data)
ব্যাকএন্ডে ডাটাবেজ থেকে ডেটা এনে অনেক সময় ক্যাটাগরি অনুযায়ী সাজাতে (Group by) হয়। যেমন—কোন সিটিতে কোন কোন ইউজার আছে, তাদের একটি লিস্টে সাজানো:

users = [
    {"name": "Rahim", "city": "Dhaka"},
    {"name": "Karim", "city": "Sylhet"},
    {"name": "Jabbar", "city": "Dhaka"},
    {"name": "Salma", "city": "Sylhet"}
]

city_groups = {}

for user in users:
    city = user["city"]
    name = user["name"]
    
    # যদি সিটির নামে কোনো কি না থাকে, তবে একটি খালি লিস্ট `[]` বানিয়ে দিবে
    city_groups.setdefault(city, []).append(name)

print(city_groups)

{'Dhaka': ['Rahim', 'Jabbar'], 'Sylhet': ['Karim', 'Salma']}

এখানে .setdefault(city, []) এর মাধ্যমে প্রথমবার যখন নতুন সিটি (যেমন: "Dhaka") পাওয়া গেছে, 
তখন পাইথন স্বয়ংক্রিয়ভাবে একটি খালি লিস্ট [] বানিয়ে দিয়েছে, আর .append(name) দিয়ে সাথে সাথে সেই লিস্টে ইউজারের নাম ঢুকিয়ে দেওয়া হয়েছে!



.copy() মেথড
আপনি যদি চান মূল ডিকশনারিটি অক্ষত রেখে সেটির একটি হুবহু আলাদা কপি তৈরি করতে,
তবে .copy() ব্যবহার করতে হয়। এতে মূল ডিকশনারিতে কোনো পরিবর্তন না করে নতুন কপিতে কাজ করা যায়।


original = {"a": 1, "b": 2}

# একটি নতুন কপি তৈরি করা হলো
clone = original.copy()

print(clone)
# আউটপুট: {'a': 1, 'b': 2}






popitem()  Method

ডিকশনারির .popitem() মেথডটি খুবই চমৎকার এবং দরকারী একটি মেথড। 
এর মূল কাজ হলো ডিকশনারি থেকে সর্বশেষ (Last) Key-Value জোড়াটিকে 
রিমুভ বা ডিলিট করে ফেলা এবং সেই রিমুভ করা জোড়াটি একটি টুপল (Tuple) আকারে রিটার্ন করা।

পাইথনের আধুনিক সংস্করণগুলোতে (Python 3.7+) ডিকশনারি যেহেতু অর্ডার বা ক্রম মনে রাখে,
তাই .popitem() সবসময় ডিকশনারির একদম শেষের উপাদানটিকেই ধরে রিমুভ করে।


student = {
    "name": "Abdullah",
    "age": 22,
    "cgpa": 3.75
}

# .popitem() ব্যবহার করে শেষের উপাদানটি ডিলিট করা হলো
removed_item = student.popitem()

print("রিমুভ হওয়া উপাদান:", removed_item)
print("বর্তমান ডিকশনারি:", student)


রিমুভ হওয়া উপাদান: ('cgpa', 3.75)
বর্তমান ডিকশনারি: {'name': 'Abdullah', 'age': 22}

একটি সতর্কতা: যদি ডিকশনারিটি একদম খালি ({}) থাকে এবং তখন .popitem() কল করেন
, তবে পাইথন KeyError বা এরর দেখাবে। তাই খালি ডিকশনারিতে এটি ব্যবহার করার আগে চেক করে নেওয়া ভালো।



ব্রাউজার হিস্ট্রি বা আনডো (Undo) সিস্টেম
ধরুন এমন একটি প্রোগ্রাম বানাচ্ছেন যেখানে ইউজারের অ্যাক্টিভিটিগুলো একে একে সেভ হচ্ছে। 
ইউজার যখন Undo বা পেছনের ধাপে যেতে চাইবে, তখন সবচেয়ে শেষের বা সাম্প্রতিক কাজটি রিমুভ করতে হবে।


# ইউজারের কাজের হিস্ট্রি (সবার শেষে যেটা হয়েছে, সেটাই সবচেয়ে লেটেস্ট)
user_history = {
    "step_1": "Opened profile",
    "step_2": "Updated email",
    "step_3": "Clicked submit"
}

# ইউজার ব্যাক বা Undo করতে চাইল, তাই শেষের অ্যাকশনটি পপ করে ফেলা হলো
last_action = user_history.popitem()

print("বাতিল হওয়া কাজ:", last_action)
print("বাকি হিস্ট্রি:", user_history)


বাতিল হওয়া কাজ: ('step_3', 'Clicked submit')
বাকি হিস্ট্রি: {'step_1': 'Opened profile', 'step_2': 'Updated email'}


লুপ চালিয়ে ডিকশনারি এক এক করে খালি করা (Processing Queue)
অনেক সময় ডিকশনারির ভেতরে অনেকগুলো টাস্ক বা ডেটা জমা থাকে। আপনি যদি চান শেষ থেকে 
একটি একটি করে টাস্ক বের করে প্রসেস করতে এবং সাথে সাথে ডিকশনারিটিকে ছোট (খালি) করতে, তবে while লুপের সাথে .popitem() ব্যবহার করা যায়:


# প্রসেস করার জন্য কিছু টাস্ক ডিকশনারিতে রাখা আছে
tasks = {
    "task_A": "Send Email",
    "task_B": "Generate PDF",
    "task_C": "Save to Database"
}

print("--- টাস্ক প্রসেসিং শুরু ---")

# ডিকশনারি খালি না হওয়া পর্যন্ত লুপ চলতে থাকবে
while len(tasks) > 0:
    task_key, task_name = tasks.popitem()
    print(f"প্রসেস হচ্ছে: {task_key} -> {task_name}")

print("সব টাস্ক শেষ! বর্তমান ডিকশনারি:", tasks)


--- টাস্ক প্রসেসিং শুরু ---
প্রসেস হচ্ছে: task_C -> Save to Database
প্রসেস হচ্ছে: task_B -> Generate PDF
প্রসেস হচ্ছে: task_A -> Send Email
সব টাস্ক শেষ! বর্তমান ডিকশনারি: {}





পাইথনের del হলো একটি বিল্ট-ইন কি-ওয়ার্ড (Keyword বা Statement), ডিকশনারির কোনো মেথড নয়। এটি ব্যবহার করে 
ডিকশনারির নির্দিষ্ট কোনো Key-Value জোড়া একেবারে মুছে ফেলতে পারেন, অথবা চাইলে পুরো ডিকশনারি ভেরিয়েবলটিকেই মেমোরি থেকে ডিলিট করে দিতে পারেন।

.pop() এবং del-এর মূল পার্থক্য হলো: .pop() ডিলিট করার পর মুছে ফেলা ভ্যালুটি রিটার্ন করে, কিন্তু del কোনো কিছু রিটার্ন করে না—সে শুধু সাইলেন্টলি ডিলিট করে দেয়।


ডিকশনারি থেকে নির্দিষ্ট Key-Value ডিলিট করা
আপনি যদি ডিকশনারির কোনো নির্দিষ্ট কি ধরে ডিলিট করতে চান, তবে del ডিকশনারির_নাম[কি] এভাবে লিখতে হয়।



student = {
    "name": "Abdullah",
    "age": 22,
    "cgpa": 3.75
}

# "age" কি এবং তার ভ্যালু ডিলিট করা হলো
del student["age"]

print(student)

{'name': 'Abdullah', 'cgpa': 3.75}

সাবধানতা: ভুল Key দিলে কী হবে?
 যদি এমন কোনো Key ডিলিট করতে চান যেটি আদতেই ডিকশনারিতে নেই, তবে পাইথন KeyError বা এরর দিয়ে কোড থামিয়ে দেবে।

student = {"name": "Abdullah"}

# "address" ডিকশনারিতে নেই, তাই এরর আসবে
del student["address"]  # KeyError: 'address'

(এই কারণে ডিলিট করার আগে if "address" in student: চেক করে নেওয়া নিরাপদ।)


পুরো ডিকশনারি ভেরিয়েবলটিই মুছে ফেলা
 যদি চান ডিকশনারির ভেতরে কিছু না রেখে পুরো ডিকশনারিটাই কম্পিউটার বা পাইথনের 
মেমোরি থেকে মুছে ফেলবেন, তবে সরাসরি del এর সাথে ভেরিয়েবলের নাম দিয়ে দিতে পারেন।


student = {"name": "Abdullah", "age": 22}

# পুরো ডিকশনারি ভেরিয়েবলটি ডিলিট করে দেওয়া হলো
del student

# এখন যদি প্রিন্ট করতে যান, তবে NameError আসবে কারণ student নামে আর কোনো ভেরিয়েবল নেই
print(student)  # NameError: name 'student' is not defined


সংক্ষেপে মনে রাখার নিয়ম:
নির্দিষ্ট কি রিমুভ করতে: del student["key_name"]

পুরো ডিকশনারি মুছে ফেলতে: del student

ডিলিট করা ভ্যালুটা যদি নিজের কাজে লাগাতে চান: student.pop("key_name")








ডিকশনারি থেকে ডেটা ডিলিট করা (pop(), popitem(), del)

pop(key): নির্দিষ্ট কোনো Key এবং তার মান মুছে ফেলতে।

popitem(): পাইথনের সাম্প্রতিক ভার্সনগুলোতে ডিকশনারির শেষের দিক থেকে যেকোনো একটি আইটেম (Key-Value জোড়া) ডিলিট করে দেয়।

del keyword: নির্দিষ্ট কি ধরে ডিলিট করতে।


pop() — নির্দিষ্ট key সরিয়ে তার value রিটার্ন করা

person = {"name": "Rahim", "age": 25, "city": "Dhaka"}

removed_value = person.pop("age")
print(removed_value)  # 25
print(person)         # {'name': 'Rahim', 'city': 'Dhaka'}

কাজ কী: নির্দিষ্ট কোনো Key এবং তার সাথে থাকা মানটি ডিকশনারি থেকে মুছে ফেলতে এটি ব্যবহার করা হয়। এছাড়া মুছে ফেলা মানটি 
চাইলে একটি ভ্যারিয়েবলে ধরেও রাখা যায়।

profile = {
    "name": "Abdullah",
    "age": 30,
    "city": "Dhaka"
}

# নির্দিষ্ট 'age' কি ডিলিট করা হচ্ছে
removed_val = profile.pop("age")

print("মুছে ফেলা মান:", removed_val)  # আউটপুট: 30
print("ডিকশনারি:", profile)          # আউটপুট: {'name': 'Abdullah', 'city': 'Dhaka'}




popitem() — সর্বশেষ যোগ হওয়া key-value জোড়া সরানো

কাজ কী: পাইথনের সাম্প্রতিক ভার্সনগুলোতে (Python 3.7+) ডিকশনারির একদম শেষের দিকে থাকা আইটেমটি (একটি Key-Value জোড়া) ডিলিট করে দেয় 
এবং সেটি একটি টাপল আকারে রিটার্ন করে। এখানে আলাদা করে কোনো কি-র নাম বলে দিতে হয় না।


person = {"name": "Rahim", "age": 25, "city": "Dhaka"}

last_item = person.popitem()
print(last_item)  # ('city', 'Dhaka')
print(person)      # {'name': 'Rahim', 'age': 25}



# একটি গাড়ির ডিকশনারি
car = {
    "brand": "Toyota",
    "model": "Premio",
    "year": 2018
}

# popitem() কল করলে একদম শেষের জোড়া ('year': 2018) ডিলিট হয়ে যাবে
deleted_item = car.popitem()

print("যে জোড়াটি মুছে গেছে:", deleted_item)  # আউটপুট: ('year', 2018)
print("ডিকশনারি এখন যেমন আছে:", car) 
# আউটপুট: {'brand': 'Toyota', 'model': 'Premio'}



del — key দিয়ে item মুছে ফেলা
কাজ কী: এটি কোনো ফাংশন বা মেথড নয়, পাইথনের একটি বিল্ট-ইন কিওয়ার্ড। সুনির্দিষ্ট কোনো Key ধরে ডিকশনারি থেকে ডেটা মুছে ফেলতে এটি ব্যবহৃত হয়।
(pop() এর মতো এটি মুছে ফেলা মান রিটার্ন করে না, সরাসরি ডিকশনারি থেকে উড়িয়ে দেয়)।


person = {"name": "Rahim", "age": 25}
del person["age"]
print(person)  # {'name': 'Rahim'}


# একটি পণ্যের ডিকশনারি
product = {
    "id": 101,
    "title": "Laptop",
    "price": 45000,
    "stock": 10
}

# del কিওয়ার্ড ব্যবহার করে 'price' কি-টি মুছে ফেলা হচ্ছে
del product["price"]

print("ডিকশনারি এখন যেমন আছে:", product) 
# আউটপুট: {'id': 101, 'title': 'Laptop', 'stock': 10}



clear() — পুরো dictionary খালি করা

person = {"name": "Rahim", "age": 25}
person.clear()
print(person)  # {}

নির্দিষ্ট কোনো Key এর নাম ধরে ডিলিট করতে  pop(key) বা del ব্যবহার করা লাগবে ।
কোনো নাম না দিয়ে ডিকশনারির একদম শেষের জোড়াটি উড়িয়ে দিতে popitem() ব্যবহার করা লাগবে।







Dictionary এর তিনটা গুরুত্বপূর্ণ View — keys(), values(), items() ডিকশনারি থেকে কি, ভ্যালু বা দুটোই একসাথে লুপ চালিয়ে বের করার জন্য চমৎকার কিছু মেথড


keys() — সব key এর তালিকা keys() মেথড


ডিকশনারির ভেতরে যতগুলো চাবি বা Key আছে, শুধু সেগুলোকে আলাদা করে বের করে আনতে এটি ব্যবহার করা হয়।


person = {"name": "Rahim", "age": 25, "city": "Dhaka"}
print(person.keys())    # dict_keys(['name', 'age', 'city'])



student = {"name": "Rahim", "age": 22, "cgpa": 3.75}

# শুধু কি-গুলো দেখতে:
for key in student.keys():
    print(key)

# শুধু ভ্যালুগুলো দেখতে:
for val in student.values():
    print(val)

# কি এবং ভ্যালু একসাথে (সবচেয়ে বেশি ব্যবহৃত):
for key, value in student.items():
    print(key, "-->", value)




# Abdullah-র তথ্য সম্বলিত ডিকশনারি
abdullah_info = {
    "name": "Abdullah",
    "age": 30,
    "profession": "Engineer"
}

# শুধু কি (Keys) গুলো বের করা হচ্ছে
all_keys = abdullah_info.keys()

print("ডিকশনারির সব কি (Keys):", all_keys)
# আউটপুট: dict_keys(['name', 'age', 'profession'])


কাজের সময় অনেক সময় শুধু কি-গুলোর ওপর লুপ চালিয়ে কাজ করতে হয়।
যেমন, আব্দুল্লাহর প্রোফাইলে কী কী ফিল্ড বা ইনফরমেশন সেভ করা আছে তা চেক করা:

abdullah_profile = {
    "name": "Abdullah",
    "age": 30,
    "city": "Sylhet",
    "status": "Active"
}

print("আব্দুল্লাহর প্রোফাইলের ফিল্ডগুলোর নাম:")
for key in abdullah_profile.keys():
    print("-", key)


আব্দুল্লাহর প্রোফাইলের ফিল্ডগুলোর নাম:
- name
- age
- city
- status





values() — সব value এর তালিকা 
ডিকশনারির কি-গুলোর বিপরীতে যে মান বা Values গুলো জমা আছে, শুধু সেগুলোকে আলাদা করে বের করতে এটি ব্যবহার করা হয়।


person = {"name": "Rahim", "age": 25, "city": "Dhaka"}
print(person.values())  # dict_values(['Rahim', 25, 'Dhaka'])


# Abdullah-র তথ্য সম্বলিত ডিকশনারি
abdullah_info = {
    "name": "Abdullah",
    "age": 30,
    "profession": "Engineer"
}

# শুধু মান (Values) গুলো বের করা হচ্ছে
all_values = abdullah_info.values()

print("ডিকশনারির সব মান (Values):", all_values)
# আউটপুট: dict_values(['Abdullah', 30, 'Engineer'])



আব্দুল্লাহর প্রোফাইলে কী কী ভ্যালু বা তথ্য ইনপুট দেওয়া আছে (কি বা নাম বাদ দিয়ে):


abdullah_details = {
    "name": "Abdullah",
    "age": 30,
    "skill": "Python",
    "country": "Bangladesh"
}

print("আব্দুল্লাহর প্রোফাইলের ভেতরের মানগুলো:")
for val in abdullah_details.values():
    print(">", val)


আব্দুল্লাহর প্রোফাইলের ভেতরের মানগুলো:
> Abdullah
> 30
> Python
> Bangladesh




items() মেথডের উদাহরণ

ডিকশনারির প্রতিটি Key এবং Value জোড়ায় জোড়ায় (Tuple আকারে) একসাথে বের করে আনতে এটি ব্যবহার করা হয়। 
লুপ চালানোর সময় এটি সবচেয়ে বেশি কাজে লাগে।

person = {"name": "Rahim", "age": 25, "city": "Dhaka"}

print(person.values())  # dict_values(['Rahim', 25, 'Dhaka'])



# Abdullah-র তথ্য সম্বলিত ডিকশনারি
abdullah_info = {
    "name": "Abdullah",
    "age": 30,
    "profession": "Engineer"
}

# কি এবং মান একসাথে (Items) বের করা হচ্ছে
all_items = abdullah_info.items()

print("ডিকশনারির সব জোড়া (Items):", all_items)
# আউটপুট: dict_items([('name', 'Abdullah'), ('age', 30), ('profession', 'Engineer')])


সবচেয়ে চমৎকার ব্যবহার হলো items() দিয়ে লুপ চালিয়ে একবারে কি এবং ভ্যালু সুন্দর ফরম্যাটে প্রিন্ট করা:

abdullah_bio = {
    "name": "Abdullah",
    "age": 30,
    "profession": "Developer",
    "score": 95
}

print("--- আব্দুল্লাহর বায়োডাটা ---")
for key, value in abdullah_bio.items():
    print(f"{key} : {value}")

--- আব্দুল্লাহর বায়োডাটা ---
name : Abdullah
age : 30
profession : Developer
score : 95






অ্যাডভান্সড লেভেল - নেস্টেড ডিকশনারি ও ডিকশনারি কমপ্রিহেনশন (Advanced Level)

১. নেস্টেড ডিকশনারি (Nested Dictionary):
একটি ডিকশনারির ভেতরের ভ্যালু হিসেবে যদি আরেকটি ডিকশনারি বসিয়ে দেওয়া হয়, তাকে নেস্টেড ডিকশনারি বলে। 
রিয়েল-ওয়ার্ল্ড প্রজেক্টে (যেমন: ডাটাবেজ বা জেসন ডেটা হ্যান্ডেলিংয়ে) এটি প্রচুর ব্যবহার করা হয়।

# একটি ক্লাসের একাধিক ছাত্রের তথ্য রাখার নেস্টেড ডিকশনারি
classroom = {
    "student_1": {"name": "Rahim", "age": 22},
    "student_2": {"name": "Karim", "age": 23}
}

# করিমের বয়স দেখতে চাইলে:
print(classroom["student_2"]["age"])  # আউটপুট: 23



২. ডিকশনারি কমপ্রিহেনশন (Dictionary Comprehension):
এক লাইনে লজিক লিখে খুব দ্রুত নতুন ডিকশনারি তৈরি করার আধুনিক পাইথন পদ্ধতি। যেমন, ১ থেকে ৫ পর্যন্ত সংখ্যাগুলোর স্কয়ার বা বর্গ বের করে একটি ডিকশনারি বানাতে হবে:


# এক লাইনে ডিকশনারি কমপ্রিহেনশন
squares = {x: x**2 for x in range(1, 6)}

print(squares)
# আউটপুট: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


 আন্ডার দ্য হুড মেকানিজম ও স্পিড (Under the Hood)কম্পিউটার সায়েন্সের দৃষ্টিকোণ থেকে ডিকশনারি হলো পাইথনের সবচেয়ে পাওয়ারফুল ডেটা স্ট্রাকচার।
 হাশ টেবিল (Hash Table): সেটের মতো ডিকশনারিও ইন্টারনালি হাশ টেবিল অ্যালগরিদম ব্যবহার করে। 
 এর ফলে যেকোনো Key দিয়ে তার Value খুঁজতে বা চেক করতে সুপার ফাস্ট সময় লাগে—যার টাইম কমপ্লেক্সিটি হলো O(1) (Constant Time)। 
 লাখ লাখ ডেটার ভেতর থেকেও ডিকশনারির কি মুহূর্তের মধ্যে খুঁজে পাওয়া যায়।
 Immutable Keys: ডিকশনারির Key হিসেবে সবসময় এমন ডেটা দিতে হয় যা পরিবর্তন করা যায় না (যেমন: String, Number, Tuple)।
 লিস্ট (List) মিউটেবল হওয়ায় ডিকশনারির Key হিসেবে ব্যবহার করা যায় না, দিলেই পাইথন TypeError দিবে।





 in দিয়ে Key আছে কিনা চেক করা

 person = {"name": "Rahim", "age": 25}

print("name" in person)      # True
print("salary" in person)    # False




Dictionary এর দৈর্ঘ্য বের করা


person = {"name": "Rahim", "age": 25, "city": "Dhaka"}
print(len(person))  # 3  (মোট কতগুলো key-value জোড়া আছে)



update() — একাধিক Key-Value একসাথে যোগ/পরিবর্তন করা

person = {"name": "Rahim", "age": 25}

person.update({"age": 26, "city": "Dhaka"})
print(person)  # {'name': 'Rahim', 'age': 26, 'city': 'Dhaka'}
age আগে থেকেই ছিল, তাই সেটা পরিবর্তন হয়েছে (26 হয়েছে), আর city নতুন ছিল, তাই যোগ হয়েছে।




Nested Dictionary (Dictionary এর ভিতরে Dictionary) — Advanced

students = {
    "student1": {"name": "Rahim", "age": 22},
    "student2": {"name": "Karim", "age": 23}
}

print(students["student1"])           # {'name': 'Rahim', 'age': 22}
print(students["student1"]["name"])   # Rahim

এটা backend/API কাজে খুবই common — একটা user এর ভিতরে আরও sub-detail (যেমন address, permissions) রাখতে হলে nested dictionary ব্যবহার হয়।




Dictionary এর ভিতরে List, List এর ভিতরে Dictionary — Advanced

company = {
    "name": "TechCorp",
    "employees": ["Rahim", "Karim", "Salma"]
}

print(company["employees"])      # ['Rahim', 'Karim', 'Salma']
print(company["employees"][0])   # Rahim


students = [
    {"name": "Rahim", "age": 22},
    {"name": "Karim", "age": 23}
]

for student in students:
    print(student["name"])

Rahim
Karim



Dictionary Comprehension — Advanced (এক লাইনে Dictionary তৈরি)

numbers = [1, 2, 3, 4, 5]

squares = {n: n**2 for n in numbers}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}



শর্ত (condition) সহ:

numbers = [1, 2, 3, 4, 5, 6]

even_squares = {n: n**2 for n in numbers if n % 2 == 0}
print(even_squares)  # {2: 4, 4: 16, 6: 36}





Dictionary Copy করা — গুরুত্বপূর্ণ সতর্কতা (List এর মতোই সমস্যা)

dict1 = {"a": 1, "b": 2}
dict2 = dict1        # ⚠️ এটা copy না, একই dictionary কে point করছে!

dict2["c"] = 3
print(dict1)  # {'a': 1, 'b': 2, 'c': 3}  -> dict1 ও পরিবর্তন হয়ে গেছে!

সঠিক copy করার পদ্ধতি:

dict1 = {"a": 1, "b": 2}
dict2 = dict1.copy()

dict2["c"] = 3
print(dict1)  # {'a': 1, 'b': 2}     -> অপরিবর্তিত
print(dict2)  # {'a': 1, 'b': 2, 'c': 3}




Key হিসেবে কী কী ব্যবহার করা যায় (Rule)

Dictionary এর key অবশ্যই immutable ডেটা টাইপ হতে হবে — যেমন string, number, tuple। 
কিন্তু list বা dictionary key হিসেবে ব্যবহার করা যায় না(কারণ এগুলো mutable)।


valid = {1: "one", "two": 2, (1, 2): "tuple key"}   # ঠিক আছে

invalid = {[1, 2]: "list key"}   # TypeError: unhashable type: 'list'

value হিসেবে যেকোনো ডেটা টাইপ ব্যবহার করা যায় (list, dictionary, এমনকি function-ও)।




fromkeys() — একই value দিয়ে একাধিক key তৈরি করা

keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print(default_dict)  # {'a': 0, 'b': 0, 'c': 0}




setdefault() — Key থাকলে value নেয়, না থাকলে নতুন যোগ করে

person = {"name": "Rahim"}

age = person.setdefault("age", 18)
print(age)      # 18  (নতুন key যোগ হয়েছে, ডিফল্ট মান দিয়ে)
print(person)   # {'name': 'Rahim', 'age': 18}

name = person.setdefault("name", "Unknown")
print(name)     # Rahim  (আগে থেকেই ছিল, তাই পুরনো মানই থাকে)



Dictionary Sorting — Advanced

Dictionary নিজে থেকে সাজানো যায় না (কারণ Python 3.7+ এ order insertion অনুযায়ী থাকে, কিন্তু sort মেথড নেই), 
তবে sorted() ফাংশন ব্যবহার করে sorted করা যায়:


marks = {"Rahim": 85, "Karim": 92, "Salma": 78}

# Key অনুযায়ী সাজানো
sorted_by_key = dict(sorted(marks.items()))
print(sorted_by_key)  # {'Karim': 92, 'Rahim': 85, 'Salma': 78}

# Value অনুযায়ী সাজানো
sorted_by_value = dict(sorted(marks.items(), key=lambda x: x[1]))
print(sorted_by_value)  # {'Salma': 78, 'Rahim': 85, 'Karim': 92}




কতবার কোনো শব্দ এসেছে গোনা (Word Count)

text = "apple banana apple mango banana apple"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)  # {'apple': 3, 'banana': 2, 'mango': 1}




Simple Database এর মতো ব্যবহার (in-memory storage)

users_db = {
    1: {"name": "Rahim", "email": "rahim@email.com"},
    2: {"name": "Karim", "email": "karim@email.com"}
}

user_id = 1
print(users_db[user_id]["name"])  # Rahim




সাধারণ ভুল (Common Mistakes)


# ভুল ১: না থাকা key সরাসরি access করা
person = {"name": "Rahim"}
print(person["age"])   # KeyError

# ভুল ২: mutable জিনিস (list) কে key হিসেবে ব্যবহার
d = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'

# ভুল ৩: dict copy না করে সরাসরি assign করে ভাবা এটা আলাদা
d1 = {"a": 1}
d2 = d1        # copy না!

# ভুল ৪: খালি dict ভেবে {} লেখা, কিন্তু ভুলে set এর সাথে গুলিয়ে ফেলা
empty = {}     # এটা dict, set না



dict()------

পাইথনে dict() হলো একটি বিল্ট-ইন ফাংশন বা কনস্ট্রাক্টর, যার প্রধান কাজ হলো 
একটি নতুন ডিকশনারি তৈরি করা অথবা অন্য কোনো ডেটা টাইপকে ডিকশনারিতে রূপান্তর (convert) করা।
এটি সাধারণত ৩টি ভিন্ন উপায়ে ব্যবহার করা হয়:



১. খালি ডিকশনারি তৈরি করতে
কোনো ডেটা ছাড়াই একটি ফাঁকা ডিকশনারি তৈরি করতে এটি ব্যবহার করা যায় 
(যদিও {} ব্র্যাকেট দিয়েও ফাঁকা ডিকশনারি বানানো যায়):খালি ডিকশনারি তৈরি করার জন্য পাইথনে মূলত দুটি জনপ্রিয় উপায় রয়েছে


এটি ডিকশনারি তৈরি করার সবচেয়ে সহজ এবং সবচেয়ে বেশি ব্যবহৃত পদ্ধতি। কোনো ডেটা না দিয়ে শুধু ফাঁকা জোড়া ব্র্যাকেট দিলেই পাইথন বুঝে নেয় এটি একটি খালি ডিকশনারি।

উদাহরণ ১:

# একটি খালি ডিকশনারি তৈরি করা
empty_dict_1 = {}

# এটি যে সত্যিই ডিকশনারি, তা টাইপ চেক করে দেখা
print(type(empty_dict_1)) 
# আউটপুট: 

print(empty_dict_1) 
# আউটপুট: {}



উদাহরণ ২: dict() কনস্ট্রাক্টর ফাংশন ব্যবহার করে 
এটি পাইথনের বিল্ট-ইন ফাংশন। এর ভেতরে কোনো আর্গুমেন্ট না দিয়ে কল করলেই একটি খালি ডিকশনারি তৈরি হয়ে যায়।

# Creating an empty dictionary using dict()
empty_dict = dict()
print(empty_dict)  # Output: {}



# dict() ফাংশন ব্যবহার করে খালি ডিকশনারি তৈরি করা
empty_dict_2 = dict()

# এটিও যে ডিকশনারি, তা চেক করা
print(type(empty_dict_2)) 
# আউটপুট: 

print(empty_dict_2) 
# আউটপুট: {}




২. কি-ওয়ার্ড আর্গুমেন্ট (Keyword Arguments) দিয়ে 

এই পদ্ধতিতে dict() ফাংশনের ভেতরে সরাসরি কী (Key) এবং তার মান (Value) লিখে দেওয়া হয়। 
এখানে সবচেয়ে বড় সুবিধা হলো—Key-এর চারপাশে কোনো কোটেশন ("" বা '') দেওয়ার প্রয়োজন হয় না। 
পাইথন স্বয়ংক্রিয়ভাবে সেগুলোকে স্ট্রিং কি (String keys) হিসেবে ধরে নেয়।


student = dict(name="Abdullah", age=30, subject="Programming")
print(student)  
# Output: {'name': 'Abdullah', 'age': 30, 'subject': 'Programming'}


# dict() ফাংশনে কি-ওয়ার্ড আর্গুমেন্ট ব্যবহার করে ডিকশনারি তৈরি
student = dict(name="Arman", age=22, city="Dhaka", is_married=False)

print(student)
print(type(student))

১. কোটেশন লাগবে না: আপনি যখন সরাসরি লিখছেন name="Arman", 
তখন পাইথন নিজে থেকেই name-কে কি হিসেবে ধরে নেয়। তাই একে 'name' এভাবে লেখার দরকার নেই।
২. ভ্যালিড ভেরিয়েবল নেম: এই পদ্ধতিতে কি (Key)-এর নাম অবশ্যই পাইথনের ভেরিয়েবল নামকরণের নিয়ম মেনে চলতে হবে 
(যেমন—মাঝে কোনো স্পেস বা হাইফেন - থাকতে পারবে না, সংখ্যা দিয়ে শুরু হতে পারবে না)। 
যেমন: dict(first-name="Arman") লিখলে পাইথন SyntaxError দেবে। যদি স্পেস বা বিশেষ অক্ষর দিতে হয়, 
তবে  স্বাভাবিক পদ্ধতি ({"first name": "Arman"}) ব্যবহার করতে হবে।




৩. টিউপল বা লিস্টের জোড়া (Pairs) থেকে 

এই পদ্ধতিতে বাইরে একটি প্রধান লিস্ট বা টিউপল থাকে, আর তার ভেতরে ছোট ছোট জোড়া (Pairs) আকারে উপাদানগুলো সাজানো থাকে।
প্রতিটা জোড়ার প্রথম উপাদানটি হয় Key এবং দ্বিতীয় উপাদানটি হয় Value।


# Creating a dictionary from a list of tuples
pairs = [("name", "Abdullah"), ("age", 30), ("subject", "Programming")]
student = dict(pairs)
print(student)  
# Output: {'name': 'Abdullah', 'age': 30, 'subject': 'Programming'}

১. ভেতরের ডেটার গঠন: ভেতরের জোড়াগুলো সাধারণত টিউপল আকারে (("key", "value")) দেওয়া হয়,
তবে লিস্ট আকারেও (["key", "value"]) দেওয়া যেতে পারে।
২. কোথায় ব্যবহার করবেন: যখন কাছে ডেটাগুলো কোনো ফাইল, 
ডাটাবেস বা অন্য কোনো ফাংশন থেকে জোড়ায় জোড়ায় লিস্ট বা টিউপল আকারে আসবে, 
তখন সেগুলোকে সহজে ডিকশনারিতে রূপান্তর করার জন্য এটি সবচেয়ে কাজের পদ্ধতি।


লিস্টের ভেতরে লিস্ট (List of Lists) দিয়ে
এখানে মূল উপাদানটি একটি লিস্ট, আর তার ভেতরে প্রতিটি জোড়াও আলাদা আলাদা ছোট লিস্ট ([...]) আকারে আছে।

# লিস্টের ভেতরে লিস্ট আকারে ডেটা রাখা
car_pairs = [
    ["brand", "Toyota"],
    ["model", "Premio"],
    ["year", 2020]
]

# dict() কনস্ট্রাক্টর ব্যবহার করে ডিকশনারিতে রূপান্তর
car_dict = dict(car_pairs)

print(car_dict)
print(type(car_dict))

{'brand': 'Toyota', 'model': 'Premio', 'year': 2020}


টিউপলের ভেতরে টিউপল (Tuple of Tuples) দিয়ে
এখানে মূল উপাদানটি একটি টিউপল, আর তার ভেতরের জোড়াগুলোও টিউপল আকারে ((...)) সাজানো আছে।

# টিউপলের ভেতরে টিউপল আকারে ডেটা রাখা
laptop_pairs = (
    ("processor", "Core i5"),
    ("ram", "16GB"),
    ("ssd", "512GB")
)

# dict() কনস্ট্রাক্টর ব্যবহার করে ডিকশনারিতে রূপান্তর
laptop_dict = dict(laptop_pairs)

print(laptop_dict)
print(type(laptop_dict))

{'processor': 'Core i5', 'ram': '16GB', 'ssd': '512GB'}




১. লিস্টের ভেতরে লিস্ট (List of Lists)
এখানে মূল কালেকশনটি একটি লিস্ট এবং ভেতরের জোড়াগুলোও লিস্ট আকারে থাকে।

# Create dictionary from a list of lists
data = [["name", "Arman"], ["age", 25], ["city", "Dhaka"]]
result = dict(data)

print(result)



২. টিউপলের ভেতরে টিউপল (Tuple of Tuples)
এখানে মূল কালেকশনটি একটি টিউপল এবং ভেতরের জোড়াগুলোও টিউপল আকারে থাকে।

# Create dictionary from a tuple of tuples
data = (("id", 101), ("dept", "CSE"), ("cgpa", 3.85))
result = dict(data)

print(result)


৩. লিস্টের ভেতরে টিউপল (List of Tuples)
এখানে মূল কালেকশনটি একটি লিস্ট, কিন্তু ভেতরের জোড়াগুলো টিউপল আকারে থাকে। (এটি সবচেয়ে বেশি ব্যবহৃত হয়।)

# Create dictionary from a list of tuples
data = [("brand", "Dell"), ("price", 65000), ("in_stock", True)]
result = dict(data)

print(result)


৪. সেটের ভেতরে টিউপল (Set of Tuples)
যেহেতু সেটের উপাদানগুলোকে ইউনিক বা অদ্বিতীয় হতে হয়, তাই সেটের ভেতরে টিউপল জোড়া রেখেও ডিকশনারি বানাতে পারেন
(তবে লিস্ট রাখা যায় না, কারণ লিস্ট আনহ্যাসএবল)।

# Create dictionary from a set of tuples
data = {("x", 10), ("y", 20), ("z", 30)}
result = dict(data)

print(result)

সংক্ষেপে: পাইথনে ডিকশনারি তৈরির জন্য লিস্ট ([]), টিউপল (()) কিংবা সেট ({})—যেকোনো কালেকশন ব্যবহার করা যাবে,
যতক্ষণ না ভেতরের জোড়াগুলোর গঠন সঠিক থাকে (key, value)।
