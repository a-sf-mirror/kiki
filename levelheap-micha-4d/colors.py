
if Controller.isDebugVersion(): print '[colors.py]'

# .................................................................................................................
# ........................................................ apply color scheme
def applyColorScheme (scheme):
    """applies the color scheme"""
    for item in scheme.items():
        for subitem in item[1].items():
            colorstr = str(subitem[1])
            color = apply(KColor, subitem[1])
            eval(item[0]+".setObjectColor(\'"+subitem[0]+"\', color)")


# ........................................................michas default color_scheme
tron_scheme = {       # red green blue transparency
        "KikiWorld":        {   "base":         (0.0, 0.0, 0.3), 
                                "plate":        (0.05, 0.05, 0.2), 
                            },

        "KikiLight":        {   "base":         (0.0, 0.0, 1.0),
                                "diffuse":      (0.0, 0.0, 1.0),
                                "specular":     (0.0, 0.0, 1.0),
                                "halo":         (0.0, 0.0, 1.0),
                            },
        "KikiSpikes":       {   "base":         (0.5, 0.5, 0.5),
                            },
        "KikiBomb":         {   "base":         (0.5, 0.0, 0.0),
                            },
        "KikiStone":        {   "base":         (0.0, 0.0, 1.0, 1.0),
                            },
        "KikiMovesAtom":   {   "base":         (0.5, 0.5, 0.0, 0.4),
                                "neutron":      (0.0, 0.5, 0.0, 0.2),
        
	                    },
#        "KikiHealthAtom":   {   "base":         (0.0, 0.5, 0.0, 0.8),
#                                "neutron":      (0.5, 1.0, 0.0, 0.8),
#                            },
        "KikiSwitch":       {   "base":         (0.0, 0.0, 0.5, 0.8),
                                "sphere":       (1.0, 1.0, 0.0, 0.8),     
                            },
        "KikiGate":         {   "base":         (1.0, 1.0, 0.0, 0.8),
                                "sphere":       (1.0, 1.0, 0.0, 0.8),
                            },
        "KikiPlayer":       {   "base":         (0.5, 0.5, 0.5),
                                "dead":         (0.3, 0.1, 0.0),
                                "tire":         (0.0, 0.0, 0.5),
                            },
        "KikiMutant":       {   "base":         (0.5, 0.0, 0.0),
                                "dead":         (0.0, 0.0, 0.2, 0.4),
                                "tire":         (0.0, 0.0, 0.2),
                            },
        "KikiText":         {   "base":         (0.8, 0.8, 0.0),
                                "bright":       (1.0, 1.0, 0.0),
                                "dark":         (0.6, 0.4, 0.0),
                            },
        "KikiGear":         {   "base":         (0.1, 0.1, 0.9, 0.9), 
                            },
        "KikiValve":        {   "base":         (0.0, 0.0, 0.5, 0.9), 
                            },
        "KikiMotorCylinder":{   "base":         (0.0, 0.0, 0.6, 0.9), 
                            },
        "KikiMotorGear":    {   "base":         (0.0, 0.0, 0.6, 0.9), 
                            },
        "KikiGenerator":    {   "base":         (0.0, 0.0, 0.5, 0.9), 
                            },
        "KikiWire":         {   "base":         (0.1, 0.1, 0.9, 0.6),
                                "light":        (1.0, 1.0, 0.0), 
                            },
    }
