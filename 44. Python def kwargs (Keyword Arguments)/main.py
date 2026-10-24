পাইথনের **kwargs (Keyword Arguments) হলো এমন একটি শক্তিশালী ফিচার, যার মাধ্যমে ফাংশনে নামসহ (Key-Value Pair) ইচ্ছামতো ডেটা পাস করা যায়।

এটি একটি function কে নামযুক্ত (key=value) যেকোনো সংখ্যক argument নিতে দেয়। ভেতরে এগুলো একটি dictionary হিসেবে আসে।

kwargs নামটি একটি সাধারণ convention। আপনি **data, **options ইত্যাদিও লিখতে পারেন। তবে ** চিহ্নটিই আসল

**kwargs আসলে কী এবং কেন?
  
যখন  ফাংশন ডিফাইন করার সময় প্যারামিটারে **kwargs (দুটি স্টার বা অ্যাস্টারিস্ক সহ) ব্যবহার করা হয়, 
তখন পাইথন বাইরে থেকে পাঠানো সমস্ত নামযুক্ত আর্গুমেন্টকে স্বয়ংক্রিয়ভাবে একটি ডিকশনারি (Dictionary)-তে প্যাক করে ফেলে।

এর প্রধান সুবিধা হলো: ফাংশন কল করার আগে আগে থেকে ঠিক করে রাখতে হয় না যে কয়টি প্যারামিটার লাগবে। ইউজার ইচ্ছামতো কি-ভ্যালু জোড়া পাঠাতে পারে।


১. সাধারণ তথ্য প্রিন্ট করা (Basic Information Printer)
সবচেয়ে সহজ উদাহরণ হলো যেকোনো কি-ভ্যালু জোড়া রিসিভ করে তা সরাসরি প্রিন্ট করা।

def print_user_profile(**kwargs):
    print("Received Data Type:", type(kwargs))
    print("Content:", kwargs)

# টেস্ট করা যাক:
print_user_profile(username="Abdullah", age=30, role="Backend Developer")

১. লাইন ১: def print_user_profile(**kwargs):
কী ঘটল: পাইথন ইন্টারপ্রেটার যখন এই লাইনে আসে, তখন সে দেখে একটি ফাংশন ডিফাইন (Define) করা হচ্ছে।

কীভাবে কাজ করল:

পাইথন মেমরিতে print_user_profile নামে একটি ফাংশন অবজেক্ট তৈরি করে রাখে।

প্যারামিটারে দেওয়া **kwargs-এর ** (ডাবল স্টার) চিহ্ন নির্দেশ করে এটি Arbitrary Keyword Arguments গ্রহণ করবে।

অর্থাৎ, এই ফাংশনে যতগুলোই Key=Value আকারের ডেটা পাঠানো হবে, পাইথন সেগুলোকে নিয়ে একটি ডিকশনারি (dict) বানিয়ে kwargs নামক ভেরিয়েবলে রেখে দেবে।

ফলাফল: ফাংশনটি ডিফাইন হয়ে মেমরিতে রেজিস্টার্ড হয়, কিন্তু এর ভেতরের কোড এখনো এক্সিকিউট (রান) হয় না।

২. লাইন ২: print("Received Data Type:", type(kwargs))
কী ঘটল: এই লাইনটি ফাংশনের বডির (Body) প্রথম অংশ। তবে ফাংশন কল না হওয়া পর্যন্ত ইন্টারপ্রেটার এটিকে স্কিপ করে পরবর্তী লাইনে চলে যায়।

৩. লাইন ৩: print("Content:", kwargs)
কী ঘটল: এটি ফাংশনের দ্বিতীয় লাইন। এটিও ফাংশন কল হওয়া পর্যন্ত অপেক্ষা করে।

৪. লাইন ৪: # টেস্ট করা যাক:
কী ঘটল: এটি একটি কমেন্ট (Comment)।

কীভাবে কাজ করল: পাইথন ইন্টারপ্রেটার কমেন্ট লাইনকে সম্পূর্ণ উপেক্ষা (Skip) করে পরবর্তী লাইনে চলে যায়।

৫. লাইন ৫: print_user_profile(username="Abdullah", age=30, role="Backend Developer")
কী ঘটল: এটি অ্যাকচুয়াল এক্সিকিউশন লাইন বা ফাংশন কল (Function Call)।

কীভাবে কাজ করল:

পাইথন print_user_profile ফাংশনটিকে তার প্যারামিটারসহ কল করে।

প্যারামিটারে ৩টি Keyword Argument পাঠানো হয়েছে:

username = "Abdullah"

age = 30

role = "Backend Developer"

মেমোরি প্রসেসিং (**kwargs প্যাকেজিং): পাইথন এই ৩টি Key=Value জোড়াকে একসাথে প্যাক (Pack) করে একটি Dictionary বানায়:


kwargs = {
    'username': 'Abdullah',
    'age': 30,
    'role': 'Backend Developer'
}


এখন কন্ট্রোল (Control) লাইন ১-এ ফাংশনের ভেতরে প্রবেশ করে।


৬. ফাংশনের ভেতর প্রবেশ করে লাইন ২ চালানো:
কোড: print("Received Data Type:", type(kwargs))

কীভাবে কাজ করল:

পাইথন প্রথমে type(kwargs) চেক করে। যেহেতু kwargs একটি ডিকশনারি, তাই type(kwargs) এর মান বের হয় <class 'dict'>।

এরপর print() ফাংশন কনসোলে বা স্ক্রিনে টেক্সটটি প্রিন্ট করে।

আউটপুট স্ক্রিনে আসবে:

Received Data Type: <class 'dict'>


৭. ফাংশনের ভেতর লাইন ৩ চালানো:
কোড: print("Content:", kwargs)

কীভাবে কাজ করল:

পাইথন kwargs ভেরিয়েবলের মধ্যে থাকা পুরো ডিকশনারিটির কন্টেন্ট পড়ে নেয়।

print() ফাংশন দিয়ে ডিকশনারিটি কনসোলে প্রিন্ট করে।

আউটপুট স্ক্রিনে আসবে:

Content: {'username': 'Abdullah', 'age': 30, 'role': 'Backend Developer'}


৮. ফাংশন সমাপ্তি:
ফাংশনে আর কোনো লাইন নেই এবং কোনো return স্টেটমেন্ট দেওয়া নেই।

তাই ফাংশনটির কাজ শেষ হয় এবং প্রোগ্রামটি সম্পূর্ণ সফলভাবে বন্ধ হয়।

চূড়ান্ত কনসোল আউটপুট:
Plaintext
Received Data Type: <class 'dict'>
Content: {'username': 'Abdullah', 'age': 30, 'role': 'Backend Developer'}




২. লুপ চালিয়ে কি (Key) এবং ভ্যালু (Value) আলাদা করা

ডিকশনারির ওপর .items() মেথড চালিয়ে **kwargs-এর ভেতরের ডেটাগুলো সুন্দরভাবে প্রসেস করা যায়।

def describe_car(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()} -> {value}")

# টেস্ট করা যাক:
describe_car(brand="Toyota", model="Corolla", year=2022, color="Black")

১. লাইন ১: def describe_car(**kwargs):
কী ঘটল: পাইথন ইন্টারপ্রেটার describe_car নামের একটি ফাংশন মেমরিতে ডিফাইন (সংরক্ষণ) করে রাখে।

কীভাবে কাজ করল: **kwargs দিয়ে পাইথন বুঝে নেয় যে এই ফাংশনে যেকোনো সংখ্যক Keyword Arguments (Key=Value স্টাইলে) 
পাঠানো যাবে এবং সেগুলোকে একটি Dictionary বা ডিকশনারি হিসেবে গ্রহণ করা হবে।

অবস্থা: ফাংশনের ভেতরের কোড এখনো রান হবে না।

২. লাইন ২: for key, value in kwargs.items():
কী ঘটল: এটি ফাংশনের বডির লুপ অংশ। ফাংশন কল না হওয়া পর্যন্ত এটি নিষ্ক্রিয় থাকবে।

