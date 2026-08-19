# Between Two Buckets

# Given two buckets of paint, each with an RGB color and a fullness level, return the mixed RGB color as an array of three integers.

# Each bucket is an object (JavaScript) or dictionary (Python) with a color property (an array of three integers [r, g, b]) and a fullness property (0–100).
# The mixed color is a weighted average of each channel in the two colors based on fullness level, with each channel rounded to the nearest integer.
# 


def mix_paint(bucket1, bucket2):
    
    #
    # Testing
    #
    # storage1 = {
        
    #         "color":{
    #             'r' : 250,
    #             'g' : 250,
    #             'b' : 250
    #             },
    #         "fullness": 80
        
    # }
    # storage2 = {
        
    #         "color":{
    #             'r' : 10,
    #             'g' : 10,
    #             'b' : 10
    #             },
    #         "fullness": 20
        
    # }

    bucket1['color'][0] = round(
        (
            (bucket1['color'][0] * (bucket1['fullness']))
            +
            (bucket2['color'][0] * (bucket2['fullness']))
        )
        / 
        (bucket1['fullness'] + bucket2['fullness'])
    )

    bucket1['color'][1] = round(
        (
            (bucket1['color'][1] * (bucket1['fullness']))
            +
            (bucket2['color'][1] * (bucket2['fullness']))
        )
        /
        (bucket1['fullness'] + bucket2['fullness'])
    )

    bucket1['color'][2] = round(
        (
            (bucket1['color'][2] * (bucket1['fullness']))
            +
            (bucket2['color'][2] * (bucket2['fullness']))
        )
        /
        (bucket1['fullness'] + bucket2['fullness'])
    )
       
    return bucket1['color']

mix_paint({"color": [250, 250, 250], "fullness": 50}, {"color": [0, 0, 0], "fullness": 50})
mix_paint({"color": [250, 250, 250], "fullness": 80}, {"color": [0, 0, 0], "fullness": 20})
mix_paint({"color": [100, 150, 200], "fullness": 30}, {"color": [100, 150, 200], "fullness": 70})
mix_paint({"color": [143, 143, 101], "fullness": 45}, {"color": [100, 204, 204], "fullness": 90})
mix_paint({"color": [15, 134, 249], "fullness": 29}, {"color": [97, 178, 55], "fullness": 54})

