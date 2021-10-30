---
title: "DualBootPatcher Ultimate Guide: How to use, build and add new devices!"
description: "DualBootPatcher is an open-source app that allows multiple ROMs to be installed on a single Android device. In this article I will cover everything about it, for regular and super users as well."
tags:
  - Android
  - Development
date: 2017-08-26
---

## Introduction & How to use DualBootPatcher?

### What is DualBootPatcher?

> DualBootPatcher is an open-source app that allows multiple ROMs to be installed on a single Android device. It does its best to work with existing code and does not require explicit support from ROMs. There are currently 270+ supported devices and their variations.
> It's originally developed by the amazing developer @chenxiaolong with help of many [contributors](https://github.com/chenxiaolong/DualBootPatcher/graphs/contributors)

### What does this app do ?
**It patches...**

- Custom kernels for dual boot support
- ROMs so that they can be installed as secondary
- Google Apps packages for AOSP-based ROMs
- SuperSU so that it can be used in the secondary ROM

### Where can i find it?

- [Website](https://dbp.noobdev.io/)
- [XDA Main Thread](http://forum.xda-developers.com/showthread.php?t=2447534)
- [Github](https://github.com/chenxiaolong/DualBootPatcher)

### What's supported ?

> Except Toaster and Alarm clocks pretty much everything is supported.

### How to use the App?

- Download, install and open the app.
- Swipe to the right to open the menu. Click "ROMS". Now if this is the first time you use it, it will ask you if you want to set kernel. Do so!
- After it has finished go to ROM Settings (primary ROM 3 dot menu) and select Update Ramdisk. It will update it and will ask you to reboot. Press Reboot Now, or Reboot later.
- Now Download any ROM you like and open the app again and open the menu and open Patch Zip File from the menu. Ensure that your Device is set to (yourdevicename) and under Partition configuration select secondary/dataslot (will install 2nd ROM in /system) or data slot.
- Click continue and select where to save the patched file.
- You should see the file is being put in "Queue". Just click the confirm button to the upper right.
  **Note:** If you want to go back, just swipe the ROM in queue to right and start over.
- The app will patch the zip. When done, go back to "ROMs".
- Click "Flash zip files" (the big pink button on the lower right). Click the pink plus button to add your previously patched zip file.
- Locate the file you have patched in step 7. Unless you have changed the name there, it should be something like ROM_name_partition_config_ID.zip (like RR-N-v5.8.3-20170707-cheeseburger-Unofficial_dual.zip).
- Click on that file and choose "Keep location". Now confirm the flash with the button on the upper right side.
  **Note:** You can also install the patched zip files in recovery.
- It will now open the terminal and begin flashing the file. This requires some patience. After it has flashed the file you'll see success message in green.
- Now click back and you should see your newly installed ROM along with the Primary ROM.
  **Note:** You can find more options by clicking on the three buttons on each ROM.
- Now reboot and wait till finishing 2nd ROM first boot. install DualBootPatcher apk so you can easily switch ROMs, there is another way to change ROMs: flash DualBootUtilities.zip and switch ROM manually.

#### Using Bootui:

- Open app then select settings and press install (update) bootui. then Swipe to the right to open the menu. Click "ROMS" again and open secondary ROM Settings) and select Update Ramdisk, Now you can change ROMs simply using boot ui (something like grub bootloader but it works like twrp).

### Partitions Configurations:

The patcher offers several locations for installing ROMs:

- Primary: This is normally used for installing a zip to the primary ROM. It is not required, but is strongly recommended because it has code to prevent the zip from inadvertently affecting other ROMs.
- Dual: Dual/Secondary is the first multiboot installation location. It installs to the system partition. This is a good spot for installing a second ROM because it doesn't take any space away from the internal storage.
- Multi-slots: There are 3 multislots: multi-slot-1, multi-slot-2, multi-slot-3. These install to the cache partition. This is specifically for devices, like the Galaxy S4, that have a massive cache partition.
- Data-slots: There can be an unlimited number of data slots. These install to the data partition and eat up space on the internal storage. This is useful for devices where the system partition is nearly full and the cache partition is tiny. These slots are named "data-slot-[id]", where "id" is something you provide in the app.
- Extsd-slots: There can be an unlimited number of extsd slots. These install to the external SD card, which is useful as it keeps the ROMs off of the internal storage. Note that the ROM's data files are still stored on the data partition.

### Apps and Data sharing:

> DualBootPatcher very recently got support for sharing apps and their data across ROMs. Maybe sharing is somewhat of a misleading term. The feature actually makes Android load the shared apps and data from a centralized location, /data/multiboot/_appsharing. So you're not sharing apps from one ROM to another per se. The ROMs are just loading the apps from one shared location. Let me make this clearer with an analogy.
>
> Think of the people in a company office as ROMs. You want to share with your coworkers some documents (apps). Instead of telling them to come over to your desk to see those documents (sharing apps from one ROM to another), everyone goes to the conference room to look at the documents together (loading apps from a shared location). That's how app and data sharing is implemented.

To use app sharing, follow these steps **in every ROM that you want to use app sharing**: (doesn't work with JB ROMs)

- Install the app you want to share
- Open DualBootPatcher and go to "App Sharing" in the navigation drawer
- Enable individual app sharing
- Tap "Manage shared applications" and enable APK/data sharing for the app
- Reboot

> When you uninstall an app that's shared, it simply become unshared for the current ROM. That way, other ROMs are not affected. To continue the analogy above, if you quit your job, you won't shred the documents that everybody else was looking at.
>
> If you unshare an app's data, it will go back to using the data it had before it was shared. In other words, you leave the conference room and go back to work on your own documents at your desk.

### FAQ:

**How to boot to another ROM ?**

This is simple ... There is no reboot to primary, secondary or whatever. So all you have to do is:

1) Go to ROMs section of the App.
2) Click on the ROM you want to boot to. You should see "Switching ROM" message. After few seconds, you should see a report message saying that "ROM successfully switched".
3) Now just do a normal reboot of your device. See the magic! It should boot to the ROM you have switched on step 2.
   **Note**: You can find more options by selecting the three buttons on each ROMs (like creating reboot widgets for directly rebooting to specific rom).
   You also need to install the App to all of the ROMs you install. Otherwise, you want be able to boot to other ROMs!

