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





#this returns patient pdf from azure's blob instance as pdf (filewrite) object
def azure_patient_report(connection_string, accession_id):
    import os, uuid
    import PyPDF2
    from io import BytesIO
    from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, StorageStreamDownloader, __version__

    connect_str = connection_string

    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(accession_id)

    pt_report = 'default'
    filewriter = None

    for blob in container_client.list_blobs():
        if 'patient-reports' in blob.name:
            pt_report = blob.name
        
    if pt_report != 'default':
        blob_client = container_client.get_blob_client(pt_report)

        streamdownloader = blob_client.download_blob()

        stream = BytesIO()
        streamdownloader.download_to_stream(stream)

        filewriter = PyPDF2.PdfFileWriter()
        filereader = PyPDF2.PdfFileReader(stream)

        filewriter.appendPagesFromReader(filereader)
    
    return filewriter


def random_text():
    import os
    import biocept
    
    dir_path = os.path.dirname(biocept.__file__)
    base = r'pdfs\random.txt'
    path = os.path.join(dir_path,base)

    f = open(path,'r')

    print(f.read())




def florida_report_fill(patient_dict, coordinates_dict):
    import os
    import biocept
    import pdfrw
    import PyPDF2
    from io import BytesIO
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter

    dir_path = os.path.dirname(biocept.__file__)
    base_path = r'pdfs\florida_disease_report.pdf'
    form_path = os.path.join(dir_path,base_path)

    stream = BytesIO()
    lname = patient_dict['lastname']

    width, height = letter
    c = canvas.Canvas(stream)
    c.setFont('Times-Roman', 10)
    c.setPageSize([width,height])

    c.drawString(coordinates_dict['ssn'][0],coordinates_dict['ssn'][1], patient_dict['ssn'])
    c.drawString(coordinates_dict['mrn'][0],coordinates_dict['mrn'][1], patient_dict['mrn'])
    c.drawString(coordinates_dict['lastname'][0],coordinates_dict['lastname'][1], patient_dict['lastname'])
    c.drawString(coordinates_dict['receiveddate'][0], coordinates_dict['receiveddate'][1], patient_dict['receiveddate'])
    c.drawString(coordinates_dict['signeddate'][0], coordinates_dict['signeddate'][1], patient_dict['signeddate'])
    c.drawString(coordinates_dict['firstname'][0], coordinates_dict['firstname'][1], patient_dict['firstname'])
    if patient_dict['sex'] == 'M':
        c.drawString(coordinates_dict['male'][0],coordinates_dict['male'][1], 'X')
    elif patient_dict['sex'] == 'F':
        c.drawString(coordinates_dict['female'][0],coordinates_dict['female'][1], 'X')
    else:
        c.drawString(coordinates_dict['genunkn'][0], coordinates_dict['genunkn'][1], 'X')
    c.drawString(coordinates_dict['dob'][0], coordinates_dict['dob'][1], patient_dict['dob'])
    if patient_dict['race'] == 'W':
        c.drawString(coordinates_dict['White'][0],coordinates_dict['White'][1],'X')
    elif patient_dict['race'] == 'B':
        c.drawString(coordinates_dict['Black'][0],coordinates_dict['Black'][1],'X')
    elif patient_dict['race'] == 'A':
        c.drawString(coordinates_dict['Asian'][0], coordinates_dict['Asian'][1], 'X')
    elif patient_dict['race'] == 'I':
        c.drawString(coordinates_dict['NativeAmerican'][0], coordinates_dict['NativeAmerican'][1], 'X')
    elif patient_dict['race'] == 'P':
        c.drawString(coordinates_dict['Asian'][0], coordinates_dict['Asian'][1], 'X')
    elif patient_dict['race'] == 'O':
        c.drawString(coordinates_dict['Other'][0], coordinates_dict['Other'][1], 'X')
    else:
        c.drawString(coordinates_dict['UnknownRace'][0], coordinates_dict['UnknownRace'][1], 'X')
    if patient_dict['ethnicity'] == 'H':
        c.drawString(coordinates_dict['Hispanic'][0], coordinates_dict['Hispanic'][1], 'X')
    elif patient_dict['ethnicity'] == 'NH':
        c.drawString(coordinates_dict['NonHispanic'][0], coordinates_dict['NonHispanic'][1], 'X')
    else:
        c.drawString(coordinates_dict['UnknownEth'][0], coordinates_dict['UnknownEth'][1], 'X')
    c.drawString(coordinates_dict['Address'][0], coordinates_dict['Address'][1], patient_dict['address'])
    c.drawString(coordinates_dict['ZIP'][0], coordinates_dict['ZIP'][1], patient_dict['ZIP'])
    c.drawString(coordinates_dict['City'][0], coordinates_dict['City'][1], patient_dict['City'])
    c.drawString(coordinates_dict['State'][0], coordinates_dict['State'][1], 'FL')
    c.drawString(coordinates_dict['Phone'][0], coordinates_dict['Phone'][1], patient_dict['Phone'])
    if patient_dict['sex'] == 'F':
        if patient_dict['Pregnant'] == 'Y':
            c.drawString(coordinates_dict['PregYes'][0], coordinates_dict['PregYes'][1], 'X')
        elif patient_dict['Pregnant'] == 'N':
            c.drawString(coordinates_dict['PregNo'][0], coordinates_dict['PregNo'][1], 'X')
        else:
            c.drawString(coordinates_dict['PregUnk'][0], coordinates_dict['PregUnk'][1], 'X')
    c.drawString(coordinates_dict['Physician'][0], coordinates_dict['Physician'][1], patient_dict['Physician'])
    c.drawString(coordinates_dict['client_add'][0],coordinates_dict['client_add'][1], patient_dict['client_add'])
    c.drawString(coordinates_dict['client_city'][0], coordinates_dict['client_city'][1], patient_dict['client_city'])
    c.drawString(coordinates_dict['client_phone'][0], coordinates_dict['client_phone'][1], patient_dict['client_phone'])
    c.drawString(coordinates_dict['client_state'][0], coordinates_dict['client_state'][1], patient_dict['client_state'])
    c.drawString(coordinates_dict['client_zip'][0], coordinates_dict['client_zip'][1], patient_dict['client_zip'])
    c.drawString(coordinates_dict['comments'][0], coordinates_dict['comments'][1], patient_dict['comments'])
    c.drawString(coordinates_dict['diedunk'][0], coordinates_dict['diedunk'][1], 'X')
    c.drawString(coordinates_dict['hospunk'][0], coordinates_dict['hospunk'][1], 'X')
    c.drawString(coordinates_dict['treatedunk'][0], coordinates_dict['treatedunk'][1], 'X')
    c.drawString(coordinates_dict['labtestyes'][0], coordinates_dict['labtestyes'][1], 'X')
    c.drawString(6.61*72, 1.83*72, 'X')
    c.save()
    
    '''#pdfrw
    form = pdfrw.PdfReader(form_path)
    markdown = pdfrw.PdfReader()
    markdown = markdown.load_stream_objects(stream)
    mark = markdown.pages[0]

    for page in range(len(form.pages)):
        merger = pdfrw.PageMerge(form.pages[page])
        merger.add(mark).render()
    
    pdf_writer = pdfrw.PdfWriter()

    for page in range(len(form.pages)):
        pdf_writer.addpage(form.pages[page])


    '''
    # PyPDF2
    form = PyPDF2.PdfFileReader(form_path)
    markdown = PyPDF2.PdfFileReader(stream)

    pdf_writer = PyPDF2.PdfFileWriter()

    for page in range(form.getNumPages()):
        form_page = form.getPage(page)
        form_page.mergePage(markdown.getPage(0))
        pdf_writer.addPage(form_page)

    return pdf_writer