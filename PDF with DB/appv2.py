import mysql.connector
from PyPDF2 import PdfReader, PdfWriter

from scripts.ss4 import main as create_ss4

# Database connection details
host = 'sql3.freesqldatabase.com'
port = 3306
user = 'sql3716747'
password = 'KuUTTfiiKQ'
database = 'sql3716747'

# Function to create the table
# def create_table():
#     conn = mysql.connector.connect(
#         host=host,
#         port=port,
#         user=user,
#         password=password,
#         database=database
#     )
#     cursor = conn.cursor()
#     create_table_query = """
#     CREATE TABLE ss4_table (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         ss4_1 VARCHAR(255),
#         ss4_2 VARCHAR(255),
#         ss4_3 VARCHAR(255),
#         ss4_4a VARCHAR(255),
#         ss4_4b VARCHAR(255),
#         ss4_5a VARCHAR(255),
#         ss4_5b VARCHAR(255),
#         ss4_6 VARCHAR(255),
#         ss4_7a VARCHAR(255),
#         ss4_7b VARCHAR(255),
#         ss4_8a VARCHAR(255),
#         ss4_8b VARCHAR(255),
#         ss4_8c VARCHAR(255),
#         ss4_9aSoleProprietor VARCHAR(255),
#         ss4_9aSoleProprietorINFO VARCHAR(255),
#         ss4_9aEstate VARCHAR(255),
#         ss4_9aEstateINFO VARCHAR(255),
#         ss4_9aPartnership VARCHAR(255),
#         ss4_9aPlanAdministrator VARCHAR(255),
#         ss4_9aPlanAdministratorINFO VARCHAR(255),
#         ss4_9aCorporation VARCHAR(255),
#         ss4_9aCorporationINFO VARCHAR(255),
#         ss4_9aTrust VARCHAR(255),
#         ss4_9aTrustINFO VARCHAR(255),
#         ss4_9aPersonalServiceCorporation VARCHAR(255),
#         ss4_9aMilitary VARCHAR(255),
#         ss4_9aStateGovernment VARCHAR(255),
#         ss4_9aChurch VARCHAR(255),
#         ss4_9aFarmers VARCHAR(255),
#         ss4_9aFederalGovernment VARCHAR(255),
#         ss4_9aOtherNonprofitOrganization VARCHAR(255),
#         ss4_9aOtherNonprofitOrganizationINFO VARCHAR(255),
#         ss4_9aREMIC VARCHAR(255),
#         ss4_9aIndianTribalGovernments VARCHAR(255),
#         ss4_9aOther VARCHAR(255),
#         ss4_9aOtherINFO VARCHAR(255),
#         ss4_9aGEN VARCHAR(255),
#         ss4_9bState VARCHAR(255),
#         ss4_9bForeign VARCHAR(255),
#         ss4_10Banking VARCHAR(255),
#         ss4_10BankingINFO VARCHAR(255),
#         ss4_10StartNewBusiness VARCHAR(255),
#         ss4_10StartNewBusinessINFO VARCHAR(255),
#         ss4_10ChangedOrganization VARCHAR(255),
#         ss4_10ChangedOrganizationINFO VARCHAR(255),
#         ss4_10PurchasedBusiness VARCHAR(255),
#         ss4_10HiredEmployees VARCHAR(255),
#         ss4_10CreatedTrust VARCHAR(255),
#         ss4_10CreatedTrustINFO VARCHAR(255),
#         ss4_10ComplianceIRS VARCHAR(255),
#         ss4_10PensionPlan VARCHAR(255),
#         ss4_10PensionPlanINFO VARCHAR(255),
#         ss4_10Others VARCHAR(255),
#         ss4_10OthersINFO VARCHAR(255),
#         ss4_11 VARCHAR(255),
#         ss4_12 VARCHAR(255),
#         ss4_13Agricultural VARCHAR(255),
#         ss4_13Household VARCHAR(255),
#         ss4_13Other VARCHAR(255),
#         ss4_14 VARCHAR(255),
#         ss4_15 VARCHAR(255),
#         ss4_16HealthCare VARCHAR(255),
#         ss4_16WholesaleAgent VARCHAR(255),
#         ss4_16Construction VARCHAR(255),
#         ss4_16Rental VARCHAR(255),
#         ss4_16Transporting VARCHAR(255),
#         ss4_16Accommodation VARCHAR(255),
#         ss4_16WholesaleOther VARCHAR(255),
#         ss4_16Retail VARCHAR(255),
#         ss4_16RealEstate VARCHAR(255),
#         ss4_16Manufacturing VARCHAR(255),
#         ss4_16Finance VARCHAR(255),
#         ss4_16Other VARCHAR(255),
#         ss4_16OtherINFO VARCHAR(255),
#         ss4_17 VARCHAR(255),
#         ss4_18 VARCHAR(255),
#         ss4_18EIN VARCHAR(255),
#         ss4_DesigneeName VARCHAR(255),
#         ss4_DesigneeTelephone VARCHAR(255),
#         ss4_DesigneeAddress VARCHAR(255),
#         ss4_DesigneeFax VARCHAR(255),
#         ss4_ApplicantName VARCHAR(255),
#         ss4_ApplicantTelephone VARCHAR(255),
#         ss4_ApplicantFax VARCHAR(255)
#     );
#     """
#     cursor.execute(create_table_query)
#     conn.commit()
#     cursor.close()
#     conn.close()
#     print("Table created successfully.")



