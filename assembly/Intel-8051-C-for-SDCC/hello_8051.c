#include <8051.h>

void putchar_(char c) { SBUF = c; while (!TI); TI = 0; }

void main(void) {
    const char *s = "Hello, World!\r\n";
    SCON = 0x50; TMOD = 0x20; TH1 = 0xFD; TR1 = 1; TI = 0;
    while (*s) putchar_(*s++);
    while (1);
}
