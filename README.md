# Hello World! in 357 languages and formats

The same Hello World written in 357 programming languages, plus a few markup, data and config formats. It goes from C to COBOL, from x86 boot sectors to Malbolge, and includes HolyC, the language Terry A. Davis wrote for TempleOS.

Le même Hello World dans 357 langages et formats, classés par famille.

119 of them were compiled or run and checked to print Hello World. They are marked "yes" in the Tested column. The others follow the standard style of each language but could not be run where this repo was built (no toolchain available, or they need a GPU, a mainframe, a blockchain or a Commodore 64).

Each language has its own folder: `<category>/<language>/<file>`.

`tools/esorun.py` contains small interpreters for Brainfuck, Ook!, COW, Whitespace, Befunge, Unlambda, HQ9+, Thue, Underload and Malbolge, so those only need Python.

## Highlights

| Language | File | Note |
|---|---|---|
| HolyC (TempleOS) | [`hello.HC`](systems/HolyC-TempleOS-by-Terry-A-Davis/hello.HC) | A string literal on its own line is printed |
| Malbolge | [`hello.mb`](esoteric/Malbolge/hello.mb) | Designed to be almost impossible to program in |
| Boot sector | [`boot.asm`](assembly/Boot-sector-x86-real-mode-BIOS/boot.asm) | Runs without any operating system |
| Machine code | [`hello.hex`](assembly/Machine-code-x86-64-Linux-ELF-hex/hello.hex) | A Linux executable written as hex bytes |
| Whitespace | [`hello.ws`](esoteric/Whitespace/hello.ws) | Only spaces, tabs and newlines |
| INTERCAL | [`hello.i`](esoteric/INTERCAL/hello.i) | The compiler rejects programs that are not polite enough |
| COBOL, JCL, PL/I, RPG | see the historic folder | Still used in banking systems |

## Systems & compiled (53)

| Language | File | Tested |
|---|---|:-:|
| Ada | [`hello.adb`](systems/Ada/hello.adb) | yes |
| Ballerina | [`hello.bal`](systems/Ballerina/hello.bal) |  |
| Beef | [`Program.bf`](systems/Beef/Program.bf) |  |
| C | [`hello.c`](systems/C/hello.c) | yes |
| C (K&R 1978) | [`hello_kr.c`](systems/C-K-R-1978/hello_kr.c) | yes |
| C# | [`hello.cs`](systems/Csharp/hello.cs) | yes |
| C# (top-level) | [`hello_toplevel.cs`](systems/Csharp-top-level/hello_toplevel.cs) |  |
| C++ | [`hello.cpp`](systems/Cpp/hello.cpp) | yes |
| C3 | [`hello.c3`](systems/C3/hello.c3) |  |
| Carbon | [`hello.carbon`](systems/Carbon/hello.carbon) |  |
| Chapel | [`hello.chpl`](systems/Chapel/hello.chpl) |  |
| COBOL | [`hello.cob`](systems/COBOL/hello.cob) | yes |
| Crystal | [`hello.cr`](systems/Crystal/hello.cr) | yes |
| CUDA | [`hello.cu`](systems/CUDA/hello.cu) |  |
| Cyclone | [`hello.cyc`](systems/Cyclone/hello.cyc) |  |
| Cython | [`hello.pyx`](systems/Cython/hello.pyx) |  |
| D | [`hello.d`](systems/D/hello.d) | yes |
| Dart | [`hello.dart`](systems/Dart/hello.dart) |  |
| Delphi (Object Pascal) | [`hello.dpr`](systems/Delphi-Object-Pascal/hello.dpr) | yes |
| Eiffel | [`hello.e`](systems/Eiffel/hello.e) |  |
| F# | [`hello.fsx`](systems/Fsharp/hello.fsx) |  |
| Fortran 77 | [`hello.f`](systems/Fortran-77/hello.f) | yes |
| Fortran 90 | [`hello.f90`](systems/Fortran-90/hello.f90) | yes |
| Gleam | [`hello.gleam`](systems/Gleam/hello.gleam) |  |
| Go | [`hello.go`](systems/Go/hello.go) | yes |
| Groovy | [`hello.groovy`](systems/Groovy/hello.groovy) | yes |
| Hare | [`hello.ha`](systems/Hare/hello.ha) |  |
| Haxe | [`Main.hx`](systems/Haxe/Main.hx) | yes |
| HolyC (TempleOS, by Terry A. Davis) | [`hello.HC`](systems/HolyC-TempleOS-by-Terry-A-Davis/hello.HC) |  |
| Jai | [`hello.jai`](systems/Jai/hello.jai) |  |
| Java | [`Hello.java`](systems/Java/Hello.java) | yes |
| Java 21+ (unnamed class) | [`HelloModern.java`](systems/Java-21p-unnamed-class/HelloModern.java) |  |
| Kotlin | [`hello.kt`](systems/Kotlin/hello.kt) |  |
| LLVM IR | [`hello.ll`](systems/LLVM-IR/hello.ll) |  |
| Lobster | [`hello.lobster`](systems/Lobster/hello.lobster) |  |
| Modula-2 | [`hello.mod`](systems/Modula-2/hello.mod) |  |
| Mojo | [`hello.mojo`](systems/Mojo/hello.mojo) |  |
| Nim | [`hello.nim`](systems/Nim/hello.nim) | yes |
| Oberon | [`Hello.Mod`](systems/Oberon/Hello.Mod) |  |
| Objective-C | [`hello.m`](systems/Objective-C/hello.m) | yes |
| Odin | [`hello.odin`](systems/Odin/hello.odin) |  |
| OpenCL C (kernel) | [`hello.cl`](systems/OpenCL-C-kernel/hello.cl) |  |
| Pascal | [`hello.pas`](systems/Pascal/hello.pas) | yes |
| Pony | [`hello.pony`](systems/Pony/hello.pony) |  |
| Roc | [`hello.roc`](systems/Roc/hello.roc) |  |
| Rust | [`hello.rs`](systems/Rust/hello.rs) | yes |
| Scala | [`hello.scala`](systems/Scala/hello.scala) |  |
| Swift | [`hello.swift`](systems/Swift/hello.swift) |  |
| V | [`hello.v`](systems/V/hello.v) |  |
| Vala | [`hello.vala`](systems/Vala/hello.vala) | yes |
| Visual Basic .NET | [`hello.vb`](systems/Visual-Basic-NET/hello.vb) |  |
| WebAssembly (WAT, WASI) | [`hello.wat`](systems/WebAssembly-WAT-WASI/hello.wat) |  |
| Zig | [`hello.zig`](systems/Zig/hello.zig) |  |

