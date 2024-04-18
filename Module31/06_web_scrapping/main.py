import re
import requests

if __name__ == '__main__':
    link_text = requests.get('http://www.columbia.edu/~fdc/sample.html').text
    # link_text = requests.get('https://www.javatpoint.com/what-is-a-webpage').text

    with open('link_data.txt', 'w') as file:
        file.write(link_text)

    pattern_for_line = r'<h3'
    pattern_for_headder = r'[">]{2}.*'

    with open('link_data.txt', 'r') as file_from:
        my_list = []
        for i_line in file_from:
            if re.match(pattern_for_line, i_line.rstrip()):
                result = re.findall(pattern_for_headder, i_line)
                my_list.append(result[0][2:-5])

    print(my_list)
