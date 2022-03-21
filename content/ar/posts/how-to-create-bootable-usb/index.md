+++
title = "كيفية عمل فلاشه للإقلاع منها لأي نظام تشغيل"
date = "2015-05-17"
description = "هل لديك نسخة ويندوز بصيغة ISO ولا تستطيع حرقها على أسطوانة، نقدم لك عزيزي القارئ طريقة وضع نسخة من أي نظام تشغيل على الفلاشه والتثبيت منها مباشرة."
categories = ["مهارات رقمية",]
tags = ["موقع لغة العصر"]

+++

هل لديك نسخة ويندوز بصيغة ISO ولا تستطيع حرقها على أسطوانة، نقدم لك عزيزي القارئ طريقة وضع نسخة من أي نظام تشغيل على الفلاشه والتثبيت منها مباشرة.
إذا كنت تريد حرق نسخة من ويندوز 7 يمكنك استخدام أداة Windows 7 USB/DVD download tool المجانية، من انتاج مايكروسوفت، بعد تثبيت الأداة قم بفتحها بصلاحيات المدير Run as administrator ثم اتبع الخطوات.

1. قم بتحميل أداة Rufus [من موقعها الرسمي من هنا](http://rufus.akeo.ie/).
2. قم بفتح الأداة بصلاحيات المدير Run as administrator.
3. قم بالضغط على Device ثم اختر الفلاشه التي تريد وضع الويندوز عليها.

![1](images/2015-635674731358872206-887.jpg)

4. اختر “MBR partition scheme for BIOS or UEFI computers “للإقلاع من ال BIOS.
أو أختر “GPT partition scheme for UEFI computer ” للإقلاع من ال UEFI.

![2](images/2015-635674731502465956-246.jpg)

5. اختر نظام الملفات NTFS إذا كان حجم ملف ال ISO أكبر من 4 جيجا.

![3](images/2015-635674731627309706-730.jpg)

6. اترك قيمة cluster size كما هي.
7. قم بضبط إعدادات الفورمات كما الآتي:
اختر “Quick Format “.
اختر “Create extended label and icon files “.
اختر “Create a bootable disk using “.

![4](images/2015-635674731768403456-840.jpg)

8. اضغط علي علامة القرص بجانب “Create a bootable disk using “ثم اختر ملف ال ISO.

![5](thumbnail-2015-635674731908872206-887.jpg)

9. تأكد من الإعدادات التي قمت بعملها ثم اضغط زر Start لبدأ حرق النسخة.

![6](images/2015-635674732058403456-840.jpg)


قائمة أنظمة التشغيل التي تدعمها أداة Rufus:
* Arch Linux
* Archbang
* BartPE/pebuilder
* CentOS
* Damn Small Linux
* Fedora
* FreeDOS
* Gentoo
* GParted
* gNewSense
* Hiren’s Boot CD
* LiveXP
* Knoppix
* KolibriOS
* Kubuntu
* Linux Mint
* NT Password Registry Editor
* OpenSUSE
* Parted Magic
* Partition Wizard
* ReactOS
* rEFInd
* Slackware
* Tails
* Trinity Rescue Kit
* Ubuntu
* Ultimate Boot CD
* Windows XP (SP2+)
* Windows Server 2003 R2
* Windows Vista
* Windows 7
* Windows 8
* Windows 8.1

---
هذا الموضوع نٌشر باﻷصل على موقع مجلة لغة العصر.

http://aitmag.ahram.org.eg/News/15640.aspx