## Scripting & dynamic (91)

| Language | File | Tested |
|---|---|:-:|
| ActionScript 3 | [`Hello.as`](scripting/ActionScript-3/Hello.as) |  |
| AngelScript | [`hello.as`](scripting/AngelScript/hello.as) |  |
| AppleScript | [`hello.applescript`](scripting/AppleScript/hello.applescript) |  |
| AssemblyScript | [`hello.as.ts`](scripting/AssemblyScript/hello.as.ts) |  |
| AutoHotkey v2 | [`hello.ahk`](scripting/AutoHotkey-v2/hello.ahk) |  |
| AutoIt | [`hello.au3`](scripting/AutoIt/hello.au3) |  |
| AWK | [`hello.awk`](scripting/AWK/hello.awk) | yes |
| bc | [`hello.bc`](scripting/bc/hello.bc) | yes |
| BeanShell | [`hello.bsh`](scripting/BeanShell/hello.bsh) | yes |
| Boo | [`hello.boo`](scripting/Boo/hello.boo) |  |
| Civet | [`hello.civet`](scripting/Civet/hello.civet) |  |
| CoffeeScript | [`hello.coffee`](scripting/CoffeeScript/hello.coffee) | yes |
| Dart (script) | [`hello_script.dart`](scripting/Dart-script/hello_script.dart) |  |
| dc | [`hello.dc`](scripting/dc/hello.dc) | yes |
| Elixir | [`hello.exs`](scripting/Elixir/hello.exs) | yes |
| Elm | [`Main.elm`](scripting/Elm/Main.elm) |  |
| Elvish | [`hello.elv`](scripting/Elvish/hello.elv) |  |
| Emacs Lisp | [`hello.el`](scripting/Emacs-Lisp/hello.el) | yes |
| Erlang (escript) | [`hello.erl`](scripting/Erlang-escript/hello.erl) | yes |
| Expect | [`hello.exp`](scripting/Expect/hello.exp) | yes |
| Fennel | [`hello.fnl`](scripting/Fennel/hello.fnl) |  |
| Ferret | [`hello.fql`](scripting/Ferret/hello.fql) |  |
| GDScript (Godot) | [`hello.gd`](scripting/GDScript-Godot/hello.gd) |  |
| Genie | [`hello.gs`](scripting/Genie/hello.gs) | yes |
| GNU Octave | [`hello_octave.m`](scripting/GNU-Octave/hello_octave.m) | yes |
| Hy | [`hello.hy`](scripting/Hy/hello.hy) |  |
| Icon | [`hello.icn`](scripting/Icon/hello.icn) | yes |
| IDL | [`hello.pro`](scripting/IDL/hello.pro) |  |
| Imba | [`hello.imba`](scripting/Imba/hello.imba) |  |
| Io | [`hello.io`](scripting/Io/hello.io) |  |
| Janet | [`hello.janet`](scripting/Janet/hello.janet) |  |
| JavaScript (Node.js) | [`hello.js`](scripting/JavaScript-Node-js/hello.js) | yes |
| JavaScript (Rhino) | [`hello_rhino.js`](scripting/JavaScript-Rhino/hello_rhino.js) | yes |
| jq | [`hello.jq`](scripting/jq/hello.jq) | yes |
| JRuby | [`hello_jruby.rb`](scripting/JRuby/hello_jruby.rb) | yes |
| JScript (Windows Script Host) | [`hello.wsf.js`](scripting/JScript-Windows-Script-Host/hello.wsf.js) |  |
| Julia | [`hello.jl`](scripting/Julia/hello.jl) |  |
| Jython | [`hello_jython.py`](scripting/Jython/hello_jython.py) | yes |
| Kotlin script | [`hello.main.kts`](scripting/Kotlin-script/hello.main.kts) |  |
| Lasso | [`hello.lasso`](scripting/Lasso/hello.lasso) |  |
| LFE (Lisp Flavoured Erlang) | [`hello.lfe`](scripting/LFE-Lisp-Flavoured-Erlang/hello.lfe) |  |
| LiveScript | [`hello.ls`](scripting/LiveScript/hello.ls) |  |
| Logo | [`hello.logo`](scripting/Logo/hello.logo) |  |
| Lua | [`hello.lua`](scripting/Lua/hello.lua) | yes |
| LuaJIT | [`hello_jit.lua`](scripting/LuaJIT/hello_jit.lua) | yes |
| m4 | [`hello.m4`](scripting/m4/hello.m4) | yes |
| Maple | [`hello.mpl`](scripting/Maple/hello.mpl) |  |
| MATLAB | [`hello.m`](scripting/MATLAB/hello.m) |  |
| Mint | [`Main.mint`](scripting/Mint/Main.mint) |  |
| MoonScript | [`hello.moon`](scripting/MoonScript/hello.moon) |  |
| Neko | [`hello.neko`](scripting/Neko/hello.neko) | yes |
| newLISP | [`hello.lsp`](scripting/newLISP/hello.lsp) | yes |
| Nickle | [`hello.5c`](scripting/Nickle/hello.5c) | yes |
| NQP | [`hello.nqp`](scripting/NQP/hello.nqp) | yes |
| Nushell | [`hello.nu`](scripting/Nushell/hello.nu) |  |
| Pawn | [`hello.p`](scripting/Pawn/hello.p) |  |
| Perl | [`hello.pl`](scripting/Perl/hello.pl) | yes |
| Pharo Smalltalk | [`hello_pharo.st`](scripting/Pharo-Smalltalk/hello_pharo.st) |  |
| PHP | [`hello.php`](scripting/PHP/hello.php) | yes |
| PicoLisp | [`hello.l`](scripting/PicoLisp/hello.l) | yes |
| Pike | [`hello.pike`](scripting/Pike/hello.pike) | yes |
| PureScript | [`Main.purs`](scripting/PureScript/Main.purs) |  |
| PyPy | [`hello_pypy.py`](scripting/PyPy/hello_pypy.py) | yes |
| Python 2 | [`hello2.py`](scripting/Python-2/hello2.py) |  |
| Python 3 | [`hello.py`](scripting/Python-3/hello.py) | yes |
| Q# | [`hello.qs`](scripting/Qsharp/hello.qs) |  |
| R | [`hello.R`](scripting/R/hello.R) | yes |
| Raku (Perl 6) | [`hello.raku`](scripting/Raku-Perl-6/hello.raku) | yes |
| ReasonML | [`hello.re`](scripting/ReasonML/hello.re) |  |
| Rebol | [`hello.r3`](scripting/Rebol/hello.r3) |  |
| Red | [`hello.red`](scripting/Red/hello.red) |  |
| ReScript | [`Hello.res`](scripting/ReScript/Hello.res) |  |
| REXX | [`hello.rexx`](scripting/REXX/hello.rexx) | yes |
| Ring | [`hello.ring`](scripting/Ring/hello.ring) |  |
| Ruby | [`hello.rb`](scripting/Ruby/hello.rb) | yes |
| SAS | [`hello.sas`](scripting/SAS/hello.sas) |  |
| Scilab | [`hello.sce`](scripting/Scilab/hello.sce) |  |
| sed | [`hello.sed`](scripting/sed/hello.sed) | yes |
| Smalltalk (GNU) | [`hello.st`](scripting/Smalltalk-GNU/hello.st) |  |
| SNOBOL4 | [`hello.sno`](scripting/SNOBOL4/hello.sno) |  |
| Squirrel | [`hello.nut`](scripting/Squirrel/hello.nut) |  |
| Stata | [`hello.do`](scripting/Stata/hello.do) |  |
| Tcl | [`hello.tcl`](scripting/Tcl/hello.tcl) | yes |
| TypeScript | [`hello.ts`](scripting/TypeScript/hello.ts) | yes |
| Uiua | [`hello.ua`](scripting/Uiua/hello.ua) |  |
| VBA (Excel macro) | [`hello.bas`](scripting/VBA-Excel-macro/hello.bas) |  |
| VBScript | [`hello.vbs`](scripting/VBScript/hello.vbs) |  |
| Vim script | [`hello.vim`](scripting/Vim-script/hello.vim) | yes |
| Wolfram Language (Mathematica) | [`hello.wl`](scripting/Wolfram-Language-Mathematica/hello.wl) |  |
| Wren | [`hello.wren`](scripting/Wren/hello.wren) |  |
| Xonsh | [`hello.xsh`](scripting/Xonsh/hello.xsh) |  |

