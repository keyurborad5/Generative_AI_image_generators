from model import FluxModel

class FluxSchnell(FluxModel):
    def __init__(self)-> None :
        name = "black-forest-labs/FLUX.Schnell"
        save_path = "SavedModel/FLUX_Schnell"
        model = "FLUX.Schnell"
        super().__init__(name,save_path,model)