৩. লাইন ৩: print(f"{key.capitalize()} -> {value}")
কী ঘটল: এটি লুপের ভেতরের প্রিন্ট স্টেটমেন্ট। এটিও ফাংশন কলের সময় কাজ করবে।

৪. লাইন ৫: # টেস্ট করা যাক:
কী ঘটল: পাইথন এটি কমেন্ট হিসেবে দেখে সম্পূর্ণ এড়িয়ে (Skip) পরবর্তী লাইনে চলে যায়।

৫. লাইন ৬: describe_car(brand="Toyota", model="Corolla", year=2022, color="Black")
কী ঘটল: এটি হলো ফাংশন কল (Function Call)।

কীভাবে কাজ করল:

আমরা ফাংশনটিকে ৪টি Keyword Argument দিয়ে কল করেছি:

brand="Toyota"

model="Corolla"

year=2022

color="Black"

**kwargs এই ৪টি আর্গুমেন্টকে সংগ্রহ করে নিচের মতো একটি ডিকশনারিতে রূপান্তর করে মেমরিতে রাখে:

Python
kwargs = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022,
    "color": "Black"
}
এবার কোডের কন্ট্রোল (Control) সরাসরি ফাংশনের ভেতরে লাইন ২-এ চলে যায়।

৬. লুপ রান হওয়া (লাইন ২ এবং লাইন ৩):
kwargs.items() মূলত ডিকশনারির প্রতিটি Key এবং Value-কে জোড়ায় জোড়ায় আলাদা করে দেয়। লুপটি মোট ৪ বার ঘুরবে:

ইটারেশন ১ (প্রথম চক্কর):
Key: "brand", Value: "Toyota"

লাইন ৩ প্রসেসিং: key.capitalize() প্রয়োগ করার ফলে "brand" হয়ে যায় "Brand"।

প্রিন্ট হবে:

Brand -> Toyota
ইটারেশন ২ (দ্বিতীয় চক্কর):
Key: "model", Value: "Corolla"

লাইন ৩ প্রসেসিং: key.capitalize() প্রয়োগ করার ফলে "model" হয়ে যায় "Model"।

প্রিন্ট হবে:


Model -> Corolla
ইটারেশন ৩ (তৃতীয় চক্কর):
Key: "year", Value: 2022

লাইন ৩ প্রসেসিং: key.capitalize() প্রয়োগ করার ফলে "year" হয়ে যায় "Year"।

প্রিন্ট হবে:


Year -> 2022
ইটারেশন ৪ (চতুর্থ চক্কর):
Key: "color", Value: "Black"

লাইন ৩ প্রসেসিং: key.capitalize() প্রয়োগ করার ফলে "color" হয়ে যায় "Color"।

প্রিন্ট হবে:


Color -> Black
৭. প্রোগ্রাম সমাপ্তি:
ডিকশনারির সব তথ্য বের করা শেষ হলে লুপটি থেমে যায় এবং ফাংশন থেকে বের হয়ে প্রোগ্রামটি সফলভাবে সমাপ্ত হয়।

চূড়ান্ত কনসোল আউটপুট:
Plaintext
Brand -> Toyota
Model -> Corolla
Year -> 2022
Color -> Black




৩. ডিফল্ট সেটিংস ওভাররাইড করা (Config Overrider)
প্রোগ্রামিংয়ে ডিফল্ট কনফিগারেশন আপডেট করার জন্য **kwargs ব্যাপকভাবে ব্যবহৃত হয়।

def setup_server(**kwargs):
    # ডিফল্ট সার্ভার সেটিংস
    config = {"host": "localhost", "port": 8000, "debug": True}
    
    # kwargs দিয়ে সেটিংস আপডেট বা ওভাররাইড করা
    config.update(kwargs)
    print("Final Server Config:", config)

# টেস্ট করা যাক (পোর্ট ও ডিবাগ বদলে দেওয়া হলো):
setup_server(port=5000, debug=False)


১. ফাংশন ডিফাইন করা (def setup_server(**kwargs):)
পাইথন setup_server নামের একটি ফাংশন তৈরি করে।

**kwargs এর মাধ্যমে ফাংশনে যেকোনো সংখ্যক কি-ওয়ার্ড আর্গুমেন্ট (Key=Value) পাঠানো যায়, যা ভেতরে গিয়ে একটি ডিকশনারি (Dictionary) হয়ে যায়।

২. ডিফল্ট কনফিগারেশন সেট করা (config = {...})

ফাংশনের ভেতরে প্রথমে একটি config নামের ডিকশনারি তৈরি করা হয়, যেখানে সার্ভারের ডিফল্ট মানগুলো সেট করা আছে:

Python
{"host": "localhost", "port": 8000, "debug": True}

৩. ফাংশন কল ও kwargs-এর রূপান্তর (setup_server(port=5000, debug=False))

আমরা যখন ফাংশনটি কল করলাম, তখন আমরা দুটি মান পাস করেছি: port=5000 এবং debug=False।

**kwargs এই মানগুলোকে নিয়ে একটি ডিকশনারি বানিয়ে ফেলবে:


kwargs = {"port": 5000, "debug": False}

৪. আপডেট করা (config.update(kwargs))

.update() মেথডটি config ডিকশনারির ভেতরের মানগুলোকে kwargs-এর মান দিয়ে আপডেট বা ওভাররাইড করে দেয়:

ডিকশনারিতে আগে port: 8000 ছিল, kwargs-এ নতুন port: 5000 থাকায় সেটি ওভাররাইড হয়ে ৫০০০ হয়ে যায়।

আগে debug: True ছিল, নতুন debug: False থাকায় সেটি পরিবর্তিত হয়ে False হয়ে যায়।

host নিয়ে কোনো কথা বলা হয়নি (পাঠানো হয়নি), তাই ডিফল্ট "localhost" অপরিবর্তিত থাকে।

৫. প্রিন্ট করা (print(...))

পরিশেষে, আপডেট হওয়া চূড়ান্ত config ডিকশনারিটি প্রিন্ট করে দেখায়।

চূড়ান্ত আউটপুট (Final Output):

কোডটি রান করলে কনসোলে নিচের আউটপুটটি দেখা যাবে:



Final Server Config: {'host': 'localhost', 'port': 5000, 'debug': False}


কেন এই পদ্ধতিটি দারুণ?

এই উপায়ে কোড লিখলে সুবিধা হলো—ইউজার যদি কোনো মান না দেয়, তবে ডিফল্ট মান কাজ করবে (host: localhost), 
আর ইউজার যদি নতুন কোনো মান পাস করে (port=5000), তবে সেটি স্বয়ংক্রিয়ভাবে ডিফল্ট মানকে ওভাররাইড করে নেবে। 
রিয়েল-ওয়ার্ল্ড প্রজেক্টে কনফিগারেশন সেট করার জন্য এই টেকনিকটি খুব বেশি ব্যবহার করা হয়।





৪. .get() মেথড ব্যবহার করে সেফলি কি খোঁজা
ডিকশনারিতে নির্দিষ্ট কোনো কি আছে কি না বা না থাকলে ডিফল্ট মান কী হবে তা .get() দিয়ে চেক করা যায়।

def check_permissions(**kwargs):
    # যদি 'admin' কি না থাকে, তবে ডিফল্টভাবে False ধরবে
    is_admin = kwargs.get("admin", False)
    
    if is_admin:
        print("Access Granted: Welcome Admin!")
    else:
        print("Access Denied: Regular user privileges.")

# টেস্ট করা যাক:
check_permissions(role="guest")
check_permissions(admin=True, role="superuser")

১. is_admin = kwargs.get("admin", False)
এখানে ডিকশনারির .get() মেথড ব্যবহার করা হয়েছে।

.get("admin", False) এর অর্থ হলো:

kwargs ডিকশনারির ভেতরে খুঁজে দেখো "admin" নামের কোনো Key আছে কি না।

যদি থাকে, তবে তার ভেতরের মানটি (True বা False) is_admin এ বসিয়ে দাও।

