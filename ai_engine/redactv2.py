import fitz
import json
import requests
import re
import logging
import google.generativeai as genai
import ast
from dotenv import load_dotenv
import hashlib
import os
import fitz
import random
from groq import Groq

load_dotenv()

API_KEY = os.getenv("API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

genai.configure(api_key=GOOGLE_API_KEY)


def add_txn(input_pdf, output_pdf, txn=None):
    doc = fitz.open(input_pdf)

    if txn:
        transaction_hash = f"Signed using hash: {txn}"
    else:
        transaction_hash = f"Signed using hash: {hashlib.sha256(str(random.random()).encode()).hexdigest()[:16]}"

    font_size = 8

    for page in doc:
        page_height = page.rect.height
        hash_height = font_size

        margin_x = 10
        margin_y = 10
        x = margin_x
        y = page_height - hash_height - margin_y

        page.insert_text((x, y), transaction_hash, fontsize=font_size, color=(0, 0, 0))

    doc.save(output_pdf)
    doc.close()

    print(f"Added transaction hash to PDF. Saved as {output_pdf}")


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    return text, doc


def extract_json(response_text):
    try:
        json_data = json.loads(response_text)
        return json_data
    except Exception:
        json_pattern = re.search(
            r"```(JSON|json)?\s*(.*?)```", response_text, re.DOTALL
        )
        if json_pattern:
            json_string = json_pattern.group(2)
            try:
                json_data = ast.literal_eval(json_string)
                return json_data
            except Exception as e:
                logging.error(f"Error decoding JSON: {str(e)}")
                return None
    return None


def get_gemini_response(prompt):
    try:
        client = Groq(api_key=GROQ_API_KEY)
        messages = [{"role": "user", "content": prompt}]
        response = client.chat.completions.create(
            messages=messages,
            model="llama-3.1-70b-versatile"
        )
        print("USING GROQ")
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error in GROQ API call: {str(e)}\nFallback to Gemini Pro")
        return get_gemini_response2(prompt)


def get_gemini_response2(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE",
            },
        ]
        response = model.generate_content(prompt, safety_settings=safety_settings)
        return response.text
    except Exception as e:
        logging.error(f"Error in Gemini API call: {str(e)}")
        return None


