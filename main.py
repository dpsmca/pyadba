import os
import subprocess
import pyodbc
import pymssql

USERNAME = 'm243189'
# USERNAME = 'wa07496'
# USERNAME = 'wa05281'
KEYCHAIN_NAME = 'PYODBC_' + USERNAME
DATABASE = 'dlmp_proteomics_wb_int'
# ENCRYPT = True
ENCRYPT = False

PASSWORD = os.getenv('PYTHON_ADBA_AUTH2')
if PASSWORD is None or PASSWORD == "":
    PASSWORD = subprocess.check_output(['security', 'find-generic-password', '-w', '-s', KEYCHAIN_NAME, "-a", USERNAME])  # nopep8

PASSWORD = PASSWORD.decode('ascii').strip()

# USERNAME = 'MFAD\\' + USERNAME
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
# instance = r'ROEFDN927Q\Default'
instance = 'ROEFDN927Q'

# server = 'tcp:' + instance + '.mayo.edu'
# server = instance + '.mayo.edu'
# server = 'v5103157.mayo.edu'
server = instance

# ENCRYPT defaults to yes starting in ODBC Driver 18.
# It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
# dburl = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+DATABASE+';DOMAIN=MFAD;USENTLMV2=yes;PORT=1433'
# DRIVER={ODBC Driver 17 for SQL Server};SERVER=myserver.mydomain.com;PORT=1433;DATABASE=MyDatabase;Domain=MyCompanyDomain;Instance=MyInstance;UID=myDomainUser;PWD=XXXXXXXX;Trusted_Connection=yes;Integrated_Security=SSPI
# dburl = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+DATABASE+';DOMAIN=MFAD.MFROOT.ORG;Trusted Connection=yes;Integrated_Security=SSPI;TrustServerCertificate=yes'
dburl = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+DATABASE+';DOMAIN=MFAD.MFROOT.ORG'
if ENCRYPT is True:
    dburl += ';ENCRYPT=yes'
else:
    dburl += ';ENCRYPT=no'
dburl += ';UID='+USERNAME+';PWD='+PASSWORD

# dburl = 'jdbc:jtds:sqlserver://ROEFDN927Q;'

if __name__ == '__main__':
    print("Connecting to: ", dburl, " …\n")
    cnxn = pyodbc.connect(dburl)
    # conn = pymssql.connect(
    #     # host=r'dbhostname\myinstance',
    #     host=server,
    #     port=1433,
    #     user=r'MFAD\\' + USERNAME,
    #     password=PASSWORD,
    #     database=DATABASE
    # )

    print("\nConnected!")
    # cursor = conn.cursor()
    cursor = cnxn.cursor()

    # Sample select query
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()
    while row:
        print(row[0])
        row = cursor.fetchone()
