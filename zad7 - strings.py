def get_two_text_with_equal_length(message1: str, message2: str) -> tuple[str, str]:
    while len(text1 := input(f'{message1}:\n')) != len(text2 := input(f'{message2}:\n')):
        print("The provided texts are not equally long")
    return text1, text2


def merge_texts(text1: str, text2: str) -> str:
    result = []
    for i in range(0, len(text1)):
        result.append(text1[i]+text2[i])
    return ''.join(result)


def main():
    message1 = "Provide first text"
    message2 = "Provide second text of equal lengths as the first one"
    text1, text2 = get_two_text_with_equal_length(message1, message2)
    merged_texts = merge_texts(text1, text2)
    print(merged_texts)


main()