def find_sensitive_data(text, level):
    # print("Level: ", level, level==1, type(level), int(level)==1)
    if level == 1 or level == 2:
        prompt = (
            "You are a powerful text analysis tool designed to identify all important and sensitive numbers in text. "
            "Please analyze the following text and flag any instances of personally identifiable numbers including but not limited to the following types of numbers:\n\n"
            "1. Aadhaar Numbers: Detect any mention of Aadhaar numbers.\n"
            "2. PAN Numbers: Identify any PAN (Permanent Account Number) in the text.\n"
            "3. Passport Numbers: Flag any references to passport numbers.\n"
            "4. Driving License Numbers: Identify any driving license numbers mentioned.\n"
            "5. Employee ID Numbers: Detect any employee ID numbers.\n"
            "6. Bank Account Numbers: Identify any bank account numbers.\n"
            "7. Credit/Debit Card Numbers: Flag any credit or debit card numbers.\n"
            "8. Roll Numbers/Registration Numbers: Flag any roll numbers or registration numbers.\n"
            "9. Other Identification Numbers: Detect any other sensitive identification numbers that could be used to identify an individual or entity.\n\n"
            "Please list each identified number in the following JSON format:\n\n"
            "[\n"
            "    {\n"
            '        "type": "Aadhaar Number",\n'
            '        "text": "1234 5678 9101"\n'
            "    },\n"
            "    {\n"
            '        "type": "PAN Number",\n'
            '        "text": "ABCDE1234F"\n'
            "    }\n"
            "    // Add ALL identified items\n"
            "]\n\n"
            "Err on the side of caution - if in doubt, include it. However, do not flag single digits or common numeric sequences unless they are part of a sensitive number. Be very thorough and take into account cultural variations such as Indian identification numbers, etc."
            "Provide your comprehensive analysis based on these instructions. Only return the JSON. If at all no item is found, return an empty list.\n\n"
            f"Text to analyze:\n{text}"
        )

    elif level == 3:
        prompt = (
            "You are a highly advanced text analysis tool with the capability to detect and flag all instances of names and numbers within a text. Your task is to comprehensively analyze the text provided and identify every occurrence of any name or number, regardless of its format, context, or cultural origin. This includes but is not limited to the following categories:\n\n"
            "1. **Personal Identification Numbers**: Capture any numbers that could serve as personal identifiers, such as Aadhaar numbers, PAN numbers, Social Security numbers, National ID numbers, and others. Include associated names if present.\n"
            "2. **Financial Account Numbers**: Identify any financial-related numbers, including bank account numbers, credit card numbers, debit card numbers, IBAN, SWIFT codes, etc., and any associated names.\n"
            "3. **Government-Issued Document Numbers**: Detect numbers related to government-issued documents, such as passport numbers, driving license numbers, voter ID numbers, visa numbers, tax identification numbers, and more. Include any related names.\n"
            "4. **Employee and Student Identification Numbers**: Identify numbers related to employment or education, including employee ID numbers, student ID numbers, and any other institutional identification numbers, along with associated names.\n"
            "5. **Contact Numbers**: Capture phone numbers, mobile numbers, fax numbers, and other contact-related numbers.\n"
            "6. **Names on Resumes, CVs, or Job Applications**: Detect any names associated with resumes, CVs, cover letters, job applications, or related documents.\n"
            "7. **Healthcare and Insurance Document Numbers**: Identify numbers related to healthcare or insurance documents, including policy numbers, patient ID numbers, health insurance numbers, and associated names.\n"
            "8. **Vehicle and Property Registration Numbers**: Detect vehicle registration numbers, property deed numbers, or any other numbers related to ownership documents, along with any related names.\n"
            "9. **Any Other Names and Numbers**: Flag any other names and numbers that could be tied to an individual, entity, or important document, including but not limited to serial numbers, utility account numbers, tax records, and registration IDs.\n\n"
            "Your task is to list every identified name and number as a separate instance in the following JSON format:\n\n"
            "[\n"
            "    {\n"
            '        "type": "Name",\n'
            '        "text": "John Doe"\n'
            "    },\n"
            "    {\n"
            '        "type": "Number",\n'
            '        "text": "1234 5678 9101"\n'
            "    },\n"
            "    {\n"
            '        "type": "Number",\n'
            '        "text": "ABCDE1234F"\n'
            "    }\n"
            "    // Add ALL identified items\n"
            "]\n\n"
            "Err on the side of caution—if there is any doubt about whether something is a name or number, include it. Consider all variations in name and number formats across different cultures and document types. Your goal is to identify every possible name and number, leaving nothing unflagged.\n"
            "Return only the JSON output containing the flagged names and numbers.\n\n"
            f"Text to analyze:\n{text}"
        )

    else:
        prompt = (
            "You are a powerful text analysis tool designed to identify all potentially sensitive, personally identifiable, or traceable information in text, including conversations. "
            "Please analyze the following text and flag ALL instances of the following types of information:\n\n"
            "1. Names: Recognize full names of individuals, including but not limited to Indian names.\n"
            "2. Identification Numbers: Identify any numbers that could be identification numbers (e.g., Aadhaar, passport, driving license, employee ID, etc.).\n"
            "3. Addresses: Detect any references to addresses, including street names, city names, and postal codes.\n"
            "4. Phone Numbers: Find all phone numbers, including international formats.\n"
            "5. Email Addresses: Identify all email addresses.\n"
            "6. URLs: Detect all URLs and web addresses.\n"
            "7. Dates: Flag all dates, including birthdays and significant events.\n"
            "8. Financial Information: Identify bank account numbers, credit card numbers, and any monetary amounts.\n"
            "9. Organizations: Flag names of companies, institutions, or any other organizations.\n"
            "10. Locations: Identify any mentioned locations, including countries, states, cities, landmarks, etc.\n"
            "11. Proper Nouns: Flag all proper nouns not covered by the above categories.\n"
            "12. Conversations: Redact entire conversations that could involve personal or sensitive information. This includes dialogue, chat transcripts, or exchanges where individuals discuss matters that could reveal identity, preferences, or other personal details.\n"
            "13. Other Potential Identifiers: Flag any other information that could potentially be used to identify or trace an individual or entity.\n\n"
            "Please list each identified item in the following JSON format:\n\n"
            "[\n"
            "    {\n"
            '        "type": "Name",\n'
            '        "text": "John Doe"\n'
            "    },\n"
            "    {\n"
            '        "type": "URL",\n'
            '        "text": "https://example.com"\n'
            "    }\n"
            "    // Add ALL identified items\n"
            "]\n\n"
            "Err on the side of caution - if in doubt, include it. However, do not flag single letters or common words unless they are part of a larger sensitive item. Be very thorough and take into account cultural variations such as Indian names, Indian addresses, etc."
            "Provide your comprehensive analysis based on these instructions. Only return the JSON.\n\n"
            f"Text to analyze:\n{text}"
        )

    data = {"messages": [{"role": "user", "content": prompt}]}

    headers = {"Content-Type": "application/json", "apiKey": API_KEY}
    try:
        response = requests.post(
            "https://api.jabirproject.org/generate", json=data, headers=headers
        )
        if response.status_code == 200:
            entities_json = response.json().get("result", {}).get("content", "")
            print(entities_json)
            try:
                entities = json.loads(entities_json)
            except json.JSONDecodeError:
                logging.error("Error: Unable to parse JSON response from Jabir API")
                entities = None
        else:
            logging.error(
                f"Error in Jabir API call: {response.status_code} - {response.text}"
            )
            entities = None
    except Exception as e:
        logging.error(f"Error in Jabir API call: {e}")
        entities = None

    if entities is None:
        logging.info("Falling back to Gemini Pro API")
        # print("prompt: ", prompt)
        gemini_response = get_gemini_response(prompt)
        print(gemini_response)
        if gemini_response:
            try:
                entities = extract_json(gemini_response)
            except Exception:
                logging.error("Error: Unable to parse JSON response from Gemini API")
                entities = []
        else:
            logging.error("Both Jabir and Gemini API calls failed")
            entities = []

    sensitive_data = []
    for entity in entities:
        item_text = entity["text"]
        if len(item_text) <= 1:
            logging.warning(f"Skipping single character: {item_text}")
            continue
        if item_text.lower() in [
            "the",
            "a",
            "an",
            "and",
            "or",
            "but",
            "in",
            "on",
            "at",
            "to",
            "for",
        ]:
            logging.warning(f"Skipping common word: {item_text}")
            continue
        start = 0
        while True:
            start = text.find(item_text, start)
            if start == -1:
                break
            end = start + len(item_text)
            sensitive_data.append((item_text, start, end, entity["type"]))
            start = end

    url_pattern = re.compile(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    )
    identifier_pattern = re.compile(
        r"\b(?:(?:\d{6,})|(?=.*\d)(?=.*[A-Z])[A-Z\d]{8,})\b"
    )

    for match in url_pattern.finditer(text):
        sensitive_data.append((match.group(), match.start(), match.end(), "URL"))

    for match in identifier_pattern.finditer(text):
        sensitive_data.append(
            (match.group(), match.start(), match.end(), "Potential Identifier")
        )

    for data in sensitive_data:
        logging.debug(f"Identified sensitive data: {data}")

    return sensitive_data


