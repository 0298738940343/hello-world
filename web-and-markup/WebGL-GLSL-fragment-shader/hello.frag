// shaders can't print text: this one paints the screen "Hello, World!" green
precision mediump float;

void main() {
    gl_FragColor = vec4(0.0, 1.0, 0.25, 1.0);
}
