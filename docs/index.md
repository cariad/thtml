# thtml

CLI tool and Python package for converting text to HTML

```text
This is just a text code block.

It's here so I can check out the style.
```

<!-- markdownlint-disable MD033 -->
<div style="font-family: monospace;">
  <span style="color: #f00;">Hello</span> <span style="color: #0f0;">world!</span>
</div>
<!-- markdownlint-enable MD033 -->

This one uses CSS:

<!-- markdownlint-disable MD033 -->
<style type="text/css">
  .thtml-container {
    font-family: monospace;
  }

  .thtml-container .fg-red {
    color: #f00;
  }

  .thtml-container .fg-green {
    color: #0f0;
  }
</style>

<div class="thtml-container">
  <span class="fg-red">Hello</span> <span class="fg-green">world!</span>
</div>
<!-- markdownlint-enable MD033 -->
