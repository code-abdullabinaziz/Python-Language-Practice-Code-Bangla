*args কী এবং কেন ব্যবহার করা হয়?
কী বলে একে? (Definition)
*args এর পুরো অর্থ হলো Arguments (তবে মূল জিনিসটি হলো সামনের তারকাচিহ্ন বা *)। 
এটি এমন একটি স্পেশাল প্যারামিটার, যা ফাংশনে অনির্ধারিত বা যত খুশি তত পজিশনাল ইনপুট (Positional Arguments) নিতে পারে।


কেন ব্যবহার করা হয়? (Why)
সাধারণত আমরা যখন ফাংশন বানাই, তখন নির্দিষ্ট করে দিতে হয় কয়টি ইনপুট নেব:

def jog(a, b):
    return a + b

এখানে শুধু দুটি সংখ্যাই যোগ করা যাবে। কিন্তু যদি এমন একটি ফাংশন বানাতে চাওয়া হয় যেখানে ইউজার চাইলে ২টি, ৫টি বা ১০টি সংখ্যা পাঠাতে পারবে—
তখন তো আর সারাজীবনের জন্য প্যারামিটার লিখে শেষ করতে পারবেন না!

এই সমস্যার সমাধানই হলো *args। এটি ইউজার যতগুলো মান পাঠাবে, সবগুলোকে একসাথে ধরে একটি Tuple (টুপল) বানিয়ে ফেলে।


def show_names(*args):
    print("The inputs are:", args)
    print("Data type:", type(args))

# ফাংশন কল করা
show_names("Rahim", "Karim", "Tanvir")


ধাপ ১: লাইন ১ (def show_names(*args):)

কী ঘটে: পাইথন ইন্টারপ্রেটার এই লাইনটি পড়ে বোঝে যে show_names নামের একটি ফাংশন ডিফাইন (Define) করা হয়েছে।

*args-এর কেরামতি: এখানে প্যারামিটারে *args থাকার কারণে পাইথন প্রস্তুত হয়ে থাকে যে, এই ফাংশনে যতগুলোই পজিশনাল আর্গুমেন্ট পাঠানো হোক না কেন, সেগুলোকে একটি Tuple (টুপল) আকারে বন্দী করতে হবে।

আউটপুট: এই লাইনে সরাসরি কোনো আউটপুট প্রিন্ট হবে না, শুধু ফাংশনটি মেমোরিতে সেভ হয়ে থাকবে।

ধাপ ২: লাইন ৬ (show_names("Rahim", "Karim", "Tanvir"))
কী ঘটে: পাইথন কোড পড়তে পড়তে যখন এই ফাংশন কলিং লাইনে আসে, তখন আসল কাজ শুরু হয়।

ফাংশনের ভেতর তিনটি মান পাঠানো হয়েছে: "Rahim", "Karim", এবং "Tanvir"।

পাইথন এই তিনটি মানকে প্যাক করে একটি টুপল বানিয়ে ফেলে: ('Rahim', 'Karim', 'Tanvir') এবং এই টুপলটিকে args ভেরিয়েবলের মধ্যে এসাইন (Assign) করে দেয়।

ধাপ ৩: ফাংশনের ভেতরে প্রবেশ এবং লাইন ২ (print("The inputs are:", args))
কী ঘটে: পাইথন এখন ফাংশনের ভেতরে ঢুকে দ্বিতীয় লাইনে আসে।

এখানে args ভেরিয়েবলের মান প্রিন্ট করার নির্দেশ দেওয়া হয়েছে। যেহেতু args-এর ভেতর টুপলটি জমা আছে, তাই পাইথন সেটি স্ক্রিনে প্রিন্ট করে দেয়।

এই লাইনের আউটপুট:

Plaintext
The inputs are: ('Rahim', 'Karim', 'Tanvir')
ধাপ ৪: লাইন ৩ (print("Data type:", type(args)))
কী ঘটে: পাইথন পরবর্তী লাইনে আসে।

এখানে type(args) ফাংশনটি কল করা হয়। পাইথন চেক করে দেখে args এর ডেটা টাইপ কী।
যেহেতু এটি *args দিয়ে রিসিভ করা হয়েছে, তাই পাইথন বলে দেয় এটি একটি tuple ক্লাস।

Data type: <class 'tuple'>


def my_function(*args):
    print("Received arguments:", args)
    print("Data type:", type(args))
    
 
    print("\nIndividual items:")
    for item in args:
        print("-", item)


my_function("apple", "banana", "cherry", 100, True)







ধাপ ১: বেসিক সমস্যা ও কেন *args দরকার? (The Basic Problem)

