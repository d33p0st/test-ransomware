class HelpText:
    text = """Test Ransomware v{}
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
"""