আর যদি "admin" কি-টি না থাকে, তবে ক্র্যাশ বা এরর (KeyError) না দেখিয়ে স্বয়ংক্রিয়ভাবে ডিফল্ট মান হিসেবে False রিটার্ন করে দাও।

২. if-else শর্ত:
যদি is_admin এর মান True হয়, তবে প্রিন্ট করবে: "Access Granted: Welcome Admin!"

যদি is_admin এর মান False হয়, তবে প্রিন্ট করবে: "Access Denied: Regular user privileges."

টেস্ট কেসগুলোর ড্রাই রান (Dry Run):
টেস্ট কেস ১: check_permissions(role="guest")
এখানে পাস করা হয়েছে: {"role": "guest"}।

kwargs.get("admin", False) লাইনে খোঁজা হলো "admin" আছে কি না। দেখা গেল এখানে শুধু role আছে, admin নেই।

যেহেতু admin নেই, .get() মেথড ডিফল্টভাবে False রিটার্ন করল। সুতরাং is_admin = False হলো।

if is_admin: শর্তটি মিথ্যা (False) হওয়ায় else ব্লকের কোড রান করবে।

আউটপুট আসবে: Access Denied: Regular user privileges.

টেস্ট কেস ২: check_permissions(admin=True, role="superuser")
এখানে পাস করা হয়েছে: {"admin": True, "role": "superuser"}।

kwargs.get("admin", False) লাইনে খোঁজা হলো "admin" আছে কি না। দেখা গেল এখানে স্পষ্টভাবে admin=True দেওয়া আছে।

ফলে is_admin এর মান সেট হলো True।

if is_admin: শর্তটি সত্য (True) হওয়ায় if ব্লকের কোড রান করবে।

আউটপুট আসবে: Access Granted: Welcome Admin!

চূড়ান্ত কনসোল আউটপুট:

কোডটি রান করলে টার্মিনালে ঠিক এই আউটপুটগুলো দেখা যাবে:


Access Denied: Regular user privileges.
Access Granted: Welcome Admin!




৫. *args এবং **kwargs একসাথে ব্যবহার করা
একই ফাংশনে পজিশনাল আর্গুমেন্ট (*args) এবং কি-ওয়ার্ড আর্গুমেন্ট (**kwargs) একসাথে ব্যবহার করা যায়।
(মনে রাখতে হবে: লেখার সময় সবসময় আগে *args এবং পরে **kwargs লিখতে হয়)।

def process_order(*items, **details):
    print("Ordered Items (Tuple):", items)
    print("Order Details (Dict):", details)

# টেস্ট করা যাক:
process_order("Laptop", "Mouse", "Keyboard", customer="Abdullah", location="Rangpur", payment="Paid")

১. *items (Arbitrary Positional Arguments): ফাংশনে যতগুলো সাধারণ বা পজিশনাল মান (যেমন: "Laptop", "Mouse", "Keyboard") পাঠানো হবে,
পাইথন সেগুলোকে স্বয়ংক্রিয়ভাবে একটি Tuple (টুপল)-এর মধ্যে প্যাক করে নেয়।
২. **details (Arbitrary Keyword Arguments): ফাংশনে যতগুলো কি-ওয়ার্ড আর্গুমেন্ট
(যেমন: customer="Abdullah", location="Rangpur") পাঠানো হবে, পাইথন সেগুলোকে একটি Dictionary (ডিকশনারি)-এর মধ্যে প্যাক করে নেয়।

নোট: পাইথন ফাংশনে সবসময় প্রথমে *args লিখতে হয় এবং তার পরে **kwargs লিখতে হয়। উল্টোটি করলে সিনট্যাক্স এরর (SyntaxError) আসবে।

স্টেপ-বাই-স্টেপ ড্রাই রান (Dry Run):
১. ফাংশন কল ও ডেটা রিসিভিং:
আমরা ফাংশনটি কল করেছি এভাবে:


process_order("Laptop", "Mouse", "Keyboard", customer="Abdullah", location="Rangpur", payment="Paid")
এখানে দুই ধরণের ডেটা পাঠানো হয়েছে:

পজিশনাল ডেটা: "Laptop", "Mouse", "Keyboard" — এগুলো সরাসরি চলে যায় *items-এর কাছে।

কি-ওয়ার্ড ডেটা: customer="Abdullah", location="Rangpur", payment="Paid" — এগুলো চলে যায় **details-এর কাছে।

২. মেমোরিতে ভেরিয়েবলগুলোর রূপ:
items ভেরিয়েবলটি হয়ে যায় একটি টুপল:


items = ('Laptop', 'Mouse', 'Keyboard')
details ভেরিয়েবলটি হয়ে যায় একটি ডিকশনারি:


details = {
    'customer': 'Abdullah',
    'location': 'Rangpur',
    'payment': 'Paid'
}
৩. প্রিন্ট স্টেটমেন্ট এক্সিকিউশন:

প্রথম প্রিন্ট: print("Ordered Items (Tuple):", items)

এটি প্রিন্ট করবে: Ordered Items (Tuple): ('Laptop', 'Mouse', 'Keyboard')

দ্বিতীয় প্রিন্ট: print("Order Details (Dict):", details)

এটি প্রিন্ট করবে: Order Details (Dict): {'customer': 'Abdullah', 'location': 'Rangpur', 'payment': 'Paid'}

চূড়ান্ত কনসোল আউটপুট:

কোডটি রান করলে টার্মিনালে ঠিক এই আউটপুটটি দেখা যাবে:


