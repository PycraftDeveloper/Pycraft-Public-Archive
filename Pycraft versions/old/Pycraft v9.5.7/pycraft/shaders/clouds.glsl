#version 330

#if defined VERTEX_SHADER

in vec2 in_vert;

uniform float CloudColor;
uniform float CloudHeight;
uniform float CloudHeightMultiplier;
uniform float cull;
uniform sampler2D Heightmap;
uniform float height_max;
uniform mat4 m_camera;
uniform mat4 m_model;
uniform mat4 m_proj;
uniform float WeatherAlpha;
uniform float X_Offset;
uniform float Y_Offset;

out float col;
out vec4 mVertex;

void main() {//maybe future blend different cloud styles r g b
    float height = ((texture(Heightmap, in_vert.xy).r)*(CloudHeightMultiplier/3.5))-CloudHeight;
    col = ((1/(height_max*(CloudHeightMultiplier/3.5)))*(height+CloudHeight));

    mat4 m_view = m_camera * m_model;
    vec4 p = m_view * vec4((in_vert.x + X_Offset - 0.5) * 3200.0, -height, (in_vert.y + Y_Offset - 0.5) * 3200.0, 1.0);
    gl_Position =  m_proj * p;
    
    mVertex = gl_Position;
}

#elif defined FRAGMENT_SHADER

in float col;
in vec4 mVertex;

uniform vec4 CameraEye;
uniform float CloudColor;
uniform float cull;
uniform float DefaultSkyCol;
uniform float light_level;
uniform vec3 u_light;
uniform sampler2D u_sampler_billboard;
uniform sampler2DShadow u_sampler_shadow;
uniform float WeatherAlpha;
uniform float w_max;
uniform float w_min;
uniform bool render_fog;

out vec4 f_color;

float getFogFactor(float d, float w_max, float w_min)
{
        if (d >= w_max) discard;
        if (d <= w_min) return 0.0;

    if (render_fog == true) {
        return 1.0-(w_max - d) / (w_max - w_min);
    } else {
        return 0.0;
    }
}

void main() {
    vec4 V = mVertex;
    float d = distance(CameraEye, V);
    float alpha = getFogFactor(d, w_max, w_min);
    
    if (((1.0-alpha)*col) <= cull) {
        discard;
    } else {
        vec4 computed_color = vec4(DefaultSkyCol-(col/CloudColor));
        f_color = vec4(computed_color.r, computed_color.g, computed_color.b, (((1.0-alpha)*(col+WeatherAlpha)*2.0)));
    }
}
#endif