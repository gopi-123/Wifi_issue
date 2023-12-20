# Wifi Adapter Issue solving in ubuntu and Windows  (HP Laptop) -- 
sample testing github

Issue with **Wireleass LAN Adapter -- "Realtek RTL8723BE 802.11 bgn Wi-Fi Adapter"**

 Version: "Realtek **RTL8723BE"** 802.11 bgn Wi-Fi Adapter

 https://www.realtek.com/en/component/zoo/category/rtl8192ee-software

 https://support.hp.com/in-en/drivers/laptops
 
 
Problem:
Cannot see own wireless network but can see others around me

Every other device can detect my wifi but not my laptop. 
Seemingly after last Windows update (though I'm not sure) I cannot see my own wireless network on my home laptop. I can see all the networks of my neighbors, but not my own.

I can see it and connect to my wireless network with my Work laptop. My partner can see it and connect to it with her two laptops and her smartphone.

I checked the **wireless network adapter (Realtek RTL8723AE Wireless LAN 802.11n PCI-E NIC)** 

Problem link:
https://answers.microsoft.com/en-us/windows/forum/all/cannot-see-own-wireless-network-but-can-see-others/ae835a08-59a6-4aaa-830c-87a1dab5761b?page=3

https://askubuntu.com/questions/645220/unable-to-connect-wifi-ubuntu-14-04-lts-hp-pavilion-network-driver-rtl8723be

**Google search : rtl8723be support ubuntu 14.04 download**

https://www.google.de/search?q=rtl8723be+support+ubuntu+14.04+download&sca_esv=591570470&ei=6Ud-ZZSGItCC9u8P-tKJ2Ak&oq=RTL8723BE+support+ubuntu+14.04&gs_lp=Egxnd3Mtd2l6LXNlcnAiHlJUTDg3MjNCRSBzdXBwb3J0IHVidW50dSAxNC4wNCoCCAAyBRAhGKABMgUQIRigAUihgwFQAFjlbnAAeAGQAQCYAYEBoAHxCqoBBDIxLjG4AQPIAQD4AQL4AQHCAgUQABiABMICBhAAGBYYHsICBxAhGKABGAriAwQYACBBiAYB&sclient=gws-wiz-serp

**https://connectwww.com/how-to-solve-realtek-rtl8723be-weak-wifi-signal-problem-in-ubuntu/4625/**

Video Solve (Solve & Fix Realtek RTL8723BE Weak WIFI Signal Problem in Ubuntu): **https://www.youtube.com/watch?v=DPFKYYOlydQ**

https://askubuntu.com/questions/847392/wlan-rtl8723be-frequently-disconnects

**Highest voted answer:**
https://askubuntu.com/questions/635625/how-do-i-get-a-realtek-rtl8723be-wireless-card-to-work?noredirect=1&lq=1



** Solve wifi issues **:

Best thing is to:
 1) To me the answer is get a new wireless card or a **USB wireless connector**.  or **USB Wi-Fi Adapter**  oer **Wireless USB adapter**  ,
  **Required Linux  Kernel version 2.6.18 to approx  4.4.3**

UBUNTU RELEASE	| ARCH	 | KERNEL VERSION
**Ubuntu 14.04 LTS	| 64-bit x86 | 	4.4 (HWE)**
Ubuntu 22.04 LTS	| 64-bit x86	| 6.2 (HWE)

I used it for a new laptop that I installed Linux Mint operating system on. The Wifi card was an Intel 6E AX211 160Mhz. I used the dongle to establish an internet connection as most modern laptops don't have a rj45 socket on them these days. i then could download all the **updates and the latest Linux kernel** and then after a reboot the Wifi was working perfectly. 



 
 3)    example device link which is compatible with Windows, Linux & MAC OS :

Netherlnad link: for support **Windows, Linux , Mac** -- **150 Mbp**s  -- Product TP-Link 150Mbps WiFi USB Adapter, Support System - Windows 11/10/8.1/8/7/XP, Mac OS 10.15 and earlier, Linux (TL-WN725N):

a) https://www.amazon.nl/-/en/TP-Link-150Mbps-Adapter-Support-System/dp/B008IFXQFU/ref=cm_cr_arp_d_product_top?ie=UTF8&th=1
b) 