# ...........(copy of default................................. nearly default color_scheme
neutron_scheme = {        
        "KikiWorld":        {   "base":         (0.13, 0.13, 0.13), 
                                "plate":        (0.5, 0.5, 0.5), 
                            },

        "KikiLight":        {   "base":         (0.0, 0.0, 0.0),
                                "diffuse":      (1.0, 1.0, 1.0),
                                "specular":     (1.0, 1.0, 1.0),
                                "halo":         (1.0, 1.0, 1.0),
                            },
        "KikiSpikes":       {   "base":         (0.5, 0.5, 0.5),
                            },
        "KikiBomb":         {   "base":         (0.5, 0.0, 0.0),
                            },
        "KikiStone":        {   "base":         (0.5, 0.5, 0.5, 0.5),
                            },
        
	"KikiMovesAtom":   {   "base":         (1.0, 1.0, 0.0, 0.5),
                                "neutron":      (0.0, 1.0, 0.0, 0.3),
                            },
#        "KikiHealthAtom":   {   "base":         (0.0, 0.5, 0.0, 0.8),
#                                "neutron":      (0.5, 1.0, 0.0, 0.8),
#                            },
        "KikiSwitch":       {   "base":         (0.0, 0.0, 0.5, 0.8),
                                "sphere":       (1.0, 1.0, 0.0, 0.8),     
                            },
        "KikiGate":         {   "base":         (1.0, 1.0, 0.0, 0.8),
                                "sphere":       (1.0, 1.0, 0.0, 0.8),
                            },
        "KikiPlayer":       {   "base":         (1.0, 0.5, 0.0),
                                "dead":         (0.3, 0.1, 0.0),
                                "tire":         (0.5, 0.0, 0.0),
                            },
        "KikiMutant":       {   "base":         (0.5, 0.0, 0.0),
                                "dead":         (0.0, 0.0, 0.2, 0.4),
                                "tire":         (0.0, 0.0, 0.2),
                            },
        "KikiText":         {   "base":         (0.8, 0.8, 0.0),
                                "bright":       (1.0, 1.0, 0.0),
                                "dark":         (0.6, 0.4, 0.0),
                            },
        "KikiGear":         {   "base":         (1.0, 0.0, 0.0, 0.0), #!!!
                            },
        "KikiValve":        {   "base":         (1.0, 0.0, 0.0, 0.0), #!!!
                            },
        "KikiMotorCylinder":{   "base":         (0.0, 0.0, 0.6, 0.9), 
                            },
        "KikiMotorGear":    {   "base":         (0.0, 0.0, 0.6, 0.9), 
                            },
        "KikiGenerator":    {   "base":         (0.0, 0.0, 0.5, 0.9), 
                            },
        "KikiWire":         {   "base":         (0.1, 0.1, 0.9, 0.6),
                                "light":        (1.0, 1.0, 0.0), 
                            },
    }

# ........................................................ test color scheme
test_scheme = {        
        "KikiWorld":        {   "base":         (1.0, 1.0, 1.0), 
                                "plate":        (0.08, 0.08, 0.08), 
                            },
        "KikiLight":        {   "base":         (0.0, 0.0, 0.0),
                                "diffuse":      (1.0, 1.0, 1.0),
                                "specular":     (1.0, 1.0, 1.0),
                                "halo":         (1.0, 1.0, 1.0),
                            },
        "KikiSpikes":       {   "base":         (0.5, 0.5, 0.5),
                            },
        "KikiBomb":         {   "base":         (0.5, 0.0, 0.0),
                            },
        "KikiStone":        {   "base":         (0.5, 0.5, 0.5, 0.5),
                            },
        "KikiMovesAtom":    {   "base":         (0.5, 0.0, 0.0, 0.8),
                                "neutron":      (1.0, 0.5, 0.0, 0.8),
                            },
#        "KikiHealthAtom":   {   "base":         (0.0, 0.5, 0.0, 0.8),
#                                "neutron":      (0.5, 1.0, 0.0, 0.8),
#                            },
        "KikiSwitch":       {   "base":         (0.0, 0.0, 0.5, 0.8),
                                "sphere":       (1.0, 1.0, 0.0, 0.8),     
                            },
        "KikiGate":         {   "base":         (1.0, 1.0, 0.0, 0.8),
                                "sphere":       (1.0, 1.0, 0.0, 0.8),
                            },
        "KikiPlayer":       {   "base":         (1.0, 0.5, 0.0),
                                "dead":         (0.3, 0.1, 0.0),
                                "tire":         (0.5, 0.0, 0.0),
                            },
        "KikiMutant":       {   "base":         (1.0, 0.5, 0.0),
                                "dead":         (0.3, 0.1, 0.0),
                                "tire":         (0.5, 0.0, 0.0),
                            },
        "KikiText":         {   "base":         (0.8, 0.8, 0.0),
                                "bright":       (1.0, 1.0, 0.0),
                                "dark":         (0.6, 0.4, 0.0),
                            },
        "KikiGear":         {   "base":         (0.1, 0.1, 0.9, 0.9), 
                            },
        "KikiValve":        {   "base":         (0.0, 0.0, 0.5, 0.9), 
                            },
        "KikiMotorCylinder":{   "base":         (0.0, 0.0, 0.6, 0.9), 
                            },
        "KikiMotorGear":    {   "base":         (0.0, 0.0, 0.6, 0.9), 
                            },
        "KikiGenerator":    {   "base":         (0.0, 0.0, 0.5, 0.9), 
                            },
        "KikiWire":         {   "base":         (0.1, 0.1, 0.9, 0.6),
                                "light":        (1.0, 1.0, 0.0), 
                            },
    }