# def insert_ss4_data(data):
#     connection = mysql.connector.connect(
#         host = 'sql3.freesqldatabase.com'
#         port = 3306
#         user = 'sql3716747'
#         password = 'KuUTTfiiKQ'
#         database = 'sql3716747'
#     )
#     cursor = connection.cursor()
#     query = """
#     INSERT INTO ss4_data (
#         ss4_1, ss4_2, ss4_3, ss4_4a, ss4_4b, ss4_5a, ss4_5b, ss4_6, ss4_7a, ss4_7b, ss4_8a, ss4_8b, ss4_8c,
#         ss4_9aSoleProprietor, ss4_9aSoleProprietorINFO, ss4_9aEstate, ss4_9aEstateINFO, ss4_9aPartnership,
#         ss4_9aPlanAdministrator, ss4_9aPlanAdministratorINFO, ss4_9aCorporation, ss4_9aCorporationINFO,
#         ss4_9aTrust, ss4_9aTrustINFO, ss4_9aPersonalServiceCorporation, ss4_9aMilitary, ss4_9aStateGovernment,
#         ss4_9aChurch, ss4_9aFarmers, ss4_9aFederalGovernment, ss4_9aOtherNonprofitOrganization, 
#         ss4_9aOtherNonprofitOrganizationINFO, ss4_9aREMIC, ss4_9aIndianTribalGovernments, ss4_9aOther,
#         ss4_9aOtherINFO, ss4_9aGEN, ss4_9bState, ss4_9bForeign, ss4_10Banking, ss4_10BankingINFO, 
#         ss4_10StartNewBusiness, ss4_10StartNewBusinessINFO, ss4_10ChangedOrganization, ss4_10ChangedOrganizationINFO,
#         ss4_10PurchasedBusiness, ss4_10HiredEmployees, ss4_10CreatedTrust, ss4_10CreatedTrustINFO, 
#         ss4_10ComplianceIRS, ss4_10PensionPlan, ss4_10PensionPlanINFO, ss4_10Others, ss4_10OthersINFO, 
#         ss4_11, ss4_12, ss4_13Agricultural, ss4_13Household, ss4_13Other, ss4_14, ss4_15, ss4_16HealthCare,
#         ss4_16WholesaleAgent, ss4_16Construction, ss4_16Rental, ss4_16Transporting, ss4_16Accommodation, 
#         ss4_16WholesaleOther, ss4_16Retail, ss4_16RealEstate, ss4_16Manufacturing, ss4_16Finance, 
#         ss4_16Other, ss4_16OtherINFO, ss4_17, ss4_18, ss4_18EIN, ss4_DesigneeName, ss4_DesigneeTelephone, 
#         ss4_DesigneeAddress, ss4_DesigneeFax, ss4_ApplicantName, ss4_ApplicantTelephone, ss4_ApplicantFax
#     ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """
#     cursor.execute(query, data)
#     connection.commit()
#     connection.close()

