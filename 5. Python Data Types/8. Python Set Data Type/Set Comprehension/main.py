ব্যাকএন্ড ডেভেলপমেন্ট বা সিকিউরিটি স্ক্রিপ্টিংয়ের সময় লজিক ফিল্টার করার জন্য সেট কমপ্রিহেনশন (Set Comprehension) জাদুর মতো কাজ করে।
এটি কোডকে খুব ছোট, সুন্দর এবং পাইথনিক (Pythonic) করে তোলে।

সাধারণ for লুপ ব্যবহার করে:

# কাঁচা ইমেল ডেটা (ডুপ্লিকেট এবং স্প্যাম থাকতে পারে)
raw_emails = [
    "admin@tech.com", 
    "user1@gmail.com", 
    "admin@tech.com",  # ডুপ্লিকেট
    "spammer@mail.xyz", # স্প্যাম ডোমেইন
    "user2@gmail.com"
]

# প্রথমে একটি খালি সেট তৈরি করা হলো
valid_unique_emails = set()

# for লুপ চালিয়ে ফিল্টার করা হচ্ছে
for email in raw_emails:
    # যদি ইমেলটি .xyz দিয়ে শেষ না হয়, তবেই সেটে যোগ করবে
    if not email.endswith(".xyz"):
        valid_unique_emails.add(email)

print("For লুপ দিয়ে আউটপুট:", valid_unique_emails)


সেট কমপ্রিহেনশন (Set Comprehension) ব্যবহার করে (এক লাইনে):
হুবহু একই কাজটিকে পাইথনের সেট কমপ্রিহেনশন ব্যবহার করে মাত্র এক লাইনে করে ফেলা যায়:

raw_emails = [
    "admin@tech.com", 
    "user1@gmail.com", 
    "admin@tech.com", 
    "spammer@mail.xyz", 
    "user2@gmail.com"
]

# সেট কমপ্রিহেনশন সিনট্যাক্স: {expression for item in iterable if condition}
valid_unique_emails_comp = {email for email in raw_emails if not email.endswith(".xyz")}

print("সেট কমপ্রিহেনশন দিয়ে আউটপুট:", valid_unique_emails_comp)




লগ ফাইল বা রিকোয়েস্ট থেকে ইউনিক আইপি (IP) অ্যাড্রেস ফিল্টার করা
ধরুন, আপনার সার্ভারে সারাদিনে হাজার হাজার রিকোয়েস্ট এসেছে এবং একটি লিস্টে সব আইপি জমা হয়েছে। 
এর মধ্যে কিছু লোকাল বা ডামি আইপি আছে (127.0.0.1) যেগুলো আপনার কাজে লাগবে না। 
চাচ্ছেন শুধু ভ্যালিড এবং ইউনিক আইপিগুলোর একটি সেট তৈরি করতে।

# সার্ভারে আসা সব রিকোয়েস্টের আইপি লিস্ট (যেখানে ডুপ্লিকেট এবং লোকাল আইপি আছে)
request_ips = [
    "192.168.1.10", 
    "10.0.0.5", 
    "192.168.1.10",  # ডুপ্লিকেট
    "127.0.0.1",     # লোকাল আইপি (বাদ দিতে হবে)
    "10.0.0.5",      # ডুপ্লিকেট
    "172.16.0.25"
]

# ১. প্রথমে একটি খালি সেট তৈরি করা হলো
unique_valid_ips = set()

# ২. for লুপ চালিয়ে একটি একটি করে আইপি চেক করা হচ্ছে
for ip in request_ips:
    # ৩. যদি আইপিটি "127.0.0.1" না হয়, তবেই সেটে যোগ করবে
    if ip != "127.0.0.1":
        unique_valid_ips.add(ip)

print("ভ্যালিড ইউনিক আইপি সমূহ (for লুপ দিয়ে):", unique_valid_ips)


comprehension

# সার্ভারে আসা সব রিকোয়েস্টের আইপি লিস্ট (যেখানে ডুপ্লিকেট এবং লোকাল আইপি আছে)
request_ips = [
    "192.168.1.10", 
    "10.0.0.5", 
    "192.168.1.10",  # ডুপ্লিকেট
    "127.0.0.1",     # লোকাল আইপি (বাদ দিতে হবে)
    "10.0.0.5",      # ডুপ্লিকেট
    "172.16.0.25"
]

