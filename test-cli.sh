#!/bin/env bash

set -euo pipefail

assert() {
  if [[ "${1}" == "${2}" ]]; then
    return
  fi

  echo "Expected \"${2}\" but got \"${1}\" 🔥"
  exit 1
}

assert "$(thtml --version)" "${CIRCLE_TAG:-"-1.-1.-1"}"
assert "$(echo "foo" | thtml)" '<!doctype html><html><head><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1" /><title>cariad/thtml</title><meta name="author" content="cariad/thtml" /></head><body><style type="text/css">.thtml { background: #101013; border-radius: 0.5rem; color: var(--white); font-family: Fira Code, Consolas, "Andale Mono WT", "Andale Mono", "Lucida Console", "Lucida Sans Typewriter", "DejaVu Sans Mono", "Bitstream Vera Sans Mono", "Liberation Mono", "Nimbus Mono L", Monaco, "Courier New", Courier, monospace;; letter-spacing: 0.03rem; margin-left: auto; margin-right: auto; padding: 2rem; width: max-content; --white: #CCC; } .thtml-code { font-family: inherit; }</style><pre class="nohighlight thtml"><code class="thtml-code">foo<br /></code></pre></body></html>'
echo "foo" | thtml --theme google-fonts
echo "foo" | thtml --theme plain
