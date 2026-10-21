// pixel shader: no text output on a GPU, so we just say hello in green
float4 main() : SV_Target
{
    return float4(0.0, 1.0, 0.25, 1.0);
}
