import markdown as md

# Remove characters that can interfere with LLM
def clean_line(line:str) -> str:
    cpy_line = line
    if cpy_line.startswith('!['):
        return None
    else:
        return cpy_line
    
# Create chunks to embed and store data properly based on Headings and Max Token Limits
def chunkify_document(document:list, token_limit:int = 200) -> list:
    # For Loop Begins
        # Section Handler
        # Table Handler
    # For Loop Ends
    pass

def main():
    document = []
    cleaned_document = []
    with open('README.md', 'r') as f:
        document.extend(f.readlines())

    for line in document:
        cleaned_line = clean_line(line)
        if cleaned_line is not None:
            cleaned_document.append(cleaned_line)
    
    print(cleaned_document)

if __name__ == "__main__":
    main()