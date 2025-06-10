SET PATH=C:\Keil_v5\ARM\ARMCC\Bin;C:\ProgramData\Oracle\Java\javapath;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Program Files\PuTTY\;C:\Program Files (x86)\Windows Live\Shared;C:\Users\proj1_wsn\AppData\Local\Programs\Python\Python312\Scripts\;C:\Users\proj1_wsn\AppData\Local\Programs\Python\Python312\;C:\Users\proj1_wsn\AppData\Local\Programs\Python\Launcher\;C:\Users\proj1_wsn\AppData\Local\Microsoft\WindowsApps;C:\Python34\Scripts;C:\Python34\Scripts
SET ARMCC5_ASMOPT=--diag_suppress=9931
SET ARMCC5_CCOPT=--diag_suppress=9931
SET ARMCC5_LINKOPT=--diag_suppress=9931
SET CPU_TYPE=ATSAMD20J18
SET CPU_VENDOR=Microchip
SET UV2_TARGET=Target 1
SET CPU_CLOCK=0x00B71B00
"C:\Keil_v5\ARM\ARMCC\Bin\ArmCC" --Via ".\objects\2.__i"
"C:\Keil_v5\ARM\ARMCC\Bin\ArmAsm" --Via ".\objects\startup_samd20._ia"
"C:\Keil_v5\ARM\ARMCC\Bin\ArmLink" --Via ".\Objects\tav.lnp"
"C:\Keil_v5\ARM\ARMCC\Bin\fromelf.exe" ".\Objects\tav.axf" --i32combined --output ".\Objects\tav.hex"