Ordered Items (Tuple): ('Laptop', 'Mouse', 'Keyboard')
Order Details (Dict): {'customer': 'Abdullah', 'location': 'Rangpur', 'payment': '







def show(**kwargs):
    print(kwargs)
    print(type(kwargs))

show(name="Abdullah", age=30)


১. ফাংশন কল করা (show(name="Abdullah", age=30)):

বাইরে থেকে দুটি কি-ওয়ার্ড আর্গুমেন্ট পাঠানো হয়েছে: name="Abdullah" এবং age=30।

ফাংশনের প্যারামিটারে থাকা দুটি স্টার (**kwargs) এই মানগুলোকে রিসিভ করে একটি ডিকশনারিতে রূপান্তর করে।

State (kwargs):

{'name': 'Abdullah', 'age': 30}

২. প্রথম প্রিন্ট (print(kwargs)):

পাইথন ডিকশনারিটিকে সরাসরি কনসোলে প্রিন্ট করে।

আউটপুট:

{'name': 'Abdullah', 'age': 30}

৩. দ্বিতীয় প্রিন্ট (print(type(kwargs))):

type() ফাংশন দিয়ে চেক করা হয় kwargs আসলে পাইথনের কোন ডাটা টাইপের।

যেহেতু এটি একটি ডিকশনারি, তাই পাইথন এর ক্লাস টাইপ প্রিন্ট করে।

আউটপুট:

<class 'dict'>

এই ছোট কোডটির মাধ্যমে মূলত **kwargs-এর মূল ভিত্তিটি (dictionary হিসেবে ডেটা রিসিভ করা)





def student_info(**kwargs):
    print("Total Info:", len(kwargs))
    print("Name exists:", "name" in kwargs)
    print("Name:", kwargs.get("name", "Not found"))
    print("Phone:", kwargs.get("phone", "Not found"))

student_info(name="Abdullah", city="Rangpur")


১. ফাংশন কল (student_info(name="Abdullah", city="Rangpur")):

ফাংশনে দুটি কি-ওয়ার্ড আর্গুমেন্ট পাঠানো হয়েছে।

**kwargs এগুলোকে প্যাক করে একটি ডিকশনারি তৈরি করে।

State (kwargs):

{'name': 'Abdullah', 'city': 'Rangpur'}

২. প্রথম লাইন (print("Total Info:", len(kwargs))):

len(kwargs) ডিকশনারির ভেতরের মোট আইটেমের সংখ্যা গণনা করে (এখানে আইটেম দুটি: name এবং city)। সংখ্যাটি হলো 2।

কনসোল আউটপুট:

Total Info: 2

৩. দ্বিতীয় লাইন (print("Name exists:", "name" in kwargs)):

"name" in kwargs চেক করে ডিকশনারির কি (Keys)-গুলোর মধ্যে "name" নামের কোনো কি আছে কি না। যেহেতু ডিকশনারিতে name রয়েছে, তাই এটি True রিটার্ন করে।

কনসোল আউটপুট:

Name exists: True

৪. তৃতীয় লাইন (print("Name:", kwargs.get("name", "Not found"))):

kwargs.get("name", "Not found") চেষ্টা করে ডিকশনারি থেকে "name" কি-এর মান খুঁজে বের করতে।

যেহেতু "name" কি-টি আছে এবং এর মান "Abdullah", তাই এটি "Abdullah" রিটার্ন করে (ডিফল্ট "Not found" ব্যবহার করার প্রয়োজন পড়ে না)।

কনসোল আউটপুট:

Name: Abdullah

৫. চতুর্থ লাইন (print("Phone:", kwargs.get("phone", "Not found"))):

kwargs.get("phone", "Not found") চেক করে ডিকশনারিতে "phone" নামের কোনো কি আছে কি না।

খেয়াল করুন, আমরা ফাংশন কল করার সময় কোনো phone পাঠাইনি। তাই ডিকশনারিতে "phone" কি-টি পাওয়া যায় না।

যখন .get() মেথড কোনো কি খুঁজে পায় না, তখন এটি দ্বিতীয় প্যারামিটারে দেওয়া ডিফল্ট মান ("Not found") রিটার্ন করে।

কনসোল আউটপুট:

Phone: Not found





def print_all(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_all(subject="Python", score=95, passed=True)



১. ফাংশন কল (print_all(subject="Python", score=95, passed=True)):

বাইরে থেকে তিনটি কি-ওয়ার্ড আর্গুমেন্ট পাঠানো হয়েছে।

**kwargs এই মানগুলোকে প্যাক করে একটি ডিকশনারি তৈরি করে।

State (kwargs):

{'subject': 'Python', 'score': 95, 'passed': True}

২. লুপ শুরু (for key, value in kwargs.items():):

.items() মেথড ডিকশনারির প্রতিটি কি (Key) এবং ভ্যালু (Value) জোড়াকে একে একে এক্সট্রাক্ট করে লুপে পাঠায়।

প্রথম ইটারেশন (First Iteration):

key = 'subject', value = 'Python'

প্রিন্ট স্টেটমেন্ট রান হয়: print(f"subject = Python")

কনসোল আউটপুট:

subject = Python

দ্বিতীয় ইটারেশন (Second Iteration):

key = 'score', value = 95

প্রিন্ট স্টেটমেন্ট রান হয়: print(f"score = 95")

কনসোল আউটপুট:

score = 95

তৃতীয় ইটারেশন (Third Iteration):

key = 'passed', value = True

প্রিন্ট স্টেটমেন্ট রান হয়: print(f"passed = True")

কনসোল আউটপুট:

passed = True

৩. লুপ সমাপ্তি:

ডিকশনারিতে আর কোনো আইটেম না থাকায় লুপটি সফলভাবে শেষ হয় এবং ফাংশনটির কাজ শেষ হয়।




কোনো argument না দিলে কী হয়

def empty_test(**kwargs):
    print(kwargs)

empty_test()

১. ফাংশন কল (empty_test()):

এখানে ফাংশনটি কল করার সময় ভেতর বা বাইরে থেকে কোনো কি-ওয়ার্ড আর্গুমেন্ট (Key-Value) পাঠানো হয়নি।

ফলে **kwargs কোনো ডেটা পাওয়ার সুযোগ পায়নি।

State (kwargs):

পাইথন এটিকে একটি খালি ডিকশনারি (Empty Dictionary) হিসেবে তৈরি করে।

kwargs = {}

২. প্রিন্ট স্টেটমেন্ট (print(kwargs)):

print ফাংশনটি খালি ডিকশনারিটিকে কনসোলে প্রিন্ট করে।

কনসোল আউটপুট:

{}




def greet(name, **kwargs):
    print(f"Hello, {name}!")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

greet("Abdullah", city="Rangpur", job="DSA")


১. ফাংশন কল (greet("Abdullah", city="Rangpur", job="DSA")):

এখানে প্রথম মানটি পজিশনাল আর্গুমেন্ট হিসেবে যায় এবং পরের নামযুক্ত মানগুলো কি-ওয়ার্ড আর্গুমেন্ট হিসেবে যায়।

Parameter Mapping:

name = "Abdullah" (পজিশনাল আর্গুমেন্ট হিসেবে সরাসরি name ভেরিয়েবলে বসে যায়)।

বাকী অতিরিক্ত মানগুলো প্যাক হয়ে **kwargs ডিকশনারি তৈরি করে।

State (kwargs):

{'city': 'Rangpur', 'job': 'DSA'}

২. প্রথম প্রিন্ট (print(f"Hello, {name}!")):

name-এর মান "Abdullah" ব্যবহার করে স্ট্রিং ফরম্যাটিং করা হয়।

কনসোল আউটপুট:

Hello, Abdullah!

৩. লুপ শুরু (for key, value in kwargs.items():):

kwargs ডিকশনারির ওপর লুপ চালিয়ে প্রতিটি কি (Key) এবং ভ্যালু (Value) আলাদা করা হয়।

প্রথম ইটারেশন (First Iteration):

key = 'city', value = 'Rangpur'

প্রিন্ট স্টেটমেন্ট রান হয়: print(f"  city: Rangpur")

কনসোল আউটপুট:

  city: Rangpur

দ্বিতীয় ইটারেশন (Second Iteration):

key = 'job', value = 'DSA'

প্রিন্ট স্টেটমেন্ট রান হয়: print(f"  job: DSA")

কনসোল আউটপুট:

  job: DSA

৪. লুপ সমাপ্তি:

ডিকশনারিতে আর কোনো উপাদান না থাকায় লুপটি শেষ হয় এবং ফাংশনের এক্সিকিউশন সমাপ্ত হয়।



def demo(a, **kwargs):
    print(a, kwargs)

demo(1, x=10, y=20)


১. ফাংশন কল (demo(1, x=10, y=20)):

এখানে আর্গুমেন্টগুলো নিয়ম অনুযায়ী দুই ভাগে ভাগ হয়ে বসে:

প্রথম মানটি (1) পজিশনাল আর্গুমেন্ট হিসেবে সরাসরি প্রথম প্যারামিটারে চলে যায়। তাই a = 1।

এর পরের অতিরিক্ত নামযুক্ত মানগুলো (x=10, y=20) প্যাক হয়ে **kwargs ডিকশনারি তৈরি করে।

State (kwargs):

{'x': 10, 'y': 20}

২. প্রিন্ট স্টেটমেন্ট (print(a, kwargs)):

পাইথন a-এর মান এবং kwargs ডিকশনারিটিকে একসাথে প্রিন্ট করে।

কনসোল আউটপুট:

1 {'x': 10, 'y': 20}




**kwargs দিয়ে Default মান সেট করা

def create_user(username, **options):
    settings = {
        "role": "user",
        "active": True,
        "language": "bn",
    }
    settings.update(options)  
    return {"username": username, **settings}

print(create_user("Abdullah"))
print(create_user("Aziz", role="admin", language="en"))


১. ফাংশন কল ও আর্গুমেন্ট ম্যাপিং:

username = "Abdullah" (পজিশনাল আর্গুমেন্ট হিসেবে বসে)।

বাইরে থেকে আর কোনো অতিরিক্ত কি-ওয়ার্ড আর্গুমেন্ট পাঠানো হয়নি, তাই **options খালি ডিকশনারি হয় (options = {})।

২. প্রাথমিক settings ডিকশনারি তৈরি:

State (settings):

{"role": "user", "active": True, "language": "bn"}

৩. আপডেট বা মার্জ করা (settings.update(options)):

যেহেতু options খালি ({}), তাই settings-এ নতুন কোনো পরিবর্তন হয় না। আগের ডিফল্ট মানগুলোই বহাল থাকে।

৪. রিটার্ন ও ডিকশনারি আনপ্যাকিং (return {"username": username, **settings}):

এখানে ডিকশনারি আনপ্যাকিং (**settings) ব্যবহার করে সবকিছু একটি নতুন ডিকশনারিতে জোড়া লাগানো হয়:

"username": "Abdullah"

**settings আনপ্যাক হয়ে যোগ হয়: "role": "user", "active": True, "language": "bn"

ফাইনাল রিটার্নড ডিকশনারি:

{'username': 'Abdullah', 'role': 'user', 'active': True, 'language': 'bn'}

৫. কনসোল আউটপুট:

{'username': 'Abdullah', 'role': 'user', 'active': True, 'language': 'bn'}

টেস্ট কেস ২: print(create_user("Aziz", role="admin", language="en"))
১. ফাংশন কল ও আর্গুমেন্ট ম্যাপিং:

username = "Aziz"

অতিরিক্ত নামযুক্ত মানগুলো প্যাক হয়ে options ডিকশনারি তৈরি করে:

options = {'role': 'admin', 'language': 'en'}

২. প্রাথমিক settings ডিকশনারি তৈরি:

State (settings):

{"role": "user", "active": True, "language": "bn"}

৩. আপডেট বা মার্জ করা (settings.update(options)):

.update() মেথড options-এর নতুন মানগুলো দিয়ে settings-এর পুরোনো মানগুলো ওভাররাইড (আপডেট) করে:

role: "user" বদলে হয়ে যায় "admin"

language: "bn" বদলে হয়ে যায় "en"

active: যেহেতু options-এ এটি ছিল না, তাই ডিফল্ট True অপরিবর্তিত থাকে।

Updated State (settings):

{"role": "admin", "active": True, "language": "en"}

৪. রিটার্ন ও ডিকশনারি আনপ্যাকিং (return {"username": username, **settings}):

মানগুলো একত্র করা হয়:

"username": "Aziz"

**settings আনপ্যাক হয়ে যোগ হয়: "role": "admin", "active": True, "language": "en"

ফাইনাল রিটার্নড ডিকশনারি:

{'username': 'Aziz', 'role': 'admin', 'active': True, 'language': 'en'}

৫. কনসোল আউটপুট:

{'username': 'Aziz', 'role': 'admin', 'active': True, 'language': 'en'}




Keyword argument যাচাই (Validation)


ALLOWED_FIELDS = {"name", "email", "age"}

def update_profile(user_id, **fields):
    invalid = set(fields) - ALLOWED_FIELDS
    if invalid:
        raise ValueError(f"Unauthorized fields: {invalid}")
    print(f"Updating user {user_id}:", fields)

update_profile(1, name="Abdullah", age=30)

try:
    update_profile(1, password="123")
except ValueError as e:
    print("Error:", e)




১. কনস্ট্যান্ট ডিফাইন করা (ALLOWED_FIELDS = {"name", "email", "age"}):

মেমোরিতে একটি সেট (Set) তৈরি করা হয়, যেখানে অনুমোদিত ফিল্ডগুলোর নাম সংরক্ষিত থাকে।

State: ALLOWED_FIELDS সেটে আছে {'name', 'email', 'age'}।

টেস্ট কেস ১: update_profile(1, name="Abdullah", age=30)
Line 4 (user_id = 1, এবং **fields প্যাকিং):

user_id এর মান বসে 1

অতিরিক্ত কি-ওয়ার্ড আর্গুমেন্টগুলো প্যাক হয়ে fields ডিকশনারি তৈরি করে।

State: fields ডিকশনারিতে আছে {'name': 'Abdullah', 'age': 30}।

Line 5 (invalid = set(fields) - ALLOWED_FIELDS):

set(fields) মানে ডিকশনারির কি (Keys) দিয়ে একটি নতুন সেট তৈরি করা: {'name', 'age'}।

সেট বিয়োগের কাজ: {'name', 'age'} থেকে {'name', 'email', 'age'} বাদ দেওয়া হচ্ছে।

যেহেতু পাস করা ফিল্ডগুলো অনুমোদিত সেটের ভেতরেই আছে, তাই অতিরিক্ত বা অননুমোদিত কোনো ফিল্ড বাকি থাকে না।

State: invalid হলো একটি খালি সেট set()।

Line 6-7 (if invalid:):

কন্ডিশন চেক: খালি সেটের বুলিয়ান ভ্যালু হলো False।

ফলে if ব্লকের ভেতরে থাকা ValueError রান করে না।

Line 9 (print(f"Updating user {user_id}:", fields)):

সাকসেসফুল মেসেজ প্রিন্ট হয়।

কনসোল আউটপুট:

Updating user 1: {'name': 'Abdullah', 'age': 30}

টেস্ট কেস ২: update_profile(1, password="123")
Line 4 (user_id = 1, এবং **fields প্যাকিং):

user_id এর মান বসে 1

State: fields ডিকশনারিতে আছে {'password': '123'}।

Line 5 (invalid = set(fields) - ALLOWED_FIELDS):

সেট অপারেশন: {'password'} থেকে {'name', 'email', 'age'} বাদ দেওয়া হচ্ছে।

যেহেতু "password" ফিল্ডটি অনুমোদিত সেটের মধ্যে নেই, তাই এটি বাদ যায় না।

State: invalid সেটে থেকে যায় {'password'}।

Line 6-7 (if invalid:):

কন্ডিশন চেক: উপাদানের উপস্থিতি থাকার কারণে বুলিয়ান ভ্যালু হলো True।

raise ValueError রান করে এবং একটি এক্সেপশন বা ত্রুটি ছুঁড়ে মারে।

Line 11-13 (except ValueError as e:):

try ব্লকে ত্রুটি ধরা পড়ার কারণে কোডটি ক্র্যাশ না করে except ব্লকে চলে আসে।

ত্রুটির মেসেজটি e ভেরিয়েবলে জমা হয় এবং প্রিন্ট হয়।

কনসোল আউটপুট:

Error: Unauthorized fields: {'password'}




Dictionary unpacking দিয়ে Configuration

def send_email(to, subject, body="", cc=None, priority="normal"):
    print(f"To: {to}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    print(f"CC: {cc}, Priority: {priority}")

email_data = {
    "to": "karim@example.com",
    "subject": "Meeting",
    "body": "Tomorrow at 10 AM",
    "priority": "high",
}

send_email(**email_data)


১. ফাংশন ডিফাইন করা (def send_email(...)):

পাইথনের মেমোরিতে send_email ফাংশনটি লোড হয়।

এই ফাংশনে কিছু ডিফল্ট প্যারামিটার রয়েছে: body="", cc=None, এবং priority="normal"।

২. ডিকশনারি ডিফাইন করা (email_data):

মেমোরিতে email_data নামের একটি ডিকশনারি তৈরি হয় যেখানে ইমেইলের তথ্যগুলো রাখা আছে।

State (email_data):

{'to': 'karim@example.com', 'subject': 'Meeting', 'body': 'Tomorrow at 10 AM', 'priority': 'high'}

৩. ফাংশন কল ও ডিকশনারি আনপ্যাকিং (send_email(**email_data)):

এখানে ডাবল স্টার (**) দিয়ে email_data ডিকশনারিটিকে আনপ্যাক (Unpack) করে ফাংশনে পাঠানো হচ্ছে।

পাইথন ডিকশনারির কি (Keys) গুলোর সাথে ফাংশনের প্যারামিটারগুলোর নাম মিলিয়ে মানগুলো বসিয়ে দেয়:

to = "karim@example.com"

subject = "Meeting"

body = "Tomorrow at 10 AM"

priority = "high"

নোট: ডিকশনারিতে cc না থাকায় এটি তার ডিফল্ট মান None গ্রহণ করে।

৪. ফাংশনের ভেতরের প্রিন্ট স্টেটমেন্টগুলোর এক্সিকিউশন:

প্রথম লাইন (print(f"To: {to}")):

to প্যারামিটারের মান প্রিন্ট হয়।

কনসোল আউটপুট:

To: karim@example.com

দ্বিতীয় লাইন (print(f"Subject: {subject}")):

subject প্যারামিটারের মান প্রিন্ট হয়।

কনসোল আউটপুট:

Subject: Meeting

তৃতীয় লাইন (print(f"Body: {body}")):

body প্যারামিটারের মান প্রিন্ট হয়।

কনসোল আউটপুট:

Body: Tomorrow at 10 AM

চতুর্থ লাইন (print(f"CC: {cc}, Priority: {priority}")):

cc-এর ডিফল্ট মান None এবং priority-এর আপডেট করা মান high প্রিন্ট হয়।

কনসোল আউটপুট:

CC: None, Priority: high






ব্যাকএন্ড রিকোয়েস্ট লগার মিডলওয়্যার (Request Logger Middleware Simulator)
একটি API-এ বিভিন্ন রিকোয়েস্ট আসার সময় ডাইনামিক মেটাডেটা বা লগ রেকর্ড করার জন্য এমন প্যাটার্ন ব্যবহার করা হয়।

def log_api_request(endpoint, **metadata):
    print(f"\n[LOG] Endpoint Hit: {endpoint}")
    print("--- Request Metadata ---")
    
    # যদি মেটাডেটা খালি থাকে
    if not metadata:
        print("No extra metadata provided.")
        return
        
    for key, value in metadata.items():
        print(f"  {key.upper()} : {value}")

# টেস্ট করা যাক:
log_api_request("/api/v1/users", method="POST", ip="192.168.1.50", status_code=201, auth_required=True)
log_api_request("/api/v1/health-check") # কোনো kwargs ছাড়া




def log_api_request(endpoint, **metadata):

এখানে প্রথম প্যারামিটারটি (endpoint) একটি সাধারণ বাধ্যতামূলক আর্গুমেন্ট, যা দিয়ে এপিআই-এর পাথ বা ইউআরএল গ্রহণ করা হয়।

দ্বিতীয় প্যারামিটারটি (**metadata) হলো **kwargs, যার মাধ্যমে অতিরিক্ত যেকোনো তথ্য (যেমন মেথড, আইপি, স্ট্যাটাস কোড ইত্যাদি) ডিকশনারি আকারে পাঠানো যায়।

if not metadata:

পাইথনে কোনো ডিকশনারি খালি থাকলে ({}) তা False হিসেবে গণ্য হয়।

not metadata মানে হলো—যদি কোনো অতিরিক্ত মেটাডেটা বা কি-ওয়ার্ড আর্গুমেন্ট না পাঠানো হয়, তবে এই শর্তটি সত্য (True) হবে।

শর্ত সত্য হলে print("No extra metadata provided.") প্রিন্ট করে return এর মাধ্যমে ফাংশনের কাজ সেখানেই শেষ করে দেওয়া হয়, যাতে নিচের লুপে আর কোনো এরর না আসে।

for key, value in metadata.items():

যদি মেটাডেটা থাকে, তবে লুপটি ডিকশনারির প্রতিটি Key এবং Value আলাদা করে।

key.upper() ব্যবহার করার ফলে কি-গুলোর সব অক্ষর বড় হাতের (Uppercase) হয়ে প্রিন্ট হয় (যেমন: method হয়ে যাবে METHOD)।

টেস্ট কেসগুলোর ড্রাই রান (Dry Run):
টেস্ট কেস ১: log_api_request("/api/v1/users", method="POST", ip="192.168.1.50", status_code=201, auth_required=True)
endpoint = "/api/v1/users"

metadata ডিকশনারিটি তৈরি হলো:

Python
{
    "method": "POST",
    "ip": "192.168.1.50",
    "status_code": 201,
    "auth_required": True
}
if not metadata: শর্তটি মিথ্যা (False) হবে, কারণ মেটাডেটা খালি নয়।

লুপ ঘুরে প্রতিটি ডেটা বড় হাতের অক্ষরে প্রিন্ট হবে:

METHOD : POST

IP : 192.168.1.50

STATUS_CODE : 201

AUTH_REQUIRED : True

টেস্ট কেস ২: log_api_request("/api/v1/health-check")

endpoint = "/api/v1/health-check"

এখানে কোনো অতিরিক্ত কি-ওয়ার্ড আর্গুমেন্ট দেওয়া হয়নি। ফলে metadata হলো একটি খালি ডিকশনারি {}।

if not metadata: শর্তটি সত্য (True) হবে।

ফলে কোডটি প্রিন্ট করবে: No extra metadata provided. এবং return করে ফাংশন থেকে বের হয়ে যাবে।

চূড়ান্ত কনসোল আউটপুট:
কোডটি রান করলে টার্মিনালে ঠিক নিচের মতো আউটপুট দেখতে পাবেন:


[LOG] Endpoint Hit: /api/v1/users
--- Request Metadata ---
  METHOD : POST
  IP : 192.168.1.50
  STATUS_CODE : 201
  AUTH_REQUIRED : True

[LOG] Endpoint Hit: /api/v1/health-check
--- Request Metadata ---
No extra metadata provided.





ডাইনামিক ডাটাবেজ কুয়েরি ফিল্টার সিমুলেটর (Dynamic Database Filter)
ব্যাকএন্ডে কোনো ডেটাবেজ থেকে নির্দিষ্ট শর্ত (Condition) অনুযায়ী ডেটা ফিল্টার করার লজিক **kwargs দিয়ে খুব সুন্দরভাবে লেখা যায়।

def query_database(**filters):
    # ধরে নিই এটি আমাদের ডাটাবেজের ইউজার টেবিল
    users_table = [
        {"id": 1, "name": "Abdullah", "role": "admin", "active": True},
        {"id": 2, "name": "Rahim", "role": "user", "active": True},
        {"id": 3, "name": "Karim", "role": "admin", "active": False},
        {"id": 4, "name": "Selim", "role": "user", "active": True}
    ]
    
    matched_results = []
    
    # টেবিলের প্রতিটি রেকর্ডের ওপর লুপ চালানো
    for user in users_table:
        is_match = True
        # পাস করা ফিল্টারগুলোর সাথে ইউজারের ডেটা মেলানো
        for key, value in filters.items():
            if user.get(key) != value:
                is_match = False
                break
        if is_match:
            matched_results.append(user)
            
    return matched_results

# টেস্ট ১: শুধু অ্যাডমিন রোল ফিল্টার করা
print("Admin Users:", query_database(role="admin"))

# টেস্ট ২: যারা অ্যাডমিন এবং একটিভ (active=True) তাদের খোঁজা
print("\nActive Admins:", query_database(role="admin", active=True))



টেস্ট ১: query_database(role="admin") এর ড্রাই রান
যখন ফাংশনটি role="admin" দিয়ে কল করা হয়, তখন **kwargs-এর সুবাদে filters ডিকশনারিটি হয়:

filters = {'role': 'admin'}

১. প্রাথমিক প্রস্তুতি:

users_table-এ মোট ৪ জন ইউজারের রেকর্ড আছে।

matched_results = [] (এটি একটি খালি লিস্ট, যেখানে শর্ত মিলে যাওয়া ইউজারদের রাখা হবে)।

২. বাইরের লুপ (প্রতিটি ইউজারের ওপর চেক করা):

ইউজার ১ (id: 1, name: "Abdullah", role: "admin", active: True):

লুপের শুরুতে ধরে নেওয়া হয় is_match = True (অর্থাৎ ধরে নিলাম এ আমাদের শর্ত পূরণ করে)।

ভেতরের লুপে filters.items() চেক করে: key = 'role', value = 'admin'।

কোড চেক করে: user.get('role') != 'admin' কি না? ইউজারের রোল হলো "admin", যা ফিল্টারের সাথে মিলে যায়। তাই শর্ত মিথ্যা হয় (!= মেলেনি),
ফলে is_match পরিবর্তন হয়ে False হয় না (এটি True ই থাকে)।

ভেতরের লুপ শেষ হওয়ার পর if is_match: সত্য হয়।

তাই matched_results.append(user) এর মাধ্যমে আব্দুল্লাহর পুরো ডিকশনারিটি রেজাল্ট লিস্টে যোগ হয়।

ইউজার ২ (id: 2, name: "Rahim", role: "user", active: True):

is_match = True ধরে নেওয়া হয়।

ফিল্টার চেক করে: ইউজারের রোল "user", কিন্তু আমাদের ফিল্টার হলো "admin"।

কোড চেক করে: user.get('role') != 'admin' → এই শর্তটি সত্য ('user' আর 'admin' এক নয়)।

তাই is_match = False হয়ে যায় এবং break করে ভেতরের লুপ থেকে বের হয়ে আসে।

if is_match: মিথ্যা হওয়ায় রহিম রেজাল্ট লিস্টে জায়গা পায় না।

ইউজার ৩ (id: 3, name: "Karim", role: "admin", active: False):

is_match = True দিয়ে শুরু হয়।

ইউজারের রোল "admin", যা ফিল্টারের সাথে মিলে যায় (is_match ঠিক থাকে)।

ভেতরের লুপ শেষ হলে if is_match: সত্য হয়।

তাই করিমের পুরো ডিকশনারিটি রেজাল্ট লিস্টে যোগ হয়।

ইউজার ৪ (id: 4, name: "Selim", role: "user", active: True):

রহিমের মতো সেলিমের রোলও "user" হওয়ায় এটি ফিল্টারে বাদ পড়ে যায় এবং রেজাল্টে আসে না।

৩. চূড়ান্ত রিটার্ন ও প্রিন্ট:

লুপ শেষে matched_results লিস্টে শুধু আব্দুল্লাহ এবং করিমের ডেটা জমা থাকে।

আউটপুট দেখায়:

Admin Users: [{'id': 1, 'name': 'Abdullah', 'role': 'admin', 'active': True}, {'id': 3, 'name': 'Karim', 'role': 'admin', 'active': False}]

টেস্ট ২: query_database(role="admin", active=True) এর ড্রাই রান
এখানে ফিল্টার পাঠানো হয়েছে দুটি: filters = {'role': 'admin', 'active': True}

১. প্রাথমিক প্রস্তুতি:

matched_results = []

২. বাইরের লুপ (প্রতিটি ইউজারের ওপর চেক করা):

ইউজার ১ (Abdullah):

is_match = True

ভেতরের লুপে প্রথম ফিল্টার চেক: role == "admin" → মিলে গেছে (is_match = True)।

দ্বিতীয় ফিল্টার চেক: active == True (আব্দুল্লাহর active ও True) → মিলে গেছে (is_match = True)।

সব শর্ত মিলRegistered! তাই আব্দুল্লাহ রেজাল্ট লিস্টে যোগ হলো।

ইউজার ২ (Rahim):

প্রথম ফিল্টার (role == "admin") মিলল না ('user' হওয়ায়)। সাথে সাথে is_match = False হয়ে break করে দিল। রেজাল্টে এল না।

ইউজার ৩ (Karim):

is_match = True

প্রথম ফিল্টার চেক: role == "admin" → মিলে গেছে (is_match = True)।

দ্বিতীয় ফিল্টার চেক: active == True কিন্তু করিমের active হলো False (active=False)!

কোড চেক করে: user.get('active') != True → এটি সত্য হয়।

ফলে is_match = False হয়ে যায় এবং break করে লুপ ভেঙে বের হয়ে আসে।

শর্ত পুরোপুরি না মেলায় করিম এই যাত্রায় বাদ পড়ে যায় (কারণ সে অ্যাডমিন হলেও একটিভ নয়)।

ইউজার ৪ (Selim):

প্রথম ফিল্টারেই বাদ পড়ে যায়।

৩. চূড়ান্ত রিটার্ন ও প্রিন্ট:

সব চেক শেষে শুধু সেই ইউজারটি টিকে থাকে যার রোল admin এবং স্ট্যাটাস active=True—সে হলো শুধু আব্দুল্লাহ।

আউটপুট দেখায়:

Active Admins: [{'id': 1, 'name': 'Abdullah', 'role': 'admin', 'active': True}]





ওয়েব ডেভেলপমেন্ট বা ব্যাকএন্ডে (যেমন জংগো বা ফ্লাস্টে) ডাইনামিকালি এইচটিএমএল ট্যাগ বা এট্রিবিউট তৈরির সময় **kwargs ব্যাপকভাবে ব্যবহৃত হয়।

def create_html_tag(tag_name, content, **attributes):
    # এট্রিবিউটগুলোর ডিকশনারি থেকে স্ট্রিং তৈরি করা (যেমন: class="btn" id="submit")
    attr_string = ""
    for key, value in attributes.items():
        attr_string += f' {key}="{value}"'
        
    # ফাইনাল ট্যাগ তৈরি
    html = f"<{tag_name}{attr_string}>{content}</{tag_name}>"
    return html

# টেস্ট করা যাক:
print(create_html_tag("a", "Click Here", href="https://google.com", target="_blank", className="link-primary"))
print(create_html_tag("button", "Submit", id="submit-btn", type="submit", disabled=True))



ধরে নিন আমরা ফাংশনটি এভাবে কল করেছি:

create_html_tag("div", "Hello World", class="container", id="main")

১. আর্গুমেন্ট ম্যাপিং ও প্যাকিং (Argument Mapping):
Positional Arguments: tag_name = "div", content = "Hello World"

Keyword Arguments (**attributes): পাইথন অতিরিক্ত নামযুক্ত আর্গুমেন্টগুলোকে প্যাক করে ডিকশনারি বানিয়ে নেয়:

Python
attributes = {
    'class': 'container', 
    'id': 'main'
}
২. এক্সিকিউশন ও স্টেট ট্রেস (Execution & State Trace):
Line 2 (attr_string = ""):

মেমোরিতে একটি খালি স্ট্রিং তৈরি করা হলো।

State: attr_string = ""

Line 3-4 (for key, value in attributes.items():):

ডিকশনারির ওপর লুপ চালিয়ে একটি একটি করে Key এবং Value এক্সট্রাক্ট করা হয়:

Iteration 1: key = 'class', value = 'container'

Operation: attr_string += f' class="container"'

Updated State: attr_string = ' class="container"'

Iteration 2: key = 'id', value = 'main'

Operation: attr_string += f' id="main"'

Final Updated State: attr_string = ' class="container" id="main"'

Line 6 (html = f"<{tag_name}{attr_string}>{content}</{tag_name}>"):

স্ট্রিং ইন্টারপোলেশন বা জোড়া লাগানোর কাজ:

< + "div" + ' class="container" id="main"' + ">" + "Hello World" + "</" + "div" + ">"

State: html = '<div class="container" id="main">Hello World</div>'

Line 7 (return html):

ফাংশনটি চূড়ান্ত এইচটিএমএল স্ট্রিং রিটার্ন করে এবং কাজ শেষ করে।






ইউজার প্রোফাইল আপডেটার (User Profile Updater)
একটি ব্যাকএন্ড সিস্টেমে ইউজারের প্রোফাইল আপডেট করার সময় ইউজার যেকোনো ফিল্ড (যেমন শুধু নাম, অথবা শুধু পাসওয়ার্ড, 
অথবা সবগুলো একসাথে) পরিবর্তন করতে পারে। **kwargs দিয়ে এটি খুব সহজে হ্যান্ডেল করা যায়।


# আমাদের ডাটাবেজে থাকা বর্তমান ইউজার ডেটা
user_profile = {"username": "abdullah", "email": "abdullah@gmail.com", "age": 30, "city": "Rangpur"}

def update_user_profile(**updates):
    print("Requested Updates:", updates)
    
    # বর্তমান প্রোফাইলের সাথে নতুন আপডেটগুলো মার্জ বা আপডেট করা
    for key, value in updates.items():
        if key in user_profile:
            user_profile[key] = value
            print(f"Updated '{key}' to '{value}'")
        else:
            print(f"Warning: Field '{key}' does not exist in user profile!")
            
    return user_profile

# টেস্ট করা যাক (শহর এবং বয়স আপডেট করা হচ্ছে):
updated_data = update_user_profile(city="Dhaka", age=31, country="Bangladesh")
print("\nFinal Profile:", updated_data)


১. প্রাথমিক অবস্থা (Initial State):
কোড রান করার আগে গ্লোবাল মেমোরিতে ডিকশনারিটি এভাবে আছে:

user_profile = {"username": "abdullah", "email": "abdullah@gmail.com", "age": 30, "city": "Rangpur"}

২. ফাংশন কল ও আর্গুমেন্ট প্যাকিং (update_user_profile(city="Dhaka", age=31, country="Bangladesh")):
Keyword Arguments (**updates): পাইথন পাস করা আর্গুমেন্টগুলোকে প্যাক করে ডিকশনারি বানায়:

Python
updates = {
    'city': 'Dhaka', 
    'age': 31, 
    'country': 'Bangladesh'
}
৩. এক্সিকিউশন ও স্টেট ট্রেস (Execution & State Trace):
Line 2 (print("Requested Updates:", updates)):

কনসোলে প্রিন্ট হয়:

Requested Updates: {'city': 'Dhaka', 'age': 31, 'country': 'Bangladesh'}

Line 5-11 (for key, value in updates.items():):

updates ডিকশনারির ওপর লুপ শুরু হয় এবং একে একে চেক করা হয়:

Iteration 1 (key = 'city', value = 'Dhaka'):

Check: if 'city' in user_profile: -> True (city অলরেডি user_profile-এ আছে)।

Operation: user_profile['city'] = 'Dhaka' (পুরোনো ভ্যালু "Rangpur" কেটে নতুন ভ্যালু "Dhaka" বসে যায়)।

Print: Updated 'city' to 'Dhaka'

Updated user_profile State:

{"username": "abdullah", "email": "abdullah@gmail.com", "age": 30, "city": "Dhaka"}

Iteration 2 (key = 'age', value = 31):

Check: if 'age' in user_profile: -> True (age প্রোফাইলে আছে)।

Operation: user_profile['age'] = 31 (পুরোনো বয়স 30 আপডেট হয়ে 31 হয়)।

Print: Updated 'age' to '31'

Updated user_profile State:

{"username": "abdullah", "email": "abdullah@gmail.com", "age": 31, "city": "Dhaka"}

Iteration 3 (key = 'country', value = 'Bangladesh'):

Check: if 'country' in user_profile: -> False (country নামের কোনো কি user_profile-এ নেই)।

else ব্লক রান করে।

Print: Warning: Field 'country' does not exist in user profile!

user_profile-এ কোনো পরিবর্তন হয় না।

Line 13 (return user_profile):

আপডেট হওয়া চূড়ান্ত ডিকশনারিটি updated_data ভেরিয়েবলে রিটার্ন হয়ে জমা হয়।

Line 17 (print("\nFinal Profile:", updated_data)):

কনসোলে চূড়ান্ত আউটপুট প্রিন্ট হয়:

Final Profile: {'username': 'abdullah', 'email': 'abdullah@gmail.com', 'age': 31, 'city': 'Dhaka'}






ফাংশন ওভাররাইডিং বা ডেকোরেটর প্যাটার্ন (Function Wrapper / Logging Decorator)
ব্যাকএন্ডে কোনো ফাংশন রান হওয়ার আগে বা পরে তার লজিক ট্র্যাক করার জন্য ডেকোরেটর ব্যবহার করা হয়, যেখানে **kwargs (এবং *args) জাদুকরী ভূমিকা রাখে।

def action_logger(func):
    def wrapper(*args, **kwargs):
        print(f"\n[INFO] Calling function: '{func.__name__}'")
        print(f"  -> Positional arguments passed: {args}")
        print(f"  -> Keyword arguments passed: {kwargs}")
        
        # আসল ফাংশনটি কল করা
        result = func(*args, **kwargs)
        print(f"[INFO] Function '{func.__name__' executed successfully!")
        return result
    return wrapper

# একটি সাধারণ ফাংশন ডিফাইন করে তার ওপর ডেকোরেটর বসানো
@action_logger
def calculate_salary(base, bonus, tax=0):
    return (base + bonus) - tax

# টেস্ট করা যাক:
total = calculate_salary(50000, 10000, tax=5000)
print("Final Salary:", total)



১. ডেকোরেটর আসলে কী করে?
সহজ কথায়, ডেকোরেটর হলো এমন একটি ফাংশন যা অন্য একটি ফাংশনকে মডিফাই না করে তার চারপাশে একটি "প পাহারা" বা "র‍্যাপার" বসিয়ে দেয়। 
এর ফলে আসল ফাংশন কল হওয়ার আগে বা পরে অতিরিক্ত কিছু কাজ (যেমন: লগ প্রিন্ট করা, সিকিউরিটি চেক করা) করা যায়।

২. লাইন বাই লাইন ড্রাই রান (কোড যেভাবে রান হয়)
ধাপ ক: ডেকোরেটর ডিফাইন করা এবং @ চিহ্নের ম্যাজিক
Python
@action_logger
def calculate_salary(base, bonus, tax=0):
    return (base + bonus) - tax
যখন  calculate_salary ফাংশনের ঠিক ওপরে @action_logger লেখেন, তখন পাইথন নীরবে একটি কাজ করে।
পাইথন আসলে ধরে নেয়:calculate_salary = action_logger(calculate_salary)

এর মানে হলো—আসল calculate_salary ফাংশনটি চলে যায় action_logger-এর ভেতর (func প্যারামিটার হিসেবে)।
আর বাইরে থেকে যখনই কেউ calculate_salary কল করবে, তখন সেটি আর আসল ফাংশন রান করবে না, রান করবে ডেকোরেটরের ভেতরে থাকা wrapper ফাংশনটি!

ধাপ খ: যখন ফাংশনটি কল করা হয়
Python
total = calculate_salary(50000, 10000, tax=5000)
এখানে ইউজার মানগুলো পাঠিয়েছেন। এই মানগুলো সরাসরি wrapper ফাংশনের ভেতরে থাকা *args এবং **kwargs-এ প্যাক হয়ে যায়:

args = (50000, 10000) (পজিশনাল আর্গুমেন্টগুলো টুপল হয়ে গেছে)

kwargs = {'tax': 5000} (কি-ওয়ার্ড আর্গুমেন্টটি ডিকশনারি হয়ে গেছে)

ধাপ গ: wrapper ফাংশনের ভেতরের লাইন বাই লাইন এক্সিকিউশন
এখন wrapper ফাংশনটির ভেতরের লাইনগুলো এক এক করে রান হয়:

print(f"\n[INFO] Calling function: '{func.__name__}'")

এটি রান হয়ে স্ক্রিনে প্রিন্ট করে:

[INFO] Calling function: 'calculate_salary'

print(f"  -> Positional arguments passed: {args}")

এটি প্রিন্ট করে:

-> Positional arguments passed: (50000, 10000)

print(f"  -> Keyword arguments passed: {kwargs}")

এটি প্রিন্ট করে:

-> Keyword arguments passed: {'tax': 5000}

result = func(*args, **kwargs) (সবচেয়ে গুরুত্বপূর্ণ লাইন!)

এখানে func মানে হলো আমাদের সেই আসল calculate_salary ফাংশনটি।

*args এবং **kwargs-কে ভেঙে (unpack করে) মানগুলো আসল ফাংশনে পাঠানো হয়। অর্থাৎ, আসল ফাংশনটি এভাবে কল হয়:

calculate_salary(50000, 10000, tax=5000)

আসল ফাংশন তার নিজের কাজ করে: (50000 + 10000) - 5000 = 55000।

এই 55000 মানটি result ভেরিয়েবলে জমা হয়।

print(f"[INFO] Function executed successfully!")

এটি সফলতার মেসেজ প্রিন্ট করে।

return result

ক্যালকুলেট করা মানটি (55000) বাইরে গ্লোবাল স্কোপে পাঠানো হয়, যা গিয়ে জমা হয় total ভেরিয়েবলে।

ধাপ ঘ: চূড়ান্ত প্রিন트

print("Final Salary:", total)

এটি স্ক্রিনে প্রিন্ট করে:

Final Salary: 55000
