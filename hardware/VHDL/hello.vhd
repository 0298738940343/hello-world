use std.textio.all;

entity hello is
end hello;

architecture behaviour of hello is
begin
  process
  begin
    write(output, String'("Hello, World!") & LF);
    wait;
  end process;
end behaviour;