## Functional (18)

| Language | File | Tested |
|---|---|:-:|
| Agda | [`Hello.agda`](functional/Agda/Hello.agda) |  |
| Bend | [`hello.bend`](functional/Bend/hello.bend) |  |
| Clean | [`hello.icl`](functional/Clean/hello.icl) |  |
| Coq / Rocq | [`hello.v`](functional/Coq-Rocq/hello.v) |  |
| Curry | [`Hello.curry`](functional/Curry/Hello.curry) |  |
| Elixir (Mix-less module) | [`hello_module.exs`](functional/Elixir-Mix-less-module/hello_module.exs) | yes |
| Futhark | [`hello.fut`](functional/Futhark/hello.fut) |  |
| Grain | [`hello.gr`](functional/Grain/hello.gr) |  |
| Haskell | [`hello.hs`](functional/Haskell/hello.hs) | yes |
| Idris 2 | [`Hello.idr`](functional/Idris-2/Hello.idr) |  |
| Koka | [`hello.kk`](functional/Koka/hello.kk) |  |
| Lean 4 | [`Hello.lean`](functional/Lean-4/Hello.lean) |  |
| Mercury | [`hello.m`](functional/Mercury/hello.m) |  |
| Miranda | [`hello.m`](functional/Miranda/hello.m) |  |
| OCaml | [`hello.ml`](functional/OCaml/hello.ml) | yes |
| Standard ML | [`hello.sml`](functional/Standard-ML/hello.sml) | yes |
| Standard ML (MLton) | [`hello_mlton.sml`](functional/Standard-ML-MLton/hello_mlton.sml) | yes |
| Unison | [`hello.u`](functional/Unison/hello.u) |  |