# সেট কমপ্রিহেনশন ব্যবহার করে এক লাইনে ফিল্টার ও ইউনিক করা হলো
unique_valid_ips = {ip for ip in request_ips if ip != "127.0.0.1"}

print("ভ্যালিড ইউনিক আইপি সমূহ:", unique_valid_ips)


ইউজারনেমগুলোর দৈর্ঘ্য (Length) বের করা
ধরুন, আপনার ডাটাবেজে কিছু ইউজারের নাম আছে। আপনি চেক করতে চান যে ইউজারনেমগুলোর অক্ষর সংখ্যা
বা লেংথ ইউনিকভাবে কেমন (যেমন: কারো নাম ৩ অক্ষরের, কারো ৫ অক্ষরের ইত্যাদি)। এখানেও সেট কমপ্রিহেনশন দিয়ে কাজটি সেকেন্ডে করা যায়।


usernames = ["alex", "bob", "charlie", "david", "joe", "amy"]

# ১. প্রথমে একটি খালি সেট তৈরি করা হলো
name_lengths = set()

# ২. for লুপ চালিয়ে প্রতিটি নাম নিয়ে তার দৈর্ঘ্য (length) মাপা হচ্ছে
for name in usernames:
    length = len(name)
    # ৩. দৈর্ঘ্যটি সেটে যোগ করা হচ্ছে (সেট নিজে থেকেই ডুপ্লিকেট বাদ দিয়ে দেবে)
    name_lengths.add(length)

print("নামগুলোর ইউনিক দৈর্ঘ্য (for লুপ দিয়ে):", name_lengths)


comprehension 

# ইউজারনেমের লিস্ট
usernames = ["alex", "bob", "charlie", "david", "joe", "amy"]

# সেট কমপ্রিহেনশন দিয়ে প্রতিটি নামের দৈর্ঘ্য বের করে ইউনিক সেট তৈরি
name_lengths = {len(name) for name in usernames}

print("নামগুলোর ইউনিক দৈর্ঘ্য:", name_lengths)



শুধু নির্দিষ্ট কিছু শর্ত পূরণ করলে তবেই সেটে যুক্ত হবে, তবে if ব্যবহার করতে পারেন। যেমন—শুধু জোড় (even) সংখ্যাগুলোর স্কয়ার বের করা:


numbers = [1, 2, 3, 4, 5, 6]

even_squares = {x ** 2 for x in numbers if x % 2 == 0}

print(even_squares)
# আউটপুট: {4, 16, 36} (শুধু ২, ৪, এবং ৬ এর স্কয়ারগুলো এসেছে)



কটি লিস্ট আছে যেখানে কিছু নাম বা সংখ্যা একাধিকবার (ডুপ্লিকেট) আছে। 
সেট কমপ্রিহেনশন দিয়ে খুব সহজে শুধু ইউনিক বা আলাদা উপাদানগুলো বের করে নিতে:

# একটি লিস্ট যেখানে ডুপ্লিকেট উপাদান আছে
numbers = [1, 2, 2, 3, 4, 4, 5, 1]

# সেট কমপ্রিহেনশন ব্যবহার করে স্কয়ার বা বর্গ বের করা এবং ডুপ্লিকেট বাদ দেওয়া
unique_squares = {x ** 2 for x in numbers}

print(unique_squares)
# আউটপুট: {1, 4, 9, 16, 25} 
# (খেয়াল করুন: ডুপ্লিকেট সংখ্যাগুলো নিজে থেকেই বাদ হয়ে গেছে এবং সেকেন্ড ব্র্যাকেট `{}` আসার কারণে এটি একটি সেট হয়েছে)





ভবিষ্যতে টেক্সট প্রসেসিংয়ের সময় এটি খুব কাজে লাগবে। যেমন—একটি বাক্যের ইউনিক অক্ষরগুলো (spaces বাদ দিয়ে) একটি সেট:

text = "hello python"

# ভাওয়েল বা স্পেস বাদ দিয়ে ইউনিক অক্ষর বা সব অক্ষর আলাদা করা
unique_chars = {char for char in text if char != ' '}

