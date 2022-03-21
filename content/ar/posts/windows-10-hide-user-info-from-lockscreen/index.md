+++
title = "كيفية إخفاء بيانات المستخدم من شاشة تسجيل الدخول في ويندوز 10"
date = "2016-05-22"
description = "إذا كنت تستخدم حساب مايكروسوفت لتسجيل الدخول إلى جهازك فستجد أن الويندوز يقوم بعرض اسمك وبريدك الإلكتروني في شاشة تسجيل الدخول، في درس اليوم سنقوم بمنع عرض هذه البيانات"
categories = ["ويندوز",]
series = ["ويندوز 10"]
tags = ["موقع لغة العصر"]
+++

إذا كنت تستخدم حساب مايكروسوفت لتسجيل الدخول إلى جهازك فستجد أن الويندوز يقوم بعرض اسمك وبريدك الإلكتروني في شاشة تسجيل الدخول، في درس اليوم سنقوم بمنع عرض هذه البيانات.

1- قم بالدخول إلى Local Group Policy Editor.

![1](images/2016-635995286056006319-600.jpg)

2- انتقل إلى المسار Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options/

![2](images/2016-635995286302643900-264.png)

3- اضغط على Interactive logon: Display user information when the session is locked.

![3](images/2016-635995286546005460-600.png)

4- قم بتغييرها إلى الاختيار Do not display user information ثم اضغط OK.

![4](images/2016-635995286620417937-41.png)

5- بعد ذلك افتح الاختيار Interactive logon: Do not display last user name.

![5](images/2016-635995286693582406-358.png)

6- قم بتغييرها إلى الاختيار Disabled ثم اضغط OK.

![6](images/2016-635995286766902876-690.png)

---
هذا الموضوع نٌشر باﻷصل على موقع مجلة لغة العصر.

http://aitmag.ahram.org.eg/News/49747.aspx