## Lisp family (16)

| Language | File | Tested |
|---|---|:-:|
| Arc | [`hello.arc`](lisp/Arc/hello.arc) |  |
| AutoLISP (AutoCAD) | [`hello_autolisp.lsp`](lisp/AutoLISP-AutoCAD/hello_autolisp.lsp) |  |
| Carp | [`hello.carp`](lisp/Carp/hello.carp) |  |
| Clojure | [`hello.clj`](lisp/Clojure/hello.clj) | yes |
| ClojureScript | [`hello.cljs`](lisp/ClojureScript/hello.cljs) |  |
| Common Lisp | [`hello.lisp`](lisp/Common-Lisp/hello.lisp) | yes |
| Common Lisp (CLISP) | [`hello_clisp.lisp`](lisp/Common-Lisp-CLISP/hello_clisp.lisp) | yes |
| Embeddable Common Lisp | [`hello_ecl.lisp`](lisp/Embeddable-Common-Lisp/hello_ecl.lisp) | yes |
| Lisp 1.5 (1962) | [`hello_lisp15.lisp`](lisp/Lisp-1-5-1962/hello_lisp15.lisp) |  |
| Racket | [`hello.rkt`](lisp/Racket/hello.rkt) | yes |
| Scheme (Chez) | [`hello_chez.ss`](lisp/Scheme-Chez/hello_chez.ss) | yes |
| Scheme (Chicken) | [`hello_chicken.scm`](lisp/Scheme-Chicken/hello_chicken.scm) | yes |
| Scheme (Gambit) | [`hello_gambit.scm`](lisp/Scheme-Gambit/hello_gambit.scm) | yes |
| Scheme (Guile) | [`hello.scm`](lisp/Scheme-Guile/hello.scm) | yes |
| Scheme (MIT) | [`hello_mit.scm`](lisp/Scheme-MIT/hello_mit.scm) | yes |
| Shen | [`hello.shen`](lisp/Shen/hello.shen) |  |

## Logic & constraint (5)

| Language | File | Tested |
|---|---|:-:|
| Answer Set Programming (clingo) | [`hello.lp`](logic/Answer-Set-Programming-clingo/hello.lp) |  |
| Datalog (Soufflé) | [`hello.dl`](logic/Datalog-Souffl/hello.dl) |  |
| MiniZinc | [`hello.mzn`](logic/MiniZinc/hello.mzn) |  |
| Prolog (GNU) | [`hello_gprolog.pl`](logic/Prolog-GNU/hello_gprolog.pl) | yes |
| Prolog (SWI) | [`hello.pl`](logic/Prolog-SWI/hello.pl) | yes |

## Shells, build & DevOps (20)

