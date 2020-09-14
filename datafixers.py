  # -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:09:24 2020

@author: Heeje Cho

Module contains several methods for fixing columns and rows that are present in dataframes from databases
- state_abbr
    inputs: dataframe, [column1,column2]
    output: dataframe
    *this looks at which columsn to abbreviate states for
- replace_none
    inputs: dataframe
    output: dataframe
    *this replaces all np.nan values with None values
"""

def state_code(full_state):

    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'American Samoa': 'AS',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Guam': 'GU',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Northern Mariana Islands':'MP',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Puerto Rico': 'PR',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virgin Islands': 'VI',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'
        }
    us_state_full = list(us_state_abbrev.keys())
    us_state_abv = list(us_state_abbrev.values())

    if full_state in us_state_full:
        code = us_state_abbrev[full_state]
    elif full_state in us_state_abv:
        code = full_state
    else:
        code = ''

    return code



def state_to_abbr(dataframe, columns):

    df = dataframe

    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'American Samoa': 'AS',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Guam': 'GU',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Northern Mariana Islands':'MP',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Puerto Rico': 'PR',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virgin Islands': 'VI',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'
    }
    us_state_full = list(us_state_abbrev.keys())
    us_state_abv = list(us_state_abbrev.values())

    for column in columns:
        for i, row in df.iterrows():
            state = row[column]

            if state in us_state_abv:
                abbrev = state
            if state in us_state_full:
                abbrev = us_state_abbrev[state]
            else:
                abbrev = ''
            
            df.loc[i,column] = abbrev

    return df





def state_to_full(dataframe, columns):

    df = dataframe

    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'American Samoa': 'AS',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Guam': 'GU',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Northern Mariana Islands':'MP',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Puerto Rico': 'PR',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virgin Islands': 'VI',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'
    }

    us_state_fullname = {v:k for k, v in us_state_abbrev.items()}

    us_state_full = list(us_state_abbrev.values())
    us_state_abv = list(us_state_abbrev.keys())

    for column in columns:
        for i, row in df.iterrows():
            state = row[column]

            if state in us_state_full:
                full = state
            if state in us_state_abv:
                full = us_state_fullname[state]
            else:
                full = ''
            
            df.loc[i,column] = full

    return df





#this uses azure's Cognitive Services Instance LiquidAI to extract texts from images (OCR)
def ocr_text(pdf_path):
    import sys
    import os
    import io
    import time
    import pdf2image
    from pdf2image import convert_from_path
    import requests
    import shutil

    pdfs = convert_from_path(pdf_path)
    pdf = pdfs[0]

    os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY'] = 'ffecaf88ca3b468fb3ff1bf53e3f4043'
    os.environ['COMPUTER_VISION_ENDPOINT'] = 'https://liquidai.cognitiveservices.azure.com/'
    
    missing_env = False
    # Add your Computer Vision subscription key and endpoint to your environment variables.
    if 'COMPUTER_VISION_ENDPOINT' in os.environ:
            endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
    else:
        print("From Azure Cogntivie Service, retrieve your endpoint and subscription key.")
        print("\nSet the COMPUTER_VISION_ENDPOINT environment variable, such as \"https://westus2.api.cognitive.microsoft.com\".\n")
        missing_env = True

    if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
        subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
    else:
        print("From Azure Cogntivie Service, retrieve your endpoint and subscription key.")
        print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable, such as \"1234567890abcdef1234567890abcdef\".\n")
        missing_env = True

    if missing_env:
        print("**Restart your shell or IDE for changes to take effect.**")
        sys.exit()
    
    text_recognition_url = endpoint + "/vision/v3.0/read/analyze"
    
    imgByteArr = io.BytesIO()
    pdf.save(imgByteArr, format='JPEG')
    pdfByteArr = imgByteArr.getvalue()


    # Read the image into a byte array
    #image_data = open(image_path, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/octet-stream'}
    response = requests.post(
        text_recognition_url, headers = headers, data = pdfByteArr)
    response.raise_for_status()

    # Extracting text requires two API calls: One call to submit the
    # image for processing, the other to retrieve the text found in the image.
    # Holds the URI used to retrieve the recognized text.
    #operation_url = response.headers["Operation-Location"]

    # The recognized text isn't immediately available, so poll to wait for completion.
    analysis = {}
    poll = True
    while (poll):
        response_final = requests.get(
            response.headers["Operation-Location"], headers=headers)
        analysis = response_final.json()
        #print(json.dumps(analysis, indent=4))
        time.sleep(1)
        if ("analyzeResult" in analysis):
            poll = False
        if ("status" in analysis and analysis['status'] == 'failed'):
            poll = False
    #os.chdir('N:\DataEng\Scripts\python\Accessioning QC\Tests')
    #with open('test2.json', 'w') as json_file:
        #json.dump(analysis, json_file)
    #polygons = []
    text = []
    if ("analyzeResult" in analysis):
        # Extract the recognized text, with bounding boxes.
        #polygons = [(line["boundingBox"], line["text"])
                    #for line in analysis["analyzeResult"]["readResults"][0]["lines"]]
        text = [(line['text'])
            for line in analysis['analyzeResult']['readResults'][0]['lines']]
    extracted = text

    return extracted