ধরে নেই এমন একটি ফাংশন বানাতে চাওয়া হসছে যা ইউজার যতগুলো সংখ্যা দেবে, সবগুলোর যোগফল বের করে দেবে।

সাধারণ নিয়মে আমরা এভাবে কোড লিখি:

def add(a, b):
    return a + b

print(add(5, 10))  # আউটপুট: 15


সমস্যা কোথায়?
এই add ফাংশনটি শুধু দুটি সংখ্যা যোগ করতে পারে। যদি হঠাৎ ৩টি সংখ্যা যোগ করতে চাওয়া হয় (add(5, 10, 15)), 
তখন পাইথন ভুল ধরবে এবং এরর দেবে। কারণ পাইথন জানে না কয়টি ইনপুট পাঠানো হবে।

এই সমস্যা সমাধানের জন্যই পাইথনে এসেছে *args!


ধাপ ২: *args-এর বেসিক গঠন (Basic *args)

নামের আগে একটা তারকাচিহ্ন (*) দিলেই পাইথন বুঝে নেয় যে এটি যেকোনো সংখ্যক পজিশনাল আর্গুমেন্ট গ্রহণ করতে পারে।



def print_numbers(*args):
    print(args)

# ফাংশনটিকে আমরা বিভিন্নভাবে কল করতে পারি:
print_numbers(1, 2, 3)
print_numbers(10, 20, 30, 40, 50)


(1, 2, 3)
(10, 20, 30, 40, 50)


খেয়াল করি, যতগুলোই মান দিন না কেন, পাইথন সেগুলোকে ব্র্যাকেটের মধ্যে বন্দি করে একটি Tuple (টুপল) বানিয়ে ফেলেছে।

অর্থাৎ, *args হলো জাদুকরী একটা ব্যাগ, যার মধ্যে আপনি যত খুশি মান ফেলতে পারেন 
এবং পাইথন সেগুলোকে টুপল বানিয়ে ব্যাগের ভেতর রেখে দেয়। 
(args নামটি মেন্ডেটরি নয়, আপনি চাইলে *numbers বা *items ও লিখতে পারেন, তবে কনভেনশন হলো *args লেখা)।



একটু বাস্তব উদাহরণ (Practical Example)
এখন আগের সেই যোগ করার সমস্যাটা আমরা *args দিয়ে সমাধান করব। 
যেহেতু args একটি টুপল, তাই এর ওপর লুপ (for loop) চালিয়ে সব মান যোগ করে ফেলা যায়:

def sum_all_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

# এখন আপনি যত খুশি সংখ্যা দিয়ে ট্রাই করতে পারেন:
print(sum_all_numbers(5, 10))             # আউটপুট: 15
print(sum_all_numbers(1, 2, 3, 4, 5))     # আউটপুট: 15
print(sum_all_numbers(100, 200, 300))     # আউটপুট: 600

এখানে ইউজার চাইলে ২টি সংখ্যা দিতে পারে, আবার ৫টি বা ১০টি সংখ্যাও দিতে পারে। ফাংশনটি সবার জন্যই পারফেক্টলি কাজ করবে!







একটু অ্যাডভান্সড লেভেল (Advanced Use Case)ঃ

এবার একটু অন্যরকম সিনারিও দেখি। অনেক সময় আমাদের এমন ফাংশন বানাতে হয় 
যেখানে কিছু নির্দিষ্ট প্যারামিটার থাকে এবং সাথে কিছু অতিরিক্ত বা ফ্লেক্সিবল আর্গুমেন্ট থাকতে পারে।

নিয়ম: সাধারণ প্যারামিটার এবং *args একসাথে ব্যবহার করলে, সাধারণ প্যারামিটারগুলো আগে বসাতে হয় এবং *args সবসময় শেষে বসাতে হয়।


def user_profile(username, *args):
    print(f"Username: {username}")
    print(f"User Skills/Tags (*args): {args}")

# ফাংশন কল করা
user_profile("tanvir_dev", "Python", "FastAPI", "Backend", "Docker")


Username: tanvir_dev
User Skills/Tags (*args): ('Python', 'FastAPI', 'Backend', 'Docker')

এখানে "tanvir_dev" চলে গেছে নির্দিষ্ট প্যারামিটার username-এর কাছে।

আর বাকি যতগুলো মান দেওয়া হয়েছে, সেগুলোকে পাইথন প্যাক করে একটি টুপল বানিয়ে *args-এর ভেতর ঢুকিয়ে দিয়েছে।