**Wipe /cache, /data, /system, or dalvik-cache?**
The easiest way is to do it from the app while booted in another ROM. Just go to "Roms" in the navigation drawer, tap the 3 dots options menu for the ROM you want to wipe, and tap "Wipe ROM".
**Update the primary ROM?**
Patch the zip for primary and flash it. The "primary" installation target is designed so that other ROMs won't be affected when you want to flash something for the primary ROM.
**Update a non-primary ROM?**
Patch and flash the zip exactly like how you did it the first time.
**Flash a mod or custom kernel for the primary ROM?**
Patch it for primary before flashing. If the zip does not wipe /cache, it is also safe to flash it directly.
**Flash a mod or custom kernel for a non-primary ROM?**
Just patch and flash it :)

---

## How to build DualBootPatcher from source?

When you deeply exploring DualBootPatcher [repository](https://github.com/chenxiaolong/DualBootPatcher/blob/master/docs/) you'll find all information and guides you need but for some people instructions isn't clear enough, so let me explain it here ![:D](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
\- You'll need linux, whichever distribution you use. but i'm sure building works on [Debian-Ubuntu-Fedora-Arch] and all its derivations.

### A) Prerequisites

\- You'll need these packages whatever version you want to build:

- Android NDK

Currently NDK r15 is required to build, you can get it [here](https://dl.google.com/android/repository/android-ndk-r15-linux-x86_64.zip)
Download, Extract and rename it to "android-ndk"

```bash
wget https://dl.google.com/android/repository/android-ndk-r15-linux-x86_64.zip && unzip android-ndk-r15-linux-x86_64.zip && mv android-ndk-r15 android-ndk
```

And then export android ndk:

```bash
echo "export ANDROID_NDK=$(pwd)/android-ndk" >> ~/.bashrc
echo "export ANDROID_NDK_HOME=$(pwd)/android-ndk" >> ~/.bashrc
```

- cmake

DBP needs cmake 3.7.2 or higher. you need to [download it here](https://cmake.org/files/v3.7/cmake-3.7.2.tar.gz)
Downloading & Extract command:

```bash
wget https://cmake.org/files/v3.7/cmake-3.7.2.tar.gz && tar xzf cmake-3.7.2.tar.gz
```

extract to folder and run the following commands in cmake folder



```bash
sed -i 's|cmake_options="-DCMAKE_BOOTSTRAP=1"|cmake_options="-DCMAKE_BOOTSTRAP=1 -DCMAKE_USE_OPENSSL=ON"|' bootstrap
./bootstrap
make
sudo make install
```

- OpenSSL

I'm have made a successful build using openssl-1.1.0c, [download from here](https://www.openssl.org/source/openssl-1.1.0c.tar.gz) and extract.

```bash
wget https://www.openssl.org/source/openssl-1.1.0c.tar.gz && tar xzf openssl-1.1.0c.tar.gz
```

open openssl-1.1.0c folder and install it

```bash
./config shared --prefix=/usr/local/ssl --openssldir=/usr/local/ssl
make
sudo make install
echo 'PATH=${PATH}:/usr/local/ssl' >> ~/.bashrc
```

- gtest

Install on Ubuntu / Debian:

```bash
sudo apt-get install libgtest-dev
```

On Fedora:

```bash
sudo dnf install gtest-devel
```

On Archlinux:

```bash
sudo pacman -S gtest
```

- yaml-cpp

Install on Ubuntu / Debian using

```bash
sudo apt-get install libyaml-cpp-dev
```

On Fedora

```bash
sudo dnf install yaml-cpp-devel
```

On Archlinux:

```bash
sudo pacman -S yaml-cpp
```

Other General packages that must be installed: [Skip this if you have android build environment]
Ubuntu / Debian:

```bash
sudo apt-get install ccache libboost-dev libssl-dev openssl python-minimal build-essential libfontconfig1 findutils git make libprocps-dev unzip zip gcc-multilib g++-multilib lib32ncurses5-dev transifex-client gnupg mesa-common-dev libglu1-mesa-dev
```

Fedora:

```bash
sudo dnf install ccache findutils gcc-c++ git make procps-ng unzip zip gnupg ncurses-compat-libs transifex-client openssl-devel
```

Archlinux:

```
sudo pacman -S ccache boost openssl lib32-openssl findutils git make procps-ng unzip zip gnupg gcc-multilib ncurses
```



```
sudo pacaur -S transifex-client ncurses5-compat-libs lib32-ncurseslib32-ncurses5-compat-libs
```


\- For building the android app you need:

- Android SDK

You need to install SDK using android studio (build-tools 25.0.3, platforms android-25, platform-tools and tools)
or install from terminal:

```bash
mkdir -p android-sdk && cd android-sdk
wget -q https://dl.google.com/android/repository/platform-tools_r25.0.3-linux.zip && unzip -qq platform-tools_r25.0.3-linux.zip
wget -q https://dl.google.com/android/repository/build-tools_r25.0.3-linux.zip && unzip -qq build-tools_r25.0.3-linux.zip
wget -q https://dl.google.com/android/repository/tools_r25.2.3-linux.zip && unzip -qq tools_r25.2.3-linux.zip
```

Then Export it:

```bash
echo "export ANDROID_HOME=$(pwd)" >> ~/.bashrc
echo "export PATH=${PATH}:${ANDROID_HOME}/tools" >> ~/.bashrc
```

- JDK 1.8

Ubuntu / Debian:

```bash
sudo apt-get install openjdk-8-jdk openjdk-8-jdk-headless
```

Fedora:

```bash
sudo dnf install java-1.8.0-openjdk-devel java-1.8.0-openjdk-headless
```

Archlinux:

```bash
sudo pacman -S jdk8-openjdk
```

Other packages:
Ubuntu / Debian:

```bash
sudo apt-get install lib32stdc++-6-dev
```

Fedora:

```bash
sudo dnf install glibc.i686 libstdc++.i686
```

Archlinux:

```bash
sudo pacman -S glibc libstdc++5 lib32-libstdc++5
```

And for linux version you need:

- qt5

it must be 5.3 or higher
Ubuntu / Debian:

```bash
sudo apt-get install qttools5-dev-tools libqt5core5a
```

Fedora:

```bash
sudo dnf install qt5-qtbase-devel
```

Archlinux:

```bash
sudo pacman -S qt5-base
```

Other packages:
Ubuntu / Debian:

```bash
sudo apt-get install libarchive-dev liblz4-tool liblzma-dev lz4-dev zlib1g-dev lib32z-dev
```

Fedora:

```bash
sudo dnf install libarchive-devel lz4-devel xz-devel
```

Archlinux:

```bash
sudo pacman -S libarchive lz4 xz lib32-xz lzip
```

\- Some final touches:
Enable cache:

```bash
echo "export USE_CCACHE=1" >> ~/.bashrc
```

Reload bash environment:

```bash
source ~/.bashrc
```

\- Cloning the source:

```bash
git clone --recursive https://github.com/chenxiaolong/DualBootPatcher.git
```

### B) Building Android App

- Open DualBootPatcher folder and make new folder "build" and open it.

```bash
mkdir build && cd build/
```

- Now Build the app:

```bash
cmake .. -DMBP_BUILD_TARGET=android -DMBP_BUILD_TYPE=debug
make
cpack -G TXZ
make apk
```

- And you'll find built apk in `DualBootPatcher/Android_GUI/build/outputs/apk/Android_GUI-debug.apk`

### C) Building Utilities Zip

Utilities Zip is AROMA based zip which enable you to switch ROMs form TWRP or wipe ROM when something went wrong.
\- In build folder run these commands:

```bash
make android-system_armeabi-v7a
make -C data/devices
./utilities/create.sh
```

You'll find built utilities.zip in DualBootPatcher/build/utilities/DualBootUtilities-9.2.0.zip

### **D) Building Linux **App

- In build folder run these commands:

```bash
cmake .. -DMBP_BUILD_TARGET=desktop -DMBP_PORTABLE=ON
make
cpack -G TXZ
```

or to pack it to zip file:

```bash
cpack -G ZIP
```

---

## How to build DualBootPatcher using docker images?

**What is [docker](https://www.docker.com/what-docker)?** [in case you don't know it [:confused:]

> Docker is the world’s leading software container platform. Developers use Docker to eliminate “works on my machine” problems when collaborating on code with co-workers. Operators use Docker to run and manage apps side-by-side in isolated containers to get better compute density. Enterprises use Docker to build agile software delivery pipelines to ship new features faster, more securely and with confidence for both Linux, Windows Server, and Linux-on-mainframe apps.

Firstly, make sure you have docker installed, if not [install it](https://docs.docker.com/engine/installation/)
From here you should choose a method you'll follow, Building docker images manually or use pre-built docker images.

### A) Building docker images manually:

[@chenxiaolong](https://forum.xda-developers.com/m/4277844/) has made docker image configuration files [here](https://github.com/chenxiaolong/DualBootPatcher/tree/master/docker)
all you need to do after sync the repo like part 1 is entering the following commands in DualBootPatcher directory:

```bash
./docker/generate.sh
./docker/build.sh
```

> Note that building the docker images will take a long time and consume a lot of bandwidth--multiple gigabytes at the very least. It will download all the dependencies for building DualBootPatcher for all supported targets.

### B) Using ready-made docker images:

I have made docker images and uploaded them to [docker hub](https://hub.docker.com/r/yshalsager/dualbootpatcher/)
to download "pull" it enter these commands:

```bash
docker pull yshalsager/dualbootpatcher:9.3.0-4-base
docker pull yshalsager/dualbootpatcher:9.3.0-4-android
docker pull yshalsager/dualbootpatcher:9.3.0-4-linux
```



### C) Building DualBootPatcher using docker:

\- To enter docker container and build DualBootPatcher make folder "builder" in DualBootPatcher directory.

```bash
cd DualBootPatcher && mkdir -p builder
```

\- Then run this to enter android build container

```bash
docker run --rm -it -e USER_ID=$(id -u) -e GROUP_ID=$(id -g) -v "$(pwd):/builder/DualBootPatcher:rw,z" -v "${HOME}/.android:/builder/.android:rw,z" -v "${HOME}/.ccache:/builder/.ccache:rw,z" -v "${HOME}/.gradle:/builder/.gradle:rw,z" yshalsager/dualbootpatcher:9.3.0-4-android bash
```

\- After this you'll continue like normal building:

```bash
cd DualBootPatcher/builder && cmake .. -DMBP_BUILD_TARGET=android -DMBP_BUILD_TYPE=debug && make -j16 && rm -rf assets && cpack && make apk -j16
make android-system_armeabi-v7a -j16 && make -C data/devices -j16
```

\- Now exit from container and enter linux build one:

```bash
docker run --rm -it -e USER_ID=$(id -u) -e GROUP_ID=$(id -g) -v "$(pwd):/builder/DualBootPatcher:rw,z" -v "${HOME}/.android:/builder/.android:rw,z" -v "${HOME}/.ccache:/builder/.ccache:rw,z" -v "${HOME}/.gradle:/builder/.gradle:rw,z" yshalsager/dualbootpatcher:9.3.0-4-linux bash
```

\- Build utilities ZIP:

```bash
cd DualBootPatcher/builder && ./utilities/create.sh
```

\- And build linux app

```bash
cmake .. -DMBP_BUILD_TARGET=desktop -DMBP_PORTABLE=ON && make -j16 && cpack
```

\- You'll find output files in your local "builder" folder like normal build.

---

## How to build DualBootPatcher using TravisCI?

[Travis CI](http://travis-ci.org/) is free open-source continues integration service, which simply take your project from GitHub and test / build it for you !
it's amazing solution if you don't have time/free space/mind lol :cyclops: to test your code.
\- you'll need to signup Travis account, go [here](https://travis-ci.org/) and press signup, enter your GitHub account details then approve Travis needed permissions and done. ![:D](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
\- Now Fork [DualBootPatcher repository](https://github.com/chenxiaolong/DualBootPatcher) to your account and create .travis.yml file in project root.
\- Copy [my Travis configuration](https://github.com/yshalsager/DualBootPatcher/blob/travis-docker/.travis.yml) to your .travis.yml

```yaml
sudo: required

services:
  - docker

before_install:
  # Clone DualBootPatcher Repository
  - git clone --recursive https://github.com/yshalsager/DualBootPatcher -b master DualBootPatcher/
  # Pull docker images
  - docker pull yshalsager/dualbootpatcher:9.3.0-4-base
  - docker pull yshalsager/dualbootpatcher:9.3.0-4-android
  - docker pull yshalsager/dualbootpatcher:9.3.0-4-linux
script:
  # Make work directories 
  - mkdir $HOME/.android
  - mkdir -p ${TRAVIS_BUILD_DIR}/DualBootPatcher/builder/ && cd ${TRAVIS_BUILD_DIR}/DualBootPatcher/
  # Build APK
  - |
    docker run --rm -i -e USER_ID=$(id -u) -e GROUP_ID=$(id -g) -v "$(pwd):/builder/DualBootPatcher:rw,z" -v "${HOME}/.android:/builder/.android:rw,z" yshalsager/dualbootpatcher:9.3.0-4-android bash << EOF
    cd DualBootPatcher/builder && cmake .. -DMBP_BUILD_TARGET=android -DMBP_BUILD_TYPE=debug && make -j16 && rm -rf assets && cpack && make apk -j16
    make android-system_armeabi-v7a -j16 && make -C data/devices -j16
    exit
    EOF
  - |
    docker run --rm -i -e USER_ID=$(id -u) -e GROUP_ID=$(id -g) -v "$(pwd):/builder/DualBootPatcher:rw,z" -v "${HOME}/.android:/builder/.android:rw,z" yshalsager/dualbootpatcher:9.3.0-4-linux bash << EOF
    # Build Utilities Zip
    cd ~/DualBootPatcher/builder && ./utilities/create.sh
    # Build Linux
    cmake .. -DMBP_BUILD_TARGET=desktop -DMBP_PORTABLE=ON && make -j16 && cpack
    exit
    EOF
after_success:
  - export TRAVIS_CURRENT_DATE=$(date +"%d%m%y-%Hh%Mm")
  # Check output & md5sum
  - ls -l ${TRAVIS_BUILD_DIR}/DualBootPatcher/Android_GUI/build/outputs/apk/debug/Android_GUI-debug.apk
  - md5sum ${TRAVIS_BUILD_DIR}/DualBootPatcher/Android_GUI/build/outputs/apk/debug/Android_GUI-debug.apk
  - ls -l ${TRAVIS_BUILD_DIR}/DualBootPatcher/builder/utilities/DualBootUtilities-9.3.0.zip
  - md5sum ${TRAVIS_BUILD_DIR}/DualBootPatcher/builder/utilities/DualBootUtilities-9.3.0.zip
  - ls -l ${TRAVIS_BUILD_DIR}/DualBootPatcher/builder/DualBootPatcher-9.3.0-Linux.zip
  - md5sum ${TRAVIS_BUILD_DIR}/DualBootPatcher/builder/DualBootPatcher-9.3.0-Linux.zip
  # Upload to transfer.sh
  - cd ${TRAVIS_BUILD_DIR}/DualBootPatcher/Android_GUI/build/outputs/apk/debug/ &&  curl --upload-file ./Android_GUI-debug.apk https://transfer.sh/Android_GUI-debug-${TRAVIS_CURRENT_DATE}.apk
  - cd ${TRAVIS_BUILD_DIR}//DualBootPatcher/builder/utilities/ && curl --upload-file ./DualBootUtilities-9.3.0.zip https://transfer.sh/DualBootUtilities-9.3.0-${TRAVIS_CURRENT_DATE}.zip
  - cd ${TRAVIS_BUILD_DIR}/DualBootPatcher/builder/ && curl --upload-file ./DualBootPatcher-9.3.0-Linux.zip https://transfer.sh/DualBootPatcher-9.3.0-${TRAVIS_CURRENT_DATE}-Linux.zip
```

\- Edit [line 8](https://github.com/yshalsager/DualBootPatcher/blob/travis-docker/.travis.yml#L8) with your Repository and branch you want to build.

```yaml
  - git clone --recursive https://github.com/yshalsager/DualBootPatcher -b master DualBootPatcher/
```

\- This simple TravisCI configuration builds both of apk and utilities.zip and deploy them to transfer.sh.
\- Now open Travis and add your DualBootPatcher fork to projects and start building.
\- You'll find built apk md5 and links from line at the end Travis log
\- Build takes about 25 mins.
\- When you add new commits to repository Travis will always build new apk for you!
\- If you want to change something in configuration, always check its syntax to make sure it's valid YAML using [this site](http://yamllint.com/).

---

## How to add new Devices to DualBootPatcher?

To add your/new device to DualBootPatcher you need to get some information first then add it to DualBootPatcher devices:
\- Flash [GetLogs-20161128-1.zip](https://dbp.noobdev.io/misc/getlogs/GetLogs-20161128-1.zip) using recovery [TWRP highly recommended]
\- Copy /sdcard/logs/[Date&Time].tar to PC, extract it and let's start.
\- This is new device template:

```yaml
- name: (Device Name)
  id: (device id)
  codenames:
    - (device codename1)
    - (device codename2)
    - (device codename3)
  architecture: (device architecture)

  block_devs:
    base_dirs:
      - (/dev/block/bootdevice/by-name)
    system:
      - (/dev/block/bootdevice/by-name/system)
    cache:
      - (/dev/block/bootdevice/by-name/cache)
    data:
      - (/dev/block/bootdevice/by-name/userdata)
    boot:
      - (/dev/block/bootdevice/by-name/boot)
    recovery:
      - (/dev/block/bootdevice/recovery)
    extra:
      - (/dev/block/bootdevice/modem)

  boot_ui:
    supported: true
    flags:
      - (TW_HAS_DOWNLOAD_MODE)
    graphics_backends:
      - fbdev
    brightness_path: (/sys/class/leds/lcd-backlight/brightness)
    max_brightness: (255)
    default_brightness: (162)
    pixel_format: (RGBX_8888)
    theme: portrait_hdpi
```

\- You'll edit all values between brackets.
\- open logs/system/build.prop, you'll find:
**ro.product.model=** is your (Device Name)
**ro.product.name=** and **ro.product.device=** is your (device id) and (device codename1), if you know more names for your device add it in (device codename2) / (device codename3)
**ro.product.cpu.abi=** is your (device architecture)
\- open logs/recovery/recovery.fstab, you'll find main device mount points, copy each mount point to it name
\- open logs/recovery/recovery.log, you'll find **TW_BRIGHTNESS_PATH :=** /sys/class/leds/lcd-backlight/brightness this is your (brightness_path)
I:Got **max brightness** 255 is (max_brightness)
setting GGL_**PIXEL_FORMAT**_RGBA_8888 is (pixel_format)
\- Note: you can get these info from BoradConfig.mk in your device twrp tree.
\- Now read "Partition Logs:" in recovery.log
it'll tell us second mount point, as example /system | **/dev/block/mmcblk0p41**
so you should add it like

```yaml
    system:
      - /dev/block/bootdevice/by-name/system
      - /dev/block/mmcblk0p41
```

and so on with other partitions.
\- Checking more mounts: (not necessary but i recommend it)
open `logs/listings/dev_full` and scroll down to `/dev/block/platform/soc.0` you'll find another main mount point which contain by-name and by-num folders like `/dev/block/platform/soc.0/f9824900.sdhci`
from `/dev/block/platform/soc.0/f9824900.sdhci/by-name` list copy each partition mount point to your device
\- Now we're done, you should have something like

```yaml
- name: Xiaomi Mi4S
  id: aqua
  codenames:
    - aqua
  architecture: arm64-v8a

  block_devs:
    base_dirs:
      - /dev/block/bootdevice/by-name
      - /dev/block/platform/soc.0/f9824900.sdhci/by-name
    system:
      - /dev/block/bootdevice/by-name/system
      - /dev/block/platform/soc.0/f9824900.sdhci/by-name/system
      - /dev/block/mmcblk0p41
    cache:
      - /dev/block/bootdevice/by-name/cache
      - /dev/block/platform/soc.0/f9824900.sdhci/by-name/cache
      - /dev/block/mmcblk0p42
    data:
      - /dev/block/bootdevice/by-name/userdata
      - /dev/block/platform/soc.0/f9824900.sdhci/by-name/userdata
      - /dev/block/mmcblk0p44
    boot:
      - /dev/block/bootdevice/by-name/boot
      - /dev/block/platform/soc.0/f9824900.sdhci/by-name/boot
      - /dev/block/mmcblk0p37
    recovery:
      - /dev/block/bootdevice/by-name/recovery
      - /dev/block/platform/soc.0/f9824900.sdhci/by-name/recovery
      - /dev/block/mmcblk0p38

  boot_ui:
    supported: true
    graphics_backends:
      - fbdev
    flags:
      - TW_QCOM_RTC_FIX
    pixel_format: RGBX_8888
    brightness_path: /sys/class/leds/lcd-backlight/brightness
    max_brightness: 255
    default_brightness: 162
    theme: portrait_hdpi
```

\- Open DualBootPatcher/data/devices/(your device manufacturer).yml and add your device codes. then Check your code syntax [here](http://yamllint.com/) if everything is right, make commit to add your device to your repository.
\- Build apk using any method explained above to test it.

---

## How to submit new Devices to official DualBootPatcher support?

Once you checked everything is working, it's time to contribute to DualBootPatcher and add your device to official devices:
\- First, Check you made all needed changes to add your device without problems, again check for YAML syntax because if it's wrong build won't work.
\- Open [DualBootPatcher Repository](https://github.com/chenxiaolong/DualBootPatcher), press New pull request button.
\- Press compare across forks and change the head fork to your username/DualBootPatcher
\- Give a name and a description to your pull request, some thing like: "Add (Device Name) support" or "data: Add (device name)
\- Now click the "Create pull request" green button
\- Wait for your changes to be verified and merged to the project, the developer received your code and he will review, try and add it to the source code. You will be notified when your code merged.

---

**Note:** This article was posted originally on XDA Developers forums, you can find it [here](https://forum.xda-developers.com/t/guide-dualbootpatcher-use-build-from-source-using-docker-travis-and-add-new-devices.3663076/).
