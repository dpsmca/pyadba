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

```bash
python pyadba.py [-s ARG_SERVER] [-D ARG_DATABASE] [-S ARG_SCHEMA] [-i ARG_INPUT] [-o ARG_OUTPUT_SEPARATOR] [-q ARG_QUOTE_OUTPUT] [-H] [-U ARG_USERNAME] [-P ARG_PASSWORD] [-d] [-v] [-x] [-h]
```

### Help Text

```bash
Run a SQL query from the command line

Querying parameters:
  -s ARG_SERVER, --server ARG_SERVER
                        Server to connect to
  -D ARG_DATABASE, --database ARG_DATABASE
                        Database name
  -S ARG_SCHEMA, --schema ARG_SCHEMA
                        Schema to use (default: dbo)
  -i ARG_INPUT, --input ARG_INPUT
                        SQL input file containing query to run
  -o ARG_OUTPUT_SEPARATOR, --output-separator ARG_OUTPUT_SEPARATOR
                        Separate output columns with this (default: tab)
  -q ARG_QUOTE_OUTPUT, --quote-output ARG_QUOTE_OUTPUT
                        When to quote the output columns: always, never, auto (default: auto)s
  -H, --hide-header     Hide column names of results

Authentication parameters:
  -U ARG_USERNAME, --username ARG_USERNAME
                        Username for server and database
  -P ARG_PASSWORD, --password ARG_PASSWORD
                        Password for server and database

Testing, debugging, and miscellaneous parameters:
  -d, --debug           Show debug information and intermediate steps
  -v, --version         Show program's version number and exit
  -x, --examples        Show examples of usage
  -h, --help            Show this help message and exit

Usage examples:
  # Query the specified database using the query in dbquery.sql
  pyadba.py -s ROEFDN927Q -D Adventureworks2016 -s dbo -i dbquery.sql

  # Same query, but use commas to separate the output columns
  pyadba.py -s ROEFDN927Q -D Adventureworks2016 -s dbo -i dbquery.sql -o ","
```
