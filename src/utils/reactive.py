from rx import operators as ops, create, scheduler, of


source = of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")

# source.pipe(
#     ops.map(lambda s: len(s)),
#     ops.filter(lambda i: i >= 5)
# ).subscribe(lambda value: print("Received {0}".format(value)))


source.subscribe(
    on_next=lambda i: print("Received {0}".format(i)),
    on_error=lambda e: print("Error Occurred: {0}".format(e)),
    on_completed=lambda: print("Done!"),
)
