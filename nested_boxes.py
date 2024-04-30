import pandas as pd

def surfaceArea(length, width, height):
    surface_areas_of_boxes = []
    for i in range(3):
        surface_area = 2 * width * height + 2 * height * length + length * width
        surface_areas_of_boxes.append(surface_area)
        length -= 2
        width -= 2
        height -= 2
    return pd.DataFrame(
        {"Box Number": [1, 2, 3], "Surface Area": surface_areas_of_boxes}
    ).set_index("Box Number")


length = float(input("Enter the longer side of outermost box: "))
width = float(input("Enter the shorter side of outermost box: "))
height = float(input("Enter the height of the box: "))

df = surfaceArea(length, width, height)
print(df)

print(f"The total surface area for resting 3 boxes is {df['Surface Area'].sum()}")