# ........................................................ candy color scheme
candy_scheme = {        
        "KikiWorld":        {   "base":         (0.35, 0.0, 0.35), 
                                "plate":        (0.8, 0.0, 0.9), 
                            },
        "KikiLight":        {   "base":         (0.0, 0.0, 0.0),
                                "diffuse":      (1.0, 0.5, 0.0),
                                "specular":     (1.0, 0.0, 1.0),
                                "halo":         (1.0, 1.0, 1.0),
                            },
        "KikiText":         {   "base":         (0.7, 0.0, 0.7),
                                "bright":       (1.0, 0.0, 1.0),
                                "dark":         (0.4, 0.0, 0.4),
                            },
        "KikiBomb":         {   "base":         (0.73, 0.0, 0.75),
                            },
        "KikiStone":        {   "base":         (0.85, 0.0, 0.95, 0.6),
                            },
        "KikiSpikes":       {   "base":         (0.8, 0.0, 0.8),
                            },
        "KikiMovesAtom":    {   "base":         (0.5, 0.0, 0.5, 0.8),
                                "neutron":      (1.0, 0.0, 1.0, 0.8),
                            },
#        "KikiHealthAtom":   {   "base":         (1.0, 0.0, 1.0, 0.8),
#                                "neutron":      (0.6, 0.0, 0.6, 0.8),
#                            },
        "KikiSwitch":       {   "base":         (0.3, 0.0, 0.3, 0.8),
                                "sphere":       (1.0, 0.0, 1.0, 0.8),     
                            },
        "KikiGate":         {   "base":         (1.0, 0.0, 1.0, 0.8),
                                "sphere":       (1.0, 0.0, 1.0, 0.8),
                            },
        "KikiPlayer":       {   "base":         (0.7, 0.0, 0.7),
                                "tire":         (0.3, 0.0, 0.3),
                            },
        "KikiMutant":       {   "base":         (0.3, 0.0, 0.3),
                                "dead":         (0.2, 0.0, 0.45, 0.5),
                                "tire":         (0.7, 0.0, 0.7),
                            },
        "KikiBotFume":      {   "base":         (1.0, 0.0, 1.0, 0.5),
                            },
        "KikiValve":        {   "base":         (0.5, 0.0, 0.5, 0.9),
                            },
        "KikiGear":         {   "base":         (0.7, 0.0, 0.7, 0.8),
                            },
        "KikiWire":         {   "base":         (1.0, 0.0, 1.0),
                                "light":        (1.0, 1.0, 0.0),
                            },
        "KikiGenerator":    {   "base":         (0.5, 0.0, 0.5, 0.9),
                            },
        "KikiMotorCylinder":{   "base":         (1.0, 0.0, 1.0, 0.9),
                            },
        "KikiMotorGear":    {   "base":         (1.0, 0.0, 1.0, 0.9),
                            },
    }