print(unique_chars)
# আউটপুট: {'h', 'e', 'l', 'o', 'p', 'y', 't', 'n'} 
# (এখানে ডাবল 'l' বা 'o' থাকলে তা একটিই দেখাবে, কারণ এটি সেট!)





একটি সেট আছে, সেখান থেকে শর্ত সাপেক্ষে বা অপারেশন চালিয়ে সরাসরি আরেকটি সেট তৈরি

# মূল সেট
my_set = {1, 2, 3, 4, 5}

# সেট কমপ্রিহেনশন ব্যবহার করে প্রতিটা উপাদানের সাথে ২ যোগ করে নতুন সেট তৈরি
new_set = {x + 2 for x in my_set}

print(new_set)
# আউটপুট: {3, 4, 5, 6, 7} (আউটপুটটি একটি সেট হিসেবেই আসবে)




কন্ডিশন সহ সেট কমপ্রিহেনশন (Condition)
মূল সেট থেকে শুধু বিজোড় সংখ্যাগুলো ফিল্টার করে নতুন সেট তৈরি করা:


# মূল সেট
numbers_set = {10, 15, 20, 25, 30, 35}

# শুধু বিজোড় সংখ্যাগুলো দিয়ে নতুন সেট তৈরি
odd_set = {x for x in numbers_set if x % 2 != 0}

print(odd_set)
# আউটপুট: {35, 25, 15} (সেটের নিজস্ব নিয়মে অর্ডার এলোমেলো হতে পারে, কিন্তু উপাদানগুলো ইউনিক থাকবে)




ফলের সেট থেকে নির্দিষ্ট কোনো অক্ষর দিয়ে শুরু হওয়া ফলগুলো ফিল্টার করা:

# ফলের সেট
fruits_set = {"apple", "banana", "mango", "orange", "avocado"}

# যে ফলগুলো 'a' দিয়ে শুরু হয়, সেগুলোর বড় হাতের রূপ (uppercase) নিয়ে নতুন সেট
a_fruits = {fruit.upper() for fruit in fruits_set if fruit.startswith('a')}

print(a_fruits)
# আউটপুট: {'APPLE', 'AVOCADO'}

মূল কথা: ইনপুটে লিস্ট থাকুক বা সেট থাকুক, { } ব্র্যাকেট এবং ভেতরে লজিক ব্যবহার করলেই সেটি সেট কমপ্রিহেনশন হয়ে যায় 
এবং আউটপুট সবসময় একটি ইউনিক সেট হিসেবেই বের হয়ে আসে।




ডেটা ক্লিনিং বা স্ট্রিং ফরম্যাটিং (Data Cleaning)
ভবিষ্যতে ইউজারের ইনপুট করা ট্যাগ বা নামগুলোতে অতিরিক্ত স্পেস (whitespace) বা ছোট-বড় হাতের অক্ষরের ঝামেলা থাকতে পারে। 
একটি সেট থেকে সরাসরি সব স্ট্রিং ক্লিন করে নতুন সেট বানিয়ে নেওয়ার দারুণ একটা উদাহরণ:


# মূল সেট (যেখানে কিছু ট্যাগ এলোমেলো বা অতিরিক্ত স্পেসসহ আছে)
raw_tags = {" python", "JAVASCRIPT", " python ", "html", "CSS "}

# সেট কমপ্রিহেনশন দিয়ে স্পেস দূর করা এবং সব ছোট হাতের অক্ষরে রূপান্তর করা
clean_tags = {tag.strip().lower() for tag in raw_tags}

print(clean_tags)
# আউটপুট: {'python', 'javascript', 'html', 'css'}
# (অতিরিক্ত স্পেস দূর হয়ে গেছে এবং ডুপ্লিকেট 'python' নিজে থেকেই বাদ হয়ে গেছে!)




শর্ত সাপেক্ষে ফিল্টারিং (Filtering Data)
আপনার কাছে ছাত্র-ছাত্রীদের প্রাপ্ত নম্বরের একটি সেট আছে। সেখান থেকে নির্দিষ্ট শর্ত পূরণ করে পাস করা নম্বরগুলোর 
একটি নতুন সেট তৈরি করতে:


# মূল নম্বরের সেট
scores_set = {45, 82, 33, 90, 65, 50, 28}

