---
title: "How to build a Project Treble GSI ROM from source?"
description: "Project Treble is a re-architecture of Android by Google that created a split between the OS framework and device-specific low-level software. This new change allow users to flash Generic System Images on their devices, and developers to build one image for a large variety of devices. Here's how to build it!"
tags:
  - Android
  - Development
date: 2018-06-09
---

**Note:** *This guide is super old and some steps might be changed, please refer to the community edited guide for a more recent guide.*

---

As you read this guide now I'll assume you already have a previous knowledge about How to build android from source, so I won't cover some points with too many basic details.
So, let's start:

What you’ll need:

- A treble enabled device, basically all devices that come with Android 8.1 out of box support it.
- A relatively recent 64-bit computer (Linux, OS X, or Windows) with a reasonable amount of RAM and about 100 GB of free storage (more if you enable ccache or build for multiple devices). The less RAM you have, the longer the build will take (aim for 8 GB or more). Using SSDs results in considerably faster build times than traditional hard drives.
- A USB cable compatible with your device
- A decent internet connection & reliable electricity
- Some familiarity with basic Android operation and terminology. It would help if you’ve installed custom ROMs on other devices and are familiar with recovery. It may also be useful to know some basic command line concepts such as cd for “change directory”, the concept of directory hierarchies, that in Linux they are separated by /. etc.

**Summary**

1. Installing SDK
2. Installing build packages
3. Install the repo command
4. Configuring git
5. Turning on caching to speed up build
6. Building using phhusson's script
7. Building using dakkar's script
8. Building using the manual way

## 1. Installing SDK

