module hello::hello {
    use std::debug;
    use std::string;

    public entry fun main() {
        debug::print(&string::utf8(b"Hello, World!"));
    }
}
