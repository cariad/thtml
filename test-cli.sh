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