# ........................................................ default color_scheme
default_scheme = {        
        "KikiWorld":        {   "base":         (0.13, 0.13, 0.13), 
                                "plate":        (0.5, 0.5, 0.5), 
                            },

        "KikiLight":        {   "base":         (0.0, 0.0, 0.0),
                                "diffuse":      (1.0, 1.0, 1.0),
                                "specular":     (1.0, 1.0, 1.0),
                                "halo":         (1.0, 1.0, 1.0),
                            },
        "KikiSpikes":       {   "base":         (0.5, 0.5, 0.5),
                            },
        "KikiBomb":         {   "base":         (0.5, 0.0, 0.0),
                            },
        "KikiStone":        {   "base":         (0.5, 0.5, 0.5, 0.5),
                            },
        "KikiMovesAtom":   {   "base":         (0.5, 0.0, 0.0, 0.8),
                                "neutron":      (1.0, 0.5, 0.0, 0.8),
                            },
#        "KikiHealthAtom":   {   "base":         (0.0, 0.5, 0.0, 0.8),
#                                "neutron":      (0.5, 1.0, 0.0, 0.8),
#                            },
        "KikiSwitch":       {   "base":         (0.0, 0.0, 0.5, 0.8),
                                "sphere":       (1.0, 1.0, 0.0, 0.8),     
                            },
        "KikiGate":         {   "base":         (1.0, 1.0, 0.0, 0.8),
                                "sphere":       (1.0, 1.0, 0.0, 0.8),
                            },
        "KikiPlayer":       {   "base":         (1.0, 0.5, 0.0),
                                "dead":         (0.3, 0.1, 0.0),
                                "tire":         (0.5, 0.0, 0.0),
                            },
        "KikiMutant":       {   "base":         (0.5, 0.0, 0.0),
                                "dead":         (0.0, 0.0, 0.2, 0.4),
                                "tire":         (0.0, 0.0, 0.2),
                            },
        "KikiText":         {   "base":         (0.8, 0.8, 0.0),
                                "bright":       (1.0, 1.0, 0.0),
                                "dark":         (0.6, 0.4, 0.0),
                            },
        "KikiGear":         {   "base":         (0.1, 0.1, 0.9, 0.9), 
                            },
        "KikiValve":        {   "base":         (0.0, 0.0, 0.5, 0.9), 
                            },
        "KikiMotorCylinder":{   "base":         (0.0, 0.0, 0.6, 0.9), 
                            },
        "KikiMotorGear":    {   "base":         (0.0, 0.0, 0.6, 0.9), 
                            },
        "KikiGenerator":    {   "base":         (0.0, 0.0, 0.5, 0.9), 
                            },
        "KikiWire":         {   "base":         (0.1, 0.1, 0.9, 0.6),
                                "light":        (1.0, 1.0, 0.0), 
                            },
    }

