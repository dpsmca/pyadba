#!/usr/bin/env python3

# import pyodbc
import sys
import os
from os import path
from pathlib import Path
import argparse
import traceback
import pprint
from typing import Any, AnyStr, Union, Type
from termcolor import colored, cprint
import jaydebeapi

import config
config.init()
from config import Config

from utilities_string import string_good, strings_good, string_bad
import utilities_log
utilities_log.init()
from utilities_log import logDbg, logErr, logMsg, logWarn, logDryRun, logStdErr


PRETTY = pprint.PrettyPrinter(indent=2, width=200)

# Available text colors:
#     black, red, green, yellow, blue, magenta, cyan, white,
#     light_grey, dark_grey, light_red, light_green, light_yellow, light_blue,
#     light_magenta, light_cyan.
#
# Available text highlights:
#     on_black, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white,
#     on_light_grey, on_dark_grey, on_light_red, on_light_green, on_light_yellow,
#     on_light_blue, on_light_magenta, on_light_cyan.
#
# Available attributes:
#     bold, dark, underline, blink, reverse, concealed.
HELP_COLOR = "blue"
DYN_HELP_COLOR = "blue"
OUTPUT_COLOR = "magenta"
GROUP_COLOR = "cyan"
DESCRIPTION_COLOR = "green"
COLOR_COMMENT = "green"
COLOR_COMMAND = "blue"
COLOR_ARG = "light_blue"
COLOR_ARGP = "blue"


def evars():
    return os.environ


def evar(variable_name):
    return os.environ.get(variable_name)


def show_usage(argument_parser):
    if argument_parser is None or not isinstance(parser, argparse.ArgumentParser):
        usage_alert = f"show_usage: invalid parser provided, must provide valid ArgumentParser object"
        raise TypeError(usage_alert)
    argument_parser.print_help()
    print()
    show_examples()


def show_examples():
    cmd_path = sys.argv[0]
    cmd = os.path.basename(cmd_path)
    section_title = colored("Usage examples:", GROUP_COLOR)
    ex1 = list([f"{colored('  # Query the specified database using the query in dbquery.sql', COLOR_COMMENT)}",
                "  " + colored(cmd, COLOR_COMMAND)
                + " " + colored("-s", COLOR_ARG) + " " + colored('ROEFDN927Q', COLOR_ARGP)
                + " " + colored("-D", COLOR_ARG) + " " + colored('Adventureworks2016', COLOR_ARGP)
                + " " + colored("-s", COLOR_ARG) + " " + colored('dbo', COLOR_ARGP)
                + " " + colored("-i", COLOR_ARG) + " " + colored('dbquery.sql', COLOR_ARGP)
                ])
    ex2 = list([f"{colored('  # Same query, but use commas to separate the output columns', COLOR_COMMENT)}",
                "  " + colored(cmd, COLOR_COMMAND)
                + " " + colored("-s", COLOR_ARG) + " " + colored('ROEFDN927Q', COLOR_ARGP)
                + " " + colored("-D", COLOR_ARG) + " " + colored('Adventureworks2016', COLOR_ARGP)
                + " " + colored("-s", COLOR_ARG) + " " + colored('dbo', COLOR_ARGP)
                + " " + colored("-i", COLOR_ARG) + " " + colored('dbquery.sql', COLOR_ARGP)
                + " " + colored("-o", COLOR_ARG) + " " + colored('","', COLOR_ARGP)
                ])
    examples_output = section_title + "\n"
    examples_output += "\n".join(ex1) + "\n\n"
    examples_output += "\n".join(ex2) + "\n\n"
    print(examples_output)


def exit_error(code: int):
    # Add custom error logging or messages here
    sys.exit(code)


