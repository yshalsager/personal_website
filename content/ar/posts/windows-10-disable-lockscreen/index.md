+++
title = "طريقة تعطيل شاشة القفل في ويندوز 10"
date = "2017-07-11"
description = "بعد تحديث الذكرى السنوية لويندوز 10 لم يعد بإمكان المستخدمين تعطيل شاشة القفل عن طريق الرجيستري أو Group Policy، لكن توجد طريقة جديد سنتعرف عليها في هذا الموضوع."
categories = ["ويندوز",]
series = ["ويندوز 10"]
tags = ["موقع لغة العصر"]
+++

بعد تحديث الذكرى السنوية لويندوز 10 لم يعد بإمكان المستخدمين تعطيل شاشة القفل عن طريق الرجيستري أو Group Policy، لكن توجد طريقة جديد سنتعرف عليها في هذا الموضوع.

**كيفية تعطيل شاشة القفل (ماعدا عند الإقلاع):**

كل ما سنقوم بفعله هو منع الويندوز من الوصول إلى تطبيق Microsoft.LockApp، وأبسط طريقة لفعل ذلك دون الدخول في تعقيدات هو عن طريق إعادة تسمية ملفات التطبيق.

1. قم بفتح مستعرض الملفات File Explorer ثم انتقل إلى المسار:

`C:\Windows\SystemApps`

![1](images/1.png)

2. ستجد المجلد Microsoft.LockApp\_cw5n1h2txyewy قم بالضغط بزر الماوس الأسمن عليه ثم اختر Rename من القائمة المختصرة، وغير اسمه إلى

`Microsoft.LockApp\_cw5n1h2txyewy.backup`

![2](images/2.png)

3. وهكذا لن يستطيع الويندوز الوصول لتطبيق شاشة القفل.

- إذا أردت إعادة تفعيل شاشة القفل مرة أخرى، توجه إلى نفس المسار وأعد تسميه المجلد مجددا إلى Microsoft.LockApp\_cw5n1h2txyewy

![3](images/3.png)

**كيفية تعطيل شاشة القفل عند تسجيل الدخول:**

1. قم بفتح مربع Run ثم اكتب netplwiz

2. قم بتحديد الحساب ثم اضغط أزل العلامة من الاختيار Users must enter a user name and password to use this computer واضغط OK.

3. ستظهر لك نافذة تطلب ادخال بينات المستخدم من اسم وكلمة مرور، قم بكتابتهم ثم اضغط OK.

![4](images/4.png)

---
هذا الموضوع نٌشر باﻷصل على موقع مجلة لغة العصر.

http://aitmag.ahram.org.eg/News/72882.aspx