# শুধু ৫০ বা তার বেশি নম্বরগুলো নিয়ে নতুন সেট তৈরি
passed_scores = {score for score in scores_set if score >= 50}

print(passed_scores)
# আউটপুট: {82, 90, 65, 50, 45}



গণিত বা ক্যালকুলেশন সরাসরি সেটে প্রয়োগ (Mathematical Calculations)
ধরে নিন আপনার কাছে কিছু পণ্যের দামের (ডলারে) একটি সেট আছে। 
সেট কমপ্রিহেনশন ব্যবহার করে এক লাইনেই সেগুলোকে টাকায় রূপান্তর করে নতুন সেট বানিয়ে ফেলতে:


# ডলারে পণ্যের দামের সেট
prices_in_usd = {10, 25, 50, 100}

# প্রতিটির সাথে ১১৭ গুণ করে টাকায় রূপান্তর করে নতুন সেট তৈরি (ধরে নিলাম ১ ডলার = ১১৭ টাকা)
prices_in_bdt = {price * 117 for price in prices_in_usd}

print(prices_in_bdt)
# আউটপুট: {11700, 2925, 5850, 1170}



বিভিন্ন শব্দের একটি সেট আছে। আপনি চান প্রতিটি শব্দের দৈর্ঘ্য (কতটি অক্ষর আছে) কত,
তা দিয়ে একটি নতুন সেট বানাতে (এখানে ডুপ্লিকেট দৈর্ঘ্যগুলো নিজে থেকেই বাদ হয়ে যাবে):

# শব্দের সেট
words_set = {"apple", "banana", "cat", "dog", "elephant"}

# প্রতিটি শব্দের দৈর্ঘ্য বের করে নতুন সেট তৈরি
lengths_set = {len(word) for word in words_set}

print(lengths_set)
# আউটপুট: {3, 5, 6, 8} (ডুপ্লিকেট বাদ দিয়ে ইউনিক অক্ষরের সংখ্যাগুলো চলে আসবে)





নেগেটিভ সংখ্যাকে পজিটিভ করা (Absolute Values)
আপনার কাছে পজিটিভ এবং নেগেটিভ (ঋণাত্মক) সংখ্যার একটি এলোমেলো সেট আছে।
abs() ফাংশন ব্যবহার করে সেগুলোকে পজিটিভ বানিয়ে নতুন সেট তৈরি করতে


# মিশ্র সংখ্যার সেট
numbers_set = {-5, 3, -2, 8, -5, 10}

# সব নেগেটিভ সংখ্যাকে পজিটিভ করে নতুন সেট তৈরি
positive_set = {abs(num) for num in numbers_set}

print(positive_set)
# আউটপুট: {2, 3, 5, 8, 10} (এখানে -5 এবং 5 এর কারণে ডুপ্লিকেট হওয়ার কথা থাকলেও সেট তা নিজে থেকেই হ্যান্ডেল করে ইউনিক রাখবে)




কন্ডিশন এবং অপারেশন একসাথে (Condition + Transformation)
ভবিষ্যতে ডেটা ফিল্টার করার সময় এই প্যাটার্নটি প্রচুর কাজে লাগবে। 
যেমন—৩ অক্ষরের চেয়ে বড় শব্দগুলোকে বড় হাতের অক্ষরে (upper) রূপান্তর করে নতুন সেট বানানো:


# ছোট শব্দের সেট
tech_set = {"ai", "python", "css", "django", "html"}

# ৩ অক্ষরের বেশি বড় শব্দগুলো ফিল্টার করে uppercase করা
processed_set = {word.upper() for word in tech_set if len(word) > 3}

print(processed_set)
# আউটপুট: {'PYTHON', 'DJANGO', 'HTML'} (ছোট 'ai' এবং 'css' বাদ পড়ে গেছে)



একটি সেটে কিছু নামের আগে বা পরে অতিরিক্ত স্পেস ( ) রয়ে গেছে। 
.strip() ব্যবহার করে এক লাইনে সেগুলোকে একদম পরিষ্কার করে ফেলা যায়:


# এলোমেলো স্পেসযুক্ত নামের সেট
raw_names = {"  rahim ", "karim", " rahim", "salma  ", "  karim "}

# .strip() দিয়ে অতিরিক্ত স্পেস দূর করা এবং ডুপ্লিকেট বাদ দেওয়া
clean_names = {name.strip() for name in raw_names}

