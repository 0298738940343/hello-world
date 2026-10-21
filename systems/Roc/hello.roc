# replace the URL with the latest basic-cli release from github.com/roc-lang/basic-cli
app [main!] { pf: platform "https://github.com/roc-lang/basic-cli/releases/download/<version>/<hash>.tar.br" }

import pf.Stdout

main! = |_args|
    Stdout.line!("Hello, World!")
