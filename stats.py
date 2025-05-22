def get_word_count(book_text:str) -> int:
    return  len(book_text.split())


def get_characters(book_text:str): 
    characters = dict()
    for char in book_text:
        if char.lower() not in characters:
            characters[char.lower()] = 0
        characters[char.lower()] += 1
        
    return characters

def book_report(book_characters:dict) -> list[dict]:
    report = []
    
    for k,v in book_characters.items():
        report.append({"char": k, "num": v})
        
    return sorted(report, key=lambda item: item["num"], reverse=True)