print(clean_names)
# আউটপুট: {'rahim', 'karim', 'salma'} 
# (স্পেসও দূর হলো, ডুপ্লিকেট 'rahim' ও 'karim' ও বাদ পড়ে গেল!)


.strip() এর সাথে ছোট হাতের অক্ষরে রূপান্তর (.lower())
বাস্তব প্রজেক্টে ডেটা ক্লিনিংয়ের সময় .strip() এবং .lower() একসাথে প্রচুর ব্যবহৃত হয়। 
এতে লেখা ছোট-বড় বা এলোমেলো যাই থাকুক না কেন, সেট একদম নিখুঁত হয়ে যায়:


# এলোমেলো ক্যাপিটাল ও স্পেসযুক্ত ক্যাটাগরির সেট
raw_categories = {" Electronics", "CLOTHING ", "electronics", "  books "}

# .strip() এবং .lower() একসাথে ব্যবহার করে ইউনিক ক্লিন সেট তৈরি
normalized_categories = {cat.strip().lower() for cat in raw_categories}

print(normalized_categories)
# আউটপুট: {'electronics', 'clothing', 'books'}




স্পেস রিমুভ করার পাশাপাশি খালি বা ফাঁকা উপাদান বাদ দেওয়া (Condition with strip)
অনেক সময় ইউজারের ইনপুটে শুধু স্পেস বা ফাঁকা স্ট্রিং থাকতে পারে। .strip() ব্যবহার করে 
খুব সহজেই শর্ত দিয়ে সেগুলোকে ফিল্টার করে বাদ দিতে



# ফাঁকা স্পেস বা ডেটাসহ সেট
user_inputs = {"  apple ", "   ", "banana", "  ", " mango "}

# স্পেস রিমুভ করার পর যেগুলোর লেন্থ শূন্য নয় (অর্থাৎ খালি নয়), শুধু সেগুলো রাখা
valid_inputs = {item.strip() for item in user_inputs if item.strip() != ""}

print(valid_inputs)
# আউটপুট: {'apple', 'banana', 'mango'} 
# (মাঝখানের শুধু স্পেস বা ফাকা মানগুলো নিজে থেকেই ফিল্টার হয়ে বাদ গেছে!)











ফাইল আপলোড সিকিউরিটি (অনিরাপদ ফাইল এক্সটেনশন ফিল্টার করা)
ওয়েব অ্যাপ্লিকেশনে ইউজাররা যখন ফাইল আপলোড করে, তখন সিকিউরিটির জন্য
অনেক সময় .exe, .bat, বা .sh এর মতো ক্ষতিকারক এক্সটেনশনগুলো ব্লক করতে হয়।

# ইউজারদের আপলোড করা ফাইলের লিস্ট
uploaded_files = ["avatar.png", "script.exe", "document.pdf", "malware.exe", "resume.docx"]

# খালি সেট
safe_files = set()

for file in uploaded_files:
    # যদি ফাইলটি .exe দিয়ে শেষ না হয়, তবেই সেটে যোগ করবে
    if not file.endswith(".exe"):
        safe_files.add(file)

print("For লুপ দিয়ে নিরাপদ ফাইল:", safe_files)



সেট কমপ্রিহেনশন দিয়ে (এক লাইনে):


uploaded_files = ["avatar.png", "script.exe", "document.pdf", "malware.exe", "resume.docx"]

# এক লাইনে সেট কমপ্রিহেনশন
safe_files_comp = {file for file in uploaded_files if not file.endswith(".exe")}

print("কমপ্রিহেনশন দিয়ে নিরাপদ ফাইল:", safe_files_comp)





API রিকোয়েস্ট মেথড ফিল্টার করা (অননুমোদিত মেথড বাদ দেওয়া)
আপনার ব্যাকএন্ড এপিআই-তে বিভিন্ন রিকোয়েস্ট (GET, POST, DELETE, PUT) আসে। 
আপনি হয়তো সিকিউরিটির জন্য শুধু নির্দিষ্ট কিছু রিড-অনলি বা সেফ মেথডগুলো ট্র্যাক করতে চান বা ডিলিট রিকোয়েস্টগুলোকে ফিল্টার করতে চান।

