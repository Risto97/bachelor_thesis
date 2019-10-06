$@$gear(svgen={'compile': True})
async def serialize(din: Array) -> b'din.dtype':
    async with din as val:
        for i in range(len(din.dtype)):
            yield val[i]
