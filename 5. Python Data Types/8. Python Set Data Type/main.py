Set কী?

পাইথনে Set হলো এমন একটি ডেটা স্ট্রাকচার, যা মূলত গণিতের 'সেট' (Set) এর ধারণার ওপর ভিত্তি করে তৈরি।

Set হলো পাইথনের একটা ডেটা টাইপ যেটা দিয়ে একাধিক জিনিস রাখা যায়, কিন্তু এর দুইটা বিশেষ বৈশিষ্ট্য আছে:

এর প্রধান দুটি জাদুকরী বৈশিষ্ট্য হলো:
১. সেটের ভেতর কোনো ডুপ্লিকেট বা একই মান দুইবার থাকতে পারে না। যদি ভুল করেও একই ডেটা বারবার রাখেন, পাইথন নিজে থেকেই ডিরেক্ট ডুপ্লিকেটগুলো মুছে ফেলবে।
২. সেটের কোনো নির্দিষ্ট ইনডেক্স বা সিরিয়াল নেই (Unordered)। তাই আপনি fruits[0] এভাবে ইনডেক্স দিয়ে কোনো আইটেম এক্সেস করতে পারবেন না।
কোনো নির্দিষ্ট ক্রম (order) থাকে না

Python-এ set (সেট) প্রধানত ২ প্রকার।

১. Mutable Set (পরিবর্তনযোগ্য সেট)এটি হলো সাধারণ set। এটি তৈরি করার পর এর উপাদানগুলো পরিবর্তন (যোগ বা বিয়োগ) করা যায়।
সিনট্যাক্স: my_set = {1, 2, 3} 
বৈশিষ্ট্য: এটি পরিবর্তনশীল (mutable)। 
তাই এতে নতুন উপাদান যোগ করতে add() বা বাদ দিতে remove() ব্যবহার করা যায়।


২. Immutable Set / Frozen Set (অপরিবর্তনযোগ্য সেট)পাইথনে একে frozenset বলা হয়। এটি তৈরি করার পর এর উপাদানগুলো আর পরিবর্তন করা যায় না।

সিনট্যাক্স: my_frozen_set = frozenset([1, 2, 3])
বৈশিষ্ট্য: এটি অপরিবর্তনশীল (immutable)। 
অর্থাৎ, একবার তৈরি করলে এতে নতুন কোনো উপাদান যোগ বা বিয়োগ করা সম্ভব নয়। 
এটি সাধারণত ডিকশনারির (dictionary) কি (key) হিসেবে ব্যবহারের জন্য উপযোগী।



১. সেটের সাথে মিল কোথায়?
সাধারণ সেটের মতোই frozenset-এ কোনো ডুপ্লিকেট উপাদান থাকে না।

সেটের মতোই এগুলোর কোনো নির্দিষ্ট ক্রম বা ইনডেক্স থাকে না।

গণিতের সেট অপারেশনগুলো (union, intersection, difference) এগুলোতেও খুব সুন্দরভাবে করা যায়।

২. পার্থক্য কোথায়? (Immutable কেন?)
সাধারণ সেট হলো mutable (পরিবর্তনশীল), তাই সেটে নতুন কিছু যোগ করার জন্য .add() বা বাদ দেওয়ার জন্য .remove() ব্যবহার করা যায়।

কিন্তু frozenset হলো immutable (অপরিবর্তনশীল)।
একবার এটি তৈরি করে ফেললে এর ভেতরে আর নতুন কিছু যোগ করা বা বাদ দেওয়া যায় না। আপনি যদি .add() করতে যান, পাইথন সাথে সাথে এরর দেবে।


# frozenset তৈরি করা
my_frozenset = frozenset(["apple", "banana", "mango"])
print(my_frozenset)

# এটি কাজ করবে না (Error দিবে) karena এটি immutable:
# my_frozenset.add("orange")


যেহেতু সাধারণ সেট পরিবর্তনশীল হওয়ায় হ্যাশ করা যায় না, তাই সেগুলোকে ডিকশনারির কি (dictionary key) বা অন্য কোনো সেটের উপাদান হিসেবে ব্যবহার করা যায় না।
কিন্তু frozenset অপরিবর্তনশীল হওয়ায় এগুলোকে ডিকশনারির কি বা আরেকটি সেটের ভেতরের আইটেম হিসেবে অনায়াসে ব্যবহার করা যায়।



সেট (Set) আনপ্যাক করা যায়! লিস্ট বা টুপলের মতোই সেটের উপাদানগুলোকেও ভেরিয়েবলে আনপ্যাক করা সম্ভব।

তবে এখানে একটি ছোট ব্যাপার মনে রাখতে হবে: সেটের তো কোনো নির্দিষ্ট ক্রম (order) বা ইনডেক্স থাকে না। 
তাই পাইথন যখন সেট আনপ্যাক করে, তখন সেটি এলোমেলো (random) বা যেকোনো অর্ডারে ভেরিয়েবলগুলোতে বসিয়ে দেয়।


সাধারণ আনপ্যাক করা (Star Operator * ছাড়া)
যদি সেটে যতটি উপাদান আছে, ঠিক ততটি ভেরিয়েবল বা চলক দেন, তবে এভাবে আনপ্যাক করতে:


my_set = {"apple", "banana", "mango"}

a, b, c = my_set
print(a)
print(b)
print(c)
# আউটপুট যেকোনো অর্ডারে আসতে পারে, কারণ সেটের কোনো নির্দিষ্ট সিরিয়াল নেই!


স্টার অপারেটর (*) দিয়ে আনপ্যাক করা
সেটের উপাদান সংখ্যা যদি বেশি হয় এবং নির্দিষ্ট কোনোটিকে আলাদা রেখে বাকিগুলোকে একটি লিস্টে রাখতে, তবে স্টার (*) অপারেটর ব্যবহার করতে

my_set = {"apple", "banana", "mango", "cherry"}

a, *rest = my_set

print(a)     # যেকোনো একটি আইটেম এখানে চলে আসবে
print(rest)  # বাকি আইটেমগুলো একটি লিস্ট আকারে এখানে চলে আসবে

লিস্ট বা টুপলের মতো সেটেও আনপ্যাক করা যায় (a, b, c = my_set)।

কিন্তু সেটের ক্ষেত্রে কোন ভেরিয়েবলে কোন আইটেমটি ঢুকবে তার কোনো নির্দিষ্ট গ্যারান্টি থাকে না, কারণ সেটের ডেটাগুলো এলোমেলোভাবে সাজানো থাকে।


পাইথনে যখনই আপনি স্টার বা অ্যাস্টারিস্ক (*) দিয়ে ভ্যারিয়েবল আনপ্যাক করবেন, 
তখন বাকি সব আইটেমগুলো সবসময় একটি List-এ পরিণত হয়ে যাবে—মূল কালেকশনটি সেট (set) হোক, টিউপল (tuple) হোক বা লিস্টই হোক না কেন।

এটি পাইথনের একটি বিল্ট-ইন রুল (Extended Iterable Unpacking Rule)। স্টার (*) ব্যবহার করলেই পাইথন বাই-ডিফল্ট সেটিকে লিস্ট হিসেবে স্টোর করে।



সংক্ষেপে: সেটে ইনডেক্স ([0]) বা ব্র্যাকেট কি (["apple"])—কোনোটি দিয়েই উপাদান এক্সেস করা যায় না!

১. [0] (ইনডেক্স দিয়ে এক্সেস করা) কেন কাজ করে না?
সেটের কোনো নির্দিষ্ট ক্রম (order) বা ইনডেক্স নেই। তাই লিস্টের মতো ইনডেক্স নম্বর দিয়ে (my_set[0]) সেটের কোনো উপাদান বের করা যায় না। 
এটি করতে গেলে পাইথন সাথে সাথে TypeError (যেমন: 'set' object is not subscriptable) দিয়ে কোড আটকে দেবে।

২. ["apple"] (ব্র্যাকেটে নাম দিয়ে খোঁজা) কেন কাজ করে না?
সেট কোনো ডিকশনারি (Dictionary) নয় যে এখানে কি (Key) এবং ভ্যালু (Value) জোড়ায় জোড়ায় থাকে। 
সেট হলো শুধুমাত্র কিছু ইউনিক উপাদানের কালেকশন। তাই ডিকশনারির 
মতো ব্র্যাকেটের ভেতর নাম লিখে my_set["apple"] এভাবে উপাদান এক্সেস করা যায় না। এটি করলেও TypeError আসবে।

তাহলে সেটের উপাদান কীভাবে চেক বা দেখতে হয়?
সেটের মান দেখার বা চেক করার সঠিক উপায়গুলো হলো:

লুপ চালিয়ে: for লুপ ব্যবহার করে সেটের সব উপাদান একে একে প্রিন্ট করা যায়।

চেক করার জন্য (in): কোনো নির্দিষ্ট উপাদান সেটে আছে কি না তা দেখতে in কিওয়ার্ড ব্যবহার করা হয়। যেমন:

my_set = {"apple", "banana", "mango"}
print("apple" in my_set)  # আউটপুট: True (কারণ এটি সেটে আছে)


vvi---------

পাইথনে কেন টুপল বা লিস্ট থেকে মান বের করার সময় () ব্যবহার করা হয় না—এর একটি খুব বড় এবং নির্দিষ্ট কারণ রয়েছে।
কারণটি হলো: গোল ব্র্যাকেট () পাইথনে ফাংশন কল করার জন্য রিজার্ভ করা থাকে।
১. ব্র্যাকেটের দ্বন্দ্ব (Conflict)
পাইথনে আমরা যখন কোনো ফাংশন রান বা কল করি, তখন সবসময় ব্র্যাকেট () ব্যবহার করি। যেমন:

print("Hello")

greet()

len(my_list)

এখন যদি পাইথন টুপল বা লিস্টের মান খোঁজার জন্য () ব্যবহার করার অনুমতি দিত (যেমন: my_tuple(0)), 
তাহলে পাইথনের কম্পাইলার বা ইন্টারপ্রেটার কনফিউজড হয়ে যেত। 
সে বুঝতে পারত না—এটি কি একটি ফাংশন কল করা হয়েছে, নাকি টুপলের কোনো ইনডেক্স খোঁজা হচ্ছে?

২. পাইথনের নিয়ম
এই বিভ্রান্তি দূর করার জন্যই পাইথনে কাজের ভাগ করে দেওয়া হয়েছে:

গোল ব্র্যাকেট (): শুধু ফাংশন কল করার জন্য এবং গাণিতিক হিসাবে অগ্রাধিকার (Order of operations) ঠিক করার জন্য।

স্কয়ার ব্র্যাকেট []: কালেকশনের ভেতর থেকে ইনডেক্স দিয়ে মান খোঁজা বা এক্সেস করার জন্য (যাকে প্রোগ্রামিংয়ে Subscripting বা Indexing বলা হয়)।

তাই লিস্ট বা টুপল ডিফাইন করার সময় বা মান বের করার সময় পাইথন সুনির্দিষ্ট নিয়ম মেনে চলে:

ডিফাইন করার সময়: my_tuple = (10, 20, 30)

মান বের করার সময়: my_tuple[0] ([] ব্র্যাকেট দিয়ে)


সব ডাটা টাইপের ক্ষেত্রে কিন্তু [] ব্যবহার করে মান বের করা যায় না।


লিস্ট ও টুপল (List & Tuple): ইনডেক্স বা পজিশন দিয়ে মান বের করতে [] লাগে।

উদাহরণ: my_list[0] বা my_tuple[1]

ডিকশনারি (Dictionary): কি (Key) বা নাম দিয়ে মান বের করতে [] লাগে।

উদাহরণ: my_dict["name"]

স্ট্রিং (String / Text): লেখার অক্ষর বা ক্যারেক্টার পজিশন দেখতে [] লাগে।

উদাহরণ: name[0]







Set তৈরি করা
Curly Bracket { } দিয়ে


fruits = {"apple", "banana", "mango"}
print(fruits)  # {'banana', 'apple', 'mango'}  -> ক্রম এলোমেলো হতে পারে

numbers = {1, 2, 3, 4, 5}
names = {"Rahim", "Karim", "Salma"}



Set তৈরি করার নিয়ম

Set লেখা হয় curly bracket { } দিয়ে (Dictionary এর মতোই দেখতে, কিন্তু ভিতরে শুধু value থাকে, key-value জোড়া না)।


⚠️ খালি Set — এখানে ভুল সবচেয়ে বেশি হয়

যদি ফাঁকা সেকেন্ড ব্র্যাকেট দিয়ে সেট বানাতে চাওয়া হয়:

empty_set = {}

তাহলে পাইথন এটিকে সেট হিসেবে ধরবে না, বরং একটি ডিকশনারি (Dictionary) হিসেবে ধরবে!

ফাঁকা সেট তৈরি করার সঠিক নিয়ম হলো set() ফাংশন ব্যবহার করা:

empty = {}
print(type(empty))   # <class 'dict'>  -> এটা Set না, Dictionary!

empty = set()
print(type(empty))   # <class 'set'>   -> সঠিক





data = {} এটি Set নয়। এটি Dictionary।

data = set()

print(type(data)) <class 'set'>

"কোনো কি-ভ্যালু পেয়ার থাকে না"

সহজ ভাষায় বলতে গেলে: ডিকশনারিতে ডেটা জমা হয় জোড়ায় জোড়ায় (Key-Value Pair), কিন্তু সেটে শুধু একা একা (Single Values) মান থাকে।

