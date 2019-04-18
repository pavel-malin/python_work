# 
def make_shirt(size, size_text):
    print("\nT-shirt size: " + size)
    print("Size of printed text: " + size_text + ".")

make_shirt('XLL', '15x15')

def make1_shirt(size_text, size='XLL'):
    print("\nT-shirt size: " + size)
    print("Size of printed text: " + size_text + ".")

make1_shirt('15x15')
make1_shirt(size='XXL', size_text='22x22')

def make2_shirt(size_text='25x25', size='XXX'):
    print("\nT-shirt size: " + size)
    print("Size of printed text: " + size_text + ".")

make2_shirt()

def make3_shirt(size='L', text='I love Python'):
    print("\nT-shirt size: " + size)
    print("Print text t-shirt: " + text + ".")

make3_shirt()

def make4_shirt(size='L', size_text='22x22', text='I love Python'):
    print("\nT-shirt size: " + size)
    print("Size of printed size: " + size_text + "\tPrint text: " +
        text + ".")
    
make4_shirt()
