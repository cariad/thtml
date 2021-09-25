# CLI usage

## Input

**In theory,** `thtml` will convert piped text to HTML.

```bash
echo "Hello, world!" | thtml
```

**However,** many applications will detect that they're running non-interactively and will "clean up" their output, including removing colour codes. For example, `pipenv --help` will present colourful notes, but `pipenv --help | cat` filters out the color.

If your application filters its output when run non-interactively, you can have `thtml` run the command in a pseudo terminal via the `-c` or `--command` argument.

```bash
thtml --command pipenv --help
```

!!! warning "Windows"
    At the time of writing, the `-c`/`--command` arguments probably won't work in Windows due to lack of support for pseudo terminals.

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
