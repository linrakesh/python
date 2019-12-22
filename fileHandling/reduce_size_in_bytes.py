import tinify

tinify.key = "B6xXQjG6JWYjPyBN7tyQ306mrvmRtzcx"

source = tinify.from_file("C:/Users/rakesh/Desktop/serpEmpire/1.png")

resized = source.resize(method='fit', width=900, height=450)

resized.to_file("C:/Users/rakesh/Desktop/serpEmpire/1_small_optimized.png")

print('finished')