# ........................................................ bronze color scheme
bronze_scheme = {        
        "KikiWorld":        {   "base":         (0.25, 0.15, 0.05), 
                                "plate":        (0.8, 0.6, 0.2), 
                            },
        "KikiLight":        {   "base":         (0.1, 0.1, 0.0),
                                "diffuse":      (0.4, 0.2, 0.1),
                                "specular":     (1.0, 1.0, 0.5),
                                "halo":         (1.0, 0.9, 0.2),
                            },
        "KikiSpikes":       {   "base":         (0.8, 0.6, 0.2),
                            },
        "KikiStone":        {   "base":         (1.0, 0.8, 0.4, 0.8),
                            },
        "KikiMovesAtom":   {   "base":         (0.4, 0.4, 0.1, 0.8),
                                "neutron":      (0.4, 0.4, 0.1, 0.8),
                            },
#        "KikiHealthAtom":   {   "base":         (0.7, 0.4, 0.1, 0.8),
#                                "neutron":      (0.7, 0.4, 0.1, 0.8),
#                            },
        "KikiSwitch":       {   "base":         (0.9, 0.7, 0.1, 0.8),
                                "sphere":       (1.0, 1.0, 0.7, 0.8),     
                            },
        "KikiGate":         {   "base":         (0.9, 0.7, 0.1),
                                "sphere":       (1.0, 0.8, 0.1, 0.8),
                            },
        "KikiPlayer":       {   "base":         (0.8, 0.6, 0.3),
                                "dead":         (0.4, 0.1, 0.0),
                                "tire":         (0.5, 0.2, 0.1),
                            },
        "KikiMutant":       {   "base":         (0.5, 0.2, 0.1, 0.8),
                                "dead":         (0.5, 0.2, 0.1, 0.4),
                                "tire":         (0.3, 0.1, 0.0),
                            },
        "KikiBotFume":      {   "base":          (1.0, 0.5, 0.1, 0.5),
                            },
        "KikiGear":         {   "base":         (0.7, 0.4, 0.1, 0.9), 
                            },
        "KikiValve":        {   "base":         (0.5, 0.2, 0.1, 0.9), 
                            },
        "KikiGenerator":    {   "base":         (0.7, 0.5, 0.3, 0.9), 
                            },
        "KikiMotorCylinder":{   "base":         (0.8, 0.6, 0.2, 0.9), 
                            },
        "KikiMotorGear":    {   "base":         (0.8, 0.6, 0.2, 0.9), 
                            },
        "KikiWire":         {   "base":         (0.7, 0.5, 0.3, 0.9),
                                "light":        (1.0, 1.0, 0.0), 
                            },
        "KikiBomb":         {   "base":         (0.9, 0.7, 0.1),
                            },
        "KikiText":         {   "base":         (0.7, 0.5, 0.1),
                                "bright":       (0.9, 0.7, 0.15),
                                "dark":         (0.6, 0.4, 0.0),
                            },
    }

# ........................................................ red color scheme
red_scheme = {        
        "KikiWorld":        {   "base":         (0.2, 0.0, 0.0), 
                                "plate":        (0.3, 0.0, 0.0), 
                            },
        "KikiLight":        {   "base":         (0.1, 0.1, 0.1),
                                "diffuse":      (1.0, 1.0, 0.0),
                                "specular":     (1.0, 1.0, 0.0),
                                "halo":         (1.0, 1.0, 0.0),
                            },
        "KikiBomb":         {   "base":         (0.5, 0.0, 0.0),
                            },
        "KikiStone":        {   "base":         (0.5, 0.0, 0.0, 0.6),
                            },
        "KikiSpikes":       {   "base":         (0.3, 0.0, 0.0),
                            },
        "KikiMovesAtom":   {   "base":         (0.4, 0.0, 0.0, 0.6),
                                "neutron":      (0.5, 0.0, 0.0, 0.6),
                            },
#        "KikiHealthAtom":   {   "base":         (0.6, 0.0, 0.0, 0.6),
#                                "neutron":      (0.5, 0.5, 0.0, 0.6),
#                            },
        "KikiSwitch":       {   "base":         (0.8, 0.0, 0.0, 0.8),
                                "sphere":       (1.0, 1.0, 0.1, 0.8),     
                            },
        "KikiGate":         {   "base":         (1.0, 0.2, 0.0, 0.8),
                                "sphere":       (1.0, 1.0, 0.1, 0.8),
                            },
        "KikiPlayer":       {   "base":         (0.7, 0.0, 0.0),
                                "tire":         (0.3, 0.0, 0.0),
                            },
        "KikiMutant":       {   "base":         (0.3, 0.0, 0.0),
                                "dead":         (0.2, 0.0, 0.0, 0.5),
                                "tire":         (0.7, 0.0, 0.0),
                            },
        "KikiBotFume":      {   "base":         (1.0, 1.0, 0.0, 0.5),
                            },
        "KikiValve":        {   "base":         (0.5, 0.2, 0.0),
                            },
        "KikiGear":         {   "base":         (1.0, 0.5, 0.0, 0.5),
                            },
        "KikiWire":         {   "base":         (0.5, 0.0, 0.0),
                            },
        "KikiGenerator":    {   "base":         (0.5, 0.0, 0.0),
                            },
        "KikiMotorCylinder":{   "base":         (0.25, 0.0, 0.0),
                            },
        "KikiMotorGear":    {   "base":         (0.25, 0.0, 0.0),
                            },
        "KikiText":         {   "base":         (1.0, 0.5, 0.0),
                                "bright":       (1.0, 0.8, 0.0),
                                "dark":         (0.4, 0.2, 0.0),
                            },
    }