def redact_text_in_pdf(pdf_doc, sensitive_data, level, mode):
    fill_colors = {"black": (0, 0, 0), "white": (1, 1, 1), "blur": (0.5, 0.5, 0.5)}

    for page_num in range(pdf_doc.page_count):
        page = pdf_doc[page_num]
        for data, start, end, data_type in sensitive_data:
            instances = page.search_for(data, quads=True)
            for inst in instances:
                logging.info(
                    f"Redacting full text on page {page_num + 1}: {data} ({data_type})"
                )
                page.add_redact_annot(inst, fill=fill_colors[mode])

            # words = data.split()
            # for word in words:
            #     word_instances = page.search_for(word, quads=True)
            #     for word_inst in word_instances:
            #         logging.info(
            #             f"Redacting word on page {page_num + 1}: {word} ({data_type})"
            #         )
            #         page.add_redact_annot(word_inst, fill=fill_colors[mode])

        if level < 2:
            page.apply_redactions(images=0, graphics=0)
        else:
            page.apply_redactions()


def custom_redact_text(pdf_doc, sensitive_data, level, mode):
    fill_colors = {"black": (0, 0, 0), "white": (1, 1, 1), "blur": (0.5, 0.5, 0.5)}

    for page_num in range(pdf_doc.page_count):
        page = pdf_doc[page_num]
        for data, start, end, data_type in sensitive_data:
            instances = page.search_for(data, quads=True)
            for inst in instances:
                logging.info(
                    f"Redacting full text on page {page_num + 1}: {data} ({data_type})"
                )
                page.add_redact_annot(inst, fill=fill_colors[mode])

        if level < 2:
            page.apply_redactions(images=0, graphics=0)
        else:
            page.apply_redactions()