If you haven’t previously installed adb and fastboot, you can [download them from Google](https://dl.google.com/android/repository/platform-tools-latest-linux.zip). Extract it using:

```bash
unzip platform-tools-latest-linux.zip -d ~
```

Now we have to add adb and fastboot to our path. Open ~/.profile and add the following:

```bash
# add Android SDK platform tools to path
if [ -d "$HOME/platform-tools" ] ; then
    PATH="$HOME/platform-tools:$PATH"
fi
```

Then, run this to update your environment.

```bash
source ~/.profile
```

## 2. Installing build packages

Several packages are needed to build Android. You can install these using your distribution’s package manager.
You’ll need:

```bash
bc bison build-essential curl flex g++-multilib gcc-multilib git gnupg gperf imagemagick lib32ncurses5-dev
lib32readline-gplv2-dev lib32z1-dev libesd0-dev liblz4-tool libncurses5-dev libsdl1.2-dev libwxgtk3.0-dev
libxml2 libxml2-utils lzop pngcrush schedtool squashfs-tools xsltproc zip zlib1g-dev openjdk-8-jdk
```

## 3. Installing the repo command

Enter the following to download the repo binary and make it executable (runnable):

```bash
mkdir -p ~/bin
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo
```

Put the ~/bin directory in your path of execution

In recent versions of Ubuntu, ~/bin should already be in your PATH. You can check this by opening ~/.profile with a text editor and verifying the following code exists (add it if it is missing):

```bash
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi
```

Then, use this to update your environment.

```bash
source ~/.profile
```

## 4. Configuring git

You’ll need to set up git identity in order to sync the source, run these commands:

```bash
git config --global user.name "your username"
git config --global user.email yourmail@example.com
```

## 5. Turning on caching to speed up build

You can speed up subsequent builds by running:

```bash
export USE_CCACHE=1
export CCACHE_COMPRESS=1
```

And adding that line to your `~/.bashrc` file. Then, specify the maximum amount of disk space you want the cache to use by typing this from the top of your Android tree:

```bash
prebuilts/misc/linux-x86/ccache/ccache -M 50G
```

Where 50G corresponds to 50GB of cache. This needs to be run once. Anywhere from 25GB-100GB will result in very noticeably increased build speeds (for instance, a typical 1hr build time can be reduced to 20min). If you’re only building for one device, 25GB-50GB is fine. If you plan to build for several devices that do not share the same kernel source, aim for 75GB-100GB. This space will be permanently occupied on your drive, so take this into consideration. See more information about ccache on [Google’s Android build environment initialization page](https://source.android.com/source/initializing.html#setting-up-ccache).

## **6. Building using phhusson's script**

We can't deny that [@phhusson](https://forum.xda-developers.com/m/1915408/) has made amazing works and countless contributions to Project Treble ROMs development apart from his [experimentations](https://github.com/phhusson/treble_experimentations/) is a build script which make build a GSI super simple job.
By default, it supports building LineageOS - RR - Carbon.
1- Open your terminal and run:

```bash
git clone https://github.com/phhusson/treble_experimentations
```

2- To clone and build enter the following command and replace "romname" with lineage|rr|carbon

```bash
mkdir romname; cd romname
bash ../treble_experimentations/build-rom.sh android-8.1 romname
```

3- The script will automatically initialize the repository, sync the source, apply patches and start building.

## 7. Building using dakkar's script

dakkar's script is another treble building script, originally made by [@Dakkar](https://forum.xda-developers.com/m/260854/) and improved by contributors on [treble experimentations](https://github.com/phhusson/treble_experimentations/) repo. It's customizable, easy to understand and can build almost all [ROMs](https://github.com/phhusson/treble_experimentations/blob/master/build-dakkar.sh#L29) with simple [edits](https://github.com/phhusson/treble_experimentations/commit/a5e1b285cb3a3c0430a85b2ad8db16cbee3328f5).

1- Open your terminal and run:

```bash
git clone https://github.com/phhusson/treble_experimentations
```

2- To start the process:

```bash
bash ../treble_experimentations/build-dakkar.sh romname variant
```

> Variants are dash-joined combinations of (in order):
> * processor type
> * "arm" for ARM 32 bit
> * "arm64" for ARM 64 bit
> * A or A/B partition layout ("aonly" or "ab")
> * GApps selection
> * "vanilla" to not include GApps
> * "gapps" to include opengapps
> * "go" to include gapps go
> * SU selection ("su" or "nosu")
> for example:
> * arm-aonly-vanilla-nosu
> * arm64-ab-gapps-su
>
> Click to collapse

**Note:** check patches when you use these auto scripts, if some patch is broken you'll have build errors ![:p](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 8. Building using the manual way

In simple steps:

1. Repo init the rom you want to build GSI for.

```bash
mkdir ~/rom &&  cd ~/rom
repo init -u https://github.com/LineageOS/android.git -b lineage-15.1
```

2. Add phh repos to your local_manifest

```bash
git clone https://github.com/phhusson/treble_manifest .repo/local_manifests -b android-8.1
```

After git clone you need to remove replace.xml if you're building any rom expect aosp.

> phhusson said:
>
> The replace.xml is meant only for AOSP, if you build a custom ROM, remove it, but don't forget to cherry-pick the patches.

3. Sync the source

```bash
repo sync -c -j4 --force-sync --no-tags --no-clone-bundle
```

4. Modify the source to fix issues in other devices using one of these methods:
- Apply [phh patches](https://github.com/phhusson/treble_patches/tree/android-8.1/patches):

```bash
git clone https://github.com/phhusson/treble_patches -b android-8.1
```

Then apply each path in its project

```bash
patch -p1 < patch
```

- Or cherry-pick changes by phhusson from here, remember to choose the latest branch
[platform_build](https://github.com/phhusson/platform_build/) - [platform_external_selinux](https://github.com/phhusson/platform_external_selinux) - [platform_frameworks_av](https://github.com/phhusson/platform_frameworks_av) - [platform_frameworks_base](https://github.com/phhusson/platform_frameworks_base) - [platform_frameworks_native](https://github.com/phhusson/platform_frameworks_native) - [platform_frameworks_opt_telephony](https://github.com/phhusson/platform_frameworks_opt_telephony) - [platform_system_bt](https://github.com/phhusson/platform_system_bt) - [platform_system_core](https://github.com/phhusson/platform_system_core) - [platform_system_libvintf](https://github.com/phhusson/platform_system_libvintf) - [platform_system_vold](https://github.com/phhusson/platform_system_vold)

```bash
git fetch repo branch && git cherry-pick commit
```

5. Go to the phh device repo and edit the .mk for your ROM (example lineage.mk)
6. Lunch the [build varaint](https://github.com/phhusson/treble_experimentations/blob/master/build.sh#L38) you want (ex. treble_arm64_avN-userdebug) and start the build

```bash
. build/envsetup.sh
lunch treble_arm64_avN-userdebug
WITHOUT_CHECK_API=true make -j8 systemimage
```

7. If you want to compress the system image after build finishes, go to out/target/product/phh_*/ folder and run

```bash
xz -c system.img > system.img.xz
```

**Credits:**
- [@phhusson](https://forum.xda-developers.com/m/1915408/) for all his contributions, without his efforts this can't be possible.
- [@Dakkar](https://forum.xda-developers.com/m/260854/) for his build script
- [@fAIyaZ](https://forum.xda-developers.com/m/6817926/) for helping me build my first GSI
- [@sooti](https://forum.xda-developers.com/m/4460995/) for his simplified instruction on phh-treble telegram.
- [@lineageos](https://forum.xda-developers.com/m/7967832/) guys for their wiki



---

**Note:** This article was posted originally on XDA Developers forums, you can find it [here](https://forum.xda-developers.com/t/guide-how-to-build-a-project-treble-gsi-rom-from-source-31-08.3801803/).
