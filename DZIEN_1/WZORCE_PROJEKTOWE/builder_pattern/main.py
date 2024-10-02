from director import Director
from concretebuilder1 import ConreteBuilder1

director = Director()
builder = ConreteBuilder1()

director.builder = builder

print("\n produkt podstawowy:")
director.build_minimal_version()
builder.product.list_parts()


print("\npełna wersja:")
director.build_full_version()
builder.product.list_parts()

print("\nprodukt specjalny:")
builder.produce_part_a()
builder.produce_part_c()
builder.product.list_parts()