আরও একটু অ্যাডভান্সড — আনপ্যাকিং (Unpacking with *)ঃ

ফাংশন তৈরি করার সময় যেমন *args দিয়ে মান প্যাক করি, 
ঠিক তেমনি পাইথনে কোনো লিস্ট বা টুপলকে ভেঙে ফাংশনে পাঠাতে চাইলে স্টার (*) ব্যবহার করে আনপ্যাক করা যায়।



def multiply(a, b, c):
    return a * b * c

# আমাদের কাছে একটি সাধারণ লিস্ট আছে:
numbers = [2, 3, 4]

# যদি আমরা সরাসরি multiply(numbers দিই, পাইথন এরর দেবে। 
# কিন্তু সামনে একটি স্টার (*) দিয়ে দিলে পাইথন লিস্টটি ভেঙে আলাদা আলাদা মান হিসেবে পাঠিয়ে দেবে:

result = multiply(*numbers)  # এটি আসলে multiply(2, 3, 4) এর সমান কাজ করে

print("Multiplication Result:", result)  # আউটপুট: 24


সারাংশ (Summary):
বেসিক: যখন জানা থাকে না ইউজার কয়টি ইনপুট পাঠাবে, তখন *args ব্যবহার করা হয়।

মেকানিক্স: এটি সব পজিশনাল ইনপুটকে একটি Tuple বানিয়ে ফেলে।

লুপ: টুপল হওয়ার কারণে এর ওপর লুপ চালিয়ে ডেটা প্রসেস করা যায়।

অ্যাডভান্সড: নির্দিষ্ট প্যারামিটারের সাথে এটি কম্বাইন করে ব্যবহার করা যায় এবং লিস্ট/টুপল আনপ্যাকিংয়ের কাজেও * ব্যবহৃত হয়।







অবস্থান বা সিকোয়েন্স (Position Rule)
ফাংশন ডিফাইন করার সময় পজিশনাল প্যারামিটার এবং *args-এর ক্রম বা সিরিয়াল ঠিক রাখা জরুরি:

# সঠিক পদ্ধতি:
def correct_func(a, b, *args):
    pass

# ভুল পদ্ধতি (এটি এরর দেবে):
# def wrong_func(*args, a, b):
#     pass

নিয়ম: সাধারণ প্যারামিটারগুলো সবসময় আগে এবং *args সবসময় পরে বসবে।


ফাঁকা ইনপুট দেওয়া (Empty *args)
ফাংশন কল করার সময় আপনি যদি *args-এর জন্য কোনো মান নাও দেন,
তাও পাইথন কোনো এরর দেবে না। সে ক্ষেত্রে এটি একটি খালি টুপল () হিসেবে কাজ করবে।

def check_data(main_id, *args):
    print("Main ID:", main_id)
    print("Extra Args:", args)

check_data(101) 
# Output: 
# Main ID: 101
# Extra Args: ()



নির্দিষ্ট প্যারামিটারের সাথে *args ব্যবহার (Advanced Use Case)
অনেক সময় আমাদের ব্যাকএন্ড ফাংশনে কিছু নির্দিষ্ট (Fix) প্যারামিটার দরকার হয়, আর বাকিগুলো ফ্লেক্সিবল রাখতে হয়।

নিয়ম: সাধারণ প্যারামিটারকে সবসময় আগে রাখতে হবে, আর *args-কে শেষে বসাতে হবে।

def create_user_profile(username, role, *skills):
    print("Username:", username)
    print("Role:", role)
    print("Skills (Tuple):", skills)

# ফাংশন কল করা
create_user_profile("tanvir_dev", "Backend Developer", "Python", "FastAPI", "Docker", "PostgreSQL")


ড্রাই রান ও আউটপুট:
প্রথম মান "tanvir_dev" চলে যাবে নির্দিষ্ট প্যারামিটার username-এ।

দ্বিতীয় মান "Backend Developer" চলে যাবে role-এ।

এরপরের যতগুলো দক্ষতা পাঠানো হয়েছে ("Python", "FastAPI", "Docker", "PostgreSQL"), সেগুলো প্যাক হয়ে একটি Tuple বানিয়ে skills (*args নাম দিয়ে) এ জমা হবে।

Username: tanvir_dev
Role: Backend Developer
Skills (Tuple): ('Python', 'FastAPI', 'Docker', 'PostgreSQL')


ধাপ ১: সাধারণ সমস্যা (নির্দিষ্ট লিমিট থাকা)।

ধাপ ২: *args-এর মূল কাজ (সবকিছুকে টুপল বানিয়ে ফেলে)।