def redact_images_in_pdf(pdf_doc, mode):
    fill_colors = {"black": (0, 0, 0), "white": (1, 1, 1), "blur": (0.5, 0.5, 0.5)}

    for page_num in range(pdf_doc.page_count):
        page = pdf_doc[page_num]
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            rect = page.get_image_bbox(img)
            logging.info(f"Redacting image on page {page_num + 1}")
            page.add_redact_annot(rect, fill=fill_colors[mode])

        page.apply_redactions()


def save_redacted_pdf(pdf_doc, output_path):
    pdf_doc.save(output_path, garbage=4, deflate=True, clean=True)
    pdf_doc.close()


def get_custom_sensitive_data(text, user_prompt):
    prompt = (
        "You are an advanced, highly adaptable text analysis tool. "
        "Your task is to analyze the following text based on the user's custom prompt. "
        "This tool is culturally aware and capable of understanding diverse proper nouns, "
        "including names, addresses, and unique regional terms from various cultural contexts, such as Indian, East Asian, Middle Eastern, African, and Western names. "
        "The analysis should be precise, handling subtle differences in syntax and structure common in various languages and dialects. "
        "Ensure flexibility in recognizing variations in spelling, transliteration, and formatting of culturally specific information.\n\n"
        f"User Prompt: {user_prompt}\n\n"
        "Your task is to identify and flag all items that match the user's criteria in a manner that respects regional naming conventions, abbreviations, and format differences. "
        "Be thorough, and do not deviate from the user's prompt, but ensure the analysis accounts for a wide range of global linguistic patterns and naming conventions.\n\n"
        "Return all identified items in the following JSON format:\n\n"
        "[\n"
        "    {\n"
        '        "type": "Name",\n'
        '        "text": "Dupindar Singh"\n'
        "    },\n"
        "    {\n"
        '        "type": "Address",\n'
        '        "text": "123, M.G. Road, Bengaluru, Karnataka, India"\n'
        "    }\n"
        "    // Add ALL identified items\n"
        "]\n\n"
        "Ensure that you maintain this exact format at ALL COSTS.\n\n"
        f"Text to analyze:\n{text}"
    )
    # print("Prompt: ", prompt)
    try:
        gemini_response = get_gemini_response(prompt)
        if gemini_response:
            print(gemini_response)
            try:
                entities = extract_json(gemini_response)
            except Exception:
                logging.error("Error: Unable to parse JSON response from Gemini API")
                return []
        else:
            logging.error("Error: No response from Gemini API")
            return []
    except Exception as e:
        logging.error(f"Error in Gemini API call: {e}")
        return []

    sensitive_data = []
    for entity in entities:
        item_text = entity["text"]
        if len(item_text) <= 1:
            logging.warning(f"Skipping single character: {item_text}")
            continue
        if item_text.lower() in [
            "the",
            "a",
            "an",
            "and",
            "or",
            "but",
            "in",
            "on",
            "at",
            "to",
            "for",
        ]:
            logging.warning(f"Skipping common word: {item_text}")
            continue
        start = 0
        while True:
            start = text.find(item_text, start)
            if start == -1:
                break
            end = start + len(item_text)
            sensitive_data.append((item_text, start, end, entity["type"]))
            start = end

    for data in sensitive_data:
        logging.debug(f"Identified sensitive data: {data}")

    return sensitive_data


def get_sensitive(input_pdf, level):
    text, pdf_doc = extract_text_from_pdf(input_pdf)
    sensitive_data = find_sensitive_data(text, level)
    return sensitive_data