if __name__ == "__main__":
    '''
    This script runs a SQL query.
    '''
    program_docstring = colored("Run a SQL query from the command line", DESCRIPTION_COLOR)
    version_docstring = colored(f"{ Config['PROGRAM_NAME']} v{Config['PROGRAM_VERSION']}", DESCRIPTION_COLOR)
    parser = argparse.ArgumentParser(description=program_docstring, add_help=False)
    query_args = parser.add_argument_group(colored("Querying parameters", GROUP_COLOR))
    auth_args = parser.add_argument_group(colored("Authentication parameters", GROUP_COLOR))
    meta_args = parser.add_argument_group(colored("Testing, debugging, and miscellaneous parameters", GROUP_COLOR))
    query_args.add_argument('-s', '--server', required=False, type=str, dest="arg_server", default=None, help=colored("Server to connect to", HELP_COLOR))
    query_args.add_argument('-D', '--database', required=False, type=str, dest="arg_database", default=None, help=colored("Database name", HELP_COLOR))
    query_args.add_argument('-S', '--schema', required=False, type=str, dest="arg_schema", default=None, help=colored("Schema to use (default: dbo)", HELP_COLOR))
    query_args.add_argument('-i', '--input', required=False, type=str, dest="arg_input", default=None, help=colored("SQL input file containing query to run", HELP_COLOR))
    query_args.add_argument('-o', '--output-separator', required=False, type=str, dest="arg_output_separator", default="\t", help=colored("Separate output columns with this (default: tab)", HELP_COLOR))
    query_args.add_argument('-q', '--quote-output', required=False, type=str, dest="arg_quote_output", default="always", help=colored("When to quote the output columns: always, never, auto (default: auto)s", HELP_COLOR))
    query_args.add_argument('-H', '--hide-header', required=False, dest="arg_hide_header", action="store_true", help=colored("Hide column names of results", HELP_COLOR))

    auth_args.add_argument('-U', '--username', required=False, type=str, dest="arg_username", default=None, help=colored("Username for server and database", HELP_COLOR))
    auth_args.add_argument('-P', '--password', required=False, type=str, dest="arg_password", default=None, help=colored("Password for server and database", HELP_COLOR))

    meta_args.add_argument('-d', '--debug', required=False, dest="debug", action='store_true', help=colored("Show debug information and intermediate steps", HELP_COLOR))
    meta_args.add_argument('-v', '--version', action='version', version=version_docstring, help=colored("Show program's version number and exit", HELP_COLOR))
    meta_args.add_argument('-x', '--examples', dest="arg_examples", action='store_true', help=colored("Show examples of usage", HELP_COLOR))
    meta_args.add_argument('-h', '--help', required=False, dest="show_help", action='store_true', help=colored("Show this help message and exit", HELP_COLOR))
    inpArgs = parser.parse_args()
    show_help = inpArgs.show_help
    debug = inpArgs.debug
    Config["DEBUG"] = debug
    arg_examples = inpArgs.arg_examples
    if len(sys.argv) < 2:
        show_usage(parser)
        exit_error(0)
    if show_help:
        show_usage(parser)
        exit_error(0)
    if arg_examples:
        show_examples()
        exit_error(0)
    logDbg(f"Arguments: {' '.join(sys.argv)}")

    server = inpArgs.arg_server
    database = inpArgs.arg_database
    schema = inpArgs.arg_schema
    query_file = inpArgs.arg_input
    hide_header = inpArgs.arg_hide_header
    output_separator = inpArgs.arg_output_separator
    quote_output = inpArgs.arg_quote_output.strip(" '""").lower()
    username = inpArgs.arg_username
    password = inpArgs.arg_password
    debug = inpArgs.debug

    if string_bad(server):
        server = evar("ADBA_SERVER")

    if string_bad(database):
        database = evar("ADBA_DATABASE")

    if string_good(evar("ADBA_SCHEMA")):
        schema = evar("ADBA_SCHEMA")
        if string_bad(schema):
            schema = "dbo"

    if string_bad(username):
        username = evar("ADBA_USERNAME")

    if string_bad(password):
        password = evar("ADBA_PASSWORD")

    if config is not None and config.Config is not None:
        config.Config['DEBUG'] = debug

    valid_quote_options = list(['always', 'never', 'auto'])
    if quote_output not in valid_quote_options:
        logWarn(f"Unrecognized quote output option: '{quote_output}', will use 'always' (options: [ {', '.join(valid_quote_options)} ])")

    if not strings_good([server, database, schema]):
        show_usage(parser)
        logErr("Must specify server, database, and schema,")
        logErr("or use environment variables ADBA_SERVER, ADBA_DATABASE, ADBA_SCHEMA")
        logErr(f"Currently: server='{server}', database='{database}', schema='{schema}'")
        print(file=sys.stderr)
        exit_error(1)

    if not strings_good([username, password]):
        show_usage(parser)
        logErr("Must specify login information,")
        logErr("or use environment variables ADBA_USERNAME and ADBA_PASSWORD")
        logErr("Currently:")
        if string_bad(username):
            logErr("- username not set")
        if string_bad(password):
            logErr("- password not set")
        print(file=sys.stderr)
        exit_error(1)

    driver = "net.sourceforge.jtds.jdbc.Driver"

    server_name = server
    db_name = database
    schema = schema
    usr = username
    pwd = password

    jdbc_url = f"jdbc:jtds:sqlserver://{server_name}/{db_name};useNTLMv2=true;domain=MFAD;currentSchema={schema}"
    jdbc_file = "jtds-1.3.1.jar"
    jdbc_path = path.realpath(path.join("lib", jdbc_file))
    jdbc_lib = jdbc_path if path.exists(jdbc_path) else path.join("..", "lib", jdbc_file)

    logDbg(f"JDBC URL: {jdbc_url}")

    jdbc_lib_path = path.abspath(jdbc_lib)
    logDbg(f"JDBC abspath: {jdbc_lib_path}")
    if not path.exists(jdbc_lib_path):
        logErr(f"Could not find JDBC driver file: '{jdbc_lib_path}'")

    raw_query = ""
    if path.exists(query_file):
        with open(query_file, "r") as query_file:
            for line in query_file:
                trimmed_line = line.strip()
                if trimmed_line.startswith("#") or trimmed_line.startswith("--") or trimmed_line == "":
                    continue
                raw_query = raw_query + trimmed_line + "\n"
    else:
        logErr(f"Could not find query file: '{query_file}'")
        exit_error(1)

    query = raw_query.replace("##DATABASE##", db_name)
    query = query.replace("##SCHEMA##", schema)
    query = query.strip()

    if query is None or query.strip() == "":
        logErr(f"Query file '{query_file}' is empty")
        exit_error(1)

    namespace = {"server_name": server_name, "db_name": db_name, "usr": usr, "pwd": pwd, "schema": schema, "driver": driver, "query": query, "jdbc_url": jdbc_url, "jdbc_lib": jdbc_lib_path}

    HL = "============================================================================================="
    logDbg(f"Querying: [{server_name}].[{db_name}].[{schema}], user={usr}, query:\n{HL}\n{query}\n{HL}")

    conn = jaydebeapi.connect(driver, jdbc_url, [usr, pwd], jdbc_lib)
    curs = conn.cursor()

    curs.execute(query)

    res = curs.fetchall()
    num_cols = len(curs.description)
    col_names = list([i[0] for i in curs.description])

    rows = ""
    sep = output_separator
    if len(rows) == 0:
        logStdErr("(no results)")
        exit_error(0)
    if not hide_header:
        print(sep.join(col_names))
    for row in res:
        cols: list[str] = list()
        for col in row:
            col = col.replace("\r", "\\r")
            col = col.replace("\n", "\\n")
            col = col.replace("\t", "\\t")
            col = col.strip("'""` ")
            out = col
            if quote_output == 'auto':
                out = '""' if col is None or col == "" else '"' + str(col) + '"' if " " in str(col) else str(col)
            elif quote_output == 'never':
                out = "" if col is None else str(col)
            elif quote_output == 'always':
                out = '""' if col is None or col == "" else '"' + str(col) + '"'
            cols.append(out)
        print(sep.join(cols))
