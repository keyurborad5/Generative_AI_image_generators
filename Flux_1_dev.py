from model import FluxModel

class Flux1_dev(FluxModel):
    def __init__(self)-> None :
        name = "black-forest-labs/FLUX.1-dev"
        save_path = "SavedModel/FLUX_1-dev"
        model = "FLUX.1-dev"
        super().__init__(name,save_path,model)

