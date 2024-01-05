def print_field(text, loader_context):
    print_field = loader_context.get('print_field', '')

    print(f"\n\nTEXT:\n{text}\n\n")

    return text