ডিকশনারির গঠন (Key-Value Pair সহ):
              
ডিকশনারিতে প্রতিটি মানের সাথে একটি করে চাবি বা কি (Key) জুড়ে দেওয়া থাকে। যেমন:

# এটি একটি ডিকশনারি (Dictionary)
student = {
    "name": "Abdullah",  # এখানে "name" হলো Key, আর "Abdullah" হলো Value
    "age": 30        # এখানে "age" হলো Key, আর 30 হলো Value
}

প্রতিটি মানের আগে একটি কোলন (:) দিয়ে তার একটি নাম বা কি (Key) দেওয়া আছে। একেই বলে Key-Value Pair (চাবি ও মানের জোড়া)।



সেটের গঠন (কোনো Key-Value Pair নেই):
           
এখন সেটের দিকে তাকান। সেটে কোনো জোড়া বা কোলন (:) থাকে না। সেখানে শুধু সরাসরি মানগুলো কমা দিয়ে বসিয়ে দেওয়া হয়:

# এটি একটি সেট (Set)
numbers = {10, 20, 30, 40}

এখানে শুধু সরাসরি সংখ্যাগুলো (10, 20, 30, 40) আছে। এদের আগে কোনো Key বা কোলন (:) নেই।



ঠিক একইভাবে স্ট্রিংয়ের সেট হতে পারে:

fruits = {"apple", "banana", "mango"}

এখানেও শুধু ফলের নামগুলো আছে, আলাদা কোনো কি-ভ্যালু জোড়া নেই।


⚠️ বিশেষ সতর্কতা (খুব গুরুত্বপূর্ণ ট্রিক):

যদি একদম ফাঁকা সেট বানাতে চাওয়া হয় , তবে ভুল করেও শুধু {} লিখা যাবে না! কারণ পাইথনে {} লিখলে সেটি সেট হিসেবে নয়,

বরং ডিকশনারি হিসেবে গণ্য হয়। ফাঁকা সেট বানাতে হয় এভাবে:

empty_set = set()  # এটি সঠিক ফাঁকা সেট

wrong_set = {}     # এটি আসলে একটি ফাঁকা ডিকশনারি (Dictionary)!


empty_set = {}

print(type(empty_set))  # <class 'dict'>  -> এটা set না, dictionary!

empty_set = set()

print(type(empty_set))  # <class 'set'>   -> সঠিক পদ্ধতি

শুধু {} লিখলে পাইথন এটাকে Dictionary ধরে নেয়, খালি Set বানাতে হলে অবশ্যই set() ফাংশন ব্যবহার করতে হবে।




List/Tuple থেকে Set তৈরি করা

my_list = [1, 2, 2, 3, 3]
my_set = set(my_list)
print(my_set)   # {1, 2, 3}




সেট আসলে কী এবং কেন এটি দরকার?

Set হলো পাইথনের এমন একটি বিল্ট-ইন ডেটা স্ট্রাকচার, যার দুটি প্রধান ও অপরিহার্য বৈশিষ্ট্য রয়েছে:

Unordered (ক্রমহীন): সেটের ভেতরের ডেটাগুলো কোনো নির্দিষ্ট ক্রমানুসারে মেমোরিতে সাজানো থাকে না। যেভাবে ডেটা রাখা হবে,
প্রিন্ট করার সময় সেটি উল্টাপাল্টা অর্ডারে আসতে পারে।

No Duplicates (ডুপ্লিকেট নিষিদ্ধ): সেটের ভেতরে কখনোই হুবহু এক ডেটা একাধিকবার থাকতে পারবে না।  যদি ভুলে একই মান ১০ বারও দেওয়া হয়, 
পাইথন নিজের বুদ্ধিমত্তায় বাকি ৯টি মুছে ফেলবে এবং শুধু ১টি রাখবে।

Set এর সবচেয়ে বড় বৈশিষ্ট্য — Duplicate নিজে থেকেই বাদ যায়

numbers = {1, 2, 2, 3, 4, 4, 5, 1}
print(numbers)  # আউটপুট: {1, 2, 3, 4, 5} (ডুপ্লিকেটগুলো নিজে থেকেই গায়েব!)

একই সংখ্যা একাধিকবার লিখলেও Set এ সেটা একবারই থাকে। এটা Set এর সবচেয়ে গুরুত্বপূর্ণ ও বেশি ব্যবহৃত বৈশিষ্ট্য।




সেট যেহেতু ইনডেক্স মেনে চলে না (যেমন: my_set[0] লিখলে এরর আসবে), তাই এর ডেটা পরিবর্তন,
যোগ বা বাদ দেওয়ার জন্য পাইথন কিছু স্পেশাল মেথড বা ফাংশন দেয়।
Index দিয়ে Access করা যায় না (কারণ Order নেই)

fruits = {"apple", "banana", "mango"}

print(fruits[0]) TypeError: 'set' object is not subscriptable

List/Tuple এর মতো Set এ index number দিয়ে item বের করা যায় না, কারণ Set এর ভিতরের item গুলোর কোনো নির্দিষ্ট ক্রম নেই — 

এলোমেলোভাবে (unordered) সংরক্ষিত থাকে। Order না থাকায় কোনো "প্রথম" বা "দ্বিতীয়" item বলে কিছু নেই।





১. সেটে নতুন উপাদান যোগ করা (add() এবং update())

লিস্টের মতো সেটেও নতুন উপাদান যোগ করা যায়, তবে এখানে .append() না বলে .add() ব্যবহার করা হয়:

add(): একটিমাত্র উপাদান সেটে যোগ করতে।

update(): একসাথে একাধিক উপাদান (যেমন: অন্য কোনো লিস্ট বা সেট) যুক্ত করতে।


fruits = {"apple", "banana"}

# ১টি উপাদান যোগ করা
fruits.add("orange")
print(fruits)  # আউটপুট: {'apple', 'orange', 'banana'} (অর্ডার এলোমেলো হতে পারে)


fruits = {"apple", "banana"}
fruits.add("mango")
print(fruits)  # {'apple', 'banana', 'mango'}

যদি আগে থেকেই থাকা মান আবার add() করা হয়, কিছুই পরিবর্তন হবে না (কারণ duplicate রাখা যায় না):
fruits.add("apple")  # কিছু হবে না, ইতিমধ্যে আছে 


colors = {"red", "green"}
colors.add("blue")

print(colors)  {'red', 'blue', 'green'}  # সিরিয়াল যেকোনোটা আগে-পিছে হতে পারে 


fruits_set = {"apple", "banana", "mango"}

fruits = fruits_set.add("kk")

print(fruits_set)

print(fruits) None
  
---

update() মেথডের কাজ কী?
পাইথনের সেটের (set) নিজস্ব একটি বিল্ট-ইন মেথড হলো .update()। 
এই মেথডের কাজ হলো যেকোনো ইটারেবল (Iterable) বা সংগ্রহ টাইপের ডেটা—
যেমন: List, Tuple, Set, বা Dictionary থেকে উপাদানগুলো নিয়ে মূল সেটের সাথে যুক্ত করা।



# একাধিক উপাদান (লিস্ট বা অন্য সেট) একসাথে যোগ করা update() — একাধিক item একসাথে যোগ করা


fruits_set = {"apple", "banana", "mango"}

fruits_set.update(["kk", "grape"])

print(fruits_set) 



my_set = {"apple"}

# লিস্ট থেকে যোগ করা
my_set.update(["banana", "mango"])

# টুপল থেকে যোগ করা
my_set.update(("cherry", "orange"))

print(my_set)
# আউটপুট সব উপাদান মিলে একটি সেট হয়ে যাবে (ক্রম এলোমেলো হতে পারে)




fruits_set = {"apple", "banana", "mango"}

kk = (("kk", "grape"))

fruits_set.update(kk)

print(fruits_set)


fruits = {"apple", "banana"}
fruits.update(["mango", "orange", "grape"])
print(fruits)  # {'apple', 'banana', 'mango', 'orange', 'grape'}

# প্রথমে একটি প্রাথমিক সেট তৈরি করা হলো
fruits = {"apple", "banana"}

# নতুন কিছু ফল লিস্ট আকারে একটি আলাদা ভেরিয়েবলে রাখা হলো
new_fruits = ["mango", "grape", "orange"]

# .update() মেথড দিয়ে একাধিক উপাদান একসাথে মূল সেটে যোগ করা হলো
fruits.update(new_fruits)

# আপডেট হওয়া সেটটি প্রিন্ট করা হচ্ছে
print(fruits)  {'apple', 'banana', 'mango', 'grape', 'orange'}


# মূল সেট
my_skills = {"python", "git"}
print("Original set:", my_skills)

# একটি লিস্ট যার মধ্যে নতুন স্কিল রয়েছে
new_skills_list = ["docker", "sql", "python"]

# update() ব্যবহার করে লিস্টের উপাদানগুলো সেটে যুক্ত করা হলো
my_skills.update(new_skills_list)

print("After update:", my_skills)

Original set: {'python', 'git'}
After update: {'git', 'python', 'docker', 'sql'}


দুটি ভিন্ন সেটের ডেটা মার্জ করা
দুটি আলাদা সেটকে একসাথে মিলিয়ে ফেলার জন্যও এটি ব্যবহৃত হয়।


# প্রাথমিক ফ্রেন্ডস লিস্ট
group_a = {"rahim", "karim"}
print("Group A:", group_a)

# নতুন ফ্রেন্ডস লিস্ট
group_b = {"tanvir", "salma"}

# group_a এর মধ্যে group_b এর উপাদানগুলো আপডেট করা হলো
group_a.update(group_b)

print("After updating Group A:", group_a)


add() দিয়ে সেটে একে একে শুধুমাত্র একটি উপাদান যোগ করা যায়।

আর update() দিয়ে একসাথে একাধিক উপাদান (সেট, লিস্ট বা অন্যান্য ইটারেবল থেকে) যোগ করে মূল সেটটিকে এক লাফে বড় করে ফেলা যায়।




২. সেট থেকে উপাদান বাদ দেওয়া (remove(), discard(), pop())

remove(item): নির্দিষ্ট উপাদানটি মুছে ফেলতে। তবে উপাদানটি যদি সেটে না থাকে, তবে পাইথন KeyError বা Error দেবে।

discard(item): এটিও নির্দিষ্ট উপাদান মুছে ফেলে। তবে উপাদান সেটে না থাকলেও কোনো এরর দেয় না, চুপচাপ কোড চালিয়ে নেয়।

pop(): সেটের ভেতর থেকে র‍্যান্ডম বা যেকোনো একটি উপাদান ডিলিট করে দেয় এবং সেটি রিটার্ন করে। যেহেতু সেটের কোনো ইনডেক্স নেই,
তাই কোনটি ডিলিট হবে তা নির্দিষ্ট করে বলা যায় না।


remove() — নির্দিষ্ট মান সরানো (না থাকলে error)
remove() মেথড
কাজ কী: সেটের ভেতর থেকে নির্দিষ্ট কোনো উপাদানকে মুছে ফেলতে এটি ব্যবহার করা হয়।
বিশেষ সতর্কতা: যে উপাদানটি  মুছে ফেলতে চাওয়া হসছে সেটি যদি সেটের ভেতরে না থাকে, তবে পাইথন ক্র্যাশ করবে এবং একটি KeyError (এরর) দিবে।


fruits = {"apple", "banana", "mango"}
fruits.remove("banana")
print(fruits)  # {'apple', 'mango'}

fruits.remove("orange")  # KeyError: 'orange' -> এটা নেই তাই error


fruits_set = {"apple", "banana", "mango"}

kk = fruits_set.remove("kk")

print(kk)

print(fruits_set)



fruits_set = {"apple", "banana", "mango"}

kk = fruits_set.remove("banana")

print(kk) None

print(fruits_set)


# ফলের একটি সেট
fruits = {"apple", "banana", "mango", "orange"}

# সেট থেকে "banana" মুছে ফেলা হচ্ছে
fruits.remove("banana")

print("পরে:", fruits)
# আউটপুট: {'apple', 'mango', 'orange'} (ব্যানানা সফলভাবে মুছে গেছে)

# ⚠️ সমস্যা কোথায় হয়:
# fruits.remove("grape")  # 'grape' তো সেটের ভেতরে নেই! 
# আউটপুট: KeyError: 'grape' (প্রোগ্রাম এখানে এসে আটকে বা ক্র্যাশ করবে)




discard() — নির্দিষ্ট মান সরানো (না থাকলে error দেবে না)

discard() মেথড

কাজ কী: এটিও remove() এর মতো নির্দিষ্ট কোনো উপাদানকে সেট থেকে মুছে ফেলতে ব্যবহার করা হয়।
পার্থক্য: যে উপাদানটি মুছে ফেলতে চাওয়া হসছে সেটি যদি সেটের ভেতরে না-ও থাকে, 
তবুও পাইথন কোনো এরর বা ঝামেলা করবে না। কোড একদম শান্তিতে পরের লাইনে চলে যাবে।

fruits = {"apple", "banana", "mango"}
fruits.discard("orange")  # কোনো error আসবে না, চুপচাপ কিছুই হবে না
print(fruits)  # {'apple', 'banana', 'mango'}

⚠️ remove() vs discard() এর পার্থক্য মনে রাখা জরুরি: item না থাকলে remove() error দেয়, কিন্তু discard() নীরবে কিছুই করে না। 
যখন নিশ্চিত না থাকো item আছে কিনা, তখন discard() ব্যবহার করা নিরাপদ।

