+++
title = "طريقة إضافة خيارات Copy To / Move To إلى القائمة المختصرة في الويندوز"
date = "2015-04-14"
description = "نظام الويندوز كالمحيط العميق الذي كلما تعمقت فيه أكثر اكتشفت أسراره وخفاياه، نقدم لك عزيزي القارئ سرا جديدا من اسرار الويندوز هو كيفية إضافة ميزتي النسخ والقص الى مجلد محدد الى قائمة الزر الأيمن في ويندوز"
categories = ["مهارات رقمية",]
tags = ["موقع لغة العصر"]

+++

نظام الويندوز كالمحيط العميق الذي كلما تعمقت فيه أكثر اكتشفت أسراره وخفاياه، نقدم لك عزيزي القارئ سرا جديدا من اسرار الويندوز هو كيفية إضافة ميزتي "النسخ والقص الى مجلد محدد" الى قائمة الزر الأيمن في ويندوز.



تعتمد هذه الحيلة على تعديل ملفات الريجيسترى الخاصة بالويندوز، كما أنها تعمل على كل إصدارات الويندوز.

## الطريقة اليدوية:


1. قم بفتح محرر الريجيسترى عن طريق RUN (Windows+R) ثم انتقل الى هذا المفتاح


HKEY\_CLASSES\_ROOT\AllFilesystemObjects\shellex\ContextMenuHandlers


2. قم بالضغط على هذا المجلد، من قائمة New اختر Key.



![img](images/1.png)


3. اضغط مرتين على (Default) ثم ادخل القيمة الآتية:


{C2FBB630.2971.11D1.A18C-00C04FD75D13}


4. اضغط موافق (تمت إضافة خيار Copy to).



![img](images/2.png)

5. قم بعمل New Key مرة أخرى ثم قم بإدخال هذه القيمة:


{C2FBB631.2971.11D1.A18C-00C04FD75D13}


6. اضغط مواقف (تمت إضافة خيار Move To).


عند الضغط بزر الفأرة الأيمن على أي ملف أو مجلد ستظهر لك الخيارات الجديدة كما بالصور:



![img](images/3.png)

![img](images/3-2.png)



![img](images/4.png)

![img](images/4-2.png)

## الطريقة الاوتوماتيكية:


قم بتحميل هذا الملف [من هنا](http://cdn5.howtogeek.com/wp-content/uploads/gg/copyto_moveto.zip)، ثم قم بفك الضغط ستجد ملفي ريجسترى، تستطيع تفعيل خيار Copy To أو Move To أو كلاهما.

---
هذا الموضوع نٌشر باﻷصل على موقع مجلة لغة العصر.

http://aitmag.ahram.org.eg/News/9729.aspx