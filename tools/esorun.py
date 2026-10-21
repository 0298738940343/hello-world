#!/usr/bin/env python3
"""esorun.py :: tiny interpreters for the esoteric Hello Worlds in this repo.

usage: python3 tools/esorun.py <bf|ook|cow|ws|befunge|unlambda|hq9|thue|underload|malbolge> FILE
"""
import sys

out = sys.stdout


def bf(code):
    code = [c for c in code if c in "+-<>[].,"]
    jump, st = {}, []
    for i, c in enumerate(code):
        if c == "[":
            st.append(i)
        elif c == "]":
            j = st.pop(); jump[i], jump[j] = j, i
    tape, p, pc = [0] * 30000, 0, 0
    while pc < len(code):
        c = code[pc]
        if c == ">": p += 1
        elif c == "<": p -= 1
        elif c == "+": tape[p] = (tape[p] + 1) % 256
        elif c == "-": tape[p] = (tape[p] - 1) % 256
        elif c == ".": out.write(chr(tape[p]))
        elif c == ",":
            ch = sys.stdin.read(1); tape[p] = ord(ch) if ch else 0
        elif c == "[" and tape[p] == 0: pc = jump[pc]
        elif c == "]" and tape[p] != 0: pc = jump[pc]
        pc += 1


def ook(code):
    m = {("Ook.", "Ook?"): ">", ("Ook?", "Ook."): "<", ("Ook.", "Ook."): "+",
         ("Ook!", "Ook!"): "-", ("Ook!", "Ook."): ".", ("Ook.", "Ook!"): ",",
         ("Ook!", "Ook?"): "[", ("Ook?", "Ook!"): "]"}
    w = code.split()
    bf("".join(m[(w[i], w[i + 1])] for i in range(0, len(w) - 1, 2)))


def cow(code):
    ops = ["moo", "mOo", "moO", "mOO", "Moo", "MOo", "MoO", "MOO", "OOO", "MMM", "OOM", "oom"]
    prog = [t for t in code.split() if t in ops]
    mem, p, pc, reg = [0] * 30000, 0, 0, None
    while pc < len(prog):
        t = prog[pc]
        if t == "moO": p += 1
        elif t == "mOo": p -= 1
        elif t == "MoO": mem[p] += 1
        elif t == "MOo": mem[p] -= 1
        elif t == "OOO": mem[p] = 0
        elif t == "OOM": out.write(str(mem[p]) + "\n")
        elif t == "Moo":
            if mem[p] == 0:
                ch = sys.stdin.read(1); mem[p] = ord(ch) if ch else 0
            else:
                out.write(chr(mem[p] % 256))
        elif t == "MMM":
            if reg is None: reg = mem[p]
            else: mem[p], reg = reg, None
        elif t == "MOO" and mem[p] == 0:
            depth, pc = 1, pc + 1
            while depth:
                pc += 1
                if prog[pc] == "MOO": depth += 1
                elif prog[pc] == "moo": depth -= 1
        elif t == "moo":
            depth = 1
            while depth:
                pc -= 1
                if prog[pc] == "moo": depth += 1
                elif prog[pc] == "MOO": depth -= 1
            pc -= 1
        pc += 1


def ws(code):
    c = [ch for ch in code if ch in " \t\n"]
    i, stack, heap = 0, [], {}

    def num():
        nonlocal i
        sign = 1 if c[i] == " " else -1; i += 1
        v = 0
        while c[i] != "\n":
            v = v * 2 + (1 if c[i] == "\t" else 0); i += 1
        i += 1
        return sign * v

    while i < len(c):
        a = c[i]
        if a == " ":                               # stack manipulation
            b = c[i + 1]; i += 2
            if b == " ": stack.append(num())
            elif b == "\n" and c[i] == " ": i += 1; stack.append(stack[-1])
            elif b == "\n" and c[i] == "\t": i += 1; stack[-1], stack[-2] = stack[-2], stack[-1]
            elif b == "\n" and c[i] == "\n": i += 1; stack.pop()
        elif a == "\t" and c[i + 1] == "\n":       # I/O
            x, y = c[i + 2], c[i + 3]; i += 4
            if x == " " and y == " ": out.write(chr(stack.pop()))
            elif x == " " and y == "\t": out.write(str(stack.pop()))
        elif a == "\n" and c[i + 1] == "\n" and c[i + 2] == "\n":
            return
        else:
            raise SystemExit("unsupported whitespace instruction in this tiny interpreter")