# ........................................................ blue color scheme
blue_scheme = {        
        "KikiWorld":        {   "base":         (0.0, 0.0, 0.2), 
                                "plate":        (0.1, 0.1, 0.6), 
                            },
        "KikiLight":        {   "base":         (0.1, 0.1, 0.1),
                                "diffuse":      (1.0, 1.0, 1.0),
                                "specular":     (1.0, 1.0, 1.0),
                                "halo":         (1.0, 1.0, 1.0),
                            },
        "KikiStone":        {   "base":         (0.0, 0.0, 0.5, 0.6),
                            },
        "KikiSpikes":       {   "base":         (0.1, 0.1, 0.6, 0.8),
                            },
        "KikiMovesAtom":   {   "base":         (0.0, 0.0, 0.6, 0.6),
                                "neutron":      (0.2, 0.2, 0.8, 0.6),
                            },
#        "KikiHealthAtom":   {   "base":         (0.0, 0.0, 0.6, 0.6),
#                                "neutron":      (0.5, 0.5, 0.9, 0.6),
#                            },
        "KikiSwitch":       {   "base":         (0.0, 0.0, 0.6, 0.8),
                                "sphere":       (1.0, 1.0, 1.0, 0.8),     
                            },
        "KikiBomb":         {   "base":         (0.2, 0.2, 0.9, 0.8),
                            },
        "KikiGate":         {   "base":         (0.0, 0.2, 1.0),
                                "sphere":       (1.0, 1.0, 1.0, 0.8),
                            },
        "KikiPlayer":       {   "base":         (0.0, 0.0, 0.7),
                                "tire":         (0.0, 0.0, 0.3),
                            },
        "KikiBotFume":      {   "base":         (0.5, 0.5, 1.0, 0.5),
                            },
        "KikiMutant":       {   "base":         (0.0, 0.0, 0.3),
                                "dead":         (0.0, 0.0, 0.2, 0.5),
                                "tire":         (0.0, 0.0, 0.7),
                            },
        "KikiText":         {   "base":         (0.2, 0.4, 0.8),
                                "bright":       (0.7, 0.8, 1.0),
                                "dark":         (0.0, 0.0, 0.6),
                            },
        "KikiGear":         {   "base":         (0.1, 0.1, 0.9, 0.9), 
                            },
        "KikiValve":        {   "base":         (0.0, 0.0, 0.5, 0.9), 
                            },
        "KikiMotorCylinder":{   "base":         (0.0, 0.0, 0.6, 0.9), 
                            },
        "KikiMotorGear":    {   "base":         (0.0, 0.0, 0.6, 0.9), 
                            },
        "KikiGenerator":    {   "base":         (0.0, 0.0, 0.5, 0.9), 
                            },
        "KikiWire":         {   "base":         (0.1, 0.1, 0.9, 0.6),
                                "light":        (1.0, 0.5, 0.0), 
                            },
    }

