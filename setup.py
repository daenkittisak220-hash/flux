import curl -X POST https://api.bfl.ai/v1/flux-3-video \
  -H "x-key: $BFL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "mode": "i2v",
    "prompt": "from this frame the camera rises slowly above the alley as they rush away beneath the lanterns, their laughter fading into the night",
    "keyframes": "data:image/png;base64,<opening frame>"
  }'setuptools

setuptools.setup()