# সার্ভারে আসা রিকোয়েস্ট মেথডের লিস্ট
api_requests = ["GET", "POST", "GET", "DELETE", "PUT", "POST", "GET"]

# ইউনিক ও সেফ মেথড রাখার জন্য সেট
allowed_methods = set()

for method in api_requests:
    # যদি মেথডটি DELETE বা PUT না হয়
    if method != "DELETE" and method != "PUT":
        allowed_methods.add(method)

print("For লুপ দিয়ে অ্যালাউড মেথড:", allowed_methods)



সেট কমপ্রিহেনশন দিয়ে (এক লাইনে):

api_requests = ["GET", "POST", "GET", "DELETE", "PUT", "POST", "GET"]

# এক লাইনে সেট কমপ্রিহেনশন
allowed_methods_comp = {method for method in api_requests if method not in ("DELETE", "PUT")}

print("কমপ্রিহেনশন দিয়ে অ্যালাউড মেথড:", allowed_methods_comp)



HTTP স্ট্যাটাস কোড ফিল্টার করা (সার্ভার এরর কোড বাদ দেওয়া)
ব্যাকএন্ডে কোনো এপিআই রিকোয়েস্টের পর বিভিন্ন স্ট্যাটাস কোড (200, 400, 500, 404) আসতে পারে।
আপনি হয়তো চাচ্ছেন সার্ভারের বড় কোনো ক্র্যাশ বা এরর কোড (500) বাদ দিয়ে বাকি ইউনিক রেসপন্স কোডগুলোর একটি সেট তৈরি করতে।

# এপিআই রেসপন্স থেকে আসা স্ট্যাটাস কোডের লিস্ট
status_codes = [200, 400, 500, 200, 404, 500, 201]

# খালি সেট
valid_statuses = set()

for code in status_codes:
    # যদি কোডটি 500 (সার্ভার এরর) না হয়
    if code != 500:
        valid_statuses.add(code)

print("For লুপ দিয়ে ভ্যালিড স্ট্যাটাস:", valid_statuses)


সেট কমপ্রিহেনশন দিয়ে (এক লাইনে):

status_codes = [200, 400, 500, 200, 404, 500, 201]

# এক লাইনে সেট কমপ্রিহেনশন
valid_statuses_comp = {code for code in status_codes if code != 500}

print("কমপ্রিহেনশন দিয়ে ভ্যালিড স্ট্যাটাস:", valid_statuses_comp)




কমন আইটেম খোঁজা (যা .intersection() বা & অপারেটরের কাজ করে)
ব্যাকএন্ড স্কিল এবং সিকিউরিটি স্কিলের দুটি লিস্ট আছে। উভয় লিস্টেই আছে (কমন) এমন স্কিলগুলো বের করতে 

backend_skills = ["Python", "Node.js", "SQL", "Docker"]
security_skills = ["Python", "Linux", "Docker", "Wireshark"]

common_skills = set()

for skill in backend_skills:
    # যদি স্কিলটি সিকিউরিটি লিস্টেও থাকে
    if skill in security_skills:
        common_skills.add(skill)

print("For লুপ দিয়ে কমন স্কিল:", common_skills)

সেট কমপ্রিহেনশন দিয়ে (এক লাইনে):

backend_skills = ["Python", "Node.js", "SQL", "Docker"]
security_skills = {"Python", "Linux", "Docker", "Wireshark"}

# এক লাইনে কমপ্রিহেনশন
common_skills_comp = {skill for skill in backend_skills if skill in security_skills}

print("কমপ্রিহেনশন দিয়ে কমন স্কিল:", common_skills_comp)




বাদ দেওয়া বা ডিফারেন্স বের করা (যা .difference() বা - অপারেটরের কাজ করে)
ধরুন, মোট ইউজারের লিস্ট থেকে ব্যান হওয়া ইউজারদের বাদ দিয়ে একটিভ ইউজারদের লিস্ট বের করতে চান।

all_users = ["Rahim", "Karim", "Sakib", "Arman"]
banned_users = ["Karim", "Sakib"]

active_users = set()

for user in all_users:
    # যদি ইউজারটি ব্যানড লিস্টে না থাকে
    if user not in banned_users:
        active_users.add(user)

print("For লুপ দিয়ে একটিভ ইউজার:", active_users)