# ........................................................ yellow color scheme
yellow_scheme = {        
        "KikiWorld":        {   "base":         (0.34, 0.34, 0.0), 
                                "plate":        (0.9, 0.9, 0.0), 
                            },
        "KikiLight":        {   "base":         (0.0, 0.0, 0.0),
                                "diffuse":      (1.0, 0.5, 0.0),
                                "specular":     (1.0, 0.5, 0.0),
                                "halo":         (1.0, 1.0, 0.0),
                            },
        "KikiBomb":         {   "base":         (0.75, 0.75, 0.0),
                            },
        "KikiStone":        {   "base":         (0.8, 0.85, 0.0, 0.6),
                            },
        "KikiSpikes":       {   "base":         (0.8, 0.8, 0.0),
                            },
        "KikiMovesAtom":   {   "base":         (0.5, 0.5, 0.0, 0.8),
                                "neutron":      (1.0, 1.0, 0.0, 0.8),
                            },
#        "KikiHealthAtom":   {   "base":         (1.0, 1.0, 0.0, 0.8),
#                                "neutron":      (0.6, 0.6, 0.0, 0.8),
#                            },
        "KikiSwitch":       {   "base":         (0.8, 0.8, 0.0, 0.8),
                                "sphere":       (1.0, 1.0, 0.0, 0.8),     
                            },
        "KikiGate":         {   "base":         (1.0, 1.0, 0.0, 0.8),
                                "sphere":       (1.0, 1.0, 0.0, 0.8),
                            },
        "KikiPlayer":       {   "base":         (0.7, 0.7, 0.0),
                                "tire":         (0.3, 0.3, 0.0),
                            },
        "KikiMutant":       {   "base":         (0.3, 0.3, 0.0),
                                "dead":         (0.2, 0.2, 0.0, 0.5),
                                "tire":         (0.7, 0.7, 0.0),
                            },
        "KikiBotFume":      {   "base":         (1.0, 1.0, 0.0, 0.5),
                            },
        "KikiValve":        {   "base":         (0.5, 0.5, 0.0, 0.9),
                            },
        "KikiGear":         {   "base":         (0.7, 0.5, 0.0, 0.8),
                            },
        "KikiWire":         {   "base":         (1.0, 1.0, 0.0),
                                "light":        (0.0, 0.0, 1.0),
                            },
        "KikiGenerator":    {   "base":         (0.5, 0.5, 0.0, 0.9),
                            },
        "KikiMotorCylinder":{   "base":         (0.95, 0.95, 0.0),
                            },
        "KikiMotorGear":    {   "base":         (0.95, 0.95, 0.0),
                            },
        "KikiText":         {   "base":         (0.7, 0.7, 0.0),
                                "bright":       (1.0, 1.0, 0.0),
                                "dark":         (0.4, 0.4, 0.0),
                            },
    }

# ........................................................ green color scheme
green_scheme = {        
        "KikiWorld":        {   "base":         (0.0, 0.2, 0.0), 
                                "plate":        (0.1, 0.6, 0.1), 
                            },
        "KikiLight":        {   "base":         (0.0, 0.0, 0.0),
                                "diffuse":      (0.5, 1.0, 0.5),
                                "specular":     (0.7, 1.0, 0.7),
                                "halo":         (1.0, 1.0, 1.0),
                            },
        "KikiStone":        {   "base":         (0.0, 0.5, 0.0, 0.6),
                            },
        "KikiSpikes":       {   "base":         (0.0, 0.6, 0.0, 0.8),
                            },
        "KikiMovesAtom":   {   "base":         (0.0, 0.6, 0.0, 0.6),
                                "neutron":      (0.0, 0.8, 0.0, 0.6),
                            },
#        "KikiHealthAtom":   {   "base":         (0.0, 0.98, 0.0, 0.6),
#                                "neutron":      (0.0, 0.5, 0.0, 0.6),
#                            },
        "KikiSwitch":       {   "base":         (0.0, 0.6, 0.0, 0.8),
                                "sphere":       (1.0, 1.0, 1.0, 0.8),     
                            },
        "KikiBomb":         {   "base":         (0.0, 0.2, 0.0, 0.8),
                            },
        "KikiGate":         {   "base":         (0.0, 0.5, 0.0),
                                "sphere":       (1.0, 1.0, 1.0, 0.8),
                            },
        "KikiPlayer":       {   "base":         (0.0, 0.7, 0.0),
                                "tire":         (0.0, 0.3, 0.0),
                            },
        "KikiBotFume":      {   "base":         (0.5, 1.0, 0.5, 0.5),
                            },
        "KikiMutant":       {   "base":         (0.0, 0.3, 0.0),
                                "dead":         (0.0, 0.2, 0.0, 0.5),
                                "tire":         (0.0, 0.7, 0.0),
                            },
        "KikiText":         {   "base":         (0.0, 0.4, 0.0),
                                "bright":       (0.0, 0.6, 0.0),
                                "dark":         (0.0, 0.2, 0.0),
                            },
        "KikiGear":         {   "base":         (0.0, 0.2, 0.0, 0.9), 
                            },
        "KikiValve":        {   "base":         (0.0, 0.5, 0.0, 0.9), 
                            },
        "KikiMotorCylinder":{   "base":         (0.0, 0.6, 0.0, 0.9), 
                            },
        "KikiMotorGear":    {   "base":         (0.0, 0.6, 0.0, 0.9), 
                            },
        "KikiGenerator":    {   "base":         (0.0, 0.5, 0.0, 0.9), 
                            },
        "KikiWire":         {   "base":         (0.1, 0.9, 0.0, 0.6),
                                "light":        (1.0, 1.0, 1.0), 
                            },
    }


