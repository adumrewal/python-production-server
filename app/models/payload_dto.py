class HeroInfoPayloadDTO():
    def __init__(self, payload) -> None:
        self.hero_name = payload['hero_name'] # compulsory payload field
        self.universe_name = payload.get('universe_name') or 'marvel' # optional payload field
