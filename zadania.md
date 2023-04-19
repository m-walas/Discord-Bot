<h1>Bot Discord</h1>

***

Autorzy: **Maja Wiśniewska, Mateusz Walas**

*Teleinformatyka AGH*

***
<h2>Instrukcja</h2>
Przed rozpoczęciem rozwiązywania zadań mały wstęp jak rozpocząć pracę.

> Aby przyspieszyć i usprawnić całą pracę zostały już przygotowane aplikacje na platformie Discord Developer Portal.
> Wystarczy, że zalogujesz się na swoje konto Discord i dołączysz do serwera, na którym znajdują się już dodane boty.
><br><br>Link do serwera: ***WSTAWIĆ LINK***.
><br><br>Każdy bot ma swoją unikalną *nazwę* i *token*. Wszystkie potrzebne dane zostały Wam przekazane na karteczkach.
> <br>**Podczas pracy z botem należy używać tylko kanału tekstowego odpowiadającego nazwie otrzymanego bota.**
> <br><br>**! WAŻNE !**
> Zaprogramuj swojego bota tak, aby reagował tylko na komendy, które zaczynają się od prefiksu `jpwpID_`, gdzie ID to numer z kartki.
>>Przykład: `jpwp1_hello`
 
Wszystkie potrzebne informacje o bibliotece discord.py znajdują się na stronie: https://discordpy.readthedocs.io/en/latest/index.html.

***

#### Zadanie 1 - synchroniczne i asynchroniczne wejście/wyjście
- *Cel: zaznajomienie się z asynchronicznym i synchroniczym wejściem/wyjściem.*


>Część 1 - synchroniczne wejście/wyjście
<p>
Napisz krótki, prosty program, który będzie zawierał funkcję, najpierw wypisującą Twoje imię, a dwie sekundy później nazwisko. 
W mainie za pomocą pętli wywołaj swoją funkcję np. 3 razy. 
Wykorzystaj bibliotekę time i oblicz czas wykonywania się całego programu.
</p>

>Część 2 - asynchroniczne wejście/wyjście
<p>
Teraz przerób swój kod, lub napisz nowy, w którym wykorzystasz bibliotekę asyncio do wykorzystania asynchronicznego działania. Pomocne będą słowa kluczowe async oraz await.
Ponownie jak poprzednio oblicz czas wykonywania programu i porównaj wyniki.
</p>

*Dla chętnych więcej do poczytania: https://realpython.com/async-io-python/*

***

#### Zadanie 2 - eventy bota Discord
- *Cel: Podstawowe poznanie z biblioteką discord.py*

> Część 1 - pierwszy event bota Discord - on_ready

Napisz prosty event bota Discord, który po załadowaniu się bota wyświetli wiadomość *Bot został załadowany* i numer bota na czacie odpowiedniego kanału tekstowego.

Potrzebne do tego mogą okazać się:
- `bot.event`
- `channel.send()`
- `bot.user`
- `on_ready()`

> Część 2 - event on_message

Rozbuduj swojego bota o event on_message, który będzie reagował na wiadomość użytkownika.

W przypadku, gdy użytkownik wpisze komendę `jpwpID_hej`, bot powinien odpowiedzieć na czacie wiadomością `Cześć!`.

Potrzebne do tego mogą okazać się:
- `bot.event`
- `message.content`
- `channel.send()`
- `on_message()`

***

#### zadanie 3 - komendy bota Discord
- *Cel: Poznanie komend bota Discord*

> Stworzenie własnej komendy bota Discord
 
Napisz własną komendę bota Discord, która będzie reagowała na `!jpwpID_rybka`.
Jej zadaniem będzie wysłanie na czacie losowego obrazka z katalogu paletki.
Katalog z obrazkami znajduje się na githubie - images/paletki.

Pamiętaj, że ma być to komenda, a nie event, więc nie używaj `on_message()`, tylko `@bot.command()`.


***

#### zadanie 4 - własna gra na Discordzie
- *Cel: Wykorzystanie biblioteki Pillow oraz poznanych wcześniej umiejętności do stworzenia własnej gry*

Napisz implementację gry w kółko i krzyżyk na Discordzie. Wykorzystaj do tego bibliotekę Pillow.

Możesz wykorzystać grafiki udostępnione na githubie.
Dla uproszczenia gra może być dla dwóch graczy, aby naprzemiennie wpisywać ruchy na czacie.

> Przykład: <br>
> - Po wpisaniu komendy `jpwpID_start` bot wyświetla na czacie planszę do gry
> - gracz 1 wpisuje komendę `jpwpID_kolko 1 1`
> - gracz 2 wpisuje komendę `jpwpID_krzyzyk 2 2`
> - . . .
> - rozstrzygnięcie gry

***

[//]: # (#### zadanie 5 - wykorzystanie poznanej wiedzy)

[//]: # (- *Cel: Wykorzystanie całej do tej pory zdobytej wiedzy do stworzenia własnej gry*)

[//]: # ()
[//]: # (Napisz własną grę w pythonie, która będzie grą na platfomie Discord, wykorzystując do tej pory zdobyte umiejętności.)

[//]: # (> Może być to np. gra w papier, kamień i nożyce. <br>)

[//]: # (> Działanie gry: <br>)

[//]: # (> - użytkownik wpisuje komendę do bota, np. !pkn start<br>)

[//]: # (> - użytkownik wpisuje swój wybór, np. !pkn kamień <br>)

[//]: # (> - bot losuje jedną z trzech opcji &#40;papier, kamień, nożyce&#41; <br>)

[//]: # (> - bot porównuje wybór użytkownika z losową opcją i wyświetla wynik <br>)

[//]: # ()
[//]: # (*Masz pomysł na swoją grę? Zaskocz nas! :&#41;*)