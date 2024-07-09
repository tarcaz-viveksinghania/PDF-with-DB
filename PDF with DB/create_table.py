import mysql.connector

# Database connection details
host = 'sql3.freesqldatabase.com'
port = 3306
user = 'sql3716747'
password = 'KuUTTfiiKQ'
database = 'sql3716747'

# host_name = "sql3.freesqldatabase.com"
# user_name = "sql3716747"
# user_password = "KuUTTfiiKQ"
# db_name = "sql3716747"

# Establish the connection
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor object
cursor = conn.cursor()

# SQL statement to create the table
create_table_query = """
CREATE TABLE ss4_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ss4_1 VARCHAR(255),
    ss4_2 VARCHAR(255),
    ss4_3 VARCHAR(255),
    ss4_4a VARCHAR(255),
    ss4_4b VARCHAR(255),
    ss4_5a VARCHAR(255),
    ss4_5b VARCHAR(255),
    ss4_6 VARCHAR(255),
    ss4_7a VARCHAR(255),
    ss4_7b VARCHAR(255),
    ss4_8a VARCHAR(255),
    ss4_8b VARCHAR(255),
    ss4_8c VARCHAR(255),
    ss4_9aSoleProprietor VARCHAR(255),
    ss4_9aSoleProprietorINFO VARCHAR(255),
    ss4_9aEstate VARCHAR(255),
    ss4_9aEstateINFO VARCHAR(255),
    ss4_9aPartnership VARCHAR(255),
    ss4_9aPlanAdministrator VARCHAR(255),
    ss4_9aPlanAdministratorINFO VARCHAR(255),
    ss4_9aCorporation VARCHAR(255),
    ss4_9aCorporationINFO VARCHAR(255),
    ss4_9aTrust VARCHAR(255),
    ss4_9aTrustINFO VARCHAR(255),
    ss4_9aPersonalServiceCorporation VARCHAR(255),
    ss4_9aMilitary VARCHAR(255),
    ss4_9aStateGovernment VARCHAR(255),
    ss4_9aChurch VARCHAR(255),
    ss4_9aFarmers VARCHAR(255),
    ss4_9aFederalGovernment VARCHAR(255),
    ss4_9aOtherNonprofitOrganization VARCHAR(255),
    ss4_9aOtherNonprofitOrganizationINFO VARCHAR(255),
    ss4_9aREMIC VARCHAR(255),
    ss4_9aIndianTribalGovernments VARCHAR(255),
    ss4_9aOther VARCHAR(255),
    ss4_9aOtherINFO VARCHAR(255),
    ss4_9aGEN VARCHAR(255),
    ss4_9bState VARCHAR(255),
    ss4_9bForeign VARCHAR(255),
    ss4_10Banking VARCHAR(255),
    ss4_10BankingINFO VARCHAR(255),
    ss4_10StartNewBusiness VARCHAR(255),
    ss4_10StartNewBusinessINFO VARCHAR(255),
    ss4_10ChangedOrganization VARCHAR(255),
    ss4_10ChangedOrganizationINFO VARCHAR(255),
    ss4_10PurchasedBusiness VARCHAR(255),
    ss4_10HiredEmployees VARCHAR(255),
    ss4_10CreatedTrust VARCHAR(255),
    ss4_10CreatedTrustINFO VARCHAR(255),
    ss4_10ComplianceIRS VARCHAR(255),
    ss4_10PensionPlan VARCHAR(255),
    ss4_10PensionPlanINFO VARCHAR(255),
    ss4_10Others VARCHAR(255),
    ss4_10OthersINFO VARCHAR(255),
    ss4_11 VARCHAR(255),
    ss4_12 VARCHAR(255),
    ss4_13Agricultural VARCHAR(255),
    ss4_13Household VARCHAR(255),
    ss4_13Other VARCHAR(255),
    ss4_14 VARCHAR(255),
    ss4_15 VARCHAR(255),
    ss4_16HealthCare VARCHAR(255),
    ss4_16WholesaleAgent VARCHAR(255),
    ss4_16Construction VARCHAR(255),
    ss4_16Rental VARCHAR(255),
    ss4_16Transporting VARCHAR(255),
    ss4_16Accommodation VARCHAR(255),
    ss4_16WholesaleOther VARCHAR(255),
    ss4_16Retail VARCHAR(255),
    ss4_16RealEstate VARCHAR(255),
    ss4_16Manufacturing VARCHAR(255),
    ss4_16Finance VARCHAR(255),
    ss4_16Other VARCHAR(255),
    ss4_16OtherINFO VARCHAR(255),
    ss4_17 VARCHAR(255),
    ss4_18 VARCHAR(255),
    ss4_18EIN VARCHAR(255),
    ss4_DesigneeName VARCHAR(255),
    ss4_DesigneeTelephone VARCHAR(255),
    ss4_DesigneeAddress VARCHAR(255),
    ss4_DesigneeFax VARCHAR(255),
    ss4_ApplicantName VARCHAR(255),
    ss4_ApplicantTelephone VARCHAR(255),
    ss4_ApplicantFax VARCHAR(255)
);
"""

# Execute the query
cursor.execute(create_table_query)

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Table created successfully.")