# রঙের একটি সেট
colors = {"red", "green", "blue"}

# "green" মুছে ফেলা হলো
colors.discard("green")
print("green মুছে ফেলার পর:", colors)
# আউটপুট: {'red', 'blue'}


# এবার এমন একটি রং মুছতে চাচ্ছি যা সেটের ভেতর নেই ("yellow"):
colors.discard("yellow") 
print("yellow ডাসকার্ড করার পর:", colors)
# আউটপুট: {'red', 'blue'} (কোনো এরর দেয়নি, চুপচাপ কাজ শেষ করেছে!)



fruits = {"apple", "banana", "mango", "orange"}
print("Original set:", fruits)

fruits.remove("banana")
print("After removal:", fruits)



colors = {"red", "green", "blue"}
print("Original set:", colors)

# সেটে থাকা উপাদান রিমুভ করা
colors.discard("green")
print("After discarding 'green':", colors)

# সেটে নেই এমন উপাদান ডিসকার্ড করার চেষ্টা (কোনো এরর আসবে না)
colors.discard("yellow")
print("After discarding non-existent 'yellow':", colors)



fruits_set = {"apple", "banana", "mango"}

kk = fruits_set.discard("kk")

print(kk) 

print(fruits_set)



fruits_set = {"apple", "banana", "mango"}

kk = fruits_set.discard("banana")

print(kk) None

print(fruits_set)






pop() — এলোমেলোভাবে একটা item সরিয়ে রিটার্ন করা

pop() মেথড

তাই পাইথনের .pop() মেথড সেট থেকে  একটি র‍্যান্ডম (অনির্দিষ্ট) উপাদানকে ডিলিট করে দেয় এবং ডিলিট হওয়া উপাদানটি রিটার্ন করে।

বিশেষ সতর্কতা: সেটের যেহেতু কোনো নির্দিষ্ট ইনডেক্স বা সিরিয়াল নেই (0, 1 নম্বর বলে কিছু নেই), 
তাই pop() কল করলে ঠিক কোন উপাদানটি মুছে যাবে তা আগে থেকে নিশ্চিত করে বলতে পারা যায় না। 
পাইথন নিজের ইচ্ছামমতো যেকোনো একটি আইটেম উড়িয়ে দেবে। তাছাড়া, সেট ফাঁকা (Empty) থাকলে এটিও এরর দিবে।


fruits = {"apple", "banana", "mango"}
removed = fruits.pop()
print(removed)  # যেকোনো একটা (কোনটা আসবে নিশ্চিত না, কারণ order নেই)
print(fruits)   # বাকি দুইটা

⚠️ List এ pop() নির্দিষ্ট index থেকে সরাতো, কিন্তু Set এ index নেই বলে pop() এলোমেলোভাবে যেকোনো একটা item সরিয়ে দেয়।

# সংখ্যার একটি সেট
numbers = {10, 20, 30, 40, 50}

# pop() কল করলে যেকোনো একটি উপাদান ডিলিট হয়ে সেটি রিমুভড ভ্যারিয়েবলে জমা হবে
removed_item = numbers.pop()

print("যে উপাদানটি মুছে গেছে:", removed_item)
print("মুছে ফেলার পর সেটটি যেমন আছে:", numbers)

# আউটপুট কেমন আসতে পারে (অর্ডার র‍্যান্ডম হওয়ায় পাল্টাতে পারে):
# যে উপাদানটি মুছে গেছে: 40 (বা অন্য যেকোনো একটি সংখ্যা)
# মুছে ফেলার পর সেটটি যেমন আছে: {10, 20, 30, 50}



# একটি সেট তৈরি করা হলো
colors = {"red", "green", "blue", "yellow"}

# .pop() ব্যবহার করে একটি র‍্যান্ডম উপাদান রিমুভ করা হলো
removed_item = colors.pop()

print(f"মুছে ফেলা উপাদানটি হলো: {removed_item}")
print(f"আপডেট হওয়া সেট: {colors}")


আউটপুট দেখতে কেমন হতে পারে?
(যেহেতু সেটের কোনো অর্ডার নেই, তাই প্রতিবার কোড চালালে ভিন্ন ভিন্ন উপাদান ডিলিট হতে পারে)

মুছে ফেলা উপাদানটি হলো: blue
আপডেট হওয়া সেট: {'red', 'green', 'yellow'}



# একটি ফলের সেট
fruits = {"apple", "banana", "mango", "orange"}
print("Original set:", fruits)

# pop() মেথড ব্যবহার করে যেকোনো একটি আইটেম রিমুভ করা হলো এবং তা ভেরিয়েবলে রাখা হলো
removed_item = fruits.pop()

print("Removed item:", removed_item)
print("After pop set:", fruits)


vvi
fruits = {'apple', 'banana'}
some_fruits = ('mango', 'cherry', 'jackfruit')

fruits.update(some_fruits)

fruits.pop(0)

print(fruits)

fruits.update(some_fruits) লাইনটি খুব সুন্দরভাবে কাজ করবে। 
এর ফলে fruits সেটের ভেতর mango, cherry এবং jackfruit 
যোগ হয়ে সেটটি বড় হবে (যেমন: {'apple', 'banana', 'mango', 'cherry', 'jackfruit'}).

কিন্তু পরের লাইনে এসে : fruits.pop(0)।

আগেই আমরা আলোচনা করেছি যে, সেটের (Set) কোনো ইনডেক্স থাকে না।

তাছাড়া, সেটের .pop() মেথডে কোনো ইনডেক্স নম্বর পাস করা যায় না (ফাঁকা রাখতে হয়)।


fruits = {'apple', 'banana'}
some_fruits = ('mango', 'cherry', 'jackfruit')

fruits.update(some_fruits)

fruits.pop()

print(fruits)





🎯 সংক্ষেপে একনজরে পার্থক্য:

উপাদান ফিক্সড এবং সেটে থাকতেই হবে, না থাকলে কোড ভেঙে ফেলার দরকার হলে remove() ব্যবহার করতে হবে।

উপাদান ডিলিট করতে চাওয়া হলে, কিন্তু সেট না থাকলেও কোড যেন ক্র্যাশ না করে এমন নিরাপত্তা চাইলে  discard() ব্যবহার করতে হবে।

নির্দিষ্ট কোনো নাম না ধরে, শুধু র‍্যান্ডম যেকোনো একটি উপাদান সেট থেকে পপ বা হাওয়া করে দিতে চাইলে  pop() ব্যবহার  করতে হবে।


fruits_set = {"apple", "banana", "mango"}

removed = fruits_set.remove("kk")

print(removed) 

print(fruits_set)





fruits_set = {"apple", "banana", "mango"}

removed = fruits_set.remove("banana")

print(removed) None

print(fruits_set)






clear() হলো পাইথনের একটি বিল্ট-ইন মেথড (Method)। এর আক্ষরিক অর্থ হলো "পরিষ্কার করা" বা "সব মুছে ফেলা"।

সেটের .clear() মেথডটি খুবই সহজ এবং কাজের। এর কাজ হলো একটি সেটের ভেতরের সব উপাদান
চিরতরে মুছে ফেলা এবং সেটটিকে একটি খালি (empty) সেটে রূপান্তর করা।

fruits_set = {"apple", "banana", "mango"}

removed = fruits_set.clear()

print(removed) None

print(fruits_set) set()



fruits = {"apple", "banana", "mango", "orange"}
print("Original set:", fruits)

# clear() মেথড ব্যবহার করে সেটের সব উপাদান মুছে ফেলা হলো
fruits.clear()

print("After clear:", fruits)
print("Type of set:", type(fruits))



# শুরুতে সেটে ৩টি ফল আছে
fruits = {"apple", "banana", "mango"}
print("আগে:", fruits)  # আউটপুট: {'apple', 'banana', 'mango'} (অর্ডার এলোমেলো হতে পারে)

# clear() মেথড কল করা হলো
fruits.clear()

# এখন প্রিন্ট করলে কী দেখা যাবে?
print("পরে:", fruits)  # আউটপুট: set()



# কিছু উপাদানসহ একটি সেট তৈরি করা হলো
permissions = {"read", "write", "execute"}

print(f"আগের সেট: {permissions}")

# .clear() মেথড ব্যবহার করে সব উপাদান মুছে ফেলা হলো
permissions.clear()

print(f"বর্তমান সেট: {permissions}")


গুরুত্বপূর্ণ পয়েন্টসমূহ:
১. পুরো সেট খালি করে দেয়: এটি একটি একটি করে উপাদান (remove() বা discard() এর মতো) ডিলিট করে না; বরং একবারে সেটের ভেତরের সমস্ত উপাদান মুছে ফেলে।
২. ভ্যারিয়েবল থাকে, শুধু ডেটা মুছে যায়: fruits নামের ব্যাগ বা ভ্যারিয়েবলটি মেমোরিতে ঠিকই বেঁচে থাকে, কিন্তু তার ভেତরের মালপত্র বা উপাদানগুলো শূন্য হয়ে যায়।
৩. আউটপুট কেমন দেখায়? কোড রান করার পর আউটপুটে set() দেখাবে, যার মানে হলো সেটটি এখন একদম ফাঁকা (Empty Set)।


.remove() বা .discard() দিয়ে একটি একটি করে উপাদান মুছতে হয়, কিন্তু .clear() দিয়ে এক ক্লিকেই পুরো সেটের সব ডেটা সাফ করে দেওয়া যায়।

ডেটা মুছে গেলেও সেট ভেরিয়েবলটি ডিলিট হয় না, বরং সেটি একটি খালি সেট (set()) হিসেবে মেমোরিতে বেঁচে থাকে।





.copy() মেথড
এই মেথডটির কাজ হলো হুবহু একই রকম আরেকটি নতুন সেট তৈরি করা (যাতে মূল সেটটি অপরিবর্তিত রেখে নতুন কপিতে পরিবর্তন করা যায়)।
.copy() মেথডের কাজ হলো হুবহু একটি নতুন সেট তৈরি করা (কপি বা ক্লোন করা), অন্যের ডেটা এনে জোড়া লাগানো নয়। যেমন:



original_set = {'apple', 'banana'}

# এটি original_set-এর একটি হুবহু কপি তৈরি করে নতুন ভেরিয়েবলে রাখবে
new_set = original_set.copy()

print(new_set)  # আউটপুট: {'apple', 'banana'}



# মূল সেট
original_set = {"apple", "banana", "mango"}
print("Original set:", original_set)

# copy() মেথড ব্যবহার করে নতুন কপি তৈরি করা হলো
copied_set = original_set.copy()
print("Copied set:", copied_set)

# এখন শুধু কপি করা সেটে নতুন একটি উপাদান যোগ করা যাক
copied_set.add("orange")

print("\n--- After modifying the copied set ---")
print("Original set (unchanged):", original_set)
print("Copied set (updated):", copied_set)




# মূল সেট
fruits_set = {"apple", "banana", "mango"}
print("fruits set:", fruits_set)

copy_set = fruits_set.copy()

print("copy set", copy_set)

copy_set.add("orange")

print(copy_set)



# মূল সেট
original_set = {"apple", "banana", "cherry"}

# .copy() ব্যবহার করে নতুন সেট তৈরি করা হলো
copied_set = original_set.copy()

# নতুন সেটে একটি আইটেম যোগ করা হলো
copied_set.add("orange")

print(f"মূল সেট: {original_set}")
print(f"কপি করা সেট: {copied_set}")


মূল সেট: {'apple', 'banana', 'cherry'}
কপি করা সেট: {'apple', 'banana', 'cherry', 'orange'}

কপি সেটে পরিবর্তন করলেও মূল সেটটি একদম নিরাপদ ও অপরিবর্তিত থাকে।






intersection আসলে কী করে?

ইন্টারসেকশনের কাজ হলো কেবল এবং কেবল দুটি সেটের মধ্যে যে উপাদানগুলো কমন বা মিল আছে, 
শুধু সেগুলোকেই নেওয়া। প্রথম সেটে যে উপাদানগুলোর মিল নেই, সেগুলোকে এটি সম্পূর্ণ বাদ বা ডিলিট করে দেয়।

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# intersection শুধু কমন উপাদানগুলো রাখবে
result = set1.intersection(set2)

print(result)  
# আউটপুট দেখাবে: {3, 4} (কারণ শুধু 3 আর 4 উভয় সেটে আছে)
# খেয়াল করুন: প্রথম সেটের 1 এবং 2 বাদ হয়ে গেছে, কারণ সেগুলো দ্বিতীয় সেটে ছিল না।




my_set = {'apple', 'kk', 'banana', 'mango'}
fruits = {'yy', "banana", "mango", 'orange'}

# এটি শুধু কমন উপাদানগুলো বের করে দেখাবে, কিন্তু my_set বদলাবে না
result = my_set.intersection(fruits)

print(result)  # আউটপুট: {'banana', 'mango'} (কমনগুলো আলাদা হয়ে আসলো)
print(my_set)  # আউটপুট: {'apple', 'kk', 'banana', 'mango'} (আসল সেট অপরিবর্তিত আছে!)

vvi-------

my_set = {'apple', 'kk', 'banana', 'mango'}
fruits = {'yy',  "banana", "mango", 'orange'} 


my_set.intersection(fruits)

print(my_set)

১. মূল ভ্যারিয়েবল (my_set) অপরিবর্তিত থাকে।
২. .intersection() মেথডটি প্রথম ও দ্বিতীয় সেটের মধ্যকার মিল থাকা (common) উপাদানগুলো খুঁজে বের করে।

