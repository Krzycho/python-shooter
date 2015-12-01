# Side Scrolling Shooter

## Zadanie

Side scrolling shooter - klasyczna strzelanka gdzie lecimy statkiem/innym obiektem caly czas w prawo i walczymy z nadlatującymi wrogami. Gra powinna zawierac kilka plansz, rozne rodzaje wrogow, broni/bonusow, conajmniej jedna walke z bossem i tryb dla 2 graczy.

## Technologię

Python 3 + Cocos2d

## Instalacja

### Wymagania

0. [python 3](https://www.python.org/)
1. [pip](https://pip.pypa.io/en/latest/installing.html)
2. [cocos2d](https://github.com/los-cocos/cocos)

Dla systemów Linux można użyć komand:

    [sudo] apt-get install libsdl2-dev libsdl2-image-dev libsdl2-ttf-dev libsdl2-mixer-dev

Dla OS X:

    brew install sdl2 sdl2_image sdl2_ttf sdl2_mixer

### Wymagane moduły Pythona

Dla instalacji modułów, użyć `pip`:

    pip install cocos2d

## TODO

1. Create a PlayerController class, which will encapsulate both player instance and his controlling functions (mouse / keyboard). Layer shall contain multiple PlayerControllers and pass on_mouse_motion and on_key_press to them.
