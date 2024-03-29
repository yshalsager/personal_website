+++
title = "طريقة إزالة التطبيقات المدمجة في ويندوز 10 وإعادة تثبيتهم"
date = "2015-08-16"
description = "يحتوي ويندوز 10 على العديد من التطبيقات الموحدة Universal apps مثل البريد والتقويم، ولا توجد طريقة لإلغاء تثبيتهم بشكل طبيعي مثل باقي التطبيقات، في درس اليوم أقدم لك عزيزي القارئ طريقة إزالة التطبيقات المدمجة في ويندوز 10 وإعادة تثبيتهم مرة أخرى."
categories = ["ويندوز",]
series = ["ويندوز 10"]
tags = ["موقع لغة العصر"]
+++

يحتوي ويندوز 10 على العديد من التطبيقات الموحدة Universal apps مثل البريد والتقويم، ولا توجد طريقة لإلغاء تثبيتهم بشكل طبيعي مثل باقي التطبيقات، في درس اليوم أقدم لك عزيزي القارئ طريقة إزالة التطبيقات المدمجة في ويندوز 10 وإعادة تثبيتهم مرة أخرى.

**أولا: إزالة بعض التطبيقات بالطريقة التقليدية:**
تعمل هذه الطريقة على التطبيقات: Get Office, Get Skype, Get Started, Microsoft Solitaire Collection, Money, News, Phone Companion, و Sport.
من قائمة البداية اضغط يزر الفأرة الأيمن على التطبيق الذي تريد إلغاء تثبيته ثم اختر Uninstall.

**ثانيا: إزالة التطبيقات الأخرى باستخدام** **Windows PowerShell:**

1. قم بكتابة PowerShell في البحث ثم اضغط بزر الفأرة الأيمن واختر Run as administrator ثم اضغط Yes.

![](images/2015-635753262652127366-212.png "2")

2. هذه قائمة أوامر لإزالة أي تطبيق من التطبيق الموجودة في ويندوز 10:

|            التطبيق             |                            أمر اﻹزالة                             |
| :----------------------------: | :---------------------------------------------------------------: | --- |
|           3D Builder           |         Get-AppxPackage _3dbuilder_ \| Remove-AppxPackage         |
|        Alarms and Clock        |       Get-AppxPackage _windowsalarms_ \| Remove-AppxPackage       |
|           Calculator           |     Get-AppxPackage _windowscalculator_ \| Remove-AppxPackage     |
|       Calendar and Mail        | Get-AppxPackage _windowscommunicationsapps_ \| Remove-AppxPackage |
|             Camera             |       Get-AppxPackage _windowscamera_ \| Remove-AppxPackage       |
|        Contact Support         |                        غير مسموح بإزالته                         |     |
|            Cortana             |                        غير مسموح بإزالته                         |     |
|           Get Office           |         Get-AppxPackage _officehub_ \| Remove-AppxPackage         |
|           Get Skype            |         Get-AppxPackage _skypeapp_ \| Remove-AppxPackage          |
|          Get Started           |        Get-AppxPackage _getstarted_ \| Remove-AppxPackage         |
|          Groove Music          |         Get-AppxPackage _zunemusic_ \| Remove-AppxPackage         |
|              Maps              |        Get-AppxPackage _windowsmaps_ \| Remove-AppxPackage        |
|         Microsoft Edge         |                        غير مسموح بإزالته                         |     |
| Microsoft Solitaire Collection |    Get-AppxPackage _solitairecollection_ \| Remove-AppxPackage    |
|             Money              |        Get-AppxPackage _bingfinance_ \| Remove-AppxPackage        |
|          Movies & TV           |         Get-AppxPackage _zunevideo_ \| Remove-AppxPackage         |
|              News              |         Get-AppxPackage _bingnews_ \| Remove-AppxPackage          |
|            OneNote             |          Get-AppxPackage _onenote_ \| Remove-AppxPackage          |
|             People             |          Get-AppxPackage _people_ \| Remove-AppxPackage           |
|        Phone Companion         |       Get-AppxPackage _windowsphone_ \| Remove-AppxPackage        |
|             Photos             |          Get-AppxPackage _photos_ \| Remove-AppxPackage           |
|             Store              |       Get-AppxPackage _windowsstore_ \| Remove-AppxPackage        |
|             Sports             |        Get-AppxPackage _bingsports_ \| Remove-AppxPackage         |
|         Voice Recorder         |       Get-AppxPackage _soundrecorder_ \| Remove-AppxPackage       |
|            Weather             |        Get-AppxPackage _bingweather_ \| Remove-AppxPackage        |
|        Windows Feedback        |                        غير مسموح بإزالته                         |     |
|              Xbox              |          Get-AppxPackage _xboxapp_ \| Remove-AppxPackage          |

3. قم بنسخ أي أمر من الأوامر السابقة ثم قم بلصقه في PowerShell واضغط Enter.

![](images/2015-635753262771814866-181.png "3")

**ثانيا: إعادة تثبيت جميع تطبيقات الويندوز مرة أخرى باستخدام** **Windows PowerShell:**

1. قم بكتابة PowerShell في البحث ثم اضغط بزر الفأرة الأيمن واختر Run as administrator ثم اضغط Yes.
2. قم بنسخ هذا الأمر ثم قم بلصقه في PowerShell واضغط Enter.
   `Get-AppxPackage -AllUsers| Foreach {Add-AppxPackage -DisableDevelopmentMode -Register “$($\_.InstallLocation)\AppXManifest.xml”}`

3. سيأخذ تنفيذ الأوامر بعض الوقت للانتهاء من التثبيت.

---

هذا الموضوع نٌشر باﻷصل على موقع مجلة لغة العصر.
