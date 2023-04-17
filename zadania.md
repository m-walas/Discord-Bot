<h1>Bot Discord</h1>

***

Autorzy: **Maja Wiśniewska, Mateusz Walas**

*Teleinformatyka AGH*

***

#### zadanie 1 - synchroniczne i asynchroniczne wejście/wyjście
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

#### zadanie 2 - pierwsza prosta funkcja bota Discord
- *Cel: Podstawowe poznanie z biblioteką discord.py*

<p>
Napisz prostą funkcję bota Discord, która po dołączeniu do serwera wyświetli wiadomość powitalną na czacie ogólnym.
</p>

> Podpowiedź: <br>
> client.on_user_join() - wywoływana po dołączeniu użytkownika do serwera <br>

***

#### zadanie 3 - komendy bota Discord
- *Cel: Poznanie więcej komend bota Discord*


***

#### zadanie 4 - zapoznanie się z biblioteką Pillow
- *Cel: Umiejętność wykorzystania biblioteki Pillow do przedstawiania grafiki w postaci obrazków*

***

#### zadanie 5 - wykorzystanie poznanej wiedzy
- *Cel: Wykorzystanie całej do tej pory zdobytej wiedzy do stworzenia własnej gry*

Napisz własną grę w pythonie, która będzie grą na platfomie Discord, wykorzystując do tej pory zdobyte umiejętności.
> Może być to np. gra w papier, kamień i nożyce. <br>
> Działanie gry: <br>
> - użytkownik wpisuje komendę do bota, np. !pkn start<br>
> - użytkownik wpisuje swój wybór, np. !pkn kamień <br>
> - bot losuje jedną z trzech opcji (papier, kamień, nożyce) <br>
> - bot porównuje wybór użytkownika z losową opcją i wyświetla wynik <br>

*Masz pomysł na swoją grę? Zaskocz nas! :)*