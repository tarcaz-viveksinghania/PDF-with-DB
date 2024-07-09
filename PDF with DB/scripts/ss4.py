from pdfrw import PdfReader, PdfDict, PdfWriter, PdfName
from typing import Dict, Any


### Function to change PDF fields, run once to modify the original PDF
def change_pdf_fields(pdf: PdfReader) -> PdfReader:
    # pdf = PdfReader(pdf_path)
    new_field_names_9a = [
        "9aSoleProprietor", "9aSoleProprietorINFO", "9aEstate", "9aEstateINFO", "9aPartnership", "9aPlanAdministrator", 
        "9aPlanAdministratorINFO", "9aCorporation", "9aCorporationINFO", "9aTrust", "9aTrustINFO", "9aPersonalServiceCorporation", 
        "9aMilitary", "9aStateGovernment", "9aChurch", "9aFarmers", "9aFederalGovernment", "9aOtherNonprofitOrganization", 
        "9aOtherNonprofitOrganizationINFO", "9aREMIC", "9aIndianTribalGovernments", "9aOther", "9aOtherINFO", "9aGEN", 
    ]
    new_field_names_10 = [
        "10Banking", "10BankingINFO", "10StartNewBusiness", "10StartNewBusinessINFO", "10StartNewBusinessINFO2", "10ChangedOrganization", 
        "10ChangedOrganizationINFO", "10PurchasedBusiness", "10HiredEmployees", "10CreatedTrust", "10CreatedTrustINFO", "10ComplianceIRS", 
        "10PensionPlan", "10PensionPlanINFO", "10Others", "10OthersINFO",
    ]
    new_field_names_16 = [
        "16HealthCare", "16WholesaleAgent", "16Construction", "16Rental", "16Transporting", "16Accommodation", "16WholesaleOther", 
        "16Retail", "16RealEstate", "16Manufacturing", "16Finance", "16Other", "16OtherINFO",
    ]
    new_field_names = (
        ["EIN", "1", "2", "3", "4a", "4b", "5a", "5b", "6", "7a", "7b", "8aYes", "8aNo", "8b", "8cYes", "8cNo"]
        + new_field_names_9a 
        + ["9bState", "9bForeign"]
        + new_field_names_10
        + ["11", "12", "13Agricultural", "13Household", "13Other", "14", "15"] 
        + new_field_names_16
        + ["17", "18Yes", "18No", "18EIN", "DesigneeName", "DesigneeTelephone", "DesigneeAddress", "DesigneeFax", "ApplicantName", "ApplicantTelephone", "ApplicantFax"]
    )
    field_counter = 0    
    for page in pdf.pages:
        annotations = page['/Annots']
        if annotations:
            for annotation in annotations:
                if annotation['/Subtype'] == '/Widget':
                    field_name = annotation.get('/T')
                    if field_name:
                        field_name = pdf_fields[field_counter]
                        annotation.update(PdfDict(T=field_name))
                        field_counter += 1
    # PdfWriter().write(pdf_path, pdf)
    return pdf


### Function to get PDF fields, run once to verify the change
def get_pdf_fields(pdf_path: str):
    field_names = []
    pdf = PdfReader(pdf_path)
    for page in pdf.pages:
        annotations = page['/Annots']
        if annotations:
            for annotation in annotations:
                if annotation['/Subtype'] == '/Widget':
                    field_name = annotation.get('/T')
                    if field_name:
                        field_names.append(field_name)
    return field_names


pdf_fields = [
    '(EIN)', '(1)', '(2)', '(3)', '(4a)', '(4b)', '(5a)', '(5b)', '(6)', '(7a)', '(7b)', '(8aYes)', '(8aNo)', '(8b)', '(8cYes)', '(8cNo)', 
    '(9aSoleProprietor)', '(9aSoleProprietorINFO)', '(9aEstate)', '(9aEstateINFO)', '(9aPartnership)', '(9aPlanAdministrator)', '(9aPlanAdministratorINFO)', 
    '(9aCorporation)', '(9aCorporationINFO)', '(9aTrust)', '(9aTrustINFO)', '(9aPersonalServiceCorporation)', '(9aMilitary)', '(9aStateGovernment)', '(9aChurch)', 
    '(9aFarmers)', '(9aFederalGovernment)', '(9aOtherNonprofitOrganization)', '(9aOtherNonprofitOrganizationINFO)', '(9aREMIC)', '(9aIndianTribalGovernments)', 
    '(9aOther)', '(9aOtherINFO)', '(9aGEN)', '(9bState)', '(9bForeign)', '(10Banking)', '(10BankingINFO)', '(10StartNewBusiness)', '(10StartNewBusinessINFO)', 
    '(10StartNewBusinessINFO2)', '(10ChangedOrganization)', '(10ChangedOrganizationINFO)', '(10PurchasedBusiness)', '(10HiredEmployees)', '(10CreatedTrust)', 
    '(10CreatedTrustINFO)', '(10ComplianceIRS)', '(10PensionPlan)', '(10PensionPlanINFO)', '(10Others)', '(10OthersINFO)', '(11)', '(12)', '(13Agricultural)', 
    '(13Household)', '(13Other)', '(14)', '(15)', '(16HealthCare)', '(16WholesaleAgent)', '(16Construction)', '(16Rental)', '(16Transporting)', '(16Accommodation)', 
    '(16WholesaleOther)', '(16Retail)', '(16RealEstate)', '(16Manufacturing)', '(16Finance)', '(16Other)', '(16OtherINFO)', '(17)', '(18Yes)', '(18No)', '(18EIN)', 
    '(DesigneeName)', '(DesigneeTelephone)', '(DesigneeAddress)', '(DesigneeFax)', '(ApplicantName)', '(ApplicantTelephone)', '(ApplicantFax)'
]

