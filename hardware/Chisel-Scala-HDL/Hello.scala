import chisel3._

class Hello extends Module {
  val io = IO(new Bundle {})
  printf("Hello, World!\n")
}
