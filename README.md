# pyadba
This Python module allows a daring individual to access and query a SQL Server database.

It may work with Active Directory domain / NTLMv2 authentication when `pyodbc` and `pymssql` and even `sqlcmd` just **WILL**. **NOT**. **AUTHENTICATE**.

It is intended to be useful for DBAs to perform repeated tasks that would be handy to build some sort of automatic SQL script generator for. Or to grab some data for a shell script, perhaps. Or, say, to run a periodic SQL task via cron. Or just to kick back on a Friday night and get wild and crazy with some joins and cursors.

## Installation
Clone the repository and run the install script:
```
python install.py
```
This will:
- Create a virtual environment in the `venv` folder
- Install the required dependencies in the virtual environment
- Create a wrapper script to make the program easy to run (Bash or Windows)

## System Requirements
This puppy shoud work on any modern desktop operating system (Linux, Windows, Mac OS) with Python 3.6 (or higher) installed.
- **macOS**
  - Tested on macOS Monterey 12.7.4 and Ventura 13.6.6
- **Linux**
  - Tested on Red Hat Enterprise Linux 8.9 and CentOS 7.9.2009
- **Windows**
  - Tested on Windows 10 Pro x64 and Windows Server 2019
- **ChromeOS**
  - Let's be real here, if you're using a Chromebook, you're not going to be using this. And you should know, all your friends are laughing at you and your "computer" is. Seriously, could anything be more pathetic than using a computer that's basically just a giant phone with a keyboard?
- **Windows Phone**
  - ... ..... ........... well played.

# Examples

Further documentation will come later. In the meantime, here's some auto-generated info.

### Command Usage
<blockquote>
<div style="font-family:'Courier','Courier New',monospace;">
<span style="color:rgba(255,255,192,0.9);">pyadba.py</span>
<span style="color: rgba(192, 192, 255, 0.5);">[<span style="color: rgba(192, 192, 255, 0.95);">-s</span>
<span style="color: rgba(192, 128, 255, 0.9);">ARG_SERVER</span>]
[<span style="color: rgba(192, 192, 255, 0.95);">-D</span> <span style="color: rgba(192, 128, 255, 0.9);">ARG_DATABASE</span>]
[<span style="color: rgba(192, 192, 255, 0.95);">-S</span> <span style="color: rgba(192, 128, 255, 0.9);">ARG_SCHEMA</span>]
[<span style="color: rgba(192, 192, 255, 0.95);">-i</span> <span style="color: rgba(192, 128, 255, 0.9);">ARG_INPUT</span>]
[<span style="color: rgba(192, 192, 255, 0.95);">-o</span> <span style="color: rgba(192, 128, 255, 0.9);">ARG_OUTPUT_SEPARATOR</span>]
[<span style="color: rgba(192, 192, 255, 0.95);">-q</span> <span style="color: rgba(192, 128, 255, 0.9);">ARG_QUOTE_OUTPUT</span>]
[<span style="color: rgba(192, 192, 255, 0.95);">-H</span>]
[<span style="color: rgba(192, 192, 255, 0.95);">-U</span> <span style="color: rgba(192, 128, 255, 0.9);">ARG_USERNAME</span>]
[<span style="color: rgba(192, 192, 255, 0.95);">-P</span> <span style="color: rgba(192, 128, 255, 0.9);">ARG_PASSWORD</span>]
[<span style="color: rgba(192, 192, 255, 0.95);">-d</span>] [<span style="color: rgba(192, 192, 255, 0.95);">-v</span>]
[<span style="color: rgba(192, 192, 255, 0.95);">-x</span>] [<span style="color: rgba(192, 192, 255, 0.95);">-h</span>]</span>
</div>
</blockquote>


### Help Text

<blockquote style="font-family:'Courier','Courier New',monospace;">
<div style="white-space:pre-wrap;font-size:13px;">
<span style="color:lightgreen;font-size:24px;font-weight:bold;">pyadba</span>: <span style="color:lightgreen;font-size:16px;">run a sql server query from the command line</span></span><br>
<span style="color:cyan;text-decoration: underline;">Querying parameters:</span>
  <span style="color:plum;">(-s|--server)</span> <span style="color:lawngreen;">{server}</span>                   <span style="color:deepskyblue;"># Server to connect to</span>
  <span style="color:plum;">(-D|--database)</span> <span style="color:lawngreen;">{database}</span>               <span style="color:deepskyblue;"># Database name</span>
  <span style="color:plum;">(-S|--schema)</span> <span style="color:lawngreen;">{schema}</span>                   <span style="color:deepskyblue;"># Schema to use (default: dbo)</span>
  <span style="color:plum;">(-i|--input)</span> <span style="color:lawngreen;">{input_file}</span>                <span style="color:deepskyblue;"># SQL input file containing query to run</span>
  <span style="color:plum;">(-o|--output-separator)</span> <span style="color:lawngreen;">{separator}</span>      <span style="color:deepskyblue;"># Separate output columns with this (default: tab)</span>
  <span style="color:plum;">(-q|--quote-output)</span> <span style="color:lawngreen;">{quote_rule}</span>         <span style="color:deepskyblue;"># When to quote the output columns:</span><br>                                              <span style="color:deepskyblue;">(auto|always|never) (default: auto)</span>
  <span style="color: plum;">(-H|--hide-header)</span>                       <span style="color:deepskyblue;"># Hide column names of results</span><br>
<span style="color:cyan;text-decoration: underline;">Authentication parameters:</span>
  <span style="color: plum;">(-U|--username)</span> <span style="color:lawngreen;">{username}</span>               <span style="color:deepskyblue;"># Username for server and database</span>
  <span style="color: plum;">(-P|--password)</span> <span style="color:lawngreen;">{password}</span>               <span style="color:deepskyblue;"># Password for server and database</span><br>
<span style="color:cyan;text-decoration: underline;">Testing, debugging, misc. parameters:</span>
  <span style="color: plum;">(-d|--debug)</span>                             <span style="color:deepskyblue;"># Show debug information and intermediate steps</span>
  <span style="color: plum;">(-v|--version)</span>                           <span style="color:deepskyblue;"># Show program's version number and exit</span>
  <span style="color: plum;">(-x|--examples)</span>                          <span style="color:deepskyblue;"># Show examples of usage</span>
  <span style="color: plum;">(-h|--help)</span>                              <span style="color:deepskyblue;"># Show this help message and exit</span><br>
<span style="color:cyan;text-decoration: underline;">Examples:</span>
  <span style="color:forestgreen;"># Query the default server, database, and schema using the query in dbquery.sql</span>
  <span style="color:deepskyblue;">pyadba.py -i dbquery.sql</span><br>
  <span style="color:forestgreen;"># Query using commas to separate the output columns</span>
  <span style="color:deepskyblue;">pyadba.py -i dbquery.sql -o ","</span>
</span>
</div>
</blockquote>