# # Example data
# data = (
#     'John Doe', '123 Main St', 'Suite 1', 'Cityville', 'ST', '12345', 'USA', 'Company Inc.', 'EIN12345', 'SSN12345',
#     'Yes', '123-45-6789', 'No', 'Yes', 'N/A', 'No', 'N/A', 'No', 'Yes', 'N/A', 'No', 'N/A', 'No', 'N/A', 'No',
#     'No', 'No', 'No', 'No', 'No', 'No', 'No', 'N/A', 'No', 'N/A', 'No', 'N/A', 'Yes', 'N/A', 'Yes', 'N/A', 'Yes',
#     'N/A', 'No', 'Yes', 'N/A', 'No', 'No', 'N/A', 'Yes', 'N/A', 'No', 'No', 'No', 'No', 'N/A', 'No', 'N/A', 'No',
#     'N/A', 'Yes', 'N/A', 'No', 'N/A', 'Yes', 'No', 'No', 'No', 'No', 'N/A', 'Yes', 'N/A', 'Jane Doe', '123-456-7890',
#     '456 Elm St', '123-456-7891', 'John Doe', '123-456-7892', '123-456-7893'
# )

# insert_ss4_data(data)


# import mysql.connector

# def insert_ss4_data(data):
#     connection = mysql.connector.connect(
#         host='sql3.freesqldatabase.com',
#         port=3306,
#         user='sql3716747',
#         password='KuUTTfiiKQ',
#         database='sql3716747'
#     )
#     cursor = connection.cursor()
#     query = """
#     INSERT INTO ss4_table (
#         ss4_1, ss4_2, ss4_3, ss4_4a, ss4_4b, ss4_5a, ss4_5b, ss4_6, ss4_7a, ss4_7b, ss4_8a, ss4_8b, ss4_8c,
#         ss4_9aSoleProprietor, ss4_9aSoleProprietorINFO, ss4_9aEstate, ss4_9aEstateINFO, ss4_9aPartnership,
#         ss4_9aPlanAdministrator, ss4_9aPlanAdministratorINFO, ss4_9aCorporation, ss4_9aCorporationINFO,
#         ss4_9aTrust, ss4_9aTrustINFO, ss4_9aPersonalServiceCorporation, ss4_9aMilitary, ss4_9aStateGovernment,
#         ss4_9aChurch, ss4_9aFarmers, ss4_9aFederalGovernment, ss4_9aOtherNonprofitOrganization, 
#         ss4_9aOtherNonprofitOrganizationINFO, ss4_9aREMIC, ss4_9aIndianTribalGovernments, ss4_9aOther,
#         ss4_9aOtherINFO, ss4_9aGEN, ss4_9bState, ss4_9bForeign, ss4_10Banking, ss4_10BankingINFO, 
#         ss4_10StartNewBusiness, ss4_10StartNewBusinessINFO, ss4_10ChangedOrganization, ss4_10ChangedOrganizationINFO,
#         ss4_10PurchasedBusiness, ss4_10HiredEmployees, ss4_10CreatedTrust, ss4_10CreatedTrustINFO, 
#         ss4_10ComplianceIRS, ss4_10PensionPlan, ss4_10PensionPlanINFO, ss4_10Others, ss4_10OthersINFO, 
#         ss4_11, ss4_12, ss4_13Agricultural, ss4_13Household, ss4_13Other, ss4_14, ss4_15, ss4_16HealthCare,
#         ss4_16WholesaleAgent, ss4_16Construction, ss4_16Rental, ss4_16Transporting, ss4_16Accommodation, 
#         ss4_16WholesaleOther, ss4_16Retail, ss4_16RealEstate, ss4_16Manufacturing, ss4_16Finance, 
#         ss4_16Other, ss4_16OtherINFO, ss4_17, ss4_18, ss4_18EIN, ss4_DesigneeName, ss4_DesigneeTelephone, 
#         ss4_DesigneeAddress, ss4_DesigneeFax, ss4_ApplicantName, ss4_ApplicantTelephone, ss4_ApplicantFax
#     ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """

#     print(f"Number of placeholders in query: {query.count('%s')}")

#     cursor.execute(query, data)
#     connection.commit()
#     connection.close()