সেট কমপ্রিহেনশন দিয়ে (এক লাইনে):

all_users = ["Rahim", "Karim", "Sakib", "Arman"]
banned_users = {"Karim", "Sakib"}

# এক লাইনে কমপ্রিহেনশন
active_users_comp = {user for user in all_users if user not in banned_users}

print("কমপ্রিহেনশন দিয়ে একটিভ ইউজার:", active_users_comp)



ইউনিয়ন বা সব এক করা (যা .union() বা | অপারেটরের কাজ করে)
ধরুন, আপনার কাছে আলাদা দুটি ভিন্ন লিস্ট বা সেট আছে, যেগুলোকে লুপ চালিয়ে বা কমপ্রিহেনশন দিয়ে একটি ইউনিক সেটে রূপান্তর করতে চান।

team_a = ["Rahim", "Karim"]
team_b = ["Karim", "Sakib", "Arman"]

all_members = set()

# প্রথম লিস্টের মেম্বার যোগ করা
for name in team_a:
    all_members.add(name)

# দ্বিতীয় লিস্টের মেম্বার যোগ করা
for name in team_b:
    all_members.add(name)

print("For লুপ দিয়ে Union:", all_members)

সেট কমপ্রিহেনশন দিয়ে (নেস্টেড লুপ সহ):

team_a = ["Rahim", "Karim"]
team_b = ["Karim", "Sakib", "Arman"]

# দুটি লিস্টকে একসাথে লুপ চালিয়ে সেট কমপ্রিহেনশন
union_comp = {name for team in (team_a, team_b) for name in team}

print("কমপ্রিহেনশন দিয়ে Union:", union_comp)




সিমেট্রিক ডিফারেন্স বা উভয় সেটের কমন উপাদান বাদ দেওয়া (যা .symmetric_difference() এর কাজ করে)
এর কাজ হলো—যে উপাদানগুলো উভয় সেটে আছে (কমন) সেগুলো বাদ দিয়ে বাকি ইউনিক উপাদানগুলো খুঁজে বের করা।


set1 = {1, 2, 3}
set2 = {3, 4, 5}

sym_diff_result = set()

# set1 এর উপাদান চেক করা যা set2 এ নেই
for x in set1:
    if x not in set2:
        sym_diff_result.add(x)

# set2 এর উপাদান চেক করা যা set1 এ নেই
for x in set2:
    if x not in set1:
        sym_diff_result.add(x)

print("For লুপ দিয়ে Symmetric Difference:", sym_diff_result)

সেট কমপ্রিহেনশন দিয়ে:

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# কমপ্রিহেনশনে লজিক: যা উভয় সেটের মিলের (intersection) মধ্যে নেই
sym_diff_comp = {x for x in set1.union(set2) if x not in set1.intersection(set2)}

print("কমপ্রিহেনশন দিয়ে Symmetric Difference:", sym_diff_comp)



আপডেট মেথডসমূহ (যা সরাসরি মূল সেটকে পরিবর্তন করে ফেলে)
ক. .update() মেথড
এটি একাধিক উপাদান বা অন্য কোনো ইটারেবল (যেমন লিস্ট বা অন্য সেট) থেকে ডেটা এনে সরাসরি মূল সেটের সাথে যুক্ত করে দেয় 
(যেমনটা .union() করে, তবে এটি নতুন সেট না বানিয়ে মূল সেটকেই বড় করে)।

allowed_ips = {"192.168.1.1"}
new_ips = ["10.0.0.1", "172.16.0.1"]

# for লুপ দিয়ে একটি একটি করে আইপি মূল সেটে যোগ করা
for ip in new_ips:
    allowed_ips.add(ip)

print("For লুপ দিয়ে Update:", allowed_ips)



.difference_update() মেথডের কাজ for লুপ দিয়ে
নির্দিষ্ট কিছু উপাদান লিস্ট বা সেট থেকে লুপ চালিয়ে বাদ দেওয়া:

permissions = {"read", "write", "execute", "delete"}
restricted = {"delete"}

# for লুপ চালিয়ে রেস্ট্রিক্টেড আইটেমগুলো বাদ দেওয়া
for perm in restricted:
    permissions.discard(perm)  # discard ব্যবহার করলে উপাদান না থাকলেও এরর খাবে না