https://www.amazon.de/-/en/TP-Link-TL-WN823N-300Mbit-installation-compatible/dp/B0088TKTY2/ref=sr_1_3?crid=3RRKYLOJQ7CKF&keywords=USB+Wi-Fi+Adapter+for+linux+and+windows&qid=1702601553&refinements=p_72%3A419117031&rnid=419116031&sprefix=usb+wi-fi+adapter+for+linux+and+windows%2Caps%2C71&sr=8-3

 5) From mediamakrt prdouct: "ASUS USB-N10 NANO"  --compatiblw wiht linux , mac and windows:
    https://www.mediamarkt.nl/nl/product/_asus-usb-n10-nano-1722882.html
    
    
 6)  --updating the driver in device manager --**Intel driver to the Microsoft driver
   Uninstall / reinstall the wi-fi adapter by following this procedure:            
            https://www.drivereasy.com/knowledge/how-to-reinstall-wi-fi-driver-on-windows-10-easily/ 
 
1) **Guru prasad solution:** https://askubuntu.com/questions/721981/how-to-configure-rtl8723be-to-detect-wifi-networks-solved-for-hp-laptop

2) https://l.facebook.com/l.php?u=https%3A%2F%2Fanswers.microsoft.com%2Fen-us%2Fwindows%2Fforum%2Fall%2Fcannot-see-own-wireless-network-but-can-see-others%2Fae835a08-59a6-4aaa-830c-87a1dab5761b%3Fpage%3D5%26fbclid%3DIwAR1zHSgwkGOxL4UZ-dLZSPxb3VpDEQIsMP04ILBJrfzL5c5XCZVuFgJMeXc&h=AT0mCk6nl3Y4SX2D9d82qJ8huTw9ZE_wrepG_zGec5DnrjuaWUwo8PrtO1iK3GTwhM08B8NUe_Bk76FdrISfjeCD_XR-cv02vMImF1gxq1cBAHZFxQRKtgIt7Y1m_lQhShY4Xg

3) https://answers.microsoft.com/en-us/windows/forum/all/cannot-see-own-wireless-network-but-can-see-others/ae835a08-59a6-4aaa-830c-87a1dab5761b?page=3

4) The solution to the first problem is to go to device manager - Network adapters - TP-Link...**Adapter - Properties - Power Management, and turning off the "allow this device to be turned off to save power"**or whatever similar. I have no idea why such a braindead feature is featured on windows, why would I ever want to turn off my little USB internet dongle to save power???
5) The solution to the second problem was drivers. I tried updating my network and product drivers for like 5 times with no effect. The solution apparently was to update some g**eneric Intel drivers that windows automatically found for me.** I had no idea this would work but was pleasantly surprised, the product works great now!

3) I turned on 802-11d and "lo
4) I turned on 802.11d in the network adapter.
5) I had this same issue and wanted to share my experience with a Lenovo IdeaPad Yoga 13 model 20175 and the Realtek Semiconductor Corp. RTL8723AU 802.11n WLAN Adapter. After trying all of the troubleshooting steps in this thread, I can confirm this issue to be driver related as installing Linux on the same hardware does allow finding and connecting to my home network.
6) I had exactly the same problem.It was solved when I changed the settings of the router. Specifically, I tried different "Wireless Modes" (f.x. 802.11b or 802.11b+g+n and so on) until I found one all my computers could see.Hope it helps.
7)  Easier fix.  Reboot router!
8)  Just resolved it. Just go to your router and at your 2.4 connection set the wi-fi mode to  **Mixed 802.11 b/n/g**
9)  I got thinking about this logically and my system said that the Wifi Adapter was working correctly and there were no updates for the drivers. So I thought to myself what controls this? 
This is the Realtek PCle GbE Family Controller.  I got mine to work by opening **Device Manager > Realtek PCle GbE Family Controller > Properties > Advanced > Power Saving Mode** ..  The Power Saving Mode was showing as Enabled... as soon as I made the value to **Disabled**(i.e., not in power saving mode) my wifi internet connection icon changed and it was online once more... So, it was the **Realtek PCle GbE Family Controller** that was stopping the Ralink 802.11n Wireless Lan Card being seen because of the power saving option in the controller... As such it could not connect to the internet.
10) Hi, I had exactly the same problem. I solved it by going in to my router (login as admin) and changed the wireless mode from 802.11ax to to another one such as **802.11b+g+n**
11) Below you can find out how I solved this issue for my laptop:
          1. Log in to your router - you can do this w**ith the login details shown on your router (username and password).** On Google, you can look for the ways of logging in to your router, it depends on the brand of the router.
          
          2. Select Network (on the top navigation bar).
          
          3. Go to Wireless 2.4 GHz and/or 5 GHz (on the left navigation), then you will see the option to change the channel. (For the 2.4 GHz band channels 1, 6, and 11 are recommended since they are the only non-overlapping channels). In my case, I have only "Wireless 2.4 GHz" option available, **so I just changed the channel to "11"**.
          
          4. Save this change and hopefully, your issue will also be solved.

