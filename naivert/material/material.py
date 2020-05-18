class Material(object):
    '''Class Maririal

    ** Input: **

    - n: float for refraction rate
    
    - f_reflect: list of three floats of the fraction of rgb that is reflected

    - f_refract: list of three floats of the fraction of rgb that is refracted

    - ks: list of three floats of the specular light coefficient 
    
    - kd: list of three floats of the diffusion light coefficient

    - ks: list of three float of the ambient light coefficient

    - alpha: gloss constant
    '''
    
    @classmethod
    def Glass(cls):
        return cls(
            n = 1.33,
            f_reflect=[0.05,0.05,0.05],
            f_refract=[0.95,0.95,0.95],
            ks = [0.95,0.95,0.95],
            kd = [0.02,0.02,0.02],
            ka = [0,0,0],
            alpha = [10,10,10]
            )

    


    def __init__(self,n,f_reflect,f_refract,ks,kd,ka,alpha):
        self.n = n
        self.f_reflect = f_reflect
        self.f_refract = f_refract
        self.ks = ks
        self.kd = kd
        self.ka = ka
        self.alpha = alpha

__all__ = ('Material',)