ছোট করে একটি ব্যাপার মনে রাখবেন—যেহেতু এটি কমন উপাদানগুলো খুঁজে একটি নতুন ফলাফল রিটার্ন করে (কিন্তু মূল সেট বদলায় না), 
তাই সেই ফলাফলটি দেখতে চাইলে হয় সরাসরি প্রিনটের ভেতরে লিখতে হবে, অথবা নতুন কোনো ভ্যারিয়েবলে সেভ করে রাখতে হবে। 

# এভাবে প্রিনটের ভেতর দিলে কমন উপাদানগুলো দেখতে পাবেন:
print(my_set.intersection(fruits))  # আউটপুট: {'banana', 'mango'}

# আর মূল সেট প্রিন্ট করলে আগেরটাই থাকবে:
print(my_set)  # আউটপুট: {'apple', 'kk', 'banana', 'mango'}


my_set = {"apple", "banana", "mango"}

added = ('arman', 'aziz', 'abdullah', 'chreey', 'jackfruits', "banana", "mango")

kk = my_set.intersection(added)

print(my_set) {"apple", "banana", "mango"}

print(kk) // print(my_set.intersection(added)) {'mango', 'banana'}




.intersection_update() মেথড

পাইথনের সেটে .intersection_update() মেথডটি খুবই কাজের একটি ফাংশন। 
এটি মূলত দুটি বা ততোধিক সেটের মধ্যে কমন (Common) বা সাধারণ উপাদানগুলো 
খুঁজে বের করে এবং মূল সেটটিকে শুধুমাত্র ওই কমন উপাদানগুলো দিয়েই আপডেট করে দেয়।

.intersection_update() মেথডটি ঠিক এই কাজটিই করে।
এটি মূল ভ্যারিয়েবলকে (my_set) অপরিবর্তিত না রেখে সরাসরি পরিবর্তন (modify বা update) করে দেয়।

ইন-প্লেস পরিবর্তন (In-place Modification): .intersection() মেথড যেখানে নতুন একটি সেট রিটার্ন করে, 
সেখানে .intersection_update() নতুন কোনো সেট তৈরি করে না—বরং মূল সেটটিকেই পরিবর্তন করে ফেলে।

কমন উপাদান রাখা: দুটি সেটের মধ্যে যে উপাদানগুলো উভয় দলেই রয়েছে, শুধু সেগুলোকে রেখে বাকি সব উপাদান মূল সেট থেকে মুছে দেয়।

fruits_set = {"apple", "banana", "mango"}

fruits = {"kk", 'yy',  "banana", "mango", 'orange'} 

kk = fruits_set.intersection_update(fruits)

print(fruits_set) "banana", "mango"

print(kk) None



my_set = {'apple', 'kk', 'banana', 'mango'}
fruits = {'yy',  "banana", "mango", 'orange', 'apple', 'cherry'} 

my_set.intersection_update(fruits)

print(my_set)





# দুটি সেট
my_permissions = {"read", "write", "execute"}
allowed_permissions = {"read", "execute", "delete"}

# my_permissions-কে আপডেট করা হবে যেন শুধু কমন উপাদানগুলো থাকে
my_permissions.intersection_update(allowed_permissions)

print(f"আপডেট হওয়া পারমিশন সেট: {my_permissions}")


আপডেট হওয়া পারমিশন সেট: {'read', 'execute'}

খানে my_permissions এবং allowed_permissions এর মধ্যে কমন আইটেম ছিল শুধু "read" এবং "execute",
আর .intersection_update() কল করার কারণে মূল my_permissions সেটটি ছোট হয়ে শুধু এই দুটি উপাদানই নিজের ভেতর রেখে দিয়েছে।



# দুটি সেট তৈরি করা হলো
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Original set1:", set1)
print("Set2:", set2)

# intersection_update() ব্যবহার করা হলো
set1.intersection_update(set2)

print("\nAfter intersection_update:")
print("Updated set1:", set1)


Original set1: {1, 2, 3, 4, 5}
Set2: {4, 5, 6, 7, 8}

After intersection_update:
Updated set1: {4, 5}

জরুরি নোট: যেহেতু এটি সরাসরি মূল সেটকে পরিবর্তন করে, তাই এর রিটার্ন ভ্যালু None হয়। 
যদি সরাসরি প্রিন্ট করতে  print(set1.intersection_update(set2)), তবে আউটপুট None দেখাবে। 
তাই মেথডটি আলাদা লাইনে চালিয়ে পরে set1 প্রিন্ট করতে হয়।


এডমিন প্যানেল থেকে ইনঅ্যাক্টিভ ইউজার বাদ দেওয়া
ধরে নিন আপনার সিস্টেমে কিছু রেজিস্টার্ড এডমিন আছেন এবং একটিভ ইউজারের লিস্ট আছে। 
 মূল এডমিন লিস্টটিকে আপডেট করে শুধু তাদেরই রাখতে যারা বর্তমানে সিস্টেমে একটিভ আছেন।

# মূল এডমিনদের সেট
admins = {"rahim", "karim", "tanvir", "salma", "atik"}

# বর্তমানে অনলাইন বা একটিভ ইউজারদের সেট
active_users = {"karim", "salma", "atik", "jabbar"}

print("Original Admins:", admins)
print("Active Users:", active_users)

# intersection_update ব্যবহার করে শুধু কমন এডমিনদের রাখা হলো
admins.intersection_update(active_users)

print("\nAfter intersection_update (Only Active Admins):")
print("Updated Admins:", admins)



দুটি ভিন্ন শপিং ক্যাটাগরির কমন প্রোডাক্ট ফিল্টার করা
ধরে নিন আপনার কাছে একটি ফ্যাশন স্টোরের ট্রেন্ডিং পণ্যের সেট আছে এবং কাস্টমারদের পছন্দের পণ্যের সেট আছে।
দেখতে ট্রেন্ডিংয়ের মধ্যে কোন পণ্যগুলো কাস্টমাররা বেশি পছন্দ করছে।

# ট্রেন্ডিং পণ্যের সেট
trending_products = {"shoes", "jacket", "watch", "sunglasses", "cap"}

# কাস্টমারদের পছন্দের পণ্যের সেট
customer_favorites = {"jacket", "watch", "backpack", "shoes"}

print("Trending Products:", trending_products)
print("Customer Favorites:", customer_favorites)

# intersection_update দিয়ে ট্রেন্ডিং সেটটি আপডেট করা হলো
trending_products.intersection_update(customer_favorites)

print("\nAfter intersection_update (Top Selling Trending Items):")
print("Updated Trending Products:", trending_products)



জবের রিকোয়ারমেন্টের সাথে প্রার্থীর স্কিল ম্যাচ করা
ধরে নিন একটি ব্যাকএন্ড ডেভেলপার পদের জন্য কিছু নির্দিষ্ট স্কিল প্রয়োজন। 
এখন একজন প্রার্থীর যতগুলো স্কিল আছে, সেগুলোর মধ্যে থেকে শুধু জবের
সাথে মিলে যাওয়া (কমন) স্কিলগুলো দিয়ে প্রার্থীর স্কিল সেটটি আপডেট করতে।


# প্রার্থীর বর্তমান স্কিলসমূহের সেট
candidate_skills = {"python", "git", "html", "css", "docker"}

# জবের জন্য প্রয়োজনীয় স্কিলসমূহের সেট
required_skills = {"python", "django", "sql", "git", "docker"}

print("Candidate's Original Skills:", candidate_skills)
print("Required Job Skills:", required_skills)

# intersection_update ব্যবহার করে প্রার্থীর স্কিল ফিল্টার করা হলো
candidate_skills.intersection_update(required_skills)

print("\nAfter intersection_update (Matched/Valid Skills):")
print("Updated Candidate Skills:", candidate_skills)

এখানে প্রার্থীর অপ্রয়োজনীয় স্কিলগুলো (html, css) বাদ হয়ে গেছে 
এবং শুধু জবের রিকোয়ারমেন্টের সাথে মিলে যাওয়া কমন স্কিলগুলো (python, docker, git) দিয়ে candidate_skills সেটটি আপডেট হয়ে গেছে!





.difference()

পাইথনের সেটে .difference() মেথডটি খুবই চমৎকার একটি ফাংশন। 
এর কাজ হলো দুটি সেটের মধ্যে তুলনা করে প্রথম সেটটিতে আছে কিন্তু দ্বিতীয় সেটটিতে নেই—এমন উপাদানগুলো নিয়ে নতুন একটি সেট তৈরি করা।

.difference() মেথড মূলত এই কাজটিই করে:

এটি চেক করে প্রথম ভেরিয়েবলে (1st variable) কী কী আছে।

এরপর সেখান থেকে দ্বিতীয় ভেরিয়েবলের (2nd variable) ভেতরের উপাদানগুলোকে বাদ দিয়ে দেয়।

সহজ কথায়: প্রথম সেটে আছে কিন্তু দ্বিতীয় সেটে নেই, শুধু সেই উপাদানগুলোই সে রিটার্ন করে।

এটি মূল সেটগুলোকে অপরিবর্তিত রেখে ফলাফল হিসেবে সম্পূর্ণ নতুন একটি সেট রিটার্ন করে। তাই এর আউটপুট একটি ভেরিয়েবলে রেখে দিতে হয়।

কমন বা মিলগুলো বাদ চলে যাবে, আর প্রথম ভ্যারিয়েবলে যেগুলো শুধু একা আছে (অর্থাৎ যেগুলোর সাথে মিল পাওয়া যায়নি), শুধু সেগুলোর সেটই রিটার্ন করবে।


my_set = {'apple', 'kk', 'banana', 'mango'}
fruits = {'yy',  "banana", "mango", 'orange', 'apple', 'cherry'} 

new_result = my_set.difference(fruits)

print(my_set)   {'apple', 'kk', 'banana', 'mango'}

print(new_result) {'kk'}


মূল ভ্যারিয়েবল অপরিবর্তিত থাকে: print(my_set) করলে আপনার আসল সেটটি আগের মতোই অক্ষত থাকে।

মিলগুলো বাদ যায়: প্রথম সেট (my_set) এবং দ্বিতীয় সেট (fruits) এর মধ্যে যে 
উপাদানগুলোর মিল ছিল (apple, banana, mango) সেগুলো বাদ হয়ে যায়।

ডিফারেন্স বা পার্থক্য জমা হয়: শুধু প্রথম সেটের যে উপাদানটি দ্বিতীয় সেটে ছিল না ('kk'),
সেটি নতুন ভ্যারিয়েবলে (new_result) স্টোর বা জমা হয়।

my_set = {'apple', 'kk', 'banana', 'mango'}
fruits = {'yy',  "banana", "mango", 'orange', 'apple', 'cherry'} 

my_set.difference(fruits)

print(my_set) {'apple', 'kk', 'banana', 'mango'}



বিয়োগ করার মতো কাজ: সহজ কথায়, প্রথম সেট থেকে দ্বিতীয় সেটের কমন উপাদানগুলো বাদ দিয়ে বাকি যা থাকে,
তা নিয়ে নতুন সেট বানিয়ে দেয় (Set1 - Set2-এর মতো কাজ করে)।

# দুটি সেট তৈরি করা হলো
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Original set1:", set1)
print("Set2:", set2)

# difference() ব্যবহার করে নতুন সেট তৈরি করা হলো এবং result_set এ রাখা হলো
result_set = set1.difference(set2)

print("\nAfter difference operation:")
print("New Result Set:", result_set)
print("Original set1 (Unchanged):", set1)


Original set1: {1, 2, 3, 4, 5}
Set2: {4, 5, 6, 7, 8}

After difference operation:
New Result Set: {1, 2, 3}
Original set1 (Unchanged): {1, 2, 3, 4, 5}



# যারা ক্রিকেট খেলে
cricket_players = {"rahim", "karim", "tanvir", "sakib"}

# যারা ফুটবল খেলে
football_players = {"karim", "sakib", "salma"}

# difference() ব্যবহার করে শুধু ক্রিকেট খেলা খেলোয়াড়দের বের করা হলো
only_cricket = cricket_players.difference(football_players)

print("Only Cricket Players:", only_cricket)
print("Original Cricket Set (Safe):", cricket_players)


Only Cricket Players: {'rahim', 'tanvir'}
Original Cricket Set (Safe): {'sakib', 'karim', 'tanvir', 'rahim'}

.difference() বা .intersection() এর মতো নন-মিউটেবল মেথডগুলোর মূল নিয়মই এটি:

ফলাফলটি ধরে রাখার জন্য অবশ্যই একটি নতুন ভ্যারিয়েবল নিতে হবে।

আর মূল ভ্যারিয়েবলটি একেবারে অপরিবর্তিত থাকবে।






.difference_update() মেথড

সাধারণ - বা .difference() অপারেটর শুধু ডিফারেন্স দেখায়, কিন্তু .intersection_update() এর মতো 
.difference_update() এটি মূলত একটি সেট থেকে অন্য সেটের কমন উপাদানগুলো মুছে ফেলার (Remove) জন্য ব্যবহার করা হয়।


.difference_update() মেথডের কাজটাই হলো এটি:
১. মূল ভ্যারিয়েবল (my_set) থেকে প্রথম ও দ্বিতীয় সেটের কমন বা মিল থাকা উপাদানগুলোকে বাদ দিয়ে দেয়।
২. ফলে মূল ভ্যারিয়েবলটি পরিবর্তিত হয়ে যায় এবং সেখানে শুধু অমিল বা ব্যতিক্রম উপাদানটিই আউটপুট হিসেবে থেকে যায়।


