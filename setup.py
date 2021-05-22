# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['supports_color']

package_data = \
{'': ['*']}

install_requires = \
['dict>=2020.12.3,<2021.0.0', 'has-flag>=0.1.1,<0.2.0']

setup_kwargs = {
    'name': 'supports-color',
    'version': '0.1.1',
    'description': 'Detect whether a terminal supports color',
    'long_description': "# supports-color\n\n> Detect whether a terminal supports color\n\nA port of the Node.js package [`supports-color`](https://github.com/chalk/supports-color) to Python.\n\n## Install\n\n```\npython3 -m pip install -U supports-color\n```\n\n## Usage\n\n```py\nfrom supports_color import supportsColor\n\nif supportsColor.stdout:\n    print('Terminal stdout supports color');\n\nif supportsColor.stdout.has256:\n    print('Terminal stdout supports 256 colors');\n\nif supportsColor.stderr.has16m:\n    print('Terminal stderr supports 16 million colors (truecolor)');\n```\n\n## API\n\nSee [chalk/supports-color API docs](https://github.com/chalk/supports-color#api).\n\n## License\n\nMIT\n\n## Contact\n\nA library by [Shawn Presser](https://www.shawwn.com). If you found it useful, please consider [joining my patreon](https://www.patreon.com/shawwn)!\n\nMy Twitter DMs are always open; you should [send me one](https://twitter.com/theshawwn)! It's the best way to reach me, and I'm always happy to hear from you.\n\n- Twitter: [@theshawwn](https://twitter.com/theshawwn)\n- Patreon: [https://www.patreon.com/shawwn](https://www.patreon.com/shawwn)\n- HN: [sillysaurusx](https://news.ycombinator.com/threads?id=sillysaurusx)\n- Website: [shawwn.com](https://www.shawwn.com)\n\n",
    'author': 'Shawn Presser',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/shawwn/supports-color-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
