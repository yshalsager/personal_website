+++
title = "كيفية توفير مساحة القرص الصلب عن طريق ميزة CompactOS في ويندوز 10"
date = "2017-03-21"
description = "يحتوي ويندوز 10 على ميزة تسمي CompactOS حيث تقوم بضغط حجم ملفات النظام لتوفير مزيد من مساحة القرص الصلب، إليك كيفية تفعيل هذه الميزة"
categories = ["ويندوز",]
series = ["ويندوز 10"]
tags = ["موقع لغة العصر"]

+++

يحتوي ويندوز 10 على ميزة تسمي CompactOS حيث تقوم بضغط حجم ملفات النظام لتوفير مزيد من مساحة القرص الصلب، إليك كيفية تفعيل هذه الميزة.

هذه الميزة مصممة في الأساس لأجهزة الكمبيوتر التي تحتوي على قرص صلب صغير مثل بعض أجهزة اللاب توب، حيث تشبه هه الميزة إلى حد كبير ضغط نظام NTFS الموجود ضمن خيارات القرص الصلب.

1. قم بفتح موجه الأوامر Command Prompt عن طريق الضغط بزر الماوس الأيمن على زر البداية (أو اضغط على Windows+X) ثم اختر Command Prompt (Admin).

![img](images/1.png)

2. للتحقق من وضع CompactOS الحالي قم بكتابة الأمر:

`Compact.exe /CompactOS:query`

![img](images/2.png)

3. لتفعيل CompactOS قم بكتابة:

`Compact.exe /CompactOS:always`

![img](images/3.png)

لكن عليك الانتباه إلى أن تفعيل الميزة قد يستغرق 20 دقيقة أو أكثر حسب جهازك، وبعد ذلك سيقوم بتوفير حوالي 2.2 جيجا من المساحة.

4. أما لتعطيل الميزة مرة أخرى نفذ هذا الأمر:

`Compact.exe /CompactOS:never`

![img](images/4.png)

---
هذا الموضوع نٌشر باﻷصل على موقع مجلة لغة العصر.

http://aitmag.ahram.org.eg/News/72883.aspx