| Language | File | Tested |
|---|---|:-:|
| Ansible playbook | [`hello.yml`](shell/Ansible-playbook/hello.yml) |  |
| Bash | [`hello.bash`](shell/Bash/hello.bash) | yes |
| C shell (tcsh) | [`hello.csh`](shell/C-shell-tcsh/hello.csh) | yes |
| CMake | [`CMakeLists.txt`](shell/CMake/CMakeLists.txt) |  |
| DCL (OpenVMS) | [`hello.com`](shell/DCL-OpenVMS/hello.com) |  |
| Dhall | [`hello.dhall`](shell/Dhall/hello.dhall) |  |
| Dockerfile | [`Dockerfile`](shell/Dockerfile/Dockerfile) |  |
| Fish | [`hello.fish`](shell/Fish/hello.fish) | yes |
| GitHub Actions | [`hello.workflow.yml`](shell/GitHub-Actions/hello.workflow.yml) |  |
| JCL (IBM mainframe) | [`hello.jcl`](shell/JCL-IBM-mainframe/hello.jcl) |  |
| Jsonnet | [`hello.jsonnet`](shell/Jsonnet/hello.jsonnet) |  |
| KornShell | [`hello.ksh`](shell/KornShell/hello.ksh) | yes |
| Makefile | [`Makefile`](shell/Makefile/Makefile) | yes |
| Nix | [`hello.nix`](shell/Nix/hello.nix) |  |
| Plan 9 rc | [`hello.rc`](shell/Plan-9-rc/hello.rc) |  |
| POSIX sh | [`hello.sh`](shell/POSIX-sh/hello.sh) | yes |
| PowerShell | [`hello.ps1`](shell/PowerShell/hello.ps1) |  |
| Terraform (HCL) | [`main.tf`](shell/Terraform-HCL/main.tf) |  |
| Windows Batch | [`hello.bat`](shell/Windows-Batch/hello.bat) |  |
| Zsh | [`hello.zsh`](shell/Zsh/hello.zsh) | yes |

## Historic & mainframe (30)

| Language | File | Tested |
|---|---|:-:|
| ABAP (SAP) | [`hello.abap`](historic/ABAP-SAP/hello.abap) |  |
| ALGOL 60 | [`hello.alg`](historic/ALGOL-60/hello.alg) |  |
| ALGOL 68 | [`hello.a68`](historic/ALGOL-68/hello.a68) | yes |
| APL | [`hello.apl`](historic/APL/hello.apl) |  |
| B (Bell Labs, 1969) | [`hello.b`](historic/B-Bell-Labs-1969/hello.b) |  |
| BCPL | [`hello.b`](historic/BCPL/hello.b) |  |
| BQN | [`hello.bqn`](historic/BQN/hello.bqn) |  |
| Classic ASP (VBScript) | [`hello.asp`](historic/Classic-ASP-VBScript/hello.asp) |  |
| Clipper / xBase | [`hello.prg`](historic/Clipper-xBase/hello.prg) |  |
| ColdFusion (CFML) | [`hello.cfm`](historic/ColdFusion-CFML/hello.cfm) |  |
| dBase | [`hello_dbase.prg`](historic/dBase/hello_dbase.prg) |  |
| Dylan | [`hello.dylan`](historic/Dylan/hello.dylan) |  |
| Factor | [`hello.factor`](historic/Factor/hello.factor) |  |
| Forth | [`hello.fs`](historic/Forth/hello.fs) | yes |
| FORTRAN I-style (1957, fixed form) | [`hello_fortran66.f`](historic/FORTRAN-I-style-1957-fixed-form/hello_fortran66.f) | yes |
| HyperTalk (HyperCard) | [`hello.hypertalk`](historic/HyperTalk-HyperCard/hello.hypertalk) |  |
| J | [`hello.ijs`](historic/J/hello.ijs) |  |
| K | [`hello.k`](historic/K/hello.k) |  |
| MUMPS (M) | [`hello.mumps`](historic/MUMPS-M/hello.mumps) |  |
| Natural (Software AG) | [`hello.nsp`](historic/Natural-Software-AG/hello.nsp) |  |
| Occam | [`hello.occ`](historic/Occam/hello.occ) |  |
| pForth | [`hello_pforth.fth`](historic/pForth/hello_pforth.fth) | yes |
| PL/I | [`hello.pli`](historic/PL-I/hello.pli) |  |
| PostScript | [`hello.ps`](historic/PostScript/hello.ps) | yes |
| Ratfor | [`hello.r`](historic/Ratfor/hello.r) |  |
| RPG IV (free form) | [`hello.rpgle`](historic/RPG-IV-free-form/hello.rpgle) |  |
| Sather | [`hello.sa`](historic/Sather/hello.sa) |  |
| Self | [`hello.self`](historic/Self/hello.self) |  |
| Simula 67 | [`hello.sim`](historic/Simula-67/hello.sim) |  |
| Turing | [`hello.t`](historic/Turing/hello.t) |  |

## BASIC family (15)

