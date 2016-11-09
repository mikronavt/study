# This is a Python comment.
#
# You aren't meant to understand any of this code yet, but try
# reading through it anyway. Do you see anything that looks familiar?
#
# When you've read through it, try to predict what will happen
# when you press the Test Run button. Once you have a guess,
# press Test Run

def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
    <div class="concept">
        <div class="concept-title">
            ''' + concept_title
    html_text_2 = '''
        </div>
        <div class="concept-description">
            ''' + concept_description
    html_text_3 = '''
        </div>
    </div>'''

    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

first_concept = 'CSS'
first_description = 'CSS stands for Cascading Style Sheets.'

second_concept = 'Computers are Stupid'
second_description = 'Computers do EXACTLY what you tell them. Tiny typos can cause big errors.'

print(generate_concept_HTML(first_concept, first_description))
print(generate_concept_HTML(second_concept, second_description))

# Click the "Test Run" button below!