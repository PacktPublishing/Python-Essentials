import argparse
import sys
import Chapter_12.config_params as config_params

parser= argparse.ArgumentParser()
parser.add_argument("--env", default="DEV")
options= parser.parse_args()

# Simple
#Config = getattr(config_params, options.env)

# Hairy
Base= getattr(config_params, options.env)
class Config(Base):
    def __repr__(self):
        names= {}
        for cls in reversed(self.__class__.__mro__):
            cls_names= dict((nm, (cls.__name__, val)) for nm,val in cls.__dict__.items() if nm[0] != "_")
            names.update( cls_names )
        return ", ".join( "{0}.{1}={2}".format(class_val[0], nm, class_val[1]) for nm,class_val in names.items() )

Config.options= options

print( __name__, Config() )