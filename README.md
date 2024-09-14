[![Build](https://github.com/d33p0st/test-ransomware/actions/workflows/Build.yml/badge.svg)](https://github.com/d33p0st/test-ransomware/actions/workflows/Build.yml)
[![Downloads](https://static.pepy.tech/badge/test-ransomware)](https://pepy.tech/project/test-ransomware)

# Overview

I've tried searching ransomwares for testing in macos but most of them turned out to be shady. This one is different. I created it on my own and it replicates basic ransomware behaviour. The user has full control over which `directories` and which `file-types` to target.

After significant thinking about interruption during runtime of the ransomware and assessing the irreversible damages, I have added a few failsafes which might come in handy. One of them being `The files being encrypted multiple times due to starting and stopping of the ransomware`. In cases like these, the multiple encrypted files can also be recovered, which makes it significantly better than any other test ransomware I found online.

> Note: As I mentioned earlier, this is made for `macOS` only as I have used `Applescript` and other macOS dependent features to make it replicate ransomware behaviour.

> However, If you like it and want me to create one for your prefered operating system, create an issue [here](https://github.com/d33p0st/test-ransomware) and I'd be happy to help. Do star the repo!

## Table of Contents

* [Working](#working)
* [Instruction of Usage](#instruction-of-usage)
* [Detailed Features](#detailed-features)
* [Precautions](#precautions)
* [Issues](#issues)
* [Pull Requests](#pull-requests)
* [DISCLAIMER](#disclaimer)

> Please Read all Disclaimer and Precautions before use.

## Working

```console
,_________________,       Monitors        ,____________,
| Kill Protection |-------->------>-------| Ransomware |
|     Program     |-------->------>-------|  Program   |
'-----------------'   Restarts if killed  '-----,------'
                                                |
                                                |
                    ,---------------------------'
                    | - For All Targeted Directories
                    | - Encrypts Targeted File Types
                    |
    ,--------,  ,---'----,      ,--------,
    |  Dir1  |  |  Dir2  | .... |  Dir n |
    '---,----'  '-,------'      '---,----'
        |         |                 |
,-------',  ,-----'--,        ,-----'--,
| File 1 |  | File 2 |  ..... | File n |
'--------'  '--------'        '--------'
```

## Instruction of Usage

* `Installation`

    ```bash
    pip install test-ransomware
    ```

* `Usage`

    ```bash
    $ rw --help
    Test Ransomware v0.1.0
    author: Soumyo Deep Gupta (d33p0st, d33pster)
    description: Dummy Ransomware to test Prevention/Detection and similar techniques.

    Syntax: rw [OPTIONS]

    [OPTIONS]

    --start | -s            : This option starts the Kill Protection
                            program which then starts the Ransomware.

    --recover | -r          : This option recovers the affected files.

    --directories | -d      : This option helps select target directories.
                            [This is a mandatory option]
                            Example: rw --start --directories dir1 dir2 ...

    --types | -t            : This option helps select the target file types
                            [NOT mandatory. Accepts File Extensions]
                            Example: rw --start -d dir1 dir2 -t txt docx

    --help | -h             : shows this help text and exit.

    [Developer OPTIONS] (Use with precautions)

    --start-runtime | -sr   : starts ransomware directly.

    --rec | -rec            : recovers files directly.
    ```

* `Basic Examples`

    ```bash
    # to start ransomware will kill protection and target jpg and jpeg files
    rw --directories ~/dir1 ~/dir2/dir3 --types jpg jpeg --start
    ```

    ```bash
    # to recover the files affected by the above code.
    rw --directories ~/dir1 ~/dir2/dir3 --types jpg jpeg --recover
    ```

## Detailed Features

* `Base Ransomware`

    The `Ransomware` scans and isolates the targeted files and replaces them with encrypted contents rendering them useless.

    After that step, It keeps on checking the encrypted file hashes and if some file change is detected (could be the user being successful in decrypting some file or simply changed the encrypted file either accidently or due to ill motive), the `Ransomware` again encrypts the changed file.

* `Kill Protection`

    The `Ransomware` automatically restarts and re-encrypts the files.
    > Note: Each time the ransomware quits due to any reason, it restarts and re-encrypts all the files.

* `Recovery`

    No matter how many times a file is encrypted, The `Test Ransomware` will recover the original file.

* `Multiple Terminal Output`

    Once you start the `Ransomware`, apart from the current terminal, other terminals will open to notify about files and statuses.

* `Faster than most`

    The `Ransomware` is written in a python-rust mix leveraging rust's speed in time consuming tasks such as scanning for files and as such.
    > Note: This provides an addition test vector for Detection Techniques.

## Precautions

* As I mentioned earlier, Repeated killing wont help preventing/Safe-Guarding from the `Ransomware`. As soon as the `Ransomware` re-encrypts the files, the file size increases and therefore repeated killing will only result in resource loss.

* The Developer options are merely for testing and is not recommended to use.

* Double-check directories and files before using the `Ransomware`. If by any chance, recovery fails, I am not responsible for any kind of damage.

* It is recommended to use this software for educational pupose only. Any damages to property or data or resource in any form or usage in illegal activities will result in the user being liable.

## Issues

Create any issues found during usage or suggestions or anything [here](https://github.com.d33p0st/test-ransomware/issues).

## Pull Requests

For any Modifications or changes or upgrades make sure you create a pull request [here](https://github.com/d33p0st/test-ransomware/pulls).

## DISCLAIMER

**THIS SOFTWARE IS PROVIDED FOR EDUCATIONAL AND RESEARCH PURPOSES ONLY. THE CREATOR DOES NOT CONDONE OR ENCOURAGE THE USE OF THIS SOFTWARE FOR ANY ILLEGAL OR MALICIOUS ACTIVITY.**

**BY USING THIS SOFTWARE, YOU ACKNOWLEDGE AND AGREE THAT:**

1. **THE CREATOR SHALL NOT BE HELD RESPONSIBLE OR LIABLE** for any damage, loss, or disruption caused by the use of this software. This includes but is not limited to damage to data, hardware, software, or other systems, whether used in testing, production, or otherwise.

2. **THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,** either express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the creator be liable for any claims, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

3. **USERS OF THIS SOFTWARE ARE FULLY RESPONSIBLE** for ensuring that they have all necessary permissions to use the software, especially in cases where it interacts with files, systems, or environments that do not belong to them.

4. **ANY USE OF THIS SOFTWARE IN VIOLATION OF LOCAL, STATE, NATIONAL, OR INTERNATIONAL LAW** is strictly prohibited and is the sole responsibility of the user. The creator is not liable for any legal consequences that may arise from improper or unauthorized use of this software.

5. **BY USING OR DISTRIBUTING THIS SOFTWARE, YOU AGREE TO RELEASE THE CREATOR** from any and all liability, claims, or damages arising from the use or misuse of the software, including any unauthorized distribution, modification, or reverse engineering of the software.

---

**IMPORTANT: DO NOT USE THIS SOFTWARE IN PRODUCTION ENVIRONMENTS OR ON SYSTEMS THAT YOU DO NOT OWN WITHOUT EXPLICIT PERMISSION. ANY MALICIOUS USE OF THIS SOFTWARE IS STRICTLY PROHIBITED.**

---