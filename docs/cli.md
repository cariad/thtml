# CLI usage

## Input

In most cases, you can simply pipe a command's output into `thtml`:

```bash
echo "Hello, world!" | thtml
```

However, many applications will detect that they're running non-interactively and will "clean up" their output, including removing colour codes. For example, `pipenv --help` will present colourful notes, but `pipenv --help | cat` filters out the color.

If your application filters its output when run non-interactively, you can have `thtml` run the command in a pseudo terminal by passing the command as arguments:

```bash
thtml pipenv --help
```

!!! warning "Windows"
    At the time of writing, these arguments probably won't work in Windows due to lack of support for pseudo terminals.

## Output

`thtml` sends the generated HTML to _stdout_. Redirect the output to write to a file.

```bash
echo "Hello, world!" | thtml > hello.html
```

## Scope

By default, `thtml` will return an entire HTML document. To return only a fragment -- say, to insert into your own `<body>` element -- pass `--scope fragment`.

```bash
echo "Hello, world!" | thtml --scope fragment
```

## Browsers

Send the HTML directly to the default browser by adding the `-o` or `--open` argument.

```bash
echo "Hello, world!" | thtml --open
```

## Custom theme

Use a custom [theme](themes.md) by adding the `-t` or `--theme` argument.

For example, to use Google Fonts to support additional styles:

```bash
echo "Hello, world!" | thtml --theme google-fonts
```

To provide your own [custom theme](custom-themes.md):

```bash
echo "Hello, world!" | thtml --theme custom.yml
```