my_set = {'apple', 'kk', 'banana', 'mango'}
fruits = {'yy',  "banana", "mango", 'orange', 'apple', 'cherry'} 

my_set.difference_update(fruits)

print(my_set)






fruits_set = {"apple", "banana", "mango"}

fruits = {"kk", 'yy',  "banana", "mango", 'orange'} 

kk = fruits_set.difference_update(fruits)

print(fruits_set) 

print(kk) None


কোডটি কী করছে?
fruits_set: {"apple", "banana", "mango"}

fruits: {"kk", "yy", "banana", "mango", "orange"}

অপারেশন: fruits_set.difference_update(fruits)

আপনার প্রশ্ন অনুযায়ী "orange" কেন এল না বা কী হলো?
orange কেন বাদ বা এল না?
.difference_update() মেথডের কাজ হলো প্রথম সেট (fruits_set) থেকে ওই উপাদানগুলো মুছে ফেলা, যেগুলো দ্বিতীয় সেটে (fruits) কমন বা মিল রয়েছে।

orange কেবল fruits সেটের মধ্যে ছিল, কিন্তু আপনার মূল fruits_set-এ orange নামটাই ছিল না!

যেহেতু fruits_set-এ orange আগে থেকেই ছিল না, তাই সেখান থেকে নতুন করে কিছু বাদ দেওয়ার বা যোগ করার সুযোগ নেই।

তাহলে আসলে কী ঘটল?

fruits_set এবং fruits উভয়ের মধ্যে কমন উপাদান ছিল "banana" এবং "mango"।

.difference_update(fruits) চালানোর ফলে fruits_set থেকে ওই কমন উপাদানগুলো (banana এবং mango) ডিলিট হয়ে গেছে।

ফলে শুধু "apple" বাকি থাকে। তাই print(fruits_set) করলে আউটপুট আসবে: {'apple'}।

print(kk) তে কী আসবে?
আপনি kk = fruits_set.difference_update(fruits) লিখেছেন।

আমরা আগেই জেনেছি, সমস্ত ইন-প্লেস আপডেট মেথড (যেমন: difference_update, intersection_update, update) নতুন কোনো সেট রিটার্ন করে না, এগুলো সরাসরি মূল সেটকে পরিবর্তন করে এবং রিটার্ন হিসেবে None দেয়।

তাই print(kk) রান করলে আউটপুট দেখাবে: None। (আর এখানেই অনেকে ভুল করেন, তারা মনে করেন নতুন সেটটি kk-তে জমা হয়েছে)।



all_users = {"Rahim", "Karim", "Sakib", "Arman"}
banned_users = {"Karim", "Sakib"}

# all_users থেকে ব্যান হওয়া ইউজারদের বাদ দিয়ে মূল সেটটি আপডেট করা হলো
all_users.difference_update(banned_users)

print(all_users)
# আউটপুট: {'Rahim', 'Arman'} (Karim ও Sakib বাদ পড়ে গেছে)




# দুটি সেট তৈরি করা হলো
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Original set1:", set1)
print("Set2:", set2)

# difference_update() ব্যবহার করা হলো
set1.difference_update(set2)

print("\nAfter difference_update:")
print("Updated set1:", set1)


Original set1: {1, 2, 3, 4, 5}
Set2: {4, 5, 6, 7, 8}

After difference_update:
Updated set1: {1, 2, 3}


কোডটি যেভাবে কাজ করল:
১. set1 এবং set2 উভয়ের মধ্যেই কমন বা মিল রয়েছে 4 এবং 5 এর মধ্যে।
২. যখন set1.difference_update(set2) চালানো হলো, তখন পাইথন set1 থেকে ওই কমন উপাদানগুলো (4 এবং 5) মুছে দিল।
৩. ফলে set1-এ শুধু বাকি উপাদানগুলো (1, 2, 3) রয়ে গেল এবং মূল সেটটি আপডেট হয়ে গেল।



চ্যাট গ্রুপ থেকে ব্লক করা বা নিষিদ্ধ ইউজারদের বাদ দেওয়া
ধরে নিন আপনার একটি কমিউনিটি চ্যাট গ্রুপের সমস্ত সদস্যের একটি সেট আছে। এর মধ্যে কিছু ইউজার নিয়ম 
ভঙ্গ করায় তাদের একটি "ব্ল্যাকলিস্ট" বা নিষিদ্ধ ইউজারের সেটে রাখা হয়েছে। এখন আপনি মূল গ্রুপ থেকে ওই নিষিদ্ধ ইউজারদের পাকাপাকিভাবে বাদ দিতে চান।


# গ্রুপে থাকা সমস্ত ইউজারের সেট
all_users = {"rahim", "karim", "tanvir", "salma", "atik", "jabbar"}

# নিয়ম ভঙ্গের কারণে ব্লক বা নিষিদ্ধ করা ইউজারদের সেট
blocked_users = {"tanvir", "jabbar"}

print("All Users:", all_users)
print("Blocked Users:", blocked_users)

# difference_update ব্যবহার করে মূল সেট থেকে নিষিদ্ধ ইউজারদের বাদ দেওয়া হলো
all_users.difference_update(blocked_users)

print("\nAfter difference_update (Allowed Users):")
print("Active Users:", all_users)


All Users: {'jabbar', 'karim', 'salma', 'atik', 'rahim', 'tanvir'}
Blocked Users: {'jabbar', 'tanvir'}

After difference_update (Allowed Users):
Active Users: {'rahim', 'karim', 'salma', 'atik'}


কোডটি যেভাবে কাজ করল:
১. all_users এবং blocked_users উভয়ের মধ্যে কমন বা মিল থাকা ইউজাররা ("tanvir" এবং "jabbar") চিহ্নিত হলো।
২. all_users.difference_update(blocked_users) চালানোর সাথে সাথেই মূল all_users সেট থেকে ওই নিষিদ্ধ ইউজারগুলো চিরতরে মুছে গেল।
৩. ফলে মূল সেটটি আপডেট হয়ে শুধু বৈধ ইউজারদের নিয়ে থেকে গেল।



রেসিপি থেকে অ্যালার্জিযুক্ত বা ক্ষতিকর উপাদান বাদ দেওয়া
ধরে নিন আপনি একটি রান্নার রেসিপির জন্য প্রয়োজনীয় উপকরণের একটি সেট তৈরি করেছেন। 
এখন কোনো নির্দিষ্ট ব্যক্তির খাবারের অ্যালার্জি (जैसे: peanuts বা milk) থাকার কারণে সেই উপাদানগুলো আপনার রেসিপি থেকে বাদ দিতে চান।


# রেসিপির সমস্ত উপকরণের সেট
recipe_ingredients = {"flour", "sugar", "peanuts", "milk", "butter", "chocolate"}

# বাদ দিতে হবে বা অ্যালার্জিযুক্ত উপকরণের সেট
allergens = {"peanuts", "milk"}

print("Original Recipe Ingredients:", recipe_ingredients)
print("Allergens to Avoid:", allergens)

# difference_update ব্যবহার করে রেসিপি থেকে ক্ষতিকর উপাদানগুলো বাদ দেওয়া হলো
recipe_ingredients.difference_update(allergens)

print("\nAfter difference_update (Safe Ingredients):")
print("Safe Ingredients:", recipe_ingredients)




# ১. ইউজারের বর্তমানে সেশনে থাকা অ্যাক্টিভ পারমিশনগুলোর সেট (সার্ভার ক্যাশ বা মেমোরিতে আছে)
active_user_permissions = {"read", "write", "delete", "execute", "upload"}

# ২. অ্যাডমিন যে পারমিশনগুলো বাতিল বা রিমুভ করেছেন
revoked_permissions = {"delete", "execute"}

print("Before Revoke (Active Permissions):", active_user_permissions)

# ৩. difference_update ব্যবহার করে মূল অ্যাক্টিভ সেটটি সরাসরি আপডেট করা হলো
active_user_permissions.difference_update(revoked_permissions)

print("After Revoke (Updated Active Permissions):", active_user_permissions)







.symmetric_difference() এবং .symmetric_difference_update()

১. .symmetric_difference()


my_set = {'apple', 'kk', 'banana', 'mango'}
fruits = {'yy',  "banana", "mango", 'orange', 'apple', 'cherry'} 

result = my_set.symmetric_difference(fruits)

print(my_set) {'apple', 'kk', 'banana', 'mango'}

print(result) {'kk', 'yy', 'orange', 'cherry'}

মূল ভ্যারিয়েবল অপরিবর্তিত থাকে: print(my_set) করলে আপনার আসল my_set আগের মতোই ({'apple', 'kk', 'banana', 'mango'}) একদম অক্ষত থাকবে।

তবে print(result) এ কী আসবে—সেখানে ছোট্ট একটি বিষয় একটু ভিন্নভাবে কাজ করে। চলুন দেখি:

.symmetric_difference() আসলে কী করে?
এটি দুই সেট থেকে কমন বা মিল থাকা উপাদানগুলোকে বাদ দেয়, কিন্তু শুধু প্রথম সেট নয়—উভয় সেটের অমিল বা ব্যতিক্রম উপাদানগুলো একসঙ্গে করে একটি নতুন রেজাল্ট দেয়।

এই কোডে কী হবে দেখুন:

কমন উপাদানগুলো বাদ যাবে: apple, banana, mango (দুটো সেট থেকেই বাদ)।

বাকি যেগুলো থাকবে (উভয় সেটের একক উপাদান):

my_set থেকে থাকবে: 'kk'

fruits থেকে থাকবে: 'yy', 'orange', 'cherry'

মূল ভ্যারিয়েবল: অপরিবর্তিত থাকে (print(my_set) আগের মতোই থাকে)।

রিসাল্ট (result): উভয় সেটের মিলগুলো বাদ দিয়ে বাকি সব উপাদান একসঙ্গে করে নতুন রেজাল্ট দেয়!


এই মেথডটি দুটি সেটের মধ্যে থাকা কমন (Common) উপাদানগুলো বাদ দিয়ে বাকি অমিল (Uncommon)
বা ইউনিক উপাদানগুলো নিয়ে নতুন একটি সেট রিটার্ন করে। এটি মূল সেটগুলোকে অপরিবর্তিত রাখে।

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# symmetric_difference ব্যবহার করে নতুন সেট তৈরি করা হলো
result_set = set1.symmetric_difference(set2)

print("Original set1:", set1)
print("Original set2:", set2)
print("Symmetric Difference Result:", result_set)


আউটপুট কেমন আসবে:

কমন উপাদান (3, 4) বাদ যাবে।

বাকি উপাদানগুলো নিয়ে নতুন সেট হবে: {1, 2, 5, 6}।

মূল set1 এবং set2 আগের মতোই অক্ষত থাকবে।


fruits_set = {"apple", "banana", "mango"}

fruits = {"kk", 'yy',  "banana", "mango", 'orange'} 

kk = fruits_set.symmetric_difference(fruits)

print(fruits_set) 

print(kk) 




২. .symmetric_difference_update()
"মূল ভ্যারিয়েবল আর দ্বিতীয় ভ্যারিয়েবলের কমন মিল সব বাদ যাবে, আর অমিলগুলো থাকবে (এবং মূল ভ্যারিয়েবল পরিবর্তন হয়ে যাবে)।"

এই কোডটির ক্ষেত্রে কী হবে?
কমন উপাদানগুলো বাদ যাবে: apple, banana, আর mango (যেহেতু এগুলো উভয় সেটে মিল আছে, 
তাই দুটো সেট থেকেই এগুলো চিরতরে মুছে যাবে)।

অমিলগুলো থাকবে: my_set-এর অমিল অংশ ('kk') এবং fruits-এর অমিল অংশ 
('yy', 'orange', 'cherry')—সবগুলো একসাথে মিলে আপনার মূল my_set-টি আপডেট হয়ে যাবে।


my_set = {'apple', 'kk', 'banana', 'mango'}
fruits = {'yy',  "banana", "mango", 'orange', 'apple', 'cherry'} 

result = my_set.symmetric_difference_update(fruits)

print(my_set) {'yy', 'kk', 'cherry', 'orange'}

print(result) None


my_set = {'apple', 'kk', 'banana', 'mango'}
fruits = {'yy',  "banana", "mango", 'orange', 'apple', 'cherry'} 

my_set.symmetric_difference_update(fruits)

print(my_set) 






set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Original set1:", set1)

# set1-কে সরাসরি আপডেট করা হলো
set1.symmetric_difference_update(set2)

print("After symmetric_difference_update (Updated set1):", set1)


fruits_set = {"apple", "banana", "mango"}

fruits = {"kk", 'yy',  "banana", "mango", 'orange'} 

kk = fruits_set.symmetric_difference_update(fruits)

print(fruits_set)    {'apple', 'kk', 'orange', 'yy'}

print(kk) None





বাস্তব উদাহরণ: দুটি গেমিং টিমের খেলোয়াড় সিলেকশন
ধরে নিন একটি কলেজে দুটি আলাদা কোডিং ক্লাব বা গেমিং টিম আছে। কিছু শিক্ষার্থী দুটি টিমেই আছে (কমন), আবার কিছু শিক্ষার্থী শুধু একটি টিমে আছে। 
এখন আপনি এমন একটি সেট চান যেখানে শুধু সেই শিক্ষার্থী থাকবে যারা যেকোনো একটি টিমে আছে, কিন্তু উভয় টিমে নেই (অর্থাৎ অমিল বা এক্সক্লুসিভ মেম্বাররা)।

