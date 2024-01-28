import requests
from bs4 import BeautifulSoup

url = 'https://www.veethi.com/places/tamil-nadu-state-24.htm'
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text

    # Parse HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove scripts and styles
    for script_or_style in soup(['script', 'style']):
        script_or_style.decompose()

    # Remove all links, keeping the link text
    for link in soup.find_all('a'):
        link.replace_with(link.text)

    # Remove elements with the "gallery" class
    for gallery_element in soup.find_all(class_='gallery'):
        gallery_element.decompose()

    # Select elements with specific classes
    allowed_classes = ['main-left', 'additional-info']
    filtered_elements = soup.find_all(class_=allowed_classes)

    # Create a new HTML document with the selected elements
    filtered_html = '<html><head></head><body>{}</body></html>'.format(''.join(map(str, filtered_elements)))

    # Save the filtered HTML to a file
    with open('filtered_page.html', 'w', encoding='utf-8') as file:
        file.write(filtered_html)

    print('Filtered HTML saved to filtered_page.html')
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