ধাপ ৩: লুপ চালিয়ে ডেটা প্রসেস করা (যোগফল বের করার উদাহরণ)।

ধাপ ৪: নির্দিষ্ট প্যারামিটার + *args কম্বিনেশন (ইউজার প্রোফাইলের উদাহরণ)।

ধাপ ৫: আনপ্যাকিং (লিস্ট বা টুপলকে ভেঙে ফাংশনে পাঠানো)।





def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total  # যোগফলটি বাইরে পাঠিয়ে দেওয়া

# ফাংশন কল করে রেজাল্ট প্রিন্ট করা
result = add_all(5, 10, 15)
print("Result:", result)


এখানে add_all(5, 10, 15) দিলেন।

*args-এর ভেতরে সেগুলো টুপল হয়ে গেল: (5, 10, 15)।

লুপ চালিয়ে সবগুলোর যোগফল total ভেরিয়েবলে জমলো (30)।

সবশেষে return total দিয়ে সেই রেজাল্টটি বাইরে পাঠিয়ে দেওয়া হলো এবং আমরা print করে তা দেখতে পেলাম।





def calculate(operation, *args):
    # যদি কোনো সংখ্যা বা আর্গুমেন্ট না দেওয়া হয়
    if not args:
        return "No numbers provided!"
    
    # প্রথম সংখ্যা দিয়ে ইনিশিয়ালাইজ করা
    result = args[0]
    
    # যোগ (Addition)
    if operation == "add":
        for num in args[1:]:
            result += num
            
    # বিয়োগ (Subtraction)
    elif operation == "subtract":
        for num in args[1:]:
            result -= num
            
    # গুণ (Multiplication)
    elif operation == "multiply":
        for num in args[1:]:
            result *= num
            
    # ভাগ (Division)
    elif operation == "divide":
        for num in args[1:]:
            if num == 0:
                return "Error: Division by zero is not allowed!"
            result /= num
            
    else:
        return "Invalid operation!"
        
    return result

# ==========================================
# ফাংশনগুলো বিভিন্ন অপারেশন দিয়ে টেস্ট করা যাক:
# ==========================================

print("Addition Result:", calculate("add", 10, 5, 2))          # আউটপুট: 17 (10 + 5 + 2)
print("Subtraction Result:", calculate("subtract", 20, 5, 3))   # আউটপুট: 12 (20 - 5 - 3)
print("Multiplication Result:", calculate("multiply", 2, 3, 4)) # আউটপুট: 24 (2 * 3 * 4)
print("Division Result:", calculate("divide", 100, 2, 5))       # আউটপুট: 10.0 (100 / 2 / 5) 






শুধু যোগ করার জন্য (+) *args
ইউজার যতগুলো সংখ্যাই দিক না কেন, সবগুলোর যোগফল বের করার সবচেয়ে সহজ কোড:

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

# টেস্ট করা যাক:
print("Addition:", add_numbers(5, 10, 15))       # আউটপুট: 30
print("Addition:", add_numbers(2, 4, 6, 8, 10))  # আউটপুট: 30



২. শুধু বিয়োগ করার জন্য (-) *args
প্রথম সংখ্যাটি থেকে পরের সংখ্যাগুলো একে একে বিয়োগ করার কোড:

def sub_numbers(*args):
    if not args:
        return 0
    
    result = args[0]  # প্রথম সংখ্যা দিয়ে শুরু
    for num in args[1:]:
        result -= num
    return result

# টেস্ট করা যাক:
print("Subtraction:", sub_numbers(50, 10, 5))    # আউটপুট: 35 (50 - 10 - 5)



৩. শুধু গুণ করার জন্য (*) *args
যতগুলো সংখ্যা দেওয়া হবে, তাদের সবার গুণফল বের করার কোড:


def multiply_numbers(*args):
    if not args:
        return 1
        
    result = 1  # গুণের ক্ষেত্রে ১ দিয়ে শুরু করতে হয় (০ দিলে সব জিরো হয়ে যাবে)
    for num in args:
        result *= num
    return result

# টেস্ট করা যাক:
print("Multiplication:", multiply_numbers(2, 3, 4))      # আউটপুট: 24 (2 * 3 * 4)
print("Multiplication:", multiply_numbers(5, 5))         # আউটপুট: 25 (5 * 5)




৪. শুধু ভাগ করার জন্য (/) *args
প্রথম সংখ্যাটিকে পরের সংখ্যাগুলো দিয়ে পরপর ভাগ করার কোড (সাথে ০ দিয়ে ভাগের সুরক্ষাও রাখা হয়েছে):