কোড উদাহরণ (.symmetric_difference() ব্যবহার করে):

# টিম-এ এর খেলোয়াড়দের সেট
team_a = {"rahim", "karim", "tanvir", "salma"}

# টিম-বি এর খেলোয়াড়দের সেট
team_b = {"tanvir", "salma", "atik", "jabbar"}

print("Team A:", team_a)
print("Team B:", team_b)

# symmetric_difference ব্যবহার করে উভয়ের কমন মেম্বার বাদ দিয়ে শুধু ইউনিক মেম্বারদের নিয়ে নতুন সেট তৈরি
exclusive_members = team_a.symmetric_difference(team_b)

print("\nExclusive Members (In only one team, not both):", exclusive_members)
print("Original Team A (Unchanged):", team_a)


কোডটি যেভাবে কাজ করল:
১. team_a এবং team_b উভয়ের মধ্যে কমন সদস্য ছিল "tanvir" এবং "salma"।
২. .symmetric_difference() মেথড ওই কমন মেম্বারগুলোকে বাদ দিয়ে বাকিদের (rahim, karim, atik, jabbar) নিয়ে নতুন একটি সেট তৈরি করে দিয়েছে।
৩. মূল team_a বা team_b অপরিবর্তিত রয়েছে। আপনি যদি চান যে নতুন সেট 
না বানিয়ে সরাসরি team_a-কে আপডেট করে ফেলবেন, তবে team_a.symmetric_difference_update(team_b) ব্যবহার করতে পারেন।


বাস্তব উদাহরণ: দুটি ডেটাবেজের সিঙ্ক বা ডিভাইস সিঙ্ক্রোনাইজেশন
ধরে নিন একটি অফলাইন নোটস অ্যাপ এবং ক্লাউড সার্ভারের মধ্যে ডেটা সিঙ্ক করা হচ্ছে। যে ফাইলগুলো উভয় স্থানেই হুবহু আছে সেগুলোর প্রয়োজন নেই,
কিন্তু যে ফাইলগুলো শুধু একটি জায়গায় আছে (অফলাইনে অথবা ক্লাউডে), সেগুলোকে চিহ্নিত করে লোকাল ডিভাইস সেটটিকে আপডেট করতে চান।



# লোকাল ডিভাইসে থাকা ফাইলের সেট
local_files = {"doc1.txt", "doc2.txt", "doc3.txt"}

# ক্লাউড সার্ভারে থাকা ফাইলের সেট
cloud_files = {"doc2.txt", "doc3.txt", "doc4.txt", "doc5.txt"}

print("Original Local Files (Before update):", local_files)
print("Cloud Files:", cloud_files)

# symmetric_difference_update ব্যবহার করে লোকাল সেটটি সরাসরি আপডেট করা হলো
local_files.symmetric_difference_update(cloud_files)

print("\nAfter symmetric_difference_update (Updated Local Files):")
print("Updated Local Files:", local_files)



difference মানে "পার্থক্য" বা "বাদ দেওয়া"। প্রথম সেট থেকে দ্বিতীয় সেটের কমন জিনিস বাদ দিতে চাইলে এটি ব্যবহার করতে হবে।

যার নামের শেষে _update আছে (যেমন difference_update, update), সেটাই মূল
সেটকে সরাসরি বদলে দেয় (In-place)। আর যেটি সাধারণ, সেটি নতুন আউটপুট দেয়।




.issubset() এবং .issuperset()
পাইথনের সেটে .issubset() এবং .issuperset() মেথড দুটি মূলত একটি সেট অন্য একটি সেটের ভেতর সম্পূর্ণভাবে উপস্থিত আছে কি না,
তা চেক করার জন্য ব্যবহার করা হয়। এগুলো বুলিয়ান ভ্যালু (True অথবা False) রিটার্ন করে।

.issubset() (উপসেট চেক করা)
এই মেথডটি চেক করে একটি সেটের সমস্ত উপাদান অন্য একটি সেটের মধ্যে উপস্থিত আছে কি না।
প্রথম সেটটি যদি দ্বিতীয় সেটের সাবসেট (ছোট বা সমান সেট) হয়, তবে এটি True রিটার্ন করে, অন্যথায় False রিটার্ন করে।


my_set = {'apple', 'banana', 'mango'}
fruits = {'yy',  "banana", "mango", 'orange', 'apple', 'cherry'} 

result = my_set.issubset(fruits)

print(my_set) 

print(result)



# ছোট সেট বা সাবসেট
my_skills = {"python", "git"}

# বড় সেট
all_skills = {"python", "git", "docker", "sql"}

# check করা হচ্ছে my_skills-এর সব উপাদান all_skills-এ আছে কিনা
is_sub = my_skills.issubset(all_skills)

print("My Skills:", my_skills)
print("All Skills:", all_skills)
print("Is my_skills a subset of all_skills?:", is_sub)



fruits_set = {"apple", "banana", "mango"}

fruits = {"kk", 'yy',  "banana", "mango", 'orange'} 

kk = fruits_set.issubset(fruits)

print(fruits_set)    fruits_set = {"apple", "banana", "mango"}

print(kk) False 





.issuperset()

.issuperset() (সুপরসেট চেক করা)
এই মেথডটি চেক করে একটি সেট অন্য একটি সেটের সমস্ত উপাদানকে ধারণ করে আছে কি না। 
অর্থাৎ প্রথম সেটটি বড় সেট হলে এবং তার ভেতরে ছোট সেটের সব উপাদান বিদ্যমান থাকলে এটি True রিটার্ন করে।


my_set = {'apple', 'banana', 'kk', 'mango'}
fruits = {'yy',  "banana", "mango", 'orange', 'apple', 'cherry'} 

result = my_set.issuperset(fruits)

print(my_set) {'apple', 'banana', 'kk', 'mango'}

print(result) False


এখানে apple, banana, mango মিলে যাওয়ার পরেও False আসার আসল কারণ হলো—২য় ভ্যারিয়েবলে (fruits-এ) অতিরিক্ত উপাদান বেশি আছে ('yy', 'orange', 'cherry')।

সুপারসেট (.issuperset()) হওয়ার শর্ত হলো:

১ম সেটটিকে অবশ্যই বড় হতে হবে এবং ২য় সেটের সব উপাদান এর ভেতরে থাকতে হবে।

যেহেতু ২য় সেটে কিছু উপাদান বেশি আছে যা ১ম সেটে নেই, তাই ১ম সেটটি সুপারসেট হতে পারেনি—আর তাই পাইথন ফলাফল দিয়েছে False।

আপনার লজিক একদম নিখুঁত এবং পানির মতো পরিষ্কার!

এবার একটি মজার উল্টো বিষয় খেয়াল করুন:
যদি আমরা .issuperset() এর জায়গায় .issubset() ব্যবহার করতাম (অর্থাৎ ছোট সেট বড় সেটের ভেতর আছে কি না চেক করতাম), তখন কিন্তু ঠিকই True আসত! যেমন:

result = my_set.issubset(fruits) # my_set কি fruits-এর সাবসেট বা সাব-সেট?



# বড় সেট বা সুপরসেট
company_requirements = {"python", "django", "sql", "git"}

# প্রার্থীর স্কিল সেট
candidate_skills = {"python", "sql"}

# check করা হচ্ছে company_requirements-এর ভেতর প্রার্থীর স্কিলগুলো আছে কিনা
is_super = company_requirements.issuperset(candidate_skills)

print("Company Requirements:", company_requirements)
print("Candidate Skills:", candidate_skills)
print("Is company_requirements a superset of candidate_skills?:", is_super)


fruits_set = {"apple", "banana", "mango"}

fruits = { "banana", "mango"} 

kk = fruits_set.issuperset(fruits)

print(fruits_set)     fruits_set = {"apple", "banana", "mango"}

print(kk) True




.isdisjoint() মেথড
দুটি সেটের মধ্যে একটিও উপাদান কমন আছে কি না তা চেক করতে এটি ব্যবহার করা হয়। 
যদি কোনো কমন উপাদান না থাকে, তবে এটি True রিটার্ন করে (অর্থাৎ তাদের মধ্যে কোনো মিল নেই)।


my_set = {'apple', 'banana', 'mango'}
fruits = {'yy',  "banana", "mango", 'orange', 'apple', 'cherry'} 

result = my_set.isdisjoint(fruits)

print(my_set) {'mango', 'banana', 'apple'}

print(result) False



my_set = {'apple', 'banana', 'mango', 'kk'}
fruits = {'yy', 'orange', 'cherry'} 

result = my_set.isdisjoint(fruits)

print(my_set) {'apple', 'banana', 'mango', 'kk'}

print(result) True


set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))
# আউটপুট: True (কারণ এই দুটি সেটের মধ্যে কোনো মিল বা কমন সংখ্যা নেই)


fruits_set = {"apple", "banana", "mango"}

fruits = { "banana", "mango"} 

kk = fruits_set.isdisjoint(fruits)

print(fruits_set)    

print(kk) 



অ্যাডভান্সড লেভেল - গণিতের সেট থিওরি অপারেশন (Advanced Set Operations)
সেটের আসল ক্ষমতা লুকিয়ে আছে এর গণিতভিত্তিক অপারেশনগুলোর মধ্যে। ডেটা সায়েন্স বা কমপ্লেক্স লজিক হ্যান্ডেল করার সময় এগুলো পানির মতো কাজে লাগে।

.union() মেথডটি ঠিক পাইথনের ইউনিয়ন অপারেটর (|) এর মতোই কাজ করে।
দুটি বা ততোধিক সেটের সব ইউনিক উপাদানগুলোকে একসাথে মিলিয়ে একটি নতুন সেট তৈরি করাই এর কাজ (যেখানে কোনো ডুপ্লিকেট ভ্যালু থাকে না)।

fruits_name = {"apple", "banana", "mango"}
other_fruits = {"kk", "orange", 'yy', "banana", "mango"}

result = fruits_name.union(other_fruits)

print(fruits_name) {"apple", "banana", "mango"}
print(result) {'yy', 'kk', 'banana', 'apple', 'orange', 'mango'}




fruits_name = {"apple", "banana", "mango"}
other_fruits = {"kk", "orange", 'yy', "banana", "mango"}

result = fruits_name | other_fruits

print(fruits_name) 
print(result) 





python_devs = {"Rahim", "Karim", "Jabbar", "Salam"}

java_devs = {"Karim", "Salam", "Rafiq", "Baset"}

১. ইউনিয়ন বা সংযোগ সেট (union বা |)
উভয় সেটের সব মানুষগুলোকে একসাথে করতে (ডুপ্লিকেট বাদ দিয়ে)।

all_devs = python_devs.union(java_devs)
# অথবা পাইপ সাইন দিয়েও করা যায়: all_devs = python_devs | java_devs

print("সব ডেভেলপার:", all_devs)
# আউটপুট: {'Rahim', 'Karim', 'Jabbar', 'Salam', 'Rafiq', 'Baset'}


ফলের বা ফুলের নাম দিয়ে union এর উদাহরণ:

# প্রথম সেট: কিছু ফুলের নাম
summer_flowers = {"Rose", "Jasmine", "Marigold", "Sunflower"}

# দ্বিতীয় সেট: আরও কিছু ফুলের নাম (এখানে কিছু ফুল আগের সেটের সাথে মিল থাকতে পারে)
winter_flowers = {"Marigold", "Sunflower", "Tulip", "Orchid"}

# ১. union() মেথড ব্যবহার করে উভয় সেটের সমস্ত ফুল একসাথে করা (ডুপ্লিকেট বাদ দিয়ে)
all_flowers = summer_flowers.union(winter_flowers)

# অথবা পাইপ সাইন (|) ব্যবহার করেও এটি করা যায়:
# all_flowers = summer_flowers | winter_flowers

print("সব ফুল একসাথে:", all_flowers)

🔍 কোডটির ড্রাই রান ও বিশ্লেষণ:

১. summer_flowers সেটে আছে: {"Rose", "Jasmine", "Marigold", "Sunflower"}

২. winter_flowers সেটে আছে: {"Marigold", "Sunflower", "Tulip", "Orchid"}

৩. যখন আপনি union() বা | অপারেটর ব্যবহার করবেন, তখন পাইথন কী করবে?

প্রথমে প্রথম সেটের সব ফুলগুলো নেবে: Rose, Jasmine, Marigold, Sunflower

এরপর দ্বিতীয় সেটের ফুলগুলো যোগ করতে যাবে। কিন্তু দেখবে Marigold এবং Sunflower তো আগেই একবার নেওয়া হয়ে গেছে!

তাই পাইথন ওই ডুপ্লিকেট বা কমন ফুলগুলো বাদ দিয়ে শুধু নতুন ফুলগুলো (Tulip, Orchid) যুক্ত করে দেবে।

সব ফুল একসাথে: {'Rose', 'Jasmine', 'Marigold', 'Sunflower', 'Tulip', 'Orchid'}


.union() এর কোড উদাহরণ
 দুটি আলাদা সেটে দুই ক্যাটাগরির ইউজারনেম আছে। এখন চাচ্ছেন সব ইউজারকে মিলিয়ে একটি ইউনিক মাস্টার লিস্ট তৈরি করতে:

