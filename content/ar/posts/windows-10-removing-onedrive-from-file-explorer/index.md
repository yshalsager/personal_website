+++
title = "تعلم ويندوز 10.. كيفية إزالة OneDrive من مدير الملفات"
date = "2015-10-18"
description = "تحدثنا في الموضوع السابق عن طريقة إزالة تثبيت خدمة OneDrive من ويندوز 10، واستكمالا للدرس السابق سنتعلم في درس اليوم طريقة إزالة القسم الخاص ب OneDrive من مدير الملفات File Explorer باستخدام حيل الرجيستري"
categories = ["ويندوز",]
series = ["ويندوز 10"]
tags = ["موقع لغة العصر"]
+++

تحدثنا في الموضوع السابق عن طريقة إزالة تثبيت خدمة OneDrive من ويندوز 10، واستكمالا للدرس السابق سنتعلم في درس اليوم طريقة إزالة القسم الخاص ب OneDrive من مدير الملفات File Explorer باستخدام حيل الرجيستري.

1. اضغط على WinKey+R لفتح مربع Run.

![1](images/2015-635807957963580996-358.jpg)

2. قم بكتابة regedit، سيفتح محرر الرجيستري كما بالصورة:

![2](images/2015-635807958093736413-373.png)

3. من قائمة Edit قم باختيار Find ثم اكتب المسار التالي:
4. HKEY_CLASSES_ROOT\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}

![3](images/2015-635807959038730365-873.png)

4. على الجانب الأيسر ستجد مفتاح DWORD اسمه System.IsPinnedToSpaceTree، قيمته الافتراضية هي 1، لإزالة OneDrive من مدير الملفات سنغير هذه القيمة إلى 0.

5. اضغط مرتين بزر الفأرة الأيسر على المفتاح وقم بتغيير القيمة كما بالصورة:

![4](images/2015-635807959428102873-810.png)

6. اضغط Ok ثم اخرج من المحرر.

تأكد من إغلاق مدير الملفات ثم قم بفتحه لتجد التعديلات التي قمنا بها قد تمت ولم تعد هناك أيقونة OneDrive على الجانب الأيسر مع باقي المجلدات كما بالصورة:

-   قبل التعديلات:

![5](images/2015-635807960317784679-778.png)

-   بعد التعديلات:

---

هذا الموضوع نٌشر باﻷصل على موقع مجلة لغة العصر.

http://aitmag.ahram.org.eg/News/34139.aspx
