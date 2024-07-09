import mysql.connector

# Establish MySQL connection
connection = mysql.connector.connect(
    host="sql3.freesqldatabase.com",
    port="3306",
    user="sql3716747",
    password="KuUTTfiiKQ",
    database="sql3716747"
)

# Create a cursor object using the connection
cursor = connection.cursor()

# Sample data tuple (replace with your actual data)
data = (
    # 'John Doe', '123 Main St', 'Suite 1', 'Cityville', 'ST', '12345', 'USA', 'Company Inc.', 'EIN12345', 'SSN12345',
    # 'Yes', 'N/A', 'No', 'Yes', 'N/A', 'No', 'N/A', 'No', 'Yes', 'N/A', 'No', 'N/A', 'No', 'N/A', 'No',
    # 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'N/A', 'No', 'N/A', 'No', 'N/A', 'Yes', 'N/A', 'Yes', 'N/A', 'Yes',
    # 'N/A', 'No', 'Yes', 'N/A', 'No', 'No', 'N/A', 'Yes', 'N/A', 'No', 'No', 'No', 'No', 'N/A', 'No', 'N/A', 'No',
    # 'N/A', 'Yes', 'N/A', 'No', 'N/A', 'Yes', 'No', 'No', 'No', 'No', 'N/A', 'Yes', 'N/A', 'Jane Doe', '123-456-7890',
    # '456 Elm St', 'Suite 2', 'Citytown', 'CA', '54321', 'Canada', 'Company Ltd.', 'EIN54321', 'SSN54321',
    # 'No', 'N/A', 'Yes', 'No', 'N/A', 'Yes', 'N/A', 'No', 'No', 'No', 'No', 'N/A', 'Yes', 'N/A', 'No',
    # '123-456-7891', '789 Oak St', 'Suite 3', 'Villagetown', 'NY', '67890', 'USA', 'John Smith', '987-654-3210', '987-654-3211', '987-654-3212',
    'Additional Data 1', 'Additional Data 2', 'Additional Data 3', 'Additional Data 4', 'Additional Data 5',
    'Additional Data 6', 'Additional Data 7', 'Additional Data 8', 'Additional Data 9', 'Additional Data 10',
    'Additional Data 11', 'Additional Data 12', 'Additional Data 13', 'Additional Data 14', 'Additional Data 15',
    'Additional Data 16', 'Additional Data 17', 'Additional Data 18', 'Additional Data 19', 'Additional Data 20',
    'Additional Data 21', 'Additional Data 22', 'Additional Data 23', 'Additional Data 24', 'Additional Data 25',
    'Additional Data 26', 'Additional Data 27', 'Additional Data 28', 'Additional Data 29', 'Additional Data 30',
    'Additional Data 31', 'Additional Data 32', 'Additional Data 33', 'Additional Data 34', 'Additional Data 35',
    'Additional Data 36', 'Additional Data 37', 'Additional Data 38', 'Additional Data 39', 'Additional Data 40',
    'Additional Data 41', 'Additional Data 42', 'Additional Data 43', 'Additional Data 44', 'Additional Data 45',
    'Additional Data 46', 'Additional Data 47', 'Additional Data 48', 'Additional Data 49', 'Additional Data 50',
    'Additional Data 51', 'Additional Data 52', 'Additional Data 53', 'Additional Data 54', 'Additional Data 55',
    'Additional Data 56', 'Additional Data 57', 'Additional Data 58', 'Additional Data 59', 'Additional Data 60',
    'Additional Data 61', 'Additional Data 62', 'Additional Data 63', 'Additional Data 64', 'Additional Data 65',
    'Additional Data 66', 'Additional Data 67', 'Additional Data 68', 'Additional Data 69', 'Additional Data 70',
    'Additional Data 71', 'Additional Data 72', 'Additional Data 73', 'Additional Data 74', 'Additional Data 75',
    'Additional Data 76', 'Additional Data 77', 'Additional Data 78', 'Additional Data 79', 'Additional Data 80',
    'Additional Data 81', 'Additional Data 82', 'Additional Data 83', 'Additional Data 84'
)

