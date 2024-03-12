
def parse_name(full_name):
    """
    Parses a full name into first, middle, and last names.
    Parameters:
    - full_name (str): The full name to be parsed.
    Returns:
    - dict: A dictionary with keys 'first', 'middle', and 'last' for the corresponding parts of the name.
            Parts of the name that are not present are excluded from the dictionary.
    """
    # Split the full name into parts based on spaces
    name_parts = full_name.strip().split()
    # Create an empty dictionary to store the name parts
    name_dict = {}
    # Assign the first name part
    if len(name_parts) > 0:
        name_dict['first'] = name_parts[0]
    # Assign the last name part if there are more than one part
    if len(name_parts) > 1:
        name_dict['last'] = name_parts[-1]
    # Assign the middle name part(s) if there are more than two parts
    if len(name_parts) > 2:
        name_dict['middle'] = ' '.join(name_parts[1:-1])
    return name_dict


def map_fields(json_data):
    # Mapping of JSON keys to the form field IDs
    key_to_field_id = {
        "Name": "First Name_pg1",  # Assuming "Name" maps to "First Name" for simplicity
        "DOB": "Date of Birth",
        "Sex": None,  # No direct field for Sex, ignoring
        "Address": "Home Address_pg1",
        "Mailing" : "Mailing Address if different_pg1",
        "Are you homeless_No?" : "Are you homeless_No?",
        "Are you homeless_Yes?" : "Are you homeless_Yes?",
        

        "If you do not want DTA to text you, please check this box_Yes":"If you do not want DTA to text you, please check this box_Yes",
        "If you do not want DTA to text you, please check this box_No":"If you do not want DTA to text you, please check this box_No",
        "Language / Idioma": "What language do you prefer to speak",
        "Phone number / Número de teléfono": "Phone Number",
        "Date" : "Date",
        "Social Security Number (If you are a U.S citizen) / Número de Seguro Social (Si eres ciudadano americano)": "Social Security Number",
        "Do you have any of these programs?": "Has anyone recieved SNAP benefits outside Massachusetts within the past 30 days? If yes, who?",
        "Can you provide your signature? /¿Podrías darnos tu firma de autorización?": "Signature",
        "Total number in household.": "Other:",  # Using "Other:" as a generic field for lack of a better match
        "Gross Earnings for Last 4 Weeks": "Gross amount Row1_pg4",  # Assuming mapping to a gross amount field
        "Income type": "Self-Employment1_pg4",
        "Is the household responsible to pay shelter costs?_Yes": "Shelter costs_Yes",  # Assuming rent as a type of shelter cost
        "Is the household responsible to pay shelter costs?_No": "Shelter costs_No",  # Assuming rent as a type of shelter cost
        "Type of shelter costs": "Property Taxes_pg5",
        "Shelter amount":"Other type of shelter cost amount",
        "Is anyone responsible to pay for adult or child care costs?_Yes": "Is anyone responsible to pay for adult or child care costs?_Yes",  # Assuming mapping to a dependent care cost
        "Is anyone responsible to pay for adult or child care costs?_No": "Is anyone responsible to pay for adult or child care costs?_No",  # Assuming mapping to a dependent care cost
        "Frequency of payment": "Row1_frequency_biweekly_pg6",
        "Do you want to give us permission to contact a person or agency if we cannot reach you by phone?_Yes*": "Do you want to give us permission to contact a person or agency if we cannot reach you by phone?_Yes*",
        "Do you want to give us permission to contact a person or agency if we cannot reach you by phone?_No*": "Do you want to give us permission to contact a person or agency if we cannot reach you by phone?_No*",
        "Assisting with Applicatioin - Name of Person or Agency":"Assisting with Applicatioin - Name of Person or Agency",
        "Assisting with Application - Phone Number":"Assisting with Application - Phone Number",
        "Assisting with Application - Address":"Assisting with Application - Address",
        "Email address / Dirección de correo electrónico": None,  # No direct field for email
        "Are you a U.S. Citizen?_Yes": "Are you a U.S. Citizen?_Yes",  # No direct field for citizenship status
        "Are you a U.S. Citizen?_No": "Are you a U.S. Citizen?_No",  # No direct field for citizenship status
        "(SNAP Eligibility) Select one of the following / Selecciona una de las siguientes opciones": None,  # No direct field for SNAP eligibility details
        "Are you homeless? / ¿No tienes hogar?": None,   # No direct field for homelessness
        "If you do not want DTA to text you, please check this box_Yes":"If you do not want DTA to text you, please check this box_Yes",
        "If you do not want DTA to text you, please check this box_No":"If you do not want DTA to text you, please check this box_No",
        
        "Do you have a Massachusetts Electronic Benefits Transfer (EBT) card?_Yes": "Do you have a Massachusetts Electronic Benefits Transfer (EBT) card?_Yes",  # No direct field for EBT card status
        "Do you have a Massachusetts Electronic Benefits Transfer (EBT) card?_No":"Do you have a Massachusetts Electronic Benefits Transfer (EBT) card?_No",
        "Are you a person with a disability?_physical": "Are you a person with a disability?_Physical",  # No direct field for disability status
        "Are you a person with a disability?_Intellectual/Cognitive": "Are you a person with a disability?_Intellectual/Cognitive",  # No direct field for disability status
        "If yes, please check off your impairment type(s)_Hearing": "If yes, please check off your impairment type(s)_Hearing",
        "If yes, please check off your impairment type(s)_Emotional/Mental Health":"If yes, please check off your impairment type(s)_Emotional/Mental Health",
        "If yes, please check off your impairment type(s)_Visual":"If yes, please check off your impairment type(s)_Visual",    
        "If yes, please check off your impairment type(s)_Other": "If yes, please check off your impairment type(s)_Other",
        "What is your preferred method of communication?_InPerson": "What is your preferred method of communication?_InPerson",  # No direct field
        "What is your preferred method of communication?_Telephone":"What is your preferred method of communication?_Telephone",
        "What is your preferred method of communication?_Video Relay Services VRS": "What is your preferred method of communication?_Video Relay Services VRS",
        "VRS Phone Number":"VRS Phone Number",
        "Has Massachusetts certified that you have a disability?_Yes": "Has Massachusetts certified that you have a disability?_Yes",  # No direct field
        "Has Massachusetts certified that you have a disability?_No": "Has Massachusetts certified that you have a disability?_No",  # No direct field
        "Are you a U.S. Citizen?_Yes": "Are you a U.S. Citizen?_Yes",  # No direct field for living status
        "Are you a U.S. Citizen?_No": "Are you a U.S. Citizen?_No",  # No direct field for living status
        "Do you live with other people?_No":"Do you live with other people?_No",
        "Do you live with other people?_Yes":"Do you live with other people?_Yes",
        "List the members of your household.": "Household member name1",  # Assuming the first member as an example
        "Has anyone worked in the last 60 days?_Yes": "Has anyone worked in the last 60 days?_Yes",  # No direct field for employment history
        "Has anyone worked in the last 60 days?_No": "Has anyone worked in the last 60 days?_No",  # No direct field for employment history
        "Employer name or information": "Employer1",  # Mapping to the first employer field
        "Does anyone receive any other type of income such as Unemployment Compensation, Child Support, Social Security, SSI, Workers’ Compensation, Veterans’ Benefits, Pensions or Rental Income?_Yes": "Does anyone receive any other type of income such as Unemployment Compensation, Child Support, Social Security, SSI, Workers’ Compensation, Veterans’ Benefits, Pensions or Rental Income?_Yes",  # No direct field, but could be inferred
        "Does anyone receive any other type of income such as Unemployment Compensation, Child Support, Social Security, SSI, Workers’ Compensation, Veterans’ Benefits, Pensions or Rental Income?_No": "Does anyone receive any other type of income such as Unemployment Compensation, Child Support, Social Security, SSI, Workers’ Compensation, Veterans’ Benefits, Pensions or Rental Income?_No",  # No direct field, but could be inferred
        "Income Type": "Other Income type Row1_pg4",  # Additional income types
        "Is the household responsible to pay utility costs separate from shelter costs?_Yes": "Utility costs_Yes",  # No direct field for utility costs
        "Is the household responsible to pay utility costs separate from shelter costs?_No": "Utility costs_No",  # No direct field for utility costs
        "Utility costs detailed information": None,  # No direct field for detailed utility costs
        "Select the utility costs you pay": "Heat oil gas electricity or propane etc",  # No direct field for selecting utility costs
        "Electricity for an air conditioner in the summer":"Electricity for an air conditioner in the summer",
        "A fee to use an air conditioner in the summer":"A fee to use an air conditioner in the summer",
        "Phone or cell phone service including prepaid":"Phone or cell phone service including prepaid",
        
        
        
        
        "Name of child/dependent": "Row1_name of dependent_pg6",  # Mapping to the name of the first dependent
        "Amount paid": "Row1_amount_pg6",  # Assuming mapping to the amount paid for the first dependent
        "Does anyone who is at least 60 years old and/or disabled have out-of-pocket medical expenses?_Yes": "Does anyone who is at least 60 years old and/or disabled have out-of-pocket medical expenses?_Yes",  # No direct field
        "Does anyone who is at least 60 years old and/or disabled have out-of-pocket medical expenses?_No": "Does anyone who is at least 60 years old and/or disabled have out-of-pocket medical expenses?_No",  # No direct field
        "Name of the person": "Name1",  # Assuming mapping to a generic name field for medical expenses
        "Total cost per month": "Total cost per month1",  # Assuming mapping to total cost for medical expenses
        "Does anyone travel to and/or from medical care such as a pharmacy, doctor, therapist, etc.)?_Yes": "Does anyone travel to and/or from medical care such as a pharmacy, doctor, therapist, etc.)?_Yes",  # No direct field for travel to medical care
        "Address or medical provider": "Address of Medical Provider1",  # Mapping to the first medical provider address
        "Number of cars TO":"To1",
        "Number of cars FROM":"From1",
        "Cost for Parking Public Transportation Taxi Cab Shuttle etc1":"Cost for Parking Public Transportation Taxi Cab Shuttle etc1",
        "Is anyone in a training program at least 80 hours per month?_Yes": "Is anyone in a training program at least 80 hours per month?_Yes",  # No direct field for training program participation
        "Is anyone in a training program at least 80 hours per month?_No": "Is anyone in a training program at least 80 hours per month?_No",  # No direct field for training program participation
        "If yes, provide the full name":"If yes, who?1",
        "Is anyone working in exchange for goods and services (in-kind work)?_Yes": "Is anyone working in exchange for goods and services (in-kind work)?_Yes",  # No direct field for in-kind work
        "Is anyone working in exchange for goods and services (in-kind work)?_No": "Is anyone working in exchange for goods and services (in-kind work)?_No",  # No direct field for in-kind work
        "If yes, provide the full name.": "If yes, who?3",
        "Is anyone doing an unpaid internship?_Yes": "Is anyone doing an unpaid internship?_Yes",  # No direct field for internships
        "Is anyone doing an unpaid internship?_No": "Is anyone doing an unpaid internship?_No",  # No direct field for internships
        "Is anyone volunteering?_Yes": "Is anyone volunteering?_Yes",  # No direct field for volunteering
        "Is anyone volunteering?_No": "Is anyone volunteering?_No",  # No direct field for volunteering
        "Who is volunteering?" : "If yes, who?7",
        "Has anyone received SNAP benefits outside of MA within past 30 days?_Yes":"Has anyone received SNAP benefits outside of MA within past 30 days?_Yes",
        "Has anyone received SNAP benefits outside of MA within past 30 days?_No": "Has anyone received SNAP benefits outside of MA within past 30 days?_No",  # Clarifying mapping
        "Do you want to give a person or agency permission to speak with DTA and get relevant confidential information about your case?_Yes*": "Do you want to give a person or agency permission to speak with DTA and get relevant confidential information about your case?_Yes*",
        "Do you want to give a person or agency permission to speak with DTA and get relevant confidential information about your case?_No*": "Do you want to give a person or agency permission to speak with DTA and get relevant confidential information about your case?_No*",
         "If yes, provide the name of the person or the Agency. ": "Authorization to Release Information - Name of Person or Agency",
         "Authorizaton to Release Information - Phone Number":"Authorizaton to Release Information - Phone Number",
        "Authorization to Release Information - Address": "Authorization to Release Information - Address",  # Mapping to a field for an address related to assistance
        "Authorized Representative for Certification - Name of Person or Agency": "Authorized Representative for Certification - Name of Person or Agency",  # Correcting a typo in the original mapping
        "Authorized Representative for Certification - Phone Number": "Authorized Representative for Certification - Phone Number",  # Mapping to a phone number related to assistance
        "Federal Employer ID Number - Agency Only": "Federal Employer ID Number - Agency Only",  # Direct mapping
        "If yes, provide the full name of the person.": "Authorized Rep for EBT Transactions - Name of Person",  # Clarifying mapping for authorized representative
"Do you want to give someone you trust permission to get an EBT card to food shop for you using your SNAP benefits?*_Yes":"Do you want to give someone you trust permission to get an EBT card to food shop for you using your SNAP benefits?*_Yes",
"Do you want to give someone you trust permission to get an EBT card to food shop for you using your SNAP benefits?*_No":"Do you want to give someone you trust permission to get an EBT card to food shop for you using your SNAP benefits?*_No",
        "Authorized Rep for EBT Transactions - Name of Person":"Authorized Rep for EBT Transactions - Name of Person",
        "Authorized Rep for EBT Transactions - Phone Number":"Authorized Rep for EBT Transactions - Phone Number",
    }

    # Mapping process
    mapped_data = {}
    for key, value in json_data.items():
        if key in key_to_field_id and key_to_field_id[key] is not None:
            mapped_data[key_to_field_id[key]] = value

    return mapped_data
