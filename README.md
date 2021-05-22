# supports-color

> Detect whether a terminal supports color

A port of the Node.js package [`supports-color`](https://github.com/chalk/supports-color) to Python.

## Install

```
python3 -m pip install -U supports-color
```

## Usage

```py
from supports_color import supportsColor

if supportsColor.stdout:
    print('Terminal stdout supports color');

if supportsColor.stdout.has256:
    print('Terminal stdout supports 256 colors');

if supportsColor.stderr.has16m:
    print('Terminal stderr supports 16 million colors (truecolor)');
```

## API

See [chalk/supports-color API docs](https://github.com/chalk/supports-color#api).

## License

MIT

## Contact

A library by [Shawn Presser](https://www.shawwn.com). If you found it useful, please consider [joining my patreon](https://www.patreon.com/shawwn)!

My Twitter DMs are always open; you should [send me one](https://twitter.com/theshawwn)! It's the best way to reach me, and I'm always happy to hear from you.

- Twitter: [@theshawwn](https://twitter.com/theshawwn)
- Patreon: [https://www.patreon.com/shawwn](https://www.patreon.com/shawwn)
- HN: [sillysaurusx](https://news.ycombinator.com/threads?id=sillysaurusx)
- Website: [shawwn.com](https://www.shawwn.com)