| Language | File | Tested |
|---|---|:-:|
| Applesoft BASIC | [`hello_apple2.bas`](basic/Applesoft-BASIC/hello_apple2.bas) |  |
| BASIC (Dartmouth, 1964) | [`hello.bas`](basic/BASIC-Dartmouth-1964/hello.bas) | yes |
| BBC BASIC | [`hello_bbc.bas`](basic/BBC-BASIC/hello_bbc.bas) |  |
| BlitzBasic | [`hello.bb`](basic/BlitzBasic/hello.bb) |  |
| Commodore 64 BASIC | [`hello_c64.bas`](basic/Commodore-64-BASIC/hello_c64.bas) |  |
| FreeBASIC | [`hello_fb.bas`](basic/FreeBASIC/hello_fb.bas) |  |
| GW-BASIC | [`hello_gw.bas`](basic/GW-BASIC/hello_gw.bas) |  |
| Liberty BASIC | [`hello_lb.bas`](basic/Liberty-BASIC/hello_lb.bas) |  |
| PureBasic | [`hello.pb`](basic/PureBasic/hello.pb) |  |
| QBasic / QuickBASIC | [`hello_qb.bas`](basic/QBasic-QuickBASIC/hello_qb.bas) |  |
| Small Basic (Microsoft) | [`hello.sb`](basic/Small-Basic-Microsoft/hello.sb) |  |
| TI-BASIC (TI-83/84) | [`hello_ti.8xp.txt`](basic/TI-BASIC-TI-83-84/hello_ti.8xp.txt) |  |
| Visual Basic 6 | [`hello_vb6.frm`](basic/Visual-Basic-6/hello_vb6.frm) |  |
| Yabasic | [`hello.yab`](basic/Yabasic/hello.yab) | yes |
| ZX Spectrum BASIC | [`hello_zx.bas`](basic/ZX-Spectrum-BASIC/hello_zx.bas) |  |

## Assembly & machine code (15)

| Language | File | Tested |
|---|---|:-:|
| 6502 Assembly (Commodore 64) | [`hello_6502.s`](assembly/6502-Assembly-Commodore-64/hello_6502.s) | yes |
| ARM32 Assembly (Linux) | [`hello_arm32.s`](assembly/ARM32-Assembly-Linux/hello_arm32.s) | yes |
| ARM64 / AArch64 Assembly (Linux) | [`hello_arm64.s`](assembly/ARM64-AArch64-Assembly-Linux/hello_arm64.s) | yes |
| Boot sector (x86 real mode, BIOS) | [`boot.asm`](assembly/Boot-sector-x86-real-mode-BIOS/boot.asm) | yes |
| CIL / MSIL (.NET IL) | [`hello.il`](assembly/CIL-MSIL-NET-IL/hello.il) | yes |
| Intel 8051 (C for SDCC) | [`hello_8051.c`](assembly/Intel-8051-C-for-SDCC/hello_8051.c) | yes |
| Java bytecode (Jasmin) | [`Hello.j`](assembly/Java-bytecode-Jasmin/Hello.j) |  |
| Machine code (x86-64 Linux ELF, hex) | [`hello.hex`](assembly/Machine-code-x86-64-Linux-ELF-hex/hello.hex) | yes |
| MIPS Assembly (SPIM / MARS) | [`hello_mips.asm`](assembly/MIPS-Assembly-SPIM-MARS/hello_mips.asm) | yes |
| MS-DOS Assembly (COM, 8086) | [`hello_dos.asm`](assembly/MS-DOS-Assembly-COM-8086/hello_dos.asm) | yes |
| RISC-V Assembly (Linux) | [`hello_riscv.s`](assembly/RISC-V-Assembly-Linux/hello_riscv.s) | yes |
| x86 Assembly (32-bit Linux, NASM) | [`hello_x86.asm`](assembly/x86-Assembly-32-bit-Linux-NASM/hello_x86.asm) | yes |
| x86-64 Assembly (GAS, AT&T syntax) | [`hello_gas.s`](assembly/x86-64-Assembly-GAS-AT-T-syntax/hello_gas.s) | yes |
| x86-64 Assembly (Linux, NASM) | [`hello_x64.asm`](assembly/x86-64-Assembly-Linux-NASM/hello_x64.asm) | yes |
| Z80 Assembly (ZX Spectrum) | [`hello_z80.asm`](assembly/Z80-Assembly-ZX-Spectrum/hello_z80.asm) | yes |

## Hardware & embedded (9)

| Language | File | Tested |
|---|---|:-:|
| Arduino | [`hello.ino`](hardware/Arduino/hello.ino) |  |
| Chisel (Scala HDL) | [`Hello.scala`](hardware/Chisel-Scala-HDL/Hello.scala) |  |
| G-code (CNC) | [`hello.gcode`](hardware/G-code-CNC/hello.gcode) |  |
| Ladder logic (IEC 61131-3 Structured Text) | [`hello.st`](hardware/Ladder-logic-IEC-61131-3-Structured-Text/hello.st) |  |
| MicroPython | [`main.py`](hardware/MicroPython/main.py) |  |
| OpenSCAD | [`hello.scad`](hardware/OpenSCAD/hello.scad) |  |
| SystemVerilog | [`hello.sv`](hardware/SystemVerilog/hello.sv) | yes |
| Verilog | [`hello.v`](hardware/Verilog/hello.v) | yes |
| VHDL | [`hello.vhd`](hardware/VHDL/hello.vhd) | yes |

