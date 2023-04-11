def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hej' or p_message == 'cześć' or p_message == 'siema':
        return 'Cześć!'

    if p_message == 'co tam?':
        return 'Lajtowo byku'

    if p_message == '!help':
        return '`Aby zobaczyć dostępne komendy wpisz .help.\n Aby uzyskać szczegółowe informacje na temat ' \
               'komendy wpisz .help [komenda].\n Aby otrzymać odpowiedź w wiadomości prywatnej dodaj ' \
               'pv, na przykład: pv,!help.\n`' \

    if p_message == 'zagramy w kółko i krzyżyk?' or p_message == 'zagramy w coś?':
        return 'Zagramy! ' \
                  'Wpisz ".start" aby rozpocząć grę w kółko i krzyżyk!.'

    # if p_message didn't match any of the above do nothing
    return ''
