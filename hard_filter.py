mesa = [37, 39, 167, 38, 166, 165]

def should_filter(biome_array):
    return all(mesa_id not in biome_array for mesa_id in mesa)