## Web, templates & markup (23)

| Language | File | Tested |
|---|---|:-:|
| Angular | [`hello.component.ts`](web-and-markup/Angular/hello.component.ts) |  |
| Bookmarklet | [`bookmarklet.txt`](web-and-markup/Bookmarklet/bookmarklet.txt) |  |
| CSS | [`hello.css`](web-and-markup/CSS/hello.css) |  |
| HAML | [`hello.haml`](web-and-markup/HAML/hello.haml) |  |
| Handlebars | [`hello.hbs`](web-and-markup/Handlebars/hello.hbs) |  |
| HLSL | [`hello.hlsl`](web-and-markup/HLSL/hello.hlsl) |  |
| HTML | [`hello.html`](web-and-markup/HTML/hello.html) |  |
| Jinja2 | [`hello.j2`](web-and-markup/Jinja2/hello.j2) |  |
| JSP (JavaServer Pages) | [`hello.jsp`](web-and-markup/JSP-JavaServer-Pages/hello.jsp) |  |
| LaTeX | [`hello.tex`](web-and-markup/LaTeX/hello.tex) |  |
| Liquid | [`hello.liquid`](web-and-markup/Liquid/hello.liquid) |  |
| Markdown | [`hello.md`](web-and-markup/Markdown/hello.md) |  |
| Pug | [`hello.pug`](web-and-markup/Pug/hello.pug) |  |
| Razor (ASP.NET) | [`Hello.cshtml`](web-and-markup/Razor-ASP-NET/Hello.cshtml) |  |
| React (JSX) | [`Hello.jsx`](web-and-markup/React-JSX/Hello.jsx) |  |
| Svelte | [`Hello.svelte`](web-and-markup/Svelte/Hello.svelte) |  |
| SVG | [`hello.svg`](web-and-markup/SVG/hello.svg) |  |
| TeX (plain) | [`hello_plain.tex`](web-and-markup/TeX-plain/hello_plain.tex) |  |
| Vue | [`Hello.vue`](web-and-markup/Vue/Hello.vue) |  |
| WebGL / GLSL (fragment shader) | [`hello.frag`](web-and-markup/WebGL-GLSL-fragment-shader/hello.frag) |  |
| WGSL (WebGPU) | [`hello.wgsl`](web-and-markup/WGSL-WebGPU/hello.wgsl) |  |
| XQuery | [`hello.xq`](web-and-markup/XQuery/hello.xq) |  |
| XSLT | [`hello.xsl`](web-and-markup/XSLT/hello.xsl) | yes |

## Data & query (16)

| Language | File | Tested |
|---|---|:-:|
| Cypher (Neo4j) | [`hello.cypher`](data-and-query/Cypher-Neo4j/hello.cypher) |  |
| Excel formula | [`hello.excel.txt`](data-and-query/Excel-formula/hello.excel.txt) |  |
| Google Apps Script | [`Code.gs`](data-and-query/Google-Apps-Script/Code.gs) |  |
| GraphQL | [`hello.graphql`](data-and-query/GraphQL/hello.graphql) |  |
| JSON | [`hello.json`](data-and-query/JSON/hello.json) |  |
| Kusto (KQL) | [`hello.kql`](data-and-query/Kusto-KQL/hello.kql) |  |
| MySQL stored procedure | [`hello_mysql.sql`](data-and-query/MySQL-stored-procedure/hello_mysql.sql) |  |
| Oracle PL/SQL | [`hello_plsql.sql`](data-and-query/Oracle-PL-SQL/hello_plsql.sql) |  |
| PostgreSQL (PL/pgSQL) | [`hello_plpgsql.sql`](data-and-query/PostgreSQL-PL-pgSQL/hello_plpgsql.sql) |  |
| Protocol Buffers | [`hello.proto`](data-and-query/Protocol-Buffers/hello.proto) |  |
| Regex (PCRE) | [`hello.regex`](data-and-query/Regex-PCRE/hello.regex) |  |
| SPARQL | [`hello.rq`](data-and-query/SPARQL/hello.rq) |  |
| SQL | [`hello.sql`](data-and-query/SQL/hello.sql) | yes |
| T-SQL (SQL Server) | [`hello_tsql.sql`](data-and-query/T-SQL-SQL-Server/hello_tsql.sql) |  |
| TOML | [`hello.toml`](data-and-query/TOML/hello.toml) |  |
| YAML | [`hello.yaml`](data-and-query/YAML/hello.yaml) |  |

## Blockchain (7)

