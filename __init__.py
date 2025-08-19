from Flux_1_dev import Flux1_dev
from Flux_schnell import FluxSchnell


def main():
    dev= Flux1_dev()
    dev.generate_image("Racing Street dogs","dog_race")

    '''
    Case when we don not hav model'''
    # schnell= FluxSchnell()
    # schnell.save_model() # Use just to save model, Once saved Just comment it
    # ## uncomnet below to generate image
    # schnell.generate_image("A dog racing in a city park", "dog_race_2")



if __name__=="__main__":
    main()