12) After sleeping on the same issue last night I tried again this morning and resolved it in a couple of minutes (this is on Win 11 pc but should be fine on 10)   I created a hotspot to my phone
         **Searched for Realtek 8812AU Wireless driver** and found this link....https://driverpack.io/en/devices/wifi/realtek/realtek-8812au-wireless-lan-802-11ac-usb-nic?os=windows-10-x64
         
      **I downloaded the zip file. unzipped it**.
         
         **Went to device manager - clicked on Network Adaptors** Right clicked on Realtek 8812AU, Selected 'Browse my computer for drivers', selected the folder I had just unzipped to.
         
         After install my home network re-appeared and the problem was solved.
         
         Cheers all. 
         
         PS I had ordered this https://www.amazon.co.uk/gp/product/B01NBMJGA9/ref=ppx_od_dt_b_asin_title_s00?ie=UTF8&psc=1 and might still keep it as I've just changed over service providers and the Eero router they provide should in theory be a lot faster with this card but we will see.


13) . I have an **Intel Dual Band Wireless-AC 7260 modem.**

I had to “Roll Back the Driver” then it could see and connect to my home network as it did before.. Crazy part is, the newest driver is from 2017 the rolled back one is 2015..


14) https://answers.microsoft.com/en-us/windows/forum/all/hp-laptop-after-a-clean-installation-of-windows-10/bf7c539f-f031-465f-b67d-c7eefb06fb34

first of all go to Settings> Network and Internet**>WI-FI, click on Manage known networks on the side, select and then remove all network profiles present, then check if the network is detected and reconnect by re-entering the wi-fi password.**

Do you use the 2.4 or 5 GHz network? Does the problem occur for both networks? Do the 2 networks have the same SSID or different SSIDs?

Login to the router via another device, go to the wireless settings page and change the radio channel manually. **For the 2.4 GHz band choose channels 1, 6 or 11.** For the 5 GHz band, set channels 48, 64 or 136 .Save your changes, restart the router and try again.

14) Switched from the **Intel driver to the Microsoft driver and lo,** the digital divide parted and I now feast on delicious wifi. Thank you, kind internet stranger.
    --updating the driver in device manager
    
    1) Uninstall / reinstall the wi-fi adapter by following this procedure:
            
            https://www.drivereasy.com/knowledge/how-to-reinstall-wi-fi-driver-on-windows-10-easily/ 
            
            NOTE:This is a non Microsoft website. The page appears to provide accurate and secure information. Beware of ads on the site that may advertise products often classified as PUPs (potentially unwanted products).
            
            Ignore advertising tips, do not use third-party driver installation programs.
            
            2) Try changing the driver by looking for it on your computer:
            
            1) Go to Device Manager> Network Adapters, right click on your network adapter> Update Driver.
            
            2) Select "Search my computer for drivers"
            
            3) Select "Choose from a list of drivers available on your computer"
            
            4) Windows will propose 2 or more compatible drivers for the network adapter in use, select a driver other than the one currently in use> Next. The driver will be installed automatically. Restart the PC.
            
            Otherwise, download and reinstall the latest driver version available from the pc manufacturer's website
            

15) **My network adapter are [Intel(R) Dual Band Wireless-AC 3160].

**Following is my operation steps:****

       **(1) Run Device Manager;
       
       (2) Select Network adapters and then [Intel(R) Dual Band Wireless-AC 3160]
       
       (3) Right click and select update driver
       
       (4) Select [Browse my computer for drivers]
       
       (5) Click [Let me pick from a list of available drivers on my computer]
       
       (6) Select [[Intel(R) Dual Band Wireless-AC 3160] (Microsoft)]
       
       (7) Click Next**




#####
https://www.amazon.nl/-/en/TP-LINK-MU-MIMO-Wireless-Supports-T3U/dp/B07M69276N/ref=cm_cr_arp_d_product_top?ie=UTF8&th=1

Instructions for Linux / Debian
###
Execute the command "lsusb" in a shell (command line) or "sudo dmesg":lsusb
# On a Raspberry PI with OpenWRT installed (OpenWrt 22.03.5, r20134-5f15225c1e) I was shown the following on the shell:Bus 001 Device 014: ID 2357:0109 Realtek 802.11n NIC
# It is important to name the ID "2357:

0109" because it is a Realtek chip RTL8192EU which is installed in the USB WLAN adapter TP-Link TL-WN823N!

#Auf a "normal" PC (with Intel I5 processor) I was shown the following line (the name of the ID "2357:0109" is also important here, because it is then a Realtek chip RTL8192EU)
Bus 001 Device 006: ID 2357:0109 TP-Link TL-WN823N v2/v3 [Realtek RTL8192EU]

###

# Tested under:# Debian 12# Linux kernel in version 6.1.0-12-amd64