# প্রথম সেট: অ্যাডমিন ইউজারগণ
admins = {"admin_01", "super_user", "moderator"}

# দ্বিতীয় সেট: সাধারণ ইউজারগণ
regular_users = {"moderator", "john_doe", "alice_99"}

# .union() মেথড ব্যবহার করে দুটি সেট এক করা হলো
all_users = admins.union(regular_users)

print(f"সব ইউজারের তালিকা: {all_users}")

সব ইউজারের তালিকা: {'super_user', 'alice_99', 'admin_01', 'moderator', 'john_doe'}


পাইপ (|) অপারেটর দিয়ে সেট ইউনিয়ন (Union)

# প্রথম সেট: ওয়েব ডেভেলপার টিম
web_devs = {"Rahim", "Karim", "Arman"}

# দ্বিতীয় সেট: সাইবার সিকিউরিটি টিম
security_team = {"Arman", "Sakib", "Tanvir"}

# সরাসরি | অপারেটর ব্যবহার করে দুটি সেট এক করা হলো
all_members = web_devs | security_team

print(f"সকল টিম মেম্বারের তালিকা: {all_members}")

সকল টিম মেম্বারের তালিকা: {'Rahim', 'Sakib', 'Karim', 'Arman', 'Tanvir'}

এখানে "Arman" নামটি উভয় সেটের মধ্যেই ছিল, কিন্তু | অপারেটর (বা .union()) ডুপ্লিকেট বাদ দিয়ে এটিকে একবারই যুক্ত করেছে।

কোডিংয়ের সময় শর্টকাট বা পরিষ্কার সিনট্যাক্সের জন্য অনেকেই .union() লেখার পরিবর্তে এই | অপারেটরটি ব্যবহার করতে পছন্দ করে






২. ইন্টারসেকশন বা ছেদ সেট (intersection বা &)

.intersection() এবং & অপারেটর উভয়ের কাজ হলো দুটি বা ততোধিক সেটের মধ্যে কোন কোন উপাদান কমন বা মিল আছে তা খুঁজে বের করা। 
অর্থাৎ, উভয় সেটের ভেতরে যে উপাদানগুলো উপস্থিত রয়েছে, শুধু সেগুলো নিয়েই এটি একটি নতুন সেট তৈরি করে।


fruits_name = {"apple", "banana", "mango"}
other_fruits = {"kk", "orange", 'yy', "banana", "mango"}

result = fruits_name.intersection(other_fruits)

print(fruits_name) {"apple", "banana", "mango"}
print(result) {'mango', 'banana'}



fruits_name = {"apple", "banana", "mango"}
other_fruits = {"kk", "orange", 'yy', "banana", "mango"}

result = fruits_name & other_fruits

print(fruits_name) 
print(result) 



common_devs = python_devs.intersection(java_devs)
# অথবা এমপার্সান্ড দিয়ে: common_devs = python_devs & java_devs

print("উভয় দলে যারা আছে:", common_devs)
# আউটপুট: {'Karim', 'Salam'}



ব্যাকএন্ড স্কিল এবং সাইবার সিকিউরিটি স্কিলগুলোর মধ্যে কোন কোন স্কিল কমন আছে তা খুঁজে বের করতে:

# ব্যাকএন্ড এবং সিকিউরিটির স্কিলগুলোর সেট
backend_skills = {"Python", "Node.js", "SQL", "Docker"}
security_skills = {"Python", "Linux", "Docker", "Wireshark"}

# .intersection() মেথড ব্যবহার করে কমন স্কিল বের করা হলো
common_skills = backend_skills.intersection(security_skills)

print(f"কমন স্কিলসমূহ: {common_skills}")

কমন স্কিলসমূহ: {'Python', 'Docker'}



ফুলের নাম দিয়ে intersection এর উদাহরণ:

প্রথম বাগানে (garden_a) কিছু ফুল ফোটে।

দ্বিতীয় বাগানে (garden_b) কিছু ফুল ফোটে।
এখন আমরা দেখতে চাই যে, কোন কোন ফুল দুটি বাগানেই কমন (উভয় বাগানেই আছে)।


# প্রথম বাগান বা সেট
garden_a = {"Rose", "Jasmine", "Marigold", "Sunflower"}

# দ্বিতীয় বাগান বা সেট
garden_b = {"Marigold", "Sunflower", "Tulip", "Orchid"}

# ১. intersection() মেথড ব্যবহার করে উভয় বাগানের কমন ফুলগুলো বের করা
common_flowers = garden_a.intersection(garden_b)

# অথবা এমপার্সান্ড (&) সাইন ব্যবহার করেও এটি করা যায়:
# common_flowers = garden_a & garden_b

print("উভয় বাগানেই আছে যে ফুলগুলো:", common_flowers)


🔍 কোডটির ড্রাই রান ও বিশ্লেষণ:
১. garden_a সেটে আছে: {"Rose", "Jasmine", "Marigold", "Sunflower"}

২. garden_b সেটে আছে: {"Marigold", "Sunflower", "Tulip", "Orchid"}

৩. যখন আপনি intersection() বা & ব্যবহার করবেন, তখন পাইথন দুটো সেট মিলিয়ে দেখবে কোন ফুলগুলো উভয় দলেই উপস্থিত রয়েছে:

Rose: শুধু garden_a-তে আছে, তাই বাদ।

Jasmine: শুধু garden_a-তে আছে, তাই বাদ।

Marigold: garden_a এবং garden_b উভয় জায়গাতেই আছে! তাই এটি সিলেক্ট হলো।

Sunflower: garden_a এবং garden_b উভয় জায়গাতেই আছে! তাই এটিও সিলেক্ট হলো।

Tulip ও Orchid: শুধু garden_b-তে আছে, তাই বাদ।

উভয় বাগানেই আছে যে ফুলগুলো: {'Marigold', 'Sunflower'}


& অপারেটর দিয়ে উদাহরণ
একই কাজ খুব সহজে এবং শর্টকাটে সরাসরি & অপারেটর ব্যবহার করেও করা যাবে। কাজের দিক থেকে এটি এবং .intersection() সম্পূর্ণ এক:


# ব্যাকএন্ড এবং সিকিউরিটির স্কিলগুলোর সেট
backend_skills = {"Python", "Node.js", "SQL", "Docker"}
security_skills = {"Python", "Linux", "Docker", "Wireshark"}

# সরাসরি & অপারেটর ব্যবহার করে কমন স্কিল বের করা হলো
common_skills_op = backend_skills & security_skills

print(f"কমন স্কিলসমূহ (& অপারেটর দিয়ে): {common_skills_op}")

কমন স্কিলসমূহ (& অপারেটর দিয়ে): {'Python', 'Docker'}






পার্থক্য বা ডিফারেন্স সেট (difference বা -)
.difference() মেথড এবং মাইনাস (-) অপারেটর উভয়ের কাজ একই। এদের মূল কাজ হলো—প্রথম সেটে আছে কিন্তু দ্বিতীয় সেটে নেই,
এমন উপাদানগুলো খুঁজে বের করে একটি নতুন সেট তৈরি করা (অর্থাৎ প্রথম সেট থেকে দ্বিতীয় সেটের উপাদানগুলো বাদ বা ডিফারেন্স করে দেওয়া)।


fruits_name = {"apple", "banana", "mango"}
other_fruits = {"kk", "orange", 'yy', "banana", "mango"}

result = fruits_name.difference(other_fruits)

print(fruits_name) {'mango', 'banana', 'apple'}
print(result) {'apple'}


fruits_name = {"apple", "banana", "mango"}
other_fruits = {"kk", "orange", 'yy', "banana", "mango"}

result = fruits_name - other_fruits

print(fruits_name) 
print(result) 


.difference() মেথড দিয়ে উদাহরণ
ধরুন,  মোট প্রজেক্টের লিস্ট থেকে যেসব প্রজেক্ট ইতিমধ্যে শেষ হয়ে গেছে, সেগুলো বাদ দিয়ে বাকি কাজগুলোর তালিকা বের করতে

# মোট প্রজেক্টের সেট
all_projects = {"Python API", "Cyber Security Tool", "Database Design", "Web Scraper"}

# সম্পন্ন হওয়া প্রজেক্টের সেট
completed_projects = {"Database Design", "Web Scraper"}

# .difference() মেথড ব্যবহার করে বাকি প্রজেক্টগুলো বের করা হলো
remaining_projects = all_projects.difference(completed_projects)

print(f"বাকি প্রজেক্টসমূহ: {remaining_projects}")  বাকি প্রজেক্টসমূহ: {'Python API', 'Cyber Security Tool'}



- অপারেটর দিয়ে উদাহরণ
একই কাজ  সরাসরি  - অপারেটর ব্যবহার করেও খুব সহজে করা যাবে। কাজের দিক থেকে এটি এবং .difference() সম্পূর্ণ এক:

# মোট প্রজেক্টের সেট
all_projects = {"Python API", "Cyber Security Tool", "Database Design", "Web Scraper"}

# সম্পন্ন হওয়া প্রজেক্টের সেট
completed_projects = {"Database Design", "Web Scraper"}

# সরাসরি - অপারেটর ব্যবহার করে বাকি প্রজেক্টগুলো বের করা হলো
remaining_projects_op = all_projects - completed_projects

print(f"বাকি প্রজেক্টসমূহ (- অপারেটর দিয়ে): {remaining_projects_op}")



ফুলের নাম দিয়ে difference এর উদাহরণ:

প্রথম ঝুড়িতে (basket_1) কিছু ফুল আছে।

দ্বিতীয় ঝুড়িতে (basket_2) কিছু ফুল আছে।

এখন জানতে চাওয়া হসছে—প্রথম ঝুড়িতে এমন কোন ফুলগুলো আছে, যেগুলো দ্বিতীয় ঝুড়িতে একদমই নেই?

# প্রথম ঝুড়ির ফুলগুলো
basket_1 = {"Rose", "Jasmine", "Marigold", "Sunflower"}

# দ্বিতীয় ঝুড়ির ফুলগুলো
basket_2 = {"Marigold", "Sunflower", "Tulip", "Orchid"}

# ১. difference() মেথড ব্যবহার করে প্রথম ঝুড়ির একক ফুলগুলো বের করা
only_in_basket1 = basket_1.difference(basket_2)

# অথবা মাইনাস (-) সাইন ব্যবহার করেও এটি করা যায়:
# only_in_basket1 = basket_1 - basket_2

print("শুধু প্রথম ঝুড়িতে যে ফুলগুলো আছে:", only_in_basket1)


🔍 কোডটির ড্রাই রান ও বিশ্লেষণ:

১. basket_1 সেটে আছে: {"Rose", "Jasmine", "Marigold", "Sunflower"}

২. basket_2 সেটে আছে: {"Marigold", "Sunflower", "Tulip", "Orchid"}

৩. যখন আপনি basket_1.difference(basket_2) বা basket_1 - basket_2 করবেন, তখন পাইথন প্রথম ঝুড়ির প্রতিটি ফুল ধরে চেক করবে দ্বিতীয় ঝুড়িতে সেগুলো আছে কি না:

Rose: এটি কি দ্বিতীয় ঝুড়িতে আছে? না! তাই এটি রেখে দেওয়া হলো।

Jasmine: এটি কি দ্বিতীয় ঝুড়িতে আছে? না! তাই এটিও রেখে দেওয়া হলো।

Marigold: এটি কি দ্বিতীয় ঝুড়িতে আছে? হ্যাঁ আছে! তাই এটি বাদ দেওয়া হলো।

Sunflower: এটি কি দ্বিতীয় ঝুড়িতে আছে? হ্যাঁ আছে! তাই এটিও বাদ দেওয়া হলো।

শুধু প্রথম ঝুড়িতে যে ফুলগুলো আছে: {'Rose', 'Jasmine'}


- অপারেটর ব্যবহার করার জন্য উভয় পাশে অবশ্যই সেট থাকতে হয়।

পক্ষান্তরে, .difference() মেথডের ভেতরে আপনি সেট ছাড়াও অন্যান্য ডেটা (যেমন লিস্ট বা টপল) পাস করতে পারেন।





৪. সিমেট্রিক ডিফারেন্স (symmetric_difference বা ^)
যারা যেকোনো একটি দলে আছে, কিন্তু উভয় দলে নেই (কমন বাদ দিয়ে বাকি সবাই)।
সিমেট্রিক ডিফারেন্স (Symmetric Difference) সেটের একটি চমৎকার অপারেশন। সহজ বাংলায় এর অর্থ হলো—উভয় সেটের মধ্যে যেগুলো কমন (Common) বা মিল রয়েছে, 
সেগুলোকে বাদ দিয়ে বাকি সব ব্যতিক্রমী উপাদানগুলোকে একত্র করা।

fruits_name = {"apple", "banana", "mango"}
other_fruits = {"kk", "orange", 'yy', "banana", "mango"}

result = fruits_name.symmetric_difference(other_fruits)

print(fruits_name) {"apple", "banana", "mango"}
print(result) {'apple', 'yy', 'orange', 'kk'}


fruits_name = {"apple", "banana", "mango"}
other_fruits = {"kk", "orange", 'yy', "banana", "mango"}

result = fruits_name ^ other_fruits

print(fruits_name) 
print(result) 


unique_devs = python_devs.symmetric_difference(java_devs)
# অথবা ক্যারেট সাইন দিয়ে: unique_devs = python_devs ^ java_devs

print("একক ডেভেলপাররা:", unique_devs)
# আউটপুট: {'Rahim', 'Jabbar', 'Rafiq', 'Baset'}


