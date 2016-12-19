# bunia

**bunia** is a library, that allows you to write multi-interface commands.

This means that the same command can be launched using eg. console, Web GUI, e-mail, SMS, or any other provider you might wish.

You specify a command as a class.

## Integrated runner
To run a command from console, type:

```bash
python -m bunia.runner.console mymodule:MyCommandClass ... arguments ... 
```