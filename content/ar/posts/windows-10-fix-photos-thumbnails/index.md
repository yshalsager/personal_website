+++
title = "حل مشكلة عدم ظهور مصغرات الصور في ويندوز 10"
date = "2016-01-31"
description = "في بعض الأحيان وخصوصا مع الصور كبيرة الحجم في ويندوز 10 تحدث مشكلة وهي عدم ظهور المصغرات، وظهور أيقونة صورة فقط، في هذا الدرس سنتعرف على طريقة حل هذه المشكلة"
categories = ["ويندوز",]
series = ["ويندوز 10"]
tags = ["موقع لغة العصر"]

+++

في بعض الأحيان وخصوصا مع الصور كبيرة الحجم في ويندوز 10 تحدث مشكلة وهي عدم ظهور المصغرات، وظهور أيقونة صورة فقط، في هذا الدرس سنتعرف على طريقة حل هذه المشكلة.

1- قم بالدخول إلى هذا المسار:
`C:\Users\<your username>\AppData\Local\Microsoft\Windows\Explorer`
مع استبدال <your username> باسم المستخدم الخاص بك.

2- اضغط زر Shift مع الاستمرار ثم اضغط بزر الماوس الأيمن على مجلد Explorer واختر Open command window here.

![1](images/2016-635898534602922229-292.png)

3- سيتم فتح موجة الأوامر في هذا المسار.

![2](images/2016-635898534699486848-948.png)

4- تأكد من أنك في المسار الصحيح ثم اكتب الأمر dir لتظهر لك ملفات المصغرات كما بالصورة.

![3](images/2016-635898534784351392-435.png)

5- قم بفتح مدير المهام Task Manager بالضغط بزر الماوس الأيمن على شريط المهام واختيار Task Manager.

![4](images/2016-635898534923972287-397.png)

6- اضغط بزر الماوس الأيمن على Windows Explorer ثم اختر End task.

![5](images/2016-635898535002440790-244.png)

7- ارجع مرة اخري الي موجه الأوامر ثم اكتب الأمر التالي واضغط Enter:
del iconcache*

![6](images/2016-635898535206646099-664.png)

8- اكتب الأمر dir لتتحقق من مسح ملفات المصغرات، إذا وجدت أي ملفات أغلق جميع التطبيقات المفتوحة بالخلفية ثم أعد الخطوات السابقة.

![7](images/2016-635898535337374937-737.png)

9- اضغط Ctrl+Alt+Del ثم اختر Sign out وأعد تسجيل الدخول مرة أخري.

---
هذا الموضوع نٌشر باﻷصل على موقع مجلة لغة العصر.

http://aitmag.ahram.org.eg/News/42429.aspx