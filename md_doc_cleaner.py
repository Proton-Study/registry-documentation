from langchain.text_splitter import MarkdownHeaderTextSplitter
import langchain_core.documents

def extract_data_from_row(row:str) -> list[str]:
    row_data = row[1:-1].split('|')
    row_data = [data.strip() for data in row_data]
    return row_data

def generate_row_text(headers:list[str], values:list[str]) -> str:
    row_text = ""
    for header, value in zip(headers, values):
        row_text += f"{header}: {value},\n"
    row_text = row_text[:-2]
    return row_text

def content_handler(content:str, token_limit:int) -> list[str]:
    final_page_content = []
    # Table Handler
    if content.startswith('|'):
        chunk = ""
        rows = content.split('\n')
        headers = extract_data_from_row(rows.pop(0))
        del rows[0]
        for row in rows:
            row_data = extract_data_from_row(row)
            row_text = generate_row_text(headers, row_data)
            if len(row_text) > token_limit:
                final_page_content.append(chunk)
                chunk = ""
                final_page_content.append(row_text[:token_limit])
            elif len(chunk) + len(row_text) > token_limit:
                final_page_content.append(chunk)
                chunk = ""
                chunk += row_text
    elif content.startswith('!['):
        return []
    else:
        # TODO: Split the tokens by words to prevent tokens split mid-word
        if len(content) > token_limit:
            final_page_content = [content[0+i:token_limit+i] for i in range(0, len(content), token_limit)]             
        else:
            final_page_content = [content]
    
    return final_page_content

def chunkify_document(document:list[langchain_core.documents.base.Document], token_limit:int = 200) -> list[str]:
    modified_token_limit = token_limit-50
    final_chunkified_document = []

    for section in document:
        major_heading = section.metadata['major_heading'] if 'major_heading' in section.metadata else 'None'
        minor_heading = section.metadata['minor_heading'] if 'minor_heading' in section.metadata else 'None'
        sub_heading = section.metadata['sub_heading'] if 'sub_heading' in section.metadata else 'None'
        page_content = section.page_content

        final_page_content = content_handler(page_content, modified_token_limit)
        
        for content in final_page_content:
            chunk = f"Major Heading: {major_heading},\nMinor Heading: {minor_heading},\nSub Heading: {sub_heading},\nContent: {content}"
            l_chunk = len(chunk)
            chunk += f",\nLen: {l_chunk}"
            final_chunkified_document.append(chunk)
    
    return final_chunkified_document

def main():
    markdown_text = open('README.md').read()
    splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[('#', 'major_heading'), ('##', 'minor_heading'), ('###', 'sub_heading')]
    )
    split_document = splitter.split_text(markdown_text)
    chunkified_document = chunkify_document(split_document)
    # print(len(chunkified_document))
    print(chunkified_document)

if __name__ == "__main__":
    main()