# ........................................................ metal color scheme
metal_scheme = {        
        "KikiWorld":        {   "base":        (0.2, 0.2, 0.2), 
                                "plate":               (1.0, 1.0, 1.0), 
                            },
        "KikiLight":        {   "base":         (0.0, 0.0, 0.0),
                                "diffuse":      (0.2, 0.2, 0.4),
                                "specular":     (0.0, 0.0, 1.0),
                                "halo":         (0.0, 0.0, 1.0),
                            },
        "KikiStone":        {   "base":         (1.0, 1.0, 1.0, 0.6),
                            },
        "KikiSpikes":       {   "base":         (1.0, 1.0, 1.0, 0.8),
                            },
#        "KikiHealthAtom":   {   "base":         (0.6, 0.6, 0.7, 0.8),
#                                "neutron":      (0.4, 0.4, 0.5, 0.8),
#                            },
        "KikiMovesAtom":   {   "base":         (0.3, 0.3, 0.35, 0.8),
                                "neutron":      (0.7, 0.7, 0.75, 0.8),
                            },
        "KikiSwitch":       {   "base":         (0.9, 1.0, 0.9, 0.8),
                                "sphere":       (0.5, 0.5, 1.0, 0.8),     
                            },
        "KikiGate":         {   "base":         (1.0, 1.0, 1.0, 0.8),
                                "sphere":       (0.5, 0.5, 1.0, 0.8),
                            },
        "KikiPlayer":       {   "base":         (0.6, 0.6, 0.6),
                                "tire":         (0.3, 0.3, 0.3),
                            },
        "KikiMutant":       {   "base":         (0.8, 0.8, 0.8),
                                "tire":         (0.7, 0.7, 0.7),
                                "dead":         (1.0, 1.0, 1.0, 0.3),
                            },
        "KikiBotFume":      {   "base":         (0.8, 0.8, 0.8, 0.5),
                            },
        "KikiBomb":         {   "base":         (0.4, 0.4, 0.5, 0.9), 
                            },
        "KikiGear":         {   "base":         (0.2, 0.4, 0.5, 1.0), 
                            },
        "KikiValve":        {   "base":         (0.4, 0.4, 0.5, 0.9), 
                            },
        "KikiMotorCylinder":{   "base":         (0.5, 0.5, 0.5, 0.9), 
                            },
        "KikiMotorGear":    {   "base":         (0.5, 0.5, 0.5, 0.9), 
                            },
        "KikiGenerator":    {   "base":         (1.0, 1.0, 1.0, 0.9), 
                            },
        "KikiWire":         {   "base":         (1.0, 1.0, 1.0, 0.9),
                                "light":        (0.0, 0.0, 1.0), 
                            },
        "KikiText":         {   "base":         (0.2, 0.4, 0.5),
                                "bright":       (0.3, 0.9, 1.0),
                                "dark":         (0.1, 0.3, 0.4),
                            },
    }

applyColorScheme (default_scheme)