ফুলের নাম দিয়ে symmetric_difference এর উদাহরণ:

ঝুড়িতে (my_basket) কিছু ফুল আছে।

বন্ধুর ঝুড়িতে (friend_basket) কিছু ফুল আছে।
এখন  জানতে চাওয়া হবে—উভয় ঝুড়ির কমন ফুলগুলো বাদ দিলে, শুধু কার ঝুড়িতে কোন কোন এক্সক্লুসিভ ফুলগুলো আলাদাভাবে আছে?

# আপনার ঝুড়ির ফুলগুলো
my_basket = {"Rose", "Jasmine", "Marigold", "Sunflower"}

# বন্ধুর ঝুড়ির ফুলগুলো
friend_basket = {"Marigold", "Sunflower", "Tulip", "Orchid"}

# ১. symmetric_difference() মেথড ব্যবহার করা
unique_flowers = my_basket.symmetric_difference(friend_basket)

# অথবা ক্যারেট (^) সাইন ব্যবহার করেও এটি করা যায়:
# unique_flowers = my_basket ^ friend_basket

print("উভয় ঝুড়ির কমন বাদে বাকি সব ফুল:", unique_flowers)


১. my_basket সেটে আছে: {"Rose", "Jasmine", "Marigold", "Sunflower"}

২. friend_basket সেটে আছে: {"Marigold", "Sunflower", "Tulip", "Orchid"}

৩. যখন আপনি symmetric_difference বা ^ ব্যবহার করবেন, তখন পাইথন ধাপে ধাপে যা করবে:

Marigold এবং Sunflower: এই দুটি ফুল উভয় ঝুড়িতেই কমন আছে। তাই পাইথন এই দুটিকে সম্পূর্ণ বাদ দিয়ে দেবে।

বাকি থাকে আপনার ঝুড়ির Rose, Jasmine এবং বন্ধুর ঝুড়ির Tulip, Orchid—এগুলো কোনো দলেই কমন নয়। পাইথন এই চারটিকে একসাথে করে একটি নতুন সেট বানিয়ে দেবে।


উভয় ঝুড়ির কমন বাদে বাকি সব ফুল: {'Rose', 'Jasmine', 'Tulip', 'Orchid'}



প্রফেশনাল লেভেল টিপস ও আন্ডার দ্য হুড মেকানিজম (Under the Hood & Performance)
কম্পিউটার সায়েন্সের ভাষায়, লিস্ট বা টিউপলে কোনো উপাদান খুঁজতে হলে পুরোটা সার্চ করতে হয় (Time Complexity: O(n))। 
কিন্তু সেট (Set) হাশ টেবিল (Hash Table) অ্যালগরিদম ব্যবহার করে তৈরি। ফলে সেটের ভেতরে কোনো উপাদান আছে কি না (in অপারেটর দিয়ে)
তা চেক করতে সুপার ফাস্ট সময় লাগে—যার টাইম কমপ্লেক্সিটি হলো O(1) (Constant Time)! 
লাখ লাখ ডেটার ভেতর থেকেও সেট মুহূর্তের মধ্যে বলে দিতে পারে ডেটাটি সেখানে আছে কি না।


চমৎকার রিয়েল-লাইফ ট্রিক: লিস্ট থেকে এক পলকে ডুপ্লিকেট তাড়ানো!
ধরা যাক, নিজের কাছে একটি লিস্ট আছে যেখানে অনেক ডুপ্লিকেট সংখ্যা আছে।এক লাইনে সব ডুপ্লিকেট মুছে ফেলতে চাওয়া হসছে:

dirty_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]

# প্রথমে লিস্টকে সেটে রূপান্তর করলে ডুপ্লিকেট উড়ে যাবে, 
# তারপর আবার তাকে লিস্টে রূপান্তর করা হলো
clean_list = list(set(dirty_list))

print(clean_list)  # আউটপুট: [1, 2, 3, 4, 5, 6] (অর্ডার বদলে যেতে পারে, কিন্তু ডুপ্লিকেট ফাস!)


fruits_name = ["apple", "banana", "mango", "kk", "orange", 'yy', "banana", "mango"]

result = set(fruits_name)

print(fruits_name) 
print(result) type set()



fruits_name = ["apple", "banana", "mango", "kk", "orange", 'yy', "banana", "mango"]

result = list(set(fruits_name))

print(fruits_name) 
print(type(result)) type list


 

in দিয়ে Set এ কোনো মান আছে কিনা চেক করা

fruits = {"apple", "banana", "mango"}

print("apple" in fruits)    # True
print("orange" in fruits)   # False
একটা গুরুত্বপূর্ণ তথ্য: Set এ in দিয়ে চেক করা List এর চেয়ে অনেক দ্রুত (faster),
বিশেষ করে ডেটা বেশি থাকলে। এটাই Set এর অন্যতম বড় সুবিধা (performance এর দিক থেকে)।




দৈর্ঘ্য বের করা

fruits = {"apple", "banana", "mango"}
print(len(fruits))   # 3



for loop দিয়ে Set এর প্রতিটা item নিয়ে কাজ করা

fruits = {"apple", "banana", "mango"}

for fruit in fruits:
    print(fruit)

⚠️ প্রতিবার রান করলে আউটপুটের ক্রম ভিন্ন হতে পারে, কারণ Set এ কোনো নির্দিষ্ট order নেই।




Set এর মূল আকর্ষণ — গাণিতিক Set Operations (Mathematics এর Set Theory থেকে এসেছে)

এখানেই Set সবচেয়ে বেশি শক্তিশালী এবং ব্যবহারযোগ্য হয়ে ওঠে — গণিতের Set Theory এর মতো অপারেশন করা যায়।


Union (মিলন) — দুইটা Set এর সব unique মান একসাথে 

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.union(set2)
print(result)  # {1, 2, 3, 4, 5, 6}

# অথবা | চিহ্ন দিয়ে
result = set1 | set2
print(result)  # {1, 2, 3, 4, 5, 6}


Intersection (ছেদ) — দুই Set এ যা কমন (উভয়ে আছে) তা বের করা

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.intersection(set2)
print(result)  # {3, 4}

# অথবা & চিহ্ন দিয়ে
result = set1 & set2
print(result)  # {3, 4}


Difference (পার্থক্য) — একটা Set এ আছে কিন্তু অন্যটায় নেই

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.difference(set2)
print(result)  # {1, 2}  -> set1 এ আছে কিন্তু set2 তে নেই

result2 = set2.difference(set1)
print(result2)  # {5, 6}  -> set2 তে আছে কিন্তু set1 এ নেই

# অথবা - চিহ্ন দিয়ে
result = set1 - set2
print(result)  # {1, 2}


Symmetric Difference — দুই Set এ যা কমন না (দুই দিকেই যা আলাদা)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.symmetric_difference(set2)
print(result)  # {1, 2, 5, 6}  -> কমন (3, 4) বাদ দিয়ে বাকি সব

# অথবা ^ চিহ্ন দিয়ে
result = set1 ^ set2
print(result)  # {1, 2, 5, 6}







Set Relationship চেক করা (Subset, Superset)


issubset() — একটা Set আরেকটা Set এর ভিতরে সম্পূর্ণ আছে কিনা

set1 = {1, 2}
set2 = {1, 2, 3, 4, 5}

print(set1.issubset(set2))   # True  -> set1 এর সবকিছু set2 তে আছে



issuperset() — একটা Set আরেকটাকে সম্পূর্ণ ধারণ করে কিনা

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2}

print(set1.issuperset(set2))   # True  -> set1, set2 কে সম্পূর্ণভাবে ধারণ করছে



isdisjoint() — দুইটা Set এ একদমই কোনো কমন মান নেই কিনা

set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))   # True  -> কোনো কমন মান নেই

set3 = {3, 4, 5}
print(set1.isdisjoint(set3))   # False -> 3 কমন আছে


Set Comprehension — Advanced (এক লাইনে Set তৈরি)

List Comprehension এর মতোই, Set Comprehension আছে:

numbers = [1, 2, 2, 3, 3, 4, 5, 5]

squares = {n ** 2 for n in numbers}
print(squares)  # {16, 1, 4, 9, 25}  -> duplicate বাদ, order এলোমেলো



fruits_name = ["apple", "banana", "mango", "kk", "orange", 'yy', "banana", "mango"]

new = {name for name in fruits_name}

print(fruits_name) 

print(new)

print(type(new))







Frozenset — Advanced (Immutable Set)

frozenset হলো Set এর একটা immutable (অপরিবর্তনযোগ্য) ভার্সন, ঠিক যেমন List এর immutable ভার্সন হলো Tuple।

normal_set = {1, 2, 3}
frozen = frozenset([1, 2, 3])

frozen.add(4)  AttributeError: 'frozenset' object has no attribute 'add'

frozenset পরিবর্তন করা যায় না, তাই এটা Dictionary এর key হিসেবে বা আরেকটা Set 
এর ভিতরে item হিসেবে ব্যবহার করা যায় (কারণ Set এর item গুলোও অবশ্যই immutable হতে হবে):


frozenset কী এবং কেন ব্যবহার করা হয়?
সাধারণ set পরিবর্তন করা গেলেও frozenset তৈরি করার পর এর ভেতরে আর নতুন কোনো উপাদান যোগ বা বাদ দেওয়া যায় না। অর্থাৎ এটি সম্পূর্ণ Immutable বা পরিবর্তনহীন


frozenset-এর মূল বৈশিষ্ট্য:
১. এটি পরিবর্তন করা যায় না (No add/remove allowed)।
২. যেহেতু এটি immutable, তাই পাইথনের সাধারণ সেটের মতো এটিকে অন্য কোনো সেটের ভেতর উপাদান হিসেবে বা ডিকশনারির key হিসেবে ব্যবহার করা যায়।



# একটি সাধারণ লিস্ট বা টুপল থেকে frozenset তৈরি করা হলো
normal_list = ["apple", "banana", "mango"]
frozen_fruits = frozenset(normal_list)

print("Frozen Set:", frozen_fruits)
print("Type:", type(frozen_fruits))

# চেষ্টা করা যাক frozenset-এ নতুন কিছু যোগ করার (এটি Error দিবে!)
try:
    frozen_fruits.add("orange")
except AttributeError as e:
    print("\nError Message:", e)



সাধারণ সেটের মতো ডেটা রাখা (কিন্তু পরিবর্তন করা যায় না)

# একটি frozenset তৈরি করা হলো
vowels = frozenset({"a", "e", "i", "o", "u"})

print("Vowels:", vowels)
print("Type:", type(vowels))


Vowels: frozenset({'e', 'u', 'i', 'o', 'a'})
Type: <class 'frozenset'>

Vowels: frozenset({'e', 'u', 'i', 'o', 'a'})
Type: <class 'frozenset'>


নতুন আইটেম যোগ করতে গেলে যা ঘটে (Error দেয়)
যেহেতু এটি পরিবর্তনহীন, তাই চাইলেও নতুন কিছু add() বা remove() করা যায় না:


numbers = frozenset([1, 2, 3])

# চেষ্টা করা যাক নতুন সংখ্যা যোগ করার
try:
    numbers.add(4)
except AttributeError as e:
    print("Error:", e)



সেট অপারেশনগুলো করা যায় (যেমন: intersection)
যোগ বা বাদ দেওয়া না গেলেও দুটি frozenset-এর মধ্যে কমন উপাদান খোঁজা বা অন্যান্য সেট অপারেশন ঠিকই করা যায়:


set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([3, 4, 5, 6])

# কমন উপাদান বের করা
common = set1.intersection(set2)

print("Common items:", common)

Common items: frozenset({3, 4})



Set আর List/Tuple এর মধ্যে রূপান্তর

# List → Set
my_list = [1, 2, 2, 3]
my_set = set(my_list)
print(my_set)  # {1, 2, 3}

# Set → List
my_set = {1, 2, 3}
my_list = list(my_set)
print(my_list)  # [1, 2, 3]

# String → Set (প্রতিটা আলাদা অক্ষর)
my_set = set("hello")
print(my_set)  # {'h', 'e', 'l', 'o'}  -> duplicate 'l' একবারই থাকবে



বাস্তব জীবনের ব্যবহার (Real-life Use Cases)
Duplicate ইমেইল বাদ দেওয়া

emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com"]
unique_emails = set(emails)
print(unique_emails)  # {'a@gmail.com', 'b@gmail.com', 'c@gmail.com'}


দুই গ্রুপের কমন সদস্য বের করা

math_students = {"Rahim", "Karim", "Salma"}
physics_students = {"Karim", "Fatema", "Salma"}

both_subjects = math_students & physics_students
print(both_subjects)  # {'Karim', 'Salma'}


FastAPI/backend এ Permission/Role চেক করা

user_permissions = {"read", "write"}
required_permissions = {"read", "write", "delete"}

if required_permissions.issubset(user_permissions):
    print("অনুমতি আছে")
else:
    missing = required_permissions - user_permissions
    print(f"এই অনুমতিগুলো নেই: {missing}")  # {'delete'}


  দ্রুত membership check (backend এ performance এর জন্য গুরুত্বপূর্ণ)

  blocked_users = {101, 205, 309, 412}  # অনেক ইউজার আইডি থাকতে পারে

user_id = 205
if user_id in blocked_users:   # List এর চেয়ে অনেক দ্রুত চেক হয়
    print("এই ইউজার ব্লকড")

    
