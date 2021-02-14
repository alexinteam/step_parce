from steputils import p21
from steputils.p21 import ParseError, Reference, SimpleEntityInstance


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fileName = '1.stp'
    try:
        stepfile = p21.readfile(fileName)
    except IOError as e:
        print(str(e))
    except ParseError as e:
        # Invalid STEP-file
        print(str(e))
    else:
        data = stepfile.data
        if len(data):
            for instance in data[0].instances.items():
                if isinstance(instance[1], SimpleEntityInstance):
                    if instance[1].entity.name == 'CONICAL_SURFACE':
                        conical = instance[1].entity
                        print("радиус: ", conical.params[2])

                        placement = data[0].get(conical.params[1])
                        point = data[0].get(placement.entity.params[1])

                        print("центр: ", point.entity.params[1])
        con = Reference('#10')