checkboxes_field_name_dict = {
    "(8aYes)": 1, "(8aNo)": 2,
    "(8cYes)": 1, "(8cNo)": 2,
    "(9aSoleProprietor)": 1, "(9aPartnership)": 2, "(9aCorporation)": 3, "(9aPersonalServiceCorporation)": 4,
    "(9aChurch)": 5, "(9aOtherNonprofitOrganization)": 6, "(9aOther)": 7, "(9aEstate)": 8,
    "(9aPlanAdministrator)": 9, "(9aTrust)": 10, "(9aMilitary)": 11, "(9aFarmers)": 12, "(9aREMIC)": 13,
    "(9aStateGovernment)": 14, "(9aFederalGovernment)": 15, "(9aIndianTribalGovernments)": 16,
    "(10StartNewBusiness)": 1, "(10HiredEmployees)": 2, "(10ComplianceIRS)": 3, "(10Others)": 4,
    "(10Banking)": 5, "(10ChangedOrganization)": 6, "(10PurchasedBusiness)": 7, "(10CreatedTrust)": 8,
    "(14)": 1,
    "(16Construction)": 1, "(16RealEstate)": 2, "(16Rental)": 3, "(16Manufacturing)": 4,
    "(16Transporting)": 5, "(16Finance)": 6, "(16HealthCare)": 7, "(16Accommodation)": 8,
    "(16Other)": 9, "(16WholesaleAgent)": 10, "(16WholesaleOther)": 11, "(16Retail)": 12,
    "(18Yes)": 1, "(18No)": 2
}


def main(pdf: PdfReader, values: Dict[str, Any]):
    change_pdf_fields(pdf)
    for page in pdf.pages:
        annotations = page['/Annots']
        if annotations:
            for annotation in annotations:
                if annotation['/Subtype'] == '/Widget':
                    field_name = annotation.get('/T')
                    if field_name:                        
                        if field_name in values.keys():
                            value = values[field_name]
                            if field_name in checkboxes_field_name_dict:
                                if value == True:
                                    value = checkboxes_field_name_dict.get(f"{field_name}")                                    
                                annotation.update(PdfDict(V=PdfName(f'{value}')))
                            else:
                                annotation.update(PdfDict(V=PdfName(f'{value}')))
    return pdf




# ===============================================================================================

# from pdfrw import PdfReader, PdfDict, PdfWriter, PdfName
# from typing import Dict, Any

# checkboxes_field_name_dict = {
#     "(8aYes)": 1, "(8aNo)": 2,
#     "(8cYes)": 1, "(8cNo)": 2,
#     "(9aSoleProprietor)": 1, "(9aPartnership)": 2, "(9aCorporation)": 3, "(9aPersonalServiceCorporation)": 4,
#     "(9aChurch)": 5, "(9aOtherNonprofitOrganization)": 6, "(9aOther)": 7, "(9aEstate)": 8,
#     "(9aPlanAdministrator)": 9, "(9aTrust)": 10, "(9aMilitary)": 11, "(9aFarmers)": 12, "(9aREMIC)": 13,
#     "(9aStateGovernment)": 14, "(9aFederalGovernment)": 15, "(9aIndianTribalGovernments)": 16,
#     "(10StartNewBusiness)": 1, "(10HiredEmployees)": 2, "(10ComplianceIRS)": 3, "(10Others)": 4,
#     "(10Banking)": 5, "(10ChangedOrganization)": 6, "(10PurchasedBusiness)": 7, "(10CreatedTrust)": 8,
#     "(14)": 1,
#     "(16Construction)": 1, "(16RealEstate)": 2, "(16Rental)": 3, "(16Manufacturing)": 4,
#     "(16Transporting)": 5, "(16Finance)": 6, "(16HealthCare)": 7, "(16Accommodation)": 8,
#     "(16Other)": 9, "(16WholesaleAgent)": 10, "(16WholesaleOther)": 11, "(16Retail)": 12,
#     "(18Yes)": 1, "(18No)": 2
# }

# def main(pdf: PdfReader, values: Dict[str, Any]):
#     for page_number, page in enumerate(pdf.pages, start=1):
#         annotations = page['/Annots']
#         if annotations:
#             for annotation in annotations:
#                 if annotation['/Subtype'] == '/Widget':
#                     field_name = annotation.get('/T')
#                     if field_name:
#                         print(f"Page {page_number}, Field {field_name}: Found")
#                         if field_name in values.keys():
#                             value = values[field_name]
#                             print(f"Page {page_number}, Field {field_name}: Updating with value {value}")
#                             if field_name in checkboxes_field_name_dict:
#                                 if value:
#                                     value = checkboxes_field_name_dict.get(field_name)
#                                     annotation.update(PdfDict(V=PdfName('Yes'), AS=PdfName('Yes')))
#                                     print(f"Page {page_number}, Field {field_name}: Checkbox set to 'Yes'")
#                                 else:
#                                     annotation.update(PdfDict(V=PdfName('Off'), AS=PdfName('Off')))
#                                     print(f"Page {page_number}, Field {field_name}: Checkbox set to 'Off'")
#                             else:
#                                 annotation.update(PdfDict(V=str(value)))
#                                 print(f"Page {page_number}, Field {field_name}: Text set to '{value}'")
#     return pdf

# # Example usage
# pdf_path = 'templates/SS4.pdf'
# values = {
#     "(EIN)": "12-3456789",
#     "(1)": "Example Company",
#     "(8aYes)": True,
#     "(9aSoleProprietor)": True,
#     # Add more field values as needed
# }

# pdf = PdfReader(pdf_path)
# modified_pdf = main(pdf, values)
# PdfWriter().write('modified_pdf.pdf', modified_pdf)
