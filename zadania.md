<h1>Bot Discord</h1>

***

Autorzy: **Maja Wiśniewska, Mateusz Walas**

*Teleinformatyka AGH*

***
<h3>Instrukcja</h3>
Przed rozpoczęciem rozwiązywania zadań mały poradnik jak rozpocząć pracę.


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

> Część 1 - pierwszy event bota Discord

Napisz prosty event bota Discord, który po załadowaniu się bota wyświetli wiadomość na czacie z **Twoim numerem** z kartki.

> Część 2 - event on_message

Rozbuduj swojego bota o event on_message, który będzie reagował na wiadomość użytkownika.
Jeśli użytkownik wpisze komendę !hello, bot powinien odpowiedzieć na wiadomość użytkownika wiadomością "Hello!".

***

#### zadanie 3 - komendy bota Discord
- *Cel: Poznanie więcej komend bota Discord*

> Część 1 - komenda 

***

#### zadanie 4 - własna gra na Discordzie
- *Cel: Wykorzystanie biblioteki Pillow oraz poznanych wcześniej umiejętności do stworzenia własnej gry*

Napisz implementację gry w kółko i krzyżyk na Discordzie. Wykorzystaj do tego bibliotekę Pillow.

> Możesz wykorzystać grafiki udostępnione na githubie.
> Dla uproszczenia gra może być dla dwóch graczy, aby naprzemiennie wpisywać ruchy na czacie.

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