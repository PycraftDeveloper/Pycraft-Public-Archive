#version 330

#if defined VERTEX_SHADER

uniform mat4 Mvp;

in vec3 in_position;
in vec3 in_normal;
in vec2 in_texcoord_0;

out vec3 v_vert;
out vec3 v_norm;
out vec2 v_text;

void main() {
    gl_Position = Mvp * vec4(in_position, 1.0);
    v_vert = in_position;
    v_norm = in_normal;
    v_text = in_texcoord_0;
}
                
#elif defined FRAGMENT_SHADER

uniform vec3 Light;
uniform sampler2D Texture;

in vec3 v_vert;
in vec3 v_norm;
in vec2 v_text;

out vec4 f_color;

void main() {
    float lum = clamp(dot(normalize(Light - v_vert), normalize(v_norm)), 0.0, 1.0) * 0.8 + 0.2;
    f_color = vec4(texture(Texture, v_text).rgb * lum, 1.0);
}
#endif