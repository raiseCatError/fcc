# Between Two Buckets

# Given two buckets of paint, each with an RGB color and a fullness level, return the mixed RGB color as an array of three integers.

# Each bucket is an object (JavaScript) or dictionary (Python) with a color property (an array of three integers [r, g, b]) and a fullness property (0–100).
# The mixed color is a weighted average of each channel in the two colors based on fullness level, with each channel rounded to the nearest integer.
# 


def mix_paint(bucket1, bucket2):
    
    total = bucket1["fullness"] + bucket2["fullness"]

    for i in range(3):
        bucket1["color"][i] = round(
            (
                bucket1["color"][i] * bucket1["fullness"]
                +
                bucket2["color"][i] * bucket2["fullness"]
            )
            / total
        )

    return bucket1["color"]

mix_paint({"color": [250, 250, 250], "fullness": 50}, {"color": [0, 0, 0], "fullness": 50})
mix_paint({"color": [250, 250, 250], "fullness": 80}, {"color": [0, 0, 0], "fullness": 20})
mix_paint({"color": [100, 150, 200], "fullness": 30}, {"color": [100, 150, 200], "fullness": 70})
mix_paint({"color": [143, 143, 101], "fullness": 45}, {"color": [100, 204, 204], "fullness": 90})
mix_paint({"color": [15, 134, 249], "fullness": 29}, {"color": [97, 178, 55], "fullness": 54})