def befunge(code):
    g = [list(l.ljust(80)) for l in code.split("\n")] + [list(" " * 80)] * 25
    g = [r[:80] for r in g[:25]]
    x = y = 0; dx, dy = 1, 0; st = []; sm = False
    pop = lambda: st.pop() if st else 0
    for _ in range(10 ** 6):
        ch = g[y][x]
        if sm:
            if ch == '"': sm = False
            else: st.append(ord(ch))
        elif ch == '"': sm = True
        elif ch == ">": dx, dy = 1, 0
        elif ch == "<": dx, dy = -1, 0
        elif ch == "^": dx, dy = 0, -1
        elif ch == "v": dx, dy = 0, 1
        elif ch == ":": v = pop(); st += [v, v]
        elif ch == ",": out.write(chr(pop()))
        elif ch == ".": out.write(str(pop()) + " ")
        elif ch == "_": dx, dy = (1, 0) if pop() == 0 else (-1, 0)
        elif ch == "|": dx, dy = (0, 1) if pop() == 0 else (0, -1)
        elif ch == "#": x, y = (x + dx) % 80, (y + dy) % 25
        elif ch == "$": pop()
        elif ch == "+": b, a = pop(), pop(); st.append(a + b)
        elif ch.isdigit(): st.append(int(ch))
        elif ch == "@": return
        x, y = (x + dx) % 80, (y + dy) % 25


def unlambda(code):
    # supports the subset used here: ` application, .x print, r newline, i identity
    toks, i = [], 0
    s = "".join(code.split("#")[0].split()) if False else code
    while i < len(s):
        ch = s[i]
        if ch == ".":
            toks.append(("." , s[i + 1])); i += 2; continue
        if ch in "`ri":
            toks.append((ch, None))
        i += 1
    pos = 0

    def parse():
        nonlocal pos
        t = toks[pos]; pos += 1
        if t[0] == "`":
            return ("app", parse(), parse())
        return t

    def ev(e):
        if e[0] == "app":
            f, a = ev(e[1]), ev(e[2])
            if f[0] == ".": out.write(f[1]); return a
            if f[0] == "r": out.write("\n"); return a
            if f[0] == "i": return a
        return e

    ev(parse())


def hq9(code):
    for ch in code:
        if ch in "Hh": out.write("Hello, World!\n")


def thue(code):
    rules, rest = [], code.split("\n")
    while True:
        l = rest.pop(0)
        if l.strip() == "::=": break
        lhs, rhs = l.split("::=", 1); rules.append((lhs, rhs))
    state = "\n".join(rest).strip()
    changed = True
    while changed:
        changed = False
        for lhs, rhs in rules:
            if lhs in state:
                if rhs.startswith("~"):
                    out.write(rhs[1:] + "\n"); rhs = ""
                state = state.replace(lhs, rhs, 1); changed = True
                break


def underload(code):
    st, prog = [], code.strip()
    i = 0
    while i < len(prog):
        ch = prog[i]
        if ch == "(":
            d, j = 1, i + 1
            while d:
                d += {"(": 1, ")": -1}.get(prog[j], 0); j += 1
            st.append(prog[i + 1:j - 1]); i = j; continue
        if ch == "S": out.write(st.pop())
        i += 1
    out.write("\n")


def malbolge(code):
    xlat2 = ("5z]&gqtyfr$(we4{WP)H-Zn,[%\\3dL+Q;>U!pJS72FhOA1CB6v^=I_0/8|jsb9m<.TVac`uY*MK'X~xDl}REokN:#?G\"i@")
    tbl = [[1, 0, 0], [1, 0, 2], [2, 2, 1]]

    def crz(a, d):
        r, p = 0, 1
        for _ in range(10):
            r += tbl[d % 3][a % 3] * p
            a //= 3; d //= 3; p *= 3
        return r

    mem = [0] * 59049; i = 0
    for ch in code:
        if ch.isspace(): continue
        if (ord(ch) + i) % 94 not in (4, 5, 23, 39, 40, 62, 68, 81):
            raise SystemExit("invalid malbolge character")
        mem[i] = ord(ch); i += 1
    while i < 59049:
        mem[i] = crz(mem[i - 1], mem[i - 2]); i += 1
    a = c = d = 0
    for _ in range(10 ** 7):
        if not 33 <= mem[c] <= 126: return
        op = (mem[c] + c) % 94
        if op == 4: c = mem[d]
        elif op == 5: out.write(chr(a % 256))
        elif op == 23:
            ch = sys.stdin.read(1); a = ord(ch) if ch else 59048
        elif op == 39:
            a = mem[d] = mem[d] // 3 + (mem[d] % 3) * 19683
        elif op == 40: d = mem[d]
        elif op == 62: a = mem[d] = crz(a, mem[d])
        elif op == 81: return
        if 33 <= mem[c] <= 126: mem[c] = ord(xlat2[mem[c] - 33])
        c = (c + 1) % 59049; d = (d + 1) % 59049


if __name__ == "__main__":
    lang, path = sys.argv[1], sys.argv[2]
    with open(path, encoding="utf-8") as f:
        globals()[lang](f.read())
    out.flush()