# Note: it may also work with earlier Debian versions,
but I haven't checked!
###

If it works for you (which may well be the case in a few weeks or months if there are newer Linux kernels), then you don't need to do anything else and can ignore this part of the guide!

Note2: you may need to install the net-tools package to make ifconfig available on your system: sudo apt update & sudo apt install net-tools -y

# to The best way to install the external driver is to follow the instructions below, which are basically an excerpt of the file README.md (see below)
# Now run the following commands on the "normal" PC:
sudo apt update
sudo apt install linux-headers-generic build-essential dkms git net-tools

# Download
the source code git clone https://github.com/clnhub/rtl8192eu-linux

# Change
to directory cd rtl8192eu-linux# read the readme file if there are problems or if you are using another Linux distribution
less README.md

# Perform automated installation (execute the following command from the directory rtl8192eu-linux

, if necessary switch to the directory, if not already done as described above!)
./install_wifi.sh

#Zum uninstall run the following file:
./uninstall_wifi.sh

###

Short conclusion:
With a little effort (see below) anyone who knows something about Linux and can open a shell can put the USB WLAN adapter into operation.
I didn't test the adapter on Windows because it's used on Linux (OpenWrt and Rapsberry PI). Here I assume that it can be used on Windows 10 without any problems.

Link
https://www.amazon.nl/-/en/TP-LINK-MU-MIMO-Wireless-Supports-T3U/dp/B07M69276N/ref=cm_cr_arp_d_product_top?ie=UTF8&th=1


# Important note: If the OpenWRT does not have a connection to the Internet, then you should connect the Raspberry PI to the router via a network cable so that a connection to the Internet can be established and the software packages can be downloaded!

# openwrt installation for Raspberry PI2b V1.1 and higher (possibly also suitable for PI1, but not tested by me so far)
# Log in via the web interface of the OpenWrt/PI system and navigate to the menu item Software: System -> Software
# There the button "Update lists..." Click
# then under "Filter:" enter and install the following package names individually:
kmod-usb2 rtl8192eu-firmware
,
kmod-rtl8xxxu
, net-tools (this is optional and serves to detect if the WLAN adapter has been correctly detected by the system. This can also be omitted if necessary, but then the command "ifconfig" will not work!)

# or alternatively run the following command from a console:
opkg update
opkg install kmod-usb2 rtl8192eu-firmware kmod-rtl8xxxu net-tools

After that, a corresponding "radio" device should be found under "Network" -> "Wireless" (reboot the PI if necessary).
Alternatively, you can run the ip a or ifconfig -a command on the console. A device with wlanX should then appear there (X should then have a number of 0 - ... e.g. wlan0)

The connection under a Linux PC seems to be stable and correspondingly fast.
In a quick test for a router in the next room, the ping statistics for 101 packets showed the following result (signal strength to the router was about 80-94% depending on how the USB adapter was aligned):
101 packets transmitted, 101 received, 0% packet loss, time 100134ms
rtt min/avg/max/mdev = 1,965/3,088/11,641/1,424 ms

With these settings, I had been able topter on Linux. A long-term test will show how well it performs and if necessary I will note this again in the review.


******


**https://community.tp-link.com/en/home/forum/topic/248212**

Solution: 
**https://community.tp-link.com/en/home/forum/topic/208022**


Model: Adapter  
Hardware Version:
Firmware Version:
I Bought TP-Link AC1300 Mini-Wireless MU-MIMO USB Adapter Archer T3U.

 

I know there is no official support for Ubuntu 20.04 LTS. Can any body help me to make it work with my Ubuntu 20.04

Solution Explaination:

I had the same problem, check out Jags solution on Ask Ubuntu under Proper Way of Installing Wifi Drivers.

For convenience, I'll repost it here, because I can't seem to attach the link, but I take no credit for the following solution or the github repo. Make sure the adapter is unplugged, and tether to a phone or connect to ethernet. In terminal, do:

------ 


git clone https://github.com/cilynx/rtl88x2bu.git

cd rtl88x2bu

VER=$(sed -n 's/\PACKAGE_VERSION="\(.*\)"/\1/p' dkms.conf)

sudo rsync -rvhP ./ /usr/src/rtl88x2bu-${VER}

sudo dkms add -m rtl88x2bu -v ${VER}

sudo dkms build -m rtl88x2bu -v ${VER}

sudo dkms install -m rtl88x2bu -v ${VER}

sudo modprobe 88x2bu

----------
 

Hope this helped and cheers,

Monkey D. Luffy



**Bluetooth issue:**
https://askubuntu.com/questions/474839/the-bluetooth-is-disabled-on-ubuntu-14-04
