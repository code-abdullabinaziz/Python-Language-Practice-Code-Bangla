প্যাইথনে ফাংশন বা def নামকরণের জন্য বিশ্বজুড়ে গ্রহণযোগ্য এবং অফিসিয়াল স্ট্যান্ডার্ড হলো PEP 8 Guidelines (Python Enhancement Proposal 8)।



1. ক্যাসিং স্টাইল (Naming Style):

Snake Case (স্নেক কেস): পাইথনে ফাংশনের নাম সবসময় ছোট হাতের অক্ষর (lowercase) দিয়ে লিখতে হয়।

Word Separator: একাধিক শব্দ থাকলে তাদের মাঝে আন্ডারস্কোর (_) ব্যবহার করতে হবে।


# ✅ সঠিক (Recommended)
def calculate_total_price():
    pass

# ❌ ভুল (CamelCase বা PascalCase ব্যবহার করা যাবে না)
def calculateTotalPrice():
    pass




2. নামের ভাষা ও ক্যারেক্টার (Allowed Characters):

বর্ণমালার ব্যবহার: শুধুমাত্র a-z, 0-9 এবং আন্ডারস্কোর (_) ব্যবহার করা যাবে।

সংখ্যার নিয়ম: নাম কখনো সংখ্যা (Digit) দিয়ে শুরু হতে পারবে না।



3. গ্রামাটিক্যাল ও মিনিংফুল নামকরণ (Action-Oriented Verbs):

Verb (ক্রিয়াপদ) দিয়ে শুরু: ফাংশন যেহেতু কোনো কাজ সম্পন্ন করে, তাই নাম সবসময় Verb বা কাজের নাম দিয়ে শুরু হওয়া উচিত।

স্পষ্টতা (Clarity over Brevity): ছোট নাম দেওয়ার চেয়ে স্পষ্ট নাম দেওয়া উত্তম।



4. বিশেষ পাইথন ফাংশন ও আন্ডারস্কোর (_) কনভেনশন:

পাইথনে ফাংশনের শুরুতে বা শেষে আন্ডারস্কোর ব্যবহারের মাধ্যমে গুরুত্বপূর্ণ অর্থ প্রকাশ পায়:


A. Single Leading Underscore (_function_name)
অর্থ: এটি নির্দেশ করে যে ফাংশনটি Internal / Private।

ব্যবহার: সাধারণত কোনো মডিউল বা ক্লাসের ভেতরে নিজস্ব ব্যবহারের জন্য রাখা হয়। from module import * করলে এই ফাংশনটি ইম্পোর্ট হয় না।


def _internal_helper():
    pass


B. Single Trailing Underscore (function_name_)
অর্থ: পাইথনের সংরক্ষিত শব্দ (Reserved Keywords/Built-in names) এর সাথে নামের সংঘাত এড়াতে শেষে আন্ডারস্কোর দেওয়া হয়।

# class, print, list এগুলো রিজার্ভড কিউওয়ার্ড
def filter_by_class_(class_name):
    pass


C. Double Leading Underscore (__function_name)
অর্থ: এটি ক্লাসের মেথডে Name Mangling সক্রিয় করে (অ্যাক্সিডেন্টালি মেথড ওভাররাইড হওয়া ঠেকাতে)

class Account:
    def __calculate_tax(self):
        pass


D. Double Leading & Trailing Underscore (__init__, __str__)
অর্থ: এগুলোকে Dunder Methods বা Magic Methods বলা হয়।

বিশেষ নিয়ম: পাইথনের নিজস্ব সিস্টেম বা বিল্ট-ইন ফ্রেমওয়ার্ক ছাড়া কখনো নিজের সাধারণ ফাংশনে এভাবে নাম দেওয়া উচিত নয়।





5. বুলিয়ান ফাংশন (Boolean Functions):

যেসব ফাংশন শুধুমাত্র True বা False রিটার্ন করে, সেগুলোর নাম প্রশ্নবোধক শব্দ দিয়ে শুরু করা প্রফেশনাল প্র্যাকটিস:

is_

has_

can_

should_


# ✅ চমৎকার প্র্যাকটিস
def is_authenticated(user):
    return True

def has_permission(user, role):
    return True


