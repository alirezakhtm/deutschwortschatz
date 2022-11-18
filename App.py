
import csv
from googletrans import Translator
import os

class Sperator:
    MINUS: str = ' - '
    KOMA: str = ';'

def read_file(file_name: str, sperator: str) -> list:
    my_file = open(file_name, 'r')
    data = my_file.readlines()
    ans = [d.replace('\n', '').replace('sb', 'somebody').replace('sth', 'something').split(sperator) for d in data]
    return ans

def translate_to_persian(englisch: str) -> str:
    translator = Translator()
    result = translator.translate(englisch, src='en', dest='fa')
    return result.text

def process_file(file_name, sperator: str) -> list:
    file_data = read_file(file_name, sperator)
    result = []
    result_mosalingua = []
    for words in file_data:
        word = words[-1]
        persian_word = translate_to_persian(word)
        words.append(persian_word)
        result.append(words)
        # Mosalingua
        words_new = [words[0]]
        words_new.append(words[-2] + '\n' + words[-1])
        result_mosalingua.append(words_new)
    return result, result_mosalingua

def save_to_csv(file_name: str, data: list) -> None:
    with open(file_name, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def create_output(file_name: str, sperator: str):
    data, data_mosalingua = process_file(file_name, sperator)
    output_name = file_name.split('_')[0].replace('input/', 'output/')+'.csv'
    save_to_csv(output_name, data)
    save_to_csv(output_name.replace('.csv', '_mosalingua.csv'), data_mosalingua)

def find_files() -> list:
    ans = []
    for _, _, files in os.walk('input'):
        for file in files:
            if file.endswith('.txt'):
                ans.append( 'input/' + file)
    return ans


if __name__ == '__main__':
    files_input = find_files()
    for file in files_input:
        create_output(file, Sperator.KOMA)

