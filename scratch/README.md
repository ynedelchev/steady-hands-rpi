Steady hands game written in Scratch 2
=========================================

<!--Please use markdown-toc -i README.md to update the table of contents -->
<!-- -->
**Table of Contents**  *generated with [Markdown-TOC](https://www.npmjs.com/package/markdown-toc#install)*

<!-- toc -->

- [Quick Start](#quick-start)
- [Detailed Instructions](#detailed-instructions)
  * [Overview of the game](#overview-of-the-game)
  * [Numbering Schemes](#numbering-schemes)
  * [Hardware setup](#hardware-setup)
  * [Steps to generate and load the project](#steps-to-generate-and-load-the-project)
  * [Adjusting the Keyboard](#adjusting-the-keyboard)

<!-- tocstop -->

Quick Start
------------
 * Biuld the project by cd-ing to this directory and running: 
   ````
     ./build-project.sh 
   ````
   that would create a file named `steady-hands.sb2`

 * Open the file `steady-hands.sb2` as Scratch 2 project
 * Do the wiring appropriately. Instructions to come later
 * Press the flag icon to run the program

Detailed Instructions
---------------------

### Overview of the game

The steady hands game is a very old one. The main idea is that you should 
try to pass a ring wire all the way through a bent wire without touching the 
ring wire to the bent wire. Each touch gives you a failure point. 


### Numbering Schemes

Raspberry Pi is using two numbering schemes for its General Ports for Input and Output (GPIO).

 - BCM Numbering Schemes
 - Physical Numbering Scheme 
 
In our program we woud use the BCM Numbering scheme. In the image below these are the numbers 
prefixed by `GPIO` in the renctangles: 

![RPI Numbering Schemes](images/0-numbering-scheme.png "Raspberry Pi Numbering Schemes")

### Hardware setup 

Let's do the hardware setup as shown below. We would use 

 - Port GPIO14 for the beginning (A)
 - Port GPIO18 for the bent wire (C)
 - Port GPIO23 for the ending    (B)
 - Port Ground for the ring      (D)
 
![Hardware Wiring](images/0-hardware-setup.png "Steady Hands Game Hardware Wiring")

We would use

### Steps to generate and load the project

 1. Open a console terminal window:
   ![Open Termina](images/1-open-terminal.png "Open Terminal")
   
 2. Clone the project from [https://github.com/ynedelchev/steady-hands-rpi/](https://github.com/ynedelchev/steady-hands-rpi/) using the command: 
   ```
   git clone https://github.com/ynedelchev/steady-hands-rpi/
   ```
   ![Clone Project](images/2-git-clone.png "Clone Project from GitHub")
   
   ![Cloned Project](images/3-git-cloned.png "After cloning")

 3. Go to the `steady-hands-rpi/scratch` folder
   ```
   cd steady-hands-rpi/scratch
   ```
   ![Go to Scratch Subfolder](images/4-cd-steady-hands-rpi-scratch.png "Go to Scratch subfolder")
  
 4. Scratch projects are zip packages that contain source code + resources, but are not effectively stored in source control. 
   That is why we have stored an unzipped version of the project file. To be able to load it via Scratch, we need to zip it 
   back. 
   Use the command: 
   ```
   ./build-project.sh
   ```
   ![Build The Project](images/5-build-project.png "Zip back the project files")
   
 
   As a result a file `steady-hands.sb2` will appear
 
   ![Resulting Project file](images/6-build-project.png "The project file after building it")
    
 5. Start Scratch 2 from Raspberry Pi Menu - Programming - Scratch 2
 
   ![Start Scratch 2](images/7-start-scratch.png "Start the Development Environment")
    
 6. Lets add the module that allows us to work with GPIO. Go to `More Blocks` and then `Add an Extension`.
   
   ![Add GPIO Extension](images/8-more-blocks-add-extensin.png "More Blocks - Add Extension")
   
 7. Select the iconf for the PI GPIO extension and press OK. 
   
   ![Select PI GPIO Extension](images/9-add-pi-gpio-module.png "PI GPIO Extension")
   
   As a result the additional block for working with GPIO will appear in the `More Blocks` section.
   
   ![Blocks for GPIO](images/10-gpio-added.png "Blocks for working with GPIO")
   
 8. Load the project by selecting File - Load Project.
   
   ![Load Project](images/11-load-project.png "Loading the project")
   
 9. Select the project file that you have generated in step 4.
   
   ![Select Project file](images/12-select-the-project.png "Selecting the project file")
   
 10. You will be asked, whether you want to replace the existing project. Answer `OK` .
   
   ![Replace the existing project](images/13-ask-override.png "Replace the existing project")
   
 11. Review the loaded program
   
   ![Program](images/14-loaded.png "Program")
   
 12. Run the program by pressing the flag icon. 
   
   ![Run it](images/15-run-it.png "Run the program")
   
### Adjusting the Keyboard

 1. On the task bar on the top, click with the right mouse button to open a context menu and then select 
   `Add / Remove Panel Items`.
   
   ![Add / Remove Panel Items](images/k1-add-remove-panel-items.png "Adjusting Panel Items")
   
 2. In the dialog, scroll down and select `Keyboard Layout Handler`, then click `Preferences`:
   
   ![Preferences](images/k2-keyboard-layout-handler.png "Preferences")
   
 3. Adjust all the settings as per your preferences. In the below screenshot there are some sample settings: 
   
   ![Keyboard settings](images/k3-settings.png "Keyboard settings")
   
   The keyboard indicator will appear in the task panel on the top:
   
   ![Keyboard indicator](images/k4-switch.png "Switching keyboard layouts")

 4. Since there seem to be some sort of bug in raspberry pi and these settings
    are not survive a restart, here is what you need to do to make them 
    permanent. 

    a. Open the following file for editing (use escalated privileges or edit as root):
       ```
         sudo vim /etc/default/keyboard
       ```
       Instead of `vim`, you can also use `nano` or any other text editor as per your preference.

     b. Edit the file untill it looks like this:
       ```
       XKBMODEL="pc105"
       XKBLAYOUT="us,bg"
       XKBVARIANT=",phonetic"
       XKBOPTIONS="grp:lalt_lshift_toggle,compose:ralt,terminate:ctrl_alt_bksp"
       BACKSPACE="guess"
       ```
       Please note that valued `us` and `bg` for the `XKBLAYOUT` are the keyboard layouts for American English and Bulgarian. 

       Then the `,phonetic` in `XKBVARIANT`, represents the sub-variants in a comma separated list, 
       where we have an empty string for the `us` variant (which probably means the 
       default variant) and we have `phonetic` for the Bulgarian variant. 

       For Bulgarian, you could also use `bas_phonetic` which would bring you the 
       new phonetic invented in Bulgarian Academic of Science but not widespread 
       (versus `phonetic` that gives you the traditional phonetic layout - widespread).

       If you use empty string for the Bulgarian phonetic, then you would get the 
       typewriter standard also known as BDS (Bulgarian Darzhaven Standard).

       The value `grp:lalt_lshift_toggle` in `XKBOPTIONS` allows you to switch between
       American English and Bulgarian using the `Letf Alt` + `Left Shift` combination.

     c. Restart 
       ```
        sudo reboot
       ```
        