| Language | File | Tested |
|---|---|:-:|
| Bitcoin Script | [`hello.btc`](blockchain/Bitcoin-Script/hello.btc) |  |
| Cairo (StarkNet) | [`hello.cairo`](blockchain/Cairo-StarkNet/hello.cairo) |  |
| Clarity (Stacks) | [`hello.clar`](blockchain/Clarity-Stacks/hello.clar) |  |
| Michelson (Tezos) | [`hello.tz`](blockchain/Michelson-Tezos/hello.tz) |  |
| Move (Aptos/Sui) | [`hello.move`](blockchain/Move-Aptos-Sui/hello.move) |  |
| Solidity (Ethereum) | [`Hello.sol`](blockchain/Solidity-Ethereum/Hello.sol) |  |
| Vyper | [`hello.vy`](blockchain/Vyper/hello.vy) |  |

## Games, music & creative (18)

| Language | File | Tested |
|---|---|:-:|
| ChucK | [`hello.ck`](games-and-creative/ChucK/hello.ck) |  |
| Csound | [`hello.csd`](games-and-creative/Csound/hello.csd) |  |
| Gnuplot | [`hello.gp`](games-and-creative/Gnuplot/hello.gp) |  |
| Graphviz (DOT) | [`hello.dot`](games-and-creative/Graphviz-DOT/hello.dot) |  |
| Inform 7 | [`story.ni`](games-and-creative/Inform-7/story.ni) |  |
| LilyPond | [`hello.ly`](games-and-creative/LilyPond/hello.ly) |  |
| Mermaid | [`hello.mmd`](games-and-creative/Mermaid/hello.mmd) |  |
| Minecraft commands (mcfunction) | [`hello.mcfunction`](games-and-creative/Minecraft-commands-mcfunction/hello.mcfunction) |  |
| PlantUML | [`hello.puml`](games-and-creative/PlantUML/hello.puml) |  |
| Processing | [`hello.pde`](games-and-creative/Processing/hello.pde) |  |
| Ren'Py | [`script.rpy`](games-and-creative/Ren-Py/script.rpy) |  |
| Roblox Luau | [`hello.luau`](games-and-creative/Roblox-Luau/hello.luau) |  |
| Scratch (text form) | [`hello.scratch.txt`](games-and-creative/Scratch-text-form/hello.scratch.txt) |  |
| Sonic Pi | [`hello.sonicpi.rb`](games-and-creative/Sonic-Pi/hello.sonicpi.rb) |  |
| SuperCollider | [`hello.scd`](games-and-creative/SuperCollider/hello.scd) |  |
| Twine (Harlowe) | [`hello.twee`](games-and-creative/Twine-Harlowe/hello.twee) |  |
| UnityScript / C# (Unity) | [`Hello.cs`](games-and-creative/UnityScript-Csharp-Unity/Hello.cs) |  |
| Unreal Blueprint (UnrealScript classic) | [`Hello.uc`](games-and-creative/Unreal-Blueprint-UnrealScript-classic/Hello.uc) |  |

## Esoteric (21)

| Language | File | Tested |
|---|---|:-:|
| 05AB1E | [`hello.05ab1e`](esoteric/05AB1E/hello.05ab1e) |  |
| ArnoldC | [`hello.arnoldc`](esoteric/ArnoldC/hello.arnoldc) |  |
| Befunge-93 | [`hello.bf93`](esoteric/Befunge-93/hello.bf93) | yes |
| Brainfuck | [`hello.bf`](esoteric/Brainfuck/hello.bf) | yes |
| COW | [`hello.cow`](esoteric/COW/hello.cow) | yes |
| Emojicode | [`hello.emojic`](esoteric/Emojicode/hello.emojic) |  |
| FALSE | [`hello.f`](esoteric/FALSE/hello.f) |  |
| GolfScript | [`hello.gs`](esoteric/GolfScript/hello.gs) |  |
| HQ9+ | [`hello.hq9`](esoteric/HQ9p/hello.hq9) | yes |
| INTERCAL | [`hello.i`](esoteric/INTERCAL/hello.i) | yes |
| Jelly | [`hello.jelly`](esoteric/Jelly/hello.jelly) |  |
| LOLCODE | [`hello.lol`](esoteric/LOLCODE/hello.lol) |  |
| Malbolge | [`hello.mb`](esoteric/Malbolge/hello.mb) | yes |
| Ook! | [`hello.ook`](esoteric/Ook/hello.ook) | yes |
| Pyth | [`hello.pyth`](esoteric/Pyth/hello.pyth) |  |
| Rockstar | [`hello.rock`](esoteric/Rockstar/hello.rock) |  |
| Slashes (///) | [`hello.slashes`](esoteric/Slashes/hello.slashes) |  |
| Thue | [`hello.t`](esoteric/Thue/hello.t) | yes |
| Underload | [`hello.ul`](esoteric/Underload/hello.ul) | yes |
| Unlambda | [`hello.unl`](esoteric/Unlambda/hello.unl) | yes |
| Whitespace | [`hello.ws`](esoteric/Whitespace/hello.ws) | yes |

## Contributing

Missing a language ? Add a folder `<category>/<Language>/hello.<ext>` that prints `Hello, World!`.

## License

MIT