# # Example data
# data = (
#     # 'John Doe', '123 Main St', 'Suite 1', 'Cityville', 'ST', '12345', 'USA', 'Company Inc.', 'EIN12345', 'SSN12345',
#     # 'Yes', 'N/A', 'No', 'Yes', 'N/A', 'No', 'N/A', 'No', 'Yes', 'N/A', 'No', 'N/A', 'No', 'N/A', 'No',
#     # 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'N/A', 'No', 'N/A', 'No', 'N/A', 'Yes', 'N/A', 'Yes', 'N/A', 'Yes',
#     # 'N/A', 'No', 'Yes', 'N/A', 'No', 'No', 'N/A', 'Yes', 'N/A', 'No', 'No', 'No', 'No', 'N/A', 'No', 'N/A', 'No',
#     # 'N/A', 'Yes', 'N/A', 'No', 'N/A', 'Yes', 'No', 'No', 'No', 'No', 'N/A', 'Yes', 'N/A', 'Jane Doe', '123-456-7890',
#     # '456 Elm St', 'Suite 2', 'Citytown', 'CA', '54321', 'Canada', 'Company Ltd.', 'EIN54321', 'SSN54321',
#     # 'No', 'N/A', 'Yes', 'No', 'N/A', 'Yes', 'N/A', 'No', 'No', 'No', 'No', 'N/A', 'Yes', 'N/A', 'No',
#     # '123-456-7891', '789 Oak St', 'Suite 3', 'Villagetown', 'NY', '67890', 'USA', 'John Smith', '987-654-3210', '987-654-3211', '987-654-3212',
#     'Additional Data 1', 'Additional Data 2', 'Additional Data 3', 'Additional Data 4', 'Additional Data 5',
#     'Additional Data 6', 'Additional Data 7', 'Additional Data 8', 'Additional Data 9', 'Additional Data 10',
#     'Additional Data 11', 'Additional Data 12', 'Additional Data 13', 'Additional Data 14', 'Additional Data 15',
#     'Additional Data 16', 'Additional Data 17', 'Additional Data 18', 'Additional Data 19', 'Additional Data 20',
#     'Additional Data 21', 'Additional Data 22', 'Additional Data 23', 'Additional Data 24', 'Additional Data 25',
#     'Additional Data 26', 'Additional Data 27', 'Additional Data 28', 'Additional Data 29', 'Additional Data 30',
#     'Additional Data 31', 'Additional Data 32', 'Additional Data 33', 'Additional Data 34', 'Additional Data 35',
#     'Additional Data 36', 'Additional Data 37', 'Additional Data 38', 'Additional Data 39', 'Additional Data 40',
#     'Additional Data 41', 'Additional Data 42', 'Additional Data 43', 'Additional Data 44', 'Additional Data 45',
#     'Additional Data 46', 'Additional Data 47', 'Additional Data 48', 'Additional Data 49', 'Additional Data 50',
#     'Additional Data 51', 'Additional Data 52', 'Additional Data 53', 'Additional Data 54', 'Additional Data 55',
#     'Additional Data 56', 'Additional Data 57', 'Additional Data 58', 'Additional Data 59', 'Additional Data 60',
#     'Additional Data 61', 'Additional Data 62', 'Additional Data 63', 'Additional Data 64', 'Additional Data 65',
#     'Additional Data 66', 'Additional Data 67', 'Additional Data 68', 'Additional Data 69', 'Additional Data 70',
#     'Additional Data 71', 'Additional Data 72', 'Additional Data 73', 'Additional Data 74', 'Additional Data 75',
#     'Additional Data 76', 'Additional Data 77', 'Additional Data 78', 'Additional Data 79', 'Additional Data 80',
#     'Additional Data 81', 'Additional Data 82', 'Additional Data 83', 'Additional Data 84', 'Additional Data 85',
#     'Additional Data 86', 'Additional Data 87'
# )



# print(f"Number of elements in data: {len(data)}")


# insert_ss4_data(data)  




