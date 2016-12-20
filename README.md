# bunia

[![PyPI version](https://badge.fury.io/py/bunia.svg)](https://badge.fury.io/py/bunia)
[![Build Status](https://travis-ci.org/smok-serwis/bunia.svg)](https://travis-ci.org/smok-serwis/bunia)
[![Code Climate](https://codeclimate.com/github/smok-serwis/bunia/badges/gpa.svg)](https://codeclimate.com/github/smok-serwis/bunia)
[![Test Coverage](https://codeclimate.com/github/smok-serwis/bunia/badges/coverage.svg)](https://codeclimate.com/github/smok-serwis/bunia/coverage)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)]()
[![PyPI](https://img.shields.io/pypi/pyversions/bunia.svg)]()
[![PyPI](https://img.shields.io/pypi/implementation/bunia.svg)]()

**bunia** is a library, that allows you to write multi-interface commands.

This means that the same command can be launched using eg. console, Web GUI, e-mail, SMS, or any other provider you might wish.

You specify a command as a class.

## Integrated runner
To run a command from console, type:

```bash
python -m bunia.runner.console mymodule:MyCommandClass ... arguments ... 
```