# Insert query with placeholders
insert_query = """
INSERT INTO ss4_table (
    ss4_1, ss4_2, ss4_3, ss4_4a, ss4_4b, ss4_5a, ss4_5b, ss4_6, ss4_7a, ss4_7b, ss4_8a, ss4_8b, ss4_8c, 
    ss4_9aSoleProprietor, ss4_9aSoleProprietorINFO, ss4_9aEstate, ss4_9aEstateINFO, ss4_9aPartnership, ss4_9aPlanAdministrator, 
    ss4_9aPlanAdministratorINFO, ss4_9aCorporation, ss4_9aCorporationINFO, ss4_9aTrust, ss4_9aTrustINFO,ss4_9aPersonalServiceCorporation, 
    ss4_9aMilitary, ss4_9aStateGovernment, ss4_9aChurch, ss4_9aFarmers, ss4_9aFederalGovernment, ss4_9aOtherNonprofitOrganization, 
    ss4_9aOtherNonprofitOrganizationINFO, ss4_9aREMIC, ss4_9aIndianTribalGovernments, ss4_9aOther, ss4_9aOtherINFO, ss4_9aGEN, ss4_9bState, 
    ss4_9bForeign, ss4_10Banking, ss4_10BankingINFO, ss4_10StartNewBusiness, ss4_10StartNewBusinessINFO, ss4_10ChangedOrganization, 
    ss4_10ChangedOrganizationINFO, ss4_10PurchasedBusiness, ss4_10HiredEmployees, ss4_10CreatedTrust, ss4_10CreatedTrustINFO, ss4_10ComplianceIRS, 
    ss4_10PensionPlan, ss4_10PensionPlanINFO, ss4_10Others, ss4_10OthersINFO, ss4_11, ss4_12, ss4_13Agricultural, ss4_13Household, 
    ss4_13Other, ss4_14, ss4_15, ss4_16HealthCare, ss4_16WholesaleAgent, ss4_16Construction, ss4_16Rental, ss4_16Transporting, 
    ss4_16Accommodation, ss4_16WholesaleOther, ss4_16Retail, ss4_16RealEstate, ss4_16Manufacturing, ss4_16Finance, ss4_16Other, ss4_16OtherINFO, ss4_17, 
    ss4_18, ss4_18EIN, ss4_DesigneeName, ss4_DesigneeTelephone, ss4_DesigneeAddress, ss4_DesigneeFax, ss4_ApplicantName, ss4_ApplicantTelephone, ss4_ApplicantFax
) 
VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
    %s, %s, %s, %s
)
"""

try:
    # Execute the query
    cursor.execute(insert_query, data)
    
    # Commit the transaction
    connection.commit()
    print("Data inserted successfully into ss4_table.")
    
except mysql.connector.Error as error:
    print(f"Failed to insert data into MySQL table: {error}")

finally:
    # Close cursor and connection
    cursor.close()
    connection.close()








# data = (
#     'John Doe', 
#     '123 Main St', 
#     'Suite 1', 
#     'Cityville', 
#     'ST', 
#     '12345', 
#     'USA', 
#     'Company Inc.', 
#     'EIN12345', 
#     'SSN12345',
#     'Yes', 
#     '123-45-6789', 
#     'No', 
#     'No', 
#     'No', 
#     'No', 
#     'Yes', 
#     'N/A', 
#     'No', 
#     'N/A', 
#     'No', 
#     'Yes', 
#     'N/A', 
#     'No', 
#     'N/A', 
#     'No', 
#     'N/A', 
#     'No',
#     'No', 
#     'No', 
#     'No', 
#     'No', 
#     'No', 
#     'No', 
#     'No', 
#     'N/A', 
#     'No', 
#     'N/A', 
#     'No', 
#     'N/A', 
#     'Yes', 
#     'N/A', 
#     'Yes', 
#     'N/A', 
#     'Yes',
#     'N/A', 
#     'No', 
#     'Yes', 
#     'N/A', 
#     'No', 
#     'No', 
#     'N/A', 
#     'Yes', 
#     'N/A', 
#     'No', 
#     'No', 
#     'No', 
#     'No', 
#     'N/A', 
#     'No', 
#     'N/A', 
#     'No',
#     'N/A', 
#     'Yes', 
#     'N/A', 
#     'No', 
#     'N/A', 
#     'Yes', 
#     'No', 
#     'No', 
#     'No', 
#     'No', 
#     'No', 
#     'No', 
#     'N/A', 
#     'Yes', 
#     'N/A', 
#     'Jane Doe', 
#     '123-456-7890',
#     '456 Elm St', 
#     '123-456-7891', 
#     'John Doe', 
#     '123-456-7892', 
#     '123-456-7893'
# )