# Function to fill the SS4 form
def fill_ss4(ss4_path, *args):
    (
        ss4_1, ss4_2, ss4_3, ss4_4a, ss4_4b, ss4_5a, ss4_5b, ss4_6, ss4_7a, ss4_7b, ss4_8a, ss4_8b, ss4_8c,
        ss4_9aSoleProprietor, ss4_9aSoleProprietorINFO, ss4_9aEstate, ss4_9aEstateINFO, ss4_9aPartnership,
        ss4_9aPlanAdministrator, ss4_9aPlanAdministratorINFO, ss4_9aCorporation, ss4_9aCorporationINFO,
        ss4_9aTrust, ss4_9aTrustINFO, ss4_9aPersonalServiceCorporation, ss4_9aMilitary, ss4_9aStateGovernment,
        ss4_9aChurch, ss4_9aFarmers, ss4_9aFederalGovernment, ss4_9aOtherNonprofitOrganization, 
        ss4_9aOtherNonprofitOrganizationINFO, ss4_9aREMIC, ss4_9aIndianTribalGovernments, ss4_9aOther,
        ss4_9aOtherINFO, ss4_9aGEN, ss4_9bState, ss4_9bForeign, ss4_10Banking, ss4_10BankingINFO, 
        ss4_10StartNewBusiness, ss4_10StartNewBusinessINFO, ss4_10ChangedOrganization, ss4_10ChangedOrganizationINFO,
        ss4_10PurchasedBusiness, ss4_10HiredEmployees, ss4_10CreatedTrust, ss4_10CreatedTrustINFO, 
        ss4_10ComplianceIRS, ss4_10PensionPlan, ss4_10PensionPlanINFO, ss4_10Others, ss4_10OthersINFO, 
        ss4_11, ss4_12, ss4_13Agricultural, ss4_13Household, ss4_13Other, ss4_14, ss4_15, ss4_16HealthCare,
        ss4_16WholesaleAgent, ss4_16Construction, ss4_16Rental, ss4_16Transporting, ss4_16Accommodation, 
        ss4_16WholesaleOther, ss4_16Retail, ss4_16RealEstate, ss4_16Manufacturing, ss4_16Finance, 
        ss4_16Other, ss4_16OtherINFO, ss4_17, ss4_18, ss4_18EIN, ss4_DesigneeName, ss4_DesigneeTelephone, 
        ss4_DesigneeAddress, ss4_DesigneeFax, ss4_ApplicantName, ss4_ApplicantTelephone, ss4_ApplicantFax
    ) = args
    pdf = PdfReader(ss4_path)
    values = {
        '(EIN)': "", 
        '(1)': ss4_1, 
        '(2)': ss4_2, 
        '(3)': ss4_3, 
        '(4a)': ss4_4a, 
        '(4b)': ss4_4b, 
        '(5a)': ss4_5a, 
        '(5b)': ss4_5b, 
        '(6)': ss4_6, 
        '(7a)': ss4_7a, 
        '(7b)': ss4_7b, 
        '(8aYes)': True if ss4_8a == "Yes" else False, 
        '(8aNo)': True if ss4_8a == "No" else False, 
        '(8b)': ss4_8b, 
        '(8cYes)': True if ss4_8c == "Yes" else False, 
        '(8cNo)': True if ss4_8c == "No" else False, 
        '(9aSoleProprietor)': ss4_9aSoleProprietor, 
        '(9aSoleProprietorINFO)': ss4_9aSoleProprietorINFO, 
        '(9aEstate)': ss4_9aEstate, 
        '(9aEstateINFO)': ss4_9aEstateINFO, 
        '(9aPartnership)': ss4_9aPartnership, 
        '(9aPlanAdministrator)': ss4_9aPlanAdministrator, 
        '(9aPlanAdministratorINFO)': ss4_9aPlanAdministratorINFO, 
        '(9aCorporation)': ss4_9aCorporation, 
        '(9aCorporationINFO)': ss4_9aCorporationINFO, 
        '(9aTrust)': ss4_9aTrust, 
        '(9aTrustINFO)': ss4_9aTrustINFO, 
        '(9aPersonalServiceCorporation)': ss4_9aPersonalServiceCorporation, 
        '(9aMilitary)': ss4_9aMilitary, 
        '(9aStateGovernment)': ss4_9aStateGovernment, 
        '(9aChurch)': ss4_9aChurch, 
        '(9aFarmers)': ss4_9aFarmers, 
        '(9aFederalGovernment)': ss4_9aFederalGovernment, 
        '(9aOtherNonprofitOrganization)': ss4_9aOtherNonprofitOrganization, 
        '(9aOtherNonprofitOrganizationINFO)': ss4_9aOtherNonprofitOrganizationINFO, 
        '(9aREMIC)': ss4_9aREMIC, 
        '(9aIndianTribalGovernments)': ss4_9aIndianTribalGovernments, 
        '(9aOther)': ss4_9aOther, 
        '(9aOtherINFO)': ss4_9aOtherINFO, 
        '(9aGEN)': ss4_9aGEN, 
        '(9bState)': ss4_9bState, 
        '(9bForeign)': ss4_9bForeign, 
        '(10Banking)': ss4_10Banking, 
        '(10BankingINFO)': ss4_10BankingINFO, 
        '(10StartNewBusiness)': ss4_10StartNewBusiness, 
        '(10StartNewBusinessINFO)': ss4_10StartNewBusinessINFO, 
        # '(10StartNewBusinessINFO2)': ss4_10StartNewBusinessINFO, 
        '(10ChangedOrganization)': ss4_10ChangedOrganization, 
        '(10ChangedOrganizationINFO)': ss4_10ChangedOrganizationINFO, 
        '(10PurchasedBusiness)': ss4_10PurchasedBusiness, 
        '(10HiredEmployees)': ss4_10HiredEmployees, 
        '(10CreatedTrust)': ss4_10CreatedTrust, 
        '(10CreatedTrustINFO)': ss4_10CreatedTrustINFO, 
        '(10ComplianceIRS)': ss4_10ComplianceIRS, 
        '(10PensionPlan)': ss4_10PensionPlan, 
        '(10PensionPlanINFO)': ss4_10PensionPlanINFO, 
        '(10Others)': ss4_10Others, 
        '(10OthersINFO)': ss4_10OthersINFO, 
        '(11)': ss4_11, 
        '(12)': ss4_12, 
        '(13Agricultural)': ss4_13Agricultural, 
        '(13Household)': ss4_13Household, 
        '(13Other)': ss4_13Other, 
        '(14)': ss4_14, 
        '(15)': ss4_15, 
        '(16HealthCare)': ss4_16HealthCare, 
        '(16WholesaleAgent)': ss4_16WholesaleAgent, 
        '(16Construction)': ss4_16Construction, 
        '(16Rental)': ss4_16Rental, 
        '(16Transporting)': ss4_16Transporting, 
        '(16Accommodation)': ss4_16Accommodation, 
        '(16WholesaleOther)': ss4_16WholesaleOther, 
        '(16Retail)': ss4_16Retail, 
        '(16RealEstate)': ss4_16RealEstate, 
        '(16Manufacturing)': ss4_16Manufacturing, 
        '(16Finance)': ss4_16Finance, 
        '(16Other)': ss4_16Other, 
        '(16OtherINFO)': ss4_16OtherINFO, 
        '(17)': ss4_17, 
        '(18Yes)': True if ss4_18 == "Yes" else False, 
        '(18No)': True if ss4_18 == "No" else False, 
        '(18EIN)': ss4_18EIN, 
        '(DesigneeName)': ss4_DesigneeName, 
        '(DesigneeTelephone)': ss4_DesigneeTelephone, 
        '(DesigneeAddress)': ss4_DesigneeAddress, 
        '(DesigneeFax)': ss4_DesigneeFax, 
        '(ApplicantName)': ss4_ApplicantName, 
        '(ApplicantTelephone)': ss4_ApplicantTelephone, 
        '(ApplicantFax)': ss4_ApplicantFax
    }
    updated_pdf = create_ss4(pdf=pdf, values=values)
    output_path = f"SS4.pdf"
    PdfWriter().write(output_path, updated_pdf)
    return output_path

# # Function to fetch data from the database and fill the SS4 form
def fetch_and_fill_ss4():
    conn = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ss4_table LIMIT 1")  # Adjust the query as needed
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        ss4_path = 'fss4.pdf'  # Provide the correct path to your SS4 PDF template
        output_path = fill_ss4(ss4_path, *result[1:])  # Skip the first element (id)
        print(f"SS4 form filled and saved at: {output_path}")
    else:
        print("No data found in the database.")

# Run the functions
# create_table()
fetch_and_fill_ss4()