print("For লুপ দিয়ে Difference Update:", permissions)


.issubset() চেক করার কাজ for লুপ দিয়ে
একটি সেট অন্যটির সাবসেট কি না, তা for লুপ ও ফ্ল্যাগ ভ্যারিয়েবল দিয়ে চেক করা:

user_permissions = {"read", "write"}
required_permissions = {"read", "write", "execute"}

# ধরে নিলাম সাবসেট বটে
is_sub = True

for perm in user_permissions:
    if perm not in required_permissions:
        is_sub = False
        break  # মিল না পেলে লুপ ভেঙে বেরিয়ে যাবে

print("For লুপ দিয়ে Is Subset চেক:", is_sub)


যেসব মেথড (.update(), .difference_update(), .issubset() ইত্যাদি) এবং লজিক 
সেগুলোর ক্ষেত্রে কমপ্রিহেনশন (Comprehension) কেন ব্যবহার করা হয় না

কমপ্রিহেনশন কেন এই মেথডগুলোতে সচরাচর ব্যবহার করা হয় না?
পাইথনে কমপ্রিহেনশন (যেমন: সেট কমপ্রিহেনশন {x for x in ...}) তৈরি করা হয় মূলত নতুন কোনো 
কালেকশন (নতুন সেট বা লিস্ট) তৈরি করার জন্য বা ফিল্টার করার জন্য।

কিন্তু .update() বা .difference_update() এর মতো মেথডগুলোর কাজ হলো আগে থেকেই থাকা মূল সেটকে মডিফাই বা আপডেট করা (Mutate করা)। 
এগুলোর জন্য কমপ্রিহেনশনের চেয়ে সরাসরি মেথড ব্যবহার করাই পাইথনের নিয়ম এবং এটাই সবচেয়ে সহজ ও স্ট্যান্ডার্ড পদ্ধতি।





টেক্সট থেকে ইউনিক এবং ছোট হাতের (Lowercase) শব্দ আলাদা করা (For লুপ দিয়ে)


text = "Python is powerful and python is easy to learn and use"

# প্রথমে একটি খালি সেট তৈরি করা হলো
unique_words = set()

# for লুপ চালিয়ে একে একে শব্দ যোগ করা হলো
for word in text.split():
  unique_words.add(word.lower())

print("Unique Lowercase Words:", unique_words)




text = "Python is powerful and python is easy to learn and use"

# সেট কমপ্রিহেনশন ব্যবহার করে ইউনিক ও লোয়ারকেস শব্দের সেট তৈরি
unique_words = {word.lower() for word in text.split()}

print("Unique Lowercase Words:", unique_words)



ডেটাবেজ বা ইউজার ইনপুট থেকে স্পেস (Whitespace) রিমুভ করা (For লুপ দিয়ে)

raw_usernames = {" rahim", "karim ", " tanvir ", "rahim", "salma"}

# খালি সেট তৈরি
clean_usernames = set()

# for লুপ ও strip() ব্যবহার করে সেটে যুক্ত করা
for name in raw_usernames:
  clean_usernames.add(name.strip())

print("Clean Unique Usernames:", clean_usernames)



raw_usernames = {" rahim", "karim ", " tanvir ", "rahim", "salma"}

# সেট কমপ্রিহেনশন ব্যবহার করে স্পেস রিমুভ ও ইউনিক সেট তৈরি
clean_usernames = {name.strip() for name in raw_usernames}

print("Clean Unique Usernames:", clean_usernames)




কন্ডিশন ব্যবহার করে নির্দিষ্ট আইটেম ফিল্টার করা (For ও If দিয়ে)

product_prices = [45, 120, 85, 120, 250, 90, 45, 300]

# খালি সেট তৈরি
expensive_prices = set()

# লুপ এবং কন্ডিশন ব্যবহার করে ফিল্টার করা
for price in product_prices:
  if price > 100:
    expensive_prices.add(price)

print("Expensive Unique Prices:", expensive_prices)


product_prices = [45, 120, 85, 120, 250, 90, 45, 300]

# সেট কমপ্রিহেনশন এবং কন্ডিশন ব্যবহার করে এক লাইনে ফিল্টার করা
expensive_prices = {price for price in product_prices if price > 100}

print("Expensive Unique Prices:", expensive_prices)
