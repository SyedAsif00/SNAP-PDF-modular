# sample.py

# This is a sample data dictionary that contains the form field values to be filled in the PDF.
# The keys correspond to the form field names, and the values are what we want to set for those fields.

sample_data = {
    "Name": {"value": "Syed Asif Ullah", "type": "Full Name"},
    "Home Address": {
        "value": "ABC street",
        "type": "Text Field"
    },
    "City, State, Zip Code_Home": {
        "value": "abc, XYZ, 28328",
        "type": "Text Field"
    },
    "Mailing Address": {
        "value": "DEF street abc town",
        "type": "Text Field"
    },
    "Mailing Address": {
        "value": "DEF street abc town",
        "type": "Text Field"
    },
    "City State Zip Code if_mailing": {
        "value": "ABC, hjghg, 28378",
        "type": "Text Field"
    },
    "Phone Number": {
        "value": "0198989898989889",
        "type": "Text Field"
    },
    "Are you homeless": {
        "value": "Yes",
        "type": "Yes/No"
    },
    "If you do not want DTA to text you, please check this box": {
        "value": "",
        "type": "Single Checkbox"
    }, 
    "Do you have a Massachusetts Electronic Benefits Transfer (EBT) card?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    "Disability": {
        "value": [""],
        "type": "Multiple Options"
    },
    "Impairment Types": {
        "value": [""],
        "type": "Multiple Options"
    },
     "Impairment Other": {
        "value": "", 
        "type": "Text Field"
    },
     "Communication Methods": {
        "value": ["InPerson"],
        "type": "Multiple Options"
    },
     "VRS Phone Number": {
        "value": "",
        "type": "Text Field"
    },
     "Has Massachusetts certified that you have a disability?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    "Social Security Number": {
        "value": "737267",
        "type": "Text Field"
    },
    "Date of Birth": {
        "value": "",
        "type": "Text Field"
    },
    "Gender": {
        "value": "Male",  # Can be Male/Female, one at a time
        "type": "Gender"
    },
    "Are you pregnant?": {
        "value": "Yes",  # Can be Yes/No
        "type": "Yes/No"
    },
    "Are you a U.S. citizen": {
        "value": "",  # Can be Yes/No
        "type": "Yes/No"
    },
    "Language preference" : {
        "value" : "english",
        "type":"Text Field"
    },
    "Ethnicity": {
        "value": "",  
        "type": "Single Select"
    },
    "Race": {
        "value": "",  
        "type": "Single Select"
    },
    "Do other poeple live with you" : {
        "value" : "Yes",
        "type" : "Yes/No"
    },
    "Has anyone worked in the last 60 days?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    "Does anyone receive any other type of income such as Unemployment Compensation, Child Support, Social Security, SSI, Workers’ Compensation, Veterans’ Benefits, Pensions or Rental Income?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    "Is the household responsible to pay the shelter cost?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    "Is the household responsible to pay utility costs separate from shelter costs?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    "Is anyone responsible to pay for adult or child care costs?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    "Does anyone travel to and/or from a dependent care provider?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    "Does anyone who is at least 60 years old and/or disabled have out-of-pocket medical expenses?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    "Does anyone travel to and/or from medical care such as a pharmacy, doctor, therapist, etc.)?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    "Is anyone in a training program at least 80 hours per month?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    "Is anyone working in exchange for goods and services (in-kind work)?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    "Is anyone doing an unpaid internship?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    "Is anyone volunteering?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    "Has anyone received SNAP benefits outside of MA within past 30 days?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    # "Do you want to give us permission to contact a person or agency if we cannot reach you by phone?": {
    #     "value": "",
    #     "type": "Yes/No"
    # },
    "Do you want to give a person or agency permission to speak with DTA and get relevant confidential information about your case?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    "Do you want to give an agency or someone you trust permission to sign forms, report changes, complete interviews, and talk about your case with us?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    "Do you want to give someone you trust permission to get an EBT card to food shop for you using your SNAP benefits?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    
    ### assissting with application


   "Do you want to give us permission to contact a person or agency if we cannot reach you by phone?": {
        "value": "No",  
        "type": "Yes/No"
    },
    "Assisting Person or Agency Name": {"value": "abc", "type": "Text Field"},
    "Assisting Person or Agency Phone": {"value": "123-456-7890", "type": "Text Field"},
    "Assisting Person or Agency Address": {"value": "abc street", "type": "Text Field"},
    ###
    

    ## authorize to release information

    "Do you want to give a person or agency permission to speak with DTA and get relevant confidential information about your case?": {
        "value": "No",
        "type": "Yes/No"
    },
    "DTA Agent Name": {
        "value": "xyz",
        "type": "Text Field"
    },
    "DTA Agent Phone": {
        "value": "555-123-4567",
        "type": "Text Field"
    },
    "DTA Agent Address": {
        "value": "def street ",
        "type": "Text Field"
    },
    ### 

    
   # authorized representative for certification

    "Do you want to give an agency or someone you trust permission to sign forms, report changes, complete interviews, and talk about your case with us?": {
        "value": "No",
        "type": "Yes/No"
    },
    "Representative Name": {
        "value": "abc",
        "type": "Text Field"
    },
    "Representative Phone": {
        "value": "887-2232-3",
        "type": "Text Field"
    },
    "Representative FEIN": {
        "value": "82",
        "type": "Text Field"
    },
    ##

    # authorized representative for EBT transactions

    "Do you want to give someone you trust permission to get an EBT card to food shop for you using your SNAP benefits?": {
        "value": "No",
        "type": "Yes/No"
    },
    "EBT Representative Name": {
        "value": "xyz",
        "type": "Text Field"
    },
    "EBT Representative Phone": {
        "value": "555-987-6543",
        "type": "Text Field"
    },
    "EBT Representative Address": {
        "value": "abcdef street ",
        "type": "Text Field"
    },
    #
    
}
