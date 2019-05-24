import click
from py_heideltime import heideltime
@click.command()
@click.option("-t", '--text', help='insert text', required=False)
@click.option("-l", '--language', help='insert language name', required=True)
@click.option("-td", '--document_type', help='Type of the document specified by <file> (options: News, Narrative, Colloquial, Scientific).', default='News', required=False)
@click.option("-dct", '--document_creation_time', help='Creation date of document only valid format (YYYY-MM-DD).only will be considered if document type are News or colloquial.', default="", required=False)
@click.option("-i", '--input_file', help='input text file', required=False)
def dates(text, language, input_file, document_type, document_creation_time):
    def run_py_heideltime(text_content):
            output = heideltime(text_content, language, document_type, document_creation_time)
            print(output)
    if text and input_file:
        print('Select only text or file to be analysed')
        exit(1)
    elif not text and not input_file:
        print('you must insert text or select file with text')
        exit(1)
    else:
        if text:
            run_py_heideltime(text)
        else:
            with open(input_file) as file:
                text_content = file.read()
                run_py_heideltime(text_content)


if __name__ == "__main__":
    dates()