def get_sensitive_custom(input_pdf, prompt):
    text, pdf_doc = extract_text_from_pdf(input_pdf)
    sensitive_data = get_custom_sensitive_data(text, prompt)
    return sensitive_data


def custom_redactv2(input_pdf, sensitive_data, output_pdf, image, mode):
    text, pdf_doc = extract_text_from_pdf(input_pdf)
    level = 4 if image else 1
    custom_redact_text(pdf_doc, sensitive_data, level, mode)
    if image:
        redact_images_in_pdf(pdf_doc, mode)
    save_redacted_pdf(pdf_doc, output_pdf)
    logging.info(f"Redacted PDF saved as {output_pdf}")


def redactv2(input_pdf, sensitive_data, output_pdf, level, mode):
    text, pdf_doc = extract_text_from_pdf(input_pdf)
    redact_text_in_pdf(pdf_doc, sensitive_data, level, mode)
    if level > 1:
        redact_images_in_pdf(pdf_doc, mode)
    save_redacted_pdf(pdf_doc, output_pdf)
    logging.info(f"Redacted PDF saved as {output_pdf}")


def get_cat(input_pdf):
    text, pdf_doc = extract_text_from_pdf(input_pdf)
    prompt = (
        "You are a powerful text analysis tool designed to identify the type of document based on its content. "
        "Please analyze the following text and determine the category of the document. "
        "You should consider the context, language, and structure of the text to make an accurate assessment. "
        "Provide your analysis based on the following categories:\n\n"
        "1. **Identification Document**: This category includes documents such as Aadhaar cards, PAN cards, driver's licenses, passports, and other forms of identification.\n"
        "2. **Financial Document**: This category includes bank statements, tax returns, invoices, receipts, and other financial records.\n"
        "3. **Legal Document**: This category includes contracts, agreements, court orders, and other legal documents.\n"
        "4. **Medical Document**: This category includes medical reports, prescriptions, insurance claims, and other healthcare-related documents.\n"
        "5. **Educational Document**: This category includes transcripts, diplomas, certificates, and other educational records.\n"
        "6. **Personal Communication**: This category includes emails, letters, messages, and other personal correspondence.\n"
        "7. **Business Document**: This category includes business plans, proposals, reports, and other corporate documents.\n"
        "8. **Other Document**: This category includes any document that does not fit into the above categories.\n\n"
        "Please provide your analysis based on these instructions. Only return the category of the document in the following JSON format:\n\n"
        "{\n"
        '    "category": "Financial Document"\n'
        "}\n\n"
        "Ensure that you maintain this exact format at ALL COSTS.\n\n"
        f"Text to analyze:\n{text}"
    )

    response = get_gemini_response(prompt)
    try:
        response_json = extract_json(response)
        category = response_json[0]["category"]
    except Exception:
        logging.error("Error: Unable to parse JSON response from Gemini API")
        category = "Other Document"

    return category


def annotate_sensitive_data_in_pdf(pdf_doc, sensitive_data):
    for page_num in range(pdf_doc.page_count):
        page = pdf_doc[page_num]
        page_text = page.get_text()

        for entity in sensitive_data:
            entity_text = entity[0]
            entity_type = entity[3]

            instances = page.search_for(entity_text)
            for inst in instances:
                logging.info(
                    f"Annotating '{entity_text}' as {entity_type} on page {page_num + 1}"
                )

                highlight = page.add_highlight_annot(inst)

                highlight.set_info(
                    title="Sensitive Data",
                    content=f"Type: {entity_type}\nText: {entity_text}",
                )


def save_annotated_pdf(pdf_doc, output_path):
    pdf_doc.save(output_path, garbage=4, deflate=True, clean=True)
    pdf_doc.close()


def annotate_pdf(input_pdf, sensitive_data, output_pdf):
    text, pdf_doc = extract_text_from_pdf(input_pdf)
    annotate_sensitive_data_in_pdf(pdf_doc, sensitive_data)
    save_annotated_pdf(pdf_doc, output_pdf)
    logging.info(f"Annotated PDF saved as {output_pdf}")


if __name__ == "__main__":
    input_pdf = "input5.pdf"
    output_pdf = "output5.pdf"
    redactv2(input_pdf, output_pdf)