def divide_numbers(*args):
    if not args:
        return "No numbers provided!"
        
    result = args[0]
    for num in args[1:]:
        if num == 0:
            return "Error: Cannot divide by zero!"
        result /= num
    return result

# টেস্ট করা যাক:
print("Division:", divide_numbers(100, 2, 5))    # আউটপুট: 10.0 (100 / 2 = 50, তারপর 50 / 5 = 10.0)






def analyze_scores(*args):
    # যদি কোনো স্কোর দেওয়া না হয়
    if not args:
        return "No scores provided!"
    
    total_exams = len(args)             # মোট পরীক্ষার সংখ্যা
    total_marks = sum(args)             # সব নম্বরের যোগফল
    average_marks = total_marks / total_exams  # গড় নম্বর
    highest_mark = max(args)            # সর্বোচ্চ নম্বর
    lowest_mark = min(args)             # সর্বনিম্ন নম্বর
    
  
    summary = {
        "Total Exams": total_exams,
        "Total Marks": total_marks,
        "Average": round(average_marks, 2), # দশমিকের পর দুই ঘর রাখা
        "Highest": highest_mark,
        "Lowest": lowest_mark
    }
    
    return summary


# একজন ছাত্র ৫টি বিষয়ে আলাদা নম্বর পেয়েছে:
result1 = analyze_scores(85, 90, 78, 92, 88)
print("Student 1 Summary:", result1)

# আরেকজন ছাত্র ৩টি বিষয়ে নম্বর পেয়েছে:
result2 = analyze_scores(70, 65, 95)
print("\nStudent 2 Summary:", result2)


Student 1 Summary: {'Total Exams': 5, 'Total Marks': 433, 'Average': 86.6, 'Highest': 92, 'Lowest': 78}

Student 2 Summary: {'Total Exams': 3, 'Total Marks': 230, 'Average': 76.67, 'Highest': 95, 'Lowest': 65}



এটি কেন "মিডিয়াম" লেভেলের?
পাইথনের বিল্ট-ইন ফাংশনের ব্যবহার: এখানে শুধু লুপ নয়, পাইথনের শক্তিশালী
বিল্ট-ইন ফাংশন যেমন len() (গণনা করতে), sum() (যোগ করতে), max() (বড় মান বের করতে) 
এবং min() (ছোট মান বের করতে) খুব সুন্দরভাবে *args-এর সাথে ব্যবহার করা হয়েছে।

ফ্লেক্সিবিলিটি: ছাত্র ৫টি বিষয়ের পরীক্ষা দিক বা ৩টি বিষয়ের—ফাংশনটি নিজে থেকেই বুঝে নিয়ে নিখুঁত ক্যালকুলেশন করে দিচ্ছে।

প্র্যাকটিক্যাল ডেটা ফরম্যাট: ব্যাকএন্ডে API রেসপন্স পাঠানোর সময় সাধারণত ডেটাগুলো এভাবেই ডিকশনারি বা JSON ফরম্যাটে রিটার্ন করতে হয়।





ইউজার বয়স ভ্যালিডেশন (Age Verification API)
ধরে নিন আপনি একটি ইভেন্টের ব্যাকএন্ড সিস্টেম বানাচ্ছেন, যেখানে এক বা একাধিক ইউজারের বয়স পাঠানো হবে।
চেক করতে হবে যে তাদের মধ্যে কারা প্রাপ্তবয়স্ক (১৮ বা তার বেশি) এবং কারা অপ্রাপ্তবয়স্ক।

এখানে *args-এর মাধ্যমে যত খুশি ইউজারের বয়স পাঠানো যাবে, আর if কন্ডিশন দিয়ে ফিল্টার করা হবে।


def check_event_eligibility(*ages):
    # যদি কোনো বয়স বা ইনপুট না দেওয়া হয়
    if not ages:
        return "No participant ages provided!"
    
    allowed_users = []
    blocked_users = []
    
    # লুপ চালিয়ে প্রতিটি বয়সের ওপর কন্ডিশন চেক করা
    for age in ages:
        if age >= 18:
            allowed_users.append(age)  # প্রাপ্তবয়স্ক হলে অ্যালাউ লিস্টে যাবে
        else:
            blocked_users.append(age)  # ১৮ এর নিচে হলে ব্লক লিস্টে যাবে
            
    # ফাইনাল রিপোর্ট রিটার্ন করা
    return {
        "Allowed Users (18+)": allowed_users,
        "Blocked Users (Under 18)": blocked_users
    }


result = check_event_eligibility(25, 16, 30, 